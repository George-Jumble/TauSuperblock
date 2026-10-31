# Session 2026-08-20: Why the Original 7-Cycle Test Failed Even If Excess Appeared Near the Correct Frequency

**Date**: 2026-08-20  
**Framework**: Unified Tav-Superblock Cosmology (TSB / UTSC)  
**Query**: “But why did it fail under the original framework, if it was detected in the correct frequency range?”

---

## Direct Answer

Even under the original hierarchical framework, and even if some excess power sat near the theoretically interesting 1/7 (or order-6) frequency, the dual-threshold campaign still returned a non-detection because the early “detections” were not robust. They failed the stricter, calibrated protocol for three concrete reasons.

### 1. Inadequate statistical control in the early batteries

The earlier analyses that reported “tav-resonance 1/7 detected = True” across the seven dielectric series suffered from a documented pathology: near-100 % false-positive rates on pure-decay nulls.  

That means the statistic being used was capable of declaring a detection on pure noise (or on smooth Lifshitz + realistic experimental noise) far too often. When a later protocol was constructed that explicitly calibrated the null distribution and enforced a maximum false-positive rate ≤ 0.04, most of those earlier excesses were revealed as artefacts.  

Sitting near the “correct” frequency does not protect a peak if the threshold itself was uncalibrated.

### 2. Power-ratio + matched-filter is stricter than a simple periodogram excess

The dual-threshold gate required **both**:

- a primary power-ratio > 0.55 at the target frequency (after trend removal), **and**
- a secondary matched-filter score > 0.105,

while holding the false-positive rate to ≤ 0.04.

A simple periodogram can show elevated power in a bin that happens to lie near 1/7. A matched filter that templates the exact expected waveform (including any hierarchical envelope the original theory predicted) can reject a peak that does not match the full shape or that is not sufficiently elevated after proper background subtraction.  

The residual power that remained after trend removal and matched filtering simply did not clear both calibrated thresholds simultaneously.

### 3. Trend removal and pre-processing differences

Hierarchical claims are sensitive to how the smooth continuum background is removed. Different choices of polynomial order, filter width, or Savitzky-Golay parameters can move, suppress, or artificially enhance residual peaks.  

The dual-threshold campaign used a more controlled and reproducible trend-removal procedure. Once that procedure was applied uniformly, the excess at the target frequency dropped below the pre-set gates on every material series.

### Secondary features that survived are not the primary 7-cycle claim

The dual-threshold result left some weaker residuals (anisotropy_backreaction across materials, discrete steps on certain Au-organics). Those features are less specific: they can be produced by ordinary dielectric physics, surface effects, or residual trend-removal artefacts. They do not constitute a clean, frequency-locked 7-cycle resonance of the kind the original tool claimed, and elevating them after the primary signature failed would be moving the goalposts.

---

## Summary table

| Aspect | Early “detected = True” batteries | Dual-threshold campaign | Consequence |
|--------|-----------------------------------|--------------------------|-------------|
| Null calibration | High / near-100 % FPR on pure-decay nulls | Explicitly controlled, max FPR ≤ 0.04 | Early excesses largely artefacts |
| Detection statistic | Periodogram excess (more permissive) | Power-ratio **and** matched-filter (stricter) | Residual power failed both gates |
| Trend removal | Variable / less controlled | Uniform, reproducible procedure | Target-frequency excess reduced |
| Frequency specificity | Excess near 1/7 counted | Exact target + waveform match required | “Near” was not enough |
| Surviving residuals | — | Weaker, less specific (anisotropy, some steps) | Do not rescue the primary 7-cycle claim |

---

## Bottom line under the original framework

The original positive claims did not survive a properly calibrated, frequency-specific, dual-threshold test. Even if some power happened to lie near the theoretically interesting frequency, it was neither strong enough nor clean enough (after trend removal and matched filtering) to pass gates that kept the false-positive rate under control.  

That is why the test failed under the original framework itself: the earlier detections were not robust to improved statistical hygiene.

---

## Complete key

- Dual-threshold protocol: primary power-ratio gate 0.55 + secondary matched-filter threshold 0.105, max FPR ≤ 0.04.  
- Early pathology: near-100 % false-positive rates on pure-decay nulls.  
- Target frequencies: those fixed by the 1/7 / order-6 / 142857 cycle.  
- Matched filter: templates the expected waveform (including any hierarchical envelope claimed by the original theory).  
- Residual features that survived: anisotropy and discrete steps on some materials — less specific than a clean 7-cycle resonance.

---

*Terminology locked: Mirron, residual-L gravity, unbound EM (\(L=0\)), bound EM (\(L\neq0\)), \(S^1_\phi\), order-6 / 142857 cycle, Topological Exclusion Principle, 8-phase \(G_2\) clockwork.*
