# Session 2026-09-12 — 2D gasket projections lifted to overlapping 3+1D Riemann spheres

**Rule for this note:** overlap of spheres is **permitted**. Tangency and disjoint interiors are not required.

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(C(z,r)\) | Circle in a 2D chart: centre \(z\in\mathbb{C}\), radius \(r>0\) |
| \(k=1/r\) | Curvature in that chart |
| \(\widehat{\mathbb{C}}\) | Riemann sphere \(\mathbb{C}\cup\{\infty\}\cong S^2\) |
| \(\sigma\) | Stereographic projection \(\widehat{\mathbb{C}}\to S^2\subset\mathbb{R}^3\) |
| \(S_x^2\) | Riemann 2-sphere attached to a 3+1 event or Mirron centre \(x\) |
| \(\mathcal{R}_x\) | Same sphere as a \(\mathbb{CP}^1\) (conformal Riemann sphere) |
| \(E(t,y)\) | Spatial envelope 2-sphere at time \(t\), comoving centre \(y\) |
| \(\gamma_{ij}=S_i^2\cap S_j^2\) | Intersection circle of two overlapping spheres (may be empty) |
| \(M_4\) | Prime 3+1 spacetime |
| \(g_{\mu\nu}\) | Prime metric |
| \(a(t)\) | Scale factor |
| \(\Phi_7\) | Seventh-phase evaluation map |
| \(S^1_\tau(x)\) | Bound KK fiber (not a Riemann sphere) |
| \(\mathcal{C}_{\mathcal{PF}}\) | Atemporal Past–Future circle |
| \(\mathcal{F}_{\mathrm{2D}}\) | A 2D Apollonian *drawing* (projection / chart) |
| \(\mathcal{F}_{\mathrm{3+1}}\) | Family of overlapping \(S^2\)s in \(M_4\) |
| \(\ell_{\mathrm{cap}}\) | Survey-envelope cap |
| \(q=8\) | Locked octant *write* count (survey); not a no-overlap rule here |

---

## 2. What a 2D gasket circle is, in a chart

A 2D Apollonian figure \(\mathcal{F}_{\mathrm{2D}}\) is a set of circles \(\{C(z_i,r_i)\}\) in one plane (or in \(\widehat{\mathbb{C}}\)). Under stereography every circle or line in the plane is a circle on the unit Riemann sphere.

\[
\sigma:\widehat{\mathbb{C}}\to S^2,
\qquad
\sigma(u+iv)
=
\Bigl(
\frac{2u}{u^2+v^2+1},
\frac{2v}{u^2+v^2+1},
\frac{u^2+v^2-1}{u^2+v^2+1}
\Bigr),
\quad
\sigma(\infty)=(0,0,1).
\]

**Key:** \((u,v)\) = chart coordinates; \(\sigma(\infty)\) = north pole.

So already in 2D the “gasket” is a spherical picture. The plane drawing is one chart.

---

## 3. Lift to 3+1D

Attach a Riemann sphere to a Prime event (or to a Mirron centre) \(x\in M_4\):

\[
\mathcal{R}_x \cong \mathbb{CP}^1 \cong S_x^2.
\]

**Key:** \(\mathcal{R}_x\) = conformal 2-sphere at \(x\); \(S_x^2\) = the same object as a metric 2-sphere of some radius \(r(x)\) in a spatial frame.

Two concrete realizations (both allowed; they are charts of each other):

**A. Spatial envelope.** On a slice of time \(t\),

\[
S_y^2(t)
=
\bigl\{\mathbf{x}:\ a(t)\,d_{\mathrm{com}}(\mathbf{x},y)=r_{\mathrm{phys}}(t,y)\bigr\}.
\]

**Key:** \(y\) = comoving centre; \(r_{\mathrm{phys}}\) = physical radius; this is \(E(t,y)\) from the envelope notes.

**B. Celestial / twistor Riemann sphere.** Null directions at \(x\) form \(\mathbb{CP}^1\). A 2D circle in a stereographic chart of that \(\mathbb{CP}^1\) is a pencil of null rays. Overlap of two such spheres is a shared \(S^1\) of null directions.

The 2D gasket \(\mathcal{F}_{\mathrm{2D}}\) is a **projection** of \(\mathcal{F}_{\mathrm{3+1}}\): one chart, one slice, or one celestial sphere.

\[
\mathcal{F}_{\mathrm{2D}}
=
\pi\bigl(\mathcal{F}_{\mathrm{3+1}}\bigr)
\quad\text{for a chosen chart }\pi.
\]

