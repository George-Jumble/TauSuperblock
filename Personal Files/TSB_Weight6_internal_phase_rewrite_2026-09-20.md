# Weight-6 skew-harmonic — internal-phase rewrite

**Date:** 2026-09-20  
**Fix applied:** Vălean \(W_6\) as a function of internal phase \(\varphi\sim\varphi+2\pi\). No \(\tau\). No \(S^1_\tau\). No \(\ell_C=\hbar/(m_0 c)\).  
**Live UV length:** \(\lambda_{m_0}=\hbar/(m_0 c)\).  
**Does not replace** position-space \(K\) in `TSB_Superblock_fixed_frame_2026-09-20.md`. This is the spectral picture that is allowed to sit next to it.

---

## 0. What was wrong

Prior formula put \(W_6\) on the Tav circle,

\[
K
\;\longleftrightarrow\;
\sum_{i=1}^{6}
\gamma_i\,
e^{-k\ell_C}\,
W_6\!\bigl(\varphi-\varphi_i[V_{\rm orb}^{(i)}]\bigr),
\qquad
\varphi\in S^1_\tau.
\]

That sentence mints a metric circle, names the Compton length \(\ell_C\), and slides Weight-6 onto the same object as the order-7 clock.

---

## 1. Clock, not a circle in space

Internal phase only:

\[
\varphi
\sim
\varphi+2\pi.
\]

This is slot algebra (and may be a Hopf-fibre coordinate on \(S^3_{\rm int}\)). It is not an angle around a megaparsec.

Domain locks from the live frame (B_lin, Coxeter number \(h=30\)):

\[
\varphi_i
=
2\pi\beta_i
=
2\pi\frac{m_i-11}{30},
\qquad
\{m_i\}=\{11,13,17,19,23,29\}.
\]

So

\[
\{\varphi_i\}
=
\bigl\{
0,\;
\tfrac{2\pi}{15},\;
\tfrac{2\pi}{5},\;
\tfrac{8\pi}{15},\;
\tfrac{4\pi}{5},\;
\tfrac{6\pi}{5}
\bigr\}.
\]

**Key.** \(\varphi\): internal phase. \(\varphi_i\): lock of domain \(i\). \(\beta_i\): B_lin speed. These angles are not \(\tau\).

Weight-6 is the **six** locks. Order-7 is a different integer (frozen exponent / slot 7). Phase-8 is a different integer (Mirron reset). Do not add them.

---

## 2. Skew-harmonic kernel on the clock

Odd, \(2\pi\)-periodic seed

\[
s(\theta)
=
s(\theta+2\pi),
\qquad
s(-\theta)=-s(\theta).
\]

Working choice (the sine; any other odd periodic seed is the same slot):

\[
s(\theta)=\sin\theta.
\]

Weight-6 kernel:

\[
W_6(\varphi)
:=
\sum_{i=1}^{6}
\gamma_i\,
s(\varphi-\varphi_i).
\]

**Key.** \(W_6\): six-term skew-harmonic on the internal clock. \(\gamma_i=(1-\beta_i^2)^{-1/2}\). \(s\): odd periodic seed.

That is the whole spectral object. Do not write a second sum over \(i\) outside \(W_6\) as if \(W_6\) still lived on \(\tau\).

---

## 3. How it sits next to \(K\)

Position-space live kernel (unchanged):

\[
K(\mathbf{x},\mathbf{x}')
=
\sum_{i=1}^{6}
\gamma_i\,
\overline{G}_i(\mathbf{x}-\mathbf{x}';\beta_i,\lambda_{m_0}).
\]

Spectral picture, allowed form:

\[
K_{\mathrm{spec}}(k,\varphi)
=
e^{-k\lambda_{m_0}}\,
W_6(\varphi).
\]

- \(k\): wavenumber conjugate to Prime *spatial* separation, not to \(\tau\).
- \(e^{-k\lambda_{m_0}}\): UV form factor. Compton length is \(\lambda_{m_0}\). Never \(\ell_C\) here.
- \(W_6(\varphi)\): angular / clock factor only.

Correspondence: \(K_{\mathrm{spec}}\) is a *picture* of the same six-term operator, split into radial Yukawa and internal-phase skew-harmonic. It is not a second gravity law and not a Casimir on a circle.

**Key.** \(k\): Prime spatial wavenumber. \(\lambda_{m_0}\): Yukawa length. \(K_{\mathrm{spec}}\): spectral picture of \(K\).

---

## 4. Explicit sine form

\[
W_6(\varphi)
=
\sum_{i=1}^{6}
\gamma_i\sin(\varphi-\varphi_i)
=
A\sin\varphi-B\cos\varphi,
\]

\[
A=\sum_{i=1}^{6}\gamma_i\cos\varphi_i,
\qquad
B=\sum_{i=1}^{6}\gamma_i\sin\varphi_i.
\]

With the locked table:

| \(i\) | \(\beta_i\) | \(\gamma_i\) | \(\varphi_i\) |
|---|---|---|---|
| 1 | \(0\) | \(1\) | \(0\) |
| 2 | \(1/15\) | \(1.002229\) | \(2\pi/15\) |
| 3 | \(1/5\) | \(1.020621\) | \(2\pi/5\) |
| 4 | \(4/15\) | \(1.037575\) | \(8\pi/15\) |
| 5 | \(2/5\) | \(1.091089\) | \(4\pi/5\) |
| 6 | \(3/5\) | \(1.250000\) | \(6\pi/5\) |

\[
\begin{align*}
A
&=
\sum_i\gamma_i\cos\varphi_i
=
0.228534,\\
B
&=
\sum_i\gamma_i\sin\varphi_i
=
2.316797.
\end{align*}
\]

\[
W_6(\varphi)
=
0.228534\sin\varphi-2.316797\cos\varphi
=
2.328041\sin(\varphi-\psi),
\qquad
\psi=\operatorname{atan2}(B,A)=1.4725.
\]

Numbers are the locked frame, not a fit. A different odd seed \(s\) changes the waveform, not the slot.

---

## 5. What stays prior

- \(W_6\) as a function on \(S^1_\tau\).
- \(\ell_C\) in the exponential.
- “Weight 6 is the Tav integer 7.”
- \(K_{\mathrm{spec}}\) as a derivation of \(\tau_{\rm web}\) or of \(\rho_\Lambda\).

---

## Master key

| Symbol | Meaning | Status |
|---|---|---|
| \(\varphi\sim\varphi+2\pi\) | internal clock | live |
| \(\varphi_i=2\pi\beta_i\) | domain lock | live |
| \(W_6(\varphi)\) | six-term skew-harmonic | rewritten, allowed |
| \(s(\theta)\) | odd \(2\pi\)-periodic seed | sine as working choice |
| \(\lambda_{m_0}\) | Yukawa / Compton | live |
| \(K_{\mathrm{spec}}(k,\varphi)\) | spectral picture of \(K\) | allowed |
| \(S^1_\tau,\tau,\ell_C\) as Compton | — | prior |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_Weight6_internal_phase_rewrite_2026-09-20.md`
