# TSB Casimir Falsification Session — github_magnetic_fluid / Fig2 (dielPT*)

- **Session date:** 2026-09-15
- **Engine stamp:** TAV ENGINE reports `20260915_224203` through `20260915_224211`
- **Source log:** TAV ENGINE auto-discovery of 7 Casimir tables under  
  `/home/wyle-e/Storage7TB/Research/scripts/research_tool/datasets/casimir`
- **Table family:** `github_magnetic_fluid/Fig2/dielPT*`
- **Author context:** Tau-Superblock (TSB) / Tav-Superblock Casimir sector
- **This file:** `Personal Files/2026-09-15_TSB_Casimir_Falsification_dielPT_Fig2_session.md`

---

## 1. What was run

TAV ENGINE loaded seven dielectric-response tables (each shape `(600, 7)`), hashed the raw series, and ran the five-test TSB Casimir falsification battery on the **primary dielectric channel** versus Matsubara frequency.

### 1.1 Datasets (complete results)

| Label | Inferred material | SHA-256 of raw series | n(ξ) | n(ε_primary) | Plot / JSON / TXT stamp |
|---|---|---|---:|---:|---|
| `dielPTAg005` | Ag (silver), 005 series | `875bb2b607ba9665eeedd750e2a60b4ab38549887383180a1f70bbd84d9ff793` | 600 | 600 | `20260915_224203` |
| `dielPTAl005` | Al (aluminum), 005 series | `26ab14f5560abe5b305dd7480178761ec6aff181e070e39f09af7525b3c715e3` | 600 | 600 | `20260915_224206` |
| `dielPTBen_Au` | Benzene on Au | `ae498e6202fdc9c01c1a4f29e89ec949d20c491bbec629bb51906988172f634f` | 600 | 600 | `20260915_224207` |
| `dielPTCyc_Au` | Cyclohexane on Au | `b05b5f185731c6b59c594568e20bc8b5dd8afdf4e4a8261d0309a29628581bfe` | 600 | 600 | `20260915_224208` |
| `dielPTGold005` | Au (gold), 005 series | `7542c404394d77bb77d0d6d952f3c854a8e4c64ef773ff6d8597aada68752fcd` | 600 | 600 | `20260915_224209` |
| `dielPTLi005` | Li (lithium), 005 series | `47acc787718b4807308f28f74f0e9a6039d7e64d9f8f265332c473bb763fb6bb` | 600 | 600 | `20260915_224210` |
| `dielPTOct_Au` | Octane on Au | `f825c33ef46209e5c8453b74d6fec4ee27dccd6d25be269dfb07cce1dc03d7a1` | 600 | 600 | `20260915_224211` |

Column layout is not identical across the family:

- **Metal-005 tables** (`Ag`, `Al`, `Gold`, `Li`):  
  `matsubara_frequency`, `dielectric_response_1`, `dielectric_response_primary`, `dielectric_response_3` … `6`
- **Molecular-on-Au tables** (`Ben_Au`, `Cyc_Au`, `Oct_Au`):  
  `matsubara_frequency`, `dielectric_response_1`, `dielectric_response_2`, `dielectric_response_3`, `dielectric_response_primary`, `dielectric_response_5`, `dielectric_response_6`

That column-index shift is real and should stay in the loader contract: the engine already keys on `dielectric_response_primary` rather than a fixed column number.

Artifact root on the research machine:

```
/home/wyle-e/Storage7TB/Research/scripts/research_tool/artifacts/tsb_test_results/
  tsb_falsification_<LABEL>_report_<STAMP>.png
  tsb_falsification_<LABEL>_report_<STAMP>.json
  tsb_falsification_<LABEL>_summary_<STAMP>.txt
```

---

## 2. Variable and function key

Used throughout this session note. Every symbol that appears in the test interpretation is listed here.

### 2.1 Data and Lifshitz / Matsubara objects

| Symbol | Name | Meaning |
|---|---|---|
| \( n \) | Matsubara index | Discrete imaginary-frequency index, \( n = 0,1,2,\ldots \). Here the tables store 600 samples of the frequency axis. |
| \( \xi_n \) | Matsubara frequency | \( \xi_n = 2\pi n k_B T / \hbar \). Column `matsubara_frequency`. |
| \( k_B \) | Boltzmann constant | Thermal energy scale in \( \xi_n \). |
| \( T \) | Absolute temperature | Temperature of the Casimir / Lifshitz calculation that produced the table. |
| \( \hbar \) | Reduced Planck constant | Appears in \( \xi_n \). |
| \( \varepsilon(i\xi) \) | Dielectric function on the imaginary axis | Material response used by Lifshitz theory. Primary channel: `dielectric_response_primary`. Auxiliary channels: `dielectric_response_1` … `6`. |
| \( \varepsilon_{\mathrm{pri}}(\xi_n) \) | Primary dielectric series | The series the five tests actually consume. |
| \( N \) | Sample count | \( N = 600 \) for every table in this batch. |
| \( H \) | SHA-256 | Raw-series integrity hash printed as `raw_series_integrity sha256=…`. |

