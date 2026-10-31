# Session 2026-10-13: Suggested Changes for the Research Tool Project

**Date**: 2026-10-13  
**User question**: So, what suggestions do you have for any changes which may be needed for the research tool project?  
**Context**: Hard rule in force — interpret under Superblock Cosmology as the live 3+1D / 4D framework.  
**Repository examined**: George-Jumble/TauSuperblock (main, last substantial update ~2026-10-03). Entry point `research_tool.py`, engines in `sb_engine/`.  

## Summary of Current State (as of inspection)
- Description and README correctly state “Tau layer out”.
- Live constants still use `DELTA_TEP_MEV = 313.1` and `N_HIER = 45.8`.
- Empirical modules (`cms.py`, `casimir.py`, `sparc.py`) generate or inject the signal they then recover.
- `desi.py` residual is identically zero when `gamma = DELTA_N_PLASMA` (by construction); calibration uses `N_HIER`.
- Neutron module is correctly marked HOLD and notes the J-PARC 877.2 s failure of the s=0 appearance prediction.
- Geometry and bounce modules are largely free of Tau but still reference the 313.1 MeV floor.

## Suggested Changes (priority order)

### 1. Align the mass-floor protocol (high)
Live printed working floor is **309.3 MeV** (neutron dressing share; insertion/protocol, not a clock derivation). The 313.1 MeV figure is the older rounded \(M_n/3\).

- In `sb_engine/constants.py`:
  - Set `DELTA_TEP_MEV = 309.3` (or keep both with explicit labels: `PRINTED_WORKING_MEV = 309.3`, `OLD_PRINT_MEV = 313.1`).
  - Recalculate `R_M_LOCKED_FM = HBAR_C_MEV_FM / DELTA_TEP_MEV`.
- Update `README.md`, `CORPUS.md`, and any geometry snapshot that prints \(r_M \approx 0.630\) fm.
- Document clearly that the number remains a protocol insertion.

**Complete key**
- \(\Delta\): mass-floor energy scale (MeV).
- \(r_M = \hbar c / \Delta\): Compton length dual to the floor.
- \(\hbar c\): conversion constant \(\approx 197.327\) MeV·fm.

### 2. Quarantine or remove \(n_{\rm hier}\) (high)
Live frame rejects the Tau metric package, including \(n_{\rm hier} = \log_7(\tau / \lambda_{313})\). The constant `N_HIER = 45.8` remains and is used in DESI calibration.

- Remove `N_HIER` from `constants.py` or move it to a clearly retired section.
- In `desi.py`: stop using it inside `calibrate_gamma`. Default `gamma` to `DELTA_N_PLASMA` and document that the residual vanishes by construction.
- Remove or reclassify any `log7(r_M / \ell_P)` hierarchical count that is presented as live.

### 3. Label or replace planted empirical modules (high)
Current implementations recover a signal they themselves inject:

- `cms.py`: draws counts from weights \(1 + {\rm amp}\cos(2\pi k/7)\).  
- `casimir.py`: multiplies the Lifshitz curve by a hand-added \(\sin(2\pi\log_7(d/r_M))\) ripple.  
- `sparc.py`: generates synthetic NGC 3198 velocities and fits them with an `emergent_dm` function containing free phase/beta parameters.

**Options** (choose one per module):
- Add an explicit `--synthetic` / `--illustration` flag and a printed warning that the module is not a real-data confrontation.
- Replace with real open-data loaders:
  - CMS: periodogram on Open Data with a trigger-aware null (prior ATLAS/CMS exploratory notes already emphasized this).
  - Casimir: load dielectric-response files (e.g. dielPT* series) and test for 1/7 content without injecting the modulation.
  - SPARC: load published rotation-curve tables rather than synthesizing \(v_{\rm obs}\).

Until replaced, do not present the returned \(\chi^2\) or “detection” language as empirical support.

### 4. Corpus and documentation hygiene (medium)
Update `CORPUS.md` IN section and `README.md`:
- Floor = 309.3 MeV protocol (neutron dressing).
- Remove or reclassify \(n_{\rm hier}\).
- Emphasize residual-\(L\) gravity matching laboratory \(G\), six co-located copies, one Mirron, floor-only Dynamic Refresh, 4D arena only.
- Note the current status of the empirical CLIs (synthetic vs real-data).

### 5. Neutron module (low — already correct)
Keep the HOLD status and the explicit statement that J-PARC 877.2 s fails the s=0 appearance prediction. No change required beyond ensuring it remains consistent with the updated floor (it does not fit the floor).

### 6. Optional consistency checks (low)
- Add a small unit test or geometry snapshot that records the residual-\(L\) matching statement for laboratory \(G\).
- Ensure bounce and geometry output contain no residual fifth-coordinate language.

## What should stay
- Tau layer remains out.
- Mirron terminology.
- Six-domain \(V_{\rm orb}\) table.
- Neutron HOLD with the J-PARC note.
- Bounce canon statement (CCC + Mirron refresh, not \(\Phi_7\) pin-drop).

## Status
These changes bring the research tool into alignment with the live 4D locks (as of 2026-10-10/13) and with the hard rule that prompts under Superblock Cosmology are interpreted as 3+1D. The empirical modules currently function as synthetic illustrations; that fact should be made explicit until real-data pipelines replace them.

**File path**: Tau-Superblock-Universe/Personal Files/Session_2026-10-13_Suggested_Changes_for_Research_Tool_Project.md
