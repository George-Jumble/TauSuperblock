# Tau–Superblock Notes: Human-Readable Restatement and Analysis

**Session date:** 19 September 2026  
**Source:** three technical reviews of TSB / Mirron notes (impedance, gravity architecture, late-time cosmology)  
**Purpose:** rewrite the reviews in plain scientific English, keep every equation with a full variable key, then assess what is solid, what is overstated, and what to calculate next.

---

## How to read this document

The original reviews are dense and correct in spirit. They do three different jobs at once:

1. Fix numerical and algebraic errors.
2. Separate what has been *derived* from what has been *postulated*.
3. Point at the next calculation that would actually move TSB from architecture to theory.

This file restates each review in that same order, then adds an independent analysis. Nothing here is a verdict that TSB is finished or dead. The useful verdict is narrower:

> The susceptibility / nucleation logic is now scientifically useful. The vacuum-impedance *normalization* is unsolved. The gravitational field equation, as written, is not yet a field equation. The Tav dark-energy floor is not yet derived from the stated 5D action. Those three facts define the research program.

---

## Shared notation (global key)

Use this table for symbols that appear in more than one note.

| Symbol | Meaning |
|---|---|
| \(\alpha_{\rm fs}\) | Fine-structure constant. CODATA 2022: \(7.2973525643(11)\times 10^{-3}\) |
| \(Z_0\) | Vacuum impedance. CODATA 2022: \(376.730313412(59)\,\Omega\) |
| \(R_K\) | von Klitzing constant \(h/e^2\), exact in the 2019 SI |
| \(\Phi\) | Dimensionless ratio \(Z_0/R_K\) |
| \(h\) | Planck constant (exact SI) |
| \(e\) | Elementary charge (exact SI) |
| \(c\) | Speed of light (exact SI) |
| \(\hbar\) | Reduced Planck constant \(h/2\pi\) |
| \(n_M\) | Mirron number density |
| \(r_M\) | Mirron cell / core length. Quoted value \(6.302\times 10^{-16}\,\mathrm{m}\) |
| \(f\) | Dimensionless filling factor, schematically \(f\sim n_M r_M^3\) |
| \(\mathcal G\) | Locked discrete geometry (phases, multiplicities, topology) |
| \(\xi\) | Susceptibility: logarithmic response of \(\alpha\) or \(\Phi\) to \(n_M\) |
| \(\Gamma\) | Mirron nucleation rate in the continuity equation |
| \(H\) | Hubble rate |
| \(a\) | Cosmic scale factor |
| \(z\) | Redshift, \(1+z=1/a\) if \(a_0=1\) |
| \(\tau\) | Tav scale. Quoted cosmological value \(7h^{-1}\,\mathrm{Mpc}\) |
| \(G_{\mu\nu}\) | Einstein tensor (rank 2) |
| \(C_{\mu\nu\rho\sigma}\) | Weyl tensor (rank 4) |
| \(B_{\mu\nu}\) | Bach tensor (rank 2; conformal-gravity field tensor) |
| \(T_{\mu\nu}\) | Stress–energy tensor |
| \(S_5\) | Five-dimensional Einstein–Hilbert action |
| \(G_5\) | 5D Newton constant |
| \(V_{\rm eff}\) | Effective potential after reduction / loops |
| \(w\) | Dark-energy equation-of-state \(p/\rho\) |
| \(B_F(f)\) | Scalar prefactor in the effective Maxwell action |

---

# Part 1 — Vacuum impedance and the fine-structure constant

## 1.1 What the reviewer is actually saying

The newer impedance note is stronger than earlier drafts for one reason: it stops claiming that the observed vacuum impedance has already been derived. It splits the problem into two different questions.

**Normalization problem.** Why is the measured ratio exactly

\[
\Phi_{\rm obs}\equiv\frac{Z_0}{R_K}=2\alpha_{\rm fs}?
\]

**Variable key**

- \(\Phi_{\rm obs}\): observed dimensionless impedance ratio
- \(Z_0\): vacuum impedance
- \(R_K=h/e^2\): quantum Hall / von Klitzing resistance
- \(\alpha_{\rm fs}\): fine-structure constant

**Susceptibility problem.** Once that ratio exists, how does it respond to Mirron density?

\[
\xi\equiv\frac{d\ln\Phi}{d\ln n_M}
\quad\text{or equivalently}\quad
\xi=-\frac{d\ln B_F}{d\ln n_M}.
\]

**Variable key**

- \(\xi\): logarithmic susceptibility
- \(n_M\): Mirron number density
- \(B_F\): electromagnetic constitutive prefactor defined below

That split is what makes the model falsifiable. A formula that only “almost hits 376.73 Ω” is not a theory. A formula that predicts how \(\alpha\) must drift if \(n_M\) changes *is* a theory, because clocks and high-redshift spectra can kill it.

## 1.2 Correction A — the observed Φ is slightly wrong in the note

With CODATA 2022 values,

\[
\alpha_{\rm fs}=7.2973525643(11)\times 10^{-3},
\]

so

\[
\Phi_{\rm obs}=2\alpha_{\rm fs}=0.01459470513\ldots
\]

not \(0.014638\).

The SI number \(Z_0=376.730313412(59)\,\Omega\) is *not* “\(\alpha_{\rm fs}\).” It is a dimensionful quantity. After the 2019 SI revision, \(h\) and \(e\) are exact, so \(R_K\) is exact, while \(\mu_0\), \(\varepsilon_0\) and \(Z_0\) inherit the experimental uncertainty of \(\alpha_{\rm fs}\). The clean identity is

\[
\frac{Z_0}{2R_K}=\alpha_{\rm fs}.
\]

**Variable key**

- \(\mu_0\): vacuum permeability
- \(\varepsilon_0\): vacuum permittivity
- relation used implicitly: \(Z_0=\sqrt{\mu_0/\varepsilon_0}=\mu_0 c\)

Do not write “376.730 Ω is \(\alpha\).” Write the dimensionless ratio.

## 1.3 Correction B — 1/49 is not the nearest integer-square value

If the proposed integer structure is simply

\[
\Phi=\frac{1}{N^2},
\]

then the observed value implies

\[
\frac{1}{\sqrt{\Phi_{\rm obs}}}\approx 8.278.
\]

The nearest integer is \(N=8\), not \(N=7\):

