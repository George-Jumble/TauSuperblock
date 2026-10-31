# TAV ENGINE session — DESI DR2 load failure (DH_only × BGS)

**Date:** 2026-08-28 00:57–04:40 EDT  
**Host context:** `(.venv)(wyle-e@monster) ~/Research`  
**Command:** `research`  
**Pipeline:** TAU_SB_DESI / Full Production Pipeline  

## Raw stdout (as captured)

```
[TAV ENGINE] Dataset pipeline — pull→cache for TAU_SB_DESI / Full Production Pipeline
[DESI FETCH] Using cached DR2 tables: /home/wyle-e/Storage7TB/Research/scripts/research_tool/datasets/desi/bao_data/desi_bao_dr2
[TAV ENGINE] n=200 → n_freq=200, n_injection_trials=200, max_sne=200 (DESI BAO vector length unchanged)
[TAV ENGINE] DESI load failed: No data available for mode='DH_only' on tracer='BGS_BRIGHT-21.35_GCcomb'
[TAV ENGINE] Available tracers: ALL_GCcomb, BGS_BRIGHT-21.35_GCcomb, ELG_LOPnotqso_GCcomb_z1.1-1.6, LRG+ELG_LOPnotqso_GCcomb, LRG_GCcomb_z0.4-0.6, LRG_GCcomb_z0.6-0.8, Lya_GCcomb, QSO_GCcomb
[TAV ENGINE] Test output saved: /home/wyle-e/Storage7TB/Research/scripts/research_tool/artifacts/run_logs/28-08-2026_00-57_run_log/run_logs__run_log__tau_sb_desi_full_production_pipeline_stdout__08-28-2026_005700.out
```

## Diagnosis

This is **not a missing cache file**. The tracer exists. The requested *quantity* does not.

DESI DR2 BAO for BGS is published as a **1-D isotropic** measurement only:

| Quantity | Symbol | Present for BGS DR2? |
|---|---|---|
| Spherically averaged distance / sound horizon | \(D_V/r_d\) (`DV_over_rs`) | Yes |
| Hubble distance / sound horizon | \(D_H/r_d\) (`DH_over_rs`) | **No** |
| Transverse comoving distance / sound horizon | \(D_M/r_d\) (`DM_over_rs`) | **No** |

Official Cobaya/bao_data file (`desi_gaussian_bao_BGS_BRIGHT-21.35_GCcomb_mean.txt`):

```
# [z] [value at z] [quantity]
0.29500000 7.94167639 DV_over_rs
```

Covariance is a single scalar \(\sigma^2 \approx 5.79\times 10^{-3}\).

Reason given in DESI DR2 Results II and the DR1 predecessor papers: BGS quadrupole S/N is too low for a stable \(\alpha_\mathrm{AP}\) / \((D_M, D_H)\) split, so the collaboration reports only the monopole / isotropic \(D_V\).

QSO in the *same* DR2 Cobaya tables **does** have \(D_M\) and \(D_H\). LRG, ELG, Lya also have both.

## Variable key (BAO distance definitions)

- \(z\): redshift of the tracer bin (BGS \(z_\mathrm{eff}=0.295\)).
- \(r_d\): comoving sound horizon at the drag epoch.
- \(D_H(z) = c/H(z)\): Hubble distance.
- \(D_M(z)\): transverse comoving distance (\(= (1+z)D_A\)).
- \(D_V(z) = \bigl(z\, D_M(z)^2 D_H(z)\bigr)^{1/3}\): spherically averaged BAO distance.
- \(F_\mathrm{AP}(z) = D_M(z)/D_H(z)\): Alcock–Paczynski parameter.
- Mode names used by TAV ENGINE:
  - `DH_only` → look for `DH_over_rs` (or `Hz_rs` inverse).
  - `DM_only` → `DM_over_rs`.
  - `DV_only` / isotropic → `DV_over_rs`.
  - anisotropic pair → both `DM_over_rs` and `DH_over_rs` plus covariance.

