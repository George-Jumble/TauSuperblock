# Are there research-tool modifications that perform the necessary Casimir follow-ups?

- **Session date:** 2026-09-15
- **Question:** After the Fig2 `dielPT*` falsification batch, do existing research-tool modifications already perform the six follow-up steps?
- **Short answer:** **No.** Local TAV ENGINE (2026-09-15) added hashing and multi-file discovery. It did **not** add the diagnostic controls. The five statistical tests still running are the July 2026 `test_framework.py` battery, and two of them are structurally incapable of answering the questions we asked.
- **This file:** `Personal Files/2026-09-15_TSB_Casimir_research_tool_diagnostics_gap.md`

---

## 1. Variable and function key

| Symbol / name | Meaning |
|---|---|
| \(\xi_n\) | Matsubara frequency; intended x-axis for dielectric tables |
| \(\varepsilon_{\mathrm{pri}}(\xi_n)\) | Primary dielectric series; intended y-axis |
| \(N\) | Sample count (600 in the Fig2 batch) |
| \(p\) | Reported p-value |
| \(\alpha\) | Evidence threshold, `TSB_EVIDENCE_ALPHA = 0.05` |
| \(H\) | SHA-256 of the raw loaded series |
| \(\Delta\xi\) | Mean spacing of the stored x-axis, \(\mathrm{mean}(\Delta x)\) |
| \(f_s\) | Periodogram sampling frequency, \(f_s = 1/\Delta\xi\) when \(\Delta\xi>0\) |
| \(\chi^2_{\nu}\) | Chi-squared CDF used inside two of the tests |
| \(\nu\) | Degrees of freedom |
| \(s_{\mathrm{resid}}\) | `np.std(residuals)` with default `ddof=0` |
| \(m\) | Ordinary-least-squares slope of \(\log\|y\|\) vs \(\log x\) |
| \(\delta_4\) | \(\lvert m+4\rvert\), labeled “deviation from power-law −4” |
| `detect_steps` | Discrete-step test |
| `test_hysteresis` | Half-series reversal asymmetry |
| `test_periodicity` | Periodogram peak vs \(\chi^2_2\) |
| `test_log_modulations` | Sine fit on \(\log_{10} x\) |
| `test_anisotropy_or_backreaction` | \(\lvert m+4\rvert\) vs a normal tail |
| `run_full_test_suite` | Orchestrator that writes JSON / PNG / TXT |
| Family A | metal-005 tables (`Ag`, `Al`, `Gold`, `Li`) |
| Family B | molecular-on-Au tables (`Ben_Au`, `Cyc_Au`, `Oct_Au`) |

Six follow-up steps from the previous session:

1. Dump the `log_modulations` statistic and prove it moves when \(\varepsilon_{\mathrm{pri}}\) is replaced.
2. Isotropic negative control on anisotropy (copy primary into every auxiliary column).
3. Family A: compare detected period to \(\Delta\xi\).
4. Family B: bootstrap interval on hysteresis, not a point \(p\).
5. Pre-register the metal vs molecular-on-Au split before the next folder.
6. Keep SHA-256; a changed hash is a different dataset.

---

## 2. What the tool actually contains

### 2.1 On GitHub `George-Jumble/research-tool` (commit `3cacacc`, 2026-07-16)

Casimir module:

```
menus/particle/casimir/
  __init__.py
  extension.py          # menu wiring
  scanner.py            # load / download / tau-resonance scan
  test_framework.py     # the five falsification tests
  v_ppr.py              # hysteresis scale helper
```

Menu action that produced yesterday’s reports:

- `TSB Falsification Test Suite (5 predictions)` → `run_falsification_from_source` → `run_full_test_suite`

Code search on that repo for `sha256`, `raw_series_integrity`, `bootstrap`, `negative_control`, `preregister`: **zero hits**.

### 2.2 On the local TAV ENGINE that printed the 2026-09-15 log

Present locally, **not** on the July GitHub tree:

