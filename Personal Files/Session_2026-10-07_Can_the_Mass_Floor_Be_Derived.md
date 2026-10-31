# Session 2026-10-07 — Can the mass floor be derived?

**Framework**: SBT / TSB. Mirron, never soliton.  
**Date**: 2026-10-07  
**Charge**: Is there a way to derive the mass floor? Is there a reason to cling to \(313.1\,\mathrm{MeV}\)?

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-10-07_Can_the_Mass_Floor_Be_Derived.md`  
Mirrors: `Personal Files/`, `Personal_Files/`.

---

## 0. Verdict

**No derivation in the live frame. No reason to cling to the digits \(313.1\) beyond bookkeeping.**

Topological exclusion supplies a positive cost. It does not supply the MeV. Every historical “derivation” (Planck–Kerr average, Vălean weight-6, Fredholm index) was a reconstruction aimed at a number already inserted. Those reconstructions are retired.

The reason the printed value is \(313.1\) is a protocol: take the measured neutron, divide by three, round. That protocol can be replaced by a tighter nucleon share without touching the jobs the floor does. Clinging to \(313.1\) is only so existing formulae do not all shift by a part in \(10^{4}\).

---

## 1. Complete key

| Symbol | Meaning |
|--------|---------|
| \(\Delta_{\rm Tav}=m_0 c^2\) | Printed floor \(313.1\,\mathrm{MeV}\). Inserted. |
| \(M_n\) | Measured neutron mass. \(939.565\,\mathrm{MeV}\). |
| \(M_n/3\) | Equal share of the whole neutron. \(313.188\,\mathrm{MeV}\). |
| \(m_u^{\rm cur}\), \(m_d^{\rm cur}\) | Current masses. Corpus figures \(2.16\,\mathrm{MeV}\), \(4.70\,\mathrm{MeV}\). |
| \(E_{\rm dress}^{(n)}\) | Neutron mass minus current-quark masses. Colour-dressing budget. |
| \(E_g=E_{q\leftarrow g}\) | Per-line dressing. Home of the floor in the 14 September lock. |
| TEP | Occupancy rule. Supplies \(\Delta>0\), not the digits. |
| \(E_{\rm violation}\) | Cost of a forced bound \(\Phi_7\to\Phi_8\) overlap. \(\ge\Delta_{\rm Tav}\). |
| \(\lambda_{m_0}=\hbar c/\Delta_{\rm Tav}\) | Compton length of whatever scale is inserted. \(0.63024\,\mathrm{fm}\) at \(313.1\,\mathrm{MeV}\). |
| \(S_E/\hbar=2\) | Action of one diameter tick. Invariant under a rescaling of the floor. |
| Estimator B | Magnetic-moment constituent, \(\approx 336\,\mathrm{MeV}\). Not the floor. |

---

## 2. Why it is not derived

Locked language, 26 September, quoting earlier locks:

- Master v2.0 (6 July 2026): \(313.1\,\mathrm{MeV}\) is an observational input. Geometry explains mechanism, not the digits.
- 14 September 2026: input, one phenomenological home (constituent inertia).
- 21 September 2026: “IR floor \(m_0=313.1\,\mathrm{MeV}\) as input, not derived.”
- 26 September: naming \(M_n/3\) did not convert the insertion into a theorem.

What TEP actually gives:

\[
E_{\rm violation}\ge\Delta,\qquad\Delta>0.
\]

**Key.** \(E_{\rm violation}\): cost of forcing a bound colour line through local reset overlap. \(\Delta\): some positive dressing quantum. The inequality is the principle. The MeV are chosen.

Retired reconstructions, not to be revived:

- \(M_{\rm eff}^{p\text{-}k}=M_{\rm Pl}/(6\langle\gamma\rangle_6\sqrt{N_{\rm bubble}})\approx 313.1\,\mathrm{MeV}\). Right-hand side was never an independent measurement of that number.
- Vălean weight-6 residue as the floor. Not. Current up mass is not the floor either.
- \(313\,\mathrm{MeV}\) glueball pole. Retired as hallucination. The floor is per-line inertia, not a \(0^{++}\) pole.

---

## 3. Why \(313.1\) and not another number

Protocol A, the printed one: use the nucleon (strong; it is data), share equally among three valence lines (weak; proton is \(uud\), neutron is \(udd\); kinetic, hyperfine, and electromagnetic pieces are not \(1{:}1{:}1\)).

\[
\frac{M_n}{3}=313.188\,\mathrm{MeV},
\]

printed \(313.1\). **Key.** \(M_n\): neutron mass. Factor \(3\): valence count, a bookkeeping choice.

Tighter share, already computed 26 September, still an insertion:

\[
E_{\rm dress}^{(n)}
=
M_n-m_u^{\rm cur}-2m_d^{\rm cur}
=
928.01\,\mathrm{MeV},
\qquad
\frac{E_{\rm dress}^{(n)}}{3}
=
309.34\,\mathrm{MeV}.
\]

**Key.** Subtracts current masses before sharing. Assumes equal dressing, not equal total mass. Better physics. No longer \(313.1\).

Not candidates: current up \(2.16\,\mathrm{MeV}\) (Higgs remainder, not the dressing). Magnetic-moment constituent \(\approx 336\,\mathrm{MeV}\) (a different operator).

Dropping the rounding \(313.1\to M_n/3\) shifts every \(m_0\)-linear quantity by \(+2.8\times 10^{-4}\). That is the only cost of letting go of the printed digits. \(S_E/\hbar=2\) does not move. Compton length scales as \(1/m_0\).

---

## 4. What would count as a derivation

A derivation would compute the MeV from the clock and the occupancy rule without putting a hadron mass in. The live frame has no such computation. Acceptable replacements are other protocols on the same nucleon, stated as protocols. They remain insertions.

Jobs that need some positive scale, and do not care that it is \(313.1\) rather than \(309.34\): TEP cost, kernel ultraviolet cutoff, packing quantum, Mirron Compton clock. State which protocol. Keep \(313.1\) in old formulae until a calculation needs the current-mass split.

---

## 5. Status

| Claim | Status |
|-------|--------|
| Floor derived from TEP, Vălean, or Planck average | **No** |
| \(313.1=M_n/3\) rounded | **Protocol. Data plus equal share.** |
| Reason to cling to the digits | **Bookkeeping only.** Relative shift \(2.8\times 10^{-4}\) if unrounded. |
| Dressing-only share | \(309.34\,\mathrm{MeV}\). Still inserted. |
| Glueball at \(313\,\mathrm{MeV}\) | **Retired** |

---

## 6. Related files

- `Personal Files/Session_2026-09-26_Floor_was_inserted_not_derived.md`
- `Personal Files/Session_2026-09-26_Most_valid_use_of_the_313_floor.md`
- `Personal Files/Session_2026-09-26_TEP_floor_from_observables_up_constituent.md`
- `Personal Files/Session_2026-10-07_Current_State_of_the_Project.md`
