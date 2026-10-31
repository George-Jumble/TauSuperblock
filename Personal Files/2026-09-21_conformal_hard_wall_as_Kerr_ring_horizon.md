# Session: Conformal-crossover hard wall = 3D Kerr-ring event horizon
# Superblock as a black hole

- **Session date:** 2026-09-21
- **Instruction:** Treat the hard wall of the conformal crossover as an event horizon equal to the event horizon of a Kerr ring, in 3 dimensions. i.e. the Superblock as a black hole itself.
- **Status in the corpus:** *Candidate geometric identification*, not a replacement of the bounce. The bounce remains the original TSB/CCC object: conformal aeon crossover + Mirron / Planck–Kerr dynamic refresh. This note does **not** rewrite the bounce as a Φ₇ pin-drop, a Coleman instanton, or a Biquaternion-Universe M+ event. The 2026-09-21 7 Mpc / seventh-phase aside line stays out.
- **This file:** `Personal Files/2026-09-21_conformal_hard_wall_as_Kerr_ring_horizon.md`
- **Repo path:** `George-Jumble/TauSuperblock/Personal Files/2026-09-21_conformal_hard_wall_as_Kerr_ring_horizon.md`

---

## Variable and function key

Every symbol used below. SI units unless a geometric unit is named.

| Symbol | Meaning |
|---|---|
| \(\mathcal{X}\) | CCC / TSB conformal-crossover 3-surface (spacelike in standard CCC because \(\Lambda>0\)) |
| \(\mathcal{W}\) | Hard wall: the same locus as \(\mathcal{X}\), but with reflecting / impedance boundary conditions instead of a transparent conformal glue |
| \(\Sigma_+\) | Outer event-horizon 2-surface in a spatial 3-slice (topologically \(S^2\), Kerr-oblate) |
| \(\Sigma_-\) | Inner (Cauchy) horizon 2-surface, if present |
| \(\mathcal{R}\) | Kerr ring: the curvature locus \(\rho^2=0\) at \(r=0\), \(\theta=\pi/2\), coordinate radius \(a\) |
| \(\Sigma_{\mathrm{M}}\) | Mirron 2-surface (Planck–Kerr topological mirror). In this identification \(\mathcal{R}\) is the equatorial generator of \(\Sigma_{\mathrm{M}}\), not a curvature blow-up |
| \(M\) | Kerr mass parameter (geometric units: length). Superblock value written \(M_{\mathrm{SB}}\) |
| \(a=J/M\) | Kerr spin parameter (length). Superblock value written \(a_{\mathrm{SB}}\) |
| \(J\) | Angular momentum |
| \(G\) | Newton constant (data in TSB; not re-derived here) |
| \(c\) | Invariant speed in the Prime domain |
| \(\hbar\) | Reduced Planck constant |
| \(\ell_P=\sqrt{\hbar G/c^3}\) | Planck length, core seed |
| \(r_{\mathrm{M}}\) | Effective Mirron radius. Locked candidate: \(\lambda_{313}=hc/\Delta_{\mathrm{TEP}}\approx 6.302\times 10^{-16}\,\mathrm{m}\) |
| \(\Delta_{\mathrm{TEP}}\) | Topological Exclusion Principle / friction floor \(\approx 313.1\,\mathrm{MeV}\) |
| \(r_\pm\) | Kerr horizons: \(r_\pm=M\pm\sqrt{M^2-a^2}\) (geometric units \(G=c=1\)) |
| \(r_+^{\mathrm{(SI)}}\) | \(r_+\) restored: \(r_\pm=(GM/c^2)\pm\sqrt{(GM/c^2)^2-a^2}\) |
| \(\Delta(r)\) | Kerr horizon function: \(\Delta=r^2-2Mr+a^2\) (geometric units) |
| \(\rho^2\) | Kerr spin-weighted radial factor: \(\rho^2=r^2+a^2\cos^2\theta\) |
| \(r_E^\pm(\theta)\) | Ergosurfaces: \(r_E^\pm=M\pm\sqrt{M^2-a^2\cos^2\theta}\) |
| \(\theta,\phi\) | Polar and azimuthal Boyer–Lindquist angles |
| \(t,r\) | Boyer–Lindquist time and radial coordinates |
| \(g_{\mu\nu}\) | Physical 4-metric of one 3+1 domain |
| \(\tilde{g}_{\mu\nu}\) | Conformal metric, \(\tilde{g}_{\mu\nu}=\Omega^2 g_{\mu\nu}\) |
| \(\Omega\) | Conformal factor. CCC: \(\Omega\to 0\) at future infinity of the old aeon, \(\Omega\to\infty\) at the stretched bang of the new aeon |
| \(\Lambda\) | Cosmological constant (positive in standard CCC, making \(\mathcal{X}\) spacelike) |
| \(\chi_{\mathrm{M}}\) | Mirron presence: \(1\) on, \(0\) off |
| \(\zeta\) | PK-mirror superlubricant; \(\zeta\to 1\) is lossless reflection |
| \(N_\tau=7\) | Active Tav phases; 8th phase is Past⇄Future inversion |
| \(\Phi_8^P,\Phi_8^F\) | Absolute Past and Absolute Future nodes of the 8-phase engine |
| \(\beta_i=v_i/c\) | Normalized orbital speed of domain \(i=1,\ldots,6\) on the internal supersphere |
| \(\langle\gamma\rangle_6\) | Six-domain averaged Lorentz factor |
| \(V_{\mathrm{orb}}^{(i)}\) | Orbital-velocity eigenvalue of domain \(i\) (E₈ projection; geometric, not fitted) |
| \(\mathcal{S}\) | Internal supersphere on which the six 3+1 domains are co-located |
| \(R_{\mathcal{S}}\) | Coordinate radius of \(\mathcal{S}\) in the internal 3-geometry (the 3D object whose outer 2-surface is identified with \(\Sigma_+\)) |
| \(k^\mu\) | Null generator of a classical Kerr horizon |
| \(n^\mu\) | Outward normal to the hard wall \(\mathcal{W}\) in a spatial 3-slice |
| \(h_{ab}\) | Induced 3-metric on \(\mathcal{X}\) or \(\mathcal{W}\) |
| \(K_{ab}\) | Extrinsic curvature of that 3-surface |
| \(A_+\) | Area of \(\Sigma_+\): \(A_+=4\pi(r_+^2+a^2)\) |
| \(S_{\mathrm{BH}}=kc^3 A_+/(4G\hbar)\) | Bekenstein–Hawking entropy (classical comparison only) |
| \(T_{\mathrm{H}}=\hbar\kappa/(2\pi k_B c)\) | Hawking temperature; \(\kappa\) is surface gravity |
| \(\kappa_+\) | Surface gravity of the outer Kerr horizon: \(\kappa_+=(r_+-r_-)/(2(r_+^2+a^2))\) (geometric units) |
| \(\omega_+\) | Horizon angular velocity: \(\omega_+=a/(r_+^2+a^2)\) |
| \(\alpha_{\mathrm{fs}}\) | Fine-structure constant (not derived in this note) |
| \(C_{\alpha\beta\gamma\delta}\) | Weyl tensor |
| \(R_{\mu\nu}\) | Ricci tensor |
| \(\mathcal{I}^+\) | Future conformal infinity of an aeon |
| \(\mathcal{B}\) | Conformally stretched bang of the next aeon |
| Prime | The 3+1 domain we inhabit |
| Dynamic Refresh | TSB rule: a localized excitation at tick \(n\) exists by re-projection from \(\Sigma_{\mathrm{M}}\) |

