# Harmonic Binding Kit — DH_only unique-z n=9

**Run:** 28 Aug 2026 00:38  
**Action:** Harmonic Binding Detection Kit + residual diagnostics  
**Dataset:** DESI_DR2+LEGACY_DH_only_ALL_GCcomb_high_power  
**γ:** fixed 10 (`auto_calibrate_gamma=False`)

## Verdict

Null 1/7. That is the correct call on this vector.

| Claim | Result |
|---|---|
| Lomb peak at \(f=1/7\) | False |
| Detection bit | False |
| Harmonic-binding transitions | 0 |
| Alignment | null |
| 1/7 ladder significant | False |
| Statistical power stamp | LOW |
| Tau-SB extra vs poly baseline | \(\Delta\chi^2=0.58\) (not a detection) |

Compared with the 27 Aug 20:41 n=16 run (`peak=True`, \(p\approx0.021\), converted \(D_V\to D_H\) at \(z=0.106,0.15,0.295\)): the false-positive path is closed. Dedup + drop converted rows + AND-rule on the periodogram is doing what it should.

## Variable key

| Symbol | Meaning in this log |
|---|---|
| \(z\) | BAO effective redshift |
| \(D_H/r_d\) | Hubble distance / drag sound horizon (`DH_over_rs`) |
| \(n_\mathrm{raw}=20\) | stacked rows before unique-z |
| \(n_\mathrm{deduped}=9\) | after \(\lvert\Delta z\rvert\le 0.02\) |
| \(n_\mathrm{used}=9\) | rows actually fitted |
| \(\gamma=10\) | fixed cylinder stretch |
| \(\Delta s=8.809\) | s-span at that \(\gamma\) |
| \(\tau\)-cycles \(=1.26\) | \(\Delta s\) in units of the \(1/7\) period (engine count) |
| \(f=1/7\approx0.1429\) | target fundamental |
| \(f=0.2980\) | frequency of max Lomb power |
| ratio | \(\mathrm{power}(1/7)/\mathrm{power}_\max=0.169\) |
| \(\kappa\) | covariance condition number (317, unchanged after dedupe) |
| \(\lambda_\min\) | smallest eigenvalue \(1.02\times10^{-2}\) |
| \(\chi^2_\mathrm{poly}=6.13\) | quadratic baseline, dof=6, reduced 1.02 |
| \(\Delta\chi^2=0.58\) | Tau-SB template extra vs that baseline |
| \(r_d^\mathrm{TSB}=157.97\,\mathrm{Mpc}\) | framework prediction |
| \(r_d^\mathrm{obs}=147.09\,\mathrm{Mpc}\) | conventional drag scale used as “observed” |
| residual \(+7.40\%\) | \((157.97-147.09)/147.09\) |
| DW, SW, LB, BG | residual independence / normality checks |
| \(p_c\approx0.393\) | percolation placeholder |
| \(L_\mathrm{BEC}=5.5\,\mathrm{Mpc}\) | BEC coherence length (kit constant) |

## Data vector (unique-z, DH only)

| \(z\) | \(D_H/r_d\) | Note |
|---|---|---|
| 0.380 | 25.0978 | SDSS-style; not DESI DR2 BGS |
| 0.510 | 21.8629 | DESI LRG1 |
| 0.610 | 20.5948 | SDSS |
| 0.706 | 20.0787 | **value changed** vs prior DESI LRG2 19.4553 |
| 0.845 | 20.1570 | eBOSS ELG |
| 0.934 | 17.6415 | DESI LRG+ELG |
| 1.321 | 14.1760 | DESI ELG2 |
| 1.484 | 12.8170 | DESI QSO |
| 2.330 | 8.6315 | DESI Lyα |

Dropped vs the n=16 stack: converted \(D_V\) rows at 0.106, 0.15, 0.295 and the twin-z partners (0.698, 0.930, 1.317, 1.480, …). Good.

`[DATA MODE] ALL_GCcomb → 6 points` is the raw DESI ALL DH count. The kit then merges legacy and unique-z’s to 9. Those two lines are not a contradiction.

## Periodogram (AND-rule — correct this time)

Primary 1/7 track:

- power @ \(f=1/7\) = \(9.85\times10^{-2}\)
- max power = \(5.83\times10^{-1}\) at \(f=0.298\)
- ratio = 0.169
- bootstrap \(p\approx0.72\)
- peak=False, detection=False

Kit harmonics:

