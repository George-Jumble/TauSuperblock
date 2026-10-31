# Session log: 5D Einstein–dilaton hop — the continuation that can move \(\Phi\) by more than \(\mathcal{O}(1)\)

- **Session date:** Friday, 2026-09-18
- **Charge:** “The only honest continuation that could still change \(\Phi\) by more than \(\mathcal{O}(1)\) is a different hop from the 5D Einstein–dilaton reduction, not another integer story about 137. Now try to fix this.”
- **Short answer:** The hop is different, and \(\Phi\) moves by many orders of magnitude. It does not land on \(\Phi_{\mathrm{obs}}=2\alpha_{\mathrm{fs}}\). Cylinder reduction of 5D Einstein–Hilbert plus the Kaluza–Klein dilaton, in the convention
  \[
  \mathrm{d}s_5^2=g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu+\varphi^2(\mathrm{d}\theta+A_\mu\mathrm{d}x^\mu)^2,
  \]
  \(\theta\sim\theta+2\pi\), yields
  \[
  g^2=\frac{16\pi G_4}{\varphi^2},\qquad
  \alpha_{\mathrm{5D}}=\frac{g^2}{4\pi}=\frac{4G_4}{\varphi^2}=4\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2
  \]
  (\(\hbar=c=1\), \(G_4=\ell_P^2\)). Then \(\Phi_{\mathrm{5D}}=2\alpha_{\mathrm{5D}}=8(\ell_P/\varphi)^2\). The 48-vertex cell is no longer the leading \(\Phi\). Identifying \(\varphi\) with the three TSB lengths gives three wrong numbers: \(\varphi=r_{\mathrm{M}}\) \(\Rightarrow\alpha\sim 10^{-39}\); \(\varphi=R_\tau\) \(\Rightarrow\alpha\sim 10^{-116}\); \(\varphi=\ell_P\) \(\Rightarrow\alpha=4\). The unique vev that hits CODATA inside *this* prefactor is
  \[
  \varphi_{\mathrm{EM}}/\ell_P=2/\sqrt{\alpha_{\mathrm{fs}}}\approx 23.41,
  \]
  a Planckian fibre, not the Mirron clock and not the Tav cylinder. \(7\pi\approx 21.99\) misses that ratio by \(6.4\,\%\) and is not entered as a result. Dilaton kinetics vanish at constant vev and do not change the prefactor. \(e\) stays explicit: \(\alpha_{\mathrm{5D}}=e^2/(4\pi\varepsilon_0\hbar c)\) is the same \(\alpha\) as always; the 5D work is a formula for \(\alpha\), hence for \(\Phi=2\alpha\), not a new ohm that hides \(e\).
- **This file:** `Personal Files/2026-09-18_5D_Einstein_dilaton_hop_and_Phi.md`
- **Parents:** `2026-09-18_Phi_from_8phase_E8_six_domain_cell_alpha_fs_attempt.md`, `2026-09-17_Z0_of_nM_linear_response.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(\mathrm{d}s_5^2\) | 5D Einstein–Kaluza–Klein line element. |
| \(g_{\mu\nu}\) | 4D metric (zero-mode). |
| \(\varphi\) | KK dilaton / fibre radius. Length. Constant vev in this note. |
| \(\theta\) | Angular coordinate on \(S^1\), period \(2\pi\). |
| \(A_\mu\) | KK U(1) potential (zero-mode photon). |
| \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) | 4D field strength of that U(1). |
| \(G_5\) | 5D Newton constant. |
| \(G_4\) | 4D Newton constant. |
| \(\ell_P=\sqrt{\hbar G_4/c^3}\) | 4D Planck length \(\approx 1.616\times 10^{-35}\,\mathrm{m}\). |
| \(M_5\) | 5D Planck mass, \(16\pi G_5=1/M_5^3\) in one common convention; tracked, not required. |
| \(R_5,R_4\) | 5D and 4D Ricci scalars. |
| \(g^2\) | 4D Yang–Mills coupling of the KK photon, from \(S\supset -1/(4g^2)\int F^2\). |
| \(\alpha_{\mathrm{5D}}=g^2/(4\pi)\) | Fine-structure *candidate* from the reduction. |
| \(\alpha_{\mathrm{fs}}\approx 1/137.036\) | CODATA fine-structure constant. |
| \(\Phi_{\mathrm{5D}}=2\alpha_{\mathrm{5D}}\) | Impedance factor from this hop. \(Z_0=\mathrm{R_K}\Phi\). |
| \(\Phi_{\mathrm{cell}}=34/31\) | Connected \(6\times 8\) Kirchhoff result (previous session). |
| \(\Phi_{\mathrm{obs}}=2\alpha_{\mathrm{fs}}\approx 0.014595\) | Target. |
| \(\varphi_{\mathrm{EM}}\) | Fibre vev that enters the Maxwell term. |
| \(r_{\mathrm{M}}=\lambda_{313}\) | Mirron clock radius \(\approx 6.302\times 10^{-16}\,\mathrm{m}\). |
| \(R_\tau\sim 7\,h^{-1}\,\mathrm{Mpc}\) | Tav-cylinder radius. Taken \(\approx 10\,\mathrm{Mpc}\) for \(h=0.7\). |
| \(\Delta_{\mathrm{TEP}}\approx 313.1\,\mathrm{MeV}\) | TEP floor. |
| \(e,h,\mathrm{R_K}\) | Elementary charge, Planck constant, von Klitzing \(h/e^2\). |
| \(Z_{\mathrm{hop}}^{(4\mathrm{D})}=2h/e^2\) | Old tick / TEP voltage-current hop. |
| \(S_5\) | 5D Einstein–Hilbert action. |

---

## 1. Why this hop is the one that can move \(\Phi\)

The 2026-09-18 cell computed
\[
\Phi_{\mathrm{cell}}=\frac{Z_{\mathrm{hop}}^{(4\mathrm{D})}}{\mathrm{R_K}}\,R_{\mathrm{hop}}=\frac{34}{31},
\]
with \(Z_{\mathrm{hop}}^{(4\mathrm{D})}=2h/e^2\) taken from a 4D \(V/I\) on one tick. Every graph built from \(\{6,7,8\}\) left \(R_{\mathrm{hop}}=\mathcal{O}(1)\). Changing the *graph* cannot manufacture \(137\). Changing the *hop* can, because a 5D reduction replaces \(2\mathrm{R_K}\) by a coupling that knows \(\varphi/\ell_P\).

That replacement is this session. It is not an integer factorization of \(137\).

---

## 2. 5D Einstein–dilaton action and the cylinder ansatz

Einstein–Hilbert in five dimensions:
\[
S_5=\frac{1}{16\pi G_5}\int\mathrm{d}^5x\,\sqrt{-\hat g}\,R_5.
\]
**Key:** \(\hat g\) 5D metric; \(G_5\) 5D Newton constant; \(R_5\) 5D Ricci scalar.

Cylinder ansatz (TSB EKK, \(\theta\)-independent zero modes):
\[
\mathrm{d}s_5^2
=
g_{\mu\nu}(x)\,\mathrm{d}x^\mu\mathrm{d}x^\nu
+
\varphi^2\bigl(\mathrm{d}\theta+A_\mu(x)\,\mathrm{d}x^\mu\bigr)^2,
\qquad
\theta\sim\theta+2\pi.
\]
**Key:** \(\varphi\) has dimension length and *is* the proper radius of the fibre. \(A_\mu\) has dimension \(1/\mathrm{length}\). This is the same ansatz as the kinematics notes, with their \(\varphi\) written as a length rather than as a dimensionless stiffness times a frozen radius.

Volume factor:
\[
\sqrt{-\hat g}=\varphi\sqrt{-g}.
\]
The 5D Ricci scalar reduces (standard Kaluza split; dilaton not Weyl-rescaled into the 4D Einstein frame beyond what is already in \(\varphi\)) to
\[
R_5
=
R_4
-\frac{2}{\varphi}\Box\varphi
-\frac{\varphi^2}{4}F_{\mu\nu}F^{\mu\nu}
+
\text{(dilaton kinetics already in }\Box\varphi\text{)}.
\]
**Key:** \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\). The Maxwell piece is \(-\varphi^2 F^2/4\). At constant \(\varphi\) the \(\Box\varphi\) term drops. That is why a constant dilaton vev does not add a new prefactor; it only sets the number \(\varphi\).

Integrate the fibre:
\[
\int_0^{2\pi}\mathrm{d}\theta=2\pi.
\]
Einstein–Hilbert zero mode:
\[
\frac{2\pi\varphi}{16\pi G_5}\int\mathrm{d}^4x\sqrt{-g}\,R_4
=
\frac{1}{16\pi G_4}\int\mathrm{d}^4x\sqrt{-g}\,R_4,
\]
hence
\[
G_4=\frac{G_5}{2\pi\varphi}.
\]
**Key:** \(G_4\) is the observed 4D Newton constant in this reduction. TSB’s hierarchical / six-domain averaging of \(G\) is a *different* claim and is not used inside this hop; using both at once would double-count.

Maxwell zero mode:
\[
S_F
=
\frac{1}{16\pi G_5}\int\mathrm{d}\theta\,\varphi\sqrt{-g}\Bigl(-\frac{\varphi^2}{4}F^2\Bigr)
=
-\frac{2\pi\varphi^3}{64\pi G_5}\int\sqrt{-g}\,F^2
=
-\frac{\varphi^3}{32 G_5}\int\sqrt{-g}\,F^2.
\]
4D Yang–Mills convention \(S\supset -1/(4g^2)\int F^2\):
\[
\frac{1}{4g^2}=\frac{\varphi^3}{32 G_5}
\qquad\Rightarrow\qquad
\frac{1}{g^2}=\frac{\varphi^3}{8 G_5}.
\]
Substitute \(G_5=2\pi\varphi G_4\):
\[
\frac{1}{g^2}=\frac{\varphi^2}{16\pi G_4},\qquad
g^2=\frac{16\pi G_4}{\varphi^2}.
\]
Fine-structure candidate, \(\hbar=c=1\), \(\alpha=g^2/(4\pi)\), \(G_4=\ell_P^2\):
\[
\alpha_{\mathrm{5D}}
=
\frac{4G_4}{\varphi^2}
=
4\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2.
\]
**Key:** this is the hop. \(e\) has not disappeared: \(\alpha_{\mathrm{5D}}\) is the same \(\alpha\) that satisfies \(\alpha=e^2 Z_0/(2h)\). The 5D calculation predicts \(\alpha\), therefore predicts
\[
\Phi_{\mathrm{5D}}=2\alpha_{\mathrm{5D}}=8\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2.
\]

An 8π-convention in the Einstein equation (\(G_{\mu\nu}=8\pi G T_{\mu\nu}\), \(M_P^2=1/(8\pi G)\)) replaces \(4\) by \(1/(2\pi)\) and moves \(\varphi/\ell_P\) by \(\sqrt{8\pi}\). That is an \(\mathcal{O}(1)\) convention, not a \(10^{20}\) lever. It is flagged, not used to hunt \(137\).

---

## 3. Numerical hop for every TSB length

| Fibre vev \(\varphi\) | \(\varphi/\ell_P\) | \(\alpha_{\mathrm{5D}}=4(\ell_P/\varphi)^2\) | \(\Phi_{\mathrm{5D}}=2\alpha_{\mathrm{5D}}\) | \(1/\alpha_{\mathrm{5D}}\) |
|---|---|---|---|---|
| \(\ell_P\) | \(1\) | \(4\) | \(8\) | \(0.25\) |
| \(r_{\mathrm{M}}=\lambda_{313}\) | \(3.90\times 10^{19}\) | \(2.63\times 10^{-39}\) | \(5.26\times 10^{-39}\) | \(3.80\times 10^{38}\) |
| \(R_\tau\approx 10\,\mathrm{Mpc}\) | \(1.91\times 10^{58}\) | \(1.10\times 10^{-116}\) | \(2.19\times 10^{-116}\) | \(9.11\times 10^{115}\) |
| \(\varphi_{\mathrm{EM}}\) that hits \(\alpha_{\mathrm{fs}}\) | \(23.41\) | \(1/137.036\) | \(0.014595\) | \(137.036\) |

**Key:** \(\Phi_{\mathrm{cell}}=34/31\approx 1.10\) sits next to the Planckian row, not next to \(r_{\mathrm{M}}\) or \(R_\tau\). Replacing the 4D tick-hop by this 5D hop with \(\varphi=r_{\mathrm{M}}\) changes \(\Phi\) by \(\sim 10^{38}\). That is more than \(\mathcal{O}(1)\). It overshoots the target in the opposite direction from the cell.

The unique constant vev that reproduces CODATA *inside this prefactor* is Planckian:
\[
\frac{\varphi_{\mathrm{EM}}}{\ell_P}=\frac{2}{\sqrt{\alpha_{\mathrm{fs}}}}\approx 23.41.
\]
No TSB primitive equals \(23.41\). The nearest corpus combination is \(7\pi\approx 21.99\) (relative miss \(6.4\,\%\)). That miss is larger than the uncertainty on \(\alpha_{\mathrm{fs}}\) by twelve orders of magnitude. It is not a derivation.

---

## 4. Two radii, two reductions

TSB already carries two compact lengths. They cannot both be the Maxwell fibre.

| Reduction | \(\varphi\) | What it can source | What it does to \(\alpha\) |
|---|---|---|---|
| Cosmic EKK | \(R_\tau\) | late-time cylinder, voids, \(w=-1\) language | \(\alpha\sim 10^{-116}\), not EM |
| Mirron clock | \(r_{\mathrm{M}}\) | tick, TEP, \(\Delta t_\tau\) | \(\alpha\sim 10^{-39}\), not EM |
| Planckian seed | \(\sim 23\,\ell_P\) | KK photon coupling in this prefactor | \(\alpha\sim\alpha_{\mathrm{fs}}\) by construction of the vev |

The honest “fix” of the hop is therefore a **split**:
- the bounce / tick still uses \(r_{\mathrm{M}}\);
- the U(1) coupling uses a Planckian fibre \(\varphi_{\mathrm{EM}}\);
- \(R_\tau\) stays out of \(\alpha\).

That split is allowed by the corpus (seed \(\ell_P\), clock \(r_{\mathrm{M}}\), cylinder \(R_\tau\)). It is not derived from the dilaton equation. The dilaton EOM at constant \(\varphi\) is an algebraic constraint on \(F^2\) plus curvature; it does not select \(23.41\,\ell_P\).

---

## 5. Relation to the old \(V/I\) hop and to \(e\)

Old hop:
\[
Z_{\mathrm{hop}}^{(4\mathrm{D})}=\frac{\Delta_{\mathrm{TEP}}\,\Delta t_\tau}{e^2}=\frac{2h}{e^2}=2\,\mathrm{R_K}.
\]
New hop:
\[
\Phi_{\mathrm{5D}}=8\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2,\qquad
Z_0=\mathrm{R_K}\,\Phi_{\mathrm{5D}}=\frac{2h}{e^2}\cdot\alpha_{\mathrm{5D}}\cdot 2
=\frac{h}{e^2}\cdot 8\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2.
\]
**Key:** \(e\) is still in \(\mathrm{R_K}\). The 5D work never produced an ohm without \(e\). It produced \(\alpha\), which was always \(e^2 Z_0/(2h)\).

If one *multiplies* the cell by the 5D hop,
\[
\Phi\;\stackrel{?}{=}\;\Phi_{\mathrm{cell}}\cdot 4\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2,
\]
that is double counting: the cell already assumed a 4D Maxwell hop of size \(2\mathrm{R_K}\). Use one hop or the other.

Preferred statement after this session:
\[
\Phi=\Phi_{\mathrm{5D}}(\varphi_{\mathrm{EM}})
\quad\text{or}\quad
\Phi=\Phi_{\mathrm{cell}}\quad\text{(4D tick hop)},
\]
not the product.

---

## 6. Does this fix \(\alpha_{\mathrm{fs}}\)?

No.

- With \(\varphi\) chosen from the TSB set \(\{\ell_P,r_{\mathrm{M}},R_\tau\}\), \(\alpha_{\mathrm{5D}}\) is \(4\), \(10^{-39}\), or \(10^{-116}\).
- With \(\varphi\) chosen to hit \(\alpha_{\mathrm{fs}}\), the reduction is a rewrite of the target, not a prediction.
- Dilaton kinetics at constant vev do not add a factor.
- Convention \(8\pi\) vs \(16\pi\) moves \(\varphi/\ell_P\) from \(23.4\) to \(\mathcal{O}(10)\), still Planckian, still not \(r_{\mathrm{M}}\).

What *is* fixed relative to yesterday: the claim that only the cell could set \(\Phi\). The 5D hop can, and does, change \(\Phi\) by \(10^{38}\) or \(10^{116}\) if the fibre is \(r_{\mathrm{M}}\) or \(R_\tau\). Those values are empirically excluded. The remaining live option is a Planckian EM fibre coexisting with a femtometre clock. That option is now named. It is not computed from \(E_8\), from \(n_{\mathrm{hier}}\), or from the quark \(V_{\mathrm{orb}}\) sextet.

---

## 7. Direct answer

The 5D Einstein–dilaton reduction replaces
\[
\Phi=\frac{34}{31}
\quad\text{by}\quad
\Phi=8\Bigl(\frac{\ell_P}{\varphi}\Bigr)^2.
\]
That is a change by many orders of magnitude for every TSB radius except a Planckian one. It does not produce \(1/137\) from \(r_{\mathrm{M}}\), \(R_\tau\), \(N_\tau\), or \(E_8\). The only vev that matches CODATA inside the derived prefactor is \(\varphi_{\mathrm{EM}}\approx 23.41\,\ell_P\). Call that the Einstein–dilaton hop if the seed fibre is Planckian; do not call it a derivation of \(\alpha_{\mathrm{fs}}\) from Superblock geometry.

---

## Ledger

| Item | Status |
|---|---|
| Cylinder reduction \(\alpha=4G/\varphi^2\) | Derived, this session |
| Dilaton kinetics change the prefactor at constant \(\varphi\) | False |
| \(\varphi=r_{\mathrm{M}}\) or \(R_\tau\) gives \(\alpha_{\mathrm{fs}}\) | False |
| \(\varphi\approx 23.41\,\ell_P\) gives \(\alpha_{\mathrm{fs}}\) inside this prefactor | True, and tautological |
| \(7\pi\) equals \(23.41\) | False (\(6.4\,\%\)) |
| \(\Phi_{\mathrm{cell}}\times\Phi_{\mathrm{5D}}\) | Rejected (double hop) |
| \(e\) explicit | Held |

---

## Sources

- Cylinder ansatz as in the TSB kinematics / Tav-topology notes
- Standard Kaluza split of \(R_5\) (Maxwell term \(-\varphi^2 F^2/4\)); cf. the historical reduction reviewed in O’Raifeartaigh–Straumann and Overduin–Wesson
- Parent \(\Phi_{\mathrm{cell}}=34/31\); parent \(Z_{\mathrm{hop}}=2h/e^2\)
- PDG / CODATA \(\alpha_{\mathrm{fs}}\)

---

*End of session note — 2026-09-18 5D Einstein–dilaton hop and \(\Phi\).*
