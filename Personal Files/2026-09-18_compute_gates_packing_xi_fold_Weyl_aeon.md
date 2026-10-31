# Session log: Compute the gates, packing fractions, impedance susceptibility, 5D fold, Weyl scars, and aeon-matching jump — in foundational order

- **Session date:** Friday, 2026-09-18
- **Charge:** Compute the remaining items named at the end of the expanding-space scalar summary, in the order that respects dependence.
- **Parents:** `2026-09-17_Expanding_space_geometric_creation_of_Mirrons_via_scalar.md`, `2026-09-17_Z0_of_nM_linear_response.md`, `2026-09-18_two_scalar_action.md`, `2026-09-18_nucleation_current_derivation.md`, `2026-09-18_verbose_summary_expanding_space_via_scalar_mirrons.md`
- **This file:** `Personal Files/2026-09-18_compute_gates_packing_xi_fold_Weyl_aeon.md`
- **Drive folder:** Tau-Superblock Universe / Personal Files
- **Nomenclature:** Mirron, never soliton.

---

## Dependency order (why this sequence)

A quantity is computed only after everything it sits on is either locked or computed.

| Layer | Item | Sits on | Feeds |
|---|---|---|---|
| 0 | Locked geometry | corpus | everything |
| 1 | Local packing efficiency \(f_{\mathrm{geom}}\) | \(\{N_{\mathrm{dom}}=6,r_{\mathrm{M}}\}\) only | local cell, \(\Phi\) models |
| 2 | Mean cosmological density / sparse packing | Layer 1 + \(\Delta_{\mathrm{TEP}}\) + \(\rho_{\mathrm{vac}}\) (data) | \(n_{\mathrm{M}}\), \(\ell_{\mathrm{pack}}\), rest-energy budget |
| 3 | 5D / reduced fold and \(\varphi_{\mathrm{crit}}\) | two-scalar action + Layer 0 (\(r_{\mathrm{M}}=\lambda_{313}\)) | permanence of a new \(\Sigma_{\mathrm{M}}\) |
| 4 | Conformal gate \(\Lambda_{\Omega}\) | fold width + \(R_{\tau}\) + \(N_{\tau}\) | where \(\Gamma\neq 0\) |
| 5 | Impedance susceptibility \(\xi\) | Layer 1 generator models (17 Sep) | Branch A vs B (already decided geometrically) |
| 6 | Void fraction \(f_{\mathrm{void}}\) | Layer 4 wall thickness + Tav scale | \(\Delta N_{\mathrm{M}}\) per Mother Block |
| 7 | Weyl scars | fold energy (Layer 3) + \(\Gamma\) + Layers 2,6 | lensing / ISW kill criterion |
| 8 | Aeon-matching jump | Layers 2–4 + \(\Omega_A\to\Omega_B\) | CCC-style count |

What is **not** claimed: a finished \(E_8\) weight diagram. Phenomenological \(V_{\mathrm{orb}}\) from PDG (this morning) is not used as an input here.

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(r_{\mathrm{M}}=\lambda_{313}=\hbar c/\Delta_{\mathrm{TEP}}\) | Locked clock radius \(\approx 6.302\times 10^{-16}\,\mathrm{m}=0.6302\,\mathrm{fm}\) |
| \(\Delta_{\mathrm{TEP}}\) | TEP floor \(=313.1\,\mathrm{MeV}=5.016\times 10^{-11}\,\mathrm{J}\) |
| \(\ell_P=\sqrt{\hbar G/c^3}\) | Planck length \(\approx 1.616\times 10^{-35}\,\mathrm{m}\) (seed) |
| \(R_{\tau}\) | Tav-cylinder radius \(=7\,h^{-1}\,\mathrm{Mpc}\). With \(h=0.70\): \(10\,\mathrm{Mpc}=3.086\times 10^{23}\,\mathrm{m}\) |
| \(n_{\mathrm{hier}}=\log_7(R_{\tau}/r_{\mathrm{M}})\) | Hierarchical depth \(\approx 45.78\) |
| \(N_{\mathrm{dom}}=6\) | Co-located domains |
| \(N_{\tau}=7\) | Active Tav phases |
| \(N_{\phi}=8\) | Octonionic phases (8th is reset) |
| \(v_{\mathrm{M}}=\tfrac43\pi r_{\mathrm{M}}^3\) | Bookkeeping 3-volume of one equivalent sphere \(\approx 1.049\times 10^{-45}\,\mathrm{m}^3\) |
| \(f=n_{\mathrm{M}} v_{\mathrm{M}}\) | Packing fraction of equivalent spheres |
| \(f_{\mathrm{geom}}\) | Local lattice efficiency (how centres pack when they pack) |
| \(f_{\ast}\) | Cosmological target packing of Branch A |
| \(\ell_{\mathrm{pack}}=n_{\mathrm{M}}^{-1/3}\) | Mean proper spacing |
| \(\varphi_{\mathrm{n}}\) | Dimensionless nucleation / packing stiffness (two-scalar action) |
| \(\varphi_{\tau}\) | Cylinder modulus. Background \(\langle\varphi_{\tau}\rangle=R_{\tau}\) |
| \(\varphi_{\mathrm{crit}}\) | Stiffness gate. Normalized so mean structure sits at \(1\) |
| \(\Omega\) | Conformal factor |
| \(\nu\) | Conformal weight in \(V_{\mathrm{n}}\). Default \(2\) (named integer) |
| \(\mu_{\mathrm{n}}\) | Inverse width of the fold |
| \(\Lambda_{\Omega}\) | Conformal-gradient gate (inverse length) |
| \(\xi=\partial\ln Z_0/\partial\ln n_{\mathrm{M}}\) | Impedance susceptibility |
| \(\Phi\) | Dimensionless impedance, \(Z_0=\mathrm{R_K}\Phi\) |
| \(\Gamma\) | Proper nucleation rate |
| \(f_{\mathrm{void}}\) | Volume fraction that is both soft and on a void wall |
| \(C_{\alpha\beta\gamma\delta}\) | Weyl tensor |
| \(H_0\) | Hubble rate today. \(70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}=2.269\times 10^{-18}\,\mathrm{s^{-1}}\) used for numbers |
| \(\rho_{\mathrm{vac}}\) | Observed dark-energy density. \(\Omega_{\Lambda}=0.69\) at that \(H_0\) gives \(\approx 5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\approx 2.74\times 10^{-47}\,\mathrm{GeV}^4\) |
| \(\mathrm{MB}\) | Mother Block |
| \(\mathrm{SB}_n\) | Daughter Superblock |

