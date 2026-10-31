# Session 2026-10-24: How to Obtain a Clock Derivation of the Mass Floor

**Date:** 2026-10-24  
**Query:** show could we get a clock derivation? (Exact numerical value of the mass floor as a fundamental quantity rather than a protocol. \(\Delta_{\rm Tav}=309.3\) MeV is an insertion. TEP supplies only the inequality; no clock derivation exists.)  
**Framework:** Live Superblock. Mirron (not soliton). Residual-L gravity matching laboratory \(G\). Floor-only Dynamic Refresh. Tau metric package hard-rejected. Working print \(\Delta=309.3\,\mathrm{MeV}\) remains a nucleon dressing protocol until the three requirements below are met.  
**Status:** Roadmap only. No new derivation is claimed or performed here. Prior requirements (2026-10-08) restated and made operational.

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-10-24_How_to_Get_a_Clock_Derivation.md`

---

## Complete symbol key

| Symbol | Meaning |
|---|---|
| \(\Delta\) or \(\Delta_{\rm Tav}\) | Mass floor. Working print \(309.3\,\mathrm{MeV}\) (neutron dressing share protocol). Older print \(313.1\,\mathrm{MeV}=M_n/3\) rounded. Not derived. |
| clock | \((\mathbb{Z}/7\mathbb{Z})^\times\), order 6. Digit block \(142857\). Slip \(2\pi/7\). Slots 7 and 8. |
| \(f\) | Dimensionless function of the clock alone. Must be written and fixed before any comparison to a mass. |
| \(M_*\) | External dimensionful anchor mass. Must not be the floor, not \(M_n\), not \(M_n/3\), not dressing share. |
| \(E_{\rm op}\) | Named operator whose output is being derived (per-line dressing, string tension, lightest glueball, etc.). |
| TEP | Topological Exclusion Principle. Supplies only \(E_{\rm violation}\ge\Delta\) with \(\Delta>0\). |
| \(f_\pi\) | Pion decay constant (\(\approx 92\,\mathrm{MeV}\) or \(\approx 130\,\mathrm{MeV}\) by convention). Preferred external anchor. |
| \(m_\pi\) | Charged pion mass \(139.570\,\mathrm{MeV}\). Preferred external anchor. |
| \(\sqrt{\sigma}\) | QCD string tension, lattice \(\approx 440\,\mathrm{MeV}\). Usable only if \(f\) is fixed first. |
| \(S_E/\hbar=2\) | Diameter-tick action. Invariant; does not select a MeV scale. |
| \(G\), \(\tau\) | Disallowed as anchors under current cuts (gravity cut; Tau package rejected). |

---

## Why a clock derivation does not yet exist

The live clock is a finite group and a phase step. TEP is an inequality:

\[
E_{\rm violation}\ge\Delta,\qquad\Delta>0,
\qquad
f=f(6,\,2\pi/7,\,\Phi_7,\Phi_8).
\]

**Key.** \(E_{\rm violation}\): energy cost of a forced bound \(\Phi_7\to\Phi_8\) overlap. \(\Delta\): unknown positive quantum. \(f\): pure number once specified. A pure number times no mass is not a mass. \(\hbar\) and \(c\) convert an existing mass into a length; they do not choose the mass.

Until an external anchor \(M_*\), a pre-fixed \(f\), and a named operator are supplied, the print remains the protocol \(309.3\,\mathrm{MeV}\).

---

## Three requirements for a clock derivation

1. **External anchor that is not the answer**  
   \[
   \Delta_{\rm clock}=f\,M_*.
   \]  
   **Key.** \(M_*\): measured or theoretical mass fixed independently of the nucleon dressing share. Allowed candidates (stated as such): \(f_\pi\), \(m_\pi\), a lepton mass, a boson mass, \(\sqrt{\sigma}\) from a lattice scheme that did not use this floor. Disallowed under current cuts: \(M_n\), \(M_n/3\), \(E_{\rm dress}/3\), \(\tau\), \(M_{\rm Pl}\) (uses \(G\)).

2. **Clock function written first**  
   \(f\) must be an explicit expression in the clock alone (order 6, slip \(2\pi/7\), empty residue \(0\bmod 7\), associator class of the antipodal hop, etc.) and published before anyone multiplies by an anchor or compares to \(309.3\,\mathrm{MeV}\). Fitting \(f\) after the fact so that \(f M_*=309.3\,\mathrm{MeV}\) is not a derivation.

3. **Named operator that can miss**  
   State which physical quantity is being computed: per-line IR dressing, string tension, lightest \(0^{++}\) glueball, or another. Lattice glueball masses sit near \(1.5\)–\(1.8\,\mathrm{GeV}\); \(\sqrt{\sigma}\approx 440\,\mathrm{MeV}\); the dressing share is \(309.3\,\mathrm{MeV}\). These are different operators. After the calculation, compare. A miss is a legitimate result. Redefining \(\Delta\) as “whatever came out” returns the insertion.

---

## Concrete paths that satisfy the requirements

- **Preferred path (pion decay constant)**  
  Write an explicit \(f\) from the clock (example form only; not yet derived): e.g., a product of the slip, the order, and a fixed combinatorial factor from the 142857 cycle. Then compute \(\Delta_{\rm clock}=f\,f_\pi\) and compare to the protocol \(309.3\,\mathrm{MeV}\). A miss is allowed and informative. The operator must still be named (dressing share versus chiral scale).

- **Preferred path (pion mass)**  
  Same procedure with \(M_*=m_\pi\approx 139.570\,\mathrm{MeV}\). Maximally independent of the nucleon. Again, \(f\) fixed first; operator named.

- **Usable but stricter path (string tension)**  
  Use \(\sqrt{\sigma}\approx 440\,\mathrm{MeV}\) only after \(f\) is published. Because the numbers are close, post-hoc adjustment of \(f\) near \(0.7\) would be immediately suspicious. Operator: string tension, not dressing.

- **Honest but likely to miss (lepton masses)**  
  Anchor on \(m_e\) or \(m_\mu\). The required \(f\) would be large and would test a lepton-to-dressing ratio rather than QCD binding. A miss is expected and still useful.

**Not recommended as anchors**  
\(\Lambda_{\overline{\mathrm{MS}}}\) (scheme-dependent and defined near the QCD scale), nucleon mass or any third of it, constituent-up estimators, \(M_W+M_Z\), Planck mass, retired \(\tau\).

---

## What this does not require

- Another rounding of \(M_n/3\).
- Restoration of the retired Tau circle, \(n_{\rm hier}\), or \(\hbar c/\tau^4\).
- A Vălean residue aimed at the old print.
- Lifting the gravity cut so that \(M_{\rm Pl}\) can be used.

---

## Status after this note

| Item | Status |
|---|---|
| Clock raw material | In hand (dimensionless) |
| Anchor \(M_*\neq\Delta\) | Still missing; preferred candidates named (\(f_\pi\), \(m_\pi\)) |
| \(f\) fixed in advance | Still missing; must be written from the clock alone |
| Named operator | Not yet chosen |
| Working print until all three exist | \(309.3\,\mathrm{MeV}\) (protocol) |

A clock derivation becomes available the moment an explicit \(f\) is published, an allowed \(M_*\) is selected, the operator is named, and the product is compared. Until that comparison is performed and can miss, the floor remains an insertion.

End of session note.
