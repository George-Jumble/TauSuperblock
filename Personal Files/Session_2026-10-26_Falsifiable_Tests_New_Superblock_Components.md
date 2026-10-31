# Session 2026-10-26: Falsifiable Tests to Add or Refine in the Research Tool Reflecting New Superblock Cosmology Components

**Date:** 2026-10-26  
**Framework:** Live Tau-Superblock / Superblock Cosmology (post dual-channel residual-L adoption, 2026-10-25)  
**Research tool:** George-Jumble/TauSuperblock `research_tool.py` (sb_engine modules: geometry, corpus, bounce, neutron, sparc, desi, cms, casimir)  
**Status:** Exploratory inventory of implementable, non-planted confrontations. Essential locks preserved (4D frame, Tau package hard-rejected, residual-L laboratory \(G\) match via dominant-glob, floor-only Dynamic Refresh + kinematic UPS, mass floor as protocol insertion, Casimir/virtuals as floor objects refused as dynamical sources of \(G\) or \(\rho_\Lambda\)).

## New Components Reflected (Live Corpus as of 2026-10-25)

1. **Dual-channel residual-L gravity**  
   - Time-like channel (\(+L_{\rm res}\)): propagates at \(c\), attractive compression toward the dominant-glob center of gravity; matches laboratory \(G\) under the dominant-glob rule.  
   - Space-like channel (\(-L_{\rm res}\) on \(\Sigma_{\rm now}\)): outward push deposited on the non-metric atemporal hard-wall circle \(C_{\rm atemp}\); phenomenological account of \(\rho_\Lambda\) with free efficiency \(\eta\).  
   Supersedes earlier DE attempts (entropic wall, empty-fraction, domain orbitals, virtual/Casimir sums).

2. **Hard wall as eternal conformal crossover**  
   Non-metric atemporal circle \(C_{\rm atemp}\) on which every hierarchy-relative slice \(\Sigma_p\) (level set of \(T_{\rm priv}^{(p)}\)) is simultaneous. Space-like residual deposits there; unbound bounce is the null circuit of this wall (residual \(L=0\)).

3. **Seventh phase \(\Phi_7\) as kinematic \(T_{\rm priv}\)**  
   Realized by the geometric point of simultaneity of every point; matched equal point in every co-located domain. Braided neutrino acts on Mirron fabric of \(\Phi_7\) to excite transient floor-level virtual bonding (organizational bookkeeping only; does not source residual-L or \(\rho_\Lambda\)).

4. **Six co-located domains**  
   Implies a \(6\times\) mass budget for objects that exist in every domain (e.g., black holes). Residual-L and unbound EM remain domain-local.

5. **Mass floor**  
   Protocol insertion (printed working floor \(\Delta = 309.3\) MeV neutron-dressing share, or legacy 313.1 MeV \(M_n/3\)); not derived. \(S_E/\hbar = 2\) invariant.

6. **Rotational dilution**  
   Domain-orbital kinetic density dilutes under expansion; fits DESI-type indications of diminishing Lambda (phenomenological, free coefficients).

## Falsifiable Tests to Add or Refine

All proposals avoid planting the signal they recover (current SPARC, CMS, Casimir modules generate synthetic data containing the recovered pattern; DESI residual is identically zero by \(\gamma\) calibration to \(\Delta N_{\rm plasma}=10.74\)). Prefer independent data loads, proper nulls, and free-parameter upper limits.

### 1. SPARC residual-L confrontation (refine existing `sparc` module)
**Target component:** Dual-channel residual-L, time-like channel matching laboratory \(G\) via hierarchical dominant-glob.  
**Current state:** `sparc.py` synthesizes NGC3198-like points with NFW “observed” and an emergent_dm theory that depends on \(\beta^2\) and phase; \(\chi^2\) is therefore not an independent test.  
**Proposed refinement:**  
- Load real SPARC rotation-curve points (or a fixed public subset).  
- Compute baryonic contribution only, then residual velocity after a residual-L (dominant-glob hierarchical) model normalized to laboratory \(G\).  
- Report residual \(\chi^2\) against pure baryonic, NFW, and residual-L baselines.  
- Optional free screening length for any space-like leakage; place upper limit from local/solar-system consistency.  

