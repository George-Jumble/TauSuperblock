# Session 2026-09-12 — Hierarchical binding of the bound circle as Apollonian structure

**Claim under study:** Inside one bound cell, binding is a hierarchy of envelopes whose radii follow an osculatory (Apollonian / Soddy) packing, sitting on the locked octant first generation.

**Status:** Structure stated. Survey lattice unchanged (\(q=8\)). Mass gap still the \(\Phi_7\) floor, not \(\delta\).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(S^1_\tau(x)\) | Bound compact KK fiber at a written centre \(x\) |
| \(\tau\) | Frozen fiber radius (lattice input) |
| \(\mathcal{B}_0\) | Parent 3-ball at the cap |
| \(R=\ell_{\mathrm{cap}}\) | Parent physical radius at split |
| \(q=8\) | Locked octant daughter count |
| \(\mathcal{B}_k^{(1)}\) | First-generation octant ball, \(k=1,\ldots,8\) |
| \(a\) | Radius of each \(\mathcal{B}_k^{(1)}\) |
| \(\mathcal{B}_c^{(2)}\) | Central interstitial ball (generation 2) |
| \(r_c\) | Radius of \(\mathcal{B}_c^{(2)}\) |
| \(k=1/r\) | Curvature of an envelope sphere |
| \(k_0=-1/R\) | Curvature of the parent as container |
| \(k^{(1)}=(1+\sqrt{3})/R\) | Curvature of an octant daughter |
| \(k_c=(2+\sqrt{3})/R\) | Curvature of the central ball |
| \(g_{\mathrm{oct}}\) | Octant generations that hit the cap (survey) |
| \(g_{\mathrm{A}}\) | Apollonian / osculatory generation inside a cell |
| \(\Phi_7\) | Seventh-phase scrape |
| PK-Mirron | Planck–Kerr mirror |
| \(\Delta\) | Bound-sector mass gap (floor of the hierarchy) |
| \(L\) | Residual angular momentum of a stopped bounce |
| \(\delta_3\) | 3D residual-set dimension \(\approx 2.474\) |
| \(N_\tau\) | Survey Tau-fiber count |
| \(N_{\mathrm{b}}(g_{\mathrm{A}})\) | Number of bound sub-envelopes at Apollonian generation \(g_{\mathrm{A}}\) |
| \(\theta\) | Fiber angle on \(S^1_\tau\) |
| \(\mathcal{C}_{\mathcal{PF}}\) | Atemporal Past–Future circle |
| \(f_{\mathrm{oct}}\) | Fill of the eight daughters \(\approx 0.392\) |
| \(f_{8+c}\) | Fill of eight plus centre \(\approx 0.412\) |

“Bound circle” in this note has two layers that must not be fused: the **fiber** \(S^1_\tau\) and the **envelope hierarchy** \(\{\mathcal{B}\}\) in Prime 3-space.

---

## 2. What is bound, at each level

A bound object is an envelope whose bounce is stopped at Present. Binding strength is residual \(L\) stored in that ball.

- **Fiber** \(S^1_\tau(x)\): compact fifth circle written at the centre. Same \(\tau\) at every survey node. Does not recurse.  
- **Envelope hierarchy:** 3-balls inside a survey cell. Radii *do* recurse. This is the Apollonian structure.

Hierarchical binding = nested stopped bounces. Each smaller ball is a PK-Mirron evaluation of \(\mathcal{C}_{\mathcal{PF}}\) that never reaches \(\ell_{\mathrm{cap}}\).

---

## 3. Generation 1 (locked, not Apollonian)

Parent at the cap, octant split:

\[
a=\frac{R}{1+\sqrt{3}}=\frac{\sqrt{3}-1}{2}\,R,
\qquad
k^{(1)}=\frac{1+\sqrt{3}}{R}.
\]

**Key:** \(R=\ell_{\mathrm{cap}}\); \(a\) = daughter radius; \(k^{(1)}\) = daughter curvature.

The eight balls are pairwise tangent across a single sign flip and are internally tangent to the parent. They do **not** form a complete mutually tangent 4-tuple among themselves. The origin is a cavity:

\[
r_c=a(\sqrt{3}-1)=R(2-\sqrt{3}),
\qquad
k_c=\frac{2+\sqrt{3}}{R}.
\]

**Key:** \(r_c\) = radius of the largest sphere centred at the parent centre that is tangent to all eight daughters; \(k_c\) = its curvature.

Fill:

\[
f_{\mathrm{oct}}=8\left(\frac{\sqrt{3}-1}{2}\right)^3\approx 0.392,
\qquad
f_{8+c}\approx 0.412.
\]

**Key:** most of the parent is still empty after generation 2. That remainder is where the gasket lives.

---

## 4. Generation \(\ge 2\): osculatory fill

An Apollonian / Soddy step in 3D is: given a pocket bounded by four mutually tangent spheres (or by three spheres and the parent), write the unique largest new sphere tangent to all of them.

\[
k_{\mathrm{new}}
=
\sum_{j\in T}k_j
\pm
2\sqrt{\sum_{i<j\in T}k_ik_j}.
\]