---

## Layer 0 — locked inputs (not recomputed)

\[
r_{\mathrm{M}}
=\frac{\hbar c}{\Delta_{\mathrm{TEP}}}
=\frac{197.327\,\mathrm{MeV\cdot fm}}{313.1\,\mathrm{MeV}}
=0.6302\,\mathrm{fm}
=6.302\times 10^{-16}\,\mathrm{m}.
\]

**Key.** Reduced Compton length of the TEP floor. (\(hc/\Delta_{\mathrm{TEP}}\) without the bar is \(2\pi\) larger and is **not** the lock.)

\[
\frac{r_{\mathrm{M}}}{\ell_P}=3.899\times 10^{19},
\qquad
n_{\mathrm{hier}}=\log_7\frac{R_{\tau}}{r_{\mathrm{M}}}=45.78
\quad(h=0.70).
\]

**Key.** One Tav decade is a factor \(7\) in length. Forty-six decades separate the clock from the cylinder.

Two-scalar action (already written today; Maxwell absent):

\[
\mathrm{d}s_5^2
=g_{\mu\nu}\,\mathrm{d}x^{\mu}\mathrm{d}x^{\nu}
+\varphi_{\tau}^2\,\mathrm{d}\theta^2,
\qquad
V_{\mathrm{n}}
=\frac{\mu_{\mathrm{n}}^2}{2}\bigl(\varphi_{\mathrm{n}}-\Omega^{-\nu}\bigr)^2.
\]

**Key.** \(\varphi_{\tau}\) is the cylinder. \(\varphi_{\mathrm{n}}\) is the nucleation switch. They are different fields.

---

## Layer 1 — local packing efficiency \(f_{\mathrm{geom}}\)

**Question.** When engines sit next to each other, what fraction of the cell is the equivalent sphere of radius \(r_{\mathrm{M}}\)?

No second length is allowed. The only dimensionless packing numbers available from TSB integers are the sphere-packings whose coordination matches \(N_{\mathrm{dom}}=6\).

| Lattice | Coordination | \(f_{\mathrm{geom}}\) | \(\ell_{\mathrm{pack}}/r_{\mathrm{M}}\) |
|---|---|---|---|
| Simple cubic (SC) | **6** | \(\pi/6=0.5236\) | \(2\) exactly |
| BCC | 8 | \(\pi\sqrt{3}/8=0.6802\) | \(1.86\) |
| FCC / HCP | 12 | \(\pi/(3\sqrt{2})=0.7405\) | \(1.782\) |

**TSB-integer choice.** Coordination \(6\) is the lock. Local packing is simple cubic:

\[
f_{\mathrm{geom}}
=\frac{\pi}{6}
\approx 0.5236,
\qquad
\ell_{\mathrm{pack}}^{\mathrm{(loc)}}
=2\,r_{\mathrm{M}}
=1.260\times 10^{-15}\,\mathrm{m}.
\]

**Key.** \(f_{\mathrm{geom}}\) is an *efficiency*, not a cosmological filling fraction. It answers “how do neighbouring engines sit,” not “how many engines fill the Hubble volume.”

**Plain language.** Six domains, six neighbours. The engines, when they pack at all, sit on a cubic lattice with one diameter of empty space between centres. That is the local tile, not the sky.

FCC remains the *upper bound* on local efficiency (\(0.7405\)). Nothing in TSB integers prefers 12-coordination.

