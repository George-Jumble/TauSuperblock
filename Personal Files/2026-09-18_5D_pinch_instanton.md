# Session log: Derive the 5D pinch instanton

- **Session date:** Friday, 2026-09-18
- **Charge:** Derive the 5D pinch instanton left open after the reduced \(\varphi_{\mathrm{n}}\) kink.
- **Parents:** `2026-09-18_two_scalar_action.md`, `2026-09-18_compute_gates_packing_xi_fold_Weyl_aeon.md`, `2026-09-18_hierarchical_twistor_circle_EM_and_bounce.md`
- **This file:** `Personal Files/2026-09-18_5D_pinch_instanton.md`
- **Drive folder:** Tau-Superblock Universe / Personal Files
- **Nomenclature:** Mirron, never soliton. The object constructed here is a Euclidean 5D geometry with a bolt / neck. It is not a hydrodynamic standing wave.

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(\mathrm{d}s_5^2\) | 5D line element. Signature Euclidean unless stated. No KK vector. |
| \(\theta\sim\theta+2\pi\) | Angle on the pinched circle, unless a different period is named for regularity. |
| \(\varphi\) | Proper radius of that circle. Function of the 4D base. |
| \(\varphi_{\tau}\) | Cosmic cylinder modulus. Background \(R_{\tau}=7\,h^{-1}\,\mathrm{Mpc}\). |
| \(\psi\) | Local clock-fiber radius after Scale Reflection. Background \(r_{\mathrm{M}}\) on a single-engine neighbourhood. |
| \(S^1_{\tau}\) | Tav cylinder. |
| \(S^1_{\mathrm{M}}\) | Clock / tick circle at radius \(r_{\mathrm{M}}\). |
| Hopf \(S^1\) | Clifford fibre on the supersphere. Not the pinched metric circle. |
| \(r\) | Proper radial coordinate in the 4D base, or areal radius when so named. |
| \(r_s\) | Bolt radius. The 2-sphere at which the fibre shrinks. |
| \(A(r)\) | Areal radius of the transverse 2-sphere. |
| \(B(r)\) | Euclidean-time coefficient. |
| \(\tau\) | Euclidean time. Period \(\beta_{\tau}\) when compact. |
| \(\alpha\) | Asymptotic fibre coefficient, \(\varphi\to\alpha\) at infinity in the bolt solution. |
| \(F(r)\) | Schwarzschild factor \(1-r_s/r\). |
| \(\Sigma_{\mathrm{M}}\) | Mirron 2-surface. Identified with the bolt 2-sphere. |
| \(\Phi_8^P,\Phi_8^F\) | Past and Future nodes. The two sides of a neck, or the two sheets of a Kruskal-like extension. |
| \(\Delta_{\mathrm{TEP}}\) | TEP floor \(313.1\,\mathrm{MeV}\). Regularizes a complete pinch to zero. |
| \(r_{\mathrm{M}}=\hbar c/\Delta_{\mathrm{TEP}}\) | Locked clock radius. |
| \(\ell_P\) | Planck length. 5D seed, not the bolt radius. |
| \(G_{\mathrm{N}}\) | 4D Newton constant. Data. |
| \(G_5\) | 5D coupling. Bookkeeping \(G_5=2\pi R_{\tau}G_{\mathrm{N}}\) if the fifth direction is \(S^1_{\tau}\). Local clock reduction uses a different conversion. |
| \(K\) | Trace of extrinsic curvature (Gibbons–Hawking). |
| \(S_{\mathrm{E}}\) | Euclidean action of one instanton period. |
| \(\Delta t_{\tau}=2r_{\mathrm{M}}/c\) | Frozen diameter tick. Used as the Euclidean period of \(\tau\). |
| \(\mathcal{S}\) | Scale Reflection map. Sends a cosmic pinch to a clock pinch (and back). |
| \(n_{\mathrm{hier}}=\log_7(R_{\tau}/r_{\mathrm{M}})\approx 45.78\) | Decade count of that map. |
| \(R_{AB}\) | 5D Ricci tensor. |
| \(\delta\) | Conical deficit (or excess) at the bolt. |

