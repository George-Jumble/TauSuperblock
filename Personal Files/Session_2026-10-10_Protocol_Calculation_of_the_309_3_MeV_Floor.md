# Session 2026-10-10: Full Protocol Calculation of the Printed 309.3 MeV Mass Floor

**Date**: 2026-10-10  
**Project**: Tau-Superblock-Universe (live Superblock Cosmology)  
**Query**: Show full derivation of the 309.3 MeV floor  
**Status**: There is no derivation from Superblock axioms, the 8-phase clock, or TEP. The printed value is the output of an explicit insertion protocol that uses measured nucleon masses and PDG current-quark masses. Clock + TEP supply only \(\Delta > 0\).

## 1. Statement of Status (Corpus Locks)

The live corpus states repeatedly that the mass floor is an insertion, not a theorem:

- TEP supplies only the inequality \(E_{\rm violation} \ge \Delta_{\rm Tav}\) (positive cost to force a bound colour line through local \(\Phi_7\to\Phi_8\) reset overlap). Unbound completed bounces pay nothing.
- No live clock derivation exists. Requirements for a genuine clock derivation (anchor \(M_*\) that is neither the floor nor \(M_n\), dimensionless clock factor \(f\) fixed before comparison, named operator that can miss) remain unmet. \(G\) and \(\tau\) are disallowed as anchors.
- Old print 313.1 MeV was \(M_n/3\) rounded. New printed working floor (2026-10-07) is the neutron dressing share.
- Equal-share among three valence lines is weak bookkeeping; the strong protocol step is “use the nucleon” (data). Primary use is per-line IR inertia / bound colour dressing.

**Key**:
- \(\Delta, \Delta_{\rm Tav}\): printed mass-floor energy scale.
- \(E_{\rm violation}\): TEP occupancy cost.
- \(\Phi_7, \Phi_8\): scrape and reset phases of the 8-phase G2 clockwork.
- \(M_n\): neutron mass.
- \(f\): dimensionless factor that would have to be fixed by the clock before any numerical comparison.

## 2. Input Data (PDG 2026)

All inputs are external measurements, not Superblock outputs.

- Neutron mass: \(M_n = 939.5654219\) MeV
- Proton mass: \(M_p = 938.27208943\) MeV
- Current up-quark mass (\(\overline{\rm MS}\) at 2 GeV): \(m_u = 2.16 \pm 0.07\) MeV
- Current down-quark mass (\(\overline{\rm MS}\) at 2 GeV): \(m_d = 4.70 \pm 0.07\) MeV

**Key**:
- \(M_n, M_p\): measured nucleon masses (CODATA/PDG).
- \(m_u, m_d\): current (Higgs-generated) quark masses.

## 3. Neutron Dressing Protocol (the source of the printed floor)

Neutron valence content is \(udd\).

Current-quark contribution:
\[
m_u + 2 m_d = 2.16 + 2\times 4.70 = 11.56\ {\rm MeV}
\]

Dressing energy (remainder after subtracting current masses):
\[
E_{\rm dress,n} = M_n - (m_u + 2 m_d) = 939.5654219 - 11.56 = 928.005422\ {\rm MeV}
\]

Equal-share bookkeeping among three valence lines:
\[
\frac{E_{\rm dress,n}}{3} = \frac{928.005422}{3} = 309.335141\ {\rm MeV}
\]

Printed working floor:
\[
\Delta = 309.3\ {\rm MeV}
\]
(rounded from the computed 309.34 MeV share).

**Key**:
- \(E_{\rm dress,n}\): neutron dressing energy (bound-colour + residual contributions after current-mass subtraction).
- Division by 3: equal-share protocol among the three valence quarks; not derived from the clock.

## 4. Proton Share (for comparison; not the print)

Proton valence content is \(uud\).

Current-quark contribution:
\[
2 m_u + m_d = 2\times 2.16 + 4.70 = 9.02\ {\rm MeV}
\]

Dressing energy:
\[
E_{\rm dress,p} = M_p - (2 m_u + m_d) = 938.27208943 - 9.02 = 929.252089\ {\rm MeV}
\]

Equal-share:
\[
\frac{E_{\rm dress,p}}{3} = 309.750696\ {\rm MeV} \approx 309.75\ {\rm MeV}
\]

This is not the printed floor.

**Key**:
- \(E_{\rm dress,p}\): proton dressing energy.

## 5. Comparison with the Old Print

Old protocol (nucleon-third, no current-mass subtraction):
\[
\frac{M_n}{3} = 313.188474\ {\rm MeV} \quad (\text{rounded to } 313.1\ {\rm MeV})
\]
\[
\frac{M_p}{3} = 312.757363\ {\rm MeV}
\]

Switching from the old print to the dressing-share print shifts \(m_0\)-linear quantities by approximately \(+1.23\times 10^{-2}\). The invariant \(S_E/\hbar = 2\) per diameter tick is unchanged.

## 6. Why This Is Not a Derivation

1. The number is obtained by subtracting external data (\(M_n\), \(m_u\), \(m_d\)) and dividing by 3.
2. TEP only enforces positivity of the cost; it does not compute 309.3 MeV.
3. The 8-phase clock and 142857 cycle fix the discrete structure and \(\alpha = 1 - \log_7 6\), but supply no absolute energy scale that equals the nucleon dressing share.
4. Any attempt to set the floor equal to a clock expression that already contains the floor is circular.
5. Suggested external anchors that could in principle close a derivation (if a dimensionless \(f\) were fixed first) include \(f_\pi\) or \(m_\pi\); none have been written into a protocol that recovers 309.3 MeV without insertion.

## 7. Most Valid Use Inside the Corpus

The printed \(\Delta = 309.3\) MeV is the per-line IR inertia / bound-colour dressing share of the neutron under the equal-share protocol. It is the scale that appears in the TEP inequality for bound colour lines, in the Compton length \(\lambda_{m_0} = \hbar c / \Delta\), and as the packing quantum. It is not a glueball pole, not a Vălean output, and not the current up mass.

**Key**:
- \(\lambda_{m_0}\): Compton length associated with the printed floor.
- \(\hbar c\): conversion constant.

## 8. Conclusion

The 309.3 MeV floor is the rounded output of the neutron dressing-share protocol applied to PDG 2026 masses. It is an insertion that satisfies the TEP positivity requirement. No derivation from the live Superblock axioms or clockwork exists, and the corpus locks record that fact.

---

**File**: Session_2026-10-10_Protocol_Calculation_of_the_309_3_MeV_Floor.md  
**Location**: Tau-Superblock-Universe/Personal Files/  
**Alignment**: Consistent with all mass-floor locks through 2026-10-10.