Geometric units in Kerr formulae: \(G=c=1\), so \(M\) and \(a\) are lengths. SI restorations are written whenever a laboratory or cosmological number is discussed.

---

## 0. What is being asserted, and what is not

**Assertion (this session).**
In a spatial 3-slice of any one 3+1 domain, the hard wall \(\mathcal{W}\) of the TSB conformal crossover occupies the same 2-surface as the outer event horizon of a Kerr ring-source,
\[
\mathcal{W}\;\simeq\;\Sigma_+\qquad\text{in 3-space},
\]
and the Superblock (six co-located domains on the internal supersphere \(\mathcal{S}\)) is that Kerr object. The ring \(\mathcal{R}\) is not left as a curvature singularity. It is the equatorial generator of the Mirron \(\Sigma_{\mathrm{M}}\) — the Planck–Kerr reflecting engine already in the corpus.

**Not asserted.**
- The bounce is *not* replaced by gravitational collapse, a Φ₇ pin-drop, or a Coleman bounce.
- \(\mathcal{X}\) is *not* being declared null in the CCC sense. Standard CCC keeps \(\mathcal{X}\) spacelike when \(\Lambda>0\). The identification is of the *3-geometry of the wall* with the *3-geometry of a Kerr horizon slice*, plus a causal reading (no Prime return), not a naive “spacelike = null” slogan.
- The rejected 2026-09-21 7 Mpc / seventh-phase aside line is not used as a module, a DE fix, or a clock-slot gate.
- “Mirron” is not “soliton.”