---

## 0. What is being derived, and what is not

A 5D pinch instanton is a Euclidean solution of the 5D Einstein equations, with no KK vector, in which a metric circle shrinks and a compact 2-surface is left behind. That 2-surface is \(\Sigma_{\mathrm{M}}\).

It is **not**:

- the 4D kink of \(\varphi_{\mathrm{n}}\) already written in the two-scalar action (that is the reduced shadow);
- a pinch of the *cosmic* cylinder down to zero inside a fermi-sized ball (that geometry is conical with excess \(\sim R_{\tau}/r_{\mathrm{M}}\sim 10^{38}\) and is not regular);
- a Witten bubble of nothing of radius \(R_{\tau}\) (that bolt is an \(S^3\) of megaparsec radius);
- a hydrodynamic soliton;
- a Coleman false-vacuum bounce whose rate is \(e^{-S_{\mathrm{E}}/\hbar}\) replacing \(\Gamma\). Nucleation current stays the relaxation law already derived. The instanton is the *geometry of one engine*, not a replacement for \(\Gamma\).

It **is**:

- an exact Ricci-flat 5D metric (bolt family), regularity conditions included;
- a TEP-regularized two-sided neck (Past \(\leftrightarrow\) Future), which vacuum GR does not give by itself;
- the Scale-Reflected image of the same bolt written at decade \(0\) rather than decade \(n_{\mathrm{hier}}\).

---

## 1. Three circles, one pinch

From the hierarchical-twistor note, do not fuse:

| Circle | Background radius | Role |
|---|---|---|
| \(S^1_{\tau}\) | \(R_{\tau}\) | cosmic EKK cylinder |
| \(S^1_{\mathrm{M}}\) | \(r_{\mathrm{M}}\) | tick / clock fibre of one engine |
| Hopf \(S^1\) | angle, or \(r_{\mathrm{M}}\) if embedded on \(\Sigma_{\mathrm{M}}\) | photon kinematics, not the pinched metric fibre |

Pinching \(S^1_{\tau}\) with period \(2\pi\) and asymptotic radius \(R_{\tau}\) produces a regular bolt of radius \(R_{\tau}/2\), cosmic. That is the wrong object.

Pinching \(S^1_{\mathrm{M}}\) with asymptotic radius \(r_{\mathrm{M}}\) produces a regular bolt of radius \(r_{\mathrm{M}}\). That 2-sphere *is* \(\Sigma_{\mathrm{M}}\).

Scale Reflection is the statement that these are the same solution written at two decades:

\[
\frac{\varphi_{\tau}(x)}{R_{\tau}}
\;=\;
\frac{\psi\bigl(\mathcal{S}(x)\bigr)}{r_{\mathrm{M}}}.
\]

**Key.** \(\varphi_{\tau}\) cosmic modulus; \(\psi\) local clock fibre; \(\mathcal{S}\) Scale Reflection. A pinch of \(\psi\) *is* a pinch of \(\varphi_{\tau}\) after \(\mathcal{S}\). One does not physically compress ten megaparsecs into a fermi in the Einstein-frame coordinates of the Prime domain.

**Plain language.** There is a big hoop (the Tav cylinder) and a little hoop (the clock). The little hoop is the big hoop seen through the hierarchical mirror. The instanton pinches the little hoop. Calling that “a 5D pinch of \(\varphi_{\tau}\)” is legal only because of Scale Reflection. Without \(\mathcal{S}\) it would be a misuse of the cosmic modulus.

The derivation below is written for \(\psi\), then mapped.

---

## 2. 5D action and ansatz

No KK vector (ownership lock):

\[
S_5
=\frac{1}{16\pi G_5}\int\mathrm{d}^5x\,\sqrt{\lvert g_5\rvert}\,R_5
+\frac{1}{8\pi G_5}\int_{\partial}\mathrm{d}^4x\,\sqrt{\lvert h\rvert}\,K.
\]

