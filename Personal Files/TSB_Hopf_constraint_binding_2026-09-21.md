# Hopf constraint on binding \(B_{7\to i}\)

**Date:** 2026-09-21  
**Geometry:** \(S^1\to S^3_{\rm int}\to S^2\), linking number \(1\).  
**Object:** seventh-phase fabric attaching to domain face \(i\).

---

## 1. Where the six points sit

Each domain occupancy is a point \(p_i\in S^3_{\rm int}\). Hopf projects \(p_i\mapsto x_i\in S^2\). The fibre \(F_i=\pi^{-1}(x_i)\) is an \(S^1\) through \(p_i\).

Two fibres with \(x_i\neq x_j\) have linking number \(1\) in \(S^3\). Same base point: same fibre, only a phase difference.

Generic lock: six distinct \(x_i\) (six fibres). Degenerate lock: two domains share a fibre.

**Key.** \(p_i\): occupancy point. \(x_i=\pi(p_i)\): celestial / Hopf base. \(F_i\): fibre through \(p_i\).

---

## 2. Where slot 7 sits

The fabric is a section or a phase on the fibration, not a seventh point forced by F7. Working choice: \(\mu_7\) lives as a phase along fibres — the Hopf \(S^1\) is the phase-8 / slot-7 clock coordinate, as in the twistor note.

Binding \(B_{7\to i}\) is then: evaluate that phase at \(p_i\) and lock it to \(\varphi_i\).

\[
B_{7\to i}
\propto
\mu_7\big|_{p_i}^{\dagger}\psi_i
\quad\text{only if }
\mu_7\text{ is defined on }F_i.
\]

If the fabric is a *global* section (one phase law on every fibre), it is defined on all six \(F_i\) and all six bindings are topologically allowed. If the fabric is supported on a proper subset of fibres, binding off that subset is forbidden.

**Key.** Support of \(\mu_7\): union of fibres it occupies. Binding only onto that union.

---

## 3. The linking rule

Let \(\gamma_7\) be a closed Hopf fibre occupied by the fabric, and \(\gamma_i\) a small circle about \(p_i\) in a plane transverse to \(F_i\) (or the fibre \(F_i\) itself).

\[
\operatorname{Lk}(\gamma_7,\gamma_i)
\in\mathbb{Z}.
\]

Hopf says \(\operatorname{Lk}=1\) when \(\gamma_7=F_j\) and \(\gamma_i=F_i\) for \(i\neq j\), and \(\operatorname{Lk}=0\) is impossible for two distinct fibres.

**Constraint H1.** A binding that is represented by a pair of closed curves on \(S^3\) must have \(\operatorname{Lk}\in\{0,1\}\). \(\operatorname{Lk}=0\) only if both curves lie on the *same* fibre (phase lock, no inter-fibre link). \(\operatorname{Lk}=1\) if they lie on distinct fibres (standard Hopf). Other integers require a multiply-wound fabric (\(n\in\pi_3\), motherhood winding) and are not the elementary \(B_{7\to i}\).

**Constraint H2.** Two simultaneous bindings \(B_{7\to i}\) and \(B_{7\to j}\) on *distinct* fibres are linked to each other through the fabric. You cannot contract one attachment without dragging the other. That is the topological reason a 7th-phase Mirron that binds to more than one face is a *single* trans-domain object, not two holes.

**Constraint H3.** If two domains share a fibre (\(x_i=x_j\)), they differ only by a phase. Binding to one is binding to that fibre; the second domain is reached by a phase shift, not by a second link. B_lin’s six distinct \(\varphi_i\) suggest six distinct phases; they do not force six distinct base points. Distinct \(\varphi_i\) can live on one fibre. Distinct \(x_i\) need extra input.

---

## 4. What this does *not* fix

- The couplings \(\kappa_i\). Linking is \(0\) or \(1\), not a strength.
- EM neutrality. Hopf is geometry; \(Q_i\) is Maxwell. Keep the selection rule of the neutrality note.
- Which six points are chosen on \(S^3\). F7 and B_lin fix speeds and clock locks, not \(\{x_i\}\subset S^2\).

---

## 5. Working rule for the expansion event

Adopt the global-section choice: \(\mu_7\) defined on all fibres. Then H1 allows every \(B_{7\to i}\), H2 says the six attachments are one linked bundle, H3 is reserved if two locks later share a base point. That matches “one hole, six faces” on the Kerr ring: the ring *is* a Hopf fibre, the six faces are six phases (or six nearby fibres linking the ring).

---

## Master key

| Symbol | Meaning |
|---|---|
| \(\pi:S^3\to S^2\) | Hopf map |
| \(F_i,x_i,p_i\) | fibre, base, occupancy |
| \(\operatorname{Lk}\) | linking number in \(S^3\) |
| H1–H3 | allowed links, bundle, shared fibre |

---

## Session metadata

- 2026-09-21
- `Personal_Files/TSB_Hopf_constraint_binding_2026-09-21.md`