---

## Layer 2 — cosmological packing \(f_{\ast}\) (the rest-energy veto)

**Question.** Can the *mean* vacuum be the Layer-1 lattice?

Close-packed SC density:

\[
n_{\mathrm{M}}^{\mathrm{SC}}
=\frac{f_{\mathrm{geom}}}{v_{\mathrm{M}}}
=4.99\times 10^{44}\,\mathrm{m}^{-3}.
\]

Rest-energy density if every engine costs \(\Delta_{\mathrm{TEP}}\):

\[
n_{\mathrm{M}}^{\mathrm{SC}}\,\Delta_{\mathrm{TEP}}
\sim 10^{34}\,\mathrm{J\,m^{-3}}
\sim 10^{17}\,\mathrm{kg\,m^{-3}}.
\]

That is nuclear density, not the vacuum. **Layer-1 packing is forbidden as the cosmological mean.** A second length *must* enter: the mean spacing of engines in empty space.

Two geometric closures that do not invent a new constant.

### Closure C0 — no cancellation (each engine’s \(\Delta_{\mathrm{TEP}}\) *is* the vacuum energy)

Demand \(n_{\mathrm{M}}\Delta_{\mathrm{TEP}}=\rho_{\mathrm{vac}}\):

\[
n_{\mathrm{M}}^{(0)}
=\frac{\rho_{\mathrm{vac}}}{\Delta_{\mathrm{TEP}}}
=11.38\,\mathrm{m}^{-3},
\qquad
\ell_{\mathrm{pack}}^{(0)}
=0.445\,\mathrm{m},
\qquad
f_{\ast}^{(0)}
=n_{\mathrm{M}}^{(0)} v_{\mathrm{M}}
=1.19\times 10^{-44}.
\]

**Key.** \(\rho_{\mathrm{vac}}\) is *data* here (\(\Omega_{\Lambda}h^2\)), not a TSB output. C0 *uses* dark energy to set the mean density; it does not explain it.

Hierarchical check: \(r_{\mathrm{M}}\times 7^{18}=1.03\,\mathrm{m}\), \(r_{\mathrm{M}}\times 7^{17}=0.147\,\mathrm{m}\). The C0 spacing sits **between Tav decades 17 and 18**, next to a laboratory metre. That is a coincidence until someone derives why decade 18 is preferred. It is recorded, not sold as a derivation.

### Closure C6 — six-domain cancellation with a Tav residual

Suppose the six co-located domains cancel the leading rest energy and leave a residual \(\Xi\). Then

\[
n_{\mathrm{M}}\,\Delta_{\mathrm{TEP}}\,\Xi
=\rho_{\mathrm{vac}}.
\]

The only TSB-integer residuals at the domain / phase count are

| Residual \(\Xi\) | Origin | \(n_{\mathrm{M}}\,(\mathrm{m}^{-3})\) | \(\ell_{\mathrm{pack}}\) |
|---|---|---|---|
| \(7^{-6}=8.50\times 10^{-6}\) | one Tav factor per domain | \(1.34\times 10^{6}\) | \(9.1\,\mathrm{mm}\) |
| \(6^{-4}=7.72\times 10^{-4}\) | four powers of domain count | \(1.47\times 10^{4}\) | \(4.1\,\mathrm{cm}\) |
| \(6^{-6}=2.14\times 10^{-5}\) | six powers of domain count | \(5.31\times 10^{5}\) | \(1.2\,\mathrm{cm}\) |

All three are still laboratory-scale spacings, not nuclear and not megaparsec. None is derived from an overlap integral on \(S^3\) in this session; they are the integer candidates.

**Working lock for later layers.** Use C0 as the *conservative* mean (\(n_{\mathrm{M}}=11.4\,\mathrm{m}^{-3}\)), and quote C6 as a band. Local encounters still use Layer-1 SC when two engines actually touch.

**Plain language.** The vacuum is not a nuclear crystal of 0.63 fm mirrors. If it were, it would weigh like a neutron star. The engines are sparse: a handful to a million per cubic metre, centimetres to half a metre apart. The *local* tile is still a 1.26 fm cube when two of them meet.

---

## Layer 3 — the fold, and the value of \(\varphi_{\mathrm{crit}}\)

### 3.1 Width from the locked radius

The fold that writes one \(\Sigma_{\mathrm{M}}\) has one available width: \(r_{\mathrm{M}}\). In the two-scalar action that sets

\[
\mu_{\mathrm{n}}
=\frac{\hbar c}{r_{\mathrm{M}}}
=\Delta_{\mathrm{TEP}}.
\]

**Key.** \(\mu_{\mathrm{n}}\) is an energy (or an inverse length in \(\hbar=c=1\)). It is not a new parameter. The inverse width *is* the TEP floor.

### 3.2 Gate \(\varphi_{\mathrm{crit}}\) from the potential

Equilibrium of \(V_{\mathrm{n}}\):

