# Have the Casimir tests dropped the search for bound-energy residuals?

- **Session date:** 2026-09-15
- **Short answer:** **Yes.** The live Casimir falsification suite does not search for bound-energy residuals \(\Delta E = E_{\mathrm{obs}} - E_{\mathrm{Lifshitz}}\). What it runs instead is a five-test shape battery on a single \((x,y)\) series. Two leftover “residual” names in the code are not bound energy.
- **This file:** `Personal Files/2026-09-15_TSB_Casimir_bound_energy_residuals_dropped.md`

---

## Variable and function key

| Symbol / name | Meaning |
|---|---|
| \(E_{\mathrm{obs}}(d,T)\) | Measured Casimir energy (or free energy) at separation \(d\) and temperature \(T\) |
| \(E_{\mathrm{Lifshitz}}(d,T;\,\varepsilon)\) | Lifshitz prediction built from \(\varepsilon(i\xi_n)\) |
| \(\Delta E\) | Bound-energy residual: \(E_{\mathrm{obs}}-E_{\mathrm{Lifshitz}}\) (or \(F_{\mathrm{obs}}-F_{\mathrm{Lifshitz}}\)) |
| \(F/A\) | Lifshitz free energy per area |
| \(\xi_n\) | Matsubara frequency |
| \(\varepsilon_{\mathrm{pri}}(\xi_n)\) | Primary dielectric channel used as \(y\) in the current tests |
| \(d\) | Plate separation |
| \(E_{\mathrm{bind}}\) | TSB-side bound / hierarchical binding energy expected to sit in \(\Delta E\) |
| `hysteresis_residual_pN` | \(e_{\mathrm{hyst}} - \hat e_{\mathrm{V\_PPR}}\) in piconewtons; **not** \(\Delta E\) |
| \(e_{\mathrm{hyst}}\) | Half-series fold effect size from `test_hysteresis` |
| \(\hat e_{\mathrm{V\_PPR}}\) | `latency_to_pN_scale` of \(\lvert a_8-a_7\rvert\) |
| \(r_{\mathrm{smooth}}\) | Scanner residual \(y-\mathrm{rolling\,mean}(y)\); harmonic check only |
| \(\delta_4\) | \(\lvert m+4\rvert\) power-law shape deviation; **not** \(\Delta E\) |

Lifshitz object that would be required for a real residual search:

\[
\frac{F}{A}=\frac{k_B T}{2\pi}\sum_{n=0}^{\infty}{}'\int_0^{\infty}k_\perp\,dk_\perp\sum_{\sigma}\ln\!\bigl(1-r_\sigma^{(1)}r_\sigma^{(2)}e^{-2\kappa d}\bigr)
\]

\[
\Delta E(d,T)=E_{\mathrm{obs}}(d,T)-E_{\mathrm{Lifshitz}}(d,T;\,\varepsilon)
\]

A bound-energy search is a search for structure in \(\Delta E\) (floor, steps, 1/7 comb, hierarchical binding), not in raw \(\varepsilon(i\xi)\) or raw force.

---

## What the live tests actually do

`menus/particle/casimir/test_framework.py` (`run_full_test_suite`) scores five things on one sorted pair \((x,y)\):

| Test | Input | Output | Bound-energy residual? |
|---|---|---|---|
| `discrete_steps` | \(\Delta y\) vs \(2\sigma_{\Delta y}\) | step count + \(p\) | No |
| `hysteresis` | half-series fold of \(y\) | effect size + \(p\) + V_PPR bookkeeping | No |
| `periodicity` | periodogram of \(y\) | dominant period + \(p\) | No |
| `log_modulations` | sine fit on \(\log_{10}x\) | fitted \(f\) + broken \(\chi^2\) \(p\) | No |
| `anisotropy_backreaction` | \(\lvert m+4\rvert\) on \(\log\|y\|\) vs \(\log x\) | \(\delta_4\) + \(p\) | No — shape vs \(d^{-4}\), not \(\Delta E\) |

`scanner.py` `detect_tau_resonances` is the same family on the same series: 1/7 harmonics, steps, peaks, change-points, plus a detrended harmonic check \(r_{\mathrm{smooth}}=y-\mathrm{smooth}(y)\). That residual is a high-pass filter. It is not \(E_{\mathrm{obs}}-E_{\mathrm{Lifshitz}}\).