**Falsification:** Residual-L model underperforms standard baselines on independent curves after accounting for systematics; or an unscreened space-like term produces local repulsion excluded by EP tests.  

**Analytical:** Dominant-glob effective \(G_{\rm eff}\) is that of the largest coherent bound set whose residual angular momentum is dominant. Space-like push is localized to the wall and screened inside \(R_{\rm screen}\).  

**Plain language:** Check whether the gravity we measure in the lab, when applied to whole galaxies via the “strongest clump sets the pull” rule, actually explains the observed rotation curves without inventing extra dark-matter density, and without a repulsive push leaking into the Solar System.

### 2. DESI diminishing-Lambda / rotational-dilution scan (refine existing `desi` module)
**Target component:** Space-like residual-L phenomenological \(\rho_\Lambda\) with free \(\eta\); rotational decrease under expansion.  
**Current state:** `desi.py` forces residual \(\equiv 0\) by calibrating \(\gamma\) to the observed sound horizon.  
**Proposed refinement:**  
- Compare constant-\(\Lambda\) vs. a rotational-dilution model \(\rho_{\Lambda,{\rm eff}}(z) = \rho_{\Lambda,0} [1 - f_{\rm rot}(z)]\) where \(f_{\rm rot}\) is the fractional orbital kinetic density diluted by volume growth.  
- Use published DESI DR2 (or BAO) distance residuals; leave \(\eta\) and rotational fraction free.  
- Report \(\Delta\chi^2\) or evidence ratio.  

**Falsification:** Constant \(\Lambda\) preferred after the rotational piece is subtracted; or the required \(f_{\rm rot}\) exceeds the free phenomenological budget set by cluster velocity dispersions.  

**Analytical:** Sample energy ratio \(E_{\rm orb}/E_\Lambda \sim 10^{-5}\) (cluster \(\sigma_v\sim 1000\) km/s); residual dark-energy fraction \(\approx 1 -\) that percentage.  

**Plain language:** See whether the slow fade of dark-energy density that DESI hints at can be matched by the orbital energy of the six domains simply spreading out as the universe expands, without needing a new dynamical field.

### 3. Precision gravity / equivalence-principle screening bound (new module or extension)
**Target component:** Dual-channel; space-like push must not disturb laboratory \(G\).  
**Proposed addition:**  
- Confront MICROSCOPE, Eöt-Wash, or lunar laser ranging bounds on composition-dependent acceleration or fifth-force strength.  
- Map free \(\eta\) and screening length \(R_{\rm screen}\) to the excluded parameter region.  
- Residual-L time-like channel remains universal (no EP violation).  

**Falsification:** Best-fit space-like efficiency that matches cosmological \(\rho_\Lambda\) predicts a local EP violation already excluded.  

**Analytical:** Screened force \(\delta a / a \propto \eta \exp(-r/R_{\rm screen})\).  

**Plain language:** If the outward push that accounts for cosmic acceleration also operates near Earth, it would make different materials fall at slightly different rates; existing experiments already limit how strong or how long-range that push can be.

### 4. High-redshift black-hole mass budget (new module)
**Target component:** Six co-located domains \(\Rightarrow 6\times\) mass available for objects present in every domain.  
**Proposed addition:**  
- Take published JWST overmassive high-\(z\) black-hole candidates.  
- Compare inferred mass against single-domain seed expectations versus a \(6\times\) co-located budget (black hole is a black hole in each domain).  
- Report tension reduction.  

**Falsification:** Even the \(6\times\) factor leaves the most extreme objects unexplained, or the factor over-produces local black-hole mass density.  

**Plain language:** Early galaxies appear to host black holes too heavy for the time available if only one copy of the universe exists; having six co-located copies supplies six times the mass reservoir and may ease the tension.

