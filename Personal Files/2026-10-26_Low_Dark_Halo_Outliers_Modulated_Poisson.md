# Session 2026-10-26: Low dark-halo outlier galaxies under the modulated Poisson randomizing set

**Date:** 2026-10-26  
**Context:** Tau-Superblock / dual-channel residual-L; extension of the inhomogeneous Poisson process with hierarchical intensity, domain-phase orbital modulation, and prior-aeon remnant seeds.

## Query
Examine low dark halo outlier galaxies in light of this random distribution. Probabilities?

## Analytical formulation

Full modulated intensity (previous session):
\[
\lambda(\mathbf{x}) = \lambda_0 \Bigl(1 + \alpha_0\sum_{\rm rem}\delta^{(3)}(\mathbf{x}-\mathbf{x}_{\rm rem})\Bigr)
\prod_{g=1}^{g_{\rm max}} \bigl(1 + \alpha_g\,\Theta_{\rm dom}^{(g)}(\mathbf{x})\bigr)
\times \mathcal{M}(\phi_a,\boldsymbol{\omega}).
\]

A low dark-halo outlier is a galaxy-scale region \(\mathcal{G}\) whose integrated residual-L mass satisfies
\[
\frac{M_{\rm RL}(\mathcal{G})}{M_{\rm bar}(\mathcal{G})} < \epsilon,\qquad \epsilon\ll 1.
\]
(Observational examples such as NGC 1052-DF2/DF4 lie near \(\epsilon\approx 0\).)

Residual-L accumulates only through successive dominant-glob selections; \(M_{\rm RL}\) remains small only when the local intensity history contains no early high-\(\alpha\) event (remnant seed or strong phase-domain boost).

### Variable key
- \(\lambda(\mathbf{x})\): full modulated intensity
- \(\lambda_0\): base Poisson intensity
- \(\alpha_0\): large enhancement at incorporated remnant sites
- \(\alpha_g\): enhancement at hierarchical level \(g\)
- \(\Theta_{\rm dom}^{(g)}\): dominant-glob indicator at level \(g\)
- \(\mathcal{M}(\phi_a,\boldsymbol{\omega})\): domain-phase orbital modulation
- \(M_{\rm RL}(\mathcal{G})\): residual-L mass inside galaxy region \(\mathcal{G}\)
- \(M_{\rm bar}(\mathcal{G})\): baryonic mass inside \(\mathcal{G}\)
- \(\epsilon\): observational threshold for “low dark halo”
- \(\phi_a\), \(\boldsymbol{\omega}\), \(\mathbf{x}_{\rm rem}\), etc.: as previously defined

## Plain language
A galaxy looks “missing dark matter” when the residual-L process never got a strong head start in that patch. The head start comes either from a leftover black-hole remnant dropped in from the previous aeon or from a favorable domain-phase orbital shift. If a patch is far from every remnant and sits in a phase offset that delayed collapse, the hierarchical cascade stays weak and the galaxy ends up close to pure baryonic. Those patches are the low dark-halo outliers.

## Probability estimate

Probability that a random galaxy-scale volume \(\mathcal{V}_g\) contains no remnant seed and lies in a phase-domain offset that keeps the hierarchical product near unity:
\[
P_{\rm low} \approx e^{-\lambda_0 \mathcal{V}_g \langle\alpha_0\rangle_{\rm rem}} \times P\bigl(\mathcal{M}(\phi_a,\boldsymbol{\omega}) < 1+\delta\bigr).
\]
With sparse remnants (direct aeon-to-aeon incorporation, not a dense Hawking-point field) and six discrete domain phases, \(P_{\rm low}\) is naturally small but non-zero—consistent with the observed rarity of low dark-halo systems.

### Variable key (additional)
- \(P_{\rm low}\): probability of a low dark-halo outlier
- \(\mathcal{V}_g\): characteristic galaxy-scale volume
- \(\langle\alpha_0\rangle_{\rm rem}\): volume-weighted remnant enhancement
- \(\delta\): tolerance on the domain-phase modulation
- \(e^{-\cdots}\): Poisson void probability for remnant seeds

## Plain language
Because the heavy seeds from the previous aeon are rare, most galaxy-sized patches never contain one. A further fraction of those empty patches also sit in one of the six domain-phase offsets that does not pack gas early. The product of those two chances is the probability of finding a galaxy that never built a strong residual-L halo. The number is small, matching the fact that such objects are uncommon, yet it is not zero—exactly what a random process with sparse strong seeds produces.

## Implications inside the live corpus
- Low dark-halo outliers are the expected rare voids of the same inhomogeneous Poisson process that generates ordinary residual-L halos; no extra continuous dark-matter amplitude or particle species is required.
- Direct incorporation of prior-aeon remnants (rather than Hawking points) supplies the sparse high-amplitude seeds that both accelerate most halos and leave a few patches seed-free.
- Domain-phase orbital modulation adds a discrete six-fold modulation that further modulates the outlier rate without restoring a metric Tau cylinder.
- Laboratory \(G\) remains the normalization of the time-like channel; the space-like channel stays screened inside any cores that do form.
- Compatible with the earlier SPARC residual-L confrontation (majority improvement over pure baryonic; residual scatter expected from the randomizing set).

## Caveats
Numerical value of \(P_{\rm low}\) depends on the (phenomenological) remnant density and the precise amplitude of \(\mathcal{M}\). Quantitative prediction requires an N-body realization of the modulated Poisson process. Observational selection effects further shape which outliers are catalogued. Equal-mass idealization and ideal dominant-glob cut remain simplifications.

## Status
Non-locking annotation consistent with dual-channel residual-L, laboratory-\(G\) match, kinematic UPS, Tau rejection, and direct remnant incorporation (no Hawking points).
