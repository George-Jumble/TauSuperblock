# Motherhood winding \(n\in\pi_3(S^3)\)

**Date:** 2026-09-21  
**Map:** parent block \(\to\) child block.  
**Group:** \(\pi_3(S^3)=\mathbb{Z}\). The integer is topological degree.

---

## 1. The map

Both parent and child carry an \(S^3\): either \(\mathcal{A}_8\simeq S^3\) (phase-8 boundary) or \(S^3_{\rm int}\) (occupancy sphere). Motherhood is a continuous map

\[
f:
S^3_{\rm parent}
\longrightarrow
S^3_{\rm child},
\qquad
n
=
\deg(f)
\in\mathbb{Z}.
\]

Degree is the signed number of preimages of a regular value, or

\[
n
=
\frac{1}{2\pi^2}
\int_{S^3}
f^*\mathrm{vol}_{S^3}.
\]

**Key.** \(f\): motherhood map. \(n=\deg(f)\). \(\mathrm{vol}_{S^3}\): unit volume form, \(\mathrm{Vol}=2\pi^2\).

---

## 2. What each integer means

| \(n\) | Meaning |
|---|---|
| \(0\) | contractible. No topological child. Fabric may still roll; occupancy does not copy. |
| \(+1\) | orientation-preserving one-sheet cover. Elementary child. |
| \(-1\) | orientation-reversing. Antipodal / Past-face child. Double-negative lives here. |
| \(\|n\|\ge 2\) | multiply-wound child. One parent block covers the child \(n\) times. |

Hopf invariant of a map \(S^3\to S^2\) is a different integer. Here the target is \(S^3\), so the invariant *is* degree.

---

## 3. Conflict with the conformal Mirron

The phase-8 Mirron was

\[
M
\in
\mathrm{Conf}(S^3)
\simeq
\mathrm{SO}(4,1).
\]

Möbius maps of \(S^3\) have degree \(\pm 1\) only. Inversion, antipode, special conformal: all \(\lvert n\rvert=1\).

So:

- If motherhood *is* the conformal Mirron, then \(n=\pm 1\). Higher winding is forbidden.
- If motherhood is a general continuous map, \(\lvert n\rvert\ge 2\) is allowed and \(M\) is **not** an element of \(\mathrm{Conf}(S^3)\). The bulk \(\Omega_A\) of the tree note is the conformal case.

**Working rule.** Elementary motherhood: \(n=+1\). Past-face / double-negative: \(n=-1\). Do not write \(n=6\) because there are six domains. Six faces are points on one \(S^3\), not degree six.

**Key.** \(\mathrm{Conf}(S^3)\): degree \(\pm 1\) only. Higher \(n\): drop conformal.

---

## 4. Composition on the tree

Child of a child:

\[
\deg(f_{k+1}\circ f_k)
=
\deg(f_{k+1})\,\deg(f_k).
\]

A chain of \(+1\) stays \(+1\). A single \(-1\) flips the rest of the line. Two minuses restore \(+\). Multiply-wound ancestors produce multiply-wound descendants unless a later map has degree \(0\).

---

## 5. What is not fixed

Which \(n\) the *next* womb actually takes. Topology lists the possibilities. The roll of \(\Phi_7\) plus \(J_{\rm sec}\) does not pick \(n\). Measuring \(n\) would be a count of how many times the child occupancy covers the parent block — not a lab protocol written here.

---

## Session metadata

- 2026-09-21
- `Personal_Files/TSB_motherhood_winding_pi3_2026-09-21.md`