## Per-tracer quantity map (Cobaya DESI DR2 tables)

| Tracer string | \(z_\mathrm{eff}\) | Quantities in mean file |
|---|---|---|
| `BGS_BRIGHT-21.35_GCcomb` | 0.295 | `DV_over_rs` only |
| `LRG_GCcomb_z0.4-0.6` | 0.510 | `DM_over_rs`, `DH_over_rs` |
| `LRG_GCcomb_z0.6-0.8` | 0.706 | `DM_over_rs`, `DH_over_rs` |
| `LRG+ELG_LOPnotqso_GCcomb` | ~0.93 | `DM_over_rs`, `DH_over_rs` |
| `ELG_LOPnotqso_GCcomb_z1.1-1.6` | 1.321 | `DM_over_rs`, `DH_over_rs` |
| `QSO_GCcomb` | 1.484 | `DM_over_rs`, `DH_over_rs` |
| `Lya_GCcomb` | 2.33 | `DH_over_rs`, `DM_over_rs` |
| `ALL_GCcomb` | combined vector | mixed |

## Recommended loader patch

Do **not** apply a global `mode='DH_only'` to every tracer.

1. Infer available quantities from the mean file header/column `quantity`.
2. Fall back:
   - If `DH_only` requested and only `DV_over_rs` present → use `DV_only` and log a warning.
   - If anisotropic requested and only DV present → skip or convert theory \(D_V\) from model \(D_M,D_H\).
3. Hard-coded safe map:

```python
TRACER_DEFAULT_MODE = {
    "BGS_BRIGHT-21.35_GCcomb": "DV_only",
    "QSO_GCcomb": "anisotropic",   # DR2 tables now have DM+DH
    "Lya_GCcomb": "anisotropic",
    "LRG_GCcomb_z0.4-0.6": "anisotropic",
    "LRG_GCcomb_z0.6-0.8": "anisotropic",
    "LRG+ELG_LOPnotqso_GCcomb": "anisotropic",
    "ELG_LOPnotqso_GCcomb_z1.1-1.6": "anisotropic",
    "ALL_GCcomb": "mixed",
}
```

Theory-side, when comparing TSB to BGS, evaluate

\[
\frac{D_V^\mathrm{th}(z)}{r_d} = \frac{\bigl(z\, D_M^\mathrm{th}(z)^2 D_H^\mathrm{th}(z)\bigr)^{1/3}}{r_d}
\]

against \(7.94167639 \pm \sqrt{5.78998687\times10^{-3}}\).

## Immediate workarounds (no code change)

- Exclude BGS from any `DH_only` / `DM_only` sweep.
- Run BGS as its own isotropic vector.
- Use `ALL_GCcomb` only if the loader already understands mixed quantities.
- Confirm cached files match Cobaya `bao_data/desi_bao_dr2` (they do, given the tracer list).

## Implications for Tau-Superblock / TAV ENGINE

- Low-\(z\) Hubble-distance leverage from DESI is **not** available from BGS; that leverage starts at LRG1 (\(z=0.51\)).
- BGS still constrains the isotropic combination and is useful for \(H_0 r_d\) / early-vs-late consistency, but cannot isolate line-of-sight \(H(z)\) at \(z\sim0.3\).
- Injection / frequency scans that assume a uniform DH vector length across tracers will under-count BGS or crash exactly as seen (`DESI BAO vector length unchanged` then fail).

## Sources

- CobayaSampler/bao_data `desi_bao_dr2` mean/cov files.
- DESI Collaboration, DR2 Results II (arXiv:2503.14738) and DR1 BAO cosmology papers: BGS and (historically) QSO reported as \(D_V/r_d\) when quadrupole S/N is insufficient.
- Cobaya docs: `bao.desi_dr2.desi_bao_bgs` wraps the isotropic BGS likelihood.
