# Session 2026-09-14 — \(\Phi_7,\Phi_8\), spectrum of \(W\), and \(\iota\)

**Rule:** matrices from octonion algebra and a mirror involution. Not fitted to \(\rho_\Lambda\).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(e_0=1,e_1,\ldots,e_7\) | Standard octonion basis |
| \(C\) | Conjugation: \(e_0\mapsto e_0\), \(e_i\mapsto -e_i\) |
| \(L_{e_7}\) | Left multiplication by \(e_7\) |
| \(\Phi_7=C\) | Scrape / PK mirror |
| \(\Phi_8=L_{e_7}\) | Refresh along the scrape axis |
| \(W=\Phi_8\Phi_7=L_{e_7}C\) | One scrape-then-refresh |
| \(v_+\) | \(+1\)-eigenvector of \(W\) |
| \(v_-\) | \(-1\)-eigenvector of \(W\) |
| \(\iota\) | Map \(\mathbb{R}^8\to\) functions of homogeneity \(-4\) on \(\pi_{A'}\) |
| \(n\) | Twistor homogeneity |
| \(s\) | Helicity |
| \(a=1,\ldots,6\) | Domain index \(\leftrightarrow e_a\) |
| \(\zeta=\pi_{1'}/\pi_{0'}\) | Celestial chart |

Fano triples used for products \(e_ie_j=e_k\):  
\((1,2,3),\ (1,4,5),\ (1,6,7),\ (2,4,6),\ (2,5,7),\ (3,4,7),\ (3,5,6)\).

---

## 2. Locked field type

Unbound sector = photon (paper 21222606).

\[
s=+1,
\qquad
n=-2s-2=-4.
\]

**Key:** one helicity locked so \(f(\lambda Z)=\lambda^{-4}f(Z)\). The opposite helicity is the conjugate copy; not needed to define \(W\).

---

## 3. Six-domain map into \(\mathbb{PT}\)

\[
a\ \in\{1,\ldots,6\}
\;\longmapsto\;
e_a
\;\longmapsto\;
\text{the }\mathbb{CP}^1\text{ of null flags rotated by }L_{e_a}.
\]

**Key:** domains are the six imaginaries orthogonal to the scrape axis \(e_7\). There is no seventh spacetime. \(\phi_7\) is \(e_7\) itself (mirror axis). \(\phi_8\) is the tick \(L_{e_7}\).

A Prime event \(x\) still gives the incidence line \(\mathcal{R}_x\subset\mathbb{PT}\). Domain \(a\) is that line acted on by \(L_{e_a}\).

---

## 4. The matrices

\(\Phi_7=\mathrm{diag}(1,-1,-1,-1,-1,-1,-1,-1)\).

\(\Phi_8=L_{e_7}\) in the basis \((e_0,\ldots,e_7)\):

\[
L_{e_7}e_0=e_7,
\quad
L_{e_7}e_7=-e_0,
\quad
L_{e_7}e_i=e_7e_i\ (i=1,\ldots,6).
\]

**Key:** computed from the Fano table above.

\[
W=L_{e_7}C.
\]

\(W\) is real orthogonal, \(\det W=-1\).

---

## 5. Spectrum of \(W\) (computed)

\[
\mathrm{spec}(W)
=
\{
+1,\ -1,\ +i,\ +i,\ +i,\ -i,\ -i,\ -i
\}.
\]

**Key:** one-dimensional real eigenspaces for \(\pm 1\); the six domain directions sit in the period-4 (\(\pm i\)) planes.

\[
v_+
=
\frac{1}{\sqrt{2}}(e_0+e_7),
\qquad
Wv_+=+v_+,
\]

\[
v_-
=
\frac{1}{\sqrt{2}}(e_0-e_7),
\qquad
Wv_-=-v_-.
\]

**Key:** vacuum tick = identity-plus-mirror-axis. Inversion tick = \(v_-\).

The six-dimensional complement (span\(\{e_1,\ldots,e_6\}\)) is rotated by \(90^\circ\) each word \(W\). That is domain motion, not the vacuum mode.

---

## 6. The map \(\iota\)

On the primed spinor \(\pi_{A'}\),

\[
\iota(v)(\pi)
=
\bigl(v_0\,\pi_{0'}+v_7\,\pi_{1'}\bigr)^{-4}.
\]

**Key:** only the \((e_0,e_7)\) components enter the vacuum \(f\), because \(v_\pm\) live in that plane; \(n=-4\) is the locked homogeneity.

Vacuum waveform:

\[
f_+
=
\iota(v_+)
=
2^{2}
\bigl(\pi_{0'}+\pi_{1'}\bigr)^{-4}.
\]

**Key:** overall constant is conventional (\(T_{00}\) will eat \(U^4\) later). Do not rescale \(v_+\) to fit \(\rho_\Lambda\).

Check: \(f_+(\lambda\pi)=\lambda^{-4}f_+(\pi)\). Helicity \(+1\) contour \(\oint \pi_{A'}\pi_{B'}f\,\pi d\pi\) is the standard Penrose map for \(s=+1\).

---

## 7. What a stranger can recompute

From the Fano triples and \(\Phi_7=C\), \(\Phi_8=L_{e_7}\):

- \(W\) as an \(8\times 8\) matrix  
- \(\mathrm{spec}(W)\)  
- \(v_\pm\)  
- \(f_+=\iota(v_+)\)

No observed density is an input.

---

## 8. Still not done (next for \(\rho_\Lambda\))

\(T_{00}[f_+]\) and the seed \(U\). \(\iota\) puts \(f\) on \(\pi_{A'}\), not yet an energy density. Domain average of the \(\pm i\) sector is a correction, not the zero mode.

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