- Auto-discovery: `[TAV ENGINE] Auto-discovered 7 Casimir table(s) under …/datasets/casimir`
- Per-file integrity line: `[CASIMIR LOAD] raw_series_integrity sha256=…`
- Batch over every `dielPT*` table instead of the mock fixture only

Those are real modifications. They cover **step 6 in part** (hash is printed) and they made the seven-file batch possible. They do **not** implement steps 1–5.

Proof that the *statistics* are still the July battery: the printed block

```
=== TSB Casimir Falsification Test Report ===
discrete_steps: p=… | Evidence for TSB: …
```

matches `test_framework.py` line-for-line, and `log_modulations` returned the same \(p\) on every file (see §3).

---

## 3. Step-by-step: does a modification already do it?

| # | Needed step | In GitHub research-tool? | In local 2026-09-15 engine? | Why / why not |
|---|---|---|---|---|
| 1 | Dump `log_modulations` statistic; replace \(\varepsilon_{\mathrm{pri}}\) | No | No | JSON stores only `fitted_frequency` and `p_value`. No raw \(\chi^2\), no \(\nu\), no noise/Drude swap. |
| 2 | Isotropic anisotropy control (duplicate primary into aux columns) | No | No | The anisotropy function **never reads auxiliary columns**. |
| 3 | Period vs \(\Delta\xi\) for Family A | No | No | Period is stored as `dominant_period` in JSON, never compared to the grid. Console print omits it. |
| 4 | Bootstrap CI on Family B hysteresis | No | No | One point estimate from a half-series fold. No resample. |
| 5 | Pre-register metal vs molecular-on-Au split | No | No | No preregistration object, lockfile, or folder-level protocol. |
| 6 | Persist SHA-256 and refuse silent pooling | Not on GitHub | Hash is **printed** locally | Print ≠ ledger. No “hash changed ⇒ new dataset” guard in the suite. |

---

## 4. Why two of the existing tests cannot answer the questions even if you re-run them

### 4.1 `test_log_modulations` — p-value is a function of \(N\), not of modulation

Committed body (abbreviated):

1. Fit \( y \approx a\sin(2\pi f \log_{10}x + \phi)+c \) with seed \(f=1/7\).
2. \( r_i = y_i - \hat y_i \)
3. \( s_{\mathrm{resid}} = \mathrm{std}(r) \) with `ddof=0`
4. \( \chi^2 = \sum_i (r_i / s_{\mathrm{resid}})^2 \)
5. \( p = 1 - F_{\chi^2}(\chi^2;\,\nu=N-4) \)

If the intercept is in the model, \(\sum r_i^2 = N\, s_{\mathrm{resid}}^2\), so \(\chi^2 = N\) identically whenever the fit returns. For the Fig2 tables:

\[
N=600,\quad \nu=596,\quad \chi^2=600,\quad p=1-F_{\chi^2}(600;596)\approx 0.4463
\]

That is exactly the number printed seven times. Distinct SHA-256 values, identical \(p\). The test is not measuring hierarchical \(\Delta n\) structure. No existing flag, CLI switch, or menu item unwraps this.

A working replacement has to use an **external** error model (replicate scatter, published \(\varepsilon\) uncertainty, or a parametric Lifshitz residual), not the fit’s own residual standard deviation.

### 4.2 `test_anisotropy_or_backreaction` — not an anisotropy test, and not on the right observable

Committed body:

\[
m=\mathrm{polyfit}(\log x,\,\log(\lvert y\rvert+10^{-10}),\,1)_0,\qquad
\delta_4=\lvert m+4\rvert,\qquad
p=1-\Phi(\delta_4)
\]

| What the name claims | What the code does |
|---|---|
| Domain anisotropy / back-reaction | Single-channel power-law slope vs −4 |
| Uses the dielectric tensor / aux columns | Uses only the primary \((x,y)\) pair |
| Casimir force vs separation \(F(d)\sim d^{-4}\) | Yesterday’s batch passed \(\varepsilon(i\xi)\) vs \(\xi\) |

