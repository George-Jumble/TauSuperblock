# \(w_\Omega=-1/3\) plus domain orbits vs the Hubble tension

**Date:** 2026-09-20  
**Input:** conformal fluid at \(w_\Omega=-1/3\); orbital kinetic budget of the locked \(\beta_i\).  
**Question:** does that split \(H_0\) the way SH0ES vs Planck does?  
**Not live-frame law.**

---

## 1. Two pieces

Conformal homogeneous leading term with constant \(\dot\omega\) (previous note):

\[
w_\Omega=-\frac13,
\qquad
\rho_\Omega(a)=\rho_{\Omega0}\,a^{-2}.
\]

Same dilution as curvature. Background-degenerate with \(\Omega_k\).

Orbital piece from B_lin, frozen \(R_{\rm int}\) (F7 radius slot frozen, \(\beta_i\) locked):

\[
\begin{align*}
\{\beta_i\}
&=
\{0,\tfrac1{15},\tfrac15,\tfrac4{15},\tfrac25,\tfrac35\},\\
\sum_{i=2}^{6}(\gamma_i-1)
&=
0.401514,\\
\sum_{i=2}^{6}\gamma_i\beta_i^2
&=
0.7436.
\end{align*}
\]

Two book-keepings for the orbit, both written:

\[
\rho_{\rm orb}^{(A)}
=
\rho_1\sum_{i=2}^{6}(\gamma_i-1)
=
0.401514\,\rho_1,
\qquad
\rho_{\rm orb}^{(B)}
=
\frac12\rho_1\sum_{i=2}^{6}\gamma_i\beta_i^2
=
0.3718\,\rho_1.
\]

(A) is rest-frame kinetic leftover \(\gamma-1\). (B) is \(\tfrac12\gamma\beta^2\). Same order. If \(\rho_1\) is baryonic, \(\Omega_b\approx 0.049\), then

\[
\Omega_{\rm orb}^{(A)}\approx 0.020,
\qquad
\Omega_{\rm orb}^{(B)}\approx 0.018.
\]

If \(\rho_1\) tracks all visible matter, swap in \(\Omega_m\) and the number grows; that is a different ansatz and is flagged below.

Frozen \(\beta\) and frozen \(R_{\rm int}\) ⇒ \(\rho_{\rm orb}\) dilutes with \(\rho_1\). If \(\rho_1\sim a^{-3}\), the orbit is extra dust, not extra vacuum.

**Key.** \(\rho_\Omega\): conformal density, \(w=-1/3\). \(\rho_{\rm orb}\): domain-orbit kinetic budget. \(\rho_1\): Prime proper density in ansatz A.

---

## 2. Friedmann system

Flat chart (orbit is dust, not \(k\)):

\[
E^2(z)
:=
\frac{H(z)^2}{H_0^2}
=
\Omega_m(1+z)^3
+
\Omega_r(1+z)^4
+
\Omega_\Omega(1+z)^2
+
\Omega_{\rm orb}(1+z)^3
+
\Omega_\Lambda.
\]

Closure today:

\[
\Omega_m+\Omega_r+\Omega_\Omega+\Omega_{\rm orb}+\Omega_\Lambda=1.
\]

**Key.** \(E(z)\): Hubble function. \(\Omega_\Omega=\rho_{\Omega0}/\rho_{c0}\). Radiation kept for completeness, negligible at low \(z\).

Observed split to beat:

\[
H_0^{\rm CMB}\approx 67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}},
\qquad
H_0^{\rm loc}\approx 73.0,
\qquad
\frac{H_0^{\rm loc}}{H_0^{\rm CMB}}\approx 1.083.
\]

---

## 3. What each piece does to \(H_0\)

**Orbit as extra dust (\(\Omega_{\rm orb}\sim 0.02\), \(\rho_1=\rho_b\)).**  
Same as raising \(\Omega_m\) by \(0.02\). For fixed present \(H_0\) and flatness, \(\Omega_\Lambda\) drops. Distances to last scattering change at the percent level. Sign for the tension: extra late matter *slows* late expansion relative to a Λ-heavier model. That is the wrong direction if one hoped to lift local \(H_0\) above the CMB fit. Magnitude: \(\sim 2\%\) in the matter budget, not \(8\%\) in \(H_0\).

**Orbit charged to all \(\Omega_m\)** (\(\rho_1=\rho_m\)): \(\Omega_{\rm orb}\sim 0.12\). That is a different universe (too much dust). Not a small correction.

**Conformal \(\Omega_\Omega\) with \(w=-1/3\).**  
Background-identical to positive curvature if \(\Omega_\Omega>0\) is written as \(-\Omega_k\) in the usual sign. Planck+BAO already limit \(|\Omega_k|\lesssim 0.01\) in ΛCDM-like fits. A free \(\Omega_\Omega\sim 0.05\)–\(0.10\) large enough to move \(H_0\) by several km/s/Mpc is the same conflict.

At last scatter, \(\rho_\Omega/\rho_m\sim \Omega_\Omega/[\Omega_m(1+z)]\sim \Omega_\Omega/330\). Early-time lever is tiny. This is not early dark energy.

**Together.** Dust-like orbit plus curvature-like \(\Omega_\Omega\) is two late-time knobs already constrained, neither an early-time lever. They do not produce a clean 67.4 vs 73.0 split.

---

## 4. A number, not a fit

Reference flat ΛCDM: \(\Omega_m=0.315\), \(\Omega_\Lambda=0.685\), \(\Omega_\Omega=\Omega_{\rm orb}=0\), \(H_0=67.4\).

Add \(\Omega_{\rm orb}=0.020\), \(\Omega_\Omega=0.010\), take it from \(\Omega_\Lambda\):

\[
\Omega_\Lambda'=0.655,
\qquad
E(z)\ \text{changes by a few percent at }z\sim 0.5\text{–}1.
\]

Luminosity-distance shift at \(z<0.15\) (SH0ES ladder) is \(\lesssim 1\%\). Required for the tension is \(\sim 8\%\) in \(H_0\). Short by a factor of several, and the CMB curvature bound is already eating the \(\Omega_\Omega\) knob.

No retune of \(\beta_i\) is performed. B_lin stays locked.

---

## 5. Verdict

\(w_\Omega=-1/3\) plus locked domain orbits is a well-defined 4D system. It does **not** yield the Hubble tension.

- Orbit \(\to\) extra dust \(\sim 0.02\) if charged to baryons. Wrong sign to lift local \(H_0\), wrong size.
- \(\Omega_\Omega\) \(\to\) curvature twin. Size needed is larger than CMB+BAO like. Early lever negligible.
- Combined late-time shift \(\lesssim 1\%\) in the SH0ES integral, not \(8\%\).

What *would* move the tension in the usual direction is extra energy *before* recombination (early dark energy, extra \(N_{\rm eff}\)), or a late phantom component. Neither is \(w=-1/3\) plus frozen \(\beta_i\).

Do not write “orbits solve \(H_0\)” into the live frame.

---

## Master key

| Symbol | Meaning |
|---|---|
| \(w_\Omega,\rho_\Omega,\Omega_\Omega\) | conformal fluid, \(a^{-2}\) |
| \(\rho_{\rm orb},\Omega_{\rm orb}\) | locked-orbit kinetic budget |
| \(E(z)\) | \(H(z)/H_0\) |
| \(H_0^{\rm CMB},H_0^{\rm loc}\) | Planck-like vs local ladder |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_wOmega_orbits_Hubble_tension_2026-09-20.md`
