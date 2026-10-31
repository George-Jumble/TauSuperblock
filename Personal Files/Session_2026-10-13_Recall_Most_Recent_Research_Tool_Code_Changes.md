# Session 2026-10-13: Recall of Research Tool Code Changes for Local Grok Build

**Date**: 2026-10-13  
**Request**: Recall the session with the most recent code changes for the research tool through local Grok build.  
**Frame**: Live 3+1D Superblock Cosmology. Hard rule in force.  

## Identified Session

The most recent session providing code changes for the research tool (George-Jumble/TauSuperblock) intended for the local Grok build client is:

**Session_2026-10-13_Code_for_Local_Grok_Build_Client_Research_Tool_Updates.md**

Supporting sessions from the same day:

- Session_2026-10-13_Suggested_Changes_for_Research_Tool_Project.md  
- Session_2026-10-13_Explanation_of_309.3_MeV_Floor_and_n_hier_Removal.md  

All located under Personal Files in the Tau-Superblock Universe project.

## Summary of Changes

High-priority updates to align with live 4D locks:

1. Printed working mass floor changed from 313.1 MeV to **309.3 MeV** (neutron dressing protocol). Recalculate \( r_M \).
2. Remove \( N_{\rm hier} = 45.8 \) from live constants and DESI calibration.
3. Add explicit SYNTHETIC / illustration warnings to cms.py, casimir.py, and sparc.py.
4. Update README.md and CORPUS.md.

### Key Equations (with complete keys)

#### Mass floor (protocol)

\[
\Delta = 309.3\,\mathrm{MeV}
\]

Neutron dressing share:

\[
E_{\mathrm{dress}}^{(n)} = M_n - m_u^{\mathrm{cur}} - 2 m_d^{\mathrm{cur}} \approx 928.01\,\mathrm{MeV},
\qquad
\frac{E_{\mathrm{dress}}^{(n)}}{3} \approx 309.34\,\mathrm{MeV}
\]

(rounded to printed 309.3 MeV).

**Complete key**
- \(\Delta\): printed working mass-floor energy scale (MeV). Protocol insertion, not a derivation.
- \(M_n\): neutron mass (PDG).
- \(m_u^{\mathrm{cur}}\), \(m_d^{\mathrm{cur}}\): current (PDG) up and down quark masses.
- \(E_{\mathrm{dress}}^{(n)}\): dressing energy of the neutron (total mass minus current-quark masses).
- Factor \(1/3\): equal share among the three valence lines (bookkeeping).

Compton length:

\[
r_M = \frac{\hbar c}{\Delta}
\]

**Complete key**
- \(r_M\): Compton length dual to the floor (fm or m).
- \(\hbar c \approx 197.327\,\mathrm{MeV\cdot fm}\): conversion constant.
- \(\Delta\): as above.

Old print was 313.1 MeV (rounded \(M_n/3\)). Lengths scale by \(\approx +1.23\times 10^{-2}\). Invariant \(S_E/\hbar = 2\) unchanged.

**Key**
- \(S_E/\hbar = 2\): Euclidean action per diameter tick.

#### Retired hierarchical count

\[
n_{\mathrm{hier}} = \log_7\left(\frac{\tau}{\lambda_{313.1}}\right) \approx 45.8
\]

**Complete key**
- \(n_{\mathrm{hier}}\): hierarchical generation count from the retired Tau-cylinder package.
- \(\tau \approx 7\,h^{-1}\,\mathrm{Mpc}\): retired metric fifth-scale radius.
- \(\lambda_{313.1} = \hbar c / 313.1\,\mathrm{MeV}\): old Compton length.
- \(\log_7\): base-7 logarithm.

Removed because the Tau metric package (compact \(S^1_\tau\), KK, \(\rho_\Lambda = \hbar c/\tau^4\)) is hard-rejected. Live arena is 4D.

#### DESI residual (by construction)

\[
r_d = \frac{\Delta N_{\rm plasma} \cdot r_{d,\mathrm{obs}}}{\gamma}
\]

Residual identically zero when \(\gamma = \Delta N_{\rm plasma}\).

**Complete key**
- \(r_d\): predicted sound horizon (Mpc).
- \(\Delta N_{\rm plasma}\): plasma contribution parameter (input, 10.74).
- \(r_{d,\mathrm{obs}}\): observed sound horizon (147.09 Mpc).
- \(\gamma\): calibration factor (defaults to \(\Delta N_{\rm plasma}\)).

## Ready-to-Paste Code Highlights

(Full contents are in the original session file.)

**constants.py** (excerpt):
```python
DELTA_TEP_MEV = 309.3
R_M_LOCKED_FM = HBAR_C_MEV_FM / DELTA_TEP_MEV
# N_HIER retired with the Tau metric package.
```

**desi.py**: no n_hier; residual zero by construction when gamma equals DELTA_N_PLASMA.

**cms.py / casimir.py / sparc.py**: status "SYNTHETIC" with explicit warnings that they plant the signal they recover.

## Status

- Tau package remains hard-rejected.
- Floor digits = 309.3 MeV protocol.
- Empirical modules labeled synthetic until replaced with real open-data loaders.
- Live frame: 4D, six co-located copies, one Mirron, residual-L gravity matching laboratory G, floor-only Dynamic Refresh.

**Original files**:
- /workspace/artifacts/Personal Files/Session_2026-10-13_Code_for_Local_Grok_Build_Client_Research_Tool_Updates.md
- /workspace/artifacts/Personal Files/Session_2026-10-13_Suggested_Changes_for_Research_Tool_Project.md
- /workspace/artifacts/Personal Files/Session_2026-10-13_Explanation_of_309.3_MeV_Floor_and_n_hier_Removal.md

This recall file provides a self-contained pointer and key equations.
