# Tav–Superblock Session Log — Fixed E₈ Cartan Frame and the Tav Circle

> **Superseded for live Superblock algebra (2026-09-20):** Use `TSB_Superblock_fixed_frame_2026-09-20.md`. That note applies F7, B_lin, demotes \(m_0\) to an IR floor, states the far-zone Poisson theorem, and strikes trophies. This file is prior if it conflicts.


> **Corpus locks (2026-09-19, governing):** Compton length is $\lambda_{m_0}=\hbar/(m_0 c)$, not $\ell_C$. $\ell_C$ is web coherence of $\mathcal{K}_{ij}$ (Mpc-class). $K$ is a 4D averaging kernel; its IR end is an IR scale $\tau_{\rm web}$, not a metric circle. Say “circle” only for internal phase $\varphi\sim\varphi+2\pi$. Coxeter exponent 7 is clock algebra. $7\,h^{-1}\,\mathrm{Mpc}$ is catalogue / kernel scale $\tau_{\rm web}$. Two sentences. One-operator UV/IR language is a working hypothesis only if $K$ is not $S_5$ and $m_0$ is not derived from $\tau$. CMS / LHCb / 56-tick remain predictions. See `TSB_CORPUS_LOCKS_three_edits_2026-09-19.md`.


**Date:** 2026-09-19  
**Follows:** `TSB_Kernel_Six_Vorb_real_ellC_2026-09-19.md`  
**Request:** fix the E₈ Cartan frame, then explore the Tav circle  
**Convention:** Mirron, never “soliton”. All core values geometric.

---

## 0. The frame that is being fixed

The previous kernel left the five nonzero \(\beta_i\) as “a finite list of algebraic numbers once the Cartan frame is fixed.” This session fixes that frame.

**Rule (no free continuous parameter).**

1. Realize E₈ in the even coordinate system on \(\mathbb{R}^8\).
2. Use the Coxeter element of the Weyl group as the internal clock.
3. Freeze the two eigenplanes whose exponents are \(1\) (overall \(S^3_{\rm int}\) radius) and \(7\) (the Tav circle). Exponent \(7\) is the unique Coxeter exponent that *is* the Tav integer.
4. The remaining six exponents label the six domains.
5. Dimensionless orbital speeds are the Coxeter winding numbers relative to Prime, in units of the Coxeter number \(h^\vee(E_8)=30\).

That is the frame.

---

## 1. Even-coordinate Cartan frame of E₈

### 1.1 Roots

Even coordinate system: vectors in \(\mathbb{R}^8\) of squared length \(2\) whose coordinates are all integers or all half-integers, with even coordinate sum.

- \(112\) integer roots: all permutations of \((\pm 1,\pm 1,0,0,0,0,0,0)\).
- \(128\) half-integer roots: all \((\pm\tfrac12,\ldots,\pm\tfrac12)\) with an even number of minus signs.

### 1.2 Simple roots (rows; this Gram *is* the Cartan matrix)

\[
\begin{align*}
\alpha_1 &= (1,-1,0,0,0,0,0,0),\\
\alpha_2 &= (0,1,-1,0,0,0,0,0),\\
\alpha_3 &= (0,0,1,-1,0,0,0,0),\\
\alpha_4 &= (0,0,0,1,-1,0,0,0),\\
\alpha_5 &= (0,0,0,0,1,-1,0,0),\\
\alpha_6 &= (0,0,0,0,0,1,1,0),\\
\alpha_7 &= \bigl(-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12\bigr),\\
\alpha_8 &= (0,0,0,0,0,1,-1,0).
\end{align*}
\]

The Gram matrix \(G_{ij}=(\alpha_i,\alpha_j)\) equals the standard E₈ Cartan matrix \(A_{ij}\) (simply laced, \((\alpha,\alpha)=2\)).

### 1.3 Inverse Cartan matrix and fundamental-weight norms