| \(N\) | \(1/N^2\) | \(R_K/N^2\) | error vs \(Z_0\) |
|---|---|---|---|
| 8 | \(0.015625\) | \(\approx 403.33\,\Omega\) | \(\approx +7.06\%\) |
| 7 | \(1/49\approx 0.020408\) | \(\approx 526.79\,\Omega\) | \(\approx +39.8\%\) |

So “nearest square is 49” should be deleted unless \(N_\tau=7\) is independently required by TSB geometry. An eight-phase \(1/8^2\) suppression is numerically closer. That is interesting because E8 / eight-phase language already exists in the architecture. It is not a derivation; it is a better target than 49.

## 1.4 Correction C — the clock lock is algebraically over-constrained

The note writes both

\[
c=\frac{\alpha_{\rm chord}\,r_M}{\Delta t_\tau}
\]

and

\[
\Delta t_\tau=\frac{2r_M}{c}.
\]

**Variable key**

- \(\alpha_{\rm chord}\): dimensionless chord factor along the Mirron path
- \(r_M\): Mirron radius / cell size
- \(\Delta t_\tau\): Tav / bounce tick
- \(c\): invariant light speed

Substitute the second into the first:

\[
c=\frac{\alpha_{\rm chord}\,r_M}{2r_M/c}
\qquad\Rightarrow\qquad
\alpha_{\rm chord}=2
\]

identically. Then \(2\pi\) and \(2\pi/7\) cannot remain alternative chord factors *with the same frozen diameter-bounce tick*. Either:

- the tick definition changes with path geometry, or
- the chord factor is locked to 2.

This is not a philosophical objection. It is an identity. One of the two assumptions has to go.

## 1.5 Dimensional analysis: sound, but do not overclaim it

If the only dimensionful quantities allowed in the impedance law are \(h\), \(e\), \(n_M\) and \(r_M\), then

\[
Z_0=R_K\,\Phi(f),\qquad f\sim n_M r_M^3
\]

is the general form, because \(R_K=h/e^2\) already supplies ohms and \(f\) is dimensionless.

Dimensional analysis does **not** derive \(\Phi\). Once eight-phase / E8 / six-domain geometry is admitted, more dimensionless structure exists: phase angles, integer multiplicities, orientation tensors, topology. A more honest statement is

\[
Z_0=R_K\,\Phi(f;\mathcal G),
\]

where \(\mathcal G\) is the locked discrete geometry. If \(\mathcal G\) has no free parameters, that is fine. It should not be hidden by calling \(f\) the only possible input.

## 1.6 The right field-theory bridge

“Change \(Z_0\) without changing the null cone” is not inconsistent. In a relativistic effective theory the clean object is a scalar dressing of Maxwell:

\[
S_{\rm EM}=-\frac14\int d^4x\,\sqrt{-g}\,B_F(f)\,F_{\mu\nu}F^{\mu\nu}.
\]

**Variable key**

- \(S_{\rm EM}\): electromagnetic action
- \(g=\det(g_{\mu\nu})\): metric determinant
- \(B_F(f)\): dimensionless constitutive prefactor that can depend on Mirron filling
- \(F_{\mu\nu}\): Faraday tensor

Locally this behaves as

\[
\varepsilon_{\rm eff}\propto B_F,\qquad
\mu_{\rm eff}\propto B_F^{-1},
\]

which implies

\[
\varepsilon_{\rm eff}\mu_{\rm eff}=\text{constant},\qquad
c=\text{constant},\qquad
Z\propto B_F^{-1}.
\]

That is exactly the intended TSB move: impedance can run, the light cone need not. Bekenstein-type varying-\(\alpha\) theories use this structure while keeping gauge invariance and local Lorentz covariance.

In that language

\[
\Phi(f)\propto B_F(f)^{-1},\qquad
\xi=-\frac{d\ln B_F}{d\ln n_M}.
\]

The real job of the 8-phase cell calculation is therefore to derive \(B_F(f)\) from the cell, not merely a circuit resistance.

## 1.7 Clocks kill unscreened Branch B

A multi-year \(^{171}\mathrm{Yb}^+\) comparison gives

\[
\frac{\dot\alpha}{\alpha}=1.0(1.1)\times 10^{-18}\,\mathrm{yr}^{-1}
\]

(Lange et al., Phys. Rev. Lett. 126, 011102 (2021)). Using \(10^{-18}\,\mathrm{yr}^{-1}\) as the experimental scale is justified.

If Mirron density tracks ordinary Hubble dilution,

\[
\frac{\dot n_M}{n_M}=-3H,
\]

and if \(\xi=-1/3\) (the G2 / Branch B choice), then

\[
\frac{\dot\alpha}{\alpha}=H\sim 7\times 10^{-11}\,\mathrm{yr}^{-1}.
\]

That is about \(7\times 10^7\) times the clock bound. Unscreened Branch B is catastrophically incompatible with present drift measurements.

**Qualification, and it matters.** Atomic clocks constrain the *local terrestrial* value of \(\dot\alpha\). To convert that into \(\dot n_M/n_M=-3H\) you must assume Mirron density still tracks the cosmological FLRW density inside the Solar System. If Mirrons cluster, bind, screen, or otherwise decouple locally, the translation changes. Call the clock exclusion:

> conditional on locally homogeneous Hubble dilution

not model-independent.

## 1.8 Cosmology kills the same branch even more cleanly

If \(n_M\propto a^{-3}\) and \(\xi\) is constant,

\[
\frac{\alpha(z)}{\alpha_0}=(1+z)^{3\xi}.
\]

For G2, \(\xi=-1/3\),

\[
\frac{\alpha(z)}{\alpha_0}=\frac{1}{1+z}.
\]

At \(z=3\), \(\alpha\) would be only 25% of today’s value. JWST [O III] and other high-\(z\) absorption/emission constraints find no variation at roughly the \(10^{-4}\) level out to \(z\sim 9\). Cosmological data alone kill a simple constant-\(\xi=-1/3\), no-nucleation history by many orders of magnitude, independently of the local-clock caveat.

## 1.9 Branch A becomes interesting — and acquires a tuning problem

Write the proper continuity equation

\[
\dot n_M+3H n_M=\Gamma.
\]

Then

\[
\frac{\dot\alpha}{\alpha}=\xi\left(\frac{\Gamma}{n_M}-3H\right).
\]

**Variable key**

- \(\Gamma\): nucleation source term (number per volume per time)
- the parenthesis is the fractional departure from pure Hubble dilution

