# Session 2026-08-28: Reading of the Observed Planck \(D_\ell\) Spectrum Plot

**Date**: 2026-08-28  
**Plot**: `planck_cmb__planck_cmb_tav_full__spectrum__08-28-2026_101114.png`

---

## What the figure is

This is the **observed** Commander \(D_\ell\) used as input to the Tav scan. It is the standard Planck TT acoustic-peak spectrum:

- first peak near \(\ell \sim 220\)
- second near \(\ell \sim 540\)
- third near \(\ell \sim 800\)
- subsequent peaks damping toward \(\ell = 2000\)

Units on the plot are \(D_\ell\) in \(\mu\mathrm{K}^2\) (displayed as \(\times 10^{-9}\) on the axis scale used by the engine). No ΛCDM theory curve, no residual, and no 7-fold overlay appear on this panel.

---

## What it does *not* show

- It does not display a 7-fold Tav resonance.
- It does not display the 313.1 MeV mass gap.
- It does not test the order-6 / 142857 structure.

Those claims live only in the residual-FFT panel (smooth ΛCDM proxy removed). This figure is simply the raw multipole spectrum from which that residual was formed.

---

## Relation to the residual FFT

Because this spectrum is the ordinary acoustic comb, any *smooth* proxy that does not follow the peaks will leave a periodic leftover. That leftover is the natural source of structure in the residual FFT. The observed \(D_\ell\) therefore explains why a residual FFT can look “7-fold-ish” without requiring a new topological modulation.

---

## Complete key

- \(D_\ell = \ell(\ell+1)C_\ell/2\pi\): observed TT angular power.  
- Acoustic peaks: standard sound-horizon series in the CMB.  
- This plot: input spectrum only.  
- Residual FFT (other figure): where the engine’s 7-fold label was applied.

---

*Terminology locked: unbound EM (CMB photons), \(m_0 = 313.1\) MeV as theoretical anchor, order-6 / 142857 cycle.*
