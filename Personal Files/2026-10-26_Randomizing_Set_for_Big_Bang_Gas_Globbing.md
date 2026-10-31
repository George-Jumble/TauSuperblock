# Session 2026-10-26: Randomizing set for Big-Bang gas under residual-L hierarchical globbing

**Date:** 2026-10-26  
**Context:** Tau-Superblock / dual-channel residual-L framework  

## Query
Examine random distribution of roughly equal masses of gas expanding in the big bang, with a bias towards gravitic globbing, but the random nature insures that it will be uneven in effect. What randomizing set fits the scenario?

## Analytical formulation

Early expanding gas partitioned into \(N\) parcels of approximately equal mass \(m_0\). Comoving positions at early conformal time \(\eta_i\):

\[
\mathcal{P} = \{ \mathbf{x}_j \in \mathbb{R}^3 \mid j=1,\dots,N \}.
\]

Effective residual-L force (time-like channel, laboratory \(G\) normalization, dominant-glob rule):

\[
\mathbf{F}_j = -G_{\rm lab}\, m_0 \sum_{k\neq j} m_0\, \frac{\mathbf{x}_j-\mathbf{x}_k}{|\mathbf{x}_j-\mathbf{x}_k|^3}\, \Theta_{\rm dom}(\mathbf{x}_j,\mathbf{x}_k).
\]

Density contrast develops non-uniformly because initial positions and residual phase offsets \(\phi_j\) (from kinematic 142857 / G2 clock) are uncorrelated.

### Variable key
- \(N\): number of equal-mass gas parcels
- \(m_0\): parcel mass (nucleon-third protocol scale or dressing-share variant)
- \(\mathbf{x}_j\): comoving position of parcel \(j\)
- \(\eta_i\): early conformal time
- \(G_{\rm lab}\): laboratory gravitational constant (time-like residual-L normalization)
- \(\Theta_{\rm dom}\): dominant-glob selection function
- \(\phi_j\): residual phase offset of parcel \(j\)
- \(\delta(\mathbf{x})\): density contrast
- \(\rho, \bar\rho\): local and mean density

## Plain language
Every gas parcel starts with almost the same mass and feels the same laboratory-strength pull toward the biggest coherent clump nearby. Accidental neighborhoods that already contain slightly more material or a slightly more favorable residual phase become the dominant globs first; the rest lag. The bias is systematic, but the starting scatter makes the outcome patchy.

## Fitting randomizing set

**Inhomogeneous Poisson point process with hierarchical intensity modulation.**

Base measure: homogeneous Poisson process of intensity \(\lambda_0\).

Modulated intensity:

\[
\lambda(\mathbf{x}) = \lambda_0 \prod_{g=1}^{g_{\rm max}} \bigl(1 + \alpha_g\,\Theta_{\rm dom}^{(g)}(\mathbf{x})\bigr),
\]

where \(\alpha_g > 0\) is the relative enhancement at globbing level \(g\).

### Variable key (additional)
- \(\lambda_0\): mean Poisson intensity
- \(\lambda(\mathbf{x})\): modulated intensity
- \(g\): hierarchical globbing level
- \(\alpha_g\): relative enhancement at level \(g\)
- \(\Theta_{\rm dom}^{(g)}\): dominant-glob indicator at level \(g\)

### Why this set
- Discrete equal-mass elements (each point carries mass \(m_0\)).
- Purely random at the Poisson level (no preferred center).
- Becomes uneven precisely because the dominant-glob rule raises local intensity wherever a modest overdensity first appears.
- Compatible with live dual-channel residual-L (time-like attraction, space-like channel screened inside cores, \(\eta=0\)).
- Does not re-introduce a continuous free dark-matter density amplitude or a metric fifth dimension.

A pure Gaussian random field is less natural (parcels are discrete and fixed-mass; selection is a hard dominant-glob cut). A plain homogeneous Poisson process lacks the gravitic bias.

## Plain language
Think of the gas as a random sprinkling of identical droplets. The rule “the biggest nearby clump pulls hardest” acts like a local amplifier: any accidental clump immediately raises the chance that more droplets will join it. The sprinkling itself remains random, so the amplifiers light up in different places and at different times. The mathematical object that does exactly that job is a Poisson point process whose intensity is raised wherever a dominant glob has already formed.

## Implications inside the live corpus
- Unevenness is the expected outcome of residual-L hierarchical binding acting on an initially Poisson-like distribution; not an extra free parameter.
- Laboratory \(G\) remains the normalization of the time-like channel.
- Space-like channel stays screened (\(\eta=0\)) inside developing cores.
- Does not restore the Tau cylinder, a KK tower, or a continuous free density field.

## Caveats
Intensity modulation coefficients \(\alpha_g\) are phenomenological (not derived from locked structure). Full N-body realization with the exact dominant-glob rule would be required for a quantitative power spectrum or void probability function. Equal-mass idealization; real baryonic masses carry a small intrinsic scatter.

## Status
Non-locking annotation consistent with dual-channel residual-L, laboratory-\(G\) match, kinematic UPS, and Tau rejection.  
