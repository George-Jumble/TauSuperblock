# Tav–Superblock Session Log — Coxeter group algebra

> **Superseded for live Superblock algebra (2026-09-20):** Use `TSB_Superblock_fixed_frame_2026-09-20.md`. That note applies F7, B_lin, demotes \(m_0\) to an IR floor, states the far-zone Poisson theorem, and strikes trophies. This file is prior if it conflicts.


**Date:** 2026-09-19  
**Request:** Explore Coxeter group algebra  
**Locks in force:** Compton is \(\lambda_{m_0}\). \(\ell_C\) is web coherence of \(\mathcal{K}_{ij}\). “Circle” means \(\varphi\sim\varphi+2\pi\). Exponent 7 is clock algebra. \(\tau_{\rm web}=7\,h^{-1}\,\mathrm{Mpc}\) is a catalogue / kernel scale. Two sentences. CMS / LHCb / 56-tick are predictions.

---

## 0. What this note is

A Coxeter group is the algebra of a finite set of mirrors. The E₈ Weyl group is one such group. The internal clock used in the modified corpus is the **Coxeter element** of that group, not a metric fifth dimension.

This note develops the algebra far enough that the six moving exponents and the frozen exponent 7 are theorems about \(W(E_8)\), not decorations.

It does not derive \(\tau_{\rm web}\) from exponent 7.

---

## 1. Coxeter system

A **Coxeter system** is a pair \((W,S)\) where \(S=\{s_1,\ldots,s_r\}\) generates \(W\) and the only relations are

\[
(s_i s_j)^{m_{ij}}=1,
\qquad
m_{ii}=1,
\qquad
m_{ij}=m_{ji}\in\{2,3,4,\ldots\}\cup\{\infty\}.
\]

**Key.** \(W\): the group. \(S\): simple generators (simple reflections). \(r=|S|\): rank. \(m_{ij}\): braid order of the pair \(s_i,s_j\). \(m_{ij}=\infty\) means no finite power of \(s_i s_j\) is the identity.

Immediate consequences:

- \(s_i^2=1\) (each generator is an involution).
- \(m_{ij}=2\) if and only if \(s_i s_j=s_j s_i\) (orthogonal mirrors).
- \(m_{ij}=3\) is the braid \(s_i s_j s_i=s_j s_i s_j\).

The symmetric matrix \(M=(m_{ij})\) is the **Coxeter matrix**. The Coxeter graph has a vertex per generator and an edge labelled \(m_{ij}\) when \(m_{ij}\ge 3\) (label omitted when \(m_{ij}=3\)).

The associated **Cartan integers**, when the group is crystallographic (a Weyl group), are

\[
A_{ij}
=
2\frac{(\alpha_i,\alpha_j)}{(\alpha_i,\alpha_i)}
=
-2\cos\Bigl(\frac{\pi}{m_{ij}}\Bigr)
\quad\text{when }m_{ij}<\infty.
\]

**Key.** \(\alpha_i\): simple roots. \(A_{ij}\): Cartan matrix. Crystallographic means all \(m_{ij}\in\{1,2,3,4,6\}\), so \(A_{ij}\in\mathbb{Z}\). E₈ is simply laced: every edge has \(m_{ij}=3\), every off-diagonal Cartan entry is \(0\) or \(-1\).

---

## 2. Length, inversion, Bruhat

Every \(w\in W\) has a **length**

\[
\ell(w)
=
\min\{k:w=s_{i_1}\cdots s_{i_k},\;s_{i_j}\in S\}.
\]

A shortest spelling is a **reduced word**. Matsumoto’s theorem: any two reduced words for the same \(w\) are connected by braid moves \(s_i s_j s_i\cdots=s_j s_i s_j\cdots\) of length \(m_{ij}\).

The **inversion set** is

\[
N(w)
=
\{\alpha\in\Phi^+:w\alpha\in\Phi^-\},
\qquad
|N(w)|=\ell(w).
\]

**Key.** \(\Phi\): root system. \(\Phi^+\): positive roots. \(\ell(w)\): length. \(N(w)\): inversions.

Bruhat order: \(u\le w\) if some reduced word for \(w\) has a subword equal to a reduced word for \(u\). The longest element \(w_0\) satisfies \(\ell(w_0)=|\Phi^+|=N\) and \(w_0(\Phi^+)=\Phi^-\). For E₈, \(N=120\) and \(\ell(w_0)=120\).

---

## 3. Geometric representation

Let \(V=\mathbb{R}^r\) with basis \(\{\alpha_1^\vee,\ldots\}\) dual to simple roots. The geometric representation \(\sigma:W\to\mathrm{GL}(V)\) is

