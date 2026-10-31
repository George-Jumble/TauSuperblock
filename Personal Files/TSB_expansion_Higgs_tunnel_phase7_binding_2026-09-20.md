# Expansion event — Higgs tunnel, seventh-phase binding (4D reconstruction)

**Date:** 2026-09-20  
**Intent:** original Superblock expansion mechanics, minus 5D / \(7\,h^{-1}\,\mathrm{Mpc}\) KK.  
**Status:** working reconstruction. Not live-frame law. Live frame still owns F7, B_lin, \(K\), \(m_0\) as floor.  
**Convention:** Mirron, never “soliton.”

---

## 0. Phase inventory (8 ticks, no extra circle)

Octonionic refresh is eight phases. Split them by job, not by a compact fifth dimension.

| Phase slot | Job |
|---|---|
| \(1,\ldots,6\) | six domain phases (the moving copies; “prime phases” here means the six occupied domain ticks, not only \(D_1\)) |
| \(7\) | Higgs / twistor fabric. Clock algebra: frozen exponent \(7\) as \(\varphi\sim\varphi+2\pi\), residue \(0\) as the empty class. Not a megaparsec. |
| \(8\) | Mirron reset tick |

**Key.** \(\varphi_n=n\pi/4\), \(n=0,\ldots,7\): 8-phase clock. Slots \(1\)–\(6\): domain occupancy. Slot \(7\): Higgs fabric. Slot \(8\): reset. Exponent \(7\) names slot \(7\), not a length.

Original language: “\(313\,\mathrm{MeV}\) friction in the 7th-phase Higgs fabric,” “flux crosses 7th-phase Planckian mirrors into Prime,” “Phase-7 Higgs/Twistor substrate.” Keep those as fabric-and-mirror talk. Drop every sentence that parked them on a metric \(S^1_\tau\).

---

## 1. Trigger: isolated chamber, vacuum owns the stress

Same causal switch as the Superblock event note: walls leave the observer’s event horizon. Incoming Prime EM is off. Leftover radiation is CMB plus horizon glow.

\[
|P_{\rm vac}|
\gg
P_{\rm rad}
=
\frac{\rho_{\rm CMB}}{3}+\frac{\rho_{\rm GH}}{3}.
\]

Original sentence: when that inequality holds, the Higgs fabric is no longer radiation-pinned and may tunnel toward its full potential.

This is **not** the electroweak crossover at \(T\sim 100\,\mathrm{GeV}\). That already happened. This is a late, local, void-chamber statement about the *same fabric* once radiation pressure has dropped out of the budget.

**Key.** \(P_{\rm vac}=-\rho_{\rm vac}\). Chamber: isolated Prime patch. Not the early-universe EW transition.

---

## 2. Higgs fabric — tunnel to full potential

Write a two-well sketch for the slot-7 field \(\Phi_7\) (Higgs / twistor fabric, not derived from \(\tau\)):

\[
V(\Phi_7)
=
V_{\rm pin}(P_{\rm rad})
+
V_{\rm well}(\Phi_7).
\]

While \(P_{\rm rad}\) is comparable to \(|P_{\rm vac}|\), \(V_{\rm pin}\) holds \(\Phi_7\) off the deep well (radiation stimulation of Phase-7 in the old notes). When \(P_{\rm rad}\) drops out,

\[
V_{\rm pin}\to 0,
\]

and \(\Phi_7\) can tunnel or roll toward the deeper minimum \(\Phi_7\to\Phi_\star\) (“full potential”).

No calculation of the bounce action is supplied here. No derivation of \(v_{\rm EW}\) or of \(m_0\) from this well. \(m_0\) remains the IR floor of the live frame. If the old “\(313\,\mathrm{MeV}\) friction” is kept, it is a damping term in the fabric,

\[
V_{\rm fric}
\sim
\frac12 m_0\,|\dot\Phi_7|^2
\quad\text{(schematic viscosity, not a mass theorem).}
\]

**Key.** \(\Phi_7\): slot-7 fabric field. \(\Phi_\star\): deep-well value. \(V_{\rm pin}\): radiation pin. \(V_{\rm fric}\): 7th-phase friction at the \(m_0\) floor.

Default vacuum in the current derivation is still \(\nabla\rho_{\rm vac}=0\). Tunneling of \(\Phi_7\) is a change of *which well the fabric sits in*, not a derivation of \(\rho_{\rm vac}\) from \(\tau\).

---

## 3. Binding: seventh-phase Mirrons to the six domain phases

Original sentence: once the fabric is in the deep well, Mirrons that live in slot 7 can bind to the six domain phases.

Write a binding projector. Let \(\psi_i\) be the occupancy of domain phase \(i=1,\ldots,6\), and \(\mu_7\) the Mirron amplitude in slot 7.