For \(|\xi|\sim 1\), clocks require \(\Gamma\) to track \(3H n_M\) to a few parts in \(10^9\). If \(\Gamma=3H n_M\) is a geometric identity, that is acceptable. If it is a dynamical coincidence, it is a serious tuning problem. The next cosmological derivation must explain *why* nucleation locks to the expansion rate and where the associated stress–energy comes from.

## 1.10 Maxwell–Garnett is the wrong ontology, not a useless calculation

Rejecting Maxwell–Garnett as “inclusions in a pre-existing Maxwell host” is correct if Mirrons are supposed to *generate* the electromagnetic vacuum. A discrete Mirron network still needs a micro-to-macro homogenization. The quantity wanted from the eight-phase cell is its low-energy constitutive tensor. Ideally it reduces to

\[
\chi^{\mu\nu\rho\sigma}
=B_F(f)\bigl(g^{\mu\rho}g^{\nu\sigma}-g^{\mu\sigma}g^{\nu\rho}\bigr)
\]

plus extremely suppressed corrections.

**Variable key**

- \(\chi^{\mu\nu\rho\sigma}\): constitutive tensor mapping \(F\) to the induction tensor
- extra orientation-dependent pieces would produce anisotropy, birefringence, or energy-dependent photon speed

Astrophysical polarization and gamma-ray observations put very strong limits on Lorentz-violating photon terms. Those corrections are not optional decorations. They are a failure mode.

## 1.11 The honest next step for Note 1

\[
\text{8-phase Mirron cell}
\;\longrightarrow\;
\mathcal L_{\rm EM}^{\rm eff}
\;\longrightarrow\;
B_F(f)
\;\longrightarrow\;
\Phi(f)
\;\longrightarrow\;
\alpha_{\rm fs}.
\]

The cell calculation must produce three things at once:

1. the normalization \(2\alpha_{\rm fs}=0.014594705\ldots\)
2. the susceptibility \(\xi\)
3. suppression of unwanted dispersion / birefringence

If it does that without hiding \(\alpha\) inside \(r_M\), a fitted phase angle, or some other input, it is a genuine derivation. If \(r_M=6.302\times 10^{-16}\,\mathrm{m}\) was itself inferred from an electromagnetic or nuclear observable that already contains \(\alpha_{\rm fs}\), the derivation is circular. Trace that length before running the cell calculation.

**Part-1 verdict.** The susceptibility / nucleation argument is now useful. The normalization remains unsolved. That is a better scientific position than a premature match to \(376.73\,\Omega\).

---

# Part 2 — Gravity architecture

## 2.1 What the reviewer is actually saying

The gravity note is more structurally interesting than the impedance note, and also more incomplete. As written it is a partially specified speculative architecture, not yet a gravitational theory. There are two mathematical errors, one severe phenomenological conflict, and several places where the proposed mechanism can be made rigorous.

## 2.2 Mathematical error: the displayed field equation cannot be correct

The note writes something of the form

\[
G_{\mu\nu}^{(\mathrm{eff})}
=\bigl\langle C_{\mu\nu\rho\sigma}\bigr\rangle_{\rm twistor}
+8\pi G\sum_{i=2}^{6}\bigl\langle T_{\mu\nu}^{(i)}\bigr\rangle.
\]

That cannot be literal, because

- \(G_{\mu\nu}\) is rank 2,
- \(C_{\mu\nu\rho\sigma}\) is rank 4.

Averaging does not delete two indices. If the twistor operation is a projection, write the projection:

\[
\mathcal E_{\mu\nu}
=\bigl\langle C_{\mu\alpha\nu\beta}\,n^\alpha n^\beta\bigr\rangle_{\rm twistor}
\]

or an equivalent contraction that actually returns a rank-2 tensor.

**Variable key**

- \(G_{\mu\nu}^{(\mathrm{eff})}\): claimed effective Einstein tensor
- \(C_{\mu\nu\rho\sigma}\): Weyl curvature
- \(n^\alpha\): some twistor / observer / null vector used to contract
- \(T_{\mu\nu}^{(i)}\): stress tensor of domain \(i\)
- \(\langle\cdot\rangle_{\rm twistor}\): the still-unspecified averaging map

## 2.3 Weyl tensor ≠ Weyl gravity

Presence of the Weyl tensor does not make a theory conformal / Weyl gravity. Four-dimensional conformal gravity comes from a Weyl-squared action

\[
S_{\rm CG}\propto\int d^4x\sqrt{-g}\,C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma},
\]

and its metric field equation involves the Bach tensor \(B_{\mu\nu}\), not \(C_{\mu\nu\rho\sigma}\) itself.

This gives TSB a clean fork.

**Fork A — gravity is fundamentally conformal at the macroscopic level**

\[
4\alpha_g B_{\mu\nu}=T_{\mu\nu}^{\rm eff}.
\]

**Fork B — gravity comes from the displayed 5D Einstein–Hilbert action**

Then call it a 5D Einstein / Kaluza–Klein theory with a projected Weyl contribution. Do not call the dynamics Weyl gravity unless the Weyl-squared effective action is actually derived.

## 2.4 The stated 5D action does not currently produce the claimed theory

Starting from

\[
S_5=\frac{1}{16\pi G_5}\int d^5x\sqrt{-g_5}\,R_5
\]

and compactifying an ordinary circle generically yields:

- a 4D gravitational tensor sector,
- a KK vector,
- a radion / scalar.

**Variable key**

- \(G_5\): 5D gravitational coupling
- \(g_5\): 5D metric determinant
- \(R_5\): 5D Ricci scalar

It does not become conformal gravity by time averaging. Nothing in that action currently supplies:

- six domain stress tensors,
- seventh-phase fluid,
- radius stabilization,
- octonionic phase dynamics,
- the CT boundary condition.

Those ingredients need either terms in \(S_5\) or a derivation showing they emerge from its fields. Useful discipline:

> Make everything come from one action. If it cannot yet be put in the action, mark it as a constitutive / postulated rule, not derived geometry.

## 2.5 The \(7h^{-1}\,\mathrm{Mpc}\) KK radius is the hardest phenomenological problem

If \(\tau=7h^{-1}\,\mathrm{Mpc}\) is literally the radius of a conventional compact metric dimension, then at distances \(r\ll\tau\) gravity sees the extra dimension and acquires KK corrections.

For \(h\sim 0.7\),

\[
\tau\sim 10\,\mathrm{Mpc}\sim 3\times 10^{23}\,\mathrm{m}.
\]

Laboratory inverse-square-law tests constrain a single flat extra dimension to roughly tens of microns. Lee et al. (2020) and PDG summaries quote about