### 5. Neutron lifetime / braided-neutrino appearance (refine existing `neutron` module)
**Target component:** \(\Phi_7 = T_{\rm priv}\) braided neutrino exciting floor virtual bonding; domain-cross.  
**Current state:** HOLD status; J-PARC 877.2 s already fails \(s=0\) appearance for the derived BR.  
**Proposed refinement:**  
- Keep the independent lifetime comparison.  
- Add a null for any residual phase-dependent rate modulation at the 1/7 or 1/6 tick that would be expected if the braided neutrino coupled dynamically (currently organizational only).  

**Falsification:** Appearance signal at the level required by the old BR, or a periodic modulation excluded by beam and bottle data.  

**Plain language:** The neutron’s lifetime is already a clean test of whether an extra “hidden domain” decay channel exists; we can also look for any tiny rhythmic variation that a dynamical seventh-phase neutrino would produce.

### 6. Unbound-bounce residual-\(L=0\) consistency (refine `bounce` and `geometry`)
**Target component:** Unbound bounce = null circuit of the non-metric hard wall; residual \(L=0\) for completed P\(\leftrightarrow\)F bounces.  
**Proposed refinement:**  
- Assert in the geometry snapshot that photon world-tubes carry zero residual angular momentum.  
- Cross-check against precision tests of photon mass or long-range EM deviations (existing nulls).  

**Falsification:** Any positive photon mass or residual-L signature for free electromagnetic waves.  

**Analytical:** Residual \(L\) arises only when the rebound toward Absolute Future is stopped at the Present. Unbound completion \(\Rightarrow L=0\).  

**Plain language:** Light that finishes its full bounce between past and future should leave no leftover spin that could source gravity; any measured photon mass would contradict that.

### 7. Corpus and constants update (refine `corpus` and `constants.py`)
**Target:** Reflect live locks.  
- Replace legacy \(\Delta=313.1\) MeV with printed working floor 309.3 MeV (or keep both as protocol variants).  
- Explicitly mark \(N_{\rm HIER}\) as Superblock binding depth, not \(\log_7(\tau/\lambda)\).  
- Add dual-channel and non-metric wall statements to the IN ledger.  
- Remove any residual Tau-cylinder language.  

No direct falsification; ensures the tool does not reintroduce rejected packages.

### 8. Casimir shape tests remain floor-only (refine `casimir`)
**Target component:** Author cut — Casimir/virtuals are floor objects, refused as sources of laboratory \(G\) or \(\rho_\Lambda\).  
**Proposed refinement:**  
- Keep impedance/shape battery.  
- Explicitly report that any 1/7 harmonic is a planted-scanner result, not a detection.  
- Add a null comparison against ordinary Lifshitz theory without hierarchical modulation.  

**Falsification:** None required; the cut already forbids promotion to a dynamical source. A genuine independent 1/7 signal would be noted as floor phenomenology only.

## Summary Table of Priorities

| Priority | Module          | New Component Reflected                  | Planting Risk | Data Independence |
|----------|-----------------|------------------------------------------|---------------|-------------------|
| High     | sparc           | Dual-channel residual-L (time-like)     | High (remove)| Medium            |
| High     | desi            | Space-like \(\rho_\Lambda\) + dilution  | High (remove)| High              |
| Medium   | new (EP)        | Screening of space-like channel         | Low           | High              |
| Medium   | new (high-z BH) | 6× co-located mass budget               | Low           | High              |
| Medium   | neutron         | \(\Phi_7\) braided neutrino             | Low           | High              |
| Low      | bounce/geometry | Unbound null circuit, \(L=0\)           | Low           | Low (consistency) |
| Low      | casimir/corpus  | Floor cut + live locks                  | Medium        | N/A               |

All tests remain compatible with essential locks. Free parameters (\(\eta\), screening length, rotational fraction) are to be bounded, not fitted to zero residual by construction.

**File generated:** 2026-10-26  
**Related prior sessions:** Session_2026-10-24_Falsifiable_Tests_Available_Now.md; Session_2026-10-25_Dual_Channel_Gravity_Adopted_Live_Corpus_Supersedes_Earlier_DE.md