There is no Lifshitz integrator in the Casimir module. There is no subtraction of a predicted energy. There is no scan of \(\Delta E\) for a binding floor.

---

## Two names that look like residuals and are not

**1. `hysteresis_residual_pN`**

\[
\texttt{hysteresis\_residual\_pN}=e_{\mathrm{hyst}}-\hat e_{\mathrm{V\_PPR}}
\]

This compares a dimensionless fold of the *same* \(y\) series to a V_PPR latency mapped into piconewtons. It never sees a measured energy column and never sees a Lifshitz curve. It is a calibration mismatch, not a bound-energy residual.

**2. Scanner \(r_{\mathrm{smooth}}\)**

Used only inside `_try_tav_harmonic_check`. Subtracting a rolling mean cannot isolate a Casimir binding increment.

**3. \(\delta_4=\lvert m+4\rvert\)** (sometimes spoken of as a “residual from the Lifshitz power”)

That would be a bound-energy proxy *only if* \(y\) were force or energy versus separation and the comparison were to a computed Lifshitz \(F(d)\), not to a pure \(d^{-4}\) line. The Fig2 `dielPT*` batch passed \(\varepsilon(i\xi)\) versus \(\xi\). That observable cannot host \(\Delta E\).

---

## Why the Fig2 batch could not have recovered bound energy even if the test still existed

The seven tables are dielectric functions on the Matsubara axis:

\[
\bigl(\xi_n,\;\varepsilon_{\mathrm{pri}}(\xi_n),\;\varepsilon_1,\ldots,\varepsilon_6\bigr),\qquad N=600.
\]

To form \(\Delta E\) you need, at minimum:

1. a Lifshitz (or equivalent) integrator taking those \(\varepsilon(i\xi_n)\) to \(F(d,T)\) or \(E(d,T)\);
2. an observed energy or force column at known \(d,T\);
3. a residual series \(\Delta E(d)\) or \(\Delta F(d)\);
4. a search on *that* series (floor, steps, 1/7 comb, hierarchical binding).

None of those four objects are in `test_framework.py`, and (2) is not in the Fig2 `dielPT*` files. Running the current suite on those files is a shape analysis of \(\varepsilon(i\xi)\). It cannot drop or keep a bound-energy search that it has no data to run.

---

## So “dropped” in which sense?

Accurate statement:

- Relative to the TSB Casimir *program* (hierarchical binding / TSB-Casimir energy leftover after the Lifshitz continuum is removed): **yes, that search is not in the live battery.**
- Relative to the committed `test_framework.py` itself: the five tests were written as a shape/period/hysteresis suite. A \(\Delta E\) pipeline was never in that file on GitHub (`3cacacc`, 2026-07-16).
- Local 2026-09-15 engine added hashing and multi-file discovery. It did not add a Lifshitz subtractor.

What remains of “energy language” is V_PPR vacuum-*latency* bookkeeping on the hysteresis test, not a vacuum-*energy* residual.

---

## What would restore the search

Not present today. Minimum:

1. Lifshitz (or equivalent) \(E_{\mathrm{Lifshitz}}(d,T;\,\varepsilon)\) from the dielectric table.
2. Pair with a force/energy-versus-separation table, not with \(\varepsilon(\xi)\) alone.
3. Form \(\Delta E(d)\) and put the five shape tests — plus a floor / binding-step test — on \(\Delta E\), not on \(\varepsilon\).
4. Negative control: \(\Delta E\) computed from the same \(\varepsilon\) against itself must be consistent with zero within stated quadrature.

Until that exists, “Evidence for TSB” on a `dielPT*` file is not a bound-energy result.

---

## Session inventory

- Confirmed against `test_framework.py`, `v_ppr.py`, `extension.py`, and `scanner.py` on `George-Jumble/research-tool` @ `3cacacc`.
- Confirmed against the 2026-09-15 Fig2 `dielPT*` console log (columns are dielectric, not energy).
- No `bound_energy`, `E_bind`, `Lifshitz` subtraction, or \(\Delta E\) symbol in that module.

Copies:

- Workspace: `/home/workdir/artifacts/Personal Files/2026-09-15_TSB_Casimir_bound_energy_residuals_dropped.md`
- GitHub: `Personal Files/` on `George-Jumble/TauSuperblock`
- Drive: Personal Files

---

*End of session note — 2026-09-15 bound-energy residuals dropped from live Casimir tests.*