\[
A^{-1}
=
\begin{pmatrix}
2&3&4&5&6&4&2&3\\
3&6&8&10&12&8&4&6\\
4&8&12&15&18&12&6&9\\
5&10&15&20&24&16&8&12\\
6&12&18&24&30&20&10&15\\
4&8&12&16&20&14&7&10\\
2&4&6&8&10&7&4&5\\
3&6&9&12&15&10&5&8
\end{pmatrix}.
\]

With \((\alpha,\alpha)=2\),

\[
\|\omega_i\|^2
=
(A^{-1})_{ii}
=
(2,6,12,20,30,14,4,8).
\]

Highest-root marks (coefficients of \(\theta\) on the simple roots): \((2,3,4,6,5,4,3,2)\), summing to \(29\). Affine marks including the extra node: \((1,2,3,4,5,6,4,2,3)\). Dual Coxeter number \(h^\vee=30\).

### 1.4 Variable key (Cartan)

| Symbol | Meaning |
|---|---|
| \(\alpha_i\) | simple roots of E₈ in the even frame |
| \(A_{ij}\) | Cartan matrix, \(A_{ij}=2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)\) |
| \(\omega_i\) | fundamental weights, \((\omega_i,\alpha_j)=\delta_{ij}\) |
| \(\theta\) | highest root |
| \(h^\vee=30\) | dual Coxeter number of E₈ |
| \(\Lambda_{E_8}\) | E₈ root lattice |

---

## 2. Coxeter clock and the freeze

The Coxeter element \(c=s_1 s_2\cdots s_8\) acts on the Cartan as a product of four orthogonal plane rotations. Eigenvalues:

\[
\exp\bigl(2\pi i\, m_j / h^\vee\bigr),
\qquad
m_j\in\{1,7,11,13,17,19,23,29\}.
\]

These eight exponents pair as \((m,\,h^\vee-m)\):

\[
(1,29),\quad (7,23),\quad (11,19),\quad (13,17).
\]

Each pair is a complex-conjugate eigenplane of \(c\).

**Freeze.**

- Exponent \(1\): overall breathing of \(S^3_{\rm int}\) (fibre radius \(R_{\rm int}\)). Lowest, “trivial” winding.
- Exponent \(7\): the Tav circle \(S^1_\tau\). This is the unique exponent equal to the Tav integer \(7\). Its dual \(23\) remains among the moving domains and will lock to the clock.

Moving exponents, in increasing order:

\[
\{11,13,17,19,23,29\}.
\]

### 2.1 Why this freeze is forced, not chosen

- TSB already demands a compact \(S^1\) of sevenfold resonance. E₈ has exactly one Coxeter exponent equal to \(7\).
- Rank \(8-2=6\) matches the six domains.
- Octonions: seven imaginary units; pick one (\(e_7\)) as the Tav generator; six remain. G₂ = Aut(\(\mathbb{O}\)) is the stabilizer of that split. The E₈ \(\to\) G₂ chain of the kernel note is this freeze.

---

## 3. The six \(\beta_i\) and \(V_{\rm orb}^{(i)}\)

Coxeter advances phase by \(2\pi m / 30\) per tick. Identify the dimensionless orbital speed of a domain with its winding number *relative to Prime*, in units of \(h^\vee\):

\[
\beta_i
=
\frac{m_i-m_{\rm Prime}}{h^\vee}
=
\frac{m_i-11}{30}.
\]

Prime is the slowest moving exponent, so the Prime chart is instantaneously comoving with that eigenplane and \(\beta_1=0\) by construction. All six speeds stay strictly below \(1\) because the largest offset is \(18<30\).

| Domain | Role | \(m_i\) | \(\beta_i=V_{\rm orb}^{(i)}/c\) | \(\beta_i^2\) | \(\gamma_i=(1-\beta_i^2)^{-1/2}\) |
|---|---|---|---|---|---|
| \(D_1\) | Prime (future) | \(11\) | \(0\) | \(0\) | \(1\) |
| \(D_2\) | Strange | \(13\) | \(1/15\) | \(1/225\) | \(\sqrt{225/224}\) |
| \(D_3\) | Charm | \(17\) | \(1/5\) | \(1/25\) | \(\sqrt{25/24}\) |
| \(D_4\) | Bottom′ (past) | \(19\) | \(4/15\) | \(16/225\) | \(\sqrt{225/209}\) |
| \(D_5\) | Top′ | \(23\) | \(2/5\) | \(4/25\) | \(\sqrt{25/21}\) |
| \(D_6\) | Beauty′ | \(29\) | \(3/5\) | \(9/25\) | \(5/4\) |