**Key:** \(\pi\) = stereographic chart or spatial plane section.

---

## 4. Overlap is permitted

Packing language forbade interior intersection. That is dropped.

Two Riemann spheres may satisfy any of:

| Relation | Geometry | 2D chart |
|----------|----------|----------|
| Disjoint | no common points | two separate circles |
| Tangent | share one point (or one null generator) | Descartes case |
| Overlap | intersection is a circle \(\gamma_{ij}=S_i^2\cap S_j^2\cong S^1\) | two crossing circles |
| Nested | one interior contains the other | circle inside circle, possibly crossing if centres offset |

Intersection in 3-space:

\[
S_i^2\cap S_j^2
=
\gamma_{ij}
\cong
S^1
\quad\text{when }
\bigl||\mathbf{c}_i-\mathbf{c}_j|^2 - r_i^2 - r_j^2\bigr|
<
2 r_i r_j.
\]

**Key:** \(\mathbf{c}_i,\mathbf{c}_j\) = centres; \(r_i,r_j\) = radii; \(\gamma_{ij}\) = common circle.

That \(\gamma_{ij}\) is what the 2D drawing records as two overlapping gasket circles.

At Absolute Past, overlap is the *default*: many \(\mathcal{R}_x\) share almost the same 3-ball. Separation of centres with \(a(t)\) reduces overlap; it does not forbid it.

---

## 5. Bound fiber vs Riemann sphere

Do not identify them.

| Object | Dimension | Role |
|--------|-----------|------|
| \(S^1_\tau(x)\) | 1 (compact KK) | bound fifth coordinate |
| \(S_x^2\) / \(\mathcal{R}_x\) | 2 | envelope / celestial sphere |
| \(\gamma_{ij}\) | 1 | overlap of two envelopes |
| \(\mathcal{C}_{\mathcal{PF}}\) | 1 (4D bounce circle) | atemporal cylinder |

A 2D “Tau circle” in a figure is almost always \(\gamma_{ij}\) or a chart of \(\partial\mathcal{B}\), not \(S^1_\tau\).

\(\Phi_7\) evaluates \(\mathcal{C}_{\mathcal{PF}}\) into both: a fiber at \(x\) and a Riemann sphere at \(x\). Overlapping spheres mean overlapping evaluations, not a second \(\tau\).

---

## 6. What happens to previous locks

**Octant \(q=8\).** Still the *write rule* when a parent hits \(\ell_{\mathrm{cap}}\) and new centres are declared. Overlap permitted means those eight balls **may intersect** after growth or if the inscribed-ball construction is relaxed. The count \(q=8\) is unchanged; disjoint interiors are no longer required.

**Apollonian recursion.** Descartes tangency becomes optional. The hierarchy is a family of overlapping \(S^2\)s whose curvatures need not obey Soddy. If tangency is restored in a pocket, Soddy applies locally. If not, only incidence and inclusion remain.

**Hausdorff \(\delta\).** Defined for the *residual* of a non-overlapping packing. With overlap allowed, interiors are not removed as open disjoint disks. \(\delta_2,\delta_3\) cease to be the counting law unless one restricts to a non-overlapping sub-family. Do not carry \(\delta_{\mathrm{fit}}=1.302\) into the overlapping 3+1 family without that restriction.

**Mass gap.** Still the \(\Phi_7\) floor on a stopped bounce, not a sphere-overlap angle.

---

## 7. 3+1 process with overlap

\[
\mathcal{P}:
\quad
\{S_x^2\}\text{ highly overlapping, packed in one 4D region}.
\]

\[
\mathcal{N}:
\quad
\text{octant writes new centres; spheres may still intersect}.
\]

\[
\mathcal{F}:
\quad
\text{spheres of nodes with }a\chi>R_{\mathrm{EH}}\text{ leave this observer’s family}.
\]

**Key:** \(\mathcal{P},\mathcal{N},\mathcal{F}\) = Past, Present, Future; \(R_{\mathrm{EH}}\) = event horizon.

Hierarchical binding = nested *and* overlapping stopped bounces. Shared volume is shared residual \(L\), not a prohibition.

---

## 8. Status

| Item | Status |
|------|--------|
| 2D gasket = chart of a family of \(S^2\)s | lift rule |
| Overlap permitted | locked for this note |
| \(\gamma_{ij}=S_i^2\cap S_j^2\cong S^1\) | 2D circle in the drawing |
| \(S^1_\tau\) ≠ Riemann sphere | kept |
| \(\delta\) as inventory | only for a non-overlapping subpack |
| \(q=8\) write count | kept |

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
