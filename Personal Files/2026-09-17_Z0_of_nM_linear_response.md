# Session log: Linear-response derivation of \(Z_0(n_{\mathrm{M}})\)

- **Session date:** Thursday, 2026-09-17
- **Question:** Derive \(Z_0(n_{\mathrm{M}})\).
- **Short answer:** In SI, \(Z_0=1/(\varepsilon_0 c)=\mu_0 c\). TSB locks \(c\) to a *single-engine* chord, so the density dependence lives in the dimensionless factor \(\Phi\) of \(Z_0=(h/e^2)\,\Phi(f)=\mathrm{R_K}\,\Phi(f)\), with packing fraction \(f=n_{\mathrm{M}}\cdot\tfrac{4}{3}\pi r_{\mathrm{M}}^3\). Mirrons are the *generators* of Maxwell, not PEC impurities in a Maxwell host (a suspension of 0.63 fm mirrors at nuclear density would be opaque; the sky is not). That kills ordinary Maxwell–Garnett as the leading picture and kills yesterday’s crude claim that dilution “thins \(Z_0\) at order unity.” Two generator models remain: (G1) charging energy set by the cell, \(\Phi\) independent of \(n_{\mathrm{M}}\) at leading order, \(\xi=0\); (G2) charging energy set by \(r_{\mathrm{M}}\), \(\Phi\propto n_{\mathrm{M}}^{-1/3}\), \(\xi=-1/3\). Because \(\alpha_{\mathrm{fs}}=e^2 Z_0/(2h)= \Phi/2\), atomic-clock bounds \(|\dot\alpha/\alpha|\lesssim 10^{-18}\,\mathrm{yr}^{-1}\) force \(|\xi|\lesssim 5\times 10^{-9}\) *if* \(n_{\mathrm{M}}\) dilutes as \(a^{-3}\). Branch B with \(\mathcal{O}(1)\) susceptibility is ruled out. Branch A (nucleation keeps \(n_{\mathrm{M}}\) fixed) is the only option compatible with both a non-tiny \(\xi\) and the clocks. The SI number \(376.73\,\Omega\) is *not* produced by this calculation; it is equivalent to producing \(\alpha_{\mathrm{fs}}\) once \(e\) and \(h\) are given.
- **This file:** `Personal Files/2026-09-17_Z0_of_nM_linear_response.md`
- **Companion:** `Personal Files/2026-09-17_Expanding_space_geometric_creation_of_Mirrons_via_scalar.md`
- **Nomenclature:** Mirron, never soliton.

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(Z_0\) | Observed vacuum wave impedance. CODATA: \(Z_0=\sqrt{\mu_0/\varepsilon_0}\approx 376.730\,\Omega\). |
| \(\varepsilon_0\) | Observed vacuum permittivity \(\approx 8.854\times 10^{-12}\,\mathrm{F\,m^{-1}}\). |
| \(\mu_0\) | Observed vacuum permeability \(\approx 1.257\times 10^{-6}\,\mathrm{N\,A^{-2}}\). |
| \(c\) | Observed macroscopic invariant speed. Also the TSB operational clock speed \(c=\alpha r_{\mathrm{M}}/\Delta t_{\tau}\) when those two are identified. |
| \(c_{\mathrm{ph}}\) | Long-wavelength phase velocity of a Maxwell wave in an effective medium. May differ from the clock speed if Mirrons are treated as impurities. |
| \(n_{\mathrm{M}}\) | Proper number density of Mirrons. |
| \(r_{\mathrm{M}}\) | Proper Mirron radius. Lock: \(\lambda_{313}=hc/\Delta_{\mathrm{TEP}}\approx 6.302\times 10^{-16}\,\mathrm{m}\). |
| \(\ell_{\mathrm{pack}}=n_{\mathrm{M}}^{-1/3}\) | Mean proper inter-Mirron spacing. |
| \(f=n_{\mathrm{M}}\cdot\tfrac{4}{3}\pi r_{\mathrm{M}}^3\) | Geometric packing fraction of equivalent spheres. \(f\le f_{\mathrm{max}}\approx 0.74\) (HCP/FCC). |
| \(f_{\mathrm{geom}}\) | Lattice packing efficiency from E₈ / six-domain geometry (not yet computed; \(\mathcal{O}(1)\) placeholder). |
| \(\Sigma_{\mathrm{M}}\) | Mirron 2-surface. |
| \(\chi_{\mathrm{M}}\) | Presence / packing field. |
| \(\Delta t_{\tau}\) | Tav tick. Recommended freeze: diameter bounce \(2r_{\mathrm{M}}/c\). |
| \(\alpha\in\{2,2\pi,2\pi/7\}\) | Chord factor of one tick (not the fine-structure constant). |
| \(\alpha_{\mathrm{fs}}\) | Fine-structure constant \(\approx 1/137.036\). Identity: \(\alpha_{\mathrm{fs}}=e^2 Z_0/(2h)\). |
| \(e\) | Elementary charge (SI defining constant since 2019: \(1.602176634\times 10^{-19}\,\mathrm{C}\)). |
| \(h\) | Planck constant (SI defining: \(6.62607015\times 10^{-34}\,\mathrm{J\,s}\)). |
| \(\hbar=h/2\pi\) | Reduced Planck constant. |
| \(\mathrm{R_K}=h/e^2\) | von Klitzing constant \(\approx 25812.807\,\Omega\). |
| \(\Phi(f)\) | Dimensionless impedance function. \(Z_0=\mathrm{R_K}\,\Phi(f)\). |
| \(\xi\) | Density susceptibility \(\xi=\partial\ln Z_0/\partial\ln n_{\mathrm{M}}=\mathrm{d}\ln\Phi/\mathrm{d}\ln n_{\mathrm{M}}\). |
| \(\tilde\alpha_E,\tilde\alpha_M\) | Dimensionless electric / magnetic polarizabilities of one Mirron in a *host* picture (used only as a rejected control). |
| \(\varepsilon_r,\mu_r\) | Relative permittivity / permeability of an effective medium versus a host. |
| \(P_i\) | Macroscopic polarization. |
| \(M_i\) | Macroscopic magnetization. |
| \(K^a\) | Surface current on \(\Sigma_{\mathrm{M}}\). |
| \(q_{\mathrm{eff}}\) | Effective charge participating in one engine refresh (taken \(=e\) unless stated). |
| \(E_{\mathrm{charge}}\) | Energy to place charge \(e\) on one cell or one Mirron. |
| \(C_{\mathrm{cell}},L_{\mathrm{cell}}\) | Equivalent capacitance and inductance of one packing cell. |
| \(\Delta_{\mathrm{TEP}}\) | TEP floor \(\approx 313.1\,\mathrm{MeV}\). |
| \(\lambda_{313}=hc/\Delta_{\mathrm{TEP}}\) | Compton length of that floor. |
| \(H=\dot a/a\) | Hubble rate. \(H_0\approx 7.1\times 10^{-11}\,\mathrm{yr}^{-1}\) for \(H_0\approx 70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\). |
| \(a(t)\) | Scale factor. |
| \(\Gamma\) | Mirron nucleation rate (previous session). |
| \(\zeta\) | Superlubricant / lossless-interface parameter of \(\Sigma_{\mathrm{M}}\). \(\zeta\to 1\) is ideal. |
| \(\mathrm{PEC}\) | Perfect electric conductor (control model, not TSB). |
| \(n=c_{\mathrm{host}}/c_{\mathrm{ph}}\) | Refractive index of a suspension (control model). |