**Key:** \(T\) = the tangent set of four curvatures that bound the pocket; \(+\) = inner fill.

Because the octant seed is not a classical five-sphere Descartes seed, the correct name is **osculatory packing**: always insert the largest non-overlapping sphere in the current largest pocket. In 3D that packing’s residual set has dimension \(\delta_3\approx 2.474\).

Pockets after generation 2:

| Pocket | Bounding objects | Role |
|--------|------------------|------|
| Centre (already filled) | eight daughters | \(\mathcal{B}_c^{(2)}\) |
| Near a parent-wall face | parent \(+\) four daughters of one hemisphere | next-largest family |
| Edge / triple junctions | parent \(+\) three daughters | smaller family |
| Deep residual | previous fillers | gasket tail |

Each new sphere is a bound sub-envelope: a stopped bounce with its own residual \(L\), hence its own binding quantum. That is hierarchical binding as a gasket, not as equal octant copies.

---

## 5. Binding dictionary

| Apollonian object | TSB bound-sector object |
|-------------------|-------------------------|
| Container sphere (\(k_0<0\)) | Survey envelope at \(\ell_{\mathrm{cap}}\) |
| Equal first-generation spheres | Octant Mirrons; may carry a survey fiber if they later hit cap on a later tick |
| Central / pocket spheres | Sub-cap Mirrons; no new survey \(S^1_\tau\) |
| Residual set (foam) | Unbound 3+1 leftover inside the cell (voids / filaments at small scale) |
| Smallest allowed sphere | \(\Phi_7\) floor; mass gap \(\Delta\) |
| Curvature \(k\) | Inverse envelope radius; not automatically an energy |

A sub-cap Mirron does **not** write a new survey Tau node. \(N_\tau=8^{g_{\mathrm{oct}}}\) stays the large-scale count. The gasket multiplies \(N_{\mathrm{b}}\), the bound-substructure count inside one node.

---

## 6. Spectrum of a bound cell

Order envelopes by curvature:

\[
k^{(1)} < k_c < k^{(3)} < \cdots < k_{\mathrm{PK}}.
\]

**Key:** \(k_{\mathrm{PK}}=1/\ell_{\mathrm{PK}}\) = cutoff at the Planck–Kerr seed.

- Vacuum of the cell: parent \(+\) octant eight, no extra pocket sphere required.  
- First hierarchical excitation: \(\mathcal{B}_c^{(2)}\) (central ball), or the first face-pocket sphere if that is assigned as a mode.  
- Dense high-\(k\) band: residual foam, counting \(\#\{k\le K\}\sim c K^{\delta_3}\).  
- Hard floor: no sphere with \(k>k_{\mathrm{PK}}\). That floor is \(\Delta\), still identified with the \(\Phi_7\) scrape, not with \(\delta_3\).

Energy is **not** \(\hbar c\,k\) unless a separate map \(E(k)\) is derived from residual \(L\).

---

## 7. Why this matches “hierarchical binding” and not the survey web

Octant generations that hit \(\ell_{\mathrm{cap}}\) build the cosmic-web skeleton (\(7\,h^{-1}\mathrm{Mpc}\) cells only if \(\ell_{\mathrm{cap}}\) is identified with \(\tau\)).

Apollonian generations live **inside** one skeleton cell. They are the globbing of binding quanta: smaller stopped bounces packed in the \(59\%\) interstitial after \(8+c\). Stochastic gravity as fractal globbing is this foam, not a graviton, and not a new fifth radius.

The atemporal cylinder \(\mathcal{C}_{\mathcal{PF}}\) is sampled at every pocket centre by \(\Phi_7\). Many pockets, one cylinder.

---

## 8. What remains illegal

- Setting \(\Delta=\delta_2\) or \(\Delta=\delta_3\) (dimensionless).  
- Setting \(\Delta=\hbar c/\tau\).  
- Letting gasket circles be the KK fiber \(S^1_\tau\).  
- Unlocking \(q=8\) because Descartes wants a 4-tuple (use osculatory fill in the *gaps* of the eight).  
- Using \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_{313})\) as a derivation of \(313.1\,\mathrm{MeV}\).

---

## 9. Status

| Item | Status |
|------|--------|
| Octant \(q=8\), \(a=R/(1+\sqrt{3})\) | locked |
| Central ball \(r_c=R(2-\sqrt{3})\), \(k_c=(2+\sqrt{3})/R\) | computed this session |
| Deeper pockets = osculatory / Apollonian | working model of hierarchical binding |
| Survey \(N_\tau\) | unchanged |
| \(\Delta\) from \(\Phi_7\) | unchanged; not computed here |

---

## 10. Next concrete calculation

Enumerate the first face-pocket curvature from parent \(k_0=-1/R\) plus a tangent triple of octant daughters, using the 3D Soddy formula. That number is the first *unequal* binding quantum above the eight-plus-centre seed, still in units of \(1/R\), still with no MeV on the right-hand side.

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