\[
\varphi_{\mathrm{n}}=\Omega^{-\nu}.
\]

Mean structure is defined to be \(\Omega=1\), so \(\langle\varphi_{\mathrm{n}}\rangle=1\). The stiffness gate in the nucleation current note is \(\varphi_{\mathrm{n}}<1\). Therefore

\[
\varphi_{\mathrm{crit}}=1
\]

in the normalization already chosen for \(V_{\mathrm{n}}\). That is a **computed convention**, not a floating number: any other \(\varphi_{\mathrm{crit}}\) can be absorbed into the definition of \(\varphi_{\mathrm{n}}\).

What *is* physical is the combination that fires the gate. With \(\nu=2\),

\[
\varphi_{\mathrm{n}}<\varphi_{\mathrm{crit}}
\;\Longleftrightarrow\;
\Omega>1.
\]

**Key.** Every region with conformal factor above the mean-structure value is soft enough to fold. Voids (\(\Omega>1\) in the void-slicing of the two-scalar note) pass the stiffness gate; bound structure (\(\Omega\le 1\)) fails it.

**Plain language.** We named the hardness of mean structure “one.” A void is zoomed larger than mean structure, so its target hardness drops below one, and the fabric is allowed to crease. That is the whole stiffness gate.

### 3.3 Fold profile and on-shell cost

The 1-D kink of \(V_{\mathrm{n}}\) with \(\Omega\) treated as a slow background is

\[
\varphi_{\mathrm{n}}(r)
=1-\frac{\Delta\varphi}{2}\Bigl(1+\tanh\frac{r-r_0}{r_{\mathrm{M}}}\Bigr),
\qquad
\Delta\varphi=1-\Omega^{-\nu}.
\]

**Key.** \(r\) proper radial coordinate; \(r_0\) wall; \(\Delta\varphi\) is \(\mathcal{O}(1)\) on a developed void (\(\Omega\sim\mathrm{few}\)).

This is now an Euler–Lagrange profile of the *named* potential, not a decorative \(\mathrm{sech}^2\). (The \(\mathrm{sech}^2\) of 17 Sep is the derivative of this \(\tanh\), i.e. the same kink.)

Energy of one 3-D fold of size \(r_{\mathrm{M}}\) and scale \(\mu_{\mathrm{n}}=\Delta_{\mathrm{TEP}}\):

\[
E_{\mathrm{fold}}
\sim \Delta_{\mathrm{TEP}}.
\]

**Key.** One new engine costs one TEP quantum. That matches the rest-energy term \(-n_{\mathrm{M}}\Delta_{\mathrm{TEP}}\) already in \(S_{\mathrm{n}}\). No second energy appears.

Euclidean action in units \(\hbar=1\), schematic 4D instanton of radius \(r_{\mathrm{M}}\):

\[
\frac{S_{\mathrm{E}}}{\hbar}
\sim \kappa_{\mathrm{n}}\,\bigl(\Delta\varphi\bigr)^2
\sim \mathcal{O}(1).
\]

**Key.** \(\kappa_{\mathrm{n}}=\mathcal{O}(1)\) from the two-scalar note. Because the width is the Compton length of the only energy in the problem, the instanton is **not** Planck-suppressed. \(S_{\mathrm{E}}/\hbar\sim(r_{\mathrm{M}}/\ell_P)^p\) would have been \(10^{19p}\) and would have forbidden nucleation forever. That suppression does **not** appear: \(\ell_P\) is the 5D seed, not the fold width.

**Honesty.** This is a 4D reduction estimate. A genuine 5D Einstein–Kaluza–Klein instanton on \(\mathrm{d}s_5^2\) with a pinching \(\varphi_{\tau}\) is **not** solved. What is computed is the reduced fold that the two-scalar action actually contains.

### 3.4 Permanence

The fold stays if the background target remains below \(1\) after the event (void stays a void). It dissolves if Hierarchical Binding or collapse restiffens \(\varphi_{\mathrm{n}}\) above \(1\). That is already the selection rule of 17 Sep, now attached to \(V_{\mathrm{n}}\).

---

## Layer 4 — conformal gate \(\Lambda_{\Omega}\)

The second Heaviside is \(\lvert\nabla\log\Omega\rvert>\Lambda_{\Omega}\). Three candidate inverse lengths live in Layer 0. Only one belongs to void walls.

| Candidate | Value | What it would select |
|---|---|---|
| \(1/r_{\mathrm{M}}\) | \(1.59\times 10^{15}\,\mathrm{m}^{-1}\) | only nuclear-sharp creases; cosmic walls fail |
| \(H_0/c\) | \(7.57\times 10^{-27}\,\mathrm{m}^{-1}\) | Hubble-length “walls”; the gate is always on |
| \(N_{\tau}/R_{\tau}=7/R_{\tau}\) | \(2.27\times 10^{-23}\,\mathrm{m}^{-1}\) | walls thinner than \(R_{\tau}/7=1.43\,h^{0}\,\mathrm{Mpc}\) |