Dielectric functions are not \( \xi^{-4} \). \(\delta_4\) is then large, \(p\) is small, and **every** table flags True. Copying primary into auxiliary columns would not even reach this function. An isotropic control has to be written; it cannot be “turned on.”

### 4.3 The other three tests exist but stop short

**Periodicity.** Periodogram of \(y\) with \(f_s=1/\mathrm{mean}(\Delta x)\). Peak power is tested as \(\chi^2_2\). That can produce \(p=0\) when a single bin dominates — including when the “period” is the sampling grid itself. The comparison `dominant_period / Δξ` is one ratio; it is not computed.

**Hysteresis.** `mean(|y[:mid] − y[mid:][::-1]|) / std(y)`, then a normal tail. That is a shape-asymmetry number on a sorted monotone sweep, not a measured up/down Casimir loop. Family B’s \(p\sim 0.11\) is a point. No bootstrap distribution is stored.

**Discrete steps.** `diff(y)` vs \(2\sigma_{\Delta y}\), then a Poisson-like z-score on step counts. Usable as a rough detector. It is not the missing control suite.

---

## 5. What *would* have to be added

Not present today. Minimal module surface if we implement it next:

| New piece | Job |
|---|---|
| `diagnostics.log_modulation_audit(x,y)` | Return \(\chi^2\), \(\nu\), fitted \(f\), and the same \(p\) on (i) data, (ii) shuffled \(y\), (iii) monotone Drude tail. Fail the test if (i) and (ii) match to 3 digits. |
| `diagnostics.anisotropy_channel_control(df)` | Run the current slope test on primary; rerun after broadcasting primary into every `dielectric_response_*` column; run a real channel-spread statistic on the six aux series. |
| `diagnostics.period_vs_grid(x,y)` | `dominant_period`, \(\Delta\xi\), ratio, and a boolean `grid_locked`. |
| `diagnostics.hysteresis_bootstrap(x,y,B)` | Point effect + percentile CI on \(p\) and on effect size. |
| `diagnostics.preregister_split(path)` | Write a lockfile: Family A / Family B labels, \(\alpha\), test list, timestamp, hashes — before the next folder is scored. |
| `diagnostics.hash_ledger` | Keep the local SHA-256 print, and refuse to pool two files whose \(H\) differs under the same `data_label`. |

Menu action suggestion (does not exist yet):

`TSB Falsification Diagnostics (controls + audit)`

wired next to the existing five-prediction suite, writing `artifacts/tsb_test_results/tsb_diagnostics_<label>_<stamp>.json`.

---

## 6. Implications for the 2026-09-15 Fig2 batch

Re-running the *current* suite on the same seven files will reproduce the same 2/5 pattern, including the frozen `log_modulations` \(p=0.4463\) and the universal anisotropy flag. That is not confirmation and not a new measurement. The batch is still useful as a record of what the engine emits. It is not a completed falsification of Lifshitz vs TSB until the controls in §5 exist and are run.

Step 6 is the only item with a partial local implementation (`raw_series_integrity sha256=…`). Persist those hashes into the JSON report; they are not in the July GitHub `run_full_test_suite` payload.

---

## 7. Session inventory

Displayed / queried this session:

- GitHub `George-Jumble/research-tool` tree and `menus/particle/casimir/*`
- Full `test_framework.py` (SHA `73198d41…`)
- Full `extension.py` menu wiring
- Code search: `sha256`, `raw_series_integrity`, `bootstrap`, `negative_control`, `preregister` → 0 hits on GitHub
- Comparison against the 2026-09-15 TAV ENGINE console log (hashing + 7-file auto-discovery present locally)

Copies of this note:

- Workspace: `/home/workdir/artifacts/Personal Files/2026-09-15_TSB_Casimir_research_tool_diagnostics_gap.md`
- GitHub intended path: `Personal Files/2026-09-15_TSB_Casimir_research_tool_diagnostics_gap.md` on `George-Jumble/TauSuperblock`
- Drive folder: Personal Files

---

*End of session note — 2026-09-15 research-tool diagnostics gap.*