**Key.** \(G_5\) 5D coupling; \(R_5\) 5D Ricci scalar; \(h\) induced metric on the boundary; \(K\) trace of extrinsic curvature. The second term is Gibbons–Hawking. On-shell \(R_5=0\) in vacuum, so the value of the action is the boundary term.

Euclidean, spherically symmetric, static in \(\tau\):

\[
\mathrm{d}s_5^2
=B(r)\,\mathrm{d}\tau^2
+\frac{\mathrm{d}r^2}{F(r)}
+A(r)^2\mathrm{d}\Omega_2^2
+\varphi(r)^2\mathrm{d}\theta^2.
\]

**Key.** \(\mathrm{d}\Omega_2^2=\mathrm{d}\chi^2+\sin^2\chi\,\mathrm{d}\psi^2\) unit 2-sphere; \(A(r)\) areal radius of that 2-sphere; \(\varphi(r)\) fibre radius; \(B,F>0\) outside the bolt.

The 2-sphere at a fixed \(r\) is the candidate \(\Sigma_{\mathrm{M}}\).

---

## 3. Exact vacuum bolt

### 3.1 The metric

The following is Ricci-flat. Direct computation of \(R_{AB}\) (computer algebra, this session) gives \(R_{AB}=0\) identically:

\[
\mathrm{d}s_5^2
=\mathrm{d}\tau^2
+\frac{\mathrm{d}r^2}{1-r_s/r}
+r^2\mathrm{d}\Omega_2^2
+\alpha^2\Bigl(1-\frac{r_s}{r}\Bigr)\mathrm{d}\theta^2,
\qquad
r\ge r_s.
\]

**Key.** \(r_s>0\) bolt radius; \(\alpha>0\) asymptotic fibre radius, \(\varphi(r)=\alpha\sqrt{1-r_s/r}\to\alpha\) as \(r\to\infty\); \(B=1\) (Euclidean time is product); \(A(r)=r\).

This is the Euclidean 4D Schwarzschild factor written on the *fibre* rather than on \(\tau\). It is the \(\theta\leftrightarrow\tau\) swap of a black string. It is not a new guess.

### 3.2 What pinches

\[
\varphi(r_s)=0,
\qquad
A(r_s)=r_s.
\]

The fibre shrinks to a point. What remains at \(r=r_s\) is a 2-sphere of radius \(r_s\). That 2-sphere is the bolt.

**Identification.**

\[
\Sigma_{\mathrm{M}}
=\bigl\{r=r_s\bigr\}
\cong S^2(r_s).
\]

**Key.** The Mirron 2-surface *is* the bolt. Its proper radius is \(r_s\). The lock \(r_{\mathrm{M}}=\hbar c/\Delta_{\mathrm{TEP}}\) then forces \(r_s=r_{\mathrm{M}}\) on a clock-scale engine.

### 3.3 Regularity (no cone)

Near \(r=r_s\),

\[
1-\frac{r_s}{r}
=\frac{r-r_s}{r_s}+\mathcal{O}\bigl((r-r_s)^2\bigr).
\]

Set \(\rho^2=4 r_s(r-r_s)\), so \(\rho\to 0\) is the bolt and \(\mathrm{d}r^2/F\to\mathrm{d}\rho^2\). The fibre part becomes

\[
\varphi^2\mathrm{d}\theta^2
=\alpha^2\frac{\rho^2}{4 r_s^2}\,\mathrm{d}\theta^2
=\Bigl(\frac{\alpha}{2 r_s}\rho\Bigr)^2\mathrm{d}\theta^2.
\]

**Key.** \(\rho\) proper distance from the bolt in the \((r,\theta)\) plane; \(\alpha/(2 r_s)\) is the coefficient that decides a cone.

If \(\theta\) has period \(\beta_{\theta}\), the proper circumference at \(\rho\) is \(\beta_{\theta}\cdot\alpha\rho/(2 r_s)\). Flat polar coordinates need circumference \(=2\pi\rho\):

