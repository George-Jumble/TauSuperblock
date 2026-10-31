# 4D conformal crossover — importing Penrose / Tod (working note)

**Date:** 2026-09-20  
**Rule:** four dimensions only. No KK cylinder, no metric \(S^1_\tau\), no dual-role 7.  
**Status:** working note, not a replacement of the live Superblock frame.  
**Convention:** Mirron, never “soliton.”

---

## 0. What is being imported

Penrose’s conformal cyclic cosmology (CCC), in Tod’s 4D form:

Each aeon is a complete 4-manifold with \(\Lambda>0\), expanding for infinite proper time. The conformal metric continues through future infinity \(\mathscr{I}^+\) of one aeon and becomes the bang surface of the next. The join is a spacelike 3-surface \(\mathcal{X}\), the **crossover**.

That is already 4D. Nothing here needs a fifth dimension.

**Key.** Aeon: one expanding 4-history. \(\mathcal{X}\): crossover 3-surface. \(\mathscr{I}^+\): future conformal infinity. Bridging metric: an unphysical 4-metric to which both physical metrics are conformal.

---

## 1. The bandage (Penrose / Tod)

In a neighbourhood of \(\mathcal{X}\) (the bandage) there is no rest mass. The stress tensor is trace-free. Only lightcone structure remains. Two physical metrics \(\hat g_{\mu\nu}\) (late previous aeon) and \(\check g_{\mu\nu}\) (early present aeon) share a bridging metric \(g_{\mu\nu}\):

\[
\hat g_{\mu\nu}=\hat\Omega^{2}\,g_{\mu\nu},
\qquad
\check g_{\mu\nu}=\check\Omega^{2}\,g_{\mu\nu}.
\]

Penrose’s reciprocal hypothesis (one convenient choice; not the only one in the later literature):

\[
\hat\Omega\,\check\Omega=-1
\quad\text{on the bandage.}
\]

As \(\mathcal{X}\) is approached from the past, \(\hat\Omega\to 0\) (\(\mathscr{I}^+\)). From the future, \(\check\Omega\to+\infty\) (bang). Lightcones match. Clocks do not: rest mass is gone, so there is no proper-time standard on \(\mathcal{X}\).

**Key.** \(\hat\Omega,\check\Omega\): conformal factors of the two aeons. \(g_{\mu\nu}\): bridge. Bandage: region where \(T^\mu{}_\mu=0\).

Weyl tensor \(C_{\rho\sigma\mu\nu}\) is conformally invariant (with the usual weight). Tod’s reading of the Weyl curvature hypothesis: if the conformal metric extends smoothly through \(\mathcal{X}\), then \(C=0\) on \(\mathcal{X}\). Gravitational waves of the previous aeon can still register as a *normal derivative* of \(C\) across \(\mathcal{X}\).

Hawking points (Penrose): isolated points on \(\mathcal{X}\) where a previous-aeon cluster hole finishes evaporating. Claimed CMB spots. Status: disputed; later nulls at pre-registered scales. **Not a trophy here.**

---

## 2. What Superblock can carry without leaving 4D

Live Superblock already speaks conformal language: twistor averaging, Weyl gravity in the kernel’s ancestry, Mirron as a reflection of an aeon.

Map, kept thin:

| Penrose / Tod | Superblock, 4D only |
|---|---|
| Aeon | One complete 4-history of the six co-located copies |
| Crossover \(\mathcal{X}\) | The 3-surface where rest mass has faded and only \(K\)’s conformal skeleton remains |
| Bridging metric | The conformal class on which \(K\) is an average of lightcone data |
| Reciprocal \(\hat\Omega\check\Omega=-1\) | A chart choice on that class, not a new field |
| Weyl \(C=0\) on \(\mathcal{X}\) | Initial condition of the next aeon; hidden-domain shadows do not seed Weyl at \(\mathcal{X}\) |
| Mirron | The reflection map across \(\mathcal{X}\): previous aeon \(\to\) next, Planck–Kerr as the local engine of that map |
| 8-phase | Internal tick of the engine, not a fifth dimension |

Six domains stay in 4D: they share the same macroscopic \((t,\mathbf{x})\) and the same crossover 3-surface. They do not get six different bangs. If they did, conformal matching would have to be written six times and then averaged; that is a later paper.