**Why “in 3 dimensions.”**
A Kerr event horizon in 3+1 spacetime is a null 3-manifold whose constant-\(t\) slice is a 2-sphere. The user instruction asks for that slice — the wall you can draw in 3-space — and for the ring that lives in that same 3-space as a circle of radius \(a\). The Superblock-as-BH statement is a statement about that 3-geometry plus the causal role of the wall, not a reduction of the theory to 3D gravity (BTZ, etc.).

---

## 1. Kerr ring geometry, written so the dictionary is one-to-one

### 1.1 Horizons and ring

In Boyer–Lindquist coordinates the vacuum Kerr line element (geometric units) is
\[
\mathrm{d}s^2
=
-\frac{\Delta}{\rho^2}\bigl(\mathrm{d}t-a\sin^2\theta\,\mathrm{d}\phi\bigr)^2
+\frac{\sin^2\theta}{\rho^2}\bigl[(r^2+a^2)\mathrm{d}\phi-a\,\mathrm{d}t\bigr]^2
+\frac{\rho^2}{\Delta}\,\mathrm{d}r^2
+\rho^2\,\mathrm{d}\theta^2.
\]

Functions:
\[
\Delta(r)=r^2-2Mr+a^2,
\qquad
\rho^2(r,\theta)=r^2+a^2\cos^2\theta.
\]

Outer / inner horizons are the roots of \(\Delta=0\):
\[
r_\pm
=
M\pm\sqrt{M^2-a^2},
\qquad
|a|\le M
\quad\text{(sub-extremal; equality is extremal)}.
\]

The curvature singularity is *not* \(r=0\) as a point. It is the ring
\[
\mathcal{R}
=
\bigl\{
\rho^2=0
\bigr\}
=
\bigl\{
r=0,\;\theta=\pi/2
\bigr\}
=
\bigl\{
x^2+y^2=a^2,\;z=0
\bigr\}
\]
in Kerr–Schild Cartesian coordinates. The disk \(r=0\), \(\theta<\pi/2\) is regular; only the rim is singular in classical Kerr.

The outer-horizon 2-surface in a \(t=\mathrm{const}\) slice is the squashed sphere
\[
\Sigma_+:
\quad
r=r_+,
\quad
\theta\in[0,\pi],
\quad
\phi\in[0,2\pi),
\]
with induced area
\[
A_+
=
4\pi\bigl(r_+^2+a^2\bigr).
\]

Ergosurface (infinite-redshift surface for static observers, *not* the horizon):
\[
r_E^+(\theta)
=
M+\sqrt{M^2-a^2\cos^2\theta}.
\]
At the poles \(r_E^+=r_+\); at the equator \(r_E^+=2M>r_+\) unless \(a=0\).

Surface gravity and horizon angular velocity:
\[
\kappa_+
=
\frac{r_+-r_-}{2(r_+^2+a^2)},
\qquad
\omega_+
=
\frac{a}{r_+^2+a^2}.
\]

### 1.2 What “event horizon of a Kerr ring” means in 3-space

In 3-space one draws two nested objects:

1. A circle \(\mathcal{R}\) of radius \(a\) in a plane (the ring).
2. A topological 2-sphere \(\Sigma_+\) surrounding that circle, oblate, with equatorial circumference \(2\pi\sqrt{r_+^2+a^2}\) and polar radius smaller.

The classical reading: anything that crosses \(\Sigma_+\) inward cannot send a signal back to spatial infinity. The ring is hidden provided \(|a|\le M\).

The TSB reading developed below: \(\Sigma_+\) is the hard wall \(\mathcal{W}\). The ring is not hidden-as-singular; it is the Mirron engine that *makes* the wall hard.

---

## 2. Dictionary: TSB objects \(\leftrightarrow\) Kerr objects