\[
\frac{\beta_{\theta}\,\alpha}{2 r_s}=2\pi
\qquad\Longrightarrow\qquad
\beta_{\theta}=\frac{4\pi r_s}{\alpha}.
\]

**Key.** \(\beta_{\theta}\) period of \(\theta\) required for a smooth cap.

Two TSB-legal choices.

**Clock engine (this instanton).** Asymptotic fibre is the clock, \(\alpha=r_{\mathrm{M}}\), bolt is the Mirron, \(r_s=r_{\mathrm{M}}\):

\[
\beta_{\theta}=4\pi.
\]

The angle that was written as \(\theta\sim\theta+2\pi\) in the cosmic reduction must be **double-covered** on the clock fibre, or equivalently one keeps period \(2\pi\) and sets \(\alpha=2 r_{\mathrm{M}}\) (asymptotic proper radius \(2 r_{\mathrm{M}}\), bolt radius \(r_{\mathrm{M}}\)). The two descriptions differ by a constant rescaling of \(\theta\). The invariant statement is

\[
\frac{\text{asymptotic circumference}}{\text{bolt radius}}
=4\pi.
\]

**Key.** That \(4\pi\) is the regularity number of this bolt. It is not a fitted coupling.

**Cosmic cylinder (the other bolt).** \(\alpha=R_{\tau}\), period already locked to \(2\pi\):

\[
r_s=\frac{R_{\tau}}{2}.
\]

A regular cosmic pinch has a bolt of radius \(R_{\tau}/2\sim 5\,\mathrm{Mpc}\). That is a void-scale cap, not a Mirron. It is a legal 5D solution and a different object.

### 3.4 Why a fermi-sized pinch of \(S^1_{\tau}\) is illegal

Keep \(\alpha=R_{\tau}\), \(\beta_{\theta}=2\pi\), and demand \(r_s=r_{\mathrm{M}}\). Then

\[
\frac{\beta_{\theta}\alpha}{2 r_s}
=\frac{R_{\tau}}{r_{\mathrm{M}}}
\approx 4.90\times 10^{38}
\neq 2\pi.
\]

The \((r,\theta)\) plane is a cone with excess of order \(10^{38}\). That is not a geometry. It is the statement that the cosmic hoop cannot be pinched regularly inside a clock-sized ball. Scale Reflection is mandatory, not decorative.

**Plain language.** You can cap a little hoop with a little sphere, or a big hoop with a big sphere. You cannot cap a ten-megaparsec hoop with a 0.63 fm sphere and still have a smooth cap. The hierarchical map is what lets the little cap count as a picture of the big one.

---

## 4. Euclidean period = Tav tick

The metric as written is invariant along \(\tau\). An infinite \(\tau\) line makes the action extensive. TSB already has a compact time: the tick.

Freeze, from the kinematics lock:

\[
\beta_{\tau}
=\Delta t_{\tau}
=\frac{2 r_{\mathrm{M}}}{c}.
\]

**Key.** \(\beta_{\tau}\) Euclidean period of \(\tau\); diameter bounce of the same 2-sphere that is the bolt.

One instanton cell is then the product

\[
[0,\beta_{\tau}]
\times
\{r\ge r_{\mathrm{M}}\}
\times S^2
\times S^1_{\theta}.
\]

The geometry is periodic in Euclidean time with the clock that the engine itself defines. That is the TSB replacement for a Hawking temperature: the period is not \(4\pi r_s\) from a \(\tau\)-bolt (here \(\tau\) does not pinch; \(\theta\) does). The period is the diameter tick.

If one instead compactified \(\tau\) by making \(B(r_s)=0\) (a second bolt), one would have a Euclidean black hole × shrinking fibre, over-constrained. Not used.

---

## 5. On-shell action of one tick

Vacuum: \(R_5=0\). Bulk Einstein–Hilbert vanishes. What remains is Gibbons–Hawking at the bolt and at a large-radius cutoff, minus the flat-cylinder counterterm.