---

## 1. What can be derived, and what cannot

Three different objects are easy to confuse.

**Identity A (Maxwell, SI).**
\[
c=\frac{1}{\sqrt{\varepsilon_0\mu_0}},\qquad
Z_0=\sqrt{\frac{\mu_0}{\varepsilon_0}}=\frac{1}{\varepsilon_0 c}=\mu_0 c.
\]
**Key:** \(\varepsilon_0,\mu_0,c,Z_0\) as in the table. These are two relations among four quantities. Any two determine the other two.

**Identity B (SI + quantum charge).**
\[
\alpha_{\mathrm{fs}}=\frac{e^2}{4\pi\varepsilon_0\hbar c}=\frac{e^2 Z_0}{2h}=\frac{Z_0}{2\,\mathrm{R_K}}.
\]
**Key:** \(\alpha_{\mathrm{fs}}\) fine-structure constant; \(\mathrm{R_K}=h/e^2\); \(h,e\) SI defining constants. Therefore
\[
Z_0=2\alpha_{\mathrm{fs}}\,\mathrm{R_K}\approx 376.730\,\Omega
\]
is *the same statement* as the measured \(\alpha_{\mathrm{fs}}\). A TSB derivation of the SI number \(376.730\,\Omega\) *is* a derivation of \(\alpha_{\mathrm{fs}}\). This session does not derive \(\alpha_{\mathrm{fs}}\).

**Claim C (TSB, this session).** The ensemble of Mirrons supplies the constitutive pair \((\varepsilon_0,\mu_0)\). The only density-dependent object that is not already fixed by the single-engine clock is a dimensionless function \(\Phi\) of the packing fraction:
\[
Z_0(n_{\mathrm{M}})=\mathrm{R_K}\,\Phi(f),\qquad f=n_{\mathrm{M}}\cdot\frac{4}{3}\pi r_{\mathrm{M}}^3.
\]
**Key:** \(\Phi\) is what the bounce-current calculation must produce. \(e\) and \(h\) enter because impedance in ohms is energy×time/charge², and the only available quantum of that combination is \(h/e^2\).

Without \(e\) (or some other charge unit) there is no SI ohm. A “purely geometric \(Z_0\)” is well-defined only as \(\Phi\), or as \(Z_0/c\) in a unit system with \(c=1\).

---

## 2. Correction to the 2026-09-17 morning note

The nucleation note wrote
\[
\frac{\dot Z_0}{Z_0}\sim -\xi\frac{\dot n_{\mathrm{M}}}{n_{\mathrm{M}}}
\]
and treated \(\xi=\mathcal{O}(1)\) as the default. That assumed Mirrons behave as ordinary electric scatterers in a Maxwell host. Two facts kill that as the *leading* picture.

### 2.1 Transparency

A PEC sphere of radius \(r_{\mathrm{M}}\approx 0.63\,\mathrm{fm}\) has a geometric cross-section \(\sim\pi r_{\mathrm{M}}^2\) and, in the Rayleigh regime \(\lambda\gg r_{\mathrm{M}}\), a scattering cross-section
\[
\sigma_{\mathrm{sc}}\simeq\frac{8\pi}{3}k^4 r_{\mathrm{M}}^6
\]
**Key:** \(k=2\pi/\lambda\). That is small per object at radio \(\lambda\), but the *mean free path* at close packing is not “the vacuum.” More decisively: if Mirrons were extra obstacles *in addition to* the Maxwell field they generate, on-shell photons would have a second scattering channel the sky does not show. The photon *is* the Past⇄Future bounce. Counting Mirrons again as Rayleigh impurities is double counting.

