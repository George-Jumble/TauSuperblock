# TSB Core Geometry v0.1b — Global Tav manifold and local Tau fibers

**Date:** 2026-09-05  
**Status:** Terminology locked. Working geometry selected. Problem not solved.  
**Depends on:** `2026-09-05_TSB_Core_Geometry_v0.1_Bound_Global_Tav_Derivation.md`

---

## Variable key

| Symbol | Meaning |
|--------|---------|
| \(\mathcal{M}_{\mathrm{Tav}}\) | Global 5-manifold. Total space of the theory. **Not** called \(S^1_\infty\) |
| \(M_4\) | 4D base (observable spacetime) |
| \(\pi:\mathcal{M}_{\mathrm{Tav}}\to M_4\) | Projection of the working bundle |
| \(S^1_\tau(x)\) | Fiber \(\pi^{-1}(x)\), a compact circle at the event \(x\in M_4\) |
| \(R(x)\) | Metric radius of that fiber |
| \(L(x)=2\pi R(x)\) | Physical circumference if \(\theta\sim\theta+2\pi\) |
| \(L(x)=\pi R(x)\) | Circumference if the fiber is \(S^1/\mathbb{Z}_2\) |
| \(\theta\) | Fiber coordinate |
| \(\widetilde{\mathcal{M}}_{\mathrm{Tav}}\) | Universal cover of \(\mathcal{M}_{\mathrm{Tav}}\), if a cover is used |
| \(V_{\mathrm{cl}}(R)\) | Classical (tree-level) radion potential |
| \(V_{\mathrm{Cas}}(R)\) | One-loop Casimir potential of declared field content on the *fiber* |
| \(V_{\mathrm{eff}}=V_{\mathrm{cl}}+V_{\mathrm{Cas}}\) | Effective 4D potential for \(R\) |
| \(\lambda_4\) | 4D vacuum operator that does not come from fiber Casimir |
| \(R_*\) | Stationary point of \(V_{\mathrm{eff}}\), if one exists |

Reserve **Tau circle** for \(S^1_\tau(x)\) only.  
Reserve **Tav manifold** for \(\mathcal{M}_{\mathrm{Tav}}\).  
Do not write \(S^1_\infty\) until a topology theorem says the global object is a circle.

---

## 1. The ambiguity that is now closed as language, not as mathematics

“Tau circle / cylinder” was being used for

- a local finite circumference,
- a global vacuum topology,
- a Casimir cavity,
- a 7 Mpc coherence cell.

Those are four different mathematical objects. The correction is:

\[
\mathcal{M}_{\mathrm{Tav}}
\quad\longrightarrow\quad
S^1_\tau(x),
\qquad
L(x)=\oint_{S^1_\tau(x)} R(x)\,d\theta.
\]

On a single compact fiber the KK expansion is legal:

\[
\Phi(x,\theta)
=
\sum_{n\in\mathbb{Z}}\phi_n(x)\,e^{in\theta},
\qquad
p_{5,n}
=
\frac{n}{R(x)}
\quad(\hbar=1,\ \theta\sim\theta+2\pi).
\]

**Key**

- \(\Phi\): 5D field.
- \(\phi_n\): 4D KK modes.
- \(p_{5,n}\): discrete fiber momentum. This formula exists only while the fiber is compact.

That block is where a mode ladder, winding, RGC correspondence, and any derived IR scale have to live. None of it is inherited by \(\mathcal{M}_{\mathrm{Tav}}\) automatically.

---

## 2. Four inequivalent meanings of the “global” object

These are not the same manifold. Choosing one is the first mathematical problem.

### A. Fiber bundle (working choice for v0.1b)

\[
\pi:\mathcal{M}_{\mathrm{Tav}}\to M_4,
\qquad
\pi^{-1}(x)\cong S^1.
\]

The global object is the total 5-manifold. The local object is the fiber. There is one circle per base point, not two circles of different radii.

Metric (same ansatz as v0.1):

\[
d\tilde s^2
=
g_{\mu\nu}(x)\,dx^\mu dx^\nu
+
R^2(x)\bigl(d\theta+\kappa A_\mu(x)\,dx^\mu\bigr)^2.
\]

