# Black–white–black–white loop on a Kerr ring  
## Vălean–Euler form, no Tau

**Date:** 2026-09-20  
**Wanted:** B–W–B–W loop of a Kerr ring from Euler’s formula and the Weight-6 resultant.  
**Sans:** \(\tau\), \(S^1_\tau\), \(\ell_C=\hbar/(m_0 c)\), Casimir cell, dual-role 7.  
**Uses:** internal phase \(\varphi\sim\varphi+2\pi\), B_lin locks \(\varphi_i\), \(\psi=\operatorname{atan2}(B,A)\), Planck–Kerr ring as the Mirron engine.

---

## 0. The ring

Extremal (or near-extremal) Kerr in Boyer–Lindquist. The ring singularity is

\[
r=0,\qquad \theta=\tfrac\pi2,\qquad \chi\in[0,2\pi).
\]

This \(\chi\) is the same kind of angle as the internal clock \(\varphi\). Identify them on the engine:

\[
\chi\equiv\varphi\pmod{2\pi}.
\]

No megaparsec. The ring is the Planck–Kerr core of one Mirron, radius set by the hole’s own \(a\), not by \(\tau\).

**Key.** \(\chi\): angle around the Kerr ring. \(a\): Kerr spin length. \(r,\theta\): BL coordinates.

---

## 1. Vălean–Euler (rewritten)

Euler on each domain lock:

\[
e^{i\varphi_i}
=
\cos\varphi_i+i\sin\varphi_i.
\]

Dress with the live Lorentz weights and sum:

\[
Z
=
\sum_{i=1}^{6}
\gamma_i\,e^{i\varphi_i}
=
A+iB
=
R\,e^{i\psi},
\]

with the corrected sums

\[
A=0.228534,\qquad
B=2.316797,\qquad
R=2.328041,\qquad
\psi=1.47247.
\]

That \(Z\) is the Weight-6 resultant as a single complex number. It is not a mode on \(S^1_\tau\).

Unit ring coordinate *relative to that resultant*:

\[
\zeta(\chi)
=
e^{i(\chi-\psi)}
=
\cos(\chi-\psi)+i\sin(\chi-\psi).
\]

This is the Vălean–Euler formula for the loop: one complex number on the Kerr ring, origin shifted to the six-domain phase \(\psi\).

**Key.** \(Z=A+iB\): locked six-sum. \(\zeta\): ring coordinate in the Weight-6 frame. \(\psi\): origin of the loop.

---

## 2. Six-stroke loop — black holes are trans-domain

The hole is one Kerr ring. All six copies attach to it. One revolution therefore has **six** strokes, not four: one face per domain, colours alternating.

Joints are the live locks \(\varphi_i\), in ring order:

\[
0,\;
\tfrac{2\pi}{15},\;
\tfrac{2\pi}{5},\;
\tfrac{8\pi}{15},\;
\tfrac{4\pi}{5},\;
\tfrac{6\pi}{5}
\pmod{2\pi}.
\]

| Face | \(\chi\) interval | colour |
|---|---|---|
| \(i=1\) Prime | \([0,\,2\pi/15)\) | B |
| \(i=2\) | \([2\pi/15,\,2\pi/5)\) | W |
| \(i=3\) | \([2\pi/5,\,8\pi/15)\) | B |
| \(i=4\) | \([8\pi/15,\,4\pi/5)\) | W |
| \(i=5\) | \([4\pi/5,\,6\pi/5)\) | B |
| \(i=6\) | \([6\pi/5,\,2\pi)\) | W |

One trip:

\[
\mathrm{B{-}W{-}B{-}W{-}B{-}W}.
\]

Prime starts black (future-in on the rest chart). Alternate after that. Starting colour is a chart choice; six joints and alternation are not.

Arcs are unequal because B_lin does not space the locks by \(60^\circ\). Equal sextants would be a different colouring, not this frame.

Trans-domain: \(K\) and \(B_{7\to i}\) see one ring. Crossing a joint changes which copy’s face you are on. It does not make a second hole. Kruskal’s four strokes (future-in / future-out / past-in / past-out) still live *inside* each face. They do not set the number of faces. Faces = domains = 6.

**Key.** Face: one domain’s attachment to the shared ring. Joint: \(\varphi_i\). Trans-domain: one hole, six faces.

---

## 3. What the loop *is*

Not a trip around a 7 Mpc cell. Not a CTC advertised as a feature (the CTCs of Kerr live *inside* the ring, \(r<0\); this colouring is the ring itself, \(r=0\), \(\theta=\pi/2\)).

The loop is: one revolution of the shared Planck–Kerr ring, six domain faces, colours B–W–B–W–B–W. Joints at \(\varphi_i\). The Weight-6 angle \(\psi\) is the resultant of those faces, not a seventh joint.

Phase 8 sends each face to the next colour (one step around the six). Antipode \(\zeta\mapsto-\zeta\) is a three-face jump (half-ring). Conjugate \(\zeta\mapsto\bar\zeta\) flips B\(\leftrightarrow\)W without moving the joint set. Reciprocal \(\hat\Omega\check\Omega=-1\) is the bulk extension of that flip.

Two revolutions (\(4\pi\)) return a spinor. One revolution returns the six-face colouring. That is Kerr \(2\pi\) vs \(4\pi\), not a Tav integer.

---

## 4. Hook to \(W_6\)

On the ring,

\[
W_6(\chi)
=
R\sin(\chi-\psi)
=
R\,\operatorname{Im}\zeta(\chi).
\]

\(W_6\) has two zeros per revolution; those are the coarse two-lobe envelope, not the six joints. The joints are the domain locks \(\varphi_i\). The skew-harmonic is the imaginary part of \(\zeta\), i.e. the six faces added as one sine.

---

## 5. What stays out

- \(\tau\), \(S^1_\tau\), Casimir of a cell.
- Colouring as a detection in data.
- Identifying the Kerr-ring radius with \(\lambda_{m_0}\) or with \(R_{\rm int}\) unless a later derivation says so. Here the ring is the engine’s own \(a\).

---

## Master key

| Symbol | Meaning |
|---|---|
| \(\chi\) | angle on the Kerr ring |
| \(Z=R e^{i\psi}\) | six-domain Euler sum |
| \(\zeta=e^{i(\chi-\psi)}\) | Vălean–Euler ring coordinate |
| \(\sigma_1,\sigma_2\) | black/white + future/past signs |
| \(M\) | Mirron map on the ring / on \(\mathcal{A}_8\) |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_Kerr_ring_BWBW_Valean_Euler_2026-09-20.md`