\[
R\lesssim 30\,\mu\mathrm{m}
\]

for one toroidal extra dimension. The discrepancy is about

\[
10^{28}
\]

in radius.

The first KK energy would be only

\[
\frac{\hbar c}{\tau}\sim 6\times 10^{-31}\,\mathrm{eV}.
\]

The spectrum would contain an almost continuous tower of extraordinarily light gravitational modes. Wording cannot patch this. One of two things must change:

1. Tav is a genuine geometric fifth dimension — then TSB needs an explicit localization / warping / decoupling mechanism that prevents those KK modes from altering measured gravity.
2. Tav is an internal phase / resonance coordinate rather than a traversable metric dimension — then writing it as an ordinary macroscopic KK \(S^1\) inside \(\int d^5x\sqrt{-g_5}R_5\) is misleading.

Interpretation (2) is probably closer to what the architecture wants to be.

## 2.6 Ordinary Casimir energy at 10 Mpc cannot be dark energy

For an ordinary compact \(S^1\), the 4D Casimir potential scales as

\[
\rho_{\rm Cas}\sim\frac{1}{R^4}
\]

up to field-content coefficients. At \(R\sim 10\,\mathrm{Mpc}\),

\[
R^{-1}\sim 6\times 10^{-31}\,\mathrm{eV},
\qquad
\rho_{\rm Cas}\sim 10^{-121}\,\mathrm{eV}^4.
\]

Observed dark-energy density is about \(10^{-11}\,\mathrm{eV}^4\). Ordinary Casimir from this cosmological circle undershoots by about

\[
10^{110}.
\]

“Casimir pressure of the circle cannot die” may be mathematically true in the sense of remaining nonzero. It cannot supply a phenomenologically significant late-time floor without an enormous amplification mechanism, or a nonstandard topological term that is *not* ordinary KK Casimir energy.

## 2.7 The cosmic-web connection is suggestive, not an exact lock

There really are contemporary cosmic-web statistics of that order: typical filament widths around \(1h^{-1}\,\mathrm{Mpc}\) and median distances of order \(7h^{-1}\,\mathrm{Mpc}\) from non-web regions to the nearest web particle. Other analyses find filament sizes and lengths that depend strongly on smoothing scale, tracer density, and web-finding algorithm.

Therefore

> “the cosmic web therefore fractures at exactly \(7h^{-1}\,\mathrm{Mpc}\)”

is too strong.

A good test exists: freeze the TSB definition of “fracture” mathematically *before* looking at the catalogue, then measure that exact statistic in DESI / simulations. If it independently peaks at the predicted scale, that is evidence. Noticing after the fact that several web dimensions are of order 7 Mpc is not.

## 2.8 Virtual pairs need to become a field

Calling a TSB excitation something other than a conventional virtual particle is allowed. Making ordinary off-shell states ontic is not free: off-shell Green functions can depend on gauge fixing. Special constructions are required to make off-shell quantities gauge independent.

Do not stop at the slogan

\[
|\bar\psi,-t\rangle\;\longrightarrow\;|\psi,+t\rangle
\]

is “a real virtual particle.” Define a genuine TSB field \(\Psi(x,y,\phi)\) with an action and a boundary condition, for example

\[
\Psi(x,y,\phi+4)=\mathcal{CT}\,\Psi(x,y,\phi),
\]

or whatever the exact octonionic topology demands. The half-cycle lifetime should then emerge from the propagator or transfer operator.

That also forces a particle-physics test. “Up and Down are the same flux tube across the boundary” is not enough. The construction has to reproduce

\[
Q_u=+\tfrac23,\qquad Q_d=-\tfrac13,
\]

their common color representation, different weak-isospin components, hypercharges, chirality, masses, and CKM structure. If the geometry produces those rather than assuming them, the claim becomes substantive.

## 2.9 Phase 7 is one of the better-specified pieces

The fluid stress tensor

\[
T^{ab}_7=(\rho_7+P_7)u^a u^b+P_7 g^{ab}+\Pi\Delta^{ab},
\qquad
\Pi=-\zeta\theta
\]

is recognizable relativistic hydrodynamics.

**Variable key**

- \(\rho_7,P_7\): energy density and isotropic pressure of phase 7
- \(u^a\): four-velocity
- \(\Pi\): bulk viscous stress
- \(\Delta^{ab}=g^{ab}+u^a u^b\): projector orthogonal to \(u^a\)
- \(\zeta\): bulk viscosity
- \(\theta=\nabla_a u^a\): expansion scalar

\(\Pi=-\zeta\theta\) is a constitutive approximation, not microphysics. If the fluid operates at the fundamental refresh scale, promote \(\Pi\) to a dynamical variable, Israel–Stewart style:

\[
\tau_\Pi\, u^a\nabla_a\Pi+\Pi=-\zeta\theta+\cdots.
\]

Relativistic dissipative dynamics needs a relaxation time. Instantaneous viscosity is not enough.

There is a deeper tension that can become a feature. The microscopic PK / Mirron engine is described as CPT-symmetric, while \(\zeta>0\) produces entropy. That is not automatically contradictory: coarse-graining a reversible microscopic system can generate macroscopic dissipation. The twistor / time average then has to be the coarse-graining map that produces the arrow of time. Write that map.

## 2.10 Impulse-to-gravity is still an interpretation

Replace the non-covariant impulse

\[
\mathcal I=\int_{\Sigma_{\rm in}}T^{0i}\,d\Sigma_i
\]

with

\[
\Delta P^a=\int_{\Sigma_{\rm in}}T^{ab}n_b\,d\Sigma.
\]

**Variable key**

- \(\Sigma_{\rm in}\): incoming hypersurface
- \(n_b\): unit normal
- \(\Delta P^a\): four-impulse delivered through that surface

Then derive the chain

\[
\Delta P^a\;\longrightarrow\;\Pi\;\longrightarrow\;\Delta\theta\;\longrightarrow\;\Delta R_{\mu\nu}
\]

through Raychaudhuri or the effective gravitational field equations. Until that chain exists,

> “inertia becomes compression of space”

is an interpretation. After it exists, it is a mechanism.

## 2.11 Hidden \(2\pi\) inconsistency across the two notes

The gravity note identifies

\[
r_M=6.302\times 10^{-16}\,\mathrm{m}
\]

with the \(313.1\,\mathrm{MeV}\) scale. Numerically that length is

\[
r_M=\frac{\hbar c}{313.1\,\mathrm{MeV}},
\]

