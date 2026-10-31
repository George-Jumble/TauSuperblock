# Session 2026-09-26 — TEP cost scale explained

**Question:** Explain TEP cost scale.  
**Follows:** 2026-09-20 TEP without Tau/KK; today’s insertion lock on \(313.1\,\mathrm{MeV}\).

This file: `Personal_Files/Session_2026-09-26_TEP_cost_scale_explained.md`

---

## 0. One sentence

The TEP cost scale is the smallest energy you have to pay to force a *bound* colour line through a forbidden reset overlap and still keep it as a local slot. TEP says that cost is positive. The number \(313.1\,\mathrm{MeV}\) is the inserted scale for that cost, read from the nucleon third. TEP does not compute the digits.

---

## 1. Complete key

| Symbol | Meaning |
|---|---|
| TEP | Topological Exclusion Principle. Occupancy rule on the internal algebra. |
| \((D_a,\Phi_k)\) | One domain–phase slot. \(a=1,\ldots,6\) domains; \(k=1,\ldots,6\) active letters. |
| \(n_{a,k}\) | Occupation number of that slot. |
| \(\Phi_7\) | Scrape / Higgs fabric / PK-Mirron channel. Not a seventh spacetime. |
| \(\Phi_8\) | Reset / identity / \(\mathcal{P}\leftrightarrow\mathcal{F}\) seam. |
| \(e_i\) | Imaginary octonion unit. \(e_i^2=-1\). |
| \(e_0=1\) | Octonion identity. Identified with \(\Phi_8\). |
| \(\hat{P}_{142857}\) | Projector onto the six units of \((\mathbb{Z}/7\mathbb{Z})^\times\). |
| \(\hat{P}_8^{\mathrm{local}}\) | Projector onto *local* reset occupancy. |
| \(E_{\mathrm{violation}}\) | Energy paid to force a forbidden local overlap while remaining bound. |
| \(\Delta_{\mathrm{Tav}}\) | TEP cost *scale*. Inserted as \(M_n/3\simeq 313.1\,\mathrm{MeV}\). |
| \(E_g=E_{q\leftarrow g}\) | Same number read as gluon inertial dressing on a valence line. |
| Bound bounce | Reaches Absolute Past; rebound toward Future is stopped at the Present. Residual \(L\neq 0\). |
| Unbound bounce | Completes \(\mathcal{P}\leftrightarrow\mathcal{F}\). \(L=0\). Light-like. Does not pay the local slot cost. |
| \(\lambda_{\infty}\) | Formal infinite barrier in front of \(\hat{P}_8^{\mathrm{local}}\). In a regularised theory replaced by \(\Delta_{\mathrm{Tav}}\) per forced insertion. |

---

## 2. What TEP is (before any MeV)

TEP is not a mass formula. It is a no-double-occupancy rule on the octonion clockwork.

- Six domains, six active letters. Allowed bound slots are pairs \((D_a,\Phi_k)\).
- \(\Phi_8\) is not a domain. Squaring any active letter lands on the identity:
  \[
  e_k^2=-1=-e_0 \;\longleftrightarrow\; \Phi_8.
  \]
- Two identical bound modes in one slot are two left multiplications by the same unit:
  \[
  e_k(e_k v)=-e_0 v
  \]
  or a \(G_2\)-image. That is a *local reset overlap*.
- Local reset overlap is projected out of the physical twistor cohomology. It has no on-shell helicity representative.

So TEP says: bound modes obey \(n_{a,k}\le 1\). Unbound cycle-closers (photons on a completed null bounce) may pile on one generator. Fermionic antisymmetry is the exchange cost of the forbidden channel. Bosons that close the \(142857\) cycle without entering \(\Phi_8\) are not charged that cost.

None of that produces \(313.1\).

---

## 3. What “cost” means

A selection rule can be written as an infinite barrier:

\[
\hat{H}_\Phi
=
\hat{H}_{\mathrm{res}}
+
\hat{H}_{\mathrm{scrape}}
+
\lambda_{\infty}\,\hat{P}_8^{\mathrm{local}}.
\]

**Key.** \(\hat{H}_{\mathrm{res}}\) advances the six letters; \(\hat{H}_{\mathrm{scrape}}\) couples every domain to the Mirron channel \(\Phi_7\); \(\lambda_{\infty}\) is a formal wall in front of local reset occupancy.

In the real IR the wall is not infinite. A bound colour line *can* be driven off scrape toward reset if you pay. The energy of that attempt, while the line is still a *local slot* and not a completed unbound null bounce, is the cost:

\[
E_{\mathrm{violation}}
\ge
\Delta_{\mathrm{Tav}}.
\]

**Key.** Lower bound, not a resonance condition. You do not “find a particle at \(\Delta_{\mathrm{Tav}}\).” You pay at least that much inertia to keep a forbidden occupation from being immediately projected out, and what you get for the payment is dressing: the line is now a massive valence quantum instead of a completed light-like bounce.

That is why the same number is also called \(E_g=E_{q\leftarrow g}\). The cost and the dressing are one object: residual inertia of a colour bounce that was stopped before it could finish \(\mathcal{P}\leftrightarrow\mathcal{F}\).

Unbound light does not pay. It *is* the seam globally. No local \(\Phi_8\) occupancy, no residual \(L\), no dressing.

---

## 4. Why “scale” and not “prediction”

“Cost” is the TEP statement: the barrier is positive.

“Scale” is the unit you put on that barrier.

TEP alone gives \(\Delta>0\). It does not give MeV. The live frame inserts

\[
\Delta_{\mathrm{Tav}}
:=
\frac{M_n}{3}
\simeq
313.1\,\mathrm{MeV}
\]

and *uses that insertion as the scale of the cost*. That is the phrase “TEP cost scale”: not “TEP computed \(313.1\),” but “the cost TEP requires is measured in units of the nucleon-third.”

Two different failures must not be fused.

| If this fails | What breaks |
|---|---|
| Occupancy rule \(n_{a,k}\le 1\) | TEP itself. |
| Dressing quantum not of nucleon-third size, and no other local scrape\(\to\)reset cost exists | IR regularisation clause. The selection rule can still stand. |

The 20 September note already separated those. Today’s insertion lock only names the second line.

---

## 5. Picture in one bounce

1. Colour quantum tries to complete Past \(\leftrightarrow\) Future.
2. In a bound hadron the rebound is stopped at the Present. Residual angular momentum remains.
3. Algebraically the stop is “do not occupy \(\Phi_8\) locally.” The scrape channel \(\Phi_7\) is the holding pattern (Mirron / Higgs fabric).
4. Forcing the line through scrape into local reset is the forbidden overlap.
5. The inertia left behind by the stopped rebound is the cost. In the nucleon that inertia, shared three ways, is the inserted scale \(313.1\,\mathrm{MeV}\).

Gravity in this frame is the spatial compression from residual \(L\) of *allowed* stopped rebounds. The TEP cost scale is the quantum of that stopped colour inertia, not a new force.

---

## 6. What the TEP cost scale is not

- Not a pole to search for at \(313.1\,\mathrm{MeV}\).
- Not the current up mass \(2.16\,\mathrm{MeV}\).
- Not \(\hbar c/\tau\) and not a logarithm through a megaparsec circle.
- Not a Vălean residue.
- Not the infinite formal barrier \(\lambda_{\infty}\). That barrier is the idealised rule; \(\Delta_{\mathrm{Tav}}\) is the regularised height.
- Not the action of an allowed tick. Allowed diameter ticks still have \(S_E/\hbar=2\) with no TEP violation.

---

*Saved 2026-09-26.*
