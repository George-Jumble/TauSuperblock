# Session 2026-08-28: Reading of the Planck CMB Residual FFT Plot

**Date**: 2026-08-28  
**Plot**: `planck_cmb__planck_cmb_tav_full__fft__08-28-2026_101115.png`

---

## What the two panels show

**Top panel — \(D_\ell\) residuals (smooth ΛCDM proxy removed)**  
- Residual amplitude is large at low \(\ell\) (\(\sim 10^{-10}\) scale on the plotted units) and decays toward \(\ell \sim 1000\)–\(2000\).  
- This is the expected shape after subtracting a *smooth* proxy: leftover acoustic-peak structure, cosmic variance, and mask/foreground residuals all concentrate at low \(\ell\).  
- The residual definition is now explicit: **smooth ΛCDM proxy**, not the official Planck best-fit \(D_\ell^{\Lambda\mathrm{CDM}}\) with the published covariance. A smooth proxy leaves more of the acoustic comb in the residual than a proper theory spectrum would.

**Bottom panel — FFT of those residuals**  
- The transform is a dense, noisy forest of peaks across the full frequency-mode axis (0–2000).  
- Cyan dashed vertical lines mark the engine’s 7-fold search locations.  
- Many of those lines do **not** coincide with the tallest peaks. Several sit on ordinary fluctuations in a spectrum that is elevated almost everywhere.  
- There is no visually dominant, isolated harmonic series standing above a quiet continuum. The plot looks like broadband residual power, not a clean 7-fold comb.

---

## Interpretation

The engine’s “7-fold periodic structure detected” label is being applied to a noisy FFT of residuals from a **smooth** (not full-physics) ΛCDM subtraction. In that setting:

- leftover acoustic-peak periodicity is expected,
- look-elsewhere is severe (many modes, many dashed lines),
- the marked 7-fold locations are not uniquely outstanding.

This is consistent with an exploratory pipeline flag, not with a specific-frequency detection of the order-6 / 142857 structure.

The 313.1 MeV anchor remains an input of the theory. Nothing in this plot measures that energy scale from the CMB.

---

## Complete key

- \(D_\ell\): \(\ell(\ell+1)C_\ell/2\pi\).  
- Smooth ΛCDM proxy: a smoothed baseline, not the official Planck best-fit spectrum.  
- FFT frequency mode: discrete Fourier index of the residual series versus \(\ell\).  
- Cyan lines: engine-chosen 7-fold search positions.  
- Unbound EM: CMB photons; residual \(L=0\).

---

*Terminology locked: Mirron, unbound EM, bound EM, \(S^1_\phi\), order-6 / 142857 cycle, \(\Delta_{\rm Tav}\approx 313.1\) MeV.*
