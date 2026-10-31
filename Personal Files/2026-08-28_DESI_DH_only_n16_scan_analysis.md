# Tau-SB DESI DH_only n=16 scan — analysis

**Run stamp:** 27 Aug 2026 20:41  
**Dataset:** DESI_DR2+LEGACY_DH_only_ALL_GCcomb_high_power  
**Action:** Periodicity Scan (1/7 Tracks)  
**Source log:** pasted 2026-08-28

## Verdict

Do not post this as a 1/7 detection.

- Lomb power at \(f=1/7\) is \(5.88\times 10^{-8}\).
- Periodogram max is \(4.42\times 10^{-4}\) at \(f=0.5\) (Nyquist), ratio \(\approx 7520\).
- `Lomb-Scargle peak=True` is firing on bootstrap \(p\approx 0.021\), not on “1/7 is the dominant mode.”
- `peaks=[7]` is not the \(\tau=1/7\) fundamental.
- Low-z “DH” rows at \(z=0.106, 0.15, 0.295\) are converted \(D_V\to\) fiducial-\(\alpha\) \(D_H\), not measured \(D_H/r_d\).
- Geometry \(\mu\)-prior is dead: \(\chi^2=7220\), reduced \(\chi^2=481\).

## Variable / function key

| Symbol | Meaning |
|---|---|
| \(z\) | effective redshift of the BAO bin |
| \(r_d\) | drag-epoch sound horizon |
| \(D_H(z)=c/H(z)\) | Hubble distance |
| \(D_M(z)\) | transverse comoving distance |
| \(D_V(z)=(z\,D_M^2 D_H)^{1/3}\) | isotropic BAO distance |
| \(D_H/r_d\), `DH_over_rs` | line-of-sight BAO observable |
| \(D_V/r_d\), `DV_over_rs` | isotropic BAO observable |
| \(\alpha\) | BAO scale dilation vs a fiducial cosmology |
| \(\gamma\) | Tau-SB cylinder stretch (fixed at 10 in this run) |
| \(s\) | scan coordinate after \(\gamma\)-stretch; \(\Delta s=11.022\) here |
| \(\tau=1/7\) | framework period (fixed, not fitted) |
| \(\tau\)-cycles | \(\Delta s / (7)\) in the engine’s cycle count; logged as 1.57 |
| \(f\) | Lomb–Scargle frequency in the engine’s \(s\)-space units |
| \(f=1/7\) | target Tav track |
| \(f=0.5\) | Nyquist bin where max power landed |
| \(n\) | length of the stacked data vector (16) |
| \(n_\mathrm{freq}\) | requested frequency grid size (1000); bootstrap used `n_freq_bins=50` |
| \(\kappa\) | covariance condition number (\(\approx 317\)) |
| \(\lambda_\min\) | smallest covariance eigenvalue (\(1.02\times 10^{-2}\)) |
| \(\chi^2\), red. \(\chi^2\) | geometry \(\mu\)-prior fit to the DH stack |
| \(M_0=313.1\,\mathrm{MeV}\) | fixed framework mass scale |
| \(n_\mathrm{hier}\approx 45.8\) | fixed hierarchy count |
| `dedupe_z_tol=0.0` | no redshift collapsing; near-duplicate bins kept |

## Data vector (as logged)

| \(z\) | obs \(D_H/r_d\) | provenance (from source-file list + z) |
|---|---|---|
| 0.106 | 27.6025 | Beutler+2011 \(r_s/D_V\) → converted DH |
| 0.150 | 29.0731 | Ross+2015 \(D_V/r_d\) → converted DH |
| 0.295 | 25.5505 | DESI BGS \(D_V/r_d=7.9417\) → fiducial-\(\alpha\) DH |
| 0.380 | 25.0978 | SDSS DR12-style |
| 0.510 | 21.8629 | DESI LRG1 measured DH |
| 0.610 | 20.5948 | SDSS |
| 0.698 | 19.3258 | near-dup of 0.706 |
| 0.706 | 19.4553 | DESI LRG2 measured DH |
| 0.845 | 20.1570 | eBOSS ELG FSBAO MAP |
| 0.930 | 17.8761 | near-dup of 0.934 |
| 0.934 | 17.6415 | DESI LRG+ELG measured DH |
| 1.317 | 13.8237 | near-dup of 1.321 |
| 1.321 | 14.1760 | DESI ELG2 measured DH |
| 1.480 | 13.2609 | near-dup of 1.484 |
| 1.484 | 12.8170 | DESI QSO measured DH |
| 2.330 | 8.6315 | DESI Lyα measured DH |

Measured DESI DR2 DH rows that are real: \(z=0.510, 0.706, 0.934, 1.321, 1.484, 2.330\) (and possibly the ALL_GCcomb mix). BGS at 0.295 is **not** a measured DH.

## Why this relates to the earlier BGS crash

`mode='DH_only'` on tracer `BGS_BRIGHT-21.35_GCcomb` alone correctly finds no `DH_over_rs` in the Cobaya mean file.

This stack does not use that tracer file. It uses `ALL_GCcomb` + a **legacy high-power converter** that invents DH from isotropic \(D_V\) via fiducial \(\alpha\). That is why \(z=0.295\) appears here as `DH_over_rs obs=25.5505`.

That conversion assumes a fiducial \(F_\mathrm{AP}=D_M/D_H\). It can imprint low-z wiggles that a 1/7 scanner will happily eat.

## Detection predicate (must change)

Current implied rule:

```
peak = True  if  bootstrap_p(f=1/7) < 0.05
```

Required rule:

```
peak = True  iff
  argmax_f power(f) is within one bin of f_target=1/7
  AND power(1/7) / power_max >= threshold (e.g. 0.5)
  AND bootstrap_p(1/7) < alpha
  AND τ-cycles >= 2
  AND no converted-DV rows in a DH_only vector
```

On this run: first condition fails. Stop.

## Immediate code / analysis actions

1. Dedup pairs: 0.698/0.706, 0.930/0.934, 1.317/1.321, 1.480/1.484 (`dedupe_z_tol` ~ 0.01–0.02).
2. Drop converted DV rows from any `DH_only` vector (0.106, 0.15, 0.295). Keep them only in `DV_only` or a explicitly labeled `converted_DH` mode.
3. Fix `Lomb-Scargle peak=True`.
4. Keep \(\gamma=10\) fixed until \(\tau\)-cycles \(\gtrsim 2\).
5. Do not treat `peaks=[7]` as \(\tau\) confirmation without documenting the index convention.
6. Geometry \(\mu\)-prior \(\chi^2=7220\) means the distance template is not describing this stack; periodicity on those residuals is not a cosmology test until the mean model is sane.

## Plot / report paths (on the research machine)

- Plot: `.../artifacts/tau_sb_desi_scan/27-08-2026_20-41_tau_sb_desi/tau_sb_desi_scan__tau_sb_desi__summary_plot__08-27-2026_204127.png`
- Report: `.../artifacts/tau_sb_desi_scan/27-08-2026_20-41_desi_legacy_dh_over_rs_tau_sb_desi/tau_sb_desi_scan__desi_legacy_dh_over_rs_tau_sb_desi__report__08-27-2026_204127.json`
