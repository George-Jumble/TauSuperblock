# Session 2026-09-12 — Fractal dimension calculation (Apollonian residual set)

**Purpose:** State how \(\delta\) is defined and how it is actually computed. Separate a valid Boyd estimate from a failed box-count run.

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(\mathcal{R}\) | Residual set (complement of the open packed disks / balls) |
| \(\delta=\dim_H\mathcal{R}\) | Hausdorff dimension of \(\mathcal{R}\) |
| \(\mathcal{H}^s\) | \(s\)-dimensional Hausdorff measure |
| \(N(K)\) | Number of packing circles/spheres with curvature \(k\le K\) |
| \(k=1/r\) | Curvature |
| \(\varepsilon\) | Box side length |
| \(N_{\mathrm{box}}(\varepsilon)\) | Number of \(\varepsilon\)-boxes that meet a point sample of \(\mathcal{R}\) |
| \(\delta_2^{\mathrm{lit}}\) | Published 2D value \(\approx 1.305686728\) |
| \(\delta_3^{\mathrm{lit}}\) | Published 3D value \(\approx 2.4739465\) |
| \(\delta_{\mathrm{Boyd}}\) | Slope of \(\log N\) vs \(\log K\) |
| \(\delta_{\mathrm{box}}\) | Slope of \(\log N_{\mathrm{box}}\) vs \(\log(1/\varepsilon)\) |
| \(K_{\max}\) | Generation cutoff |
| \(q=8\) | Locked octant survey split (not an input to \(\delta\)) |

---

## 2. What is being measured

\(\delta\) is the Hausdorff dimension of the **residual set** \(\mathcal{R}\), not of a single circle (that is \(1\)) and not of the filled disks (that is \(2\)).

\[
\dim_H\mathcal{R}
=
\inf\bigl\{s\ge 0:\mathcal{H}^s(\mathcal{R})=0\bigr\}.
\]

**Key:** \(\mathcal{H}^s\) = Hausdorff measure at dimension \(s\); the infimum is the first \(s\) that sees \(\mathcal{R}\) as measure zero.

In 2D, \(1<\delta_2<2\): more than curves, less than area.  
In 3D, \(2<\delta_3<3\): more than surfaces, less than volume.

That is why \(\delta\) cannot be a mass gap (an energy) and cannot be \(\tau\) (a length).

---

## 3. Method A — Boyd curvature count (the practical definition)

Boyd: in a bounded Apollonian packing,

\[
N(K)
\sim
c\,K^{\delta},
\qquad
K\to\infty.
\]

**Key:** \(N(K)=\#\{i:0<k_i\le K\}\); \(c\) = packing-dependent prefactor; \(\delta=\dim_H\mathcal{R}\).

Computation:

1. Generate circles with **positions**, not curvatures alone (many circles share a \(k\)).  
2. Keep only geometrically valid Descartes centres (internally tangent, no spurious sign).  
3. Form \(N(K_j)\) on a log grid of thresholds.  
4. Least-squares

\[
\log N = \delta\log K + \log c
\]

**Key:** fit only a mid window; small \(K\) is seed-dominated, large \(K\) is truncated.

**This session, mid-window run (80k circles, \(K_{\max}\approx 2000\)):**  
\(\delta_{\mathrm{Boyd}}=1.302\), literature \(1.305686728\), relative error \(0.25\%\).

That is the usable numerical result.

---

## 4. Method B — box counting

Cover a point sample of \(\mathcal{R}\) (usually points on generated circumferences, which approximate \(\mathcal{R}\) from inside) by squares of side \(\varepsilon\):

\[
\delta_{\mathrm{box}}
=
\lim_{\varepsilon\to 0}
\frac{\log N_{\mathrm{box}}(\varepsilon)}{\log(1/\varepsilon)}.
\]

**Key:** \(N_{\mathrm{box}}(\varepsilon)\) = number of occupied boxes.

This estimator is biased unless:

- only legal circles are present,  
- small circles are sampled in proportion to their contribution to \(\mathcal{R}\),  
- \(\varepsilon\) is smaller than the smallest kept radius and larger than the point-sample spacing.

A second run in this session kept both Descartes centre-signs and filled the disk. Both Boyd and box slopes collapsed to \(\approx 1.57\) (area-like). That number is **not** \(\delta_2\). It is a packing bug: invalid disks cover positive area, so the “residual” is no longer a gasket.

---

## 5. Method C — published high precision

The literature value to \(10^{-8}\) and beyond is not a box count on \(10^5\) circles. It uses the Apollonian group (Viète involutions on Descartes quadruples), eigenvalue / transfer-operator estimates, and interval arithmetic. Quote those numbers; do not pretend a laptop BFS replaces them.

\[
\delta_2^{\mathrm{lit}}\approx 1.305686728,
\qquad
\delta_3^{\mathrm{lit}}\approx 2.4739465.
\]

**Key:** 2D gasket; 3D Soddy residual set (the one that belongs to envelope balls).

---

## 6. What failed numerically, and why it matters for TSB

| Run | Estimator | \(\delta\) | Verdict |
|-----|-----------|------------|---------|
| Mid-window, 80k legal-ish circles | Boyd | \(1.302\) | usable, \(0.25\%\) off literature |
| Second run, both centre signs | Boyd + box | \(\approx 1.57\) | invalid; area-filling |
| Literature | Apollonian group | \(1.305686728\) | standard |

If hierarchical Mirrons are an osculatory packing, the counting law is Boyd’s with \(\delta_3\), not the \(1.57\) artifact and not \(q=8\).

\[
N_{\mathrm{b}}(K)\sim c\,K^{\delta_3}.
\]

**Key:** \(N_{\mathrm{b}}\) = sub-cap bound envelopes with \(k\le K\).

Survey nodes remain \(N_\tau=8^{g_{\mathrm{oct}}}\).

---

## 7. Limits of the calculation in this framework

- \(\delta\) does not fix \(\ell_{\mathrm{cap}}\), \(\tau\), or \(\Delta\).  
- A 2D gasket \(\delta_2\) is a diagram. Envelope hierarchy is 3D; use \(\delta_3\) if a count is needed.  
- Without a named \(K_{\mathrm{cut}}=k_{\mathrm{PK}}\), \(N_{\mathrm{b}}\) is infinite.  
- Octant generation 1 is equal balls; \(\delta\) describes only the **unequal tail**.

---

## 8. Status

| Item | Status |
|------|--------|
| Definition of \(\delta\) | Hausdorff dim of residual set |
| Working 2D number | \(\delta_2^{\mathrm{lit}}=1.305686728\) (numeric check \(1.302\)) |
| Working 3D number | \(\delta_3^{\mathrm{lit}}\approx 2.4739\) |
| Artifact \(1.57\) | discarded |
| Role in TSB | inventory exponent for hierarchical Mirrons only |

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
