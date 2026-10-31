# Session 2026-10-13: Explanation of the 309.3 MeV Floor and n_hier Removal

**Date**: 2026-10-13  
**User request**: Explain the 309.3 MeV floor and n_hier removal.  
**Frame**: Live 3+1D Superblock Cosmology. Hard rule in force.  

## 1. The 309.3 MeV floor

### What it is
The printed working mass floor is  
\[
\Delta = 309.3\,\mathrm{MeV}.
\]
It is the equal dressing share of the neutron:

\[
E_{\mathrm{dress}}^{(n)} = M_n - m_u^{\mathrm{cur}} - 2m_d^{\mathrm{cur}} \approx 928.01\,\mathrm{MeV},
\qquad
\frac{E_{\mathrm{dress}}^{(n)}}{3} \approx 309.34\,\mathrm{MeV}.
\]

**Complete key**
- \(\Delta\): printed working mass-floor energy scale.
- \(M_n\): neutron mass.
- \(m_u^{\mathrm{cur}}\), \(m_d^{\mathrm{cur}}\): current (PDG) up and down quark masses.
- \(E_{\mathrm{dress}}^{(n)}\): dressing energy of the neutron (total mass minus current-quark masses).
- The factor \(1/3\): equal share among the three valence lines (bookkeeping protocol).

Rounded for print to 309.3 MeV. Proton dressing share is \(\approx 309.75\) MeV and is not the printed value.

### What it is not
- Not a derivation from the clock, from TEP, or from any geometric uniqueness theorem.
- TEP supplies only the inequality \(\Delta > 0\) (positive energy cost to force a bound colour line through local reset overlap). The numerical digits are an inserted protocol.
- Not the old print 313.1 MeV (which was rounded \(M_n/3\)).
- Not a glueball pole, not a Vălean residue, not the current up-quark mass, and not a constituent-quark mass from magnetic moments.

### Why the change from 313.1 MeV
313.1 MeV was the earlier printed insertion (\(M_n/3\) rounded). The neutron-dressing protocol is the preferred bookkeeping of the same nucleon data: it subtracts the small current-quark masses first, then shares the remainder equally. Lengths that depend on \(\Delta\) shift by \(\approx +1.23\times 10^{-2}\) when the floor is updated from 313.1 to 309.3. The invariant \(S_E/\hbar = 2\) is unchanged.

**Key**
- \(S_E/\hbar = 2\): Euclidean action per diameter tick (invariant under the floor-digit change).

## 2. Removal of \(n_{\rm hier}\)

### What \(n_{\rm hier}\) was
In the retired Tau-cylinder package,
\[
n_{\mathrm{hier}} = \log_7\left(\frac{\tau}{\lambda_{313.1}}\right) \approx 45.8,
\]
where \(\tau \approx 7\,h^{-1}\,\mathrm{Mpc}\) was a compact fifth-dimensional circle and \(\lambda_{313.1}\) was the Compton length of the old floor.

**Complete key**
- \(n_{\mathrm{hier}}\): hierarchical generation count in the Tau-cylinder framework.
- \(\tau\): retired metric fifth-scale radius.
- \(\lambda_{313.1} = \hbar c / 313.1\,\mathrm{MeV}\): old Compton length.
- \(\log_7\): logarithm base 7 (from the order-6 cycle / phase count).

### Why it is removed
The entire Tau metric package is hard-rejected in the live frame:
- no compact \(S^1_\tau\),
- no Kaluza–Klein tower,
- no \(\rho_\Lambda = \hbar c / \tau^4\),
- no \(n_{\rm hier}\) as a load-bearing stretch of binding generations.

The live arena is 4D (3+1). Hierarchical globbing exists as successive containment of coherent bound sets \(\mathcal{B}^{(g)}\) inside one another, but the generation index \(g\) is not identified with the old numerical value 45.8, and no fifth coordinate is required.

In the research tool, `N_HIER = 45.8` remained in `constants.py` and was used by the DESI calibration. Removing it prevents the retired package from re-entering live calculations. DESI residual is identically zero when \(\gamma = \Delta N_{\rm plasma}\) by construction; that fact does not depend on \(n_{\rm hier}\).

## 3. Joint status
- Floor digits = 309.3 MeV protocol (neutron dressing). Insertion, not derivation.
- \(n_{\rm hier}\) and the Tau metric package = hard-rejected.
- Live frame remains 4D: six co-located copies, one Mirron, residual-\(L\) gravity matching laboratory \(G\), floor-only Dynamic Refresh.

**File path**: Tau-Superblock-Universe/Personal Files/Session_2026-10-13_Explanation_of_309.3_MeV_Floor_and_n_hier_Removal.md