| Kerr / GR object | TSB object under this identification |
|---|---|
| Entire Kerr spacetime | The Superblock: six co-located 3+1 domains on \(\mathcal{S}\) |
| Asymptotic spatial infinity | Prime-domain late-aeon observers, after conformal stretching |
| Outer horizon slice \(\Sigma_+\) | Hard wall \(\mathcal{W}\) of the conformal crossover, drawn in 3-space |
| Horizon generators \(k^\mu\) | Null chords that *graze* \(\mathcal{W}\) and are reflected by \(\Sigma_{\mathrm{M}}\) rather than captured |
| Inner horizon \(\Sigma_-\) | Optional Cauchy wall inside the Superblock cell. Not required. If kept, it is the Past-node side of the 8-phase inversion, not a mass-inflation instability |
| Ring \(\mathcal{R}\) | Equatorial generator of the Mirron \(\Sigma_{\mathrm{M}}\). Radius \(a_{\mathrm{SB}}\) is geometric, not a curvature blow-up |
| Disk \(r=0\), \(\theta\neq\pi/2\) | Interior of the Mirron / Planck–Kerr engine (regular in Kerr; reflecting in TSB) |
| Ergosphere | Frame-dragging belt of the six staggered \(V_{\mathrm{orb}}^{(i)}\) on \(\mathcal{S}\) |
| Spin \(a=J/M\) | Net angular momentum of the E₈-projected domain orbits, divided by \(M_{\mathrm{SB}}\) |
| Mass \(M\) | Komar / ADM mass of the Superblock as seen from the Prime exterior |
| Surface gravity \(\kappa_+\) | Impedance gradient of \(\mathcal{W}\); sets the refresh rate at the wall, not a Hawking flux that evaporates the Superblock |
| Hawking temperature \(T_{\mathrm{H}}\) | Comparison quantity only. Mirron PBH branch already forbids ordinary Hawking evaporation; the Superblock inherits that prohibition |
| Weyl curvature at the ring | Bounce path-length deposited into \(C_{\alpha\beta\gamma\delta}\) (existing TSB rule), regularized by \(\chi_{\mathrm{M}}=1\) |
| CCC crossover \(\mathcal{X}\) | Same locus as \(\mathcal{W}\), but CCC writes a *transparent* conformal glue \(\mathcal{I}^+\simeq\mathcal{B}\). TSB writes a *hard* glue: reflection + Dynamic Refresh |
| Hawking points on \(\mathcal{X}\) (Penrose–Meissner 2025) | Isolated wall defects where a *local* black hole of the previous aeon finished evaporating. Distinct from the Superblock-as-BH itself |

The last row matters. CCC already puts black-hole remnants *on* the crossover as Hawking points. This session puts the *Superblock* on the other side of the analogy: the Superblock *is* the Kerr object whose horizon *is* the wall. Those are two different uses of “black hole.” Both can sit in the same manuscript if they are not fused.

---

## 3. The hard-wall problem, stated cleanly

Three surfaces that are easy to confuse:

| Surface | Causal type in its native theory | Job |
|---|---|---|
| CCC crossover \(\mathcal{X}\) | Spacelike 3-manifold (\(\Lambda>0\)) | Glue \(\mathcal{I}^+\) of aeon \(n\) to \(\mathcal{B}\) of aeon \(n+1\). Conformal metric smooth except at discrete Hawking points |
| Kerr horizon history | Null 3-manifold | One-way membrane for Prime-domain signals |
| Hard wall \(\mathcal{W}\) | Boundary condition (Dirichlet / impedance), typically timelike or mixed in a 3+1 chart | Reflect. No transmission of Prime information through the wall. Mirron bounce lives *on* it |

A slogan “spacelike = null” is false. The identification that *is* allowed is:

> In every spatial 3-slice, the 2-geometry of \(\mathcal{W}\) equals the 2-geometry of \(\Sigma_+\), and the wall is one-way for Prime-domain information *because* the Mirron reflection plus Dynamic Refresh replaces both (i) classical capture and (ii) transparent CCC transmission.

That is a *boundary-condition* identification, not a change of the causal type of \(\mathcal{X}\) in the conformal 4-geometry.

### 3.1 Conformal factor at a hard wall

Standard CCC:
\[
\tilde{g}_{\mu\nu}=\Omega^2 g_{\mu\nu},
\qquad
\Omega\to 0\text{ on }\mathcal{I}^+,
\qquad
\Omega\to\infty\text{ on }\mathcal{B}.
\]
The product can be smooth across \(\mathcal{X}\).

Hard-wall TSB:
\(\Omega\) is still allowed to run, but the *physical* fields of the Prime domain satisfy a reflecting condition on \(\mathcal{W}\). A model condition (to be frozen later, not fitted) is the impedance condition already used for finite \(c\):
\[
\bigl(n^\mu F_{\mu\nu}\bigr)\big|_{\mathcal{W}}
=
Z_{\mathrm{M}}^{-1}\,(\star F)_{\nu}{}^{\parallel}\big|_{\mathcal{W}},
\qquad
Z_{\mathrm{M}}=Z_0/\zeta,
\]
with \(\zeta\to 1\) the lossless Mirron. For the metric perturbation / Weyl deposit the analogous statement is: the incoming bounce current is re-emitted as the next-tick refresh. Nothing Prime-causal crosses \(\mathcal{W}\).

The conformal glue still exists for the *conformal* metric. The hard wall exists for the *physical* metric of each domain. That split is the whole point of calling it a conformal crossover *and* a hard wall.

### 3.2 Matching radii in 3-space

Set the Superblock cell radius in the internal 3-geometry equal to the outer Kerr horizon:
\[
R_{\mathcal{S}}
=
r_+
=
M_{\mathrm{SB}}+\sqrt{M_{\mathrm{SB}}^2-a_{\mathrm{SB}}^2}
\qquad\text{(geometric units)}.
\]