Exact γ:

\[
\begin{align*}
\gamma_1 &= 1,\\
\gamma_2 &= \sqrt{225/224} = 15/(4\sqrt{14}),\\
\gamma_3 &= \sqrt{25/24} = 5/(2\sqrt{6}),\\
\gamma_4 &= \sqrt{225/209} = 15/\sqrt{209},\\
\gamma_5 &= \sqrt{25/21} = 5/\sqrt{21},\\
\gamma_6 &= 5/4.
\end{align*}
\]

Numerical:

\[
\beta = (0,\;0.0\overline{6},\;0.2,\;0.2\overline{6},\;0.4,\;0.6),
\qquad
\gamma \approx (1,\;1.00223,\;1.02062,\;1.03757,\;1.09109,\;1.25000).
\]

### 3.1 Three future + three past

Lowest three exponents \(\{11,13,17\}\): future-oriented domains.  
Highest three \(\{19,23,29\}\): past-oriented domains.

The cut sits between the dual pair \((17,19)\). Top′ at \(m=23\) is the moving dual of the frozen Tav exponent \(7\); Beauty′ at \(m=29\) is the moving dual of the frozen radius exponent \(1\). Those two domains are the ones most tightly locked to clock and fibre size.

### 3.2 Dark-to-baryon ratio from the frame

Equal intrinsic densities (leading geometric ansatz):

\[
\frac{\Omega_{\rm DM}}{\Omega_b}
=
\sum_{i=2}^{6}\gamma_i
=
\sqrt{\frac{225}{224}}
+\sqrt{\frac{25}{24}}
+\sqrt{\frac{225}{209}}
+\sqrt{\frac{25}{21}}
+\frac{5}{4}
\approx
5.4015.
\]

Observed \(\Omega_{\rm DM}/\Omega_b\approx 5.2\) sits inside a few percent. The residual is not a free parameter to dial: it is the correction from (i) the Yukawa factor \(e^{-s_i/\lambda_{m_0}}\) of the kernel, which slightly suppresses the fastest domains, and (ii) the fact that intrinsic \(\rho_i\) need not be exactly equal once Mirron occupancy of each eigenplane is counted. The leading term is already geometric and in the right place.

### 3.3 Variable key (velocities)

| Symbol | Meaning |
|---|---|
| \(c\) | Coxeter element of \(W(E_8)\) |
| \(m_i\) | Coxeter exponent of domain \(D_i\) |
| \(h^\vee=30\) | dual Coxeter number; tick denominator |
| \(\beta_i\) | \(V_{\rm orb}^{(i)}/c = (m_i-11)/30\) |
| \(\gamma_i\) | Lorentz factor of \(D_i\) in the Prime chart |
| \(V_{\rm orb}^{(i)}\) | \(\beta_i c\) |

The kernel of the previous session is now fully numeric in the \(V_{\rm orb}\) sector: substitute the six \(\beta_i\) above, keep the real \(\lambda_{m_0}=\hbar/(m_0 c)\).

---

## 4. The Tav circle

### 4.1 What it is

The physical container is the 5D Einstein–Kaluza–Klein manifold

\[
\mathcal{M}_5
=
\mathbb{R}^3\times S^1_\tau,
\qquad
\tau
=
7\,h^{-1}\,\mathrm{Mpc}.
\]

Here \(\tau\) is the *radius* of the compact fifth dimension (Gatlin / TSB convention). It is the IR partner of the microscopic Compton length \(\ell_C\): same conformal binding, opposite end of the Mirron hierarchy.