not \(hc/(313.1\,\mathrm{MeV})\). Therefore

\[
\frac{\hbar c}{r_M}=313.1\,\mathrm{MeV},
\qquad
\frac{hc}{r_M}=2\pi\times 313.1\,\mathrm{MeV}\approx 1.97\,\mathrm{GeV}.
\]

The impedance calculation previously used \(E_{\rm ch}=hc/r_M\). If that energy was intended to be the same 313.1 MeV floor, there is a factor-\(2\pi\) inconsistency. Because the impedance estimate is proportional to \(E_{\rm ch}\Delta t/e^2\), the factor propagates directly into claimed \(R_K\) multiples. Fix this before merging the gravity and impedance branches.

## 2.12 A \(\pi/2\) phase rotation does not, by itself, kill CTCs

\(\Delta\phi=\pi/2\) may help avoid returning to the same internal state. “Kills closed timelike curves” is a spacetime statement. What must be proved is existence of a global time function \(t(x)\) with \(\nabla_\mu t\) timelike everywhere, or some other stable-causality result for the PK metric. Local phase-space orthogonality is not sufficient.

Likewise, “topological exclusion prevents singularities” requires showing that curvature invariants remain finite and that causal geodesics extend through the would-be bounce.

## 2.13 Remove the CMS / LHCb “already seen” claim

No official CMS or LHCb result establishing a sevenfold residual periodicity in the relevant spectra is sitting in the collaboration papers. Independent analyses and unrelated uses of “folding” angular distributions are not TSB evidence. Until there is an exact dataset, fit model, null simulation, look-elsewhere correction, and a collaboration or peer-reviewed reference, put

> “7-fold residuals already noted in CMS muon / LHCb spectra”

in the hypothesis / test queue, not the evidence ledger.

## 2.14 Sharp research program for gravity

\[
S_{\rm fundamental}
\;\longrightarrow\;
\text{5D / phase reduction}
\;\longrightarrow\;
T_{\mu\nu}^{\rm eff}
\;\longrightarrow\;
\text{linearized spectrum}
\;\longrightarrow\;
\text{Newton / GR limit}
\;\longrightarrow\;
\text{cosmology}.
\]

The first calculation is not another phenomenological match. Take the proposed \(S_5\), specify the Tav coordinate and six-domain / phase boundary conditions, and actually perform the dimensional reduction. That calculation answers three decisive questions:

1. What propagates?
2. What is the correct 4D gravitational field equation?
3. Why does a \(7h^{-1}\,\mathrm{Mpc}\) internal scale not destroy local gravity?

If TSB can answer those three without inserting GR by hand, the architecture moves into a different category. That is the bottleneck — not the narrative around the half-bounce.

---

# Part 3 — Late-time cosmology and the Tav floor

## 3.1 What the reviewer is actually saying

The late-time cosmological logic is coherent *conditional on* a positive, stabilized Tav vacuum floor. That floor is not derived by the equations shown. Two useful predictions are hiding in the model and have not yet been exploited.

## 3.2 Central correction: KK reduction does not itself generate Casimir dark energy

The sentence

> “Reduction of 5D Einstein–Hilbert gravity on \(\mathbb{R}^3\times S^1\) produces a Casimir / vacuum pressure on the 4D slices”

is doing too much. Classical dimensional reduction of \(S_5\) produces tensor, vector, and scalar sectors. Casimir energy appears only after quantizing fields on the compact space and evaluating vacuum loops:

\[
V_{\rm Cas}(R)=\frac{C_{\rm spectrum}}{R^4}.
\]

**Variable key**

- \(C_{\rm spectrum}\): coefficient fixed by which fields wrap the circle, their statistics, masses, and boundary conditions
- \(R\) or \(\tau\): compactification radius

The correct TSB chain is

\[
S_5
\;\longrightarrow\;
\text{KK spectrum}
\;\longrightarrow\;
\Gamma_{\rm 1-loop}
\;\longrightarrow\;
V_{\rm eff}(\tau)
\;\longrightarrow\;
\rho_{\rm Tav}.
\]

You need

\[
V'_{\rm eff}(\tau)=0,\qquad V''_{\rm eff}(\tau)>0,
\]

and then

\[
\rho_{\rm Tav}=V_{\rm eff}(\tau)>0.
\]

Only after that does a frozen \(\tau\) behave as

\[
p_{\rm Tav}=-\rho_{\rm Tav},\qquad w_{\rm Tav}=-1.
\]

Casimir contributions are not automatically positive. Sign and magnitude both have to be earned.

## 3.3 Magnitude gap, restated

For \(\tau\sim 10\,\mathrm{Mpc}\),

\[
\frac{\hbar c}{\tau}\sim 6\times 10^{-31}\,\mathrm{eV},
\qquad
\rho_{\rm Cas}\sim\tau^{-4}\sim 10^{-121}\,\mathrm{eV}^4,
\]

versus

\[
\rho_{\rm DE}\sim 10^{-11}\,\mathrm{eV}^4.
\]

Gap: \(\sim 10^{110}\).

“Rigid topological Casimir pressure” must therefore mean something substantially different from ordinary KK Casimir vacuum energy. That is allowed as a new model, but then the topological term has to appear explicitly in the effective action. Calling ordinary compactification Casimir energy the source will not get the required magnitude. This is the single most important correction to the cosmology paper.

## 3.4 Same 10 Mpc gravitational KK problem as Part 2

If Tav is a conventional fifth metric dimension through which gravity propagates,

\[
m_{\rm KK}\sim\frac{\hbar}{c\tau}\sim 10^{-30}\,\mathrm{eV}.
\]

That is an enormous tower of essentially massless gravitational modes, in conflict with inverse-square-law tests at the tens-of-microns level.

Internally consistent interpretation:

> Tav should be an internal phase / topological coordinate, not an ordinary accessible KK spatial dimension.

Then \(7h^{-1}\,\mathrm{Mpc}\) can be a coherence length projected into 4D rather than the physical circumference along which an ordinary graviton propagates. That requires changing the geometry enough that the standard

\[
M_4^2\sim 2\pi\tau\, M_5^3
\]

relation no longer applies.

## 3.5 Dimensional error in the rotational term

The note writes

\[
H^2=\frac{8\pi G}{3}\rho_m+\frac{\Lambda_{\rm Tav}}{3}+\Omega_{\rm rot}(t)
\]

and then defines

\[
\Omega_{\rm rot}=\frac12\Bigl(\sum_i\gamma_i\Bigr)\omega^2 R_{\rm superblock}^2.
\]

