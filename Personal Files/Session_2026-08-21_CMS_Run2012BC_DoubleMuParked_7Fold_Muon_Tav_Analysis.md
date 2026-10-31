# Session 2026-08-21: CMS Run2012BC DoubleMuParked 7-Fold Muon Tav Analysis

**Date**: 2026-08-21  
**Framework**: Unified Tav-Superblock Cosmology (TSB / UTSC)  
**Data**: CMS Open Data Run2012BC DoubleMuParked (nanoAOD-style muon branches)  
**Sample**: 50,000 / 61,540,413 events  
**Anchor**: \( M_0 = 313.1 \) MeV  
**Report timestamp**: 08-21-2026_023009

---

## 1. Headline Results

| Channel | Verdict | Key numbers |
|---------|---------|-------------|
| Global | **STRONG 7-FOLD (pT + multiplicity)** | Engine score σ = 12.00 (raw 62.27, capped) |
| Muon pT | SUBHARMONIC HINT | Subharmonic excess ≈ 35.60× |
| Multiplicity | EXPLORATORY_PERIODOGRAM_HINT / 7-FOLD SIGNATURE (periodogram) | 176 harmonic hits; subharmonic excess ≈ 3.18 |
| Classification | EXPLORATORY_PIPELINE_ANOMALY — **not a discovery claim** | Explicitly not Cowan et al. HEP significance |

**Complete key**  
- \( M_0 = 313.1 \) MeV: geometric friction / conformal mass-gap floor used as analysis anchor.  
- Engine score: internal pipeline metric (capped at 12); not a likelihood-ratio significance.  
- Subharmonic excess: ratio of power at subharmonic bins relative to a reference continuum estimate.

---

## 2. Critical Null-Hypothesis Issue

The multiplicity distribution in residue classes mod 7 is **strongly peaked at residue 2** (fraction ≈ 0.497).  

This is **expected** under a dimuon trigger: the dominant topology is \( n_\mu \approx 2 \), so \( n_\mu \bmod 7 = 2 \).

- \(\chi^2\) vs uniform 1/7 null: 62 036 (enormous, as expected)  
- \(\chi^2\) vs trigger-aware null (empirical \( P(n_\mu) \)): \( 2.45 \times 10^{-27} \) (fully consistent)

**Null hypothesis warning (from the report itself)**  
> Uniform 1/7 null is incorrect for DoubleMu-triggered samples; residue-2 dominance follows from \( n_\mu \approx 2 \) under dimuon trigger.  
> Recommended null: `trigger_aware_from_empirical_P_n_muon`.

Any claim of a 7-fold anomaly in the multiplicity fractions must therefore be evaluated exclusively against the trigger-aware expectation. Against that null the fractions show no significant deviation.

---

## 3. Periodogram Behaviour

Despite the trigger-aware consistency of the residue fractions, the cumulative periodogram on the multiplicity time series (or event-ordered sequence) still reports:

- 176 harmonic hits (many near phase 0 relative to the 1/7 grid),
- subharmonic excess ≈ 3.18,
- verdict “7-FOLD SIGNATURE” in the periodogram section.

The pT spectrum yields a stronger subharmonic excess (≈ 35.6×) but with far fewer points (28 bins), producing only a “SUBHARMONIC HINT”.

These periodogram features drive the global “STRONG 7-FOLD” label, but remain inside the exploratory classification.

---

## 4. Relation to Prior ATLAS Result and Framework Status

The language and structure closely parallel the earlier ATLAS Open Data 2lep (data_A) analysis (STRONG 7-FOLD, engine score 12, exploratory, \( M_0 = 313.1 \) MeV).  

In the light of:

- the dual-threshold Casimir non-detection of the primary hierarchical 7-cycle,
- the recognition that Casimir radiation is unbound EM (so hierarchical 7 Mpc / \( n_{\rm hier} \) scales are irrelevant),
- the requirement that any residual Tau resonance must sit at **specific** frequencies fixed by the order-6 cycle,

this CMS result should be treated as another **exploratory pipeline anomaly**. It does not yet constitute independent confirmation of a physical 7-cycle in the unbound or bound sectors. The trigger-aware null already removes the most obvious multiplicity anomaly; the residual periodogram power requires a pre-registered, frequency-specific, power-calibrated test before it can be interpreted as support for the framework.

---

## 5. Plot Summary (attached)

- **A.** Muon \( p_T \) spectrum (steeply falling, standard).  
- **B.** \( p_T \) periodogram showing elevated low-bin power (subharmonic hint).  
- **C.** Multiplicity fractions mod 7 — clear residue-2 peak consistent with dimuon trigger (dashed line at uniform 1/7).  
- **D.** Text summary matching the numerical verdicts above.

---

## 6. Recommended Next Steps (consistent with infinite-circle / unbound discipline)

1. Re-run the multiplicity periodogram under a strictly trigger-aware null construction and with pre-registered frequency bins corresponding to the pure order-6 / 142857 grid.  
2. Quantify power against residual amplitudes of the size expected from a pure group-theoretic modulation.  
3. Apply the same dual-threshold / calibrated-FPR discipline developed for the Casimir dielectric series.  
4. Treat any surviving excess as a residual candidate only; do not elevate it to “support” until the above controls are satisfied.

---

*Terminology locked: Mirron, residual-L gravity, unbound EM (\( L = 0 \)), bound EM (\( L \neq 0 \)), \( S^1_\phi \), order-6 / 142857 / 1-4-2-8-5-7 cycle, Topological Exclusion Principle, 8-phase \( G_2 \) clockwork, \( \Delta_{\rm Tav} \approx 313.1 \) MeV.*