The integer \(7\) is not fitted to large-scale structure. It is the Coxeter exponent that was frozen to make this circle exist inside E₈. The same integer appears as:

- the order of the Fano plane / imaginary octonions,
- the period of the decimal \(1/7=0.\overline{142857}\),
- the affine mark pattern of E₈ (the extra node of \(\tilde E_8\)),
- the measured correlation length of the cosmic web.

### 4.2 Metric and KK tower

Write the fifth coordinate as \(\psi\in[0,2\pi)\), so the physical radius is \(\tau\) and the proper circumference is \(2\pi\tau\). The 5D line element in the vacuum sector is

\[
ds_5^2
=
g_{\mu\nu}(x)\,dx^\mu dx^\nu
+
\tau^2\bigl(d\psi + A_\mu dx^\mu\bigr)^2.
\]

Fourier modes on the circle:

\[
\Phi(x,\psi)
=
\sum_{n\in\mathbb{Z}}
\Phi_n(x)\,e^{in\psi}.
\]

The 4D mass of mode \(n\) (before conformal dressing) is

\[
m_n
=
\frac{|n|}{\tau}
\qquad\text{(natural units }c=\hbar=1\text{)}.
\]

The fundamental comoving wavenumber of the spatial comb is

\[
k_\tau
=
\frac{1}{\tau}
=
\frac{1}{7}\,h\,\mathrm{Mpc}^{-1}
=
0.\overline{142857}\,h\,\mathrm{Mpc}^{-1}.
\]

That bar is the same \(142857\) cycle. Euclid / Rubin targeting of a KK comb in \([6.991,\,7.027]\,h^{-1}\,\mathrm{Mpc}\) is a direct hit on this \(k_\tau\).

### 4.3 Casimir energy: why \(w\equiv -1\)

A massless 5D field on \(\mathbb{R}^3\times S^1_\tau\) produces a 4D vacuum energy by dimensional reduction. After ζ-regularization the finite piece scales as

\[
\rho_{\rm Casimir}
=
-
\frac{C}{\tau^4},
\]

where \(C\) is a pure number built from \(\zeta(-3)=1/120\) (bosonic vector / graviton tower; fermions enter with opposite sign and the TSB matter content is the six-domain + clockwork projection). Because \(\tau\) is a fixed geometric radius, \(\rho_{\rm Casimir}\) is a constant in cosmic time. A constant energy density with no preferred 3-velocity is a cosmological-constant fluid:

\[
w
=
\frac{p}{\rho}
=
-1.
\]

This is the TSB dark-energy sector. It is not a scalar field rolling on a potential. The *dynamical* weakening reported by DESI is not this Casimir piece; it is the centrifugal term of the six-domain supersphere as the Coxeter clock walks the moving exponents (previous rotational-decay note). Baseline \(w=-1\) from the circle; slow drift from the six \(\beta_i\).

### 4.4 142857 and the 8-phase clock

Decimal structure:

\[
\frac{1}{7}
=
0.\overline{142857},
\qquad
142857\times 7
=
999999.
\]

Cyclic multiples:

\[
\begin{align*}
1\times 142857 &= 142857,\\
2\times 142857 &= 285714,\\
3\times 142857 &= 428571,\\
4\times 142857 &= 571428,\\
5\times 142857 &= 714285,\\
6\times 142857 &= 857142.
\end{align*}
\]

These six cyclic permutations are the six domain phase-locks on the Tav circle. They are not an extra input: six domains, six residues of \(\mathbb{Z}/7\mathbb{Z}^\times\).

The octonionic clock has *eight* phases (Cl(8) fibre, including the real unit). The Tav circle has *seven* ticks. They close after

\[
\mathrm{lcm}(7,8)=56
\]

fundamental ticks, which is two Coxeter periods (\(2\times 30=60\)) minus a four-step Mirron refresh. The 8-phase fibre is the local Planck–Kerr / Mirron engine; the 7-fold circle is the global compact fifth dimension. They meet at the frozen exponent \(7\).

### 4.5 Domain phases on the circle

