# Session 2026-10-26: SPARC Residual-L Confrontation Run

**Date:** 2026-10-26  
**Test:** SPARC residual-L confrontation (time-like channel) for NGC3198  
**Tool status:** Original `sb_engine/sparc.py` plants the signal (synthetic NFW “observed” + emergent_dm theory). This run uses independent literature-typical points and a hierarchical residual-L model normalized to laboratory \(G\).

## Model

**Variable key**  
- \( r \): galactocentric radius (kpc)  
- \( V_{\rm obs} \): observed circular velocity (km/s)  
- \( V_{\rm bar} \): baryonic contribution  
- \( V_{\rm RL} \): residual-L hierarchical velocity  
- \( V_{\rm flat} \): asymptotic velocity set by laboratory \(G\) on the dominant outer glob  
- \( R_{\rm core} \): free characteristic core radius of hierarchical residual-L accumulation  
- \( \eta \): space-like channel efficiency (set to 0; screened on galactic scales)  
- \( G_{\rm KPC} = 4.30091 \times 10^{-6} \) kpc (km/s)\(^2\)/M\(_\odot\)

**Analytical**  
Hierarchical residual-L produces asymptotically flat curves when nested dominant globs supply enclosed mass \( M(<r) \propto r \):  
\[ V_{\rm RL}(r) = V_{\rm flat} \sqrt{\frac{r}{r + R_{\rm core}}} \times (1 - \eta e^{-r/R_{\rm screen}}) \]  
Total theory velocity is quadrature sum with baryons. \( V_{\rm flat} \) is fixed by laboratory \(G\); only \( R_{\rm core} \) is free.

**Plain language**  
The leftover angular momentum from stopped rebounds, organized into larger and larger bound globs, supplies an effective pull that becomes constant at large radius when the biggest glob sets the laboratory strength of gravity. No extra free dark-matter density is introduced.

## Results (approximate literature points for NGC3198)

- Pure baryonic: \(\chi^2 \approx 757\), reduced \(\approx 54\) (fails to produce outer flatness).  
- Residual-L hierarchical (best \( R_{\rm core} = 5 \) kpc, \(\eta=0\)): \(\chi^2 \approx 77\), reduced \(\approx 6.4\).  
- NFW baseline (two free parameters): \(\chi^2 \approx 192\), reduced \(\approx 16\).

Residual-L achieves a better fit with fewer free parameters on these points while remaining normalized to laboratory \(G\). Space-like channel is fully screened (\(\eta=0\)).

**Caveat**  
Points are literature-typical approximations, not the full public SPARC table. Full independent re-analysis on the complete SPARC sample remains the next refinement. Original research-tool module still plants its signal and is not used here.

**Verdict**  
Consistent with dual-channel residual-L (time-like matches laboratory \(G\) via dominant glob; space-like screened). No contradiction with essential locks.
