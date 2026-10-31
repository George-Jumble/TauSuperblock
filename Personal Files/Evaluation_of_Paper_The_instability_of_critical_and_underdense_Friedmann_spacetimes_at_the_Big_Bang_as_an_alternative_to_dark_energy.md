# Evaluation of the Paper: "The instability of critical and underdense Friedmann spacetimes at the Big Bang as an alternative to dark energy"

**DOI**: 10.1098/rspa.2025.0912  
**Journal**: Proceedings of the Royal Society A, Volume 482, Issue 2338, Article 20250912 (published online 27 May 2026)  
**Authors**: C. Alexander (University College London), B. Temple and Z. Vogler (University of California, Davis)  
**Date of Evaluation**: 15 July 2026 (in context of Tau-Superblock Universe Project session)  
**Related Framework Context**: This evaluation is performed within the ongoing development of the Unified Tav-Superblock Cosmology (TSC), which provides a geometric 5D Kaluza-Klein + octonionic multi-domain alternative to standard ΛCDM, including claims of explaining anomalous acceleration without a cosmological constant via centrifugal rotation of the 6-domain supersphere, Casimir pressure from the macroscopic τ-circle (τ ≈ 7 h⁻¹ Mpc), and wavefunction dispersion redshift. The paper offers a conservative (within GR + dust) alternative mechanism based on Big Bang instabilities.

**Download Link**: [Active Download - Evaluation_of_Paper_The_instability_of_critical_and_underdense_Friedmann_spacetimes_at_the_Big_Bang_as_an_alternative_to_dark_energy.md](/home/workdir/artifacts/personal_files/Evaluation_of_Paper_The_instability_of_critical_and_underdense_Friedmann_spacetimes_at_the_Big_Bang_as_an_alternative_to_dark_energy.md)  
*(Right-click or tap to download the full markdown session log immediately from the chat interface. All prior Tau-Superblock .md and .tex files are also available in this Personal Files folder.)*

---

## 1. Summary of the Paper

**Full Title**: The instability of critical and underdense Friedmann spacetimes at the Big Bang as an alternative to dark energy.

**Abstract** (verbatim key excerpt):  
"We characterize the local instability of pressureless Friedmann spacetimes to radial perturbation at the Big Bang. The analysis is based on a formulation of the Einstein–Euler equations in self-similar variables (t, ξ), with ξ = r/t, conceived to realize the critical (k = 0) Friedmann spacetime as a stationary solution whose character as an unstable saddle rest point S_M is determined via an expansion of smooth solutions in even powers of ξ. ... We prove that all solutions smooth at the centre of symmetry agree with a Friedmann spacetime at leading order in ξ, and with an eye toward cosmology, we focus on F, the set of solutions which agree with a k < 0 Friedmann spacetime at leading order, providing the maximal family into which generic underdense radial perturbations of the unstable critical Friedmann spacetime will evolve. We prove solutions in F generically accelerate away from Friedmann spacetimes at intermediate times but decay back to the same leading-order Friedmann spacetime asymptotically as t → ∞. Thus instabilities inherent in the Einstein–Euler equations provide a natural mechanism for an accelerated expansion without recourse to a cosmological constant or dark energy."

**Main Claims**:
- The critical (flat, k=0) Friedmann spacetime is an unstable saddle point in self-similar coordinates near the Big Bang.
- Underdense (k < 0) perturbations evolve in a family F that shows intermediate accelerated expansion away from Friedmann behavior, mimicking the effect attributed to dark energy in supernova observations.
- Asymptotically (t → ∞), solutions decay back to the same k < 0 Friedmann spacetime.
- This provides a GR-internal explanation for anomalous acceleration without Λ or dark energy.
- Builds directly on the authors' 2017 paper (Smoller, Temple, Vogler, Proc. R. Soc. A 473, 20160887) which introduced similar instability ideas.

**Mathematical Approach** (with complete variable/function key):
The Einstein-Euler equations for pressureless dust (p = 0) in spherical symmetry are recast in self-similar variables:

**Key Variables and Functions**:
- t: Cosmological time coordinate (proper time at center r=0).
- r: Radial comoving coordinate.
- ξ := r / t : Self-similar radial variable (dimensionless).
- z(t, ξ), w(t, ξ), A(t, ξ), D(t, ξ): Metric and fluid variables in Schwarzschild gauge (specific definitions in paper; z related to density or expansion, w to velocity, A and D to metric coefficients).
- Expansion in even powers of ξ (to preserve smoothness/regularity at center ξ=0):
  \[
  z(t, \xi) = \sum_{n=0}^\infty z_{2n}(t) \, \xi^{2n}
  \]
  (similar for other fields; complete key: z_{2n}(t) are time-dependent coefficient functions at each order n).