The ring that sources that horizon is the Mirron equator:
\[
a_{\mathrm{SB}}
=
r_{\mathrm{M}}
\quad\text{or}\quad
a_{\mathrm{SB}}
=
\alpha_{\mathcal{R}}\,r_{\mathrm{M}},
\]
where \(\alpha_{\mathcal{R}}\) is a pure geometric factor from the E₈ / twistor projection (not a fit). Two distinguished choices, to be frozen later, not mixed:

| Choice | \(a_{\mathrm{SB}}\) | Reading |
|---|---|---|
| A. Clock-ring | \(r_{\mathrm{M}}=\lambda_{313}\) | The same circle that sets the Tav tick is the Kerr ring |
| B. Seed-ring | \(\ell_P\) | The Planck seed is the ring; \(\lambda_{313}\) is a dressed Compton width of the wall impedance, not the ring radius |

Existing length lock (2026-09-18): \(r_{\mathrm{M}}=\ell_P\) moves \(\Delta_{\mathrm{TEP}}\) to \(E_P\) and spoils the \(\alpha_{\mathrm{fs}}\) attempt. That argues *against* Choice B as a numerical lock, not against Choice B as a seed.

In SI,
\[
r_+^{\mathrm{(SI)}}
=
\frac{GM_{\mathrm{SB}}}{c^2}
+
\sqrt{\Bigl(\frac{GM_{\mathrm{SB}}}{c^2}\Bigr)^2-a_{\mathrm{SB}}^2}.
\]
If Choice A is frozen and one also demands \(R_{\mathcal{S}}=r_+\sim r_{\mathrm{M}}\), the Superblock-as-BH is a *Mirron-scale* Kerr object (a Planck–Kerr “cell BH”). If \(R_{\mathcal{S}}\) is instead the internal supersphere of the six-domain cell at a larger geometric radius, \(M_{\mathrm{SB}}\) scales up with \(R_{\mathcal{S}}\) and the ring remains small inside it — the usual Kerr hierarchy \(a\le r_+\).

Both readings are geometrically legal. They must not be averaged. Freeze one.

---

## 4. Superblock as a black hole: mass, spin, and the six domains

### 4.1 What “the Superblock is a black hole” is allowed to mean

Three nested readings. Only the first is required by the user sentence.

**Reading I (required). Cell-BH.**
The six-domain Superblock cell is one Kerr-like object. Exterior = Prime late-aeon geometry. Interior = the co-located domains + Mirron engine. Wall = \(\Sigma_+\).

**Reading II (already in corpus). Local Mirron-BH.**
Each Mirron is a Planck–Kerr object that does not Hawking-evaporate. This is the *engine*, not the Superblock. It supplies \(\mathcal{R}\) and \(\chi_{\mathrm{M}}\).

**Reading III (cosmological, optional).**
An entire aeon, seen from the conformal compactification, looks like the exterior of a single Kerr object whose horizon *is* \(\mathcal{X}\). This is a Penrose-diagram statement, not a claim that the observable universe has mass \(c^2 R_{\mathrm{H}}/G\) in the astrophysical-BH sense.

Do not collapse I, II, III into one number.

### 4.2 Spin from staggered domain orbits

Each domain \(i\) carries an orbital velocity eigenvalue \(V_{\mathrm{orb}}^{(i)}\) from the E₈ projection (geometric). In the Superblock rest frame a candidate Komar spin is
\[
J_{\mathrm{SB}}
=
\sum_{i=1}^{6}
\gamma_i\, m_i\, V_{\mathrm{orb}}^{(i)}\, R_{\mathcal{S},\perp}^{(i)},
\]
with
\[
\gamma_i=\bigl(1-\beta_i^2\bigr)^{-1/2},
\qquad
\beta_i=V_{\mathrm{orb}}^{(i)}/c,
\]
and \(m_i\) the Komar mass of domain \(i\) as seen from the common centre of \(\mathcal{S}\). Then
\[
a_{\mathrm{SB}}
=
\frac{J_{\mathrm{SB}}}{M_{\mathrm{SB}}},
\qquad
M_{\mathrm{SB}}
=
\sum_{i=1}^{6} m_i
\quad\text{(plus wall / Mirron binding, not fitted)}.
\]

No numerical lock is made in this session. The only constraint that must hold if \(\Sigma_+\) is to exist as a covering horizon is the sub-extremal inequality
\[
a_{\mathrm{SB}}^2
\le
M_{\mathrm{SB}}^2
\qquad\text{(geometric units)},
\]
i.e.
\[
J_{\mathrm{SB}}
\le
\frac{G M_{\mathrm{SB}}^2}{c}.
\]
If the six-domain sum overshoots that bound, the wall is a *naked* ring and the hard-wall-as-horizon identification fails. That is a falsifiable geometric check, not a free parameter.