Sketch of the bolt contribution. Near \(\rho=0\) the \((\rho,\theta)\) disk is polar. The bolt 2-sphere has area \(4\pi r_s^2\). Euclidean time contributes a factor \(\beta_{\tau}\). The GH integrand on a shrinking circle in two dimensions is the standard \(2\pi\) (regularity already imposed), so

\[
\frac{S_{\mathrm{E}}^{\mathrm{(bolt)}}}{\hbar}
\sim
\frac{\beta_{\tau}\,c}{\ell_P}\cdot\frac{4\pi r_s^2}{4\ell_P^2}\cdot
\Bigl(\frac{\ell_P^3}{G_5/G_{\mathrm{N}}}\Bigr)
\]

is the *wrong* mixing of 4D area-law with 5D coupling. Do not use it. It produces \(S_{\mathrm{E}}/\hbar\sim 10^{39}\) and would forbid every engine.

Correct counting for the *local* clock reduction. In a neighbourhood of one engine the relevant extra-dimension period is the clock circumference \(2\pi\alpha\sim 4\pi r_{\mathrm{M}}\), not \(2\pi R_{\tau}\). The local 5D coupling that reduces to 4D Einstein in that neighbourhood would be

\[
G_5^{\mathrm{(loc)}}
\sim
2\pi\alpha\,G_{\mathrm{N}}
\sim
4\pi r_{\mathrm{M}}\,G_{\mathrm{N}}
\]

if one insisted on reducing here. That is *not* the cosmic \(G_5=2\pi R_{\tau}G_{\mathrm{N}}\), and it is not how \(G_{\mathrm{N}}\) was declared data. Using it as a derivation of \(G_{\mathrm{N}}\) is the discarded C1 hop.

The TSB-consistent action of one tick is the one already matched to the rest-energy term in \(S_{\mathrm{n}}\):

\[
E_{\mathrm{tick}}
=\Delta_{\mathrm{TEP}},
\qquad
\frac{S_{\mathrm{E}}}{\hbar}
=\frac{E_{\mathrm{tick}}\,\Delta t_{\tau}}{\hbar}
=\frac{\Delta_{\mathrm{TEP}}\cdot(2 r_{\mathrm{M}}/c)}{\hbar}.
\]

**Key.** \(E_{\mathrm{tick}}\) energy of one refresh; \(\Delta t_{\tau}\) its duration.

Insert the lock \(r_{\mathrm{M}}=\hbar c/\Delta_{\mathrm{TEP}}\):

\[
\frac{S_{\mathrm{E}}}{\hbar}
=\frac{\Delta_{\mathrm{TEP}}\cdot 2(\hbar c/\Delta_{\mathrm{TEP}})/c}{\hbar}
=2.
\]

**Key.** The Euclidean action of one clock-scale bolt, per tick, is \(2\hbar\). Order one. Not Planck-suppressed.

The factor \(2\) is the diameter chord. A light-ring tick \(\Delta t_{\tau}=2\pi r_{\mathrm{M}}/c\) would give \(S_{\mathrm{E}}/\hbar=2\pi\). A seven-phase tick \(2\pi r_{\mathrm{M}}/(7c)\) would give \(2\pi/7\). The frozen diameter choice gives \(2\).

**Plain language.** Once the cap has the same radius as the Compton length of the only energy in the problem, the action of one tick is a few \(\hbar\). There is no \(10^{39}\) in the exponent. That huge number appears only if one treats the fermi 2-sphere as a 4D black hole horizon written with laboratory \(G_{\mathrm{N}}\). That is the wrong coupling on the wrong circle.

Honesty: the step from GH in \(G_5^{\mathrm{(loc)}}\) to \(S_{\mathrm{E}}=2\hbar\) is an identification with the TEP rest-energy already in \(S_{\mathrm{n}}\), not an independent evaluation of the 5D boundary integral with a unique \(G_5\). The *geometry* of the bolt is derived. The *value* \(2\hbar\) uses the locked pair \((r_{\mathrm{M}},\Delta_{\mathrm{TEP}},\Delta t_{\tau})\).