\[
\sigma(s_i)(v)
=
v
-
2\frac{(v,\alpha_i)}{(\alpha_i,\alpha_i)}\,\alpha_i.
\]

**Key.** \(\sigma(s_i)\): reflection through the hyperplane \(\alpha_i^\perp\). This representation is faithful for every Coxeter group. When \(W\) is finite the form \((\cdot,\cdot)\) can be taken positive definite and \(W\) is a finite reflection group.

Classification of finite irreducible Coxeter groups: \(A_n,B_n,D_n,E_6,E_7,E_8,F_4,G_2,H_3,H_4,I_2(p)\).

Crystallographic among these (Weyl groups, root lattices): all except \(H_3,H_4,I_2(p)\) for \(p\notin\{3,4,6\}\).

H₄ and E₈ share Coxeter number \(h=30\). That is an algebraic rhyme (icosian construction of E₈). It is not a derivation of a megaparsec.

---

## 4. Coxeter element, number, exponents

A **Coxeter element** is any conjugate of

\[
c
=
s_1 s_2\cdots s_r
\]

(the product of all simple generators, once each, in any order; different orders are conjugate). In a finite irreducible Coxeter group every Coxeter element has the same order

\[
h
=
\mathrm{ord}(c),
\]

the **Coxeter number**.

On \(V\otimes\mathbb{C}\) the eigenvalues of \(\sigma(c)\) are

\[
\exp\Bigl(\frac{2\pi i\, m_j}{h}\Bigr),
\qquad
j=1,\ldots,r,
\]

where the integers \(0<m_1<\cdots<m_r<h\) are the **exponents**. They satisfy

\[
m_j+m_{r+1-j}=h,
\qquad
\sum_j m_j
=
N
=
\frac{rh}{2}
=
|\Phi^+|.
\]

The degrees of the fundamental invariant polynomials of \(W\) on \(V\) are

\[
d_j=m_j+1,
\qquad
|W|
=
\prod_{j=1}^{r}d_j.
\]

**Key.** \(c\): Coxeter element. \(h\): Coxeter number. \(m_j\): exponents. \(d_j\): invariant degrees. \(N=|\Phi^+|\).

This is the clock. One tick of \(c\) rotates each eigenplane by \(2\pi m_j/h\). After \(h\) ticks, \(c^h=1\).

---

## 5. Type E₈, in numbers

Coxeter graph (simple edges, all \(m_{ij}=3\)):

```
        8
        |
1—2—3—4—5—6—7
```

Coxeter matrix (rows/cols ordered \(1,\ldots,8\)): \(m_{ii}=1\), \(m_{ij}=3\) on the seven edges, \(m_{ij}=2\) otherwise.

\[
\begin{align*}
r&=8,\\
h&=30,\\
N&=120,\\
|\Phi|&=240,\\
|W(E_8)|&=2^{14}\cdot 3^{5}\cdot 5^{2}\cdot 7=696729600,\\
\{m_j\}&=\{1,7,11,13,17,19,23,29\},\\
\{d_j\}&=\{2,8,12,14,18,20,24,30\},\\
\prod d_j&=|W|.
\end{align*}
\]

