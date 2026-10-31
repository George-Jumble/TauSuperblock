# Integrate \(J_{\rm sec}\)

**Date:** 2026-09-20  
**Object:** \(\displaystyle J^\nu_{\rm sec}=-\mathcal{P}_8\bigl(\Delta_K^\nu+\nabla_\mu T^{\mu\nu}_{\rm bind}\bigr)\) on an isolated Prime patch.  
**Binding term:** \(\kappa_i\) unknown \(\Rightarrow\) set \(T_{\rm bind}=0\) for this integral.

---

## 1. Static case

Far-zone, \(\rho_i\) constant, \(\lambda_{m_0}\ll L\):

\[
T^{00}_K
=
\sum_{i=2}^{6}\gamma_i\rho_i
=
\text{const}
\quad\Rightarrow\quad
\Delta_K^\nu=0
\quad\Rightarrow\quad
J_{\rm sec}=0.
\]

No current. Equal frozen densities do not produce occupancy.

---

## 2. Expanding dust, ansatz A, Prime empty

Isolation: \(\rho_1=0\), \(F_{\rm wall}=0\). Hidden copies still carry proper density \(\rho_i=\rho_b\) (ansatz A charged to baryons), diluting as dust,

\[
\partial_t\rho_i=-3H\rho_i.
\]

Far-zone defect:

\[
\Delta^0_K
=
\sum_{i=2}^{6}\gamma_i\partial_t\rho_i
=
-3H\rho_b\sum_{i=2}^{6}\gamma_i
=
-3H\times 5.401514\,\rho_b.
\]

Hubble is slow compared with eight ticks, so \(\mathcal{P}_8\Delta_K=\Delta_K\).

\[
J^0_{\rm sec}
=
3H\times 5.401514\,\rho_b.
\]

**Key.** \(J^0_{\rm sec}\): energy-density rate into the engine account. \(H\): local expansion. \(\rho_b\): baryon density of one copy.

---

## 3. Integral on the de Sitter patch

\[
\dot E
=
\int_{\Sigma}J^0_{\rm sec}\,dV
=
3H\times 5.401514\,\rho_b\times\mathrm{Vol}(\Sigma).
\]

Take \(\Sigma\) the interior event-horizon ball, \(r_{\rm eh}=c/H_\Lambda\), \(H=H_\Lambda\), \(\rho_b=\Omega_b\rho_c\):

\[
\begin{align*}
H_\Lambda
&\approx 1.8\times 10^{-18}\,\mathrm{s^{-1}},\\
\mathrm{Vol}
&=
\frac{4\pi}{3}r_{\rm eh}^3
\approx 2.0\times 10^{79}\,\mathrm{m^3},\\
\rho_b
&\approx 4.2\times 10^{-28}\,\mathrm{kg\,m^{-3}},\\
\dot E
&\approx 2.4\times 10^{35}\,\mathrm{kg\,s^{-1}}\,c^2
\approx 2\times 10^{52}\,\mathrm{W}.
\end{align*}
\]

Equivalent rest-mass rate if every joule became rest mass:

\[
\dot M
=
\frac{\dot E}{c^2}
\approx 2.4\times 10^{35}\,\mathrm{kg\,s^{-1}}
\approx 1.2\times 10^5\,M_\odot\,\mathrm{s^{-1}}.
\]

Over one Hubble time the accumulated density is

\[
\int J^0_{\rm sec}\,dt
\sim
5.401514\,\rho_b,
\]

i.e. the whole shadow budget poured into the Prime account. That is the kernel coupling, integrated, not a new species.

**Key.** \(\Sigma\): womb ball. \(\dot E,\dot M\): power and equivalent mass rate. Not a measured source.

---

## 4. What this is not

- Not a baryon-yield theorem. Conversion efficiency of engine-account energy into standing rest mass is not derived (\(\eta\le 1\) unknown).
- Not \(\rho_\Lambda\). Same order as \(3H\rho_\Lambda\mathrm{Vol}\) only because \(5.4\rho_b\sim 0.3\rho_c\) and \(\rho_\Lambda\sim 0.7\rho_c\). Coincidence of budgets, not a derivation.
- Not the binding current. \(\kappa_i=0\) here.
- Not compatible with strict co-location emptiness: if all six empty together, \(\rho_i=0\) and \(\dot E=0\). The integral assumes hidden dust remains after Prime has emptied. That is an extra reading of ansatz A in the womb.

---

## 5. Decision

The integral exists. Its value is \(3H\) times the shadow mass in the patch. Full conversion would refill the void in a Hubble time and cancel isolation. So either \(\eta\ll 1\), or hidden copies empty too and \(J_{\rm sec}=0\). Neither option produces a calculated \(m_0\) or a calculated \(\Lambda\).

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_integrate_Jsec_2026-09-20.md`
