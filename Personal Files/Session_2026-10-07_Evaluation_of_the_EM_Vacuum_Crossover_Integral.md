# Session 2026-10-07 — Evaluation of the EM–vacuum crossover integral

**Framework**: SBT / TSB. Mirron, never soliton. Tau/Tav metric rejection kept. Standard gravity not retouched.  
**Date**: 2026-10-07  
**Charge**: Evaluate

\[
t_\times=\int_{a_i}^{a_\times}\frac{da}{a\,H(a)}.
\]

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-10-07_Evaluation_of_the_EM_Vacuum_Crossover_Integral.md`  
Mirrors: `Personal Files/`, `Personal_Files/`.

---

## 0. Verdict

**Evaluated under stated inputs. Not a derived Superblock time.**

The integral as written is the time to dilute from an electromagnetic density equal to the floor down to \(P_{\rm EM}=|P_{\rm vac}|\). With the observed vacuum density and laboratory \(G\) inside \(H\), that time is \(4.62\,\mathrm{Gyr}\). Electromagnetic pressure is already dominant at the lower limit by \(10^{44}\). The integral does not time “EM becomes dominant again.” Dilution cannot produce that crossing: radiation falls faster than a constant vacuum.

---

## 1. Complete key

| Symbol | Meaning |
|--------|---------|
| \(a\) | Scale factor of the chamber. \(a_i=1\) by choice of unit. |
| \(a_\times\) | Scale where \(P_{\rm EM}=|P_{\rm vac}|\). |
| \(H(a)\) | Expansion rate. Friedmann form, laboratory \(G\). Not a new force. |
| \(\rho_{\rm EM}(a)\) | Radiation density, \(\propto a^{-4}\). |
| \(\rho_{\rm floor}\) | \((0.3131\,\mathrm{GeV})^4=2.004\times 10^{35}\,\mathrm{J\,m^{-3}}\). Insertion used as \(\rho_{\rm EM}(a_i)\). |
| \(\rho_{\rm vac}\) | Observed vacuum density \(5.708\times 10^{-10}\,\mathrm{J\,m^{-3}}\). Not \(\hbar c/\tau^4\). |
| \(P_{\rm EM}=\rho_{\rm EM}/3\) | Radiation pressure. |
| \(P_{\rm vac}=-\rho_{\rm vac}\) | Vacuum pressure. |
| \(G\) | \(6.67430\times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}\). Untouched. |
| \(c\) | \(2.99792458\times 10^{8}\,\mathrm{m\,s^{-1}}\). |
| \(t_\times\) | Value of the integral. |

---

## 2. Inputs, named as inputs

\[
\rho_{\rm EM}(a)=\rho_{\rm floor}\left(\frac{a_i}{a}\right)^4,
\qquad
H(a)=\sqrt{\frac{8\pi G}{3c^2}\left(\rho_{\rm EM}(a)+\rho_{\rm vac}\right)}.
\]

**Key.** First: radiation dilutes. Second: laboratory Friedmann rate with radiation plus a constant vacuum. No \(\tau\). No \(n_{\rm hier}\). \(G\) enters only as the measured constant in \(H\).

Crossover:

\[
P_{\rm EM}(a_\times)=|P_{\rm vac}|
\implies
\rho_{\rm EM}(a_\times)=3\rho_{\rm vac}
\implies
\frac{a_\times}{a_i}
=
\left(\frac{\rho_{\rm floor}}{3\rho_{\rm vac}}\right)^{1/4}
=
1.040\times 10^{11}.
\]

**Key.** Factor \(3\): equation of state \(w=1/3\). Ratio of densities \(1.170\times 10^{44}\).

---

## 3. Result

Numerical integral, \(2\times 10^{5}\) logarithmic steps:

\[
t_\times
=
1.458\times 10^{17}\,\mathrm{s}
=
4.62\,\mathrm{Gyr}.
\]

Pure-radiation \(H\), which drops the vacuum term inside the square root, gives \(4.85\,\mathrm{Gyr}\). The vacuum term shortens it. Most of the time is spent near \(a_\times\), where \(H\sim 3\times 10^{-18}\,\mathrm{s^{-1}}\).

At the lower limit, \(H(a_i)=3.53\times 10^{4}\,\mathrm{s^{-1}}\), so \(1/H(a_i)=28.3\,\mu\mathrm{s}\). Electromagnetic pressure there already exceeds \(|P_{\rm vac}|\) by \(1.17\times 10^{44}\). The \(4.62\,\mathrm{Gyr}\) is the time to fall from that dominance down to equality, not the time to reach dominance.

---

## 4. What was not evaluated

The reverse crossing — vacuum dominant just after inversion, electromagnetic dominant later — is not this integral. With \(\rho_{\rm vac}\) constant and \(\rho_{\rm EM}\propto a^{-4}\), expansion moves the ratio the other way. Reaching electromagnetic dominance after a vacuum-dominated inversion needs a source: vacuum converted into radiation, or a contraction. Neither is in the integrand. No such source term was supplied.

The \(4.62\,\mathrm{Gyr}\) is also not an age of the chamber. It is what this choice of \(\rho_{\rm floor}\) and today’s \(\rho_{\rm vac}\) produces. A different density at inversion produces a different \(t_\times\).

---

## 5. Status

| Item | Status |
|------|--------|
| Integral, floor density to \(P_{\rm EM}=\lvert P_{\rm vac}\rvert\), observed \(\rho_{\rm vac}\), laboratory \(G\) in \(H\) | **\(4.62\,\mathrm{Gyr}\)** |
| That time = EM becomes dominant after inversion | **No.** EM is already dominant at \(a_i\). |
| Reverse crossing | **Not this integral.** Needs a source. |
| \(\tau\), \(n_{\rm hier}\) | Not used |

---

## 6. Related files

- `Personal Files/Session_2026-10-07_EM_Dominance_Time_after_Vacuum_Inversion.md`
- `Personal_Files/Session_2026-07-26_Calculation_of_Pressure_Ratio_P_EM_over_P_vac_at_Capture_Scale.md`