Lifshitz free energy per unit area (context only; not recomputed in this log):

\[
\frac{F}{A} = \frac{k_B T}{2\pi} \sum_{n=0}^{\infty}{}' \int_0^{\infty} k_\perp \, dk_\perp \; \sum_{\sigma=\mathrm{TE},\mathrm{TM}} \ln\!\bigl(1 - r_\sigma^{(1)} r_\sigma^{(2)} e^{-2\kappa d}\bigr)
\]

| Symbol | Name | Meaning |
|---|---|---|
| \( F/A \) | Lifshitz free-energy density | Casimir–van der Waals free energy per area. |
| \( k_\perp \) | In-plane wave number | Integration variable in the Lifshitz integral. |
| \( \sigma \) | Polarization | TE or TM. |
| \( r_\sigma^{(j)} \) | Fresnel reflection amplitude | Plate \( j \), polarization \( \sigma \); built from \( \varepsilon(i\xi_n) \). |
| \( \kappa \) | Imaginary-axis decay | \( \kappa = \sqrt{k_\perp^2 + \xi_n^2/c^2} \) in vacuum; generalized inside media. |
| \( d \) | Plate / film separation | Geometric gap in the Casimir geometry. |
| \( \sum' \) | Primed Matsubara sum | \( n=0 \) term is counted with weight \( 1/2 \). |

### 2.2 Falsification statistics

The engine reports a p-value \( p \) and a boolean `Evidence for TSB` for each of five named tests. From this batch, the decision rule is consistent with:

\[
\text{Evidence for TSB} \;=\; \mathbf{1}\!\left[ p < \alpha \right], \qquad \alpha \approx 0.05
\]

| Symbol | Name | Meaning in this battery |
|---|---|---|
| \( p \) | p-value | Probability, under the null “no TSB-type structure,” of a statistic at least as extreme as the one observed. |
| \( \alpha \) | Decision threshold | Inferred ~0.05 from the True/False pattern (all \( p \le 6.8\times10^{-4} \) are True; all \( p \ge 0.103 \) are False). |
| \( \mathbf{1}[\cdot] \) | Indicator | 1 if the inequality holds, else 0. |
| `discrete_steps` | Step / quantization test | Asks whether \( \varepsilon_{\mathrm{pri}}(\xi_n) \) (or a transform of it) is better described by discrete levels than by a smooth continuum. Small \( p \) = steps detected = TSB-positive in the engine’s coding. |
| `hysteresis` | Path-dependence / loop test | Asks whether forward vs reverse traversal of the frequency axis (or of an auxiliary pair of dielectric channels) encloses a loop. Small \( p \) would be TSB-positive; none of the seven tables reach that. |
| `periodicity` | Periodic-component test | Asks whether a preferred period exists in \( \varepsilon_{\mathrm{pri}}(\xi_n) \) or in \( \log \xi \). \( p = 0 \) is treated as TSB-positive. |
| `log_modulations` | Log-frequency modulation test | Asks for multiplicative ripples in \( \log \xi \). In this batch the reported \( p \) is **identical** on all seven tables. |
| `anisotropy_backreaction` | Anisotropy / back-reaction test | Asks whether the dielectric tensor (or the spread among auxiliary channels) shows a statistically anisotropic back-reaction on the primary series. Small \( p \) = TSB-positive. **Universal hit in this batch.** |

Score used below:

\[
S_{\mathrm{TSB}} = \sum_{t \in \mathcal{T}} \mathbf{1}\!\left[ \text{Evidence for TSB on test } t \right], \qquad \mathcal{T} = \{\text{5 named tests}\}
\]

\[
f_{\mathrm{TSB}} = S_{\mathrm{TSB}} / 5
\]

| Symbol | Name | Meaning |
|---|---|---|
| \( S_{\mathrm{TSB}} \) | Hit count | Number of tests flagged True for a given table. Range \( 0 \ldots 5 \). |
| \( f_{\mathrm{TSB}} \) | Hit fraction | \( S_{\mathrm{TSB}}/5 \). |
| \( \mathcal{T} \) | Test set | The five named falsification tests. |

---

## 3. Complete per-table results (as printed)

### 3.1 `dielPTAg005`

```
discrete_steps:           p=1         | Evidence for TSB: False
hysteresis:               p=0.4461    | Evidence for TSB: False
periodicity:              p=0         | Evidence for TSB: True
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=0.0004284 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: periodicity, anisotropy.

### 3.2 `dielPTAl005`

```
discrete_steps:           p=1         | Evidence for TSB: False
hysteresis:               p=0.4412    | Evidence for TSB: False
periodicity:              p=0         | Evidence for TSB: True
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=0.0006767 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: periodicity, anisotropy.

### 3.3 `dielPTBen_Au`

```
discrete_steps:           p=1.257e-13 | Evidence for TSB: True
hysteresis:               p=0.1145    | Evidence for TSB: False
periodicity:              p=0.1112    | Evidence for TSB: False
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=7.824e-05 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: discrete_steps, anisotropy.

### 3.4 `dielPTCyc_Au`

```
discrete_steps:           p=0         | Evidence for TSB: True
hysteresis:               p=0.1097    | Evidence for TSB: False
periodicity:              p=0.1843    | Evidence for TSB: False
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=7.161e-05 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: discrete_steps, anisotropy.

### 3.5 `dielPTGold005`

```
discrete_steps:           p=1         | Evidence for TSB: False
hysteresis:               p=0.4466    | Evidence for TSB: False
periodicity:              p=0         | Evidence for TSB: True
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=0.0004384 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: periodicity, anisotropy.

### 3.6 `dielPTLi005`

```
discrete_steps:           p=1         | Evidence for TSB: False
hysteresis:               p=0.4412    | Evidence for TSB: False
periodicity:              p=0         | Evidence for TSB: True
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=0.0002503 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: periodicity, anisotropy.

### 3.7 `dielPTOct_Au`

```
discrete_steps:           p=0         | Evidence for TSB: True
hysteresis:               p=0.103     | Evidence for TSB: False
periodicity:              p=0.2093    | Evidence for TSB: False
log_modulations:          p=0.4463    | Evidence for TSB: False
anisotropy_backreaction:  p=6.925e-05 | Evidence for TSB: True
```

\( S_{\mathrm{TSB}} = 2 \), \( f_{\mathrm{TSB}} = 0.40 \). Hits: discrete_steps, anisotropy.

---

## 4. Cross-table matrix

| Dataset | discrete_steps | hysteresis | periodicity | log_modulations | anisotropy_backreaction | \( S_{\mathrm{TSB}} \) |
|---|---|---|---|---|---|---|
| dielPTAg005 | F (p=1) | F (0.4461) | **T (0)** | F (0.4463) | **T (4.284e-4)** | 2 |
| dielPTAl005 | F (p=1) | F (0.4412) | **T (0)** | F (0.4463) | **T (6.767e-4)** | 2 |
| dielPTBen_Au | **T (1.257e-13)** | F (0.1145) | F (0.1112) | F (0.4463) | **T (7.824e-5)** | 2 |
| dielPTCyc_Au | **T (0)** | F (0.1097) | F (0.1843) | F (0.4463) | **T (7.161e-5)** | 2 |
| dielPTGold005 | F (p=1) | F (0.4466) | **T (0)** | F (0.4463) | **T (4.384e-4)** | 2 |
| dielPTLi005 | F (p=1) | F (0.4412) | **T (0)** | F (0.4463) | **T (2.503e-4)** | 2 |
| dielPTOct_Au | **T (0)** | F (0.103) | F (0.2093) | F (0.4463) | **T (6.925e-5)** | 2 |

Hit rates across the seven tables:

| Test | # True / 7 | Notes |
|---|---:|---|
| discrete_steps | 3 / 7 | Only the three molecular-on-Au tables |
| hysteresis | 0 / 7 | Two tight clusters, neither significant |
| periodicity | 4 / 7 | Only the four metal-005 tables, all at \( p = 0 \) |
| log_modulations | 0 / 7 | **Identical \( p = 0.4463 \) on every table** |
| anisotropy_backreaction | **7 / 7** | Strongest and only universal claim in this batch |

---

## 5. Pattern, not slogan

Two families, same score, different *which* tests fire.

### Family A — elemental metal 005 (`Ag`, `Al`, `Gold`, `Li`)

- Continuum dielectric: `discrete_steps` is maximally non-significant (\( p = 1 \)). That is what a smooth Drude / plasma / Lorentz \( \varepsilon(i\xi) \) is supposed to look like.
- `periodicity` is maximally significant (\( p = 0 \)). Either the Matsubara grid itself, a stored sampling cadence, or a real modulation in \( \varepsilon(i\xi) \) is being read as a period. Distinguishing those three is the next code-level check, not a physics conclusion.
- `hysteresis` sits in a narrow band \( p \in [0.4412,\,0.4466] \).
- Anisotropy is significant but weaker than Family B: \( p \in [2.50\times10^{-4},\,6.77\times10^{-4}] \).

### Family B — molecular fluid on gold (`Ben_Au`, `Cyc_Au`, `Oct_Au`)

- `discrete_steps` is extremely significant (\( p \le 1.257\times10^{-13} \), two of three at numerical zero). That is the expected direction if a multilayer / slab / oscillator-stack dielectric is closer to a piecewise or few-pole object than a smooth metal.
- `periodicity` does *not* fire (\( p \in [0.1112,\,0.2093] \)).
- `hysteresis` is lower than Family A but still above \( \alpha \): \( p \in [0.103,\,0.1145] \). Closest miss in the battery. A one-sided or higher-powered hysteresis test could flip these.
- Anisotropy is stronger than Family A by about 4–10×: \( p \in [6.93\times10^{-5},\,7.82\times10^{-5}] \).

### Universal

`anisotropy_backreaction` is True on every table. If that test is correctly specified (comparing auxiliary dielectric channels, or a constructed anisotropic kernel, against an isotropic null), this batch is a clean confirmation of *that one* TSB-coded signature in this Fig2 family. If the test is sensitive to any multi-column table regardless of physics, it is a specificity problem and needs a negative-control series (isotropic single-channel synthetic \( \varepsilon \), shuffled columns, or a pure Drude with identical auxiliary copies).

### Dead tests in this batch

- `log_modulations`: same p-value to four digits on seven independently hashed files. That is not a measurement. Treat as a loader / statistic bug until proven otherwise (frozen RNG, unused column, constant null distribution, or shared residual from a common preprocessing step).
- `hysteresis`: never crosses \( \alpha \). Family B is the only place it is even close.

---

## 6. What this does and does not say about TSB

**Does say (descriptive, this sample only):**

1. The engine did not produce a 5/5 “everything is TSB” sweep. Every table is 2/5. That is a mixed, structured outcome, which is more useful than a uniform pass or uniform fail.
2. The split tracks material class: metals → period + anisotropy; molecular-on-Au → steps + anisotropy.
3. Anisotropy is the only claim that survives the whole Fig2 `dielPT*` cut.
4. Raw-series hashes are distinct. The common `log_modulations` p-value is therefore not explained by “the same file loaded seven times.”

**Does not say:**

1. It does not establish that Casimir physics requires extra 3+1 domains, Mirron mirrors, or Tav harmonics. The tests are *named* for TSB signatures; their mapping onto those signatures is a modeling choice that still has to be written down as a likelihood, not a label.
2. \( p = 0 \) and \( p = 1 \) are numerical endpoints. They can come from a discrete null that is exactly saturated (grid period = sample period) or from a test that returns a sentinel. Until the statistic and the null are printed next to the p-value, treat those endpoints as “the test slammed into a wall,” not as infinite evidence.
3. This is one published-style dielectric family (`github_magnetic_fluid/Fig2`). It is not SPARC, not DESI, not CMS muons, not a global TSB confirmation.

---

## 7. Immediate follow-ups (compute, not narrate)

1. **Open `log_modulations`.** Print the raw statistic, degrees of freedom, and whether the same residual vector is reused. Target: a p-value that actually moves when \( \varepsilon_{\mathrm{pri}} \) is replaced by white noise or by a monotone Drude tail.
2. **Negative controls for anisotropy.** Duplicate `dielectric_response_primary` into every auxiliary column and rerun. If `anisotropy_backreaction` still fires, the test is not measuring anisotropy.
3. **Periodicity vs grid.** For Family A, compare the detected period to \( \Delta\xi \) of the stored Matsubara axis. If they match, the hit is sampling, not physics.
4. **Hysteresis power.** Family B is sitting at \( p \sim 0.11 \). Bootstrap the same series and report the interval, not just the point p.
5. **Pre-register the split.** The metal vs molecular-on-Au partition was read off this batch. The next Casimir folder should be scored *before* looking, with the same five tests and the same \( \alpha \).
6. **Keep the hashes.** Any later edit of a `dielPT*` file that changes SHA-256 is a different dataset; do not silently pool.

---

## 8. Session inventory

Queried / displayed in this session:

- Seven TAV ENGINE falsification reports (full p-values and booleans above).
- Seven SHA-256 raw-series integrity lines.
- Seven artifact path triples (png / json / txt) with stamps `20260915_224203`–`20260915_224211`.
- GitHub repo `George-Jumble/TauSuperblock`, path `Personal Files/`.
- Google Drive folder `Personal Files` (`1Q8kRH_SrMUM-aBtyIIVq2nHgZWh9SJnk`).

Local + project copies of this note:

- Workspace: `/home/workdir/artifacts/Personal Files/2026-09-15_TSB_Casimir_Falsification_dielPT_Fig2_session.md`
- Intended GitHub path: `Personal Files/2026-09-15_TSB_Casimir_Falsification_dielPT_Fig2_session.md` on `George-Jumble/TauSuperblock` (branch `main`)
- Intended Drive folder: Personal Files

---

*End of session note — 2026-09-15 TSB Casimir falsification, Fig2 dielPT family.*