### 2.2 Duality versus PEC

Even inside the rejected host picture, a self-dual scatterer (\(\tilde\alpha_E=\tilde\alpha_M\)) changes the index \(n=\sqrt{\varepsilon_r\mu_r}\) and *leaves \(Z\) invariant*. A PEC sphere is not self-dual (\(\alpha_e=4\pi r_{\mathrm{M}}^3\), \(\alpha_m=-2\pi r_{\mathrm{M}}^3\) in Gaussian). A null bounce, which treats \(E\) and \(B\) as the same field strength, is closer to self-dual. Duality is the TSB-default; PEC is the control.

**Corrected default.** Density dependence of \(Z_0\) is *not* guaranteed at order unity. It is a property of the *generator* model, computed below. Cosmological constancy of \(c_{\mathrm{ph}}\) is a stronger, separate constraint if anyone insists on the host picture.

---

## 3. Identities once \(c\) is locked

TSB operational clock (previous sessions):
\[
c_{\mathrm{clock}}=\frac{\alpha\, r_{\mathrm{M}}}{\Delta t_{\tau}}.
\]
**Key:** \(\alpha\) chord factor; \(r_{\mathrm{M}}\) radius; \(\Delta t_{\tau}\) tick. This \(c_{\mathrm{clock}}\) does not mention \(n_{\mathrm{M}}\).

Identify \(c_{\mathrm{ph}}=c_{\mathrm{clock}}\equiv c\) (transparency + “the bounce *is* the wave”). Then Identity A gives
\[
\varepsilon_0(n_{\mathrm{M}})=\frac{1}{Z_0(n_{\mathrm{M}})\,c},\qquad
\mu_0(n_{\mathrm{M}})=\frac{Z_0(n_{\mathrm{M}})}{c}.
\]
**Key:** once \(c\) is locked, \(Z_0(n_{\mathrm{M}})\) is the *only* unknown constitutive function. \(\varepsilon_0\) and \(\mu_0\) are slaves of that function. They scale inversely / directly with \(Z_0\).

If instead one refuses the identification and lets \(c_{\mathrm{ph}}=c_{\mathrm{clock}}/n(f)\), laboratory “constancy of \(c\)” bounds \(n(f)\) directly. That route is the host picture and is not used as the main line below.

---

## 4. Dimensional skeleton (non-circular)

Impedance has dimensions energy × time / charge². The only TSB-available quantum of that combination built from \(e,h\) is \(\mathrm{R_K}=h/e^2\). The only dimensionless packing variable built from \(n_{\mathrm{M}},r_{\mathrm{M}}\) is \(f\) (or \(\ell_{\mathrm{pack}}/r_{\mathrm{M}}=(\tfrac{4}{3}\pi/f)^{1/3}\)).

Therefore any generator model *must* take the form
\[
Z_0=\mathrm{R_K}\,\Phi\!\left(\frac{\ell_{\mathrm{pack}}}{r_{\mathrm{M}}},\zeta,N_{\tau}\right)
=\mathrm{R_K}\,\Phi(f,\zeta,N_{\tau}).
\]
**Key:** \(\Phi\) dimensionless; \(\zeta\) lossless-interface parameter; \(N_{\tau}=7\) may enter if the 8-phase engine grades the current. No other SI ingredients are allowed if \(e\) and \(h\) are the charge and action units.

The measured value is
\[
\Phi_{\mathrm{obs}}=\frac{Z_0}{\mathrm{R_K}}=2\alpha_{\mathrm{fs}}\approx 0.014638.
\]
**Key:** \(\Phi_{\mathrm{obs}}\) is the number a finished geometric calculation of \(\Phi\) at the locked packing must hit. This session produces \(\Phi(f)\) up to a model-dependent \(\mathcal{O}(1)\) factor, not that number.

Linear response:
\[
\xi\equiv\frac{\partial\ln Z_0}{\partial\ln n_{\mathrm{M}}}=\frac{\partial\ln\Phi}{\partial\ln n_{\mathrm{M}}}=-\frac{1}{3}\frac{\partial\ln\Phi}{\partial\ln(\ell_{\mathrm{pack}}/r_{\mathrm{M}})}.
\]
**Key:** \(\xi\) is the quantity that enters \(\dot Z_0/Z_0=\xi\,\dot n_{\mathrm{M}}/n_{\mathrm{M}}\) and, via Identity B with \(e,h\) fixed, \(\dot\alpha_{\mathrm{fs}}/\alpha_{\mathrm{fs}}=\xi\,\dot n_{\mathrm{M}}/n_{\mathrm{M}}\).

---

## 5. Bounce-current linear response (generator calculation)

### 5.1 Single-engine impedances

On one \(\Sigma_{\mathrm{M}}\), a refresh that moves charge \(q_{\mathrm{eff}}=e\) through a potential set by energy \(E_{\mathrm{ch}}\) in time \(\Delta t_{\tau}\) is a current
\[
I=\frac{e}{\Delta t_{\tau}}.
\]
**Key:** \(I\) mean bounce current; \(e\) elementary charge; \(\Delta t_{\tau}\) tick.

A characteristic voltage on the same object is
\[
V=\frac{E_{\mathrm{ch}}}{e}.
\]
**Key:** \(E_{\mathrm{ch}}\) is the energy cost of that charge displacement. It is *the* model choice.

The ratio is already an impedance:
\[
Z_{\mathrm{eng}}=\frac{V}{I}=\frac{E_{\mathrm{ch}}\,\Delta t_{\tau}}{e^2}.
\]
**Key:** \(Z_{\mathrm{eng}}\) engine impedance of one Mirron. No \(n_{\mathrm{M}}\) yet.

Two geometric choices for \(E_{\mathrm{ch}}\) and \(\Delta t_{\tau}\) close without new constants.

**Clock freeze (recommended, kinematics figure):** \(\Delta t_{\tau}=2r_{\mathrm{M}}/c\). Compton freeze: \(\Delta t_{\tau}=\hbar/\Delta_{\mathrm{TEP}}\). With \(r_{\mathrm{M}}=hc/\Delta_{\mathrm{TEP}}\) one has \(\hbar/\Delta_{\mathrm{TEP}}=r_{\mathrm{M}}/(2\pi c)\), so the two clocks differ by \(4\pi\).

**Choice E1 — charging energy = TEP floor.**
\[
E_{\mathrm{ch}}=\Delta_{\mathrm{TEP}}=\frac{hc}{r_{\mathrm{M}}}.
\]
Diameter clock:
\[
Z_{\mathrm{eng}}=\frac{hc}{r_{\mathrm{M}}}\cdot\frac{2r_{\mathrm{M}}}{c}\cdot\frac{1}{e^2}=\frac{2h}{e^2}=2\,\mathrm{R_K}.
\]
**Key:** \(r_{\mathrm{M}}\) cancels. Single-engine impedance is two von Klitzing units, independent of radius and of density.

Compton clock:
\[
Z_{\mathrm{eng}}=\frac{hc}{r_{\mathrm{M}}}\cdot\frac{r_{\mathrm{M}}}{2\pi c}\cdot\frac{1}{e^2}=\frac{h}{2\pi e^2}=\frac{\mathrm{R_K}}{2\pi}.
\]

**Choice E2 — charging energy = one tick quantum \(\hbar/\Delta t_{\tau}\).** Then
\[
Z_{\mathrm{eng}}=\frac{\hbar}{e^2}=\frac{\mathrm{R_K}}{2\pi}
\]
for *any* clock. Again independent of \(r_{\mathrm{M}}\) and of \(n_{\mathrm{M}}\).

**Lemma 1.** Any single-engine voltage/current ratio built from \(E_{\mathrm{ch}}\in\{\Delta_{\mathrm{TEP}},\hbar/\Delta t_{\tau}\}\) and a geometric tick is a pure multiple of \(\mathrm{R_K}\) and does not depend on \(n_{\mathrm{M}}\). Density dependence can enter only through *collective* superposition of those engines.

### 5.2 Fields of one engine

Electric-like amplitude across a diameter:
\[
E_{\mathrm{eng}}\sim\frac{V}{r_{\mathrm{M}}}=\frac{E_{\mathrm{ch}}}{e\,r_{\mathrm{M}}}.
\]
Magnetic-like amplitude of the bounce loop (Ampère, no \(\mu_0\) yet: \(B\)-circulation \(=\mu_{\mathrm{geom}} I\)):
\[
H_{\mathrm{eng}}\sim\frac{I}{r_{\mathrm{M}}}=\frac{e}{\Delta t_{\tau}\,r_{\mathrm{M}}}.
\]
**Key:** \(E_{\mathrm{eng}},H_{\mathrm{eng}}\) characteristic field strengths *at the surface*. Their ratio is again \(Z_{\mathrm{eng}}\). This is the local statement that a null bounce is impedance-matched to itself.

### 5.3 Collective mode: two closures

The long-wavelength Maxwell pair \((E,H)\) is the spatial average of the engine fields over a cell of volume \(n_{\mathrm{M}}^{-1}\). How one averages is the remaining ambiguity. Two closures are local and do not reintroduce a host.

#### Model G1 — cell charging (Coulomb across \(\ell_{\mathrm{pack}}\))

Put \(E_{\mathrm{ch}}\) on the *cell*, not on the Mirron:
\[
E_{\mathrm{ch}}^{\mathrm{(cell)}}=\frac{hc}{\ell_{\mathrm{pack}}}
\]
(the only energy made from \(h,c\) and the packing length). Keep the current on the engine, \(I=e/\Delta t_{\tau}\), with \(\Delta t_{\tau}=2r_{\mathrm{M}}/c\). Then
\[
Z_{\mathrm{G1}}=\frac{E_{\mathrm{ch}}^{\mathrm{(cell)}}\,\Delta t_{\tau}}{e^2}=\mathrm{R_K}\cdot\left(\frac{2r_{\mathrm{M}}}{\ell_{\mathrm{pack}}}\right).
\]
Wait: \(hc/\ell \cdot 2r_{\mathrm{M}}/c / e^2 = (2h/e^2)(r_{\mathrm{M}}/\ell)=2\mathrm{R_K}(r_{\mathrm{M}}/\ell_{\mathrm{pack}})\).

At close packing \(\ell_{\mathrm{pack}}\sim 2r_{\mathrm{M}}\), \(Z_{\mathrm{G1}}\sim\mathrm{R_K}\). Observed \(Z_0\approx 0.0146\,\mathrm{R_K}\), so G1 at face value is too large by \(\sim 70\). A \(4\pi\), a \(N_{\tau}=7\), or a \(\zeta\)-factor can move \(\mathcal{O}(10)\), not \(\mathcal{O}(70)\), unless several such factors multiply.

**Density derivative of this raw G1 (before any packing lock):**
\[
Z_{\mathrm{G1}}\propto\frac{r_{\mathrm{M}}}{\ell_{\mathrm{pack}}}\propto n_{\mathrm{M}}^{1/3},\qquad\xi_{\mathrm{G1}}=+\frac{1}{3}.
\]
**Key:** denser packing *raises* \(Z_{\mathrm{G1}}\) in this raw closure because the cell voltage rises when \(\ell\) shrinks while the current stays tied to \(r_{\mathrm{M}}\). That sign is the opposite of yesterday morning’s guess.

A more Coulomb-standard cell energy is \(E_{\mathrm{ch}}=hc/\ell_{\mathrm{pack}}\) *and* a transit time across the cell \(\Delta t=\ell_{\mathrm{pack}}/c\):
\[
Z_{\mathrm{G1}}'=\frac{hc}{\ell_{\mathrm{pack}}}\cdot\frac{\ell_{\mathrm{pack}}}{c}\cdot\frac{1}{e^2}=\mathrm{R_K}.
\]
**Key:** \(\xi_{\mathrm{G1}}'=0\). This is the closure in which every scale in \(V/I\) is the *same* scale. It is the continuum-limit statement “the lattice looks like itself at every spacing.”

**Lemma 2 (G1).** If voltage and current are both set by the packing cell, \(\Phi=\mathrm{const}\) and \(\xi=0\). If voltage is set by the cell and current by the engine, \(\xi=+1/3\) and \(\Phi=2 r_{\mathrm{M}}/\ell_{\mathrm{pack}}\).

#### Model G2 — engine charging, lattice current return

Keep \(E_{\mathrm{ch}}=\Delta_{\mathrm{TEP}}\) on the Mirron (voltage locked to \(r_{\mathrm{M}}\)) but let the return current that sources the *macroscopic* \(H\) be diluted over the cell face of area \(\ell_{\mathrm{pack}}^2\):
\[
H_{\mathrm{mac}}\sim\frac{I}{\ell_{\mathrm{pack}}}=\frac{e}{\Delta t_{\tau}\,\ell_{\mathrm{pack}}},\qquad
E_{\mathrm{mac}}\sim\frac{V}{r_{\mathrm{M}}}=\frac{\Delta_{\mathrm{TEP}}}{e\,r_{\mathrm{M}}}.
\]
**Key:** \(E_{\mathrm{mac}}\) still set at the engine; \(H_{\mathrm{mac}}\) set by current per unit cell face. Then
\[
Z_{\mathrm{G2}}=\frac{E_{\mathrm{mac}}}{H_{\mathrm{mac}}}=\frac{\Delta_{\mathrm{TEP}}\,\Delta t_{\tau}}{e^2}\cdot\frac{\ell_{\mathrm{pack}}}{r_{\mathrm{M}}}.
\]
Diameter clock and \(\Delta_{\mathrm{TEP}}=hc/r_{\mathrm{M}}\):
\[
Z_{\mathrm{G2}}=2\,\mathrm{R_K}\cdot\frac{\ell_{\mathrm{pack}}}{r_{\mathrm{M}}}=\mathrm{R_K}\cdot 2\left(\frac{4\pi}{3f}\right)^{1/3}.
\]
**Key:** \(\Phi_{\mathrm{G2}}(f)=2(4\pi/3f)^{1/3}\). At \(f=0.74\), \((4\pi/3f)^{1/3}\approx 1.78\), \(\Phi_{\mathrm{G2}}\approx 3.56\), \(Z_{\mathrm{G2}}\approx 9.2\times 10^{4}\,\Omega\), too large by \(\sim 240\). Same “\(\mathcal{O}(1)\) geometry does not hit \(0.0146\)” verdict as G1.

Density derivative:
\[
Z_{\mathrm{G2}}\propto\ell_{\mathrm{pack}}\propto n_{\mathrm{M}}^{-1/3},\qquad\xi_{\mathrm{G2}}=-\frac{1}{3}.
\]
**Key:** this is the sign guessed yesterday, now attached to a specific averaging (macro \(H\) diluted over the cell, macro \(E\) not).

#### Model G3 — 3D LC mesh, continuum constraint

Assign each cubic cell a capacitance and an inductance with *no* preexisting \(\varepsilon_0,\mu_0\), and demand that the cell delay equal the clock delay per cell.

\[
\sqrt{L_{\mathrm{cell}}C_{\mathrm{cell}}}=\frac{\ell_{\mathrm{pack}}}{c},\qquad
Z_{\mathrm{cell}}=\sqrt{\frac{L_{\mathrm{cell}}}{C_{\mathrm{cell}}}}.
\]
**Key:** first equation is “the mesh propagates at \(c_{\mathrm{clock}}\).” It uses the locked \(c\), so it does not derive \(c\). It derives \(Z_{\mathrm{cell}}\) once \(C_{\mathrm{cell}}\) (or \(L_{\mathrm{cell}}\)) is chosen.

Capacitance from charging energy \(E_{\mathrm{ch}}=e^2/(2C)\):
\[
C_{\mathrm{cell}}=\frac{e^2}{2E_{\mathrm{ch}}}.
\]
**Key:** \(C_{\mathrm{cell}}\) farad; \(E_{\mathrm{ch}}\) as in §5.1.

Then
\[
Z_{\mathrm{cell}}=\frac{\ell_{\mathrm{pack}}}{c\,C_{\mathrm{cell}}}=\frac{2E_{\mathrm{ch}}\,\ell_{\mathrm{pack}}}{e^2 c}.
\]

- If \(E_{\mathrm{ch}}=hc/\ell_{\mathrm{pack}}\) (cell Coulomb): \(Z_{\mathrm{cell}}=2\mathrm{R_K}\), \(\xi=0\).
- If \(E_{\mathrm{ch}}=hc/r_{\mathrm{M}}\) (engine Coulomb): \(Z_{\mathrm{cell}}=2\mathrm{R_K}\,(\ell_{\mathrm{pack}}/r_{\mathrm{M}})\), \(\xi=-1/3\).

**Lemma 3 (G3).** The LC-mesh with propagation locked to \(c_{\mathrm{clock}}\) reproduces G1′ or G2 according to whether the charging energy knows about \(\ell_{\mathrm{pack}}\) or only about \(r_{\mathrm{M}}\). No third density exponent appears.

### 5.4 Logarithmic coax analogue (optional, dense-wire limit)

A coaxial (or 2-D wire-grid) formula
\[
Z_{\mathrm{coax}}=\frac{\mathrm{R_K}}{2\pi}\,\ln\!\left(\frac{\ell_{\mathrm{pack}}}{r_{\mathrm{M}}}\right)
\]
is the standard TEM result with \(Z\) measured in von Klitzing units instead of \(\sqrt{\mu/\varepsilon}\). Then
\[
\xi_{\mathrm{coax}}=-\frac{1}{3\ln(\ell_{\mathrm{pack}}/r_{\mathrm{M}})}.
\]
**Key:** log-suppressed. At \(\ell_{\mathrm{pack}}=2r_{\mathrm{M}}\), \(\ln 2\approx 0.693\), \(\xi_{\mathrm{coax}}\approx -0.48\). At \(\ell_{\mathrm{pack}}=10 r_{\mathrm{M}}\), \(\xi_{\mathrm{coax}}\approx -0.14\). This is a *thin-wire* geometry, not a 3-D packing of 2-surfaces, and is listed only as a bound on how small \(|\xi|\) can be without being identically zero.

---

## 6. Rejected control: Maxwell–Garnett host

Recorded so the next session does not rebuild it by accident.

Host medium with \((\varepsilon_h,\mu_h)\), scatterers with dimensionless polarizabilities \(\tilde\alpha_E,\tilde\alpha_M\), packing \(f\):
\[
\varepsilon_r=\frac{1+2f\tilde\alpha_E}{1-f\tilde\alpha_E},\qquad
\mu_r=\frac{1+2f\tilde\alpha_M}{1-f\tilde\alpha_M},
\]
\[
Z=Z_h\sqrt{\frac{\mu_r}{\varepsilon_r}},\qquad
c_{\mathrm{ph}}=\frac{c_h}{\sqrt{\varepsilon_r\mu_r}}.
\]
**Key:** all symbols in the table. PEC: \(\tilde\alpha_E=1\), \(\tilde\alpha_M=-1/2\). Dual: \(\tilde\alpha_E=\tilde\alpha_M\).

Problems: (i) there is no host; (ii) dual scatterers hold \(Z\) fixed and *move* \(c_{\mathrm{ph}}\), contradicting a locked macroscopic \(c\) unless \(f\tilde\alpha\) is tiny; (iii) PEC vacuum would be a lossy metamaterial, not a transparent null cone. Do not use this as the TSB constitutive law.

If someone still wants a number from it: dual dilute, \(Z=Z_h\) (\(\xi=0\)); PEC dilute,
\[
\frac{Z}{Z_h}\approx 1-\frac{3}{2}f\tilde\alpha_E+\cdots,\qquad\xi_{\mathrm{PEC}}\approx -\frac{3}{2}f\tilde\alpha_E
\]
relative to the host, which is \(\mathcal{O}(f)\) and vanishes as \(f\to 0\).

---

## 7. Constitutive pair, written out

With \(c\) locked and \(Z_0=\mathrm{R_K}\Phi(f)\):
\[
\varepsilon_0(n_{\mathrm{M}})=\frac{1}{\mathrm{R_K}\,\Phi(f)\,c}=\frac{e^2}{h c\,\Phi(f)},
\]
\[
\mu_0(n_{\mathrm{M}})=\frac{\mathrm{R_K}\,\Phi(f)}{c}=\frac{h\,\Phi(f)}{e^2 c}.
\]
**Key:** \(\varepsilon_0\) falls if \(\Phi\) rises; \(\mu_0\) rises if \(\Phi\) rises; product \(\varepsilon_0\mu_0=1/c^2\) is packing-independent by construction.

Numerical slaves at the *observed* \(\Phi_{\mathrm{obs}}=2\alpha_{\mathrm{fs}}\):
\[
\varepsilon_0=\frac{e^2}{2\alpha_{\mathrm{fs}}\,hc},\qquad\mu_0=\frac{2\alpha_{\mathrm{fs}} h}{e^2 c},
\]
which are Identity A+B and teach nothing new. The TSB content is whichever \(\Phi(f)\) of §5 is adopted, evaluated at the locked packing.

---

## 8. Numbers at the locked radius

\(r_{\mathrm{M}}=6.302\times 10^{-16}\,\mathrm{m}\).
\[
\frac{4}{3}\pi r_{\mathrm{M}}^3\approx 1.048\times 10^{-45}\,\mathrm{m}^3.
\]
Close-pack sphere density (FCC/HCP, \(f=0.74\)):
\[
n_{\mathrm{M}}^{\mathrm{cp}}=\frac{0.74}{1.048\times 10^{-45}}\approx 7.06\times 10^{44}\,\mathrm{m}^{-3},\qquad
\ell_{\mathrm{pack}}^{\mathrm{cp}}\approx 1.12\times 10^{-15}\,\mathrm{m}\approx 1.78\,r_{\mathrm{M}}.
\]
**Key:** this is a *nuclear-scale* packing of 0.63 fm objects. It is the only packing that does not introduce a second length by hand.

| Model | \(\Phi(f)\) at \(f=0.74\) | \(Z_0\) at that \(\Phi\) | \(\xi\) | Hits \(376.73\,\Omega\)? |
|---|---|---|---|---|
| G1′ (cell/cell) | \(1\) or \(2\) | \(2.58\times 10^{4}\) or \(5.16\times 10^{4}\,\Omega\) | \(0\) | No (factor \(\sim 70\)–\(140\)) |
| G1 raw | \(2 r_{\mathrm{M}}/\ell\approx 1.12\) | \(\sim 2.9\times 10^{4}\,\Omega\) | \(+1/3\) | No |
| G2 / G3-engine | \(2\ell/r_{\mathrm{M}}\approx 3.56\) | \(\sim 9.2\times 10^{4}\,\Omega\) | \(-1/3\) | No |
| Coax log | \(\ln(\ell/r_{\mathrm{M}})/2\pi\approx 0.092\) | \(\sim 2.4\times 10^{3}\,\Omega\) | \(\approx -0.5\) | No (factor \(\sim 6\)) |
| Observed | \(2\alpha_{\mathrm{fs}}\approx 0.01464\) | \(376.73\,\Omega\) | \(?\) | Definition |

The coax log lands closest *numerically* and is the wrong geometry. No honest prefactor in G1–G3 produces \(\Phi=0.0146\) without a new small number. Candidates for that number, none derived here: \(2\alpha_{\mathrm{fs}}\) itself (circular); \(1/N_{\tau}^2=1/49\approx 0.020\) (same decade as \(\Phi_{\mathrm{obs}}\), not equal); \(1/(4\pi)^2\approx 0.0063\); a hierarchical suppression \((\ell_P/r_{\mathrm{M}})^p\) (tiny, would overshoot downward).

**Live gap, restated.** \(Z_0(n_{\mathrm{M}})\) as a *function* is derived. \(Z_0\) as the *SI number* is not. The nearest non-circular hint in the TSB integer set is \(1/49\), which would give
\[
Z_0\stackrel{?}{=}\frac{\mathrm{R_K}}{49}\approx 527\,\Omega
\]
(off by \(1.40\)). That is a coincidence until a mesh calculation produces \(1/N_{\tau}^2\) from seven active phases, not a result.

---

## 9. Cosmological linear response and the clock bound

Whatever model is kept,
\[
\frac{\dot Z_0}{Z_0}=\xi\frac{\dot n_{\mathrm{M}}}{n_{\mathrm{M}}},\qquad
\frac{\dot\alpha_{\mathrm{fs}}}{\alpha_{\mathrm{fs}}}=\xi\frac{\dot n_{\mathrm{M}}}{n_{\mathrm{M}}}\quad(e,h\text{ fixed}).
\]
**Key:** Identity B with SI-fixed \(e,h\).

Branch A (previous session, nucleation \(\Gamma=3H n_{\mathrm{M}}\)):
\[
\dot n_{\mathrm{M}}=0\qquad\Rightarrow\qquad\dot Z_0=\dot\alpha_{\mathrm{fs}}=0
\]
independent of \(\xi\).

Branch B (no nucleation, comoving count fixed):
\[
\frac{\dot n_{\mathrm{M}}}{n_{\mathrm{M}}}=-3H\qquad\Rightarrow\qquad
\frac{\dot\alpha_{\mathrm{fs}}}{\alpha_{\mathrm{fs}}}=-3\xi H.
\]

Atomic-clock comparisons give
\[
\left|\frac{\dot\alpha_{\mathrm{fs}}}{\alpha_{\mathrm{fs}}}\right|\lesssim 10^{-18}\,\mathrm{yr}^{-1}
\]
(Yb⁺ E3/E2; Filzinger et al. 2023, quoted at \(1.0(1.1)\times 10^{-18}\,\mathrm{yr}^{-1}\) in the 2025 review). Hubble today is
\[
H_0\approx 7.1\times 10^{-11}\,\mathrm{yr}^{-1}.
\]
Branch B then requires
\[
|\xi|\lesssim\frac{10^{-18}}{3H_0}\approx 5\times 10^{-9}.
\]
**Key:** \(H_0\) in inverse years; the numerical factor \(3\) is the FLRW dilution exponent.

G1′ (\(\xi=0\)) survives Branch B. G2 (\(\xi=-1/3\)) and G1-raw (\(\xi=+1/3\)) and the coax log (\(|\xi|\sim 0.1\)–\(0.5\)) are excluded on Branch B by six to eight orders of magnitude.

**Theorem (clock exclusion of diluting non-neutral \(\Phi\)).** Assume Identity B, SI-fixed \(e,h\), and \(|\dot\alpha/\alpha|\le 10^{-18}\,\mathrm{yr}^{-1}\). Then either

1. \(\dot n_{\mathrm{M}}=0\) (Branch A / nucleation), or
2. \(\lvert\partial\ln\Phi/\partial\ln n_{\mathrm{M}}\rvert\lesssim 5\times 10^{-9}\).

There is no room for a diluting vacuum whose impedance knows about \(r_{\mathrm{M}}\) and \(\ell_{\mathrm{pack}}\) at order unity.

Quasar / JWST [O III] bounds (\(\Delta\alpha/\alpha\sim 10^{-4}\) over Gyr) are weaker than the clocks for a *smooth* \(3\xi H\) drift; they would still exclude \(\xi=\mathcal{O}(1)\) on Branch B (\(\Delta\alpha/\alpha\sim 3\xi\Delta\ln a\sim\mathcal{O}(1)\) from \(z\sim 1\) to now). The clocks are the sharp tool.

---

## 10. Direct answers

**What is \(Z_0(n_{\mathrm{M}})\)?**
\[
Z_0(n_{\mathrm{M}})=\mathrm{R_K}\,\Phi(f),\qquad
f=n_{\mathrm{M}}\cdot\frac{4}{3}\pi r_{\mathrm{M}}^3,\qquad
\mathrm{R_K}=\frac{h}{e^2}.
\]
\(\Phi\) is computed from bounce current / cell voltage. Two local closures:
\[
\Phi_{\mathrm{G1'}} =\mathcal{O}(1)\quad(\xi=0),
\qquad
\Phi_{\mathrm{G2}} =2\left(\frac{4\pi}{3f}\right)^{1/3}\quad(\xi=-1/3).
\]

**What are \(\varepsilon_0(n_{\mathrm{M}})\) and \(\mu_0(n_{\mathrm{M}})\)?** Slaves of that \(Z_0\) at locked \(c\):
\[
\varepsilon_0=\frac{1}{Z_0 c},\qquad\mu_0=\frac{Z_0}{c}.
\]

**Does dilution thin \(Z_0\)?** Only in G2 / G3-engine / coax. Not in G1′. Not in a dual host picture. Yesterday’s \(\xi\sim\mathcal{O}(1)\) default is withdrawn as a model-independent claim.

**Does this produce \(376.73\,\Omega\)?** No. That number is \(2\alpha_{\mathrm{fs}}\mathrm{R_K}\). Hitting it is the \(\alpha_{\mathrm{fs}}\) problem. The closest TSB integer shot is \(\mathrm{R_K}/49\approx 527\,\Omega\), not derived.

**What does this do to nucleation (morning session)?** It *strengthens* Branch A if \(\Phi\) is allowed to depend on \(f\) at any observationally relevant level. It *permits* Branch B only for the neutral closure \(\xi=0\). The morning continuity equation is unchanged. The argument that dilution is already ugly at laboratory \(Z_0\) is now a clock theorem on \(\alpha_{\mathrm{fs}}\), not a hand-waved \(\xi\sim 1\).

---

## 11. Recommended next derivations

1. Freeze one closure: G1′ (\(\xi=0\), continuum self-similar cell) or G2 (\(\xi=-1/3\), engine voltage / cell \(H\)). They are different physical claims about whether charging energy knows the packing length.
2. Compute \(\Phi\) from the 8-phase current on a six-domain / E₈ cell, including \(N_{\tau}=7\), and see whether \(1/49\) (or \(2/49\), \(1/(4\pi N_{\tau})\), …) actually falls out. That is the \(\alpha_{\mathrm{fs}}\) attempt, and it should be labelled as such.
3. Keep \(e\) explicit. Do not hide it inside a “geometric ohm.”
4. Do not resurrect Maxwell–Garnett as the generator.

---

## Sources used this session

- Companion note, this morning: `2026-09-17_Expanding_space_geometric_creation_of_Mirrons_via_scalar.md`
- `2026-09-16_Mirron_nature_and_finite_c.md` (dictionary \(Z_0\leftrightarrow\Sigma_{\mathrm{M}}\), operational \(c\))
- `2026-09-15_Mirron_radius_and_Tav_tick_from_orbit.md`, `2026-09-15_Mirron_r_locked_orbit_as_Tav_tick.md` (\(r_{\mathrm{M}}=\lambda_{313}\))
- SI identities: \(Z_0=1/(\varepsilon_0 c)\), \(\alpha_{\mathrm{fs}}=e^2 Z_0/(2h)\), \(\mathrm{R_K}=h/e^2\)
- \(\dot\alpha/\alpha\) bounds: Filzinger et al. 2023 Yb⁺ E3/E2 as quoted in the 2025 Measurement Techniques review; LAMOST / JWST [O III] as weaker cosmological cross-checks
- Standard controls: Maxwell–Garnett / Clausius–Mossotti; PEC sphere polarizabilities; coaxial TEM impedance

---

## Query results displayed

- GitHub code search on `TauSuperblock` for \(Z_0\), impedance, \(\varepsilon_0\): no prior derivation.
- Drive Personal Files search for vacuum impedance / bounce current / polarizability: no prior file. This is the first \(Z_0(n_{\mathrm{M}})\) note.
- Web: LAMOST \(\mathrm{d}(\Delta\alpha/\alpha)/\mathrm{d}t=(-3.4\pm 2.4)\times 10^{-13}\,\mathrm{yr}^{-1}\) (weak); atomic-clock linear coefficient on \(\mathrm{d}\ln\alpha/(H_0\mathrm{d}t)\) at a few ppb; Yb⁺ bound \(\sim 10^{-18}\,\mathrm{yr}^{-1}\). Those numbers are used only in §9.

---

*End of session note — 2026-09-17 \(Z_0(n_{\mathrm{M}})\) linear response.*