Let \(\varphi\in[0,2\pi)\) be the Tav angle. The kernel’s spectral twin from the previous session now has explicit locks:

\[
\varphi_i
=
\frac{2\pi\,m_i}{7}
\pmod{2\pi},
\qquad
m_i\in\{11,13,17,19,23,29\}.
\]

Reduce mod 7:

\[
\begin{align*}
11 &\equiv 4,\\
13 &\equiv 6,\\
17 &\equiv 3,\\
19 &\equiv 5,\\
23 &\equiv 2,\\
29 &\equiv 1.
\end{align*}
\]

The six residues are exactly \(\{1,2,3,4,5,6\}=\mathbb{Z}/7\mathbb{Z}^\times\). Prime (\(m=11\equiv 4\)) sits on residue \(4\), which is the midpoint of the multiplicative group. No domain sits on residue \(0\) — that slot *is* the circle itself (the frozen exponent \(7\equiv 0 \pmod{7}\)).

So the Tav circle is the missing seventh residue, and the six domains occupy every nonzero class. That is the occupancy theorem of this frame.

### 4.6 Phase velocity vs orbital velocity

Internal orbital motion on \(S^3_{\rm int}\) and winding on \(S^1_\tau\) are not the same circle, but they share the Coxeter clock. The map is

\[
\Omega_i^{\rm Tav}
=
\frac{V_{\rm orb}^{(i)}}{R_{\rm int}}
\cdot
\frac{\tau}{R_{\rm int}}
=
\beta_i\,\frac{c\tau}{R_{\rm int}^2}.
\]

The dimensionless ratio \(c\tau/R_{\rm int}^2\) is a single overall clock rate, common to all six domains. Relative Tav angular speeds therefore stand in the same ratios as the \(\beta_i\):

\[
\Omega_i^{\rm Tav}
:
\Omega_j^{\rm Tav}
=
\beta_i:\beta_j
=
0 : \tfrac{1}{15} : \tfrac{1}{5} : \tfrac{4}{15} : \tfrac{2}{5} : \tfrac{3}{5}.
\]

### 4.7 Conformal exhaustion at \(\tau\)

Local conformal binding of a preonic BEC (Mirron condensate) is the kernel \(K\) with UV scale \(\ell_C\). The same operator, lifted up the 7-fold Mirron hierarchy, exhausts when the support of \(K\) reaches one Tav radius. Past that radius the fifth dimension is “empty \(S^1\)” from the 4D point of view: correlation functions drop, filaments thin, voids open. That is the 7 \(h^{-1}\) Mpc web scale as a theorem of the kernel plus this circle, not as a fitted \(r_0\).

### 4.8 Variable key (Tav circle)

| Symbol | Meaning |
|---|---|
| \(\tau\) | radius of the compact fifth dimension, \(7\,h^{-1}\,\mathrm{Mpc}\) |
| \(\psi\) | angular coordinate on \(S^1_\tau\), period \(2\pi\) |
| \(A_\mu\) | KK graviphoton |
| \(n\) | KK mode index |
| \(m_n=\|n\|/\tau\) | 4D KK mass of mode \(n\) |
| \(k_\tau=1/\tau\) | fundamental spatial comb, \(0.\overline{142857}\,h\,\mathrm{Mpc}^{-1}\) |
| \(\rho_{\rm Casimir}\) | 4D vacuum energy from the circle, \(\propto -1/\tau^4\) |
| \(w\) | equation-of-state parameter; Casimir piece has \(w=-1\) |
| \(\varphi_i\) | Tav phase lock of domain \(D_i\) |
| \(\Omega_i^{\rm Tav}\) | angular speed of \(D_i\) on the Tav circle |
| \(142857\) | repeating block of \(1/7\); six cyclic permutations = six domains |
| residue \(0\bmod 7\) | the circle itself; unoccupied by domains |

---

## 5. How the kernel sits on the circle

Previous session:

\[
K(\mathbf{x},\mathbf{x}';\{V_{\rm orb}^{(i)}\},\lambda_{m_0})
=
\sum_{i=1}^{6}
\frac{\gamma_i}{T_i}
\int_0^{T_i}
\frac{e^{-s_i/\lambda_{m_0}}}{4\pi s_i}\,dt.
\]

Now every symbol on the right is fixed:

- six \(\beta_i\) (hence \(V_{\rm orb}^{(i)}\), \(\gamma_i\), \(T_i=2\pi R_{\rm int}/V_{\rm orb}^{(i)}\)) from the Coxeter freeze,
- \(\lambda_{m_0}=\hbar/(m_0 c)\) real,
- spectral twin on the circle:

\[
K
\;\longleftrightarrow\;
\sum_{i=1}^{6}
\gamma_i\,
e^{-k\lambda_{m_0}}\,
W_6\!\bigl(\varphi-\tfrac{2\pi m_i}{7}\bigr),
\]

with \(\{m_i\bmod 7\}=\{1,2,3,4,5,6\}\) and \(W_6\) the Weight-6 Vălean kernel.

IR scale of that spectral sum is \(\tau_{\rm web}\). UV Compton in the Yukawa factor is \(\lambda_{m_0}\). Unoccupied residue \(0\) is a phase class \(\varphi\sim\varphi+2\pi\), not a metric circle and not the IR pole of \(K\). Two-pole reading: working hypothesis only.

---

## 6. Falsifiable numbers locked by this frame

1. Catalogue IR scale: a preferred length outside the listed window around \(7\,h^{-1}\,\mathrm{Mpc}\) stresses \(\tau_{\rm web}\) as a kernel scale. That does not by itself kill Coxeter exponent 7. Two sentences.
2. \(\sum_{i=2}^{6}\gamma_i\approx 5.4015\) before Yukawa suppression. If SPARC / Planck baryon-to-shadow ratios demand a leading term far from \(5.4\) after the kernel is applied, the equal-density ansatz (not the clock frame) is first to move.
3. Six-fold photon-ring modulation at EHT: prediction, not trophy.
4. Phase-echo in entangled \(B^0\bar B^0\) at LHCb / Belle II at \(\mathrm{lcm}(7,8)=56\): prediction, not trophy.
5. DESI drift as centrifugal walk of \(\{\beta_i\}\): prediction, not trophy. Baseline \(w=-1\) is not re-derived here from a metric \(S^1\).

---

## 7. What was not free

| Item | Status after this session |
|---|---|
| E₈ coordinate realization | even frame, simple roots listed |
| Which two planes are frozen | exponents \(1\) and \(7\) |
| Which six exponents move | \(11,13,17,19,23,29\) |
| \(\beta_i\) formula | \((m_i-11)/30\) |
| Six explicit \(\beta_i\) | \(0,1/15,1/5,4/15,2/5,3/5\) |
| Six explicit \(\gamma_i\) | table above, all radicals |
| Tav radius | \(\tau=7\,h^{-1}\,\mathrm{Mpc}\) (the frozen exponent, in Mpc/\(h\)) |
| Domain residues on \(S^1_\tau\) | \(\mathbb{Z}/7\mathbb{Z}^\times\), Prime at \(4\) |
| \(\ell_C\) | still \(\hbar/(m_0 c)\), \(m_0=313.1\,\mathrm{MeV}\) |

The remaining unfixed geometric quantity in the kernel is the internal radius \(R_{\rm int}\) of \(S^3_{\rm int}\), which sets the overall clock rate \(T_i\) but cancels from every dimensionless ratio (\(\beta_i\), \(\gamma_i\), \(\Omega_i/\Omega_j\), \(\Omega_{\rm DM}/\Omega_b\)).

---

## 8. Session metadata

- Written: 2026-09-19
- Files:
  - `Personal_Files/TSB_E8_Cartan_frame_and_Tav_circle_2026-09-19.md`
  - previous: `Personal_Files/TSB_Kernel_Six_Vorb_real_ellC_2026-09-19.md`
- Request served: fix E₈ Cartan frame; explore the Tav circle