- This yields a nested system of autonomous ODEs (STV-ODE) at each perturbative order n.
- S_M : Unstable saddle rest point corresponding to the critical (k=0) Friedmann spacetime.
- M : Stable rest point corresponding to Minkowski spacetime (asymptotic attractor as t → ∞).
- Eigenvalues of the linearized system at S_M determine stability (positive eigenvalues imply instability; one negative eigenvalue removed by gauge choice of "time since Big Bang").
- Family F : Maximal set of solutions agreeing with k < 0 Friedmann at leading order (n=1).
- Decay estimates (example from Theorem 2.8):
  \[
  |\rho(\bar{t}, \bar{r}) - \rho_F(\bar{t}, \bar{r})| \leq C(\bar{r}) \, \bar{t}^{-5/2}
  \]
  (complete key: ρ = energy density; subscript F = background Friedmann; \bar{t}, \bar{r} = fixed rescaled coordinates; C(\bar{r}) = constant depending on fixed \bar{r} < \bar{t}; the exponent -5/2 comes from the leading unstable eigenvalue).
  Similar for velocity v with logarithmic correction.

**Cosmological Interpretation**:
Instabilities at the Big Bang in standard GR + dust naturally produce accelerated expansion at intermediate times without dark energy. The observed acceleration is a transient effect of evolving away from (and later back toward) Friedmann behavior due to generic underdense radial perturbations. This challenges the viability of the stable ΛCDM critical Friedmann model.

---

## 2. Strengths (Rigorous and Novel Aspects)

- **Mathematical Rigor**: Peer-reviewed in Proc. R. Soc. A (high standard). Uses self-similar reduction + perturbative expansion in even powers of ξ to convert PDEs to nested ODEs, allowing precise eigenvalue analysis and asymptotic proofs. Clear statements of theorems with explicit decay rates.
- **Builds on Prior Work**: Direct extension of authors' 2017 paper. Consistent internal logic.
- **Interesting Alternative Mechanism**: Provides a concrete, GR-based way to generate apparent acceleration from initial conditions/instabilities near t=0, without new fields or fine-tuned Λ. The "pencil standing on end" analogy (Temple quote) is apt for unstable equilibria.
- **Falsifiable Elements**: Makes predictions about higher-order terms in the redshift-luminosity expansion (e.g., differing at z^3 order from pure ΛCDM) and requires us to be in a special underdense region (challenging Copernican principle, but noted in press release).
- **Relevance to Broader Debates**: Adds to literature questioning the stability of FLRW + Λ (cf. discussions on backreaction, inhomogeneous cosmologies). The instability of k=0 is shown rigorously in this restricted setting (spherical symmetry, pressureless dust, self-similar near Big Bang).

---

## 3. Weaknesses and Criticisms (Potential Issues and Limitations)

- **Scope Limitations**: Restricted to pressureless dust (p=0) in spherical symmetry during matter-dominated epoch. Real cosmology has radiation era, baryons, neutrinos, possible early dark energy or modified gravity. The instability analysis does not automatically carry through the full thermal history or structure formation.
- **"Alternative to Dark Energy" Claim is Overstated for Full Cosmology**: The paper shows *intermediate-time acceleration* in family F that *decays back* to Friedmann asymptotically. Observed acceleration (from SN Ia at z ≲ 1) is a late-time phenomenon. It is not demonstrated that the effect persists quantitatively to match the precise supernova Hubble diagram, BAO scale, or CMB constraints *without* effectively introducing parameters equivalent to Λ or curvature adjustments. The asymptotic return to Friedmann may conflict with persistent acceleration inferred from current data.
- **Quantitative Matching to Data**: No explicit global fit to full cosmological datasets is provided in the summaries. Previous similar claims (2017 paper) have not displaced ΛCDM consensus. The required "centered underdensity" for spherical symmetry raises Copernican issues (we must be near a special center), which the authors acknowledge but do not fully resolve for a viable model.
- **Gauge and Approximation Choices**: Self-similar variables and even-power expansion assume specific regularity. The "time since Big Bang" gauge choice removes a negative eigenvalue; robustness to other gauges or full nonlinear evolution needs further validation.
- **Comparison to ΛCDM Successes**: ΛCDM fits CMB power spectrum, BAO, SN, H0 (with tensions), large-scale structure extremely well with 6 parameters. This alternative would need to reproduce or improve on all of these from first principles (Big Bang instability) without fine-tuning initial perturbations. Current evidence suggests it is an interesting toy model in a restricted setting rather than a complete replacement.
- **Relation to Other Alternatives**: Similar in spirit to backreaction or void models (e.g., Lemaître-Tolman-Bondi), which have faced challenges matching all data simultaneously. The mathematical elegance is high, but empirical viability remains to be proven at the level of precision cosmology.