**What “global vacuum” means here:** a solution of the 5D Einstein equation on \(\mathcal{M}_{\mathrm{Tav}}\), including whatever \(\lambda_4\) or \(\Lambda_5\) is declared.  
**What Casimir means here:** a one-loop determinant on the compact fiber. It belongs to \(S^1_\tau(x)\), not to “infinity.”

This option makes the old sentence “move Casimir from the 7 Mpc node onto the infinite circle” **false**. Casimir lives on the fiber.

### B. Noncompact fifth direction

\(\mathcal{M}_{\mathrm{Tav}}=M_4\times\mathbb{R}_\theta\). No global circle. Continuous spectrum in the fifth momentum. A local \(S^1_\tau\) can exist only as an approximate bound-state well (periodic potential, solitonic compactification, or a finite region where \(R(x)\) is small). Exact Fourier KK modes are lost.

Casimir of a compact circle does not exist globally. Vacuum must come from \(\Lambda_5\) or an induced 4D term.

### C. Decompactification limit of the same circle

Topologically still \(S^1\), but \(R\to\infty\). Compact coordinate, diverging metric length. Casimir \(\to 0\) after vacuum subtraction. This is a *limit of A*, not a second manifold.

### D. Universal cover

\[
\widetilde{\mathcal{M}}_{\mathrm{Tav}}
=
M_4\times\mathbb{R},
\qquad
\mathcal{M}_{\mathrm{Tav}}
=
\widetilde{\mathcal{M}}_{\mathrm{Tav}}/\mathbb{Z}
=
M_4\times S^1.
\]

The cover is noncompact and has no Casimir from discrete modes. The quotient has the KK tower and the Casimir. If someone wants “unbound Casimir,” this option gives the opposite assignment: Casimir sits on the compact quotient.

---

## 3. Working geometry (declared, not derived)

v0.1b uses **A**. Reasons:

- It is the only option already written as a metric in the project.
- It makes “global vs local” a total-space vs fiber statement, which is standard.
- It does not invent an “infinite circle.”
- It forces the Casimir question to be answered honestly: Casimir is a fiber effect.

If later calculations show that A cannot stabilize \(R_*\) and also leave a nonzero vacuum, the team switches to B or D by an explicit metric change, not by renaming \(S^1_\infty\).

---

## 4. Where the vacuum lives under A

Split the effective potential as required:

\[
V_{\mathrm{eff}}(R)
=
V_{\mathrm{cl}}(R)
+
V_{\mathrm{Cas}}(R)
+
\lambda_4.
\]

**Key**

- \(V_{\mathrm{cl}}\): reduction of Einstein–Hilbert \(+\Lambda_5+\) flux \(+\) brane tension. From v0.1, \(V_{\mathrm{cl}}\propto\Lambda_5/L\) has no finite minimum by itself.
- \(V_{\mathrm{Cas}}\): one-loop determinant of declared 5D fields on \(S^1_\tau\), with declared periodic or antiperiodic boundary conditions. Scales as \(L^{-4}\) (Jordan) and vanishes as \(L\to\infty\).
- \(\lambda_4\): 4D vacuum operator *not* generated by that determinant. This is the only term that can stay finite when the fiber decompactifies.

Dimensional check, already computed in v0.1 and kept here so it cannot drift:

\[
V_{\mathrm{Cas}}(L\sim 10\,\mathrm{Mpc})
\sim
L^{-4}
\sim
10^{-121}\,\mathrm{eV}^4,
\qquad
\rho_\Lambda^{\mathrm{obs}}
\sim
2.6\times 10^{-11}\,\mathrm{eV}^4.
\]

Mismatch \(\sim 10^{110}\). The simplest Casimir interpretation of observed dark energy is ruled out for a Mpc fiber. That calculation is done. It is a negative theorem, not a pending estimate.

Therefore, under working geometry A:

| Layer | Vacuum role |
|-------|-------------|
| Fiber Casimir \(V_{\mathrm{Cas}}\) | can help *shape* \(V_{\mathrm{eff}}\) near a finite \(R_*\); cannot be \(\rho_\Lambda\) |
| Classical \(V_{\mathrm{cl}}\) | runaway or collapse alone; needs extra operators to make a well |
| \(\lambda_4\) | only legal source of a finite global \(w=-1\) term that survives large \(R\) |