| Harmonic | \(f\) | Power | bootstrap \(p\) |
|---|---|---|---|
| 1 (1/7) | 0.1429 | 0.0624 | 0.81 |
| 2 | 0.2857 | 0.523 | 0.11 |
| 3 | 0.4286 | 0.516 | 0.10 |
| 4 | 0.5714 | 0.050 | 0.89 |
| 5 | 0.7143 | 0.365 | 0.27 |

Harmonics 2 and 3 sit near the max-power frequency \(\approx0.30\) and are still not significant. Do not promote “almost p=0.10 at h=2,3” into a ladder claim. \(n=9\), 1.26 cycles, and an unrebuilt cov make those p-values decorative.

## Mean model vs TSB add-on

Quadratic baseline: \(\chi^2=6.13\), reduced 1.02, 3 params, dof=6. That is a sane smooth \(D_H(z)/r_d\) fit.

Tau-SB extra: \(\Delta\chi^2=0.58\). No improvement worth talking about.

Sound-horizon line is a **parameter offset**, not a periodicity detection: TSB wants \(r_d=157.97\) Mpc vs 147.09 Mpc (\(+7.4\%\)). That is a scale mismatch you already know how to discuss; it is not a 1/7 peak.

## Residuals

Whitened ACF: lag1 \(-0.15\), lag2 \(-0.65\), lag3 \(+0.06\). Lag-2 looks large on \(n=9\); Ljung-Box and Breusch-Godfrey do not call it significant. Shapiro \(p=0.80\) (consistent with normal). DW \(=1.69\). Fine as “no smoking-gun residual structure,” not as proof of the template.

WHIM / web correlations all null (`whim_signature_detected=False`). 142857-cycle probe correctly skipped (\(\Delta s=8.81\ll10^6\)).

## Remaining problems (in priority order)

1. **\(n=9<12\) and \(\tau\)-cycles \(=1.26<2\).** Power stamp LOW is right. Do not add Joint_DH_DM or mixed quantities to inflate \(n\).

2. **Covariance not rebuilt after unique-z.** `rebuilt_after_dedupe=False`, \(\kappa_\mathrm{post}=\kappa_\mathrm{pre}=317\). Logger already says do not quote p-values. Rebuild \(C\) on the 9-vector before any bootstrap is treated as a number.

3. **\(z=0.706\) observable jumped** from 19.4553 (DESI LRG2 DH in the n=16 dump) to 20.0787. Dedup may have kept an SDSS row instead of DESI. Pin the survivor rule: prefer DESI DR2 measured DH when both exist.

4. **Binding-level \(z\) map vs data \(z\).** Kit puts almost every BAO point in `sub_quantum` (\(z\le2.06\)) and parks particle/atomic/web/gravitic above \(z\sim2\). Predicted transitions `[0.3, 0.687, …]` then return `Detected z: []`. That is a mapping/definition issue, not a non-detection of BAO wiggles. Document whether those \(z\) are redshift or a mapped hierarchy coordinate.

5. **ALL_GCcomb still selected first as 6 DH points**, then the high-power stack mutates the vector. Log one canonical `n_used` at the top so the two “6 points” lines stop looking like a load failure.

## What this run is allowed to say

Safe line:

> Unique-z DH-only stack, \(n=9\), fixed \(\gamma=10\), 1.26 \(\tau\)-cycles: 1/7 power ratio 0.17 vs max at \(f\approx0.30\), bootstrap \(p\approx0.72\), \(\Delta\chi^2_\mathrm{TSB}=0.58\). No transition, no 1/7 detection. Power LOW. Converted \(D_V\) rows removed.

Not allowed:

- “harmonic binding confirmed”
- “p=0.11 on harmonic 2 is a hint”
- quoting the n=16 \(p=0.021\) run as supporting evidence

## Next measurement that would actually change the call

- Rebuild unique-z covariance.
- Prefer DESI DH at overlapping \(z\).
- Stay DH_only.
- Either add **independent measured DH** bins (not converted DV) until \(n\ge12\) **and** \(\tau\)-cycles \(\ge2\), or stop scanning and publish the null with the current selection function.

Plots: `.../28-08-2026_00-38_tau_sb_desi/tau_sb_desi_scan__tau_sb_desi__summary_plot__08-28-2026_003840.png`  
Report: `.../28-08-2026_00-38_desi_legacy_dh_over_rs_tau_sb_desi/...report__08-28-2026_003840.json`