---

## 6. TEP as the cutoff on a complete pinch

The vacuum bolt pinches \(\varphi\to 0\). TSB does not allow a physical zero: the seed is \(\ell_P\), the clock is \(r_{\mathrm{M}}\), and TEP forbids packing two engines into the same slot.

Two regularizations, both legal, different meanings.

**R1 — conformal cap (vacuum, this section).** \(\varphi=0\) only at one 2-sphere, which is a coordinate origin in the \((\rho,\theta)\) plane, not a curvature singularity once \(\beta_{\theta}=4\pi r_s/\alpha\). The fibre is gone at the bolt the way the polar angle is gone at the origin of \(\mathbb{R}^2\). No TEP cost. This is the *photon-like* fold of 17 Sep: a null cap, Past and Future identified around the disk.

**R2 — TEP floor (fermion-like / permanent engine).** Stop the pinch at

\[
\varphi_{\mathrm{min}}
=\ell_P
\quad\text{or}\quad
\varphi_{\mathrm{min}}=\varepsilon r_{\mathrm{M}},
\qquad
\varepsilon\ll 1,
\]

and put a surface stress on the small 2-torus (or 2-sphere × residual circle) that Israel-matches the exterior bolt to an interior cap. The surface energy required is order \(\Delta_{\mathrm{TEP}}\). That is the selection rule: a *permanent* engine pays the floor; a single refresh does not.

**Plain language.** Vacuum GR can draw a smooth cap with the hoop shrunk to a point. That cap is one bounce. To leave a standing mirror behind, the hoop is not allowed to vanish; TEP leaves a seed and charges \(\Delta_{\mathrm{TEP}}\) for the privilege. That is why new engines are rarer than ordinary vacuum refresh.

---

## 7. Two-sided neck (Past \(\leftrightarrow\) Future)

The bolt of §3 is one-sided: \(r\ge r_s\), one exterior. Conjugacy \(\Phi_8^P\leftrightarrow\Phi_8^F\) wants two exteriors and a throat.

Vacuum Einstein with this ansatz does not give a regular two-sided neck with \(\varphi_{\mathrm{min}}>0\) and two asymptotically cylindrical ends without a source. That is the 5D version of topological censorship: a handle costs stress.

**Construction.** Take two copies of the bolt exterior, \(r\ge r_c>r_s\), and glue at \(r=r_c\) on a surface

\[
S^1_{\tau}\times S^2(r_c)\times S^1_{\theta}.
\]

Israel junction: the jump in extrinsic curvature equals a surface stress \(\mathcal{S}_{ab}\).

A minimal TEP glue sets \(r_c=r_{\mathrm{M}}\) and

\[
\int_{S^2}\mathcal{S}_{\tau\tau}\,\mathrm{d}A
=\Delta_{\mathrm{TEP}}
\]

in the rest frame of the throat (one TEP quantum on the 2-sphere). The two exteriors are the Past sheet and the Future sheet. A null bounce is a lightlike crossing of the throat; a standing engine is a timelike world-tube of the throat.

The neck is therefore **not** a second vacuum instanton. It is the vacuum bolt plus a TEP shell. That is the honest 5D status of “Past and Future identified on \(\Sigma_{\mathrm{M}}\).”

If someone later finds a smooth vacuum metric with \(\varphi_{\mathrm{min}}>0\) and two ends (for example with \(\Lambda_5\neq 0\) or a frozen \(\varphi_{\tau}\) potential), it replaces the shell. None is claimed here.

---

## 8. Reduction to the 4D kink

Far from the bolt, \(\varphi(r)\approx\alpha\bigl(1-r_s/(2r)\bigr)\). The fractional dip is

\[
\frac{\delta\varphi}{\alpha}
=\frac{r_s}{2r}.
\]