\[
B_{7\to i}
=
\kappa_i\,
\theta\bigl(|P_{\rm vac}|-P_{\rm rad}\bigr)\,
\theta\bigl(|\Phi_7-\Phi_\star|<\varepsilon\bigr)\,
\mu_7^\dagger\psi_i
+\mathrm{h.c.}
\]

**Key.** \(B_{7\to i}\): binding of a 7th-phase Mirron to domain phase \(i\). \(\kappa_i\): coupling, not fitted here. \(\theta\): step that opens only in the chamber after the fabric has reached the deep well. \(\varepsilon\): well-tolerance.

Before the trigger, \(B_{7\to i}=0\) (fabric pinned, slot 7 does not stick to the six). After the trigger, slot 7 is allowed to attach. That is hierarchical binding in the old notes, stripped of the cell radius.

The six copies remain the moving F7 set. Binding does not add a seventh spacetime. It adds a **link** from the fabric slot onto those six.

Reset slot 8 still averages with \(\mathcal{P}_8\). Binding that survives \(\mathcal{P}_8\) is secular; binding that dies under \(\mathcal{P}_8\) is tick noise.

---

## 4. Hook to the Mirron current

On the isolated patch the stress current was

\[
J^\nu_{\rm Mirron}
=
-
\Delta^\nu_K.
\]

With binding on, a piece of \(T_M\) is the bound fabric–domain stress. Then

\[
J^\nu_{\rm bind}
=
-
\nabla_\mu T^{\mu\nu}_{\rm bind},
\qquad
T_{\rm bind}
\sim
\sum_{i=1}^{6}
|B_{7\to i}|^2\,
u^\mu u^\nu
+\cdots
\]

Secular production booked into rest-mass standing waves is

\[
J^\nu_{\rm sec}
=
-
\mathcal{P}_8
\bigl(\Delta^\nu_K
+
\nabla_\mu T^{\mu\nu}_{\rm bind}\bigr).
\]

Still a transfer. Hidden copies through \(K\), plus bound slot-7 fabric, can feed the visible account after EM cutoff. Vacuum density by default still does not.

**Key.** \(T_{\rm bind}\): stress of the \(7\to i\) links. \(u^\mu\): 4-velocity of the patch observer.

---

## 5. Other original expansion pieces, kept / dropped

| Original piece | Keep in 4D? |
|---|---|
| Dynamic refresh through PK mirrors | Keep. Mirrors are local Mirron engines, not a compact fifth dimension. |
| Double-negative / Prime-Past transit | Keep as domain-orientation talk (time-reversed copy). Not a KK flux tube. |
| 7th-phase Planckian mirrors | Keep as slot-7 engine faces. |
| \(313\,\mathrm{MeV}\) fabric friction | Keep as \(V_{\rm fric}\) at the IR floor, not a prize. |
| Photons/neutrinos stimulate Phase-7 | Keep as \(V_{\rm pin}(P_{\rm rad})\). Isolation removes the stimulus. |
| Hierarchical binding \(7\to 6\) | Keep as \(B_{7\to i}\). |
| Higgs tunnel when \(P_{\rm vac}>P_{\rm rad}\) | Keep as late chamber statement, not EW \(T\sim 100\,\mathrm{GeV}\). |
| Metric \(S^1_\tau\), Casimir-\(\Lambda\), KK tower, 7 Mpc cell as the well | Drop. |
| Dual-role exponent 7 as a length | Drop. |
| “Zero parameters,” detections | Drop. |

---

## 6. Sequence (one breath)

Six domain phases run. Slot 7 is the Higgs fabric, pinned by radiation. Slot 8 resets. Walls leave the horizon. \(P_{\rm rad}\) drops out of the budget. Fabric tunnels or rolls to \(\Phi_\star\). Seventh-phase Mirrons bind to the six domain phases. \(K\) plus \(T_{\rm bind}\) set \(J_{\rm sec}\). Integrated vacuum energy still grows with volume; that is GR, not a running \(v\).

No fifth dimension appears.

---

## 7. What is not derived

- The bounce action, nucleation rate, or \(\Phi_\star\).
- The six \(\kappa_i\).
- A baryon yield from \(J_{\rm sec}\).
- Identity of \(\Phi_\star\) with \(v_{\rm EW}\).
- Any length from slot 7.

---

## Master key

| Symbol | Meaning |
|---|---|
| slots \(1\)–\(6,7,8\) | domains, Higgs fabric, reset |
| \(\Phi_7,\Phi_\star,V_{\rm pin},V_{\rm fric}\) | fabric field, deep well, radiation pin, \(m_0\) friction |
| \(B_{7\to i}\) | binding 7th-phase Mirron to domain phase \(i\) |
| \(\mu_7,\psi_i\) | slot-7 Mirron amplitude; domain occupancy |
| \(J_{\rm sec}\) | secular current after \(\mathcal{P}_8\) |
| \(\Delta_K\) | kernel defect |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_expansion_Higgs_tunnel_phase7_binding_2026-09-20.md`
