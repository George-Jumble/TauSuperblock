# Session log: Integrate the quark-increment \(V_{\mathrm{orb}}\) sextet into an \(E_8\) projection

- **Session date:** Friday, 2026-09-18
- **Question:** Can the last output (Scheme A \(V_{\mathrm{orb}}\) from quark-mass increments) be integrated into an \(E_8\) projection?
- **Short answer:** Yes, as a *hybrid object*, not as a derivation of the masses from \(E_8\). Linear projection of the 240 equal-length \(E_8\) roots onto any coordinate 4-plane yields only three radii \(\{0,1,\sqrt{2}\}\) and cannot produce \(\gamma_t/\gamma_u\sim 8\times 10^4\). What \(E_8\) *does* supply parameter-free is a six-direction system: the fundamental weights of \(E_6\subset E_8\), with Gram matrix \(A_{E_6}^{-1}\). Attach the quark \(\beta_i\) as speeds *along those weight directions* by a named Dynkin-to-flavour map. The integrated relative Lorentz factor is
  \[
  \gamma_{ij}=\gamma_i\gamma_j\bigl(1-\beta_i\beta_j\cos\theta_{ij}\bigr),\qquad
  \cos\theta_{ij}=\frac{\langle\omega_i,\omega_j\rangle}{|\omega_i||\omega_j|},
  \]
  with \(\theta_{ij}\) from \(E_6\) and \((\gamma_i,\beta_i)\) from PDG increments. That is the projection. It does not retroactively make the sextet an \(E_8\) eigenvalue.