**Key.** At \(r\sim\mathrm{few}\times r_s\) the dip is order one. At laboratory distances it is \(r_{\mathrm{M}}/r\sim 10^{-15}\,\mathrm{m}/r\).

The 4D modulus kinetic term of the two-scalar action,

\[
-\frac{\kappa_{\tau}}{2\varphi^2}(\partial\varphi)^2,
\]

evaluated on this tail, is the Newtonian shadow of the bolt. The 4D field \(\varphi_{\mathrm{n}}\) of the two-scalar note is a *dimensionless packing* field, not this modulus. The map between them on a single engine is

\[
\varphi_{\mathrm{n}}(r)
=1-\Theta(\varphi_{\mathrm{crit}}-\psi_{\mathrm{core}})
=\begin{cases}
0 & \text{inside the bolt / TEP shell},\\
1 & \text{outside, mean structure}.
\end{cases}
\]

Smeared over width \(r_{\mathrm{M}}\) that step is the \(\tanh\) kink already written. The 5D bolt is the interior geometry the kink was standing in for.

**Plain language.** Yesterday’s crease was the view from 4D. Today’s cap is what you see if you climb into the extra circle and watch it close. Same object, two projections.

---

## 9. Cosmic image of the same instanton

Apply \(\mathcal{S}\) upward by \(n_{\mathrm{hier}}\) decades. The bolt radius scales as \(r_{\mathrm{M}}\mapsto R_{\tau}\) (more precisely \(r_s\mapsto R_{\tau}/2\) if the cosmic period stays \(2\pi\)). The image is the regular cosmic pinch of §3.3:

\[
\mathrm{d}s_5^2
=\mathrm{d}\tau^2
+\frac{\mathrm{d}r^2}{1-R_{\tau}/(2r)}
+r^2\mathrm{d}\Omega_2^2
+R_{\tau}^2\Bigl(1-\frac{R_{\tau}}{2r}\Bigr)\mathrm{d}\theta^2,
\qquad
r\ge R_{\tau}/2.
\]

**Key.** Bolt at \(r=R_{\tau}/2\), fibre \(S^1_{\tau}\) of background \(R_{\tau}\), period \(2\pi\), regular. This is a void-scale cap, a candidate geometry for a Mother-Block skin or a conformal-boundary fold, not for one clock-scale Mirron.

Nucleation of a *clock* engine uses the decade-\(0\) metric of §3. Hierarchical Binding then paints the decade-\(n_{\mathrm{hier}}\) image. Do not put the megaparsec bolt into \(\Gamma\) as if each new Superblock required pinching the physical \(S^1_{\tau}\) in Prime-frame coordinates.

---

## 10. What this does to \(\Gamma\) and to Weyl

\(\Gamma\) is unchanged. The instanton is the engine’s geometry. The rate at which new engines are booked remains the packing-deficit current

\[
\Gamma
=3H n_{\mathrm{M}}
\,\Theta(1-\varphi_{\mathrm{n}})
\,\Theta\bigl(\lvert\nabla\log\Omega\rvert-\Lambda_{\Omega}\bigr).
\]

**Key.** No factor \(e^{-S_{\mathrm{E}}/\hbar}\) is inserted. \(S_{\mathrm{E}}/\hbar=2\) would not suppress anything anyway. The rarity of *permanent* engines versus ordinary refresh is the TEP shell of §6–§7, not an instanton exponent.

Weyl of one bolt: the 4D Schwarzschild factor on the fibre produces the same \(r_s/r\) potential tail as a 4D mass

\[
M_{\mathrm{shadow}}
=\frac{r_s c^2}{2G_{\mathrm{N}}}
\]

*if* one reads \(F=1-r_s/r\) with laboratory \(G_{\mathrm{N}}\). That mass is \(c^2 r_{\mathrm{M}}/(2G_{\mathrm{N}})\approx 4\times 10^{11}\,\mathrm{kg}\) — a mountain, absurd as a vacuum engine. Therefore the tail is **not** to be read with laboratory \(G_{\mathrm{N}}\). The physical 4D mass of one engine remains \(\Delta_{\mathrm{TEP}}/c^2\approx 5.58\times 10^{-28}\,\mathrm{kg}\), as in the previous session, and the Weyl estimate \(r_s^{\mathrm{(phys)}}/r_{\mathrm{M}}\sim 10^{-38}\) stands.

