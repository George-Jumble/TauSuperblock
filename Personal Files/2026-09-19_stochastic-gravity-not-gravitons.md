# The micron bound does not assume gravitons

**Session date:** 19 September 2026  
**Question:** Is the extra-dimension / warp / localization critique only there because gravitons were posited? TSB has no gravitons; gravity is stochastic.  
**Short answer:** The wording used KK gravitons because that is the usual extra-dimension dialect. The laboratory bound itself is on the *force law*, not on a spin-2 particle. Stochastic gravity does not automatically evade it. It evades it only if Tav is not a direction along which the gravitational impulse / metric / noise can spread.

---

## Variable key

| Symbol | Meaning |
|---|---|
| \(V(r)\) | potential energy between two laboratory masses |
| \(\alpha,\lambda\) | strength and range of a Yukawa correction to Newton’s law |
| \(\delta\) | number of extra spatial dimensions gravity can enter |
| \(R\) or \(\tau\) | size of a compact extra direction, if gravity spreads into it |
| \(G_{\mu\nu}\) | Einstein tensor, if a metric description is used |
| \(\xi_{\mu\nu}\) | stochastic source in an Einstein–Langevin equation |
| \(N_{\mu\nu\rho\sigma}(x,x')\) | noise kernel (two-point correlator of \(\xi\)) |
| \(\mathcal K(x,x')\) | TSB impulse propagator: how a stress increment at \(x'\) changes geometry / acceleration at \(x\) |
| \(\ell_C\) | correlation length of the noise or impulse kernel |
| \(\phi\) | Tav coordinate |

---

## 1. What Cavendish experiments actually constrain

Eöt-Wash / torsion-balance tests do not search for gravitons. They hang two macroscopic masses and ask whether the force is

\[
V(r)=-\frac{GMm}{r}
\]

or something else at separations from millimeters down to tens of microns.

The usual fit form is

\[
V(r)=-\frac{GMm}{r}\Bigl(1+\alpha\,e^{-r/\lambda}\Bigr).
\]

**Key:** \(\alpha\) is the relative strength of the extra piece; \(\lambda\) is its range. For one extra flat spatial direction that gravity can enter, \(\alpha\) is order unity and \(\lambda\sim R\). Present limits give \(R\lesssim 30\,\mu\mathrm{m}\) in that interpretation.

No quantization was used. No spin-2 particle was used. The input is a measured acceleration.

So: *not* “because gravitons were posited.” Because two masses attract as \(1/r^2\) down to tens of microns.

---

## 2. Where the graviton wording came from, and how to drop it

If you start from a 5D Einstein–Hilbert action

\[
S_5=\frac{1}{16\pi G_5}\int d^5x\sqrt{-g_5}\,R_5
\]

and let the metric depend on a compact coordinate \(\phi\) of radius \(\tau\), then *classically* — waves, not particles — the 4D linearized field splits into a massless 4D metric plus a tower of massive spin-2 fields with

\[
m_n=\frac{n}{\tau}.
\]

People call those “KK gravitons.” That is jargon. The same fact in metric language is:

> gravitational disturbances can vary along \(\phi\), so the 4D potential is no longer pure \(1/r^2\) on scales \(\lesssim\tau\).

The same fact in Gauss-law language is:

> if flux can spread into an extra spatial direction, then for \(r\ll\tau\)

\[
F\propto\frac{1}{r^{2+\delta}}.
\]

The same fact in TSB-native language should be:

> if the impulse propagator \(\mathcal K(x,x')\) can connect two 4D points by a path that winds in \(\phi\) over a length \(\tau\), then laboratory masses see that extra channel.

Refuse the word “graviton.” Keep the question about \(\mathcal K\).

---

## 3. What “gravity is stochastic” does and does not buy

Stochastic gravity, in the Hu–Verdaguer sense, replaces

\[
G_{\mu\nu}=8\pi G\,T_{\mu\nu}
\]

with an Einstein–Langevin equation

\[
G_{\mu\nu}=8\pi G\bigl(T_{\mu\nu}+\xi_{\mu\nu}\bigr),
\]

where \(\xi_{\mu\nu}\) is a colored noise whose correlator \(N_{\mu\nu\rho\sigma}(x,x')\) is fixed by the quantum stress tensor of matter.

That framework:

- does **not** require gravitons as particles,
- still has a metric,
- still predicts a mean Newtonian potential,
- still predicts fluctuations around that potential.

If TSB’s stochastic gravity is this kind of theory, laboratory tests constrain the *mean* kernel, not a graviton.

If TSB’s stochastic gravity is more radical — no metric field, only averaged Mirron impulses — then write the object that replaces the metric. Call it \(\mathcal K(x,x')\). Cavendish still constrains \(\mathcal K\) between two laboratory worldlines at \(r\sim 50\,\mu\mathrm{m}\).

Stochasticity changes how you talk about fluctuations. It does not, by itself, cancel extra channels in the mean force.

---

## 4. The real fork, restated without gravitons

The four bullets from the previous note were not four graviton stories. They were four stories about whether gravity can move in \(\phi\). Without particles they read:

**1. Warp factor \(A(y)\).**  
A position-dependent redshift in the *mean* geometry, so that extra-direction gradients cost more than \(1/\tau\) or barely overlap laboratory matter. Still a metric statement. Unused if TSB has no extra metric direction.

**2. Localization of stress-energy.**  
Laboratory masses do not source extra-direction gradients. Again a statement about \(\mathcal K\), not about a particle.

**3. No gravitational momentum in \(\phi\).**  
The impulse kernel does not propagate in \(\phi\). Tav is an internal phase / clock / topological label. Then there is no extra flux channel, and the micron bound never starts. This is the consistent TSB reading if gravity is a 4D stochastic average of Mirron processes.

**4. Two lengths.**  
The mean force law has a short gravitational correlation length \(\ell_G\lesssim 30\,\mu\mathrm{m}\), while some other sector (domains, web, phase locking) has a 10 Mpc coherence length. Two kernels, two scales. Write both.

Bullet 3 is “no gravitons” done properly: not “we decline to quantize the metric,” but “the extra coordinate is not a direction in the gravitational kernel.”

---

## 5. When stochastic TSB *does* evade the bound

It evades the bound if all of the following are true at once:

1. The mean impulse kernel \(\mathcal K\) is four-dimensional. It maps 4D stress to 4D acceleration and does not spread into a fifth metric direction.
2. Tav (\(\phi\)) enters only as a phase, clock, or label in the noise statistics — for example a 7-fold modulation of \(N_{\mu\nu\rho\sigma}\), not a compact spatial radius.
3. The 7\(h^{-1}\) Mpc number is a *correlation length or web-coherence scale* in that noise, not the circumference of a space gravity can wrap.
4. The linearized mean kernel reproduces Newton / GR from tens of microns through the solar system.

Then inverse-square-law tests are tests of item 4, not tests of a 10 Mpc circle, because there is no such circle in \(\mathcal K\).

That is a coherent theory. It is also a rewrite of any draft that still starts from

\[
S_5=\frac{1}{16\pi G_5}\int d^5x\sqrt{-g_5}\,R_5
\]

with \(\phi\) an ordinary compact coordinate of radius \(7h^{-1}\,\mathrm{Mpc}\). That action *does* let geometry vary in \(\phi\), whether or not you quantize it. If gravity is stochastic and 4D, that action is the wrong opening line.

---

## 6. What still has to be calculated

Drop gravitons. The to-do list does not get shorter. It gets cleaner.

- Write the stochastic law. Either Einstein–Langevin plus a TSB noise kernel, or a pure impulse law \(\Delta P^a\to\Delta\theta\to\) acceleration with no metric middle step.
- State whether \(\phi\) is an argument of the metric / kernel, or only of the statistics.
- Compute the mean two-body potential \(V(r)\) at \(r\sim 50\,\mu\mathrm{m}\), \(1\,\mathrm{AU}\), and \(10\,\mathrm{Mpc}\).
- Identify \(\ell_C\) in the noise. If \(\ell_C\sim 10\,\mathrm{Mpc}\), explain why that long correlation does not add a Yukawa piece inside the laboratory (usually: the long mode is homogeneous on laboratory scales and only renormalizes \(G\), or it is a phase correlation that does not carry flux).
- Keep the cosmic-web number as a correlation-scale prediction, not as a compactification radius.

---

## 7. One-sentence answer

No. The bound is not there because someone posited gravitons. It is there whenever gravitational influence can spread into a fifth *spatial* direction of size \(\tau\). If TSB gravity is a 4D stochastic average and Tav is only a phase in the noise, the bound does not apply — and the 5D Einstein–Hilbert circle should be retired as a picture of that gravity.

---

## File location

`Tau-Superblock-Universe/Personal-Files/2026-09-19_stochastic-gravity-not-gravitons.md`
