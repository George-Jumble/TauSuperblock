# How to fix Superblock (Superblock portion only)

> **Superseded for live Superblock algebra (2026-09-20):** Use `TSB_Superblock_fixed_frame_2026-09-20.md`. That note applies F7, B_lin, demotes \(m_0\) to an IR floor, states the far-zone Poisson theorem, and strikes trophies. This file is prior if it conflicts.


**Date:** 2026-09-20  
**Rule:** Tau metric \(S^1\) stays archived. Locks stay in force. No trophies.

The theory is not repaired by another status update. It is repaired by cutting sentences that cannot be derived, and by closing the few derivations that Superblock actually needs.

---

## 0. Hygiene (do this first, before any new algebra)

- One manuscript, Superblock only. No 5D KK backend, no “Tav-first unification,” no JADES 8.1σ, no resonator.
- Every empirical line is either **prediction** or **in-house fit**. Never PASS, never detected, never 12σ.
- Strike: “zero parameters,” “Yang–Mills solved,” “strong-CP solved,” “fifth dimension,” “circle is the IR pole of \(K\).”
- Caption \(m_0\), \(\tau_{\rm web}\) (if mentioned at all), the freeze, and the \(\beta\) map as **floors or frame choices** until a derivation exists.
- CMS / LHCb / Planck FFT / ALICE / 56-tick: preregister the statistic *before* touching data. If the statistic was already mined, it cannot be a confirmation.

That alone removes items 1–5 and 17 from the failure list.

---

## 1. Decide what Superblock *is*

Write one paragraph that does not mention a compact fifth dimension:

> Six co-located \(3+1\)D domains on an internal \(S^3\). Their relative motions are eigenplanes of a Coxeter element of \(W(E_8)\). Gravity seen in Prime is a 4D average \(K\) of the six copies, UV-regularized by \(\lambda_{m_0}\). Dark matter is shadow gravity from the five hidden copies. Local refresh is Mirron (Planck–Kerr), 8-phase. Clock algebra is exponent 7 as phase \(\varphi\sim\varphi+2\pi\), not as a megaparsec.

If a sentence does not follow from that paragraph, it does not belong in the paper.

---

## 2. The four derivations that would actually fix it

These are the Superblock holes. Everything else is optional.

### D1. Why freeze \(\{1,7\}\)

Today it is a choice. Fix: give a group-theoretic reason that does not look at \(\tau_{\rm web}\) or at \(\Omega_{\mathrm{DM}}\).

Acceptable: a statement about which eigenplanes of \(\sigma(c)\) can be *isometric* (frozen) while leaving a Lorentzian 3+1 chart. Or: exponent 1 is the unique lowest, exponent 7 is the unique one that divides \(|W|\) and is not 1. Write the criterion first, then freeze.

If no criterion exists, keep the freeze and **call it a frame**.

### D2. The map \(m_i\mapsto\beta_i\)

\(\beta_i=(m_i-11)/30\) is one convention. Fix: derive \(\beta\) from the eigenvalue \(\mathrm{e}^{2\pi i m/h}\) and the internal metric on \(S^3\), or tabulate two or three maps and state the selection rule *without* using \(\sum\gamma\approx 5.2\).

If the map is chosen to make \(\sum\gamma\) near 5.2, that is a fit. Label it a fit.

### D3. \(m_0\) from Mirron only

Locks forbid deriving \(m_0\) from \(\tau\). Then Superblock must produce \(313.1\,\mathrm{MeV}\) from Planck–Kerr / Mirron geometry alone, with every symbol named, or it must stop calling \(m_0\) geometric.

Target: one closed note, no 7 Mpc, no 1/7 harmonic of a cell. If the calculation will not close, write

\[
m_0=313.1\,\mathrm{MeV}
\quad\text{(IR floor, not derived in this paper).}
\]

That is honest. Prize language stays out either way.

### D4. Kernel \(\to\) Poisson + cores

Write \(K\) with \(\lambda_{m_0}\) and the six locked \(\beta_i\). Prove, under stated assumptions, that the far-zone Prime equation is Poisson with \(G_{\mathrm{eff}}=\sum_i \gamma_i G_i\) or whatever the algebra gives. Prove that the near-zone Yukawa in \(\lambda_{m_0}\) is *not* a galactic core unless a separate, named lift is postulated — and then **do not postulate a lift to \(\tau_{\rm web}\)**.

Galactic cores, if kept, need their own scale (a kpc-class coherence), declared as such. Do not mint it from \(\lambda_{m_0}\) by a 7-fold ladder.

---

## 3. Dark matter without the ansatz shopping

Pick one:

- **A.** Equal density in all six domains. Then \(\sum_{i=2}^{6}\gamma_i\approx 5.40\) is a prediction. Live with the 5.2 vs 5.40 gap, or compute the Yukawa suppression that eats 0.2. Do not retune \(\beta_i\).
- **B.** Densities not equal. Then \(\Omega_{\mathrm{DM}}/\Omega_b\) is not predicted. Say so.

SPARC: freeze \(K\) first, then fit *one* scale per galaxy (or none). Compare to Burkert with the same number of free scales. If Superblock does not win that test, it does not win.

---

## 4. What to stop promising

| Topic | Allowed sentence |
|---|---|
| Glueball | “Lattice \(0^{++}\) sits near \(2m_0\); not a computed spectrum.” |
| Strong-CP | “No geometric cancellation is shown in this paper.” |
| Sterile / partner states | prediction |
| Domain dipole | prediction; CMB dipole remains kinematic unless a specific residual is computed |
| DESI \(w(z)\) | “Centrifugal walk of \(\{\beta_i\}\) is a hypothesis; not fitted here.” |
| 56-tick | prediction, preregistered |
| Weight-6 vs 7 | two integers, kept apart |

---

## 5. Paper shape

1. Frame and locks (one page).
2. \(W(E_8)\), Coxeter element, freeze criterion or frame declaration, \(\beta_i\) table.
3. Kernel \(K\), variable key, Poisson limit.
4. Shadow-gravity estimate under ansatz A or B.
5. Predictions list, each with a named instrument and a kill criterion.
6. No cosmology-of-\(\tau\) section. If \(\tau_{\rm web}\) appears, one sentence: catalogue IR scale of \(K\), not derived from exponent 7.

---

## 6. Order of work

1. Hygiene pass on every live `.md` / Zenodo draft (this week).
2. D1 + D2 in one algebra note (clock only).
3. D3: close \(m_0\) or demote it.
4. D4: Poisson theorem.
5. Shadow-DM number under a frozen map.
6. Preregistration note for LHCb / a *defined* collider statistic / a *defined* CMB residual test.
7. Then, and only then, a single Superblock paper.

Do not start another unification note until D1–D4 exist.

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_how_to_fix_superblock_2026-09-20.md`
