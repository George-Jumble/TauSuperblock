# Session 2026-10-24: Orbitals from Lorentz Differentials in Quark Masses

**Date**: 2026-10-24  
**Framework**: Tau-Superblock (TSB / Superblock) — live 4D frame, residual-L gravity, six co-located domains, mass floor as protocol insertion (printed 309.3 MeV neutron dressing share).  
**Context**: Phenomenological stand-in treating successive quark mass increments (relative to the up quark) as Lorentz factors of hierarchical orbitals. Follows earlier V_orb notes (2026-09-18). Not a derivation of residual-L, not an E8 projection, not a clock derivation of the floor.  
**Status**: Explicit calculation of β and γ from PDG current masses. Intra-domain hierarchical velocities only.

## Plain-language summary

The current (running) quark masses increase dramatically from the up quark upward. If one treats the excess mass of each heavier flavour as pure kinetic energy of an orbital relative to an up-quark “rest” mass, the Lorentz factor is simply the mass ratio γ = m_q / m_u and the orbital speed parameter is β = √(1 − 1/γ²).  

Using PDG 2026 values this yields a sequence of orbital velocities that starts at rest for the up quark, rises to β ≈ 0.888 for the down quark, and rapidly approaches the speed of light for the strange, charm, bottom and top. These are phenomenological labels for hierarchical orbitals inside a domain; they do not fix the free inter-domain orbital of the six co-located copies, nor do they derive the mass floor or residual-L matching to laboratory G.

## Analytical calculation

**Key to symbols**  
- m_q: current (MS-bar or pole) mass of flavour q.  
- m_u: current up-quark mass (reference “Prime at rest”).  
- γ = m_q / m_u: Lorentz factor of the orbital.  
- β = √(1 − 1/γ²): orbital velocity parameter (v/c).  
- 1 − β: departure from the light-like limit.  
- PDG 2026 values used (approximate central values):  
  m_u = 2.16 MeV,  
  m_d = 4.70 MeV,  
  m_s = 92.9 MeV,  
  m_c = 1.273 GeV = 1273 MeV,  
  m_b = 4.186 GeV = 4186 MeV,  
  m_t = 172.6 GeV = 172600 MeV.

For each flavour the orbital parameters are  

\[
\gamma_q = \frac{m_q}{m_u}, \qquad \beta_q = \sqrt{1 - \frac{1}{\gamma_q^2}}.
\]

**Numerical results**  

| Flavour | m (MeV) | γ          | β            | 1 − β     |
|---------|---------|------------|--------------|-----------|
| u       | 2.16    | 1.0000     | 0            | 1         |
| d       | 4.70    | 2.1759     | 0.888139     | 1.12 × 10^{-1} |
| s       | 92.9    | 43.009     | 0.999730     | 2.70 × 10^{-4} |
| c       | 1273    | 589.31     | 0.999998560  | 1.44 × 10^{-6} |
| b       | 4186    | 1937.96    | 0.999999867  | 1.33 × 10^{-7} |
| t       | 172600  | 79907      | 0.9999999999 | 7.83 × 10^{-11} |

These match the phenomenological stand-in previously recorded (beta = (0, 0.8881, 0.999733, 1−1.440e-6, 1−1.333e-7, 1−7.83e-11), gamma = (1, 2.176, 43.29, 589.4, 1936.6, 7.989e4)).

## Repercussions and locks

- Purely phenomenological re-labelling of the observed mass hierarchy as Lorentz factors relative to m_u.  
- Does not derive the mass floor (still a nucleon-dressing protocol insertion).  
- Does not alter residual-L matching to laboratory G, kinematic UPS, or the hard rejection of the Tau/Tav package.  
- Distinct from the free inter-domain orbital E_orb = 3M⟨β²⟩c² of the six co-located copies; the quark-level β’s are intra-domain hierarchical labels.  
- Compatible with floor-only Dynamic Refresh and the dominant-glob rule.

## References

- PDG 2026 quark mass tables (current masses).  
- Earlier note: Personal Files/2026-09-18_V_orb_eigenvalues_from_quark_mass_increments.md.

---  
*Saved under Personal Files in the Tau-Superblock-Universe project (George-Jumble/TauSuperblock).*