**Variable key**

- \(H\): Hubble rate, \([H^2]=T^{-2}\)
- \(\rho_m\): matter density
- \(\Lambda_{\rm Tav}\): claimed Tav cosmological term
- \(\omega\): angular frequency of domain rotation
- \(R_{\rm superblock}\): superblock radius
- \(\gamma_i\): dimensionless weights

The left side has dimensions \(T^{-2}\). The combination \(\omega^2 R^2\) is a velocity squared, \(L^2 T^{-2}\). Those expressions cannot presently be the same physical quantity.

More important than units: \(\tfrac12 I\omega^2\)-type rotational energy does not automatically cause cosmic acceleration. Ordinary kinetic energy has positive energy density and pressure. In GR, acceleration requires

\[
\rho+3p<0.
\]

“Centrifugal force” intuition cannot be dropped into the Friedmann equation. What must be derived is

\[
T^{(5)}_{AB}(\text{domain rotation})
\;\longrightarrow\;
T_{\mu\nu}^{\rm rot,eff}
\;\longrightarrow\;
\{\rho_{\rm rot},\,p_{\rm rot}\}.
\]

Only if \(\rho_{\rm rot}+3p_{\rm rot}<0\) during the acceleration epoch does the rotational sector drive acceleration.

## 3.6 Clean Friedmann form

Write

\[
H^2=\frac{8\pi G}{3}\bigl(\rho_m+\rho_{\rm Tav}+\rho_{\rm rot}\bigr)-\frac{k}{a^2}.
\]

Conservation then forces

\[
\dot\rho_{\rm DE}+3H(\rho_{\rm DE}+p_{\rm DE})=0
\]

unless there is explicit energy exchange with other sectors.

## 3.7 The sine model hides a real DESI-facing prediction

Suppose

\[
\rho_{\rm DE}=\rho_{\rm Tav}+\rho_{\max}\sin\Bigl(\frac{\pi t}{T}\Bigr)
\]

with \(\rho_{\rm Tav}\) constant.

**Variable key**

- \(\rho_{\rm Tav}\): constant floor
- \(\rho_{\max}\): amplitude of the oscillatory piece
- \(T\): period of the six-domain separation cycle
- \(t\): cosmic time measured from a defined origin in that cycle

The effective equation of state is

\[
w_{\rm eff}
=-1
-\frac{(\pi\rho_{\max}/T)\cos(\pi t/T)}
{3H\bigl[\rho_{\rm Tav}+\rho_{\max}\sin(\pi t/T)\bigr]}.
\]

Signs:

- before maximum separation, \(\cos(\pi t/T)>0\) \(\Rightarrow\) \(w_{\rm eff}<-1\)
- at maximum separation, \(w_{\rm eff}=-1\)
- after maximum separation, \(\cos(\pi t/T)<0\) \(\Rightarrow\) \(w_{\rm eff}>-1\)

TSB does not merely predict “weakening dark energy.” It predicts a specific phantom-to-quintessence crossing:

\[
w<-1 \;\longrightarrow\; -1 \;\longrightarrow\; w>-1,
\]

tied to maximum six-domain separation.

That is relevant to DESI. Combined BAO + CMB + SN fits have repeatedly favored the quadrant

\[
w_0>-1,\qquad w_a<0,
\]

meaning a present-day value above \(-1\) with more negative \(w\) in the past. That is qualitatively the falling side of the sine. This is much more useful than saying “DESI sees rotational decay.” It is a fit target.

## 3.8 Update the DESI wording — and a small correction to the review itself

Do not write “DESI prefers weakening dark energy rather than \(\Lambda\)” as a settled fact. Preference is dataset-dependent.

As of late July / August 2026:

- DESI DR2 BAO combined with CMB has continued to allow evolving dark energy, typically in the \(w_0>-1\), \(w_a<0\) quadrant.
- The 29 July 2026 DESI DR2 Ly\(\alpha\) full-shape / Alcock–Paczynski paper (arXiv:2607.27410) still reports evolving DE preferred at about \(2.7\sigma\) for DESI+CMB and \(3.2\sigma\) when supernovae are included. It also shifts \(\Omega_m\) and slightly reduces a CMB tension inside \(\Lambda\)CDM.
- Other combinations, and some SN-sample choices, weaken the preference back toward inconclusive.

So the reviewer’s phrase that the July 2026 Ly\(\alpha\) result “moved toward the \(\Lambda\)CDM prediction” is only half right. The paper itself still quotes a several-sigma preference in some combinations, while DESI-adjacent commentary correctly warns that the hint can weaken as data improve or that a more complicated model may be required.

Safe TSB wording:

> TSB predicts a particular evolving-DE trajectory that can be tested against DESI.

Unsafe wording:

> DESI is observing TSB rotational decay.

The first survives if the data move. The second does not.

## 3.9 A positive floor does not automatically prove “no crunch”

For

\[
H^2=\frac{8\pi G\rho_{m0}}{3a^3}-\frac{k}{a^2}+\frac{\Lambda_{\rm Tav}}{3},
\]

a positive asymptotic \(\Lambda_{\rm Tav}\) dominates at sufficiently large \(a\). That does not by itself prove an expanding closed solution cannot hit \(H=0\) before reaching that asymptotic region. For the observed near-flat expanding branch this may be easy to exclude — but TSB should demonstrate

\[
H^2(a)>0\qquad\forall a>a_0.
\]

Then the no-recollapse statement is rigorous.

## 3.10 The displayed equations do not generate the BOOM

If the rotational term goes to zero,

\[
H^2\;\longrightarrow\;\frac{8\pi G}{3}\rho_m+\frac{8\pi G}{3}\rho_{\rm Tav}.
\]

Eventually

\[
H\;\longrightarrow\;\sqrt{\frac{8\pi G\rho_{\rm Tav}}{3}}
\]

and the solution approaches ordinary de Sitter-like expansion. Nothing in that equation triggers a BOOM. The BOOM is presently an additional postulate, not a consequence of rotational decay.

TSB needs an event condition, for example

\[
\mathcal F(\phi_{\rm Tav},\,\omega,\,n_{\rm hier},\,\ldots)=0,
\]

followed by matching conditions

\[
(g_{\mu\nu},K_{\mu\nu},\Psi)_-
\;\longrightarrow\;
(g_{\mu\nu},K_{\mu\nu},\Psi)_+.
\]

Otherwise the cycle ends mathematically in eternal Tav-supported expansion, not another aeon.

