# Session 2026-10-07 — EM-dominance time after vacuum inversion

**Framework**: SBT / TSB. Mirron, never soliton. Tau/Tav metric rejection kept. Standard gravity not retouched.  
**Date**: 2026-10-07  
**Charge**: The kilometre-scale Higgs figure is a placeholder. The exact scale is the time it takes for electromagnetic pressure to become dominant again after the vacuum-pressure inversion.

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-10-07_EM_Dominance_Time_after_Vacuum_Inversion.md`  
Mirrors: `Personal Files/`, `Personal_Files/`.

---

## 0. Verdict

**The placeholder is withdrawn. The time is not in the notes.**

The 26 July capture note states the hypothesis: bound mass is locked when electromagnetic pressure again dominates and suppresses Phase 7. The same day’s ratio note evaluates \(P_{\rm EM}/|P_{\rm vac}|\) at the floor density, not at a clock time, and it builds \(\rho_{\rm vac}\) with the retired stretch \(n_{\rm hier}\). The open item in that note — map the capture epoch onto hierarchical \(s\), using \(\tau\) — cannot be rerun. No live calculation returns a time or a length.

---

## 1. Complete key

| Symbol | Meaning |
|--------|---------|
| \(P_{\rm EM}\) | Electromagnetic (radiation) pressure. \(w=1/3\). |
| \(P_{\rm vac}=-\rho_{\rm vac}\) | Vacuum pressure. Negative. |
| inversion | Sign flip from vacuum-driven expansion to a radiation window. Not a derived instant. |
| \(t_\times\) | Time after inversion when \(P_{\rm EM}\) again exceeds \(\lvert P_{\rm vac}\rvert\). Not computed. |
| \(\rho_{\rm floor}=(0.3131\,\mathrm{GeV})^4\) | Floor density used in the 26 July ratio. Insertion, not an epoch. |
| \(\rho_{\rm vac}\) | Vacuum density. Input. The 26 July value \(2.5\times 10^{-47}\,\mathrm{GeV}^4\) used retired \(n_{\rm hier}\). |
| \(\Phi_7\) | Phase 7, scrape / Higgs fabric. Suppressed in the hypothesis while \(P_{\rm EM}\) is large. |
| \(300{,}000\,\mathrm{km}\) | Withdrawn placeholder length. Not \(t_\times\). |
| \(\tau\), \(n_{\rm hier}\) | Retired. Not used to time this window. |

---

## 2. What the notes say

`Session_2026-07-26_Quark_Phase_Aeon_Expansion_Mass_Binding_via_EM_Higgs_Suppression.md`: the user’s hypothesis is accepted there in structure. Domain-native quarks interact with local fields while intense radiation transiently suppresses Phase 7. Free rebound is interrupted. Residual \(L\) is captured. The note then lists as not done: numerical integration of the captured \(L\), and mapping of the capture epoch onto hierarchical \(s\), using \(\tau=7\,h^{-1}\,\mathrm{Mpc}\). That boundary condition is retired.

`Session_2026-07-26_Calculation_of_Pressure_Ratio_P_EM_over_P_vac_at_Capture_Scale.md` does not find a time. It sets \(\rho_{\rm EM}\simeq\rho_{\rm floor}\) by hand and divides:

\[
\frac{P_{\rm EM}}{|P_{\rm vac}|}
=
\frac{(0.313)^4}{3\times 2.5\times 10^{-47}}
\approx
1.28\times 10^{44}.
\]

**Key.** Numerator: floor density over \(3\), the radiation equation of state. Denominator: a vacuum density built with \(n_{\rm hier}\approx 45.8\). The ratio says that if the radiation density is the floor density, electromagnetic pressure overwhelms that vacuum. It does not say when, after inversion, the radiation density has fallen to the vacuum density. The two questions are different.

---

## 3. What a time would require

After an inversion, vacuum density is taken constant and radiation density falls as the chamber expands:

\[
\rho_{\rm EM}(a)=\rho_{\rm EM}(a_i)\left(\frac{a_i}{a}\right)^4,
\qquad
P_{\rm EM}=\frac13\rho_{\rm EM}.
\]

Dominance again means \(P_{\rm EM}(a_\times)=|P_{\rm vac}|\), so

\[
a_\times
=
a_i\left(\frac{\rho_{\rm EM}(a_i)}{3|P_{\rm vac}|}\right)^{1/4},
\qquad
t_\times
=
\int_{a_i}^{a_\times}\frac{da}{a\,H(a)}.
\]

**Key.** \(a\): scale factor of the chamber. \(a_i\): scale at inversion. \(\rho_{\rm EM}(a_i)\): radiation density there. \(H(a)\): expansion rate. None of \(a_i\), \(\rho_{\rm EM}(a_i)\), or \(H(a)\) is fixed once \(\tau\) and \(n_{\rm hier}\) are out. Laboratory \(G\) does not supply them. The integral is not evaluated.

The floor density is a particle-physics scale. Using it as \(\rho_{\rm EM}(a_i)\) is the 26 July assumption, and it produces the \(10^{44}\) ratio against cosmic \(\rho_{\rm vac}\). That fixes a density contrast, not a stopwatch reading, and the vacuum piece of that ratio is retired.

---

## 4. Status

| Item | Status |
|------|--------|
| \(300{,}000\,\mathrm{km}\) as the Higgs scale | **Placeholder. Withdrawn.** |
| Condition: EM pressure dominates again after inversion, Phase 7 suppressed, residual \(L\) captured | **Hypothesis, 26 July.** Structure kept. |
| \(t_\times\) computed | **No** |
| Ratio \(1.28\times 10^{44}\) | Density contrast at the floor. Uses retired \(n_{\rm hier}\). Not a time. |
| Gravity | Untouched |

---

## 5. Related files

- `Personal_Files/Session_2026-07-26_Quark_Phase_Aeon_Expansion_Mass_Binding_via_EM_Higgs_Suppression.md`
- `Personal_Files/Session_2026-07-26_Calculation_of_Pressure_Ratio_P_EM_over_P_vac_at_Capture_Scale.md`
- `Personal Files/Session_2026-10-07_Original_Superblock_Summary_Audit.md`
- `Personal Files/Session_2026-10-07_One_Local_c_Orbital_Envelopes.md`
