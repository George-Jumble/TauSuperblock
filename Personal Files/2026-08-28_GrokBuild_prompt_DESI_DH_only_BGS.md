# Grok Build prompt — fix TAV ENGINE DESI `DH_only` × BGS failure

**Session:** 2026-08-28  
**Failure:** `DESI load failed: No data available for mode='DH_only' on tracer='BGS_BRIGHT-21.35_GCcomb'`  
**Root cause:** global/default mode `DH_only` applied to a tracer that only publishes isotropic `DV_over_rs`.

Copy everything inside the fence below into Grok Build (attach the research_tool / TAV ENGINE workspace).

---

## PROMPT FOR GROK BUILD (copy from here)

```
Fix the TAV ENGINE / TAU_SB_DESI Full Production Pipeline DESI loader so it no longer dies on BGS.

## Exact failure

Command: research
Log:

[TAV ENGINE] Dataset pipeline — pull→cache for TAU_SB_DESI / Full Production Pipeline
[DESI FETCH] Using cached DR2 tables: .../datasets/desi/bao_data/desi_bao_dr2
[TAV ENGINE] n=200 → n_freq=200, n_injection_trials=200, max_sne=200 (DESI BAO vector length unchanged)
[TAV ENGINE] DESI load failed: No data available for mode='DH_only' on tracer='BGS_BRIGHT-21.35_GCcomb'
[TAV ENGINE] Available tracers: ALL_GCcomb, BGS_BRIGHT-21.35_GCcomb, ELG_LOPnotqso_GCcomb_z1.1-1.6, LRG+ELG_LOPnotqso_GCcomb, LRG_GCcomb_z0.4-0.6, LRG_GCcomb_z0.6-0.8, Lya_GCcomb, QSO_GCcomb

Cache is fine. Tracer exists. Requested quantity does not.

## Data facts (do not “fix” by refetching)

Cobaya DESI DR2 mean files (same schema as the cached tree):

BGS_BRIGHT-21.35_GCcomb  (z_eff = 0.295)
  0.29500000 7.94167639 DV_over_rs
  cov = scalar 5.78998687e-03
  NO DH_over_rs, NO DM_over_rs

QSO_GCcomb (z_eff = 1.484): DM_over_rs AND DH_over_rs
LRG_GCcomb_z0.4-0.6: DM + DH
LRG_GCcomb_z0.6-0.8: DM + DH
LRG+ELG_LOPnotqso_GCcomb: DM + DH
ELG_LOPnotqso_GCcomb_z1.1-1.6: DM + DH
Lya_GCcomb (z_eff = 2.33): DH_over_rs AND DM_over_rs
ALL_GCcomb: mixed vector

DESI Collaboration reports BGS as isotropic D_V / r_d only because quadrupole S/N is too low for a stable AP / (D_M, D_H) split.

## Variable / quantity key

z              redshift of the bin
r_d            sound horizon at drag epoch
D_H(z) = c/H(z)     Hubble distance          file tag: DH_over_rs
D_M(z) = (1+z) D_A  transverse comoving     file tag: DM_over_rs
D_V(z) = (z * D_M(z)^2 * D_H(z))^(1/3)      file tag: DV_over_rs
F_AP(z) = D_M / D_H                         Alcock-Paczynski

Engine modes that must be supported:
  DH_only        require DH_over_rs
  DM_only        require DM_over_rs
  DV_only        require DV_over_rs
  anisotropic    require both DM_over_rs and DH_over_rs (+ cov)
  mixed / auto   use whatever the mean file actually contains

## What is broken

Somewhere in the DESI load path (search for these strings):
  mode='DH_only'
  "No data available for mode"
  BGS_BRIGHT-21.35
  DH_only
  load_desi
  bao_data/desi_bao_dr2
  tau_sb_desi
  Full Production Pipeline

a default or pipeline-wide mode='DH_only' is applied to every tracer, including BGS. The loader then hard-fails instead of selecting the available quantity.

## Required fix (do all of this)

1. Inventory quantities from the mean file, do not assume DH exists.
   Parse the third column (`quantity`) of each
   desi_gaussian_bao_<TRACER>_mean.txt
   and keep the matching cov file.

2. Resolve mode per tracer:
   requested_mode → if that quantity exists, use it
   else fall back in this order and LOG A WARNING:
     DH_only missing  → anisotropic if both DM+DH exist
     anisotropic missing → DV_only if DV exists
     DV_only missing  → skip that tracer with a clear warning, do not abort the whole pipeline unless the user asked for that tracer only

   Hard defaults if no explicit per-tracer mode is set:

   TRACER_DEFAULT_MODE = {
       "BGS_BRIGHT-21.35_GCcomb": "DV_only",
       "QSO_GCcomb": "anisotropic",
       "Lya_GCcomb": "anisotropic",
       "LRG_GCcomb_z0.4-0.6": "anisotropic",
       "LRG_GCcomb_z0.6-0.8": "anisotropic",
       "LRG+ELG_LOPnotqso_GCcomb": "anisotropic",
       "ELG_LOPnotqso_GCcomb_z1.1-1.6": "anisotropic",
       "ALL_GCcomb": "mixed",
   }

3. Do not abort the Full Production Pipeline because one tracer lacks DH.
   BGS must load as a 1-vector DV_over_rs.
   Other tracers keep their (DM, DH) pairs.
   Combined vector length will therefore be heterogeneous — stop assuming every tracer contributes one DH sample. Update any code that sets
     n=200, n_freq=200, DESI BAO vector length
   so length is computed from the actual stacked quantities, not a hardcoded DH-only count.

4. Theory side for BGS:
   When comparing a model to BGS, evaluate
     D_V_th(z) / r_d = (z * D_M_th(z)**2 * D_H_th(z))**(1/3) / r_d
   at z = 0.295
   against 7.94167639 ± sqrt(5.78998687e-03).
   Do not invent a D_H data point for BGS.

5. Logging:
   Replace the fatal
     DESI load failed: No data available for mode='DH_only' on tracer='BGS_BRIGHT-21.35_GCcomb'
   with:
     [DESI LOAD] tracer=BGS_BRIGHT-21.35_GCcomb requested=DH_only available=['DV_over_rs'] → using DV_only (isotropic)
   Keep a hard error only if the tracer has zero usable quantities.

6. Tests / smoke check after the edit:
   - Load BGS with requested mode DH_only → succeeds, returns DV_over_rs, warning logged.
   - Load LRG_GCcomb_z0.4-0.6 with DH_only → DH_over_rs (or anisotropic pair if that is how DH_only is implemented).
   - Load QSO, Lya, ELG2, LRG+ELG → anisotropic.
   - Full Production Pipeline `research` / TAU_SB_DESI continues past DESI load.
   - Do not change cached file paths or re-download unless files are actually missing.

7. Scope:
   Touch only DESI BAO load / mode resolution / vector stacking.
   Do not refactor unrelated GUI, Docker, or other survey pipelines.
   Add a short comment at the fallback citing DESI DR2 BGS = isotropic D_V only.

Search the workspace for the raise/log that contains "No data available for mode" and fix that function first, then every caller that hardcodes mode="DH_only" for all tracers.
```

---

## How to use

1. Open Grok Build on the `research_tool` / TAV ENGINE tree (`~/Research/scripts/research_tool` or the repo you sync).
2. Paste the fenced prompt above.
3. After it edits, re-run `research` and confirm the BGS line is a warning + `DV_only`, not a hard fail.
4. If Grok Build cannot find the raise string, point it at the module that printed `[TAV ENGINE] DESI load failed`.