**Honest Assessment**: This is high-quality mathematical GR work that rigorously demonstrates an instability. However, the leap to "alternative to dark energy" in real cosmology requires substantially more: full numerical evolution through radiation/matter transition, quantitative confrontation with Planck + DESI + Pantheon+ data, and resolution of the special-location problem. It is a valuable contribution to the stability debate but does not yet constitute a viable replacement for Λ in precision cosmology.

---

## 4. Relevance to the Tau-Superblock Framework (TSC)

The TSC posits a radical geometric unification (5D EKK Tav cylinder with macroscopic τ ≈ 7 h⁻¹ Mpc, 8-phase G₂/octonionic clockwork, 6 co-located domains on S³ supersphere with E₈-staggered velocities, TEP enforcing 313.1 MeV floor, twistor-averaged emergent gravity, redshift as geometric wavefunction dispersion across domains rather than metric expansion, and dark energy-like effects from centrifugal Ω_rot(t) of the rotating supersphere + Casimir w ≡ -1 from the τ-circle).

**Points of Contact**:
- Both frameworks seek to explain anomalous acceleration *without* a fundamental cosmological constant: this paper via GR instability near Big Bang; TSC via multi-domain centrifugal/Casimir geometry.
- TSC explicitly claims parameter-free geometric derivations for many phenomena (including redshift law, emergent dark matter ratio ≈5.2, 313.1 MeV floor). This paper stays strictly within 4D GR + dust and derives instability mathematically.
- Potential Synergy or Tension: TSC's multi-domain staggering and τ-circle Casimir could be viewed as providing a higher-dimensional "regularization" or completion of the instabilities analyzed here. Conversely, if the GR instability is real and sufficient, it reduces the necessity for TSC's more radical 5D/octonionic structures *solely* for dark energy. TSC would need to demonstrate additional unique predictions (e.g., 7-fold harmonics in FRB/CMB, specific Bell-test baselines, Weyl shadows) that this paper does not address.
- Methodological Note (per TSC style): TSC emphasizes "derived, not fitted" with honest flags on open items (e.g., explicit H_φ operator, full 48D diagonalization calibration). This paper is exemplary in its rigorous derivation within its scope but shares the common challenge of extending local mathematical results to global observational cosmology.

**Conclusion for TSC Development**: This paper strengthens the case that standard FLRW + Λ may have hidden instabilities, aligning with TSC's motivation to replace it with geometry. However, TSC's strength lies in its broader unification claims (particle physics via TEP/313.1 MeV, entanglement via Tautochone curves, falsifiable 7-fold signatures). Future TSC work could explore whether the self-similar instability near the Big Bang emerges naturally from the Tau cylinder dynamics or 8-phase engine, or use this paper's techniques to analyze stability of TSC's own multi-domain solutions.

---

## 5. Overall Verdict

**Scientific Quality**: High (rigorous math, peer-reviewed prestigious journal).  
**Impact on Cosmology**: Interesting and provocative for the stability debate; may inspire further inhomogeneous or backreaction studies. Unlikely to immediately replace ΛCDM without extensive further validation against full datasets.  
**Relation to Alternative Frameworks (e.g., TSC)**: Complementary in spirit (both eliminate fundamental dark energy) but orthogonal in method (GR instability vs. new 5D geometric substrate). TSC remains more ambitious and speculative; this paper is conservative but limited in scope.

All equations above include exhaustive variable/function keys as per session requirements. This evaluation session has been saved to the Personal Files folder.

**End of Evaluation** — Compiled 15 July 2026 for the Tau-Superblock Universe Project. Further refinements or comparisons to specific TSC equations (e.g., redshift dispersion integral, Ω_rot(t)) available upon request.