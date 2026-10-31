# Session log: Two-scalar action

- **Session date:** Friday, 2026-09-18
- **Charge:** Derive the two-scalar action (\(\varphi_{\mathrm{n}}\) nucleation, \(\varphi_{\tau}\) cylinder), neither feeding Maxwell.
- **Short answer:** 5D Einstein–Hilbert on \(M_4\times S^1_\tau\) with *no* KK vector, reduced at radius \(\varphi_{\tau}\), plus a 4D packing scalar \(\varphi_{\mathrm{n}}\) with a void potential and a non-variational nucleation source. \(G_{\mathrm{N}}\) and \(\alpha_{\mathrm{fs}}\) stay data. \(\Gamma\) is a rate, not an Euler–Lagrange equation.
- **This file:** `Personal Files/2026-09-18_two_scalar_action.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(g_{\mu\nu}\) | 4D metric, mostly-plus. |
| \(\theta\in[0,2\pi)\) | Cylinder angle. |
| \(\varphi_{\tau}(x)\) | Cylinder radius (modulus). Dimensions of length. Background \(\langle\varphi_{\tau}\rangle=R_{\tau}\). |
| \(\varphi_{\mathrm{n}}(x)\) | Dimensionless packing / nucleation stiffness. Mean in structure \(\varphi_{\mathrm{n},0}=1\). |
| \(\chi_{\mathrm{M}}\) | Mirror presence (\(0\) or \(1\) coarse-grained to \(n_{\mathrm{M}} v_{\mathrm{M}}\)). |
| \(n_{\mathrm{M}}\) | Proper mirror density. |
| \(G_{\mathrm{N}}\) | Newton constant. **Data.** |
| \(S_{\tau}\) | 5D Einstein–Hilbert on the cylinder, no \(A_{\theta}\). |
| \(S_{\mathrm{n}}\) | 4D action of \(\varphi_{\mathrm{n}}\) and \(\chi_{\mathrm{M}}\). |
| \(S_{\Gamma}\) | Nucleation source. Not obtained from \(\delta S=0\). |
| \(V_{\mathrm{n}}\) | Potential that lowers \(\varphi_{\mathrm{n}}\) in voids. |
| \(\Omega\) | Conformal factor of the 3-metric, \(g_{ij}=a^2\Omega^2\delta_{ij}\) in a void slicing. |
| \(\kappa_{\tau},\kappa_{\mathrm{n}}\) | Dimensionless kinetic normalizations, \(\mathcal{O}(1)\). |
| \(\mu_{\mathrm{n}}\) | Mass scale of \(\varphi_{\mathrm{n}}\) fluctuations. Named; not computed. |
| \(\nu\) | Conformal weight in \(V_{\mathrm{n}}\). Named integer, default \(2\). |
| \(\Delta_{\mathrm{TEP}}\) | Energy cost of one new \(\Sigma_{\mathrm{M}}\). |
| \(F_{\mu\nu}\) | Maxwell field. **Absent** from this action. |

---

## 1. What is being derived

An effective action whose conservative piece owns:

- 4D gravity with measured \(G_{\mathrm{N}}\),
- a compact circle of radius \(\varphi_{\tau}\) with period \(2\pi\) and **no** KK photon,
- a packing scalar \(\varphi_{\mathrm{n}}\) that falls in voids.

The nucleation rate \(\Gamma\) is appended as a source. It is the dissipative part that creates new \(\Sigma_{\mathrm{M}}\). It does not follow from \(\delta S=0\) alone (same status as a Boltzmann collision term).

Maxwell is not in the action. That is the ownership split, not an accident of gauge fixing.

---

## 2. Cylinder sector (5D \(\to\) 4D)

Line element, product / warped, **no** \(A_{\mu}\mathrm{d}x^{\mu}\):
\[
\mathrm{d}s_5^2
=
g_{\mu\nu}(x)\,\mathrm{d}x^{\mu}\mathrm{d}x^{\nu}
+
\varphi_{\tau}(x)^2\,\mathrm{d}\theta^2,
\qquad
\theta\sim\theta+2\pi.
\]
**Key:** dropping \(A_{\mu}\) is the statement that \(S^1_{\tau}\) is not the EM fibre.

5D Einstein–Hilbert, \(G_5\) eliminated with \(G_{\mathrm{N}}=G_5/(2\pi R_{\tau})\) *as bookkeeping only* after C1 missed as a prediction. In 4D we use \(G_{\mathrm{N}}\) as data:
\[
S_{\tau}
=
\int\mathrm{d}^4x\,\sqrt{-g}
\left[
\frac{R[g]}{16\pi G_{\mathrm{N}}}
-\frac{\kappa_{\tau}}{2\varphi_{\tau}^2}(\partial\varphi_{\tau})^2
-U_{\tau}(\varphi_{\tau})
\right].
\]
**Key:** \(\kappa_{\tau}=1\) after canonical normalization of a circle modulus (standard KK, no vector). \(U_{\tau}\) freezes \(\varphi_{\tau}\) at \(R_{\tau}\):
\[
U_{\tau}=\frac12 m_{\tau}^2(\varphi_{\tau}-R_{\tau})^2
\quad\text{or a slow-roll freeze;}
\quad
m_{\tau}\ \text{large enough that }\dot R_{\tau}/R_{\tau}\text{ is not a fifth-force.}
\]
Background: \(\varphi_{\tau}=R_{\tau}=7\,h^{-1}\,\mathrm{Mpc}\). Fluctuations of \(\varphi_{\tau}\) are gravitational-strength at most (\(\kappa_{\tau}\sim 1\)) and are not photons.

Equation of motion:
\[
\kappa_{\tau}\nabla_{\mu}\Bigl(\frac{\nabla^{\mu}\varphi_{\tau}}{\varphi_{\tau}^2}\Bigr)
+\frac{\kappa_{\tau}}{\varphi_{\tau}^3}(\partial\varphi_{\tau})^2
-U_{\tau}'(\varphi_{\tau})=0.
\]
On the frozen background this is \(0=0\).

---

## 3. Nucleation scalar (4D)

\(\varphi_{\mathrm{n}}\) is not the cylinder radius. It is a dimensionless 4D field.

\[
S_{\mathrm{n}}
=
\int\mathrm{d}^4x\,\sqrt{-g}
\left[
-\frac{\kappa_{\mathrm{n}}}{2}(\partial\varphi_{\mathrm{n}})^2
-V_{\mathrm{n}}(\varphi_{\mathrm{n}},\Omega)
-\,n_{\mathrm{M}}\Delta_{\mathrm{TEP}}\,\chi_{\mathrm{unit}}
\right].
\]
**Key:** last term is the rest-energy density of existing mirrors (\(\chi_{\mathrm{unit}}\) converts \(n_{\mathrm{M}}\Delta_{\mathrm{TEP}}\) to a Lagrangian density; in the rest frame it is \(n_{\mathrm{M}}\Delta_{\mathrm{TEP}}\)). Existing mirrors cost \(\Delta_{\mathrm{TEP}}\) each. They do not stretch.

Void potential (named weight \(\nu=2\)):
\[
V_{\mathrm{n}}
=
\frac{\mu_{\mathrm{n}}^2}{2}\bigl(\varphi_{\mathrm{n}}-\Omega^{-\nu}\bigr)^2.
\]
**Key:** in mean structure \(\Omega=1\Rightarrow\langle\varphi_{\mathrm{n}}\rangle=1=\varphi_{\mathrm{n},0}\). In a void \(\Omega>1\Rightarrow\) the target \(\Omega^{-\nu}<1\), so \(\varphi_{\mathrm{n}}\) is pulled below \(\varphi_{\mathrm{crit}}=\varphi_{\mathrm{n},0}=1\). That is the stiffness gate as an equilibrium condition of \(V_{\mathrm{n}}\).

Euler–Lagrange:
\[
\kappa_{\mathrm{n}}\Box\varphi_{\mathrm{n}}
=
\mu_{\mathrm{n}}^2\bigl(\varphi_{\mathrm{n}}-\Omega^{-\nu}\bigr).
\]
In a static void, \(\varphi_{\mathrm{n}}=\Omega^{-\nu}\). The \(\Theta(\varphi_{\mathrm{crit}}-\varphi_{\mathrm{n}})\) of \(\Gamma\) then fires where \(\Omega>1\).

Gradient gate is *not* reproduced by \(V_{\mathrm{n}}\). It is part of \(\Gamma\) below.

---

## 4. Nucleation source (not \(\delta S=0\))

Continuity with creation:
\[
\nabla_{\mu}\bigl(n_{\mathrm{M}} u^{\mu}\bigr)=\Gamma,
\]
\[
\Gamma
=
3H n_{\mathrm{M}}
\,\Theta(1-\varphi_{\mathrm{n}})
\,\Theta\bigl(\lvert\nabla\log\Omega\rvert-H/c\bigr).
\]
**Key:** this is appended. It does not arise from varying \(S_{\tau}+S_{\mathrm{n}}\). The variational action conserves \(n_{\mathrm{M}} u^{\mu}\) if \(\Gamma=0\). Expansion plus the two \(\Theta\)s injects current so that \(\dot n_{\mathrm{M}}+3H n_{\mathrm{M}}=0\) on the support of the gates (Branch A).

Energy accounting: each created mirror adds \(\Delta_{\mathrm{TEP}}\) to the rest-energy density. That is a drain on the gravitational / void sector (the conformal energy in \(\Omega\)), not a Maxwell process.

---

## 5. Full effective action

\[
S
=
S_{\tau}+S_{\mathrm{n}}
=
\int\mathrm{d}^4x\,\sqrt{-g}
\Bigg[
\frac{R}{16\pi G_{\mathrm{N}}}
-\frac{\kappa_{\tau}}{2\varphi_{\tau}^2}(\partial\varphi_{\tau})^2
-U_{\tau}(\varphi_{\tau})
-\frac{\kappa_{\mathrm{n}}}{2}(\partial\varphi_{\mathrm{n}})^2
-\frac{\mu_{\mathrm{n}}^2}{2}(\varphi_{\mathrm{n}}-\Omega^{-\nu})^2
-n_{\mathrm{M}}\Delta_{\mathrm{TEP}}
\Bigg].
\]
Plus the constraint / source
\[
\nabla_{\mu}(n_{\mathrm{M}} u^{\mu})=\Gamma[\varphi_{\mathrm{n}},\Omega,H].
\]

**Absent by construction:**
\[
-\frac{1}{4}f(\varphi_{\mathrm{n}})F^2,\qquad
-\frac{1}{4}f(\varphi_{\tau})F^2,\qquad
A_{\mu}\mathrm{d}x^{\mu}\ \text{in }\mathrm{d}s_5^2.
\]

---

## 6. What is derived vs named

| Piece | Status |
|---|---|
| No KK vector on \(S^1_{\tau}\) | Ownership axiom |
| 4D Einstein term with \(G_{\mathrm{N}}\) | Data (C1 miss) |
| Modulus kinetic term \(\propto(\partial\varphi_{\tau})^2/\varphi_{\tau}^2\) | Standard circle reduction |
| \(U_{\tau}\) freeze at \(R_{\tau}\) | Named |
| \(V_{\mathrm{n}}\propto(\varphi_{\mathrm{n}}-\Omega^{-\nu})^2\) | Named; \(\nu=2\) default |
| \(\varphi_{\mathrm{crit}}=1\) | From \(\varphi_{\mathrm{n},0}=1\) |
| \(\Gamma\) with \(H/c\) gate | Named (S1); not from \(\delta S\) |
| \(\mu_{\mathrm{n}},\kappa_{\mathrm{n}},\kappa_{\tau},m_{\tau}\) | \(\mathcal{O}(1)\) or heavy; not computed |
| \(\alpha_{\mathrm{fs}}\), \(e\), \(F_{\mu\nu}\) | Not in \(S\) |

---

## 7. Direct statement

The two-scalar action is the Einstein–Hilbert term with measured \(G_{\mathrm{N}}\), a frozen circle modulus \(\varphi_{\tau}\), a packing scalar \(\varphi_{\mathrm{n}}\) slaved to \(\Omega^{-\nu}\) in equilibrium, a rest-energy density of mirrors, and a non-variational current \(\Gamma\). That is the conservative-plus-rate system that implements Branch A without an EM fibre.

---

*End of session note — 2026-09-18 two-scalar action.*