- **Parents:** `2026-09-18_V_orb_eigenvalues_from_quark_mass_increments.md`, `2026-09-18_Phi_from_8phase_E8_six_domain_cell_alpha_fs_attempt.md`
- **This file:** `Personal Files/2026-09-18_E8_projection_integrated_with_V_orb_quark_increments.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(E_8\) | Exceptional Lie algebra, \(\dim 248\), rank \(8\), \(240\) roots, all of length \(\sqrt{2}\) in the even-coordinate model. |
| \(E_6\subset E_8\) | Rank-\(6\) subalgebra. \(72\) roots. Cartan of \(E_6\) is the six-label space used below. |
| \(A_{E_6}\) | Cartan matrix of \(E_6\) (simply laced). \(\det A=3\). |
| \(\alpha_1,\ldots,\alpha_6\) | Simple roots of \(E_6\). Dynkin: chain \(1{-}2{-}3{-}4{-}5\), branch \(3{-}6\). |
| \(\omega_1,\ldots,\omega_6\) | Fundamental weights. Gram \(\langle\omega_i,\omega_j\rangle=(A_{E_6}^{-1})_{ij}\) when \(\langle\alpha,\alpha\rangle=2\). |
| \(\theta_{ij}\) | Angle between \(\omega_i\) and \(\omega_j\) in the \(E_6\) Cartan. |
| \(r\in\Delta_{E_8}\) | An \(E_8\) root. \(\lvert r\rvert=\sqrt{2}\). |
| \(P_4\) | Orthogonal projection \(\mathbb{R}^8\to\mathbb{R}^4\). Coordinate split \(4{+}4\) is the named linear probe. |
| \(\gamma_i,\beta_i,V_{\mathrm{orb},i}\) | Scheme A quark-increment eigenvalues of the parent note. Prime \(=u\) at rest. |
| \(\gamma_{ij}\) | Integrated relative Lorentz factor of domains \(i,j\). |
| \(\cos\theta_{ij}\) | Direction cosine from \(E_6\) weights, not from quark data. |
| Dynkin map | \(\omega_1\to u\), \(\omega_5\to d\) (short ends), \(\omega_2\to s\), \(\omega_4\to c\), \(\omega_6\to b\) (branch), \(\omega_3\to t\) (centre, longest weight). |
| \(G_{\mathrm{cell}}\) | 48-vertex 6-domain × 8-phase current graph. Domain-edge weights may now use \(\gamma_{ij}\) and \(\theta_{ij}\). |

---

## 1. What “integrate into an \(E_8\) projection” can mean

Three readings. Only one survives.

**Reading L (linear root projection produces \(\beta_i\)).**  
Project the 240 roots to a 4-plane and read six radii or six direction cosines as \(V_{\mathrm{orb}}\).  

**Reading W (weight directions from \(E_6\subset E_8\), speeds from quarks).**  
\(E_8\) chooses six axes. Quark increments choose six speeds on those axes. Relatives mix both.  

**Reading F (fit a 4-plane so projected norms equal \(\gamma_i\)).**  
That is an eight-parameter fit, not a projection. Rejected.

This note executes L as a negative probe and W as the integration.

---

## 2. Reading L fails (and why)

Even \(E_8\) roots, standard model:
- \(112\) vectors \(\pm e_i\pm e_j\),
- \(128\) half-integer vectors \(\tfrac12(\pm 1^8)\) with even minus count.

All have length \(\sqrt{2}\). A linear functional (inner product with a coordinate axis) takes values in \(\{0,\pm\tfrac12,\pm 1\}\) only. Orthogonal projection onto the first four coordinates takes radii in
\[
\{0,\,1,\,\sqrt{2}\}
\]
only (24 roots project to the origin; the rest sit on two shells). There is no linear image of the root system whose six radii reproduce
\[
\gamma=(1,\;2.176,\;43.29,\;589.4,\;1937,\;7.989\times 10^4).
\]
**Lemma.** No linear \(E_8\)-root projection yields the quark-increment hierarchy. The last output cannot be *derived* as an \(E_8\) eigenvalue sextet.

The \(E_6\) fundamental-weight *lengths* are also the wrong shape:
\[
\frac{|\omega|}{|\omega_1|}=(1,\;1.581,\;2.121,\;1.581,\;1,\;1.225)
\]
versus \(\gamma/\gamma_u=(1,\;2.176,\;43.29,\;589,\;1937,\;79889)\). Four length classes against six wildly separated masses.

---

## 3. Reading W: the hybrid projection

### 3.1 Six axes from \(E_6\subset E_8\)

Cartan matrix (nodes \(1{-}2{-}3{-}4{-}5\), branch at \(3\) to \(6\)):
\[
A_{E_6}
=
\begin{pmatrix}
2&-1&0&0&0&0\\
-1&2&-1&0&0&0\\
0&-1&2&-1&0&-1\\
0&0&-1&2&-1&0\\
0&0&0&-1&2&0\\
0&0&-1&0&0&2
\end{pmatrix}.
\]
**Key:** \(A_{E_6}\) is unique given the Dynkin diagram. No quark input.

Gram of the fundamental weights, \(\langle\alpha,\alpha\rangle=2\):
\[
\langle\omega_i,\omega_j\rangle=(A_{E_6}^{-1})_{ij}.
\]
Diagonal: \(\omega_i^2=\bigl(\tfrac43,\;\tfrac{10}{3},\;6,\;\tfrac{10}{3},\;\tfrac43,\;2\bigr)\).  
Direction cosines \(\cos\theta_{ij}=\langle\omega_i,\omega_j\rangle/(|\omega_i||\omega_j|)\):

|  | \(\omega_1\) | \(\omega_2\) | \(\omega_3\) | \(\omega_4\) | \(\omega_5\) | \(\omega_6\) |
|---|---|---|---|---|---|---|
| \(\omega_1\) | \(1\) | \(0.7906\) | \(0.7071\) | \(0.6325\) | \(0.5000\) | \(0.6124\) |
| \(\omega_2\) |  | \(1\) | \(0.8944\) | \(0.8000\) | \(0.6325\) | \(0.7746\) |
| \(\omega_3\) |  |  | \(1\) | \(0.8944\) | \(0.7071\) | \(0.8660\) |
| \(\omega_4\) |  |  |  | \(1\) | \(0.7906\) | \(0.7746\) |
| \(\omega_5\) |  |  |  |  | \(1\) | \(0.6124\) |
| \(\omega_6\) |  |  |  |  |  | \(1\) |

Angles in degrees (rounded): \(0\), and among off-diagonal \(26.6^\circ\)–\(60^\circ\). The two ends \(\omega_1,\omega_5\) sit at \(60^\circ\). The centre \(\omega_3\) sits at \(30^\circ\) from the branch \(\omega_6\).

A coordinate drop \(\mathbb{R}^6\to\mathbb{R}^4\) (naïve “\(S^3\subset\mathbb{R}^4\)”) *collapses* \(\omega_4\) onto \(\omega_5\) and \(\omega_3\) onto \(\omega_6\). Do not use that split. Keep the six axes in the \(E_6\) Cartan. The corpus \(S^3\) is the orbital manifold of one domain; the *labels* of the six domains live in the Cartan.

### 3.2 Named Dynkin-to-flavour map

Short ends \(\leftrightarrow\) light pair, centre (longest weight) \(\leftrightarrow\) heaviest flavour, branch \(\leftrightarrow\) \(b\):
\[
\omega_1\to u,\;
\omega_5\to d,\;
\omega_2\to s,\;
\omega_4\to c,\;
\omega_6\to b,\;
\omega_3\to t.
\]
**Key:** this uses only length-class and Dynkin position. It does not fit angles to masses. A different pairing (swap \(s\leftrightarrow c\), swap \(b\leftrightarrow t\)) is a discrete choice of size \(2\times 2=4\) inside the length classes and should be treated as a four-element discrete scan, not a continuum fit. Headline pairing is the one above.

### 3.3 Speeds from the parent note (Scheme A, PDG 2025)

\[
\beta
=
(0,\;0.8881,\;0.999733,\;1-1.440\times 10^{-6},\;1-1.333\times 10^{-7},\;1-7.83\times 10^{-11})
\]
in flavour order \((u,d,s,c,b,t)\), then reordered onto \((\omega_1,\omega_2,\omega_3,\omega_4,\omega_5,\omega_6)=(u,s,t,c,d,b)\).

### 3.4 Integrated relative factor

Two domains with speeds \(\beta_i,\beta_j\) and \(E_6\) angle \(\theta_{ij}\):
\[
\gamma_{ij}
=
\gamma_i\gamma_j\bigl(1-\beta_i\beta_j\cos\theta_{ij}\bigr).
\]
**Key:** \(\gamma_i=m_i/m_u\); \(\cos\theta_{ij}\) from §3.1; \(\beta_i\) from Scheme A. If \(\beta_u=0\), the Prime row collapses to \(\gamma_{uj}=\gamma_j\) independent of angle, as it must.

Headline \(\gamma_{ij}\) (order \(u,s,t,c,d,b\)):

|  | \(u\) | \(s\) | \(t\) | \(c\) | \(d\) | \(b\) |
|---|---|---|---|---|---|---|
| \(u\) | \(1\) | \(43.3\) | \(7.99\times 10^4\) | \(589\) | \(2.18\) | \(1.94\times 10^3\) |
| \(s\) |  | \(1\) | \(3.66\times 10^5\) | \(5.11\times 10^3\) | \(41.3\) | \(1.89\times 10^4\) |
| \(t\) |  |  | \(1\) | \(4.97\times 10^6\) | \(6.47\times 10^4\) | \(2.07\times 10^7\) |
| \(c\) |  |  |  | \(1\) | \(382\) | \(2.57\times 10^5\) |
| \(d\) |  |  |  |  | \(1\) | \(1.92\times 10^3\) |
| \(b\) |  |  |  |  |  | \(1\) |

Off-diagonal span: \(2.18\) (\(u\)–\(d\)) to \(2.07\times 10^7\) (\(t\)–\(b\)). Same-direction collinear limits from the parent note sit inside this span; antipodal (\(180^\circ\)) limits lie above it. \(E_6\) angles are acute, so the integrated relatives are *closer to the same-direction column* than to the octahedron-antipode column.

---

## 4. What this gives the \(\Phi\) cell

Domain-edge conductance on \(G_{\mathrm{cell}}\) can now be a named function of the hybrid:
\[
w_{ij}=w\bigl(\gamma_{ij},\,\theta_{ij}\bigr).
\]
Two local choices, still not fitted:
- \(w_{ij}\propto 1/\gamma_{ij}\) (mixing suppressed by relative boost),
- \(w_{ij}\propto\cos\theta_{ij}\) (mixing by \(E_6\) alignment only; speeds unused on the edge).

Either is an \(E_8\)-integrated weighting. Neither is computed through the 48-vertex Laplacian in this note. The angle system is no longer \(K_6\) (all edges equal) and no longer a unit octahedron. It is the \(E_6\) weight graph with four distinct off-diagonal cosines \(\{1/2,\;1/\sqrt{2},\;\sqrt{2/3},\;\sqrt{4/5},\ldots\}\).

---

## 5. What is *not* claimed

- \(E_8\) does not produce \(m_t/m_u\).
- The Dynkin map is discrete and small; it is not unique by a theorem, only by a named rule.
- Projecting the Cartan to a literal \(S^3\subset\mathbb{R}^4\) by dropping two coordinates destroys two axes. The orbital \(S^3\) and the label Cartan are different spaces.
- \(\langle\gamma\rangle_6\) of the parent note is still not the \(\langle\gamma\rangle_6\) of the 313.1 MeV Planck–Kerr averaging formula.
- \(\alpha_{\mathrm{fs}}\) is still not derived.

---

## 6. Direct answer

Yes: integrate by letting \(E_6\subset E_8\) furnish six axes and six angles, and letting the quark-increment sextet furnish six speeds on those axes. The projection that actually mixes the two sides is
\[
\gamma_{ij}=\gamma_i\gamma_j(1-\beta_i\beta_j\cos\theta_{ij}^{E_6}).
\]
No: do not call the PDG \(\beta_i\) “the \(E_8\) projection eigenvalues.” Linear root projection cannot emit that hierarchy. The last output remains phenomenological. \(E_8\) now owns the *wiring and the angles*, not the speeds.

---

## Ledger

| Item | Status |
|---|---|
| Linear \(E_8\)-root radii equal quark \(\gamma_i\) | False (3 shells vs 6 masses) |
| \(E_6\) weight-length ratios equal quark \(\gamma_i\) | False |
| \(E_6\) Gram angles parameter-free | Computed |
| Dynkin map \(\omega\to\) flavour | Named, discrete |
| Hybrid \(\gamma_{ij}\) table | Computed |
| Laplacian of \(G_{\mathrm{cell}}\) with \(w(\gamma_{ij},\theta_{ij})\) | Not computed this session |
| Speeds derived from \(E_8\) | Not claimed |

---

## Sources

- Parent: `2026-09-18_V_orb_eigenvalues_from_quark_mass_increments.md` (Scheme A sextet, PDG 2025)
- Standard \(E_8\) root model; \(E_6\) Cartan and \(A^{-1}\)
- TSB lock: six domains, \(E_8\) language in the unification / book outline (used as motivation, not as a hidden numerical table)

---

*End of session note — 2026-09-18 \(E_8\) projection integrated with quark-increment \(V_{\mathrm{orb}}\).*
