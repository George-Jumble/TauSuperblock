# TSB Core Geometry v0.1 — Bound/Global Tav Derivation

**Date:** 2026-09-05  
**Status:** Work package opened. Radius stabilization is the first calculation.  
**Rule:** \(\tau\) and \(313.1\,\mathrm{MeV}\) do not appear on any right-hand side as inputs.

---

## Variable key

| Symbol | Meaning |
|--------|---------|
| \(\tilde g_{MN}\) | 5D metric, \(M,N=0,1,2,3,5\) |
| \(g_{\mu\nu}\) | 4D metric in the given ansatz (Jordan-like frame) |
| \(R(x)\) | Dynamical fiber radius field. One field only |
| \(\theta\) | Fiber coordinate. Period \(2\pi\) on a circle; period \(\pi\) on \(S^1/\mathbb{Z}_2\) |
| \(L[R]\) | Physical fiber length \(\oint R\,d\theta\) |
| \(\kappa\) | Kaluza–Klein gauge coupling in the off-diagonal term |
| \(A_\mu\) | 4D KK photon / graviphoton |
| \(M_5\) | 5D Planck mass, \([M_5]=\mathrm{mass}\) |
| \(M_{\mathrm{Pl}}\) | 4D Planck mass \(1.22089\times 10^{19}\,\mathrm{GeV}\) |
| \(\overline{M}_{\mathrm{Pl}}\) | Reduced 4D Planck mass \(M_{\mathrm{Pl}}/\sqrt{8\pi}\) |
| \(\Lambda_5\) | 5D cosmological constant, \([\Lambda_5]=\mathrm{mass}^5\) in EH units used below |
| \(V_{\mathrm{eff}}(R)\) | 4D effective potential for the radius, Einstein frame unless noted |
| \(\psi\) | Einstein-frame radion, \(\psi \propto \ln(R/R_0)\) |
| \(\rho_{\mathrm{global}}, p_{\mathrm{global}}\) | Homogeneous vacuum energy and pressure seen in 4D |
| \(\ell_{\mathrm{Pl}}\) | Planck length \(1.616255\times 10^{-35}\,\mathrm{m}\) |
| \(\ell_{\mathrm{PK}}\) | Planck–Kerr length. Not an independent input until derived |
| \(n_{\mathrm{winding}}\) | Integer winding of a preonic / KK mode on the fiber |
| \(\mathcal{I}_{\mathrm{topology}}\) | Discrete topological data (orbifold vs circle, flux, holonomy) |
| \(m_0\) | Derived IR mass floor. Target comparison \(313.1\,\mathrm{MeV}\) is *output only* |
| \(h\) | Hubble parameter in units \(H_0=100h\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) |
| \(\tau_{\mathrm{obs}}\) | Observed conformal-cell scale \(\approx 7\,h^{-1}\mathrm{Mpc}\). **Not an input** |

Natural units \(\hbar=c=1\) unless a conversion is being evaluated.

---

## 0. What this package is for

The bound / unbound split reorganized the architecture. It also exposed three claims that were being carried as language rather than as theorems:

1. Why a *local* fiber sits at a finite radius.
2. How a global \(w=-1\) vacuum can exist if that fiber is allowed to decompactify.
3. How any Mpc-scale geometric object can source a hadronic IR floor.

This note starts the spine

\[
\text{5D action}
\;\rightarrow\;
V_{\mathrm{eff}}'(R_*)=0,\; V_{\mathrm{eff}}''(R_*)>0
\;\rightarrow\;
\rho_{\mathrm{global}}=V_{\mathrm{eff}}(R_\infty)
\;\rightarrow\;
m_0=\mathcal{F}(R_*,\ell_{\mathrm{PK}},n_{\mathrm{winding}},\mathcal{I}_{\mathrm{topology}})
\;\rightarrow\;
\text{eigenmodes of the stabilized fiber}.
\]

Seven is not assumed. If a sevenfold spectrum appears, it must be an eigenstructure of the stabilized fiber.

---