**Key.** Mirron: reflection across \(\mathcal{X}\), 4D. \(K\): 4D kernel. On the bandage, \(K\) can only average trace-free sources.

---

## 3. The mass problem (do not slide)

CCC needs rest mass to fade so that \(\mathcal{X}\) has no clocks. Live Superblock has an IR floor \(m_0=313.1\,\mathrm{MeV}\). Those two sentences fight.

Honest options, still 4D:

1. **Fade.** \(m_0\) is an aeon-interior floor. On the bandage it goes to zero with all other rest masses. Then \(m_0\) is not eternal. Say so.
2. **Exception.** \(m_0\) never fades. Then \(\mathcal{X}\) is not a Penrose crossover. Do not call it one.
3. **Conformal rest mass.** Some CCC variants let a rest-mass scalar recover after \(\mathcal{X}\). \(m_0\) would be that recovery scale in the new aeon. That is a hypothesis, not a derivation.

This note does not pick 1–3. It forbids writing “\(m_0\) is geometric *and* the bandage has no rest mass” in one breath.

Photon and graviton need no fade. They are the fields the bandage is made of.

---

## 4. What the kernel must do near \(\mathcal{X}\)

Far-zone Poisson is an aeon-interior statement (\(r\gg\lambda_{m_0}\), rest mass present). On the bandage:

- Yukawa range \(\lambda_{m_0}=\hbar/(m_0 c)\) diverges if \(m_0\to 0\) (option 1). The kernel becomes long-range conformal.
- If \(m_0\) stays (option 2), the kernel keeps a finite range and the crossover is not CCC.

No 7-fold lift. No megaparsec cell as \(\mathcal{X}\). \(\mathcal{X}\) is a *time* boundary (bang / \(\mathscr{I}^+\)), not a spatial web scale.

Centrifugal walk of \(\{\beta_i\}\) is an aeon-interior hypothesis (P6). It does not glue aeons.

---

## 5. What is *not* imported

- Inflation. CCC replaces it with conformal stretch of leftover massless modes. Superblock does not add a second inflaton.
- A 5D bandage or a KK circle as \(\mathcal{X}\).
- Hawking-point detections.
- Information-loss theology beyond: Penrose needs BH information loss for the 2nd law across aeons. Mirron-as-reflection is a different bookkeeping. Do not declare them the same.
- Periodicity. CCC is cyclic conformal geometry, not a periodic copy of the same history.

---

## 6. A minimal 4D working picture

One 4-manifold, many aeons, one conformal class through each \(\mathcal{X}\).

Inside an aeon: six copies, F7, B_lin, \(K\), Poisson, shadow ratio under A, \(m_0\) as floor.

At \(\mathcal{X}\): rest mass off (or the name CCC is dropped), Weyl off, lightcones on, Mirron is the reflection.

After \(\mathcal{X}\): new aeon, Weyl starts at zero, masses recover by whatever option in §3 is later chosen.

That is the import. It is 4D. It does not fix \(m_0\), does not compute \(P_{\rm vac}\), and does not mint a length from exponent 7.

---

## 7. Next calculation, if this stays

Write the bandage condition on \(K\): \(T^\mu{}_\mu=0\) for every domain that still contributes. Show that the averaged Einstein tensor remains compatible with a conformal rescaling through \(\mathcal{X}\). If that identity fails, the kernel and CCC do not fit.

Until that identity exists, this note is a dictionary, not a theorem.

---

## Master key

| Symbol | Meaning |
|---|---|
| \(\mathcal{X}\) | crossover 3-surface |
| \(\hat g,\check g,g\) | previous, present, bridge metrics |
| \(\hat\Omega,\check\Omega\) | conformal factors |
| \(C_{\rho\sigma\mu\nu}\) | Weyl tensor |
| bandage | \(T^\mu{}_\mu=0\) neighbourhood of \(\mathcal{X}\) |
| Mirron | 4D reflection across \(\mathcal{X}\) |
| \(K\) | 4D kernel; Poisson only off the bandage |
| \(m_0\) | IR floor; in tension with the bandage until §3 is chosen |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_4D_conformal_crossover_Penrose_2026-09-20.md`
- Live Superblock frame remains `TSB_Superblock_fixed_frame_2026-09-20.md`
