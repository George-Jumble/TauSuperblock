# Session 2026-10-24: Proper Candidate for Deriving the Yang–Mills Mass Gap — Constituent vs Current Quark Mass

**Date:** 2026-10-24  
**Query:** which would be the proper candidate for deriving the Yang-Mills mass gap, the constituent mass of a quark or the current mass?  
**Context:** Live Superblock frame (4D, six co-located copies, residual-\(L\) matching laboratory \(G\), floor-only DR, kinematic UPS, Tau package hard-rejected, mass floor a protocol insertion \(\approx 309.3\,\mathrm{MeV}\)). Prior notes: Yang–Mills gap unproved; floor is nucleon-dressing share, not a glueball pole, not derived from the clock or from the current up mass.  
**Status:** Neither. The Yang–Mills mass gap is an open mathematical existence problem for pure Yang–Mills (no quarks). Current mass is a UV/renormalized bare parameter; constituent mass is a phenomenological IR effective mass. The Superblock floor insertion sits near the constituent scale but does not derive the gap. TEP supplies only the inequality \(\Delta>0\).

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-10-24_YM_Mass_Gap_Candidate_Constituent_vs_Current.md`  
Mirrors: `Personal Files/`, `Personal_Files/`.

---

## Complete symbol key

| Symbol | Meaning |
|--------|---------|
| Yang–Mills mass gap | Positive lower bound \(\Delta>0\) on the spectrum of the quantum Hamiltonian of pure \(SU(N)\) Yang–Mills on \(\mathbb{R}^4\) (or \(\mathbb{R}^{1,3}\)), with the theory satisfying suitable axioms (e.g. Osterwalder–Schrader). Clay Millennium problem; unsolved. |
| pure Yang–Mills | Gauge theory of the gluon field alone; no quark fields. |
| glueball | Colour-singlet bound state of gluons. Lattice lightest scalar \(0^{++}\) mass \(\sim 1.5\)–\(1.8\,\mathrm{GeV}\). Not the Superblock floor. |
| current mass \(m_q^{\rm cur}\) | Renormalized quark mass in the \(\overline{\mathrm{MS}}\) scheme at a chosen scale (for light quarks, usually \(2\,\mathrm{GeV}\)). Perturbative/UV parameter. |
| \(m_u^{\rm cur}\) | Current up-quark mass. PDG 2026: \(2.16\pm 0.07\,\mathrm{MeV}\). |
| constituent mass \(m_q^{\rm const}\) | Phenomenological effective mass of a quark inside a hadron, incorporating binding/kinetic energy. Model-dependent. |
| NRQM constituent | Non-relativistic quark-model estimate for the up quark \(\approx 336\,\mathrm{MeV}\). |
| equal-share / dressing share | Nucleon mass minus current masses, divided by three valence lines. Printed working floor \(\approx 309.3\,\mathrm{MeV}\) (neutron protocol). Insertion, not a derivation. |
| \(\Delta_{\rm Tav}\) / floor | The inserted scale used in TEP and packing statements. Digits not supplied by the clock. |
| residual \(L\) | Angular momentum left when a bound rebound is truncated at the Present. Floor residual \(L\) is the Superblock account of colour-line inertia. |
| TEP | Topological Exclusion Principle: forced bound overlap costs \(E_{\rm violation}\ge\Delta\). Supplies the inequality only. |
| \(\Lambda_{\overline{\mathrm{MS}}}\) | QCD scale, a few hundred MeV, scheme-dependent. |
| \(\sqrt{\sigma}\) | String tension. Lattice value \(\approx 440\,\mathrm{MeV}\). |
| \(E_g=E_{q\leftarrow g}\) | Inertial energy transmitted from the bound gluon field to one valence line. Home of the floor insertion. |
| \(M_N\) | Nucleon mass. |

---

## What the Yang–Mills mass gap actually is

The Clay problem asks for a rigorous construction of quantum Yang–Mills theory for every compact simple gauge group, on four-dimensional Euclidean space, satisfying the Osterwalder–Schrader axioms, and possessing a positive mass gap: the spectrum of the Hamiltonian is bounded below by some \(\Delta>0\).

It is a pure-glue problem. Quarks are not required for the statement. Lattice simulations and experiment strongly support the existence of such a gap (glueball masses in the GeV range), but no mathematical proof is known. Recent preprints claiming solutions remain unrecognized by the Clay Institute; the problem is still listed as open.

**Plain language.** The Yang–Mills mass gap is the mathematical challenge of proving, from first principles, that a theory made only of massless gluons nevertheless produces massive particles (glueballs) and has no massless excitations. It is not a number you extract from the mass of a quark.

---

## Current mass versus constituent mass

- **Current mass.** The \(\overline{\mathrm{MS}}\) mass at \(2\,\mathrm{GeV}\). For the up quark, PDG 2026 gives \(m_u^{\rm cur}=2.16\pm 0.07\,\mathrm{MeV}\). It is a short-distance, perturbative parameter. Running it down or up does not produce the nucleon mass or a glueball mass.

- **Constituent mass.** An infrared effective mass used in quark models. Typical NRQM value for the up quark is \(\approx 336\,\mathrm{MeV}\). The equal-share nucleon-dressing protocol used in the Superblock notes yields \(\approx 309.3\,\mathrm{MeV}\) once current masses are subtracted. Both are phenomenological bookkeeping of the fact that almost all of the nucleon mass is binding energy.

Neither number is an output of the pure Yang–Mills theory, and neither is a derivation of the existence of a mass gap.

**Plain language.** The current mass is the tiny “bare” mass a quark would have if you could turn the strong force off and look at it at very short distances. The constituent mass is the much larger effective mass it appears to carry once it is locked inside a proton by the strong force. The Yang–Mills gap is about proving that the pure glue theory itself has a mass gap; it does not ask you to choose between these two quark numbers.

---

## Which is the proper candidate?

**Neither.**

- The current mass is two orders of magnitude too small and lives in the ultraviolet. Using \(E=mc^2\) on \(m_u^{\rm cur}\) simply returns \(2.16\,\mathrm{MeV}\); it does not generate a gap.
- The constituent mass (or the Superblock dressing share \(\approx 309.3\,\mathrm{MeV}\)) sits in the same ballpark as other non-perturbative QCD scales (\(\Lambda_{\overline{\mathrm{MS}}}\), \(\sqrt{\sigma}\)). It is a better *phenomenological* marker of the energy scale at which binding occurs, but it is still an input or a bookkeeping device, not a derivation of the mathematical existence of a mass gap in pure Yang–Mills.

The pure Yang–Mills gap, if it exists, is most directly related to glueball masses (\(\sim 1.5\)–\(1.8\,\mathrm{GeV}\) for the lightest scalar on the lattice). That is a different operator from the valence-quark dressing share.

In the Superblock reading the floor residual \(L\) of a stopped colour rebound is the account of the inertia of a valence line. Its printed value is the nucleon protocol insertion. TEP only guarantees \(\Delta>0\); it does not compute the digits and does not prove the Clay statement.

**Plain language.** If you are looking for a number that feels related to the non-perturbative scale of the strong force, the constituent/dressing share is the closer one. But neither the constituent mass nor the current mass is a proper candidate for *deriving* the Yang–Mills mass gap. The gap is a theorem still waiting to be proved about pure glue; the quark masses are empirical or model parameters.

---

## Superblock status

- Floor digits remain a protocol insertion (nucleon-dressing share \(\approx 309.3\,\mathrm{MeV}\)).
- Attempts to derive the floor from the current up mass fail (they return \(2.16\,\mathrm{MeV}\)).
- The floor is not a \(0^{++}\) glueball pole.
- Residual-\(L\) laboratory match, floor-only DR, kinematic UPS, and Tau rejection are unchanged.
- No claim is made that the Superblock constructs a solution to the Clay problem.

---

## Verdict

The proper answer is **neither**. The Yang–Mills mass gap is an open mathematical existence problem for pure Yang–Mills theory. The current quark mass is a UV parameter; the constituent mass is a phenomenological IR effective mass near the Superblock floor insertion. The constituent/dressing scale is the closer phenomenological marker of non-perturbative binding, but it does not derive the gap. TEP continues to supply only the inequality.

---

## Files and paths

- Primary: `Tau-Superblock-Universe/Personal Files/Session_2026-10-24_YM_Mass_Gap_Candidate_Constituent_vs_Current.md`
- Mirror: `Personal Files/Session_2026-10-24_YM_Mass_Gap_Candidate_Constituent_vs_Current.md`
- Mirror: `Personal_Files/Session_2026-10-24_YM_Mass_Gap_Candidate_Constituent_vs_Current.md`

**End of session note.**