## 1. Governing ansatz (one radius field)

\[
d\tilde s^2
=
g_{\mu\nu}(x)\,dx^\mu dx^\nu
+
R^2(x)\bigl(d\theta+\kappa A_\mu(x)\,dx^\mu\bigr)^2.
\]

**Key to this equation**

- \(\tilde s\): 5D line element.
- \(g_{\mu\nu}\): 4D metric at point \(x\).
- \(R(x)\): single dynamical radius. There are not two metric circles.
- \(\theta\): fiber angle.
- \(\kappa A_\mu dx^\mu\): KK connection. \(\kappa\) sets the charge of the graviphoton.

**Bound / unbound reading of the same field**

- *Local node:* a region where \(R(x)\) sits at a finite minimum \(R_*\). That is the bound Tau fiber.
- *Global / unbound sector:* the same field in a homogeneous or covering-space configuration \(R\to R_\infty\le\infty\). Not a second circle in the metric.

If \(\theta\sim\theta+2\pi\) the physical length is \(L=2\pi R\).  
If the fiber is an orbifold \(S^1/\mathbb{Z}_2\) with \(\theta\sim\theta+\pi\), then \(L=\pi R\).  
Both are written explicitly below. Neither is chosen to hit \(313.1\,\mathrm{MeV}\).

---

## 2. 5D action and 4D reduction

Minimal bulk action:

\[
S_5
=
M_5^3\int d^5x\,\sqrt{-\tilde g}
\left(
\frac{1}{2}\,\tilde{\mathcal{R}}
-
\Lambda_5
\right)
+
S_{\mathrm{extra}}.
\]

**Key**

- \(\tilde{\mathcal{R}}\): 5D Ricci scalar of \(\tilde g_{MN}\).
- \(\Lambda_5\): bulk cosmological term. Sign convention: \(+\Lambda_5\) in the potential piece of the action as written.
- \(S_{\mathrm{extra}}\): everything that is *not* Einstein–Hilbert plus \(\Lambda_5\) (Casimir, brane tension, Gauss–Bonnet, flux, bulk matter). This is where stabilization can live.

Integrate the fiber at fixed \(R\), \(A_\mu=0\), to obtain the Jordan-frame 4D action

\[
S_4
=
\int d^4x\,\sqrt{-g}
\left(
\frac{1}{2} M_5^3 L[R]\,\mathcal{R}_4
-
M_5^3 L[R]\,\Lambda_5
+
\frac{3}{4} M_5^3 L[R]\,(\partial\ln R)^2
+
\cdots
\right).
\]

**Key**

- \(L[R]=\oint R\,d\theta\): physical fiber length.
- \(\mathcal{R}_4\): 4D Ricci scalar of \(g_{\mu\nu}\).
- The coefficient of \(\mathcal{R}_4\) *is* the 4D Planck mass squared:

\[
M_{\mathrm{Pl}}^2(R)
=
M_5^3\,L[R].
\]

That relation will be used later as a *derived* IR scale, not as a way to insert \(313.1\,\mathrm{MeV}\).

Pass to the Einstein frame by the Weyl rescaling
\(g_{\mu\nu}= \Omega^{-2}\bar g_{\mu\nu}\) with \(\Omega^2 = M_{\mathrm{Pl}}^2(R)/M_{\mathrm{Pl},0}^2 \propto L[R]\).  
The Einstein-frame radion

\[
\psi
=
\sqrt{\frac{3}{2}}\,\overline{M}_{\mathrm{Pl}}\,\ln\!\left(\frac{L[R]}{L_0}\right)
\]

has canonical kinetics, and the Einstein-frame potential is

\[
V_{\mathrm{eff}}(R)
=
\left(\frac{L_0}{L[R]}\right)^2
\left(
M_5^3 L[R]\,\Lambda_5
+
U_{\mathrm{extra}}(R)
\right).
\]

**Key**