### 4.3 Frame-dragging as domain stagger

The Kerr ergosphere is the region in which no static observer exists. In TSB language that is the belt in which the staggered \(V_{\mathrm{orb}}^{(i)}\) force every Prime-static frame to co-rotate with the Superblock. The equatorial ergosurface \(r_E^+=2M_{\mathrm{SB}}\) is the 3-space locus where the time-averaged gravitational coupling (already a TSB object: conformal gravity via twistor space) becomes unable to support a non-orbiting observer. This is an interpretation of an existing object, not a new field.

---

## 5. The ring is a Mirron, not a singularity

Classical Kerr: \(\rho^2=0\) makes curvature invariants blow up.

TSB replacement, consistent with Dynamic Refresh and with the 2026-09-16 Mirron-impedance theorem:

1. The locus \(\{r=0,\theta=\pi/2\}\) is occupied by \(\Sigma_{\mathrm{M}}\).
2. Incoming null data hit \(\Sigma_{\mathrm{M}}\) and execute a Past⇄Future bounce \(\Phi_8^P\leftrightarrow\Phi_8^F\).
3. The bounce deposits a discrete path-length quantum into \(C_{\alpha\beta\gamma\delta}\). That is the TSB source of time-averaged gravity. It is finite because \(r_{\mathrm{M}}\) is finite and \(\chi_{\mathrm{M}}=1\).
4. There is no curvature singularity on \(\mathcal{R}\). There is a reflecting engine whose equatorial radius plays the algebraic role of Kerr’s \(a\).

This is why the phrase is “event horizon of a Kerr *ring*” rather than “event horizon of a Kerr *singularity*.” The ring stays. The singularity does not.

Roy Kerr’s own later remark — that an event horizon need not force a singularity — is the classical shadow of the same move. TSB supplies the missing interior: a Mirron, not a theorem-gap.

### 5.1 Inner horizon

If \(a_{\mathrm{SB}}\neq 0\) the algebra also produces \(r_-\). Options:

- **Drop \(\Sigma_-\).** Keep only the outer wall. Interior is the Mirron + six-domain cell with no second membrane. Simplest. Compatible with “one hard wall.”
- **Keep \(\Sigma_-\) as the Past node.** Then \(r_-\) is the 3-space radius of \(\Phi_8^P\) and \(r_+\) is the 3-space radius of the Future-facing wall. The 8-phase inversion lives *between* them. Mass-inflation instabilities of classical Cauchy horizons are not imported; the Mirron refresh cuts the blueshift.

Default for this note: drop \(\Sigma_-\) until a geometric computation forces it. One hard wall was requested.

---

## 6. Causal structure: one-way for Prime, cyclic for the engine

Draw the 3-space picture, then the conformal picture.

**3-space (this session’s demand).**
- Circle \(\mathcal{R}\) of radius \(a_{\mathrm{SB}}\) in a plane.
- Oblate 2-sphere \(\Sigma_+=\mathcal{W}\) around it, radius \(r_+\) in Boyer–Lindquist \(r\).
- Six domain-sheets co-located on \(\mathcal{S}\), cut off at \(\mathcal{W}\).
- Prime observers live at \(r>r_+\).

**Conformal 4-picture (bounce kept).**
- Aeon \(n\) future-infinity \(\mathcal{I}^+\) and aeon \(n+1\) stretched bang \(\mathcal{B}\) still occupy the same locus \(\mathcal{X}\).
- Physical Prime fields reflect on \(\mathcal{W}\subset\mathcal{X}\).
- The Mirron refresh is the *interior* process that lets the next aeon be populated without sending Prime information backward through the wall.
- That is the original TSB/CCC bounce: conformal aeon crossover + Mirron / Planck–Kerr dynamic refresh. The hard-wall language specifies the *boundary condition* of that crossover. It does not replace the bounce.

Information accounting:

| Channel | Classical Kerr | CCC | TSB hard-wall Superblock |
|---|---|---|---|
| Prime → exterior after crossing \(\Sigma_+\) | Impossible | Not defined (no \(\Sigma_+\)) | Impossible |
| Aeon \(n\) → aeon \(n+1\) | N/A | Conformal transmission, plus Hawking-point defects | Reflection + Dynamic Refresh. No Prime bit tunnels as a Prime bit |
| Engine degrees of freedom | Lost at the ring singularity | Gravitational-wave epoch + Hawking points | Stored and re-projected on \(\Sigma_{\mathrm{M}}\) |
| Hawking evaporation of the Superblock | Yes, in QFT-on-Kerr | Evaporation of *galactic* holes *before* crossover | Forbidden on the Mirron-PBH branch; Superblock inherits the prohibition |