## 3.11 Three different “cycles” are being mixed

Distinguish:

1. cyclic internal phase (142857 / octonionic clock),
2. cyclic dark-energy amplitude (the sine),
3. cyclic spacetime / aeons (scale factor turning around or conformal resurgence).

The sine establishes (2). The internal clock may establish (1). Neither automatically establishes (3).

If \(a(t)\) never decreases and never reaches zero, the universe is not cyclic in the conventional scale-factor sense. It can instead be a monotonically expanding spacetime with recurrent internal conformal state transitions. That may be the cleaner TSB claim. Do not call it a bounce cosmology until \(a(t)\) or a conformal factor actually turns over under derived matching conditions.

## 3.12 The calculation that would actually settle Part 3

\[
S_5
\;\longrightarrow\;
V_{\rm eff}(\tau,\phi,\omega)
\;\longrightarrow\;
\{\rho_{\rm Tav},\,\rho_{\rm rot},\,p_{\rm rot}\}
\;\longrightarrow\;
H(z),\,w(z)
\]

with four non-negotiable outputs:

1. \(V'_{\rm eff}(\tau)=0\)
2. \(V_{\rm eff}(\tau)>0\)
3. \(m_{\rm radion}^2>0\)
4. \(\rho_{\rm rot}+3p_{\rm rot}<0\) during the purported acceleration epoch

Then take the resulting — not assumed — \(H(z)\) and fit it to DESI.

The sine version already gives TSB an identifiable prediction: one \(w=-1\) crossing tied exactly to maximum six-domain separation. DESI’s currently preferred \(w_0>-1\), \(w_a<0\) direction is qualitatively compatible with being on the post-crossing side. That is a test, not a confirmation.

**Part-3 verdict.** Rotational-decay phenomenology could be testable. The Tav dark-energy floor has not yet been derived from the stated 5D action. That is the piece to attack first. If core papers contain an explicit one-loop Tav potential or a nonstandard topological term that changes the \(1/\tau^4\) result, that derivation is the part worth pulling out next.

---

# Independent analysis

The restatement above follows the reviewer closely. This section is the assessment of that review, not another paraphrase.

## A. The review is mostly right, and it is the right *kind* of right

The important methodological move in all three notes is the same: stop treating a narrative identification as a derivation.

| Claim type in the notes | Reviewer’s demand | Why that demand is correct |
|---|---|---|
| \(Z_0\) “comes out of” the cell | produce \(B_F(f)\), then \(\Phi\), then \(\alpha\) | otherwise \(\alpha\) can be hidden in an input |
| gravity “is Weyl” because \(C_{\mu\nu\rho\sigma}\) appears | write a rank-2 field equation from an action | tensors of different rank cannot be set equal |
| Tav “is Casimir dark energy” | derive \(V_{\rm eff}\) with a minimum and the right magnitude | classical KK reduction does not invent \(\Lambda\) |
| rotation “causes acceleration” | compute \(\rho+3p\) | kinetic energy normally decelerates |
| clocks / JWST / DESI “already confirm TSB” | state the actual bound and the actual combination | overclaiming is how a model becomes unfalsifiable in the wrong direction |

That is ordinary theoretical hygiene. It is also the only way TSB can become a competitor to \(\Lambda\)CDM + WIMPs rather than a private architecture.

## B. Ranking the problems by lethality

Not every objection is equally fatal. Ordered by “the theory cannot proceed until this is faced”:

**1. What is Tav, geometrically?**  
If Tav is a metric \(S^1\) of radius \(10\,\mathrm{Mpc}\), local gravity is destroyed and ordinary Casimir energy is \(10^{110}\) too small. If Tav is an internal phase / coherence coordinate, the 5D Einstein–Hilbert writing is the wrong starting action, or at least the wrong interpretation of that action. Every later cosmological formula inherits this choice. Decide it in print.

**2. One action, or an explicit list of postulates.**  
Six-domain stress, Phase-7 viscosity, CT boundary conditions, nucleation \(\Gamma=3Hn_M\), and the BOOM matching conditions are currently extra structure. That is allowed. It is not allowed to speak as if they fell out of \(S_5\).

**3. Rank and conformal-gravity language.**  
\(G_{\mu\nu}=\langle C_{\mu\nu\rho\sigma}\rangle\) is not an equation. Either derive a Bach equation from a \(C^2\) action, or derive a projected Einstein equation from 5D EH, or write a new tensor \(\mathcal E_{\mu\nu}\) and justify it. Mixed language will not survive a referee.

**4. Circularity audit of \(r_M\).**  
If \(r_M\) was back-solved from a hadronic or electromagnetic scale that already contains \(\alpha_{\rm fs}\) or \(hc\) vs \(\hbar c\) confusion, the impedance program cannot derive \(\alpha\). This audit is cheap and should be done before any 8-phase cell computation.

**5. The \(2\pi\) / \(hc\) vs \(\hbar c\) split.**  
This is not deep, but it is contagious. It couples the impedance numbers to the 313.1 MeV identification. Fix it once, globally.

**6. Branch B is dead as a simple history.**  
Clocks and high-\(z\) \(\alpha\) constraints really do kill \(\xi=-1/3\) with \(n_M\propto a^{-3}\) and no nucleation. That is a successful use of the new susceptibility language. Keep Branch B only if screening / binding is specified well enough to change \(\dot n_M/n_M\) locally *and* at \(z\sim 3\)–\(9\).

**7. DESI is a target, not a trophy.**  
The sine-crossing prediction is the best phenomenological sentence in the three notes. Treat it as a template for \(w(z)\), then fit. Do not announce that DESI has seen domain rotation.

**8. CMS / LHCb sevenfold residuals.**  
Park them. A wrong evidence claim is more damaging than silence.

**9. Maxwell–Garnett, CTC slogans, “exactly 7 Mpc fracture.”**  
These are wording and ontology issues. Important, not the first calculation.

## C. Where the reviewer is slightly too sharp, or incomplete

1. **Nearest-integer rhetoric.** The reviewer is correct that \(N=8\) is closer than \(N=7\) for \(\Phi=1/N^2\). TSB is not obligated to use that ansatz. If the geometry produces \(\Phi=2\alpha_{\rm fs}\) by a different combination of multiplicities — for example an 8-phase factor times a 7-fold Tav factor times a filling function \(f\) — then comparing raw \(1/49\) to \(1/64\) is the wrong test. The fair demand is: state the actual discrete formula before calling anything “nearest.”

2. **Clock exclusion is conditional, as the reviewer already says.** The qualifier is not a loophole unless the local Mirron sector is actually modeled. “Mirrons screen in the Solar System” is a new theory, not a parenthetical.

3. **July 2026 DESI Ly\(\alpha\).** The reviewer’s caution is right; the implication that Ly\(\alpha\) has walked the hint back to \(\Lambda\)CDM is too strong relative to arXiv:2607.27410, which still quotes \(2.7\sigma\)–\(3.2\sigma\) preferences in standard combinations. TSB should track the *combination*, not a single sentence from a press note.

4. **“Not yet a gravitational theory” is fair as a status label, not as a dismissal.** Many working effective field theories began as constitutive architectures. The label is a to-do list.

5. **Conformal gravity vs Einstein/KK is a fork, not an accusation.** TSB can pick either, or a hybrid in which conformal structure appears only after twistor averaging. It cannot keep both slogans and one action unless the reduction is shown.

## D. What “human readable” means for the next draft of the notes

A readable TSB note would open each section with four sentences:

1. What object is being defined.
2. What action or constitutive rule it comes from.
3. What observable it changes.
4. What observation can kill it.

Example, impedance:

1. Object: constitutive prefactor \(B_F(f;\mathcal G)\).
2. Source: 8-phase Mirron cell, not Maxwell–Garnett inclusions.
3. Observables: \(Z_0/R_K\) today, \(\dot\alpha/\alpha\) now, \(\alpha(z)/\alpha_0\) at high redshift, photon birefringence.
4. Killers: Yb\(^+\) clocks, JWST [O III], gamma-ray polarization / speed tests, and a circular \(r_M\).

Example, cosmology:

1. Object: \(V_{\rm eff}(\tau,\phi,\omega)\).
2. Source: whatever replaces ordinary \(1/\tau^4\) Casimir — must be named.
3. Observables: \(w(z)\), \(H(z)\), whether \(w\) crosses \(-1\) at maximum domain separation.
4. Killers: DESI+CMB+SN combinations, local inverse-square-law tests if Tav is metric, radion stability.

If a paragraph cannot supply those four sentences, it is still architecture.

## E. Recommended calculation order

Do these in this order. Later items inherit earlier choices.

1. **Provenance of \(r_M\).** Write the exact chain from geometry or from the 313.1 MeV identification, including \(\hbar c\) versus \(hc\).
2. **Decide Tav’s ontological status** (metric dimension vs internal phase) and rewrite \(S_5\) accordingly.
3. **Dimensional reduction of that action.** Extract the 4D field content and the linearized spectrum. This answers “what propagates?” and “why Newton’s law survives.”
4. **Effective Maxwell sector from the 8-phase cell.** Target \(B_F(f;\mathcal G)\), not a resistor. Demand suppression of birefringence.
5. **Continuity equation for \(n_M\).** Either derive \(\Gamma=3Hn_M\) geometrically or introduce screening and accept the local/cosmological split.
6. **Rotational stress tensor.** Compute \(\rho_{\rm rot}+3p_{\rm rot}\). If it is not negative, rotation is not dark energy.
7. **Effective potential \(V_{\rm eff}(\tau)\).** Minimum, positive value, radion mass. If the value is not \(\sim 10^{-11}\,\mathrm{eV}^4\), ordinary Casimir language must be abandoned in public drafts.
8. **Predict \(w(z)\) from the sine or from \(V_{\rm eff}\), then fit DESI.** Freeze the crossing condition before the fit.
9. **BOOM matching conditions** only after (7) and (8). Do not attach a new aeon to an equation that relaxes to de Sitter.
10. **CMS / LHCb test design** only after the cell calculation predicts a specific residual, not a verbal “sevenfold.”

## F. What is already worth keeping

These pieces survive the review and should not be thrown out with the broken equations:

- Splitting normalization \(\Phi\) from susceptibility \(\xi\). That is the first falsifiable electromagnetic statement TSB has had.
- The effective-action form \(B_F(f)F_{\mu\nu}F^{\mu\nu}\) as the bridge to varying-\(\alpha\) literature.
- Phase-7 viscous hydrodynamics as a recognizable continuum limit, provided it is given a relaxation time.
- The sine-model \(w_{\rm eff}\) crossing as a DESI template.
- The insistence that nucleation, if it cancels Hubble dilution, must be geometrically locked rather than tuned.
- The instinct that Tav is probably *not* an ordinary laboratory extra dimension. Follow that instinct into the action.

## G. One-sentence status for each note

**Impedance note.** Scientifically improved. Normalization unsolved. Susceptibility already predictive enough to kill simple Branch B.

**Gravity note.** Architecture, not yet a theory. Field equation is ill-posed as written. 10 Mpc metric KK is phenomenologically impossible without a decoupling mechanism.

**Cosmology note.** Conditional logic is clear. Floor is not derived. Best unexploited prediction is the phantom-to-quintessence crossing at maximum domain separation.

**Joint status.** TSB is in the correct uncomfortable place: the easy numerical coincidences have been taken off the table, and the next papers have specific ways to fail. That is progress.

---

## Verified external numbers used in this session

| Quantity | Value | Source |
|---|---|---|
| \(\alpha_{\rm fs}\) | \(7.2973525643(11)\times 10^{-3}\) | CODATA 2022 |
| \(\alpha_{\rm fs}^{-1}\) | \(137.035999177(21)\) | CODATA 2022 |
| \(Z_0\) | \(376.730313412(59)\,\Omega\) | CODATA 2022 |
| \(R_K\) | \(25812.80745\ldots\,\Omega\) (exact from \(h,e\)) | 2019 SI / CODATA 2022 |
| \(\dot\alpha/\alpha\) | \(1.0(1.1)\times 10^{-18}\,\mathrm{yr}^{-1}\) | Lange et al., PRL 126, 011102 (2021), Yb\(^+\) E3/E2 |
| One flat extra dimension | \(R\lesssim 30\,\mu\mathrm{m}\) | Lee et al. 2020; PDG extra-dimension summaries |
| DESI DR2 Ly\(\alpha\) AP | evolving DE preferred at \(2.7\sigma\) (DESI+CMB), \(3.2\sigma\) (+SN) in that paper’s combinations | arXiv:2607.27410 (29 Jul 2026) |

---

## File location

- Project path: `Tau-Superblock-Universe/Personal-Files/2026-09-19_TSB-three-notes-critique-readable-analysis.md`
- Session saved: 19 September 2026