- \(L_0\): reference length that defines the Einstein-frame unit. It cancels in stationarity conditions written in terms of \(R\).
- \(U_{\mathrm{extra}}(R)\): Jordan-frame energy density integrated over the fiber from \(S_{\mathrm{extra}}\).

---

## 3. First theorem: Einstein–Hilbert + \(\Lambda_5\) does not stabilize a finite fiber

Set \(U_{\mathrm{extra}}=0\). Then

\[
V_{\mathrm{eff}}(R)
=
C\,\frac{\Lambda_5}{L[R]},
\qquad
C=M_5^3 L_0^2.
\]

**Key:** \(C\) is a positive constant. \(L[R]\propto R\).

- If \(\Lambda_5>0\), \(V_{\mathrm{eff}}\) decreases as \(R\) increases: runaway decompactification.
- If \(\Lambda_5<0\), \(V_{\mathrm{eff}}\) decreases as \(R\) decreases: collapse to zero radius.
- There is no point with \(V_{\mathrm{eff}}'=0\) and \(V_{\mathrm{eff}}''>0\).

So a local Tau node **cannot** be a minimum of the Einstein–Hilbert plus bulk cosmological term. That is the first closed gap: the old language that “the 5D KK substrate sets \(\tau\)” is false unless \(S_{\mathrm{extra}}\) is specified.

The same theorem kills the naive identification

\[
\rho_{\mathrm{global}}
\;\stackrel{?}{=}\;
\text{Casimir of a compact Mpc circle}.
\]

A massless 5D field on a circle of length \(L\) produces a Jordan-frame Casimir piece

\[
U_{\mathrm{Cas}}(L)
=
\frac{\alpha}{L^4},
\qquad
\alpha
=
-\frac{\pi^2}{90}\,n_B
+
\frac{7\pi^2}{720}\,n_F
+
\cdots
\]

up to the usual periodic/antiperiodic signs and \(\zeta\)-values. In Einstein frame this is a \(1/L^6\) or \(1/L^4\) term according to the Weyl weight. Either way:

\[
U_{\mathrm{Cas}}(L)\to 0
\quad\text{as}\quad
L\to\infty.
\]

That is the decompactification limit the team already flagged. It cannot be the global \(w=-1\) vacuum.

Numerical size, so the point cannot drift back in later drafts. For \(L\sim 10\,\mathrm{Mpc}\),

\[
L^{-4}
\sim
10^{-121}\,\mathrm{eV}^4,
\qquad
\rho_\Lambda^{\mathrm{obs}}
\sim
2.6\times 10^{-11}\,\mathrm{eV}^4.
\]

The mismatch is \(\sim 10^{110}\). A compactification Casimir at the observed cell scale is not dark energy.

---

## 4. Minimal extra operators that *can* produce a finite minimum

Stationarity in Einstein frame:

\[
V_{\mathrm{eff}}'(R_*)=0,
\qquad
V_{\mathrm{eff}}''(R_*)>0.
\]

A finite \(R_*\) requires at least two competing \(R\)-dependences in \(U_{\mathrm{extra}}\). The cheapest local operators are:

| Operator | Jordan-frame scaling | Role |
|----------|----------------------|------|
| Bulk \(\Lambda_5\) | \(\propto L\) | runaway or collapse, no min alone |
| Massless Casimir | \(\propto L^{-4}\) | extremum with \(\Lambda_5\) is typically a *maximum* |
| Massive bulk Casimir \(\rho(m,L)\) | interpolates \(L^{-4}\leftrightarrow e^{-mL}\) | can convert a max into a min |
| 3-brane tension \(T_4\) | \(\propto L^{0}\) | shifts vacuum energy; does not set \(R_*\) by itself |
| Flux / holonomy \(n_{\mathrm{flux}}^2/L^{2}\) | \(\propto L^{-2}\) | standard KK stabilization piece |
| Gauss–Bonnet / higher curvature | mixed | can slow the radion through radiation/matter era |
| 2-loop / interacting Casimir | \(\propto g_5^2 L^{-5}\) | can stabilize without \(\Lambda_5\) (Ponton–Poppitz) |

**Working hypothesis for v0.1 (to be kept or killed by the calculation, not by taste):**

\[
U_{\mathrm{extra}}(R)
=
\frac{\alpha}{L[R]^4}
+
\frac{\beta}{L[R]^2}
+
T_4
+
U_{\mathrm{massive}}(m_i L[R]).
\]

Then \(V_{\mathrm{eff}}'(R_*)=0\) becomes an algebraic relation

\[
L_*
=
L_*(\alpha,\beta,\Lambda_5,m_i)
\]

with **no** \(7\,h^{-1}\mathrm{Mpc}\) on the right-hand side.

That is the first arrow. It has not been evaluated yet. The next calculation in this package is exactly that stationary-point equation, with \(\alpha,\beta,m_i\) taken from a declared 5D field content, not tuned to \(\tau_{\mathrm{obs}}\).

**Honesty constraint.** If the only way to land on \(10\,\mathrm{Mpc}\) is to put a mass \(m\sim 1/L_*\) into the bulk by hand, then \(\tau\) has been reinserted under another name. That is not a derivation. A genuine derivation must produce \(L_*\) from scales that are already in the 5D action for another reason (Planck scale, a 5D gauge coupling, a flux quantum, an orbifold interval fixed by topology).

At Mpc radii the only *a priori* 5D scale that is not inserted by hand is \(M_5\) itself, and \(M_5\) is slaved to \(L\) by \(M_{\mathrm{Pl}}^2=M_5^3 L\). Using \(M_5(L)\) as an input mass in \(U_{\mathrm{extra}}\) is circular unless the Einstein-frame matching is done self-consistently. That self-consistent loop *is* the calculation.

---

## 5. Global vacuum after decompactification

Require a 4D vacuum that survives \(R\to R_\infty\):

\[
\rho_{\mathrm{global}}
=
\lim_{R\to R_\infty} V_{\mathrm{eff}}(R),
\qquad
p_{\mathrm{global}}
=
-\rho_{\mathrm{global}}.
\]

From §3, neither \(\Lambda_5 L\) nor \(U_{\mathrm{Cas}}(L)\) gives a finite nonzero limit of that form in Einstein frame.

**What can:**

1. A 4D cosmological term that does not come from the fiber at all: an induced 4D Einstein–Hilbert plus \(\lambda_4\) on a brane, or an unimodular integration constant in the 4D trace of the Einstein equation. Then

\[
\rho_{\mathrm{global}}
=
\lambda_4,
\qquad
w
=
-1
\]

exactly, independent of \(R\). This is the cleanest global \(w=-1\). It is also the least “Tav-like”: the vacuum is no longer produced by the fifth direction.

2. A residual Einstein-frame value at a *finite* but cosmologically large homogeneous background \(R_\infty\neq R_*\). That is a two-critical-point potential: a local well at \(R_*\) (bound node) and a second, almost flat plateau at large \(R\) with \(V_{\mathrm{plateau}}=\rho_{\mathrm{global}}\). Possible, but it is a designed potential, not a theorem.

3. Covering-space reading. The metric fiber remains locally \(S^1\) of length \(L_*\), but the global \(\theta\)-coordinate lives on the universal cover \(\mathbb{R}\). Discrete KK sums become integrals, Casimir \(\to 0\), and the observed vacuum must again be an \(R\)-independent operator as in (1).

v0.1 position, pending the potential calculation:

> The global \(w=-1\) sector is **not** ordinary compactification Casimir. It is an \(R\)-independent 4D vacuum operator, disclosed to local physics through the stabilized fiber. Calling it “Casimir” is retired until an explicit Casimir sum is shown to survive \(R\to\infty\).

That is the second closed gap.

---

## 6. The IR floor, with \(313.1\,\mathrm{MeV}\) forbidden on the right-hand side

After a minimum \(R_*\) exists, the only geometric mass that the 5D reduction itself produces is the 5D Planck mass slaved to the fiber:

\[
M_5(R_*)
=
\left(
\frac{M_{\mathrm{Pl}}^2}{L[R_*]}
\right)^{1/3}.
\]

**Key:** \(M_{\mathrm{Pl}}\) is measured 4D gravity. \(L[R_*]\) is the derived minimum, not \(\tau_{\mathrm{obs}}\) until the potential calculation succeeds.

This is *not* a KK mode of the Mpc fiber. The KK tower of that fiber sits at

\[
m_n
=
\frac{n}{L[R_*]}
\sim
10^{-30}\,\mathrm{eV}
\quad\text{if}\quad
L\sim 10\,\mathrm{Mpc}.
\]

That tower cannot be \(m_0\). Anyone writing \(m_0\sim n/L\) at Mpc scales is done. The floor, if it exists, is a *derived 5D gravitational scale*, or a winding/exclusion cost built from \(\ell_{\mathrm{Pl}}\) and \(L_*\), not a compactification harmonic.

### 6.1 Scale arithmetic (comparison only — not a fit)

Using \(M_{\mathrm{Pl}}=1.22089\times 10^{19}\,\mathrm{GeV}\) and \(L=\tau_{\mathrm{obs}}=7\,h^{-1}\mathrm{Mpc}\) at \(h=0.698\) *only as a diagnostic*, if the potential *had already* landed on that length:

| Convention for \(L\) | \(M_5\) | \(M_5/313.1\,\mathrm{MeV}\) |
|----------------------|---------|------------------------------|
| \(L=\tau_{\mathrm{obs}}\) | \(456.4\,\mathrm{MeV}\) | \(1.458\) |
| \(L=2\pi\tau_{\mathrm{obs}}\) | \(247.3\,\mathrm{MeV}\) | \(0.790\) |
| \(L=\pi\tau_{\mathrm{obs}}\) (orbifold interval) | \(311.6\,\mathrm{MeV}\) | \(0.995\) |

The orbifold length \(L=\pi R\) lands \(0.5\%\) from \(313.1\,\mathrm{MeV}\) *if* \(R_*\) is already \(\tau_{\mathrm{obs}}\). That is a coincidence until \(R_*\) is derived and the orbifold is required by \(\mathcal{I}_{\mathrm{topology}}\), not by the proximity of \(311.6\) to \(313.1\).

Equivalent rewriting, same diagnostic:

\[
M_5
=
M_{\mathrm{Pl}}
\left(
\frac{\ell_{\mathrm{Pl}}}{L}
\right)^{1/3}.
\]

The exponent \(1/3\) is the engineering dimension of \(M_{\mathrm{Pl}}^2=M_5^3 L\). It is not a fitted \(\alpha\).

### 6.2 Allowed form of the floor

\[
m_0
=
\mathcal{F}
\bigl(
M_5(R_*),
\,\ell_{\mathrm{PK}}/\ell_{\mathrm{Pl}},
\,n_{\mathrm{winding}},
\,\mathcal{I}_{\mathrm{topology}}
\bigr).
\]

Allowed ingredients on the right-hand side: \(M_{\mathrm{Pl}}\), \(R_*\) from \(V_{\mathrm{eff}}'=0\), integers \(n_{\mathrm{winding}}\), and discrete topology.  
Forbidden: \(313.1\,\mathrm{MeV}\), \(m_\pi\), \(m_N\), \(\Lambda_{\mathrm{QCD}}\) as inputs.

v0.1 does **not** claim \(m_0=313.1\,\mathrm{MeV}\). It claims a candidate identity

\[
m_0
\;\stackrel{?}{=}\;
c_{\mathcal{I}}\,M_5(R_*)
\]

with \(c_{\mathcal{I}}\) a pure topological number of order one (orbifold length, winding, \(\zeta\)-value). If after \(R_*\) is derived one finds \(c_{\mathcal{I}} M_5 \neq 313.1\,\mathrm{MeV}\) by a factor that cannot be absorbed in topology, that part of the phenomenological layer is revised.

---

## 7. Sevenfold spectrum only after \(R_*\) exists

Order of operations from now on:

\[
S_5
\;\rightarrow\;
V_{\mathrm{eff}}(R)
\;\rightarrow\;
R_*
\;\rightarrow\;
\text{linearized fiber eigenmodes on }(R_*,\mathcal{I}_{\mathrm{topology}})
\;\rightarrow\;
\text{spectrum }\{k_n\}.
\]

The mode problem on a circle is \(k_n=n/L_*\). That is *integer*, not sevenfold.  
A sevenfold spectrum requires extra structure in \(\mathcal{I}_{\mathrm{topology}}\):

- \(\mathbb{Z}_7\) holonomy or a seventh-order orbifold,
- a potential on the fiber with seven wells,
- an octonionic / \(G_2\) structure whose harmonic analysis produces period \(7\),
- or an RGC identification that is *hardware*, not spacetime.

None of those is implied by the Einstein–Hilbert ansatz. If the team wants seven as an eigenstructure, it must be put in as topology or derived from a specified \(S_{\mathrm{extra}}\) whose symmetry is sevenfold. Starting from “\(1/7=0.142857\)” and searching for seven remains forbidden in this package.

---

## 8. Immediate next calculation (radius stabilization)

**Goal.** Write \(V_{\mathrm{eff}}(R)\) for the smallest \(S_{\mathrm{extra}}\) that admits a finite positive-mass-squared minimum, and solve \(V_{\mathrm{eff}}'(R_*)=0\) without \(\tau_{\mathrm{obs}}\) on the right-hand side.

**Proposed content of \(S_{\mathrm{extra}}\) for the first pass**

1. 5D graviton Casimir on the fiber (unavoidable).
2. One flux or holonomy integer \(n_{\mathrm{flux}}\).
3. Optional: \(S^1/\mathbb{Z}_2\) so that \(L=\pi R\) is not a fit but a topology choice, declared up front.

**Deliverable of that calculation**

- Explicit \(V_{\mathrm{eff}}(R)\).
- Existence or non-existence of \(R_*\) with \(V''>0\).
- The combination of \((M_5,\Lambda_5,n_{\mathrm{flux}})\) that sets \(R_*\), and whether that combination is independent of \(\tau_{\mathrm{obs}}\).
- The Einstein-frame value \(V_{\mathrm{eff}}(R_*)\) and the limit \(V_{\mathrm{eff}}(R\to\infty)\).

If the only minima sit at micron or TeV radii (ordinary Casimir / dark-dimension radii), then a *Mpc* bound node is not a vacuum of this action and the bound Tau cell must be re-identified: not as the KK radius itself, but as a derived coherence / exhaustion scale built from a much smaller stabilized fiber. That would be a structural revision, not a patch.

---

## 9. Where the framework stands after this note

The bound / unbound clarification is kept:

- one 5D metric,
- one dynamical radius \(R(x)\),
- local wells = bound Tau fibers,
- global vacuum \(\neq\) compactification Casimir.

What is no longer assumed:

- that \(\tau=7\,h^{-1}\mathrm{Mpc}\) is a minimum of the 5D action,
- that the global \(w=-1\) vacuum is Casimir energy of that circle,
- that \(313.1\,\mathrm{MeV}\) is a KK harmonic of a Mpc fiber,
- that seven is an eigenstructure of the Einstein–Hilbert circle.

What is queued, in order:

1. Stabilize \(R\) from \(V_{\mathrm{eff}}\).
2. Identify \(\rho_{\mathrm{global}}\) as an \(R\)-independent operator, or show an explicit surviving Casimir.
3. Form \(m_0=\mathcal{F}(M_5(R_*),\mathcal{I})\) and compare to \(313.1\,\mathrm{MeV}\) only after (1).
4. Only then ask why the eigenstructure would be sevenfold.
5. Only then freeze statistics and point them at unseen data.

---

*Saved: Tau-Superblock_Universe/Personal_Files/2026-09-05_TSB_Core_Geometry_v0.1_Bound_Global_Tav_Derivation.md*