The last cell is a corpus decision already on the books (Mirron PBHs avoid Hawking evaporation), applied now to the Superblock-as-BH. If that inheritance is later revoked, the Superblock would radiate and the wall would recede. That revocation is not made here.

---

## 7. Equations of the identification (complete)

Geometric units \(G=c=1\) in (E1)–(E6); SI restorations in (E7)–(E9).

**(E1) Horizon function of the Superblock.**
\[
\Delta_{\mathrm{SB}}(r)
=
r^2-2M_{\mathrm{SB}}r+a_{\mathrm{SB}}^2.
\]

**(E2) Hard wall in 3-space.**
\[
\mathcal{W}
=
\bigl\{
r=r_+,\;
\Delta_{\mathrm{SB}}(r_+)=0,\;
r_+
=
M_{\mathrm{SB}}+\sqrt{M_{\mathrm{SB}}^2-a_{\mathrm{SB}}^2}
\bigr\}.
\]

**(E3) Ring = Mirron equator.**
\[
\mathcal{R}
=
\bigl\{
r=0,\;\theta=\pi/2
\bigr\}
=
\text{equator of }\Sigma_{\mathrm{M}},
\qquad
a_{\mathrm{SB}}
=
\alpha_{\mathcal{R}}\,r_{\mathrm{M}}.
\]

**(E4) Cell-radius lock (choose and freeze).**
\[
R_{\mathcal{S}}
=
r_+.
\]

**(E5) Sub-extremal covering condition (falsifiable).**
\[
a_{\mathrm{SB}}^2
\le
M_{\mathrm{SB}}^2.
\]

**(E6) Conformal / physical split on the same locus.**
\[
\tilde{g}_{ab}\big|_{\mathcal{X}}
\quad\text{smooth (CCC glue)},
\qquad
n^\mu T_{\mu\nu}^{\mathrm{(Prime)}}\big|_{\mathcal{W}}
\quad\text{reflecting (hard wall)}.
\]
Here \(T_{\mu\nu}^{\mathrm{(Prime)}}\) is the Prime-domain stress tensor and \(n^\mu\) is the spatial normal of \(\mathcal{W}\).

**(E7) SI outer radius.**
\[
r_+^{\mathrm{(SI)}}
=
\frac{GM_{\mathrm{SB}}}{c^2}
+
\sqrt{\Bigl(\frac{GM_{\mathrm{SB}}}{c^2}\Bigr)^2-a_{\mathrm{SB}}^2}.
\]

**(E8) Surface gravity (comparison only).**
\[
\kappa_+
=
\frac{c^4}{2G}\,
\frac{r_+-r_-}{r_+^2+a_{\mathrm{SB}}^2}.
\]

**(E9) Operational Prime \(c\) at the wall (from the 2026-09-16 theorem, not re-derived).**
\[
c
=
\frac{\alpha\, r_{\mathrm{M}}}{\Delta t_\tau(\chi_{\mathrm{M}}=1)},
\qquad
\chi_{\mathrm{M}}=0
\;\Rightarrow\;
\text{no wall impedance, no finite }c.
\]
Clock factor \(\alpha\in\{2,2\pi,2\pi/7\}\) as previously frozen; do not mix clocks.

---

## 8. What this does to existing TSB modules

| Module | Effect of this identification |
|---|---|
| Bounce (CCC + Mirron / Planck–Kerr refresh) | **Unchanged.** The wall is the boundary condition of the bounce, not a substitute bounce |
| Finite-\(c\) Mirron-impedance theorem (2026-09-16) | Strengthened: the same \(\Sigma_{\mathrm{M}}\) that sets \(c\) is the ring that sources the wall |
| Time-averaged conformal gravity / twistor coupling | The wall is the 3-space place where bounce deposits are no longer available to Prime observers |
| Six-domain supersphere and \(V_{\mathrm{orb}}\) | Supply \(J_{\mathrm{SB}}\) and the ergosphere reading |
| Yang–Mills mass gap via Planckian mirrors | Interior engine; not moved to the horizon |
| Mirron PBHs, no Hawking evaporation | Inherited by the Superblock-as-BH |
| 2026-09-21 7 Mpc / 5D / seventh-phase aside | **Out.** Not used |
| Φ₇ pin-drop / Coleman rewrite of the bounce | **Out.** Not used |
| Three-pair inverse-time antimatter envelope | Backburner only. Not used |

---

## 9. Edge cases and failure modes

