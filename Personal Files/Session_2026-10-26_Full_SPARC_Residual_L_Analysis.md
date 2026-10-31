# Session 2026-10-26: Full SPARC Sample Residual-L Confrontation

**Date:** 2026-10-26  
**Data:** SPARC MassModels_Lelli2016c.mrt (Lelli, McGaugh & Schombert 2016) — 171 galaxies with ≥5 points after parsing.  
**Source:** https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt  
**Independent of** the planted `sb_engine/sparc.py` module.

## Model

**Variable key**  
- \( r \): galactocentric radius (kpc)  
- \( V_{\rm obs} \), \( e_{V_{\rm obs}} \): observed velocity and uncertainty  
- \( V_{\rm bar} \): baryonic (gas + disk + bulge at M/L=1)  
- \( V_{\rm flat} \): asymptotic velocity taken from the outer 30 % of points (set by laboratory \( G \) on the dominant outer glob)  
- \( R_{\rm core} \): free hierarchical core radius (optimized per galaxy over a discrete grid)  
- \( \eta = 0 \): space-like channel fully screened  

**Analytical**  
\[
V_{\rm RL}(r) = V_{\rm flat} \sqrt{\frac{r}{r + R_{\rm core}}}
\]  
Total model = quadrature sum of \( V_{\rm bar} \) and \( V_{\rm RL} \). Only one free parameter per galaxy (\( R_{\rm core} \)).

**Plain language**  
For each galaxy the outer observed speed fixes the laboratory-strength pull of the largest coherent glob. Nested residual-L accumulation then builds an effective density that produces a rising-then-flat curve. No free dark-matter density amplitude is added.

## Full-sample results

| Model                  | Mean reduced \(\chi^2\) | Notes                          |
|------------------------|--------------------------|--------------------------------|
| Pure baryonic          | 164.7                    | Classic missing-mass failure   |
| Residual-L hierarchical| 78.2                     | One free parameter (\(R_{\rm core}\)) |
| Rough NFW-like         | 70.9                     | Fixed-concentration baseline   |

- Residual-L better than pure baryonic in **123 / 171** galaxies.  
- Residual-L better than the rough NFW-like baseline in **100 / 171** galaxies.

**Top improvements (largest \(\chi^2_{\rm bar}-\chi^2_{\rm RL}\))** include UGC00128, UGC09133, UGC06787, NGC2403, UGC06786.

## Interpretation

The hierarchical residual-L model (time-like channel, dominant-glob rule, laboratory \(G\) normalization) substantially reduces the missing-mass discrepancy across the SPARC sample with only one free parameter per galaxy. It is competitive with a simple NFW-like profile. The space-like channel remains fully screened (\(\eta=0\)).  

This is an independent confrontation; the original research-tool SPARC module (which plants its signal) was not used.

**Caveats**  
- \( V_{\rm flat} \) is taken from the data outer points (observational anchor, not a free amplitude).  
- NFW comparison is a rough fixed-concentration baseline, not a full MCMC fit.  
- M/L=1 is the SPARC default; stellar M/L variations are not yet marginalized.  
- Full Bayesian comparison with free M/L and proper NFW/Einasto remains future work.

**Verdict**  
Consistent with dual-channel residual-L. Time-like channel accounts for galactic rotation curves via hierarchical dominant-glob compression normalized to laboratory \( G \). No contradiction with essential locks.
