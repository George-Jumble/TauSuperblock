# Grok Build prompt — Casimir suite diagnostics + bound-energy residuals

Copy everything inside the fence below into Grok Build. Point Build at the local research-tool tree (the one that printed `[TAV ENGINE] Auto-discovered 7 Casimir table(s)` and `raw_series_integrity sha256=`), not only at the July 2026 GitHub snapshot.

---

```
GROK BUILD TASK — TSB Casimir suite: fix broken tests, add controls, restore bound-energy residuals.

You are editing the Tau-SB / TAV ENGINE research tool on disk. Work in the repo that contains:

  menus/particle/casimir/test_framework.py
  menus/particle/casimir/scanner.py
  menus/particle/casimir/extension.py
  menus/particle/casimir/v_ppr.py

Typical local root (adjust if the tree lives elsewhere, do not invent a second copy):

  /home/wyle-e/Storage7TB/Research/scripts/research_tool/

GitHub mirror of an older snapshot: George-Jumble/research-tool @ menus/particle/casimir/
Local engine is AHEAD of that snapshot (hashing + 7-file auto-discovery already exist). Preserve those local features. Do not revert them to the July GitHub file.

============================================================
GOAL
============================================================

The live Casimir falsification battery is a five-test shape suite on one (x, y) pair. It has three classes of defect:

A. Two tests are structurally invalid.
B. Three tests stop short of the controls we need.
C. The TSB-Casimir program — bound-energy residuals after subtracting a Lifshitz continuum — is not implemented anywhere in the Casimir series.

Fix A–C throughout the Casimir series: test_framework.py, scanner.py, extension.py, and any local loader that prints [CASIMIR LOAD] / [TAV ENGINE] Falsification tests. Add a new diagnostics module rather than burying one-off scripts.

Do not “fix” results by loosening alpha or renaming flags. Fix the statistics and the observables.

============================================================
VARIABLE KEY (use these names in code, JSON, and comments)
============================================================

  xi_n              Matsubara frequency (column often matsubara_frequency)
  eps_pri           primary dielectric (column dielectric_response_primary)
  eps_k             auxiliary dielectric channels dielectric_response_1..6
  N                 sample count
  p                 p-value
  alpha             TSB_EVIDENCE_ALPHA = 0.05 (keep)
  H                 SHA-256 of the raw loaded table bytes (already printed locally)
  dx, Delta_xi      mean spacing of sorted x
  fs                periodogram sampling rate = 1/dx
  s_resid           np.std(residuals, ddof=0)  — MUST NOT be used as the chi2 sigma
  m                 OLS slope of log|y| vs log x
  delta_4           abs(m + 4)
  E_obs(d, T)       measured Casimir energy or free energy vs separation
  E_Lifshitz(d,T;eps) Lifshitz prediction from eps(i xi)
  Delta_E           bound-energy residual = E_obs - E_Lifshitz  (or F_obs - F_Lifshitz)
  E_bind            TSB hierarchical binding expected to live in Delta_E
  e_hyst            current hysteresis effect size
  e_hat_vppr        V_PPR latency mapped to pN (keep, but label it calibration residual)
  Family A          elemental metal 005 tables: dielPTAg005, dielPTAl005, dielPTGold005, dielPTLi005
  Family B          molecular-on-Au: dielPTBen_Au, dielPTCyc_Au, dielPTOct_Au

============================================================
BUGS THAT MUST BE FIXED (do not leave these standing)
============================================================

1) test_log_modulations in test_framework.py

   Current body fits
     y ≈ a * sin(2π f log10(x) + phi) + c
   with seed f = 1/7, then sets
     chi2 = sum((r_i / std(r))^2)
     p = 1 - chi2.cdf(chi2, df=N-4)

   Because std is computed from the same residuals, chi2 == N whenever the fit returns.
   For N=600 this is identically p ≈ 0.4463. That is why every Fig2 dielPT* file printed
   log_modulations p=0.4463. This is not a measurement.

   REQUIRED FIX:
   - Never divide residuals by their own sample std for a p-value.
   - Return the raw fit: a, f, phi, c, chi2_raw = sum(r_i^2), N, and a named status.
   - Audit protocol (must run every time, not optional):
       (i)  data
       (ii) y shuffled against fixed x (seed recorded)
       (iii) monotone surrogate: a decreasing Drude-like tail or a smooth cubic spline
             with no sine planted
     Fail / mark `log_modulations.identically_null = true` if p_data and p_shuffle
     agree to 3 decimal places OR if chi2_raw / N is the same to 3 digits on (i) and (ii).
   - If an external error column or published sigma exists, use that for a real
     chi2 p-value. If not, report effect size (fitted |a| / rms(y)) and a permutation
     p-value from (ii), not the broken analytic chi2.

2) test_anisotropy_or_backreaction in test_framework.py

   Current body is
     m = polyfit(log x, log(|y|+1e-10), 1)[0]
     delta_4 = abs(m + 4)
     p = 1 - norm.cdf(delta_4)

   Defects:
   - It never reads auxiliary dielectric columns.
   - −4 is a Casimir FORCE vs SEPARATION index. Yesterday’s batch passed eps(i xi) vs xi.
   - On a dielectric function, delta_4 is almost always large, so every file flags True.

   REQUIRED FIX:
   Split into two named tests. Do not keep one name that means two things.

   a) powerlaw_index
      Only legal when x is a separation/distance column AND y is force, energy, or pressure.
      Compare m to −4 (force ~ d^{-4}) or −3 (energy ~ d^{-3}) depending on y’s name.
      If x is matsubara_frequency / frequency, this test MUST return
        status = "not_applicable", p = null, evidence_for_TSB = false
      and must not be counted in S_TSB.

   b) anisotropy_channels
      Legal when two or more dielectric_response_* columns exist.
      Statistic: spread of aux channels about eps_pri
        (e.g. rms_k (eps_k - eps_pri) / rms(eps_pri), or a Hotelling / Kruskal test
         across channels).
      NEGATIVE CONTROL (mandatory every run):
        Broadcast eps_pri into every aux column, recompute the statistic.
        If the control still flags evidence_for_TSB, mark
          anisotropy_channels.control_failed = true
          evidence_for_TSB = false
        regardless of the data p-value.

3) test_periodicity

   Keep the periodogram. ADD:
     dominant_period, Delta_xi, ratio = dominant_period / Delta_xi, grid_locked bool.
   grid_locked = true if ratio is within 2% of an integer (including 1).
   If grid_locked, evidence_for_TSB must be false and the JSON must say why
   (“period matches sampling grid, not a physical modulation”).
   Print dominant_period and grid_locked in the console report, not only in JSON.

4) test_hysteresis

   Keep the point estimate. ADD a bootstrap:
     B default 1000, resample (x,y) pairs or residual-block bootstrap if x is ordered.
     Store effect_size, p_point, effect_size_ci_lo, effect_size_ci_hi,
     p_ci_lo, p_ci_hi.
   Label clearly that this is a shape-asymmetry of a sorted sweep, NOT a measured
   up/down Casimir loop, unless the table actually contains a forward and reverse pass
   (detect columns with names containing up/down, forward/reverse, retract/approach).
   If a real two-pass pair exists, compute the loop area and use THAT as e_hyst.

5) Hash ledger

   Local engine already prints
     [CASIMIR LOAD] raw_series_integrity sha256=...
   Persist H into every JSON report as raw_series_sha256.
   Keep a ledger file artifacts/tsb_test_results/casimir_hash_ledger.jsonl
   one line per (data_label, path, H, n_rows, n_cols, stamp).
   If the same data_label is reused with a different H, refuse to pool and print
     [CASIMIR LOAD] HASH MISMATCH for label=... old=... new=...
   Do not overwrite the old line.

6) Family split preregistration

   Add artifacts/tsb_test_results/preregister_casimir_families.json with:
     family_A labels, family_B labels, alpha, test list, created_utc, note
     “scored after lock; do not edit labels after first score of a new folder”.
   A new function preregister_split(...) writes this file only if it does not exist,
   or if --relock is passed. Scoring a new folder must load the lockfile first
   and attach it to the report. Do not infer families after looking at p-values.

============================================================
RESTORE BOUND-ENERGY RESIDUALS (missing, must add)
============================================================

The TSB-Casimir claim is not “eps(i xi) has wiggles”. It is that after the Lifshitz
continuum is removed, a bound / hierarchically bound energy remains:

  Delta_E(d, T) = E_obs(d, T) - E_Lifshitz(d, T; eps)

Implement this as a first working pipeline, not a comment.

New module (create):

  menus/particle/casimir/bound_energy.py

Minimum viable Lifshitz-style estimator, documented as APPROXIMATE if you cannot
port a full scattering-code integrator in one pass:

  - Inputs: xi_n, eps_pri(xi_n) [and aux channels if present], a separation grid d,
    temperature T (default 300 K unless a column or metadata provides T).
  - Compute a 1D Lifshitz / proximity-force free-energy density F/A(d) from the
    Matsubara sum using the available eps(i xi). Use a vacuum gap kernel.
    State every approximation in the JSON under "lifshitz_approximations".
  - If the table is already force/energy vs separation (not dielectric vs xi),
    skip the integrator and treat y as E_obs or F_obs directly.
  - If BOTH a dielectric table and a force/energy table are available for the
    same material label, pair them by label (Ag, Al, Au, Li, Ben_Au, Cyc_Au, Oct_Au).
  - Output columns: d, E_Lifshitz, E_obs (if present), Delta_E, Delta_E_sigma
    (use published uncertainty if present; otherwise leave sigma null and use
    permutation tests rather than fake chi2).

Search ON Delta_E, not on eps:

  - floor test: is there a stable nonzero offset E_bind after the continuum is gone?
  - discrete_steps, periodicity+grid lock, log_modulation AUDIT, hysteresis bootstrap
    all reused from the fixed test_framework, pointed at (d, Delta_E).
  - negative control: integrate eps against itself and demand Delta_E consistent
    with 0 within stated quadrature when E_obs is replaced by E_Lifshitz
    (identity subtraction). If this control fails, do not claim E_bind.

If a full Lifshitz integrator is too large for one patch, implement a clearly
named menus/particle/casimir/lifshitz_approx.py with:

  - Matsubara sum
  - TE/TM Fresnel for planar vacuum gap
  - n_max taken from the table length (600 for Fig2)
  - unit handling documented

and wire bound_energy.py to it. Do not pretend the approximation is a full
scattering code.

============================================================
APPLY THROUGHOUT THE CASIMIR SERIES
============================================================

Not just test_framework.py.

1) scanner.py detect_tau_resonances
   - Stop treating dielectric-vs-frequency as if it were force-vs-separation
     for any power-law / −4 language.
   - When aux dielectric columns exist, run anisotropy_channels + control.
   - When a force/energy vs d table is in hand, optionally compute Delta_E
     via bound_energy.py and run detect_tau_resonances on Delta_E as a second
     pass labeled observable="bound_energy_residual".
   - Persist H, param_col, value_col, observable_kind
     (dielectric | force | energy | residual) in every scan JSON.
   - _try_tav_harmonic_check residuals stay as a high-pass harmonic check but
     MUST be named "detrended_harmonic_residual" in JSON so they cannot be
     confused with Delta_E.

2) extension.py menu
   Keep existing action:
     "TSB Falsification Test Suite (5 predictions)"
   Add:
     "TSB Falsification Diagnostics (controls + audit)"
     "TSB Bound-Energy Residual Search"
   Diagnostics action runs the audit/control battery on whatever the loader
   already auto-discovers under datasets/casimir (preserve 7-file discovery).
   Bound-energy action runs bound_energy.py + tests on Delta_E.
   Both write artifacts/tsb_test_results/ with prefixes
     tsb_diagnostics_
     tsb_bound_energy_

3) Loader / [CASIMIR LOAD]
   Keep sha256 print. Also print:
     observable_kind=
     n_aux_dielectric_channels=
     applicable_tests=
   so a dielectric table is never silently scored as a d^{-4} force law.

4) Console report format
   Keep the existing block
     === TSB Casimir Falsification Test Report ===
     <test>: p=... | Evidence for TSB: True/False
   ADD under each test the extra fields above (grid_locked, control_failed,
   identically_null, n/a reason, CI). Add a second block when Delta_E exists:
     === TSB Bound-Energy Residual Report ===

5) Tests (pytest or a menus/particle/casimir/tests/ script runnable by
   python -m pytest or python menus/particle/casimir/tests/test_diagnostics.py)

   MUST include:
   a) log_modulations on white noise and on a planted sine produce DIFFERENT
      permutation p-values; the old chi2 path is gone (assert no function
      divides residuals by std(residuals) for a p-value).
   b) anisotropy_channels on identical aux copies => evidence_for_TSB False
      and control_failed False (control itself is null).
   c) powerlaw_index on a synthetic dielectric-vs-xi frame => not_applicable.
   d) powerlaw_index on y = c * d**(-4) => evidence_for_TSB False
      (consistent with Lifshitz index).
   e) periodicity on a pure sampling comb => grid_locked True, evidence False.
   f) identity Lifshitz subtraction => Delta_E consistent with 0
      (no E_bind claim).
   g) hash ledger: scoring the same path twice with unchanged bytes does not
      warn; changing one value does.

============================================================
IMPLEMENTATION CONSTRAINTS
============================================================

- Python 3.11+, numpy, scipy, pandas, matplotlib already in the tool.
- Do not add heavy new dependencies if a few hundred lines of numpy will do.
  If you need mpmath for the Matsubara sum, isolate it and guard the import.
- Keep TSB_EVIDENCE_ALPHA = 0.05.
- Keep V_PPR hysteresis calibration fields, but rename the JSON key
  hysteresis_residual_pN comment to "v_ppr_calibration_residual_pN" and
  document that it is NOT Delta_E.
- Do not edit DESI / Berard / CMS modules.
- Do not rewrite the curses UI beyond adding the two menu actions and their
  entry_fields / entry_instructions.
- Match existing TAV ENGINE log prefixes: [TAV ENGINE], [CASIMIR LOAD].
- Write a short CHANGELOG snippet at
  menus/particle/casimir/CHANGELOG_bound_energy_diagnostics.md
  listing every function changed and the acceptance tests.

============================================================
ACCEPTANCE
============================================================

Done means:

1. Re-running the Fig2 github_magnetic_fluid/Fig2/dielPT* batch no longer prints
   the same log_modulations p=0.4463 on every file unless the audit explicitly
   marks identically_null (which it should, until an external sigma exists).
2. anisotropy_backreaction is no longer a universal True on dielectric tables.
   powerlaw_index is n/a on those tables. anisotropy_channels reports a control.
3. Family A periodicity reports dominant_period, Delta_xi, grid_locked.
4. Family B hysteresis reports a bootstrap interval.
5. Every JSON has raw_series_sha256.
6. A bound-energy path exists and the identity-subtraction control runs.
7. pytest (or the local test script) for the seven cases above passes.

Start by reading the current local files, then implement. Do not stop at a plan.
```

---

## Variable key for this session note

| Name | Meaning |
|---|---|
| Grok Build | in-repo coding agent that should apply the fenced prompt to the local research tool |
| \(\Delta E\) | \(E_{\mathrm{obs}}-E_{\mathrm{Lifshitz}}\) |
| `identically_null` | audit flag that the log-modulation p-value does not move under shuffle |
| `grid_locked` | detected period is an integer multiple of \(\Delta\xi\) |
| `control_failed` | isotropic broadcast still flags anisotropy |
| `observable_kind` | `dielectric` \| `force` \| `energy` \| `residual` |

---

## How to use

1. Open Grok Build against the research-tool tree that owns `datasets/casimir/github_magnetic_fluid/Fig2/`.
2. Paste the fenced prompt unchanged.
3. After it lands, run the Fig2 `dielPT*` folder again and keep the new JSON next to the 2026-09-15 stamps (`20260915_224203`–`224211`) so the before/after is explicit.
4. Do not treat a still-True anisotropy flag on dielectric tables as progress unless `powerlaw_index` is `not_applicable` and `anisotropy_channels.control_failed` is false.

---

*End of session note — 2026-09-15 Grok Build prompt for Casimir diagnostics and bound-energy residuals.*