1. **Extremal limit \(a_{\mathrm{SB}}=M_{\mathrm{SB}}\).** Then \(r_+=r_-=M_{\mathrm{SB}}\) and \(\kappa_+=0\). The wall is degenerate. A hard wall with vanishing surface gravity is an impedance surface with no redshift gradient. Legal, but the “horizon” language becomes thin. Prefer sub-extremal unless geometry forces extremality.

2. **Naked ring \(a_{\mathrm{SB}}>M_{\mathrm{SB}}\).** No \(\Sigma_+\). The identification *fails*. This is the cleanest internal falsifier of Superblock-as-BH.

3. **\(a_{\mathrm{SB}}=0\).** Schwarzschild recovery: wall is a round 2-sphere of radius \(2M_{\mathrm{SB}}\), no ring. That contradicts “Kerr ring” unless the ring is kept as a dormant \(\Sigma_{\mathrm{M}}\) with \(J_{\mathrm{SB}}=0\). Allowed as a limit, not as the generic case.

4. **Scale clash.** If Choice A sets \(a_{\mathrm{SB}}=r_{\mathrm{M}}\sim 0.63\,\mathrm{fm}\) and Reading III wants a cosmological \(r_+\), (E5) forces a huge \(M_{\mathrm{SB}}\) and a tiny dimensionless spin \(a/M\). That is a slowly rotating cosmological cell-BH, not an extremal micro-BH. Do not silently mix Reading I at fm scale with Reading III at Hubble scale.

5. **Null vs spacelike.** If a later draft declares \(\mathcal{X}\) itself null in order to “be” a Kerr horizon 3-manifold, that draft has left CCC. This note does not do that. It identifies 3-space 2-geometries and causal roles.

6. **Information.** A hard wall that also conformal-glues two aeons looks like an information paradox with extra steps. The TSB resolution already on the books is Dynamic Refresh: bits are not transmitted; they are re-projected. If that rule is dropped, the identification re-opens the paradox and should be rejected.

7. **Ergosphere vs wall.** They coincide only at the poles. An observer can sit in the ergosphere and still be outside \(\mathcal{W}\). Domain-stagger effects that live in the ergosphere are *not* automatically “behind the hard wall.”

---

## 10. Recommended next computations (no fitting)

1. Freeze Choice A or B for \(a_{\mathrm{SB}}\), and freeze Reading I or III for \(R_{\mathcal{S}}\). Write the pair on one line and do not mix.
2. Compute \(J_{\mathrm{SB}}\) from the existing \(V_{\mathrm{orb}}^{(i)}\) table and test (E5).
3. Write the induced 2-metric on \(\mathcal{W}\) and compare its eccentricity to the Kerr oblateness \(a_{\mathrm{SB}}/r_+\).
4. Specify the impedance condition on \(\mathcal{W}\) for the Weyl deposit, parallel to the Maxwell condition that produces finite \(c\).
5. Draw one Penrose diagram in which \(\mathcal{X}\) remains spacelike and \(\mathcal{W}\) is marked as a reflecting 2-surface in each 3-slice — so the two causal types are visible at once.

---

## 11. Direct statement

The hard wall of the conformal crossover, drawn in 3-space, is identified with the outer event-horizon 2-surface of a Kerr ring-source. The Superblock is that Kerr object. The ring is the Mirron / Planck–Kerr engine, not a curvature singularity. The bounce is untouched: it remains conformal aeon crossover plus Mirron dynamic refresh. The new content is the boundary condition and the 3-geometry, not a new expansion event.

---

## Sources used this session

- Kerr metric: horizons \(r_\pm=M\pm\sqrt{M^2-a^2}\), ring \(\rho^2=0\), area \(A_+=4\pi(r_+^2+a^2)\), ergosurfaces, surface gravity. Standard GR (Boyer–Lindquist).
- CCC crossover as a spacelike 3-surface \(\mathcal{X}\) joining \(\mathcal{I}^+\) to the stretched bang; Hawking points as discrete defects (Penrose; Meissner–Penrose, arXiv:2503.24263).
- TSB corpus: Mirron \(\neq\) soliton; Dynamic Refresh; Planck–Kerr engine; finite-\(c\) Mirron-impedance theorem (`Personal Files/2026-09-16_Mirron_nature_and_finite_c.md`); length locks \(\ell_P\), \(r_{\mathrm{M}}=\lambda_{313}\); bounce kept in original TSB/CCC form (2026-09-21 decision).
- Explicitly unused: 2026-09-21 7 Mpc / seventh-phase aside line; Φ₇ pin-drop; Coleman rewrite; Biquaternion M+ bounce language.

---

*End of session note — 2026-09-21 conformal hard wall as 3D Kerr-ring horizon; Superblock as BH.*