**Geometric choice.** The cylinder is the largest coherent conformal cell. One Tav step down is the natural wall scale of the cosmic web (filament / wall thickness versus void diameter). Therefore

\[
\Lambda_{\Omega}
=\frac{N_{\tau}}{R_{\tau}}
=\frac{7}{R_{\tau}}
=\frac{1}{1.43\,h^{-1}\,\mathrm{Mpc}}.
\]

**Key.** \(N_{\tau}=7\) and \(R_{\tau}=7\,h^{-1}\,\mathrm{Mpc}\) are corpus locks. Their ratio is a derived inverse length, not a fit.

A spherical void of radius \(R_{\mathrm{void}}\sim R_{\tau}\) with a conformal drop of order one across a wall of thickness \(\delta\) has

\[
\lvert\nabla\log\Omega\rvert
\sim\frac{1}{\delta}.
\]

The gate fires when \(\delta<R_{\tau}/7\). Observed cosmic-web walls are of that order (megaparsec, not gigaparsec and not fermi). The gate is then *open on real walls and closed in homogeneous FLRW*, which is exactly the 17 Sep requirement.

**Plain language.** The crease has to be sharper than one-seventh of a Tav circle. That is a typical wall of the cosmic web. Smooth Hubble flow is not sharp enough. A proton-sized wrinkle is sharper than necessary and is not what this gate is for (that is the fold width, already used).

---

## Layer 5 — impedance susceptibility \(\xi\)

From 17 Sep, once \(c\) is locked, \(Z_0=\mathrm{R_K}\Phi(f)\) and \(\xi=\mathrm{d}\ln\Phi/\mathrm{d}\ln n_{\mathrm{M}}\). Generator models with no Maxwell host:

| Model | What sets \(V\) and \(I\) | \(\xi\) |
|---|---|---|
| G1′ | cell voltage and cell current (self-similar lattice) | \(0\) |
| G1 raw | cell voltage, engine current | \(+1/3\) |
| G2 / G3-engine | engine voltage, cell-face current | \(-1/3\) |
| Coax log (wrong geometry) | TEM wire | \(-1/(3\ln(\ell/r_{\mathrm{M}}))\) |

Layer 2 says the *cosmological* lattice is self-similar across Tav decades (\(\ell_{\mathrm{pack}}\gg r_{\mathrm{M}}\), \(f_{\ast}\sim 10^{-44}\)). The only generator that does not introduce a preferred ratio \(\ell_{\mathrm{pack}}/r_{\mathrm{M}}\) into \(\Phi\) at leading order is G1′:

\[
\xi^{(0)}=0.
\]

**Key.** At the sparse cosmological packing, \(\ell_{\mathrm{pack}}/r_{\mathrm{M}}\sim 7^{18}\approx 1.6\times 10^{15}\). G2 would then give \(\Phi\sim 10^{15}\) and a nonsense \(Z_0\). G2 is a *contact* model (macro \(H\) diluted over a cell comparable to \(r_{\mathrm{M}}\)). It does not apply to the sparse vacuum. Contact physics still uses Layer-1 SC, where G2 and G1 raw live, but that is not the mean vacuum.

Atomic-clock bound (17 Sep): if Branch B diluted \(n_{\mathrm{M}}\propto a^{-3}\), then \(\lvert\xi\rvert\lesssim 5\times 10^{-9}\) is required. G1′ satisfies that with room to spare. G2 at \(\xi=-1/3\) is incompatible with Branch B.

**Decision, now with a computed \(\xi\).**

- Mean vacuum: \(\xi=0\) (G1′). Clocks do **not** by themselves kill Branch B.
- Branch A is still required by the *geometric* packing constraint of the nucleation-current note: \(r_{\mathrm{M}}\) frozen, volume growing, target \(f_{\ast}\) a constant of motion on the support of the gates. That argument never used \(\xi\).
- Branch B remains a live control *only* if one is willing to let \(f_{\ast}\) thin and to accept a changing mean lattice. TSB does not.

**Plain language.** Spreading the engines farther apart does not change the ohm of the vacuum at leading order, because each cell looks like a scaled copy of itself. We still add engines as space grows, not because the ohm would drift, but because the tile size is frozen and the floor keeps getting bigger.

---

## Layer 6 — void fraction \(f_{\mathrm{void}}\)

Wall thickness at the gate:

\[
\delta_{\mathrm{wall}}
=\frac{1}{\Lambda_{\Omega}}
=\frac{R_{\tau}}{7}
=1.43\,h^{-1}\,\mathrm{Mpc}.
\]

A Mother Block of characteristic radius \(R_{\mathrm{MB}}\sim R_{\tau}\) (one Tav cell) modelled as a spherical void plus a wall:

\[
f_{\mathrm{void}}
=1-\Bigl(1-\frac{\delta_{\mathrm{wall}}}{R_{\mathrm{MB}}}\Bigr)^3
=1-\Bigl(1-\frac{1}{7}\Bigr)^3
=1-\Bigl(\frac{6}{7}\Bigr)^3
=\frac{127}{343}
\approx 0.370.
\]

**Key.** \(\delta/R=1/7=N_{\tau}^{-1}\). The fraction is a pure TSB rational.

If the Mother Block is a *cube* of side \(2R_{\tau}\) with walls of thickness \(R_{\tau}/7\) on all six faces (no double-counting of edges to leading order),

\[
f_{\mathrm{void}}^{\mathrm{(cube)}}
\approx 6\cdot\frac{1}{7}\cdot\frac{1}{2}
=\frac{3}{7}
\approx 0.429
\]

(the extra \(1/2\) is “half the wall belongs to this cell”). Same decade.

**Working lock.**

\[
f_{\mathrm{void}}
=\frac{127}{343}\approx 0.370.
\]

Branching count per Hubble time per Mother Block, from 17 Sep:

\[
\Delta N_{\mathrm{M}}
\simeq
3\,n_{\mathrm{M}} V_{\mathrm{MB}} f_{\mathrm{void}}.
\]

With C0 and \(V_{\mathrm{MB}}\sim\tfrac43\pi R_{\tau}^3\):

\[
V_{\mathrm{MB}}
\approx 4.19\times 10^{3}\,\mathrm{Mpc}^3
=1.23\times 10^{71}\,\mathrm{m}^3,
\qquad
n_{\mathrm{M}} V_{\mathrm{MB}}
\approx 1.40\times 10^{72},
\qquad
\Delta N_{\mathrm{M}}
\approx 1.55\times 10^{72}.
\]

**Key.** That is the number of new *clock-scale* engines written on the walls of one Tav cell per Hubble time, under C0. Hierarchical Binding then maps clusters of those engines up to Superblock images. It is **not** the number of new megaparsec Superblocks. Dividing by the number of engines per image (\(\sim 7^{3\Delta n}\) for a jump of \(\Delta n\) decades) is a separate count and is not performed here.

**Plain language.** About 37 percent of a Tav cell is “wall enough” to crease. That fraction is \(1-(6/7)^3\), not a fit. Most of the new engines appear in that skin.

---

## Layer 7 — Weyl scars

### 7.1 One fold

A rest energy \(\Delta_{\mathrm{TEP}}\) localized at scale \(r_{\mathrm{M}}\) has Schwarzschild radius

\[
r_s
=\frac{2G(\Delta_{\mathrm{TEP}}/c^2)}{c^2}
\approx 8.3\times 10^{-54}\,\mathrm{m}.
\]

Dimensionless potential at the fold:

\[
\frac{r_s}{r_{\mathrm{M}}}
\approx 1.3\times 10^{-38}.
\]

Weyl scale (one derivative per length):

\[
\lvert C\rvert_{\mathrm{fold}}
\sim\frac{r_s}{r_{\mathrm{M}}^3}
\approx 3\times 10^{-8}\,\mathrm{m}^{-2}.
\]

**Key.** The scar is Planck-feeble at the clock scale. It is not a curvature catastrophe.

### 7.2 Cosmological injection (C0, walls only)

\[
\Gamma
=3H n_{\mathrm{M}} f_{\mathrm{void}}
\approx 3\times(2.27\times 10^{-18})\times 11.38\times 0.370
\approx 2.9\times 10^{-17}\,\mathrm{m}^{-3}\,\mathrm{s}^{-1}.
\]

**Key.** Rate is per proper volume of the Mother Block, with the gate fraction already inserted.

Rest-energy injection:

\[
\Gamma\,\Delta_{\mathrm{TEP}}
\approx 1.4\times 10^{-27}\,\mathrm{J\,m^{-3}\,s^{-1}}.
\]

Over one Hubble time \(H^{-1}\approx 4.4\times 10^{17}\,\mathrm{s}\):

\[
(\Gamma\,\Delta_{\mathrm{TEP}})H^{-1}
\approx 6\times 10^{-10}\,\mathrm{J\,m^{-3}}
\sim\rho_{\mathrm{vac}}.
\]

**Key.** Under C0 this is a tautology: C0 *defined* \(n_{\mathrm{M}}\Delta_{\mathrm{TEP}}=\rho_{\mathrm{vac}}\), and \(\Gamma=3H n_{\mathrm{M}} f_{\mathrm{void}}\) then deposits \(\sim 3 f_{\mathrm{void}}\rho_{\mathrm{vac}}\) per Hubble time. With \(3f_{\mathrm{void}}\approx 1.1\), the wall engine is depositing vacuum-scale energy at vacuum-scale rate. That is consistent bookkeeping, not an independent prediction of \(\rho_{\mathrm{vac}}\).

### 7.3 Lensing / ISW

A population of scars of radius \(r_{\mathrm{M}}\) and amplitude \(10^{-38}\), even at \(n_{\mathrm{M}}\sim 10\,\mathrm{m}^{-3}\), has volume filling \(n_{\mathrm{M}}v_{\mathrm{M}}\sim 10^{-44}\). The sky-averaged Weyl from the *micro* scars is

