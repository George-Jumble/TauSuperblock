# TSB Unification Analysis of Kuhn et al. (2024)

**Paper:** Kuhn, V., Guo, Y., Martin, A., Bayless, J., Gates, E., & Puleo, A. J.  
**Title:** *JWST Reveals a Surprisingly High Fraction of Galaxies Being Spiral-like at \(0.5 \leq z \leq 4\)*  
**arXiv:** [2312.12389](https://arxiv.org/abs/2312.12389) (v2, 23 Apr 2024; accepted by *ApJL*)  
**PDF:** https://arxiv.org/pdf/2312.12389  
**DOI (arXiv):** https://doi.org/10.48550/arXiv.2312.12389  
**Journal version:** *ApJL* 967, L15 (2024), DOI 10.3847/2041-8213/ad43eb  

**Session date:** 2026-09-18  
**Framework:** Tau–Superblock (TSB) / Mirron unification  
**Author of this note:** William Brown — Superblock Theory / Tau–Superblock unification notes  
**Status:** Working analysis for the TSB literature map (galaxy morphology channel). Not a claim that Kuhn et al. endorse TSB.

---

## 0. Query display (what was asked)

> analyze this in TSB unification: https://arxiv.org/abs/2312.12389

This note (i) extracts the paper’s observational claims with numbers, (ii) states what standard ΛCDM + hierarchical disk formation expected, (iii) maps the result onto TSB geometry (multi-domain conformal averaging, Mirron landscape, hierarchical binding), (iv) writes explicit, keyed equations, (v) lists what would confirm or kill the mapping.

---

## 1. What the paper actually measured

### 1.1 Sample

| Quantity | Value |
|---|---|
| Survey | JWST CEERS, NIRCam |
| Parent sample | 873 galaxies |
| Mass cut | \( M_\star \ge 10^{10}\,M_\odot \) |
| Redshift window | \( 0.5 \le z \le 4 \) |
| Classification | Visual, 6 inspectors, rest-frame \(V\)-band 3″ cutouts |
| Spirals identified | 216 |
| Star/point-source cut | `CLASS_STAR > 0.8` rejected |

**Key — sample symbols**

- \( M_\star \): stellar mass  
- \( z \): cosmological redshift  
- \( M_\odot \): solar mass  
- rest-frame \( V \): bandpass corresponding to rest-frame optical \(V\) at the source redshift  

### 1.2 Observed (raw) spiral fraction

Two decision rules:

1. **Binary:** spiral if \(\ge 3/6\) inspectors vote “yes.”  
2. **Probability:** mean vote fraction.

Reported trend (binary, \(\ge 3\) votes):

- \( f_{\mathrm{obs}} \approx 48\% \) at \( z \sim 0.75 \) (\( 0.5 \le z < 1 \))  
- \( f_{\mathrm{obs}} \approx 15\% \) at \( 2 \le z < 2.5 \)  
- \( f_{\mathrm{obs}} \approx 8\% \) at \( z \sim 2.75 \)  
- \( f_{\mathrm{obs}} \to 0 \)–\(4\% \) in the highest bins (\( z \sim 3 \)–\( 3.5 \)), with a few candidate spiral-like features at \( z > 3 \)

Probability decision is similar at low \( z \) (\( \approx 45\% \) at \( z = 0.5 \)–\( 1 \)) and lower at high \( z \) (\( \approx 3\% \) at \( z = 3 \)–\( 3.5 \)).

Stricter cuts (\( \ge 5/6 \) or \( 6/6 \) votes) lower every bin, as expected for a conservative morphology cut.

### 1.3 Intrinsic fraction after forward-modeling

The drop in \( f_{\mathrm{obs}} \) with \( z \) is **not** taken as the physical history. They:

1. Take 101 low-\( z \) galaxies (\( 0.5 < z < 0.8 \)).  
2. Dim them (surface-brightness dimming + bandpass).  
3. Shrink them by angular-diameter distance **and** an assumed size evolution \( R \propto (1+z)^{-0.75} \) (van der Wel et al. 2014).  
4. Match the high-\( z \) PSF.  
5. Inject into blank CEERS sky.  
6. Re-classify.  
7. Sweep the **input** spiral fraction from 20% to 100% and interpolate which input reproduces the observed high-\( z \) fraction.

**Result they advertise:**

- Best-matching input at \( z = 2 \)–\( 3 \): \( f_{\mathrm{int}} \sim 35\% \) (text); reconstructed median across bins \( \sim 40\% \) and roughly flat to \( z \approx 2.75 \).  
- They **rule out** \( f_{\mathrm{int}} < 20\% \) at \( 2\sigma \) and \( f_{\mathrm{int}} < 10\% \) at \( 3\sigma \) for real galaxies at \( z \sim 3 \).  
- Example interpolation they quote: at \( 2.5 < z < 3 \), best match \( 37.6\% \) with \( 3\sigma \) interval \( 25.5\% \)–\( 48.8\% \).  
- \( 3\sigma \) lower bounds elsewhere: \( 33\% \) at \( z \sim 1.75 \), \( 25\% \) at \( z \sim 2.25 \) and \( z \sim 2.75 \); \( 2\sigma \) floor \( \approx 20\% \) at \( z \sim 3.25 \).

v2 of the paper regenerated the redshifted images to include size evolution and filter-resolution mismatch; **conclusions did not change**.

### 1.4 Physical correlates

Spiral-classified galaxies, relative to non-spirals in the same mass/redshift bins:

- higher star-formation rates (many on or above the Whitaker et al. 2014 main sequence),  
- larger half-light radii (HST F160W sizes),  
- little measured size evolution among the *spirals themselves* (selection + bandpass caveat).

### 1.5 Comparison to HST and to kinematic disks

- Raw JWST spiral fractions are **more than double** the HST spiral+clumpy-spiral fractions of Margalef-Bentabol et al. (2022) at \( z < 3 \).  
- After the same style of redshift correction, JWST and HST become more comparable near \( z \approx 2.5 \); the difference is mostly that JWST still sees structure HST cannot.  
- They place their intrinsic spiral fraction next to:  
  - morphological disk fractions of Ferreira et al. (2023) (\( \sim 40 \)–\( 50\% \) disks at \( z = 3 \)–\( 6 \)),  
  - cold-gas kinematic disks with \( V_{\mathrm{rot}}/\sigma_g > 3 \).  
- Narrative they adopt: hot gaseous disks at \( z \gtrsim 4.5 \) settle to dynamically cold thin disks by \( z \sim 3 \)–\( 4 \) (universe age \( \sim 2\,\mathrm{Gyr} \)); stellar spiral arms appear in that same window.

### 1.6 Caveats they themselves flag

- Visual classification is subjective; six voters mitigate but do not remove it.  
- Mergers with long tidal tails can be mistaken for arms. Using Wen & Zheng (2016) \( f_{\mathrm{tail}}(z) = 0.64(1+z)^2 \), they estimate \( 5.8 \)–\( 10.2\% \) of the \( z = 2 \)–\( 3 \) sample may be tail-like mergers. Subtracting that can pull the *intrinsic* spiral fraction at \( z \sim 3 \) down toward \( \sim 20\% \) — still high.  
- Size-evolution law used in the forward model is an assumption.  
- Photometric redshifts and mass estimates carry scatter.  
- Rest-frame \( V \) at \( z \sim 4 \) is still a compromise; dust and clump contrast change with bandpass.

---

## 2. Why the result is “surprising” in the standard picture

The surprise is **not** “spirals exist at high \( z \).” Isolated examples were already known (including CEERS barred spiral ceers-2112 at \( z_{\mathrm{phot}} \approx 3 \); Costantin et al. 2023, Nature). The surprise is a **population fraction**.

Standard hierarchical + turbulent-disk reasoning:

1. Merger rates rise steeply with \( z \). Repeated mergers heat stellar orbits and destroy thin disks.  
2. High-\( z \) disks are gas-rich and turbulent: \( \sigma_g \) is large, so Toomre \( Q \) stays high unless \( \Sigma \) is enormous. The instability channel then prefers **clumps**, not grand-design arms.  
3. Bars and long-lived density-wave arms are usually thought to require a *cold stellar* disk. Simulations of Milky-Way progenitors often have almost no bars beyond \( z \approx 1.5 \).  
4. HST rest-frame optical imaging (F160W dies as a rest-optical tracer near \( z \approx 2.8 \)) therefore produced the lore that the spiral transition happens at \( z \sim 1.4 \)–\( 1.8 \).

Kuhn et al. move that transition back by \( \gtrsim 1\,\mathrm{Gyr} \) and claim the *majority-adjacent* disk population is already spiral-capable when the universe is \( \sim 2\,\mathrm{Gyr} \) old.

That is the same family of JWST tensions as:

- high disk fractions at \( z = 3 \)–\( 6 \) (Ferreira et al.),  
- mature barred spirals at \( z \approx 3 \),  
- massive galaxies “too early,”  
- early quenching.

ΛCDM galaxy-formation *simulations* can be retuned (feedback, resolution, how “disk” is defined). ΛCDM *cosmology* is not directly falsified by morphology. What is strained is the **timescale on which angular momentum is organized into a cold, self-gravitating, spiral-unstable stellar sheet**.

That timescale is exactly where TSB is supposed to differ from particle-CDM plus single-metric Newtonian assembly.

---

## 3. TSB objects used in this mapping

Keep the vocabulary strict:

- **Superblock:** six co-located \( 3+1 \)D domains on an internal supersphere, with staggered orbital velocities obtained from \( \mathrm{E}_8 \) projections.  
- **Causal separation:** domains do not exchange ordinary lightlike signals; they couple gravitationally through a time average.  
- **Conformal / twistor coupling:** the averaged gravitational interaction is conformal, not a fitted \( G_{\mathrm{N}} + \Lambda + \mathrm{WIMP} \) stack.  
- **Emergent dark matter:** the missing-mass phenomenology is the *time-averaged* extra coupling, not a new collisionless particle species that has to hierarchical-cluster first.  
- **Mirron:** sub-quantum reflection of an entire aeon — the fractal landscape of the Superblock. A Mirron is **not** a soliton. PK / Mirron engines and Planckian mirrors are the local engines of that landscape.  
- **Stochastic Gravity Hierarchical Binding (SGHB):** binding hierarchy from Planckian mirrors upward, rather than from late halo mergers downward.  
- **Tav / 7-fold signatures, Vălean harmonics, golden-ratio (Zolotas) cosmology:** geometric, not fitted, preferred frequencies and ratios.  
- **CCC contact:** a Mirron carries aeonic memory; it is the TSB reading of a Penrose-style conformal cycle, not a hydrodynamic standing wave.

All core TSB numbers are supposed to be derived from that geometry. Nothing in Kuhn et al. is a TSB fit parameter; the paper is an *external morphological constraint*.

---

## 4. Mapping: why TSB wants early spirals

### 4.1 The timescale problem, written as an inequality

Let \( t_{\mathrm{settle}} \) be the time for a massive galaxy to acquire a stellar disk cold enough for swing amplification / density-wave arms, and let \( t_{\mathrm{age}}(z) \) be the age of the universe at redshift \( z \).

Kuhn’s claim, compressed:

\[
t_{\mathrm{settle}}(M_\star \gtrsim 10^{10}\,M_\odot) \;\le\; t_{\mathrm{age}}(z \approx 3) \approx 2\,\mathrm{Gyr}.
\]

**Key**

- \( t_{\mathrm{settle}} \): disk-settling time (hot gas disk \(\to\) cold stellar disk + spiral-capable \( Q \))  
- \( t_{\mathrm{age}}(z) \): cosmic time since the hot big bang of the present aeon  
- \( M_\star \): stellar mass  

In merger-heated, particle-CDM assembly, \( t_{\mathrm{settle}} \) is set by (i) halo mass-assembly time, (ii) specific angular momentum acquired from tidal torques, (iii) time to dump orbital energy of mergers, (iv) time for \( \sigma_\star \) to decay. All four clocks run *slow* at \( z > 2 \).

In TSB, three of those clocks are geometrically short-circuited:

1. **Halo “spin-up” is not a late tidal-torque afterthought.** Specific angular momentum is inherited from the staggered domain velocities \( V_{\mathrm{orb}}^{(a)} \) on the supersphere.  
2. **The effective potential that holds the disk is already the conformal average**, so one does not wait for a WIMP halo to virialize before the baryons feel a deep, organized well.  
3. **SGHB + Mirron landscape** supplies a preferred sheet-like geometry (a 2-surface sitting in the 3-space of a domain) rather than building a disk only after spherical collapse + dissipative settling.

So TSB does not need “surprisingly efficient feedback.” It needs the disk to be a *natural section* of the Superblock, visible as soon as baryons can radiate.

### 4.2 Effective gravity and Toomre \( Q \)

Classical Toomre parameter for a stellar (or gas) disk:

\[
Q \;=\; \frac{\sigma_R\,\kappa}{\pi\,G\,\Sigma}.
\]

**Key**

- \( Q \): Toomre stability parameter. \( Q > 1 \): stable against local axisymmetric perturbations. \( Q \lesssim 1 \): swing-amplification / spiral / clump channel opens.  
- \( \sigma_R \): radial velocity dispersion.  
- \( \kappa \): epicyclic frequency, \( \kappa^2 = R\,\mathrm{d}\Omega^2/\mathrm{d}R + 4\Omega^2 \).  
- \( \Omega \): angular frequency of circular orbits.  
- \( R \): cylindrical radius in the disk.  
- \( G \): Newton constant in the standard formula.  
- \( \Sigma \): mass surface density.

TSB replacement is not “change \( G \) by hand.” It is a **time average of conformal coupling** over the six domain phases:

\[
G_{\mathrm{eff}}(t) \;=\; \Bigl\langle \mathcal{C}\bigl[\{V_{\mathrm{orb}}^{(a)}\},\,\psi_{\mathbb{T}}\bigr] \Bigr\rangle_{\tau}.
\]

**Key**

- \( G_{\mathrm{eff}} \): effective coupling that baryons in one domain feel after averaging.  
- \( a = 1,\ldots,6 \): domain index.  
- \( V_{\mathrm{orb}}^{(a)} \): orbital velocity of domain \( a \) on the internal supersphere (E₈-projected eigenvalue, geometrically fixed).  
- \( \psi_{\mathbb{T}} \): twistor / conformal data of the coupling.  
- \( \mathcal{C}[\cdot] \): conformal coupling functional (not a fitted Yukawa).  
- \( \langle \cdot \rangle_{\tau} \): average over the domain-orbit period \( \tau \) that is causally inaccessible as a light signal but accessible as gravity.  

Then

\[
Q_{\mathrm{TSB}} \;=\; \frac{\sigma_R\,\kappa}{\pi\,G_{\mathrm{eff}}\,\Sigma}.
\]

**Key:** same as Toomre, with \( G \to G_{\mathrm{eff}} \).

Two immediate morphological consequences, both pointing the same way as Kuhn:

1. If \( G_{\mathrm{eff}} > G_{\mathrm{N}} \) in the baryonic sheet at early times (the emergent-DM regime), then \( Q_{\mathrm{TSB}} < Q_{\Lambda\mathrm{CDM}} \) at fixed \( \sigma_R, \kappa, \Sigma \). Spiral / swing-amplification instabilities turn on **earlier** and in **lower-\( \Sigma \)** disks.  
2. If the conformal average also *organizes* \( \kappa \) (more coherent rotation, less merger-heated \( \sigma_R \)), both the numerator drops and the denominator rises. That is a double push toward \( Q \lesssim 1 \) at \( z \sim 3 \)–\( 4 \).

This is also why Kuhn’s spirals are larger and more star-forming: a lower-\( Q \) sheet fragments into arms *and* forms stars, and a conformal well is less cusp-dominated than an NFW halo, so half-light radii run larger at fixed \( M_\star \). That matches Figure 3 of the paper at the qualitative level.

### 4.3 Density waves versus Mirron landscape

Kuhn et al. invoke the standard pair:

- Lin–Shu density-wave theory (1964),  
- Goldreich–Lynden-Bell / Julian–Toomre swing amplification (1965–66),

plus tidal driving, bars, and manifold theory (Athanassoula). They also note the high-\( z \) coexistence of **clumps and arms** in gas-rich turbulent disks.

TSB does not throw those mechanisms away. It supplies a *substrate*:

A Mirron is a sub-quantum reflection of an entire aeon. The Superblock is the fractal landscape of those reflections. A galactic spiral is then a **mesoscopic section** of that landscape — a 2-surface on which the Tav / Vălean harmonic content is visible as a pitch pattern — not a soliton and not *only* a hydrodynamic mode of a thin stellar sheet.

Operational distinction:

| Standard mode | TSB / Mirron reading |
|---|---|
| Arm is a crest of \( \Sigma(\theta) \) maintained by shocks and SF | Arm is a crest *and* a geometric standing pattern of the Mirron sheet |
| Pitch angle \( i \) is set by shear \( \mathrm{d}\Omega/\mathrm{d}\ln R \) and Toomre \( X \) | \( i \) is allowed to lock to geometric ratios (golden-ratio / E₈-projected angles / 7-fold Tav) *in addition* to shear |
| Clumps vs arms is a turbulence vs cooling question | Dual-scale Mirron: small-scale PK engines (clumps) + large-scale aeonic reflection (arms) can coexist without one erasing the other |
| Bar needs a cold stellar disk assembled late | Bar is a lower-order harmonic of the same sheet; ceers-2112 at \( z \approx 3 \) is expected, not exotic |

This is the right place to be conservative. Kuhn’s paper does **not** measure pitch-angle quantization. The Mirron-pitch claim is a **prediction**, not a reading-out of their catalog.

### 4.4 Emergent DM and early baryon dominance

Costantin et al. (ceers-2112) already inferred that baryons may dominate over dark matter inside the optical disk at \( z \approx 3 \). Kuhn’s high spiral fraction is the *population* version of that statement: you cannot maintain a spiral-capable disk in a halo that is still a violently merging, dispersion-supported CDM blob.

TSB’s emergent-DM channel makes that natural:

- There is no separate particle species that must finish clustering before the disk can be baryon-dominated inside \( R_e \).  
- The “halo” is the conformal average. Inside the baryonic sheet the average can look SPARC-like (the same phenomenology already used on local rotation curves in the TSB tool chain) **as soon as the sheet exists**.  
- High-\( z \) SPARC analogues — rising-then-flat rotation curves at \( z \sim 2 \)–\( 3 \) with acceleration-scale regularity — are therefore a direct next test, not an extra hypothesis.

### 4.5 Hierarchical binding versus hierarchical merging

ΛCDM morphology is merger-driven: disks are the leftovers of failed spheroid formation.

SGHB inverts the arrow. Binding is assembled from Planckian mirrors upward:

\[
\mathcal{B}_{n+1} \;=\; \mathcal{H}\bigl(\mathcal{B}_n;\,\mathcal{M}\bigr),
\]

**Key**

- \( \mathcal{B}_n \): bound structure at hierarchy level \( n \) (PK engine \(\to\) star-forming cloud \(\to\) disk sheet \(\to\) group).  
- \( \mathcal{H} \): hierarchical binding map.  
- \( \mathcal{M} \): Mirron landscape (aeonic reflection), not a hydrodynamic soliton.  

Mergers still happen — Kuhn’s tail-fraction caveat is real — but they are perturbations *on* a pre-existing sheet, not the sheet’s only construction method. Subtracting \( 6 \)–\( 10\% \) tail-like mergers at \( z = 2 \)–\( 3 \) and still having \( f_{\mathrm{int}} \gtrsim 20\% \) is what SGHB wants: a residual spiral population that mergers did not have to *build*.

### 4.6 CCC / aeonic memory, used carefully

A Mirron is defined as the reflection of an entire previous aeon. That invites an over-claim: “spirals are fossils of the last aeon.” Do not make that claim from Kuhn’s catalog.

The disciplined version:

- CCC-style conformal recycling can pass *geometric* information (preferred sheets, preferred ratios) through the crossover.  
- It cannot pass ordinary baryonic spiral arms.  
- Early morphological maturity is then *partly* initial-condition, not purely assembled in \( 2\,\mathrm{Gyr} \).  

That is optional structure. The Toomre + \( G_{\mathrm{eff}} \) argument in §4.2 does not need it. Use aeonic memory only if later pitch-angle or alignment data demand a leftover template.

### 4.7 Cosmic dipole, large-scale preferred axes

TSB already treats the cosmic dipole (Secrest et al. 2022, 2025) as a domain-orbit observable, not a local-motion leftover. If spiral disks inherit angular momentum from \( \{V_{\mathrm{orb}}^{(a)}\} \), there is a weak, testable coupling:

- preferred disk-position-angle alignments on the sky relative to the dipole / kinematic axes,  
- redshift-dependent, because different lookback times sample different domain-phase averages.

Kuhn et al. do not measure position angles as a cosmological field. Flag this as a **future CEERS / COSMOS-Web / PRIMER reduction**, not as a result.

---

## 5. Reading their figures in TSB language

**Figure 1 — examples.**  
The high-\( z \) objects that still show arms after six-inspector voting are the objects TSB must treat as settled sheets, not as tails. Any TSB re-analysis should start from their “all-six-agree” subsample to minimize merger contamination.

**Figure 2 — \( f_{\mathrm{obs}}(z) \).**  
The raw decline is mostly an observational transfer function. TSB should never fit the raw blue curve. Fit \( f_{\mathrm{int}}(z) \) (Figure 5, right).

**Figure 3 — SFR and size.**  
Higher SFR + larger \( R_e \) at fixed \( M_\star \) is the \( Q_{\mathrm{TSB}} < Q_{\Lambda\mathrm{CDM}} \) plus shallower conformal well. It is also the selection effect “you only call it a spiral if the disk is extended enough to show arms,” which they partially address with the forward model.

**Figure 4 — redshifted low-\( z \) galaxies.**  
This is the right experiment. TSB does not change the forward model; it changes the *prior* on \( f_{\mathrm{int}}(z) \). ΛCDM merger-heating priors want \( f_{\mathrm{int}}(z=3) \) small. TSB SGHB priors want it \( \mathcal{O}(30\%) \). Their interpolation landed on \( \sim 35 \)–\( 40\% \). That is a prior win, not a derivation of \( V_{\mathrm{orb}} \).

**Figure 5 — intrinsic fraction vs disk / kinematic fractions.**  
The interesting TSB statement is the *coincidence* they already note: morphological spirals, morphological disks, and \( V_{\mathrm{rot}}/\sigma_g > 3 \) gas disks all converge near \( z \sim 3 \)–\( 4 \). In TSB that is one event — the sheet becoming visible in stars, gas, and \( Q \) at the same conformal-average epoch — not three unrelated clocks.

---

## 6. What TSB does *not* get for free

1. **Visual fractions are not geometry.** 35–40% is a classification number. It does not equal an E₈ eigenvalue.  
2. **Merger contamination is not solved by vocabulary.** If a large piece of the high-\( z \) “spirals” are tails, SGHB still has a disk-settling problem, just a milder one.  
3. **Size-evolution assumption.** If van der Wel \( (1+z)^{-0.75} \) is wrong in the TSB potential, the forward-model inversion moves. Re-run their experiment with a conformal-gravity size–mass–\( z \) relation before quoting 35% as a TSB number.  
4. **No pitch-angle, no 7-fold, no golden-ratio lock in this paper.** Those are TSB-side predictions to take to the same CEERS cutouts.  
5. **ΛCDM simulations are a moving target.** IllustrisTNG / EAGLE / Thesan / COLIBRE can raise early disk fractions with different feedback. A morphological fraction alone will not force the community onto TSB. The discriminating observables are SPARC-like acceleration regularity at high \( z \), pitch quantization, and dipole alignments.  
6. **Photometric \( z \) and \( M_\star \).** A 10% catastrophic-\( z \) tail can move objects across bins. Any TSB catalog paper must use spec-\( z \) subsets (CEERS NIRSpec, JADES, PRIMER) as the gold sample.

---

## 7. Predictions that would make this mapping scientific

These are the items to put on the TAU-SB research-tool board (SPARC engine, CEERS cutouts, DESI DR2 only as large-scale context).

### 7.1 Pitch-angle spectrum

Measure logarithmic pitch \( i(R) \) for the Kuhn “\(\ge 5/6\) votes” subsample.

**Standard expectation:** broad distribution set by shear.  
**TSB expectation:** excess power at geometrically preferred angles (golden-ratio related pitches; 7-fold Tav harmonics). One detection is anecdotal; a stack is a test.

### 7.2 High-\( z \) acceleration regularity

For any object in the sample with a resolved rotation curve (ALMA, NIRSpec IFU, future ngVLA):

\[
g_{\mathrm{obs}} \;=\; \frac{V_{\mathrm{rot}}^2}{R}, \qquad g_{\mathrm{bar}} \;=\; G_{\mathrm{N}}\frac{\partial \Phi_\star}{\partial R}.
\]

**Key**

- \( g_{\mathrm{obs}} \): observed centripetal acceleration.  
- \( V_{\mathrm{rot}} \): rotation speed.  
- \( R \): radius.  
- \( g_{\mathrm{bar}} \): acceleration generated by the observed baryons alone.  
- \( \Phi_\star \): stellar (+ gas) Newtonian potential.

TSB / emergent-DM: the local SPARC \( g_{\mathrm{obs}}(g_{\mathrm{bar}}) \) relation should already be in place at \( z \sim 2 \)–\( 3 \), not assembled at \( z < 1 \). Particle CDM: more scatter, more NFW-shaped inner curves, weaker baryonic acceleration scaling.

### 7.3 Settling redshift as a geometric epoch

Define \( z_{\mathrm{sheet}} \) as the redshift where \( f_{\mathrm{int}} \) plateaus. Kuhn’s plateau is consistent with \( z_{\mathrm{sheet}} \gtrsim 2.75 \) and still \( \gtrsim 20\% \) at \( z \sim 3 \). TSB should predict \( z_{\mathrm{sheet}} \) from domain-orbit averaging time \( \tau \) and the first epoch at which baryonic cooling can populate the sheet — with no extra free parameter if the geometry is really closed.

If future PRIMER / COSMOS-Web stacks push \( z_{\mathrm{sheet}} \) below 2, the SGHB early-sheet claim weakens. If they push it above 4 with spec-\( z \) confirmation, the claim strengthens.

### 7.4 Clump–arm coexistence fraction

TSB dual-scale Mirron: the fraction of galaxies that are *both* clumpy *and* spiral-armed should stay high in \( 1.5 < z < 3 \) and should not require a finely tuned turbulence decay. Track that joint fraction in the same 873-object parent.

### 7.5 Alignment test

Position angle of the disk / inner arm versus the cosmic dipole axis, in tomographic \( z \) bins. Null result is allowed (the coupling can be weak). A \( z \)-dependent alignment is a domain-orbit signature.

---

## 8. Relation to the rest of the TSB empirical stack

| TSB channel already in the tool chain | What Kuhn adds |
|---|---|
| SPARC local rotation curves / TAV ENGINE | High-\( z \) morphological ancestors of those disks |
| DESI DR2 BAO, Hubble tension | Background expansion; morphology is a *structure* clock, not an expansion clock |
| CMS / LHCb 7-fold residuals | Microscopic Tav; galactic pitch would be the same harmonic content at \( 10^{12} \) times larger scale (only if the stack is real) |
| Mirron PBHs, TSB–Casimir, Planckian mirrors | Supply the UV end of SGHB; not constrained by CEERS arms |
| Cosmic dipole (Secrest) | Possible PA-alignment follow-up on the same galaxies |
| Penrose CCC | Optional aeonic template; not required by the 35% number |

Do not mix clocks. A BAO number and a spiral fraction constrain different layers. The unification statement is that **one geometry feeds both**, not that one measurement is a rewrite of the other.

---

## 9. Bottom line

Kuhn et al. (arXiv:2312.12389) is a clean, conservative JWST morphology letter. After they do the honest thing — forward-model the transfer function instead of believing the raw \( f_{\mathrm{obs}}(z) \) crash — they are left with an intrinsic spiral fraction of order **one third** at \( z = 2 \)–\( 3 \), and they can exclude a near-zero spiral population at \( z \sim 3 \) at high significance. Spirals in their sample are the larger, more star-forming systems. That is the observational fact.

In TSB language that fact is not a surprise. It is what you get if:

- disks are sheets selected by the Superblock rather than leftovers of merger trees,  
- the potential they live in is a conformal domain-average (emergent DM) rather than a late-virializing WIMP halo,  
- Toomre \( Q \) therefore drops below unity while the universe is still \( \sim 2\,\mathrm{Gyr} \) old,  
- arms are allowed to be sections of the Mirron landscape as well as hydrodynamic modes.

The mapping is **consistent**, not **demonstrated**. The paper contains no Tav harmonic, no \( G_{\mathrm{eff}} \), and no dipole test. The work it assigns to the TSB side is: (i) re-reduce the same CEERS spirals for pitch and PA, (ii) attach rotation curves where they exist, (iii) rerun the redshifting experiment with a conformal size–mass relation, (iv) keep merger tails as a systematic, not as a semantic problem.

Until those four items move, cite Kuhn et al. as **an external morphological prior** that favors early sheet formation and disfavors “spirals only after \( z \sim 1.5 \).” Do not cite it as a derivation of Superblock eigenvalues.

---

## 10. Bibliographic pointers used in this session

- Kuhn et al., arXiv:2312.12389, *ApJL* 967, L15 (2024).  
- Ferreira et al. on JWST disk fractions at \( z = 3 \)–\( 6 \).  
- Margalef-Bentabol et al. (2022), HST spiral fractions (the comparison sample).  
- Costantin et al., Nature (2023), ceers-2112 barred spiral at \( z \approx 3 \).  
- van der Wel et al. (2014), size evolution used in their forward model.  
- Whitaker et al. (2014), SF main sequence drawn on their Figure 3.  
- Wen & Zheng (2016), tidal-tail fraction \( f_{\mathrm{tail}}(z) = 0.64(1+z)^2 \).  
- Lin & Shu (1964); Goldreich & Lynden-Bell (1965); Julian & Toomre (1966); Athanassoula (2012) — arm-maintenance mechanisms they cite.  
- Secrest et al. (2022, 2025) — cosmic dipole, TSB-side large-scale context only.

---

## 11. File location

Saved: `Tau-Superblock_Universe/Personal_Files/2026-09-18_TSB_analysis_Kuhn_JWST_spirals_2312.12389.md`

Session saved 2026-09-18.