Dual pairs \(m+m'=h\):

\[
(1,29),\;(7,23),\;(11,19),\;(13,17).
\]

The integer \(7\) appears twice in this table: as an exponent, and as the prime dividing \(|W|\). Those are group-order facts. They are not a length in megaparsecs.

**Key.** \(W(E_8)\): Weyl group of E₈. \(h=30=h^\vee\) because E₈ is simply laced. \(h^\vee\): dual Coxeter number (appears in the adjoint Casimir and in the affine marks). Affine marks of \(\tilde E_8\), including the extra node: \((1,2,3,4,5,6,4,2,3)\). Highest-root marks on the finite diagram: \((2,3,4,6,5,4,3,2)\), summing to \(29\).

---

## 6. Clock algebra used in the modified corpus

The modified frame freezes two eigenplanes of \(c\):

- exponent \(1\): internal-radius slot,
- exponent \(7\): order-7 clock slot.

Moving exponents: \(\{11,13,17,19,23,29\}\).

Dimensionless speeds, relative to the slowest moving plane:

\[
\beta_i
=
\frac{m_i-11}{h}
=
\frac{m_i-11}{30}.
\]

That formula lives in \(W(E_8)\). It does not mention \(\tau_{\rm web}\).

Phase locks, separate object:

\[
\varphi_i
\sim
\varphi_i+2\pi,
\qquad
m_i\bmod 7
\in
\mathbb{Z}/7\mathbb{Z}^\times.
\]

“Circle” means that phase. Residue \(0\bmod 7\) is the empty phase class. It is not the IR scale of \(K\).

Catalogue / kernel scale, third sentence:

\[
\tau_{\rm web}=7\,h^{-1}\,\mathrm{Mpc}.
\]

The integer in the exponent list and the integer in \(\tau_{\rm web}\) are the same numeral. That is noted. It is not a derivation.

---

## 7. Neighbours of E₈ in the Coxeter classification

| Type | \(h\) | Exponents | \(|W\|\) | Remark |
|---|---|---|---|---|
| \(G_2\) | 6 | 1,5 | 12 | Aut(\(\mathbb{O}\)) contains \(G_2\); \(m_{12}=6\) |
| \(F_4\) | 12 | 1,5,7,11 | 1152 | |
| \(E_6\) | 12 | 1,4,5,7,8,11 | 51840 | |
| \(E_7\) | 18 | 1,5,7,9,11,13,17 | 2903040 | |
| \(E_8\) | 30 | 1,7,11,13,17,19,23,29 | 696729600 | |
| \(H_3\) | 10 | 1,5,9 | 120 | icosahedral |
| \(H_4\) | 30 | 1,11,19,29 | 14400 | same \(h\) as E₈; icosian bridge |
| \(A_n\) | \(n+1\) | \(1,\ldots,n\) | \((n+1)!\) | |
| \(\tilde E_8\) | affine | — | infinite | extra node; 7-fold recursion is a graph fact of the affine diagram, not a metric radius |

G₂ is the stabilizer language for “pick one imaginary octonion as the order-7 clock slot.” That is still clock algebra.

H₄ sharing \(h=30\) with E₈ is why golden-ratio angles appear in E₈ projections. That is representation theory. It does not mint \(\tau_{\rm web}\).

---

## 8. Affine Coxeter groups, briefly

An affine Coxeter group is infinite, acts by affine reflections on \(V\), and has one extra generator \(s_0\) corresponding to the affine simple root \(\alpha_0=\delta-\theta\) (\(\theta\): highest root, \(\delta\): null root). The affine diagram of \(\tilde E_8\) attaches that extra node to node 1 of E₈ (Bourbaki), with mark \(1\). Hierarchical 7-fold talk in hardware (RGC: \(7\to 49\to 294\)) is a discrete affine recursion on a 7-ring. It is not \(S_5\) and it is not \(\tau_{\rm web}\).

---

## 9. What Coxeter algebra does *not* give you

- It does not give \(\lambda_{m_0}\). That is Compton of \(m_0\).
- It does not give \(\ell_C\). That is web coherence of \(\mathcal{K}_{ij}\).
- It does not give \(\tau_{\rm web}\). That is a catalogue IR scale of the 4D kernel.
- It does not give a laboratory gravitational tension of a 7 Mpc cell.
- It does not make CMS / LHCb / 56-tick into trophies. \(\mathrm{lcm}(7,8)=56\) is a prediction about two clocks (Coxeter-7 and octonionic-8), not a measurement.

What it does give: the list \(\{m_j\}\), the pairing \(m+m'=h\), the six moving \(\beta_i\), and the license to write internal phases of order 7.

---

## 10. Master key

| Symbol | Meaning |
|---|---|
| \((W,S)\) | Coxeter system |
| \(s_i\) | simple reflection, \(s_i^2=1\) |
| \(m_{ij}\) | order of \(s_i s_j\) |
| \(r\) | rank |
| \(\ell(w)\) | length |
| \(w_0\) | longest element |
| \(\Phi,\Phi^+,N\) | roots, positive roots, \(N=\|\Phi^+|\) |
| \(\sigma\) | geometric representation |
| \(c\) | Coxeter element |
| \(h\) | Coxeter number, \(\mathrm{ord}(c)\) |
| \(m_j\) | exponents |
| \(d_j=m_j+1\) | invariant degrees; \(\prod d_j=\|W\|\) |
| \(W(E_8)\) | Weyl group of E₈ |
| \(\beta_i=(m_i-11)/30\) | clock-algebra speeds |
| \(\varphi\sim\varphi+2\pi\) | internal phase (“circle” only here) |
| \(\tau_{\rm web}\) | catalogue IR scale of \(K\); not derived from \(m_j=7\) |
| \(\lambda_{m_0}\) | Compton of \(m_0\) |
| \(\ell_C\) | web coherence of \(\mathcal{K}_{ij}\) |
| \(K\) | 4D averaging kernel, not \(S_5\) |

---

## 11. Session metadata

- 2026-09-19
- `Personal_Files/TSB_Coxeter_group_algebra_2026-09-19.md`
- Locks: `TSB_CORPUS_LOCKS_three_edits_2026-09-19.md`