\[
\langle\lvert C\rvert\rangle
\sim n_{\mathrm{M}} v_{\mathrm{M}}\cdot\lvert C\rvert_{\mathrm{fold}}
\sim 10^{-52}\,\mathrm{m}^{-2},
\]

which is many decades below cosmological Weyl (\(\sim H_0^2/c^2\sim 10^{-52}\,\mathrm{m}^{-2}\) actually — wait:

\(H_0/c=7.57\times 10^{-27}\,\mathrm{m}^{-1}\), \((H_0/c)^2=5.7\times 10^{-53}\,\mathrm{m}^{-2}\).

So \(\langle\lvert C\rvert\rangle_{\mathrm{micro}}\sim 10^{-52}\,\mathrm{m}^{-2}\) is the same *order* as the background cosmological curvature scale. That is uncomfortably close for a back-of-envelope, but the micro scars oscillate on fermi scales and do not source a coherent megaparsec lensing potential. Weak lensing and ISW see the Hierarchical Binding *images*, not the raw folds.

**Kill criterion, restated and not fired.** Overproduction would be a *coherent* wall Weyl of order the wall’s own \(\Delta H/c\) extra, on top of GR. The micro calculation does not show that. A wall-scale metric calculation (junction condition on \(\delta_{\mathrm{wall}}\)) is **not** done in this session. Status of S11: micro scars are safe; wall-scale scars remain open.

**Plain language.** Each new crease is a gravitational dimple \(10^{-38}\) deep and 0.63 fm wide. You will not see those dimples in a galaxy lens. What you might see is their magnified images on void walls. That magnified budget is the remaining Weyl homework.

---

## Layer 8 — aeon-matching jump

Penrose matching: \(\Omega_A\to 0\) at future conformal infinity of aeon \(A\), reset to \(\Omega_B\approx 1\) at the start of aeon \(B\).

During the intra-aeon history the stiffness gate is \(\Omega>1\) in voids. At the matching surface \(\Omega\) is driven through zero and reset. That is not a small gradient. \(\lvert\nabla\log\Omega\rvert\) diverges at a sharp matching (or is at least \(\gg\Lambda_{\Omega}\) on any finite-thickness crossover). Both gates slam open.

The packing field is reset from whatever late-time \(f_{\ast}\) it held to the *initial* packing of the next aeon. The jump in count inside one comoving cell that survives the conformal map is

\[
\Delta N_{\mathrm{M}}\Big|_{\mathrm{aeon}}
=N_{\mathrm{M}}^{(B)}(t_{\mathrm{init}})
-N_{\mathrm{M}}^{(A)}(t_{\mathrm{end}}).
\]

CCC matching identifies the conformal 3-geometry, not the proper 3-volume. Proper volume is rewritten by \(\Omega\). Because \(r_{\mathrm{M}}\) is a proper clock and does not scale with \(\Omega\), a conformal rescaling that sends \(\Omega_A\to 0\) *creates proper room* the same way Hubble expansion does, but globally and once.

Schematic: if the matching multiplies proper volume by a factor \(X_{\Omega}\), Branch A on the matching surface writes

\[
\Delta N_{\mathrm{M}}\Big|_{\mathrm{aeon}}
=(X_{\Omega}-1)\,N_{\mathrm{M}}^{(A)}(t_{\mathrm{end}}).
\]

**Key.** \(X_{\Omega}\) is the proper-volume jump of the matching. In textbook CCC the 3-metric is finite and the volume jump is absorbed into the conformal factor’s reset, so \(X_{\Omega}\) is a convention unless one specifies which metric is “proper” for \(r_{\mathrm{M}}\).

TSB lock: \(r_{\mathrm{M}}\) is proper in the Prime-domain Einstein frame \(g_{\mu\nu}=\Omega^2\hat g_{\mu\nu}\). The unphysical \(\hat g\) stays finite. Proper Prime volume \(\propto\Omega^3\sqrt{\hat\gamma}\). Sending \(\Omega_A\to 0\) *shrinks* proper Prime volume to zero before the reset — that is the wrong direction for creating room.

The TSB reading that is consistent with “a Mirron is a sub-quantum reflection of an entire aeon” is the opposite orientation: each surviving \(\hat g\)-cell of aeon \(A\) is *copied* onto a new Prime-frame cell of aeon \(B\) at \(\Omega_B=1\), so

\[
N_{\mathrm{M}}^{(B)}(t_{\mathrm{init}})
=N_{\hat\gamma}^{(A)}(t_{\mathrm{end}}).
\]

The jump is then “one new clock-scale engine per conformal cell of the previous aeon,” i.e. the definition of a Mirron as an aeon-reflection. That is a **countable** jump, as required, but it is a definitional identification until the matching 3-geometry is written with \(\Sigma_{\mathrm{M}}\) marked on it.

**What is computed.** Both gates open at matching; nucleation is allowed everywhere on the crossover; the jump is not a Hubble replenishment. **What is not computed.** The integer \(X_{\Omega}\) from a solved conformal matching with Mirrons drawn on the 3-geometry.

**Plain language.** At the end of a cosmic cycle the zoom is wound all the way down and then stamped back at one. That stamp is allowed to write new mirrors everywhere, not just on walls. How many new mirrors the stamp writes is the same question as “how many conformal cells did the last aeon have?” We have the question in TSB variables. We do not have the stamped 3-geometry.

---

## Numbers, collected

| Quantity | Value | Status |
|---|---|---|
| \(r_{\mathrm{M}}\) | \(6.302\times 10^{-16}\,\mathrm{m}\) | locked |
| \(\mu_{\mathrm{n}}\) | \(\Delta_{\mathrm{TEP}}=313.1\,\mathrm{MeV}\) | computed (width = clock) |
| \(\varphi_{\mathrm{crit}}\) | \(1\) | computed (normalization of \(V_{\mathrm{n}}\)) |
| stiffness gate | \(\Omega>1\) (\(\nu=2\)) | computed |
| \(\Lambda_{\Omega}\) | \(7/R_{\tau}=1/(1.43\,h^{-1}\,\mathrm{Mpc})\) | computed |
| \(f_{\mathrm{geom}}\) (local SC) | \(\pi/6\approx 0.5236\) | computed from \(N_{\mathrm{dom}}=6\) |
| \(f_{\ast}^{(0)}\) (C0 mean) | \(1.19\times 10^{-44}\) | computed from \(\rho_{\mathrm{vac}}\) as data |
| \(n_{\mathrm{M}}^{(0)}\) | \(11.4\,\mathrm{m}^{-3}\) | C0 |
| \(\ell_{\mathrm{pack}}^{(0)}\) | \(0.445\,\mathrm{m}\) | C0; sits near Tav decade 18 |
| \(\xi^{(0)}\) | \(0\) | computed (G1′ at sparse packing) |
| \(f_{\mathrm{void}}\) | \(127/343\approx 0.370\) | computed |
| \(E_{\mathrm{fold}}\) | \(\sim\Delta_{\mathrm{TEP}}\) | computed (reduced) |
| \(S_{\mathrm{E}}/\hbar\) | \(\mathcal{O}(1)\), not Planck-suppressed | computed (reduced) |
| \(r_s/r_{\mathrm{M}}\) | \(\sim 10^{-38}\) | computed |
| wall-scale Weyl | open | **not** computed |
| aeon jump \(X_{\Omega}\) | open | identification only |

---

## What remains after this session

1. **5D pinching instanton** of \(\varphi_{\tau}\) on \(\mathrm{d}s_5^2\), not only the 4D \(\varphi_{\mathrm{n}}\) kink. Layer 3 is a reduction.
2. **\(S^3\) overlap integral** that would replace C0’s use of \(\rho_{\mathrm{vac}}\) as data with a derived \(\Xi\). C6 candidates (\(7^{-6}\), \(6^{-4}\), \(6^{-6}\)) are integers looking for an integral.
3. **Why decade 18.** C0 spacing \(\approx 0.45\,\mathrm{m}\) is adjacent to \(r_{\mathrm{M}}7^{18}\). Not derived.
4. **Wall-scale junction Weyl** (the real S11 kill test).
5. **Matching 3-geometry** with \(\Sigma_{\mathrm{M}}\) marked, so \(X_{\Omega}\) is a number.
6. **\(E_8\) projection** of domain angles. Not used, still missing.

---

## Direct answer

Computed, in order, from the locked clock and the two-scalar action:

- Local tile: simple-cubic, \(f_{\mathrm{geom}}=\pi/6\), spacing \(2r_{\mathrm{M}}\).
- Mean vacuum: **not** that tile. Conservative C0 gives eleven engines per cubic metre, half-metre spacing, packing \(10^{-44}\). Nuclear packing is a neutron-star vacuum and is vetoed.
- Fold width is the clock; \(\mu_{\mathrm{n}}=\Delta_{\mathrm{TEP}}\); \(\varphi_{\mathrm{crit}}=1\); voids (\(\Omega>1\)) are the soft side.
- Conformal gate is one Tav step below the cylinder: \(\Lambda_{\Omega}=7/R_{\tau}\). Real cosmic-web walls pass; homogeneous FLRW fails.
- Mean-vacuum \(\xi=0\). Branch A is still required by frozen \(r_{\mathrm{M}}\), not by the ohm.
- Wall fraction \(127/343\).
- Micro Weyl scars are \(10^{-38}\) deep and do not lens. Wall-scale scars and the aeon stamp-count are the two items that remain genuinely uncomputed rather than named.

The idea is no longer a list of open symbols. It is a list of six computed rationals and lengths, plus two calculations (5D instanton, matching 3-geometry) that the reduced theory does not contain.

---

*End of session — 2026-09-18 compute gates / packing / ξ / fold / Weyl / aeon.*