The lesson: the function \(F=1-r_s/r\) is the *fibre* Schwarzschild factor. It is not the Prime-domain gravitational potential of a star of radius \(r_{\mathrm{M}}\). Mixing those is how C1 was missed, again.

---

## 11. Ledger

| Claim | Status |
|---|---|
| Metric of §3 is Ricci-flat | Derived (computer algebra + standard black-string swap) |
| Bolt 2-sphere is \(\Sigma_{\mathrm{M}}\) | Identification, locked to \(r_s=r_{\mathrm{M}}\) |
| Regularity \(\beta_{\theta}=4\pi r_s/\alpha\) | Derived |
| Clock engine: \(\alpha=r_{\mathrm{M}}\), \(\beta_{\theta}=4\pi\) (or \(\alpha=2r_{\mathrm{M}}\), \(\beta_{\theta}=2\pi\)) | Derived |
| Cosmic regular bolt at \(R_{\tau}/2\) | Derived; different object |
| Fermi pinch of \(S^1_{\tau}\) is conical | Derived; forbidden |
| Scale Reflection identifies the two bolts | Corpus map; used, not re-derived |
| Euclidean period \(=\Delta t_{\tau}\) | TSB lock, imposed |
| \(S_{\mathrm{E}}/\hbar=2\) per diameter tick | Derived from \((r_{\mathrm{M}},\Delta_{\mathrm{TEP}},\Delta t_{\tau})\); GH-in-\(G_5\) not independently evaluated |
| Two-sided neck | Vacuum: no. TEP shell: constructed |
| \(\Gamma=e^{-S_{\mathrm{E}}/\hbar}/\mathrm{vol}\) | **Rejected.** \(\Gamma\) stays the packing current |
| 4D \(\varphi_{\mathrm{n}}\) kink | Shadow of this bolt |
| Laboratory \(G_{\mathrm{N}}\) reading of \(F=1-r_s/r\) | **Rejected.** Wrong circle |

---

## 12. Direct answer

The 5D pinch instanton of one Mirron is the Ricci-flat metric

\[
\mathrm{d}s_5^2
=\mathrm{d}\tau^2
+\frac{\mathrm{d}r^2}{1-r_{\mathrm{M}}/r}
+r^2\mathrm{d}\Omega_2^2
+r_{\mathrm{M}}^2\Bigl(1-\frac{r_{\mathrm{M}}}{r}\Bigr)\mathrm{d}\theta^2,
\qquad
r\ge r_{\mathrm{M}},
\quad
\theta\sim\theta+4\pi,
\quad
\tau\sim\tau+\frac{2 r_{\mathrm{M}}}{c}.
\]

**Key.** Bolt at \(r=r_{\mathrm{M}}\) is \(\Sigma_{\mathrm{M}}\). Fibre is the clock circle, not \(S^1_{\tau}\). Period of \(\theta\) is \(4\pi\) so the cap is smooth. Period of \(\tau\) is the diameter tick.

A fermi-sized pinch of the physical Tav cylinder is not a solution. The cosmic cousin is the same metric with \(r_{\mathrm{M}}\mapsto R_{\tau}/2\) and \(\theta\sim\theta+2\pi\). Scale Reflection is the map between them.

Vacuum GR gives the one-sided cap (ordinary refresh). A standing engine is that cap plus a TEP shell of energy \(\Delta_{\mathrm{TEP}}\) gluing a Past exterior to a Future exterior. The Euclidean action of one tick is \(2\hbar\). Nucleation rate is not \(e^{-2}\); it remains the packing current on the two gates.

That is the 5D pinch instanton.

---

*End of session — 2026-09-18 5D pinch instanton.*
