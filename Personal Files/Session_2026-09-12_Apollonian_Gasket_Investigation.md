# Session 2026-09-12 — Apollonian gasket / sphere packing investigation

**Purpose:** State the geometry of Apollonian packings and map it, without forcing, onto the locked octant split and Mirron proliferation.

**Status:** Mathematics of the gasket is standard. TSB use is optional hierarchy for the **interstitial** \(1-f\), not a replacement of \(q=8\).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(r_i\) | Radius of circle \(i\) (2D) or sphere \(i\) (3D) |
| \(k_i=1/r_i\) | Curvature (bend) |
| \(C_i\) | Circle or sphere \(i\) |
| \(k_4^\pm\) | Two Descartes solutions in 2D (inner / outer Soddy circle) |
| \(k_5^\pm\) | Two Soddy solutions in 3D |
| \(\delta_2\) | Hausdorff dimension of the 2D residual set (gasket) |
| \(\delta_3\) | Hausdorff dimension of the 3D residual set |
| \(f_{\mathrm{oct}}\) | Octant-split fill \(\approx 0.392\) (previous lock) |
| \(1-f_{\mathrm{oct}}\) | Interstitial fraction \(\approx 0.608\) |
| \(\ell_{\mathrm{cap}}\) | Exhaustion cap of a first-generation envelope |
| \(q=8\) | Locked octant daughter count |
| \(N_\tau,N_{\mathrm{M}}\) | Tau-fiber and PK-Mirron counts |
| \(\mathcal{B}\) | Bound 3-ball |
| \(E\) | Envelope 2-sphere |
| \(\Phi_7\) | Seventh-phase evaluation map |
| \(\mathcal{C}_{\mathcal{PF}}\) | Atemporal Past–Future circle |
| \(\alpha_{\mathrm{A}}\) | Residual-set dimension used only if a gasket layer is adopted |

Negative curvature means a circle/sphere that **contains** the others (bounding circle).

---

## 2. What an Apollonian gasket is

Start with three mutually tangent circles. There are exactly two circles tangent to all three (Apollonius). Descartes’ theorem gives their curvatures. Iterate: every new triple produces two more circles. The residual set left by the open disks is the **Apollonian gasket**.

It is not a strictly self-similar IFS with one ratio. It is a fractal because the residual set has a well-defined Hausdorff dimension that is not an integer. Measured value: \(\delta_2\approx 1.3056867\).

The 3D analogue (Soddy / Apollonian **sphere** packing) starts with four mutually tangent spheres and fills the gaps with spheres tangent to four existing ones. Residual-set dimension \(\delta_3\approx 2.4739\).

For TSB envelopes the 3D packing is the relevant object: envelopes are 2-spheres in Prime 3-space. The 2D gasket is the planar picture of the same idea.

---

## 3. Descartes (2D) and Soddy (3D)

Four mutually tangent circles:

\[
k_4
=
k_1+k_2+k_3
\pm
2\sqrt{k_1k_2+k_1k_3+k_2k_3}.
\]

**Key:** \(k_i=1/r_i\); \(+\) = inner (smaller) Soddy circle; \(-\) = outer (often the bounding circle, \(k<0\)).

Equivalent form:

\[
(k_1+k_2+k_3+k_4)^2
=
2(k_1^2+k_2^2+k_3^2+k_4^2).
\]

**Key:** same four curvatures.

Five mutually tangent spheres in 3D:

\[
k_5
=
k_1+k_2+k_3+k_4
\pm
2\sqrt{\sum_{1\le i<j\le 4}k_ik_j}.
\]

**Key:** \(k_5\) = curvature of the fifth sphere; pair sum runs over the four existing spheres.

If the first curvatures are integers, later curvatures stay integers (integral Apollonian packings). That is number theory on bends, not a TSB mass formula.

---

## 4. What the gasket is *not*

- Not a tiling by equal balls. Radii fall as a hierarchy of bends.  
- Not the octant split. Octant split writes **eight equal** daughters at one generation. Apollonian writes **unequal** spheres, recursively, in the gaps.  
- Not a derivation of \(\tau\) or of \(313.1\,\mathrm{MeV}\).  
- Not automatically the cosmic web. The web in the octant lock is the \(61\%\) interstitial; Apollonian is one way to put **smaller bound balls** into that interstitial.

---

## 5. Relation to the locked octant split

Locked first generation:

\[
q=8,
\qquad
r=\frac{\sqrt{3}-1}{2}\,\ell_{\mathrm{cap}},
\qquad
f_{\mathrm{oct}}=\frac{8}{10+6\sqrt{3}}\approx 0.392.
\]

**Key:** as in the tiling note.

After that write, \(1-f_{\mathrm{oct}}\approx 0.608\) of the parent ball is empty of first-generation daughters. Two options:

**A. Interstitial stays unbound 3+1.**  
No further bound balls. Filaments/voids are the leftover. Octant lock is the whole bound-sector story.

**B. Interstitial is packed by a Soddy hierarchy.**  
Treat the parent envelope (curvature \(k_0=-1/\ell_{\mathrm{cap}}\), negative because it contains the daughters) plus the eight first-generation spheres as a seed. Further spheres with

\[
k_{n+1}
=
\sum_{j\in T}k_j
\pm
2\sqrt{\sum_{i<j\in T}k_ik_j}
\]

**Key:** \(T\) = a tangent 4-tuple already present; \(k_{n+1}\) = next Soddy sphere.

Those smaller spheres would be **sub-cap cells**: bound balls that never reach \(\ell_{\mathrm{cap}}\) because they are born in a gap and the parent generation already spent the cap. In TSB language they are candidate **hierarchical Mirrons**, not new survey-scale Tau nodes.

That matches the existing “fractal globbing / hierarchical binding” language better than it matches the survey lattice. Survey nodes stay the octant generation that hits \(\ell_{\mathrm{cap}}\). Apollonian descendants are the bound hierarchy *inside* a cell and *between* cells.

---

## 6. Counting if option B is adopted

Let \(\mathcal{S}_g\) be the set of spheres written at Soddy generation \(g\) after the octant seed (\(g=0\) is the eight equal daughters).

Curvatures grow roughly exponentially in \(g\) (Descartes \(+\) branch). The number of spheres with curvature \(\le K\) in a bounded packing scales as

\[
\#\{i:k_i\le K\}
\sim
c\,K^{\delta},
\]

**Key:** \(K\) = curvature cutoff; \(\delta=\delta_2\) in the plane, \(\delta=\delta_3\) in 3D; \(c\) = packing-dependent prefactor.

In 3D, \(\delta_3\approx 2.47\), so the number of sub-cells with radius \(\ge\varepsilon\) scales as \(\varepsilon^{-\delta_3}\). That is a fractal inventory of small Mirrons, not \(8^g\).

Do **not** add this count into \(N_\tau\) of the survey lattice. Split the registers:

\[
N_\tau^{\mathrm{(survey)}}
=
8^{g_{\mathrm{oct}}},
\qquad
N_{\mathrm{M}}^{\mathrm{(hier)}}
=
\#\{\text{Soddy spheres with }k\le K_{\mathrm{cut}}\}.
\]

**Key:** \(g_{\mathrm{oct}}\) = octant generations that hit the cap; \(K_{\mathrm{cut}}\) = a UV/IR cutoff that must be named before the hierarchy is physics.

Without a named \(K_{\mathrm{cut}}\), option B is an infinite foam and not a finite Mirron number.

---

## 7. Dual pictures

| Picture | Radii | Role in TSB |
|---------|-------|-------------|
| Octant split | equal, one ratio \(\rho=(\sqrt{3}-1)/2\) | Survey-scale node write |
| Apollonian / Soddy | unequal, Descartes recursion | Optional hierarchy in the interstitial and inside a cell |
| 2D gasket | circles in a plane | Diagram only (Tau *circles* are \(S^1\) fibers, not these packing circles) |
| 3D packing | spheres in \(\mathbb{R}^3\) | Correct analog of envelopes \(E(t,y)\) |

The bound KK fiber \(S^1_\tau\) is still the compact fifth circle at a written centre. The Apollonian “circle” is a 2D drawing of a 3D envelope. Do not identify \(S^1_\tau\) with a Descartes circle.

---

## 8. Atemporal cylinder

\(\mathcal{C}_{\mathcal{PF}}\) is unchanged. A Soddy sub-sphere is another evaluation point of \(\Phi_7\), at a smaller envelope. Past–Future unification does not need the gasket. The gasket only multiplies evaluation points below the cap.

---

## 9. Verdict

Apollonian geometry is a precise, closed algorithm for packing **unequal** tangent balls in the leftover of the octant split. It is the natural fractal if hierarchical binding inside \(1-f_{\mathrm{oct}}\) is wanted.

It is **not** a reason to unlock \(q=8\).  
It is **not** a derivation of \(\tau\).  
It becomes TSB physics only after a cutoff \(K_{\mathrm{cut}}\) is named and the survey register is kept separate from the hierarchical register.

---

## 10. If a next step is taken

Name \(K_{\mathrm{cut}}\) from clockwork (an eigenvalue of \(\Phi_7\) or a Planck-Kerr radius), then list the first few Soddy curvatures generated from the seed \(\{-1/\ell_{\mathrm{cap}}\}\) plus eight daughters of curvature \(2/((\sqrt{3}-1)\ell_{\mathrm{cap}})\). Empty RHS: do not insert \(313.1\,\mathrm{MeV}\) as that cutoff.

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