The sentence to retire: “Casimir energy belongs to the infinite circle.”  
The sentence that replaces it: “Fiber Casimir belongs to \(S^1_\tau(x)\). Global vacuum belongs to \(\mathcal{M}_{\mathrm{Tav}}\) as \(\lambda_4\) or a 5D Einstein integration constant.”

---

## 5. Stabilization problem, now well-posed

On geometry A the first target is a single pair of conditions:

\[
\left.\frac{\partial V_{\mathrm{eff}}}{\partial R}\right|_{R_*}
=
0,
\qquad
\left.\frac{\partial^2 V_{\mathrm{eff}}}{\partial R^2}\right|_{R_*}
>
0,
\]

with

\[
V_{\mathrm{eff}}(R_\infty)
=
\lambda_4
\quad\text{or a specified plateau},
\qquad
w=-1.
\]

Two things must come out of one action:

1. a local well at finite \(R_*\) (bound Tau fiber),
2. a nonzero vacuum term that is *not* \(V_{\mathrm{Cas}}(R_*)\).

If the well only exists when \(\lambda_4=0\), or the vacuum only exists when there is no well, the architecture splits and one of the two claims is dropped.

Field content for the first Casimir determinant must be declared before the derivative is taken. Placeholder content for the first pass:

- 5D graviton (unavoidable),
- optional bulk fermions with periodic or antiperiodic BC,
- optional flux integer \(n_{\mathrm{flux}}\) in \(V_{\mathrm{cl}}\).

No \(7\), no \(313.1\,\mathrm{MeV}\), no \(\tau_{\mathrm{obs}}\) on the right-hand side.

---

## 6. Reorganized architecture

| Layer | Role | What must be derived |
|-------|------|----------------------|
| Global Tav manifold \(\mathcal{M}_{\mathrm{Tav}}\) | 5D total space, long-range sector, vacuum topology | metric, topology (A/B/C/D), vacuum state |
| Local Tau fiber \(S^1_\tau(x)\) | compact gravitational / coherence cell | \(R_*\) from \(V_{\mathrm{eff}}'=0\), \(V_{\mathrm{eff}}''>0\) |
| KK spectrum | local excitations on the fiber | \(\{\phi_n,p_{5,n}\}\) from the 5D action at \(R_*\) |
| 7-fold / RGC sector | special local resonance | why 7 from topology or spectrum, not from \(n=7\) |
| PK intersection | proposed IR scale | \(m_0=\mathcal{F}(M_5(R_*),\mathcal{I})\), compare to \(313.1\,\mathrm{MeV}\) only after \(R_*\) |
| 4D Superblock projection | observable phenomenology | reduction to GR / SM limits |
| Experiments | Casimir / collider / cosmology | statistics frozen before unseen data |

Required chain:

\[
S_5
\;\rightarrow\;
\text{solution on }\mathcal{M}_{\mathrm{Tav}}
\;\rightarrow\;
S^1_\tau\text{ stabilization}
\;\rightarrow\;
\text{KK / phase spectrum}
\;\rightarrow\;
\text{special resonance}
\;\rightarrow\;
m_0
\;\rightarrow\;
\text{observable}.
\]

If an arrow fails, that layer is revised. No sideways expansion until the first two arrows exist as equations.

---

## 7. What this note does *not* claim

- It does not claim \(R_*=\tau_{\mathrm{obs}}\).
- It does not claim a computed \(V_{\mathrm{Cas}}\) for a declared spectrum. That determinant is the next calculation.
- It does not claim that seven is an eigenstructure of the Einstein–Hilbert fiber.
- It does not claim that \(M_5(R_*)\) equals \(313.1\,\mathrm{MeV}\). The orbifold diagnostic in v0.1 remains a diagnostic.

It does claim:

- \(S^1_\infty\) is retired,
- Casimir is a fiber object,
- global \(w=-1\) is not fiber Casimir,
- one working metric is now on the table.

---

*Saved: Tau-Superblock_Universe/Personal_Files/2026-09-05_TSB_Core_Geometry_v0.1b_Global_Manifold_and_Local_Fibers.md*
