# Session log: Derivation of the nucleation current

- **Session date:** Friday, 2026-09-18
- **Charge:** Derive \(\nabla_\mu(n_{\mathrm{M}}u^\mu)=\Gamma\), not merely name it.
- **Short answer:** With \(r_{\mathrm{M}}\) frozen, conserved \(N_{\mathrm{M}}\) would force \(n_{\mathrm{M}}\propto a^{-3}\). Clocks plus a non-tiny \(\xi\) forbid that (Branch B dead). Packing fraction \(f=n_{\mathrm{M}}v_{\mathrm{M}}\) is then a constraint, not a drifting degree of freedom. The unique current that holds \(f\) (and \(n_{\mathrm{M}}\)) fixed in the proper frame is \(\Gamma=3Hn_{\mathrm{M}}\) on the support of the two gates, and \(0\) off that support. The gates come from the \(\varphi_{\mathrm{n}}\) equilibrium and the wall scale \(H/c\). The *microscopic* instanton that creates one \(\Sigma_{\mathrm{M}}\) is not computed; the current is the relaxation that slaved the rate to the packing deficit.
- **This file:** `Personal Files/2026-09-18_nucleation_current_derivation.md`
- **Parent:** `2026-09-18_two_scalar_action.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(J^\mu=n_{\mathrm{M}}u^\mu\) | Proper-number current of Mirrons. |
| \(u^\mu\) | Four-velocity of the comoving rest frame (\(u^\mu=(1,0,0,0)\) in FLRW). |
| \(n_{\mathrm{M}}\) | Proper number density. \(n_{\mathrm{M}}=-J_\mu u^\mu\). |
| \(\Gamma=\nabla_\mu J^\mu\) | Proper creation rate (number per volume per proper time). |
| \(v_{\mathrm{M}}=\tfrac43\pi r_{\mathrm{M}}^3\) | Reference 3-volume per mirror (packing bookkeeping). \(r_{\mathrm{M}}\) frozen. |
| \(f=n_{\mathrm{M}}v_{\mathrm{M}}\) | Packing fraction. |
| \(f_\ast\) | Target packing (Branch A attractor). Not necessarily close-packed. |
| \(\delta f=f_\ast-f\) | Packing deficit. |
| \(\tau_{\mathrm{rel}}\) | Relaxation time toward \(f_\ast\). Instantaneous \(\Rightarrow\tau_{\mathrm{rel}}\to 0^+\). |
| \(\varphi_{\mathrm{n}}=\Omega^{-\nu}\) | Equilibrium of \(V_{\mathrm{n}}\) (two-scalar action). |
| \(G_{\mathrm{n}}=\Theta(1-\varphi_{\mathrm{n}})\) | Stiffness gate. |
| \(G_\Omega=\Theta(\lvert\nabla\log\Omega\rvert-H/c)\) | Wall gate. |
| \(T^{\mu\nu}_{\mathrm{src}}\) | Stress added when a mirror is created. |
| \(\xi\) | \(\partial\ln Z_0/\partial\ln n_{\mathrm{M}}\). Clocks \(\Rightarrow\) Branch B dead if \(\xi=\mathcal{O}(1)\). |

---

## 1. Conserved current if nothing is created

Covariant conservation of number:
\[
\nabla_\mu J^\mu=0,\qquad J^\mu=n_{\mathrm{M}}u^\mu.
\]
FLRW, comoving:
\[
\nabla_\mu J^\mu=\dot n_{\mathrm{M}}+3Hn_{\mathrm{M}}=\frac{1}{a^3}\frac{\mathrm{d}}{\mathrm{d}t}(a^3 n_{\mathrm{M}}).
\]
**Key:** if \(\Gamma=0\), \(n_{\mathrm{M}}\propto a^{-3}\). That is Branch B.

Clock lock: \(r_{\mathrm{M}}\) does not scale with \(a\). Then \(v_{\mathrm{M}}\) is constant and
\[
f=n_{\mathrm{M}}v_{\mathrm{M}}\propto a^{-3}\qquad(\Gamma=0).
\]
Packing thins. If impedance or any coupling depended on \(n_{\mathrm{M}}\) at \(\mathcal{O}(1)\), \(\dot\alpha/\alpha\) bounds kill this. Even if \(\xi=0\), the geometric constraint “mirrors do not stretch, volume grows” still *asks* for new surfaces if one wants a constant proper lattice. Branch A is that demand.

---

## 2. Packing as a constraint

Target: a frozen proper packing \(f\to f_\ast\) wherever the gates allow creation.
\[
\dot f=\dot n_{\mathrm{M}}v_{\mathrm{M}}
\]
because \(\dot v_{\mathrm{M}}=0\). Continuity with a source:
\[
\dot n_{\mathrm{M}}+3Hn_{\mathrm{M}}=\Gamma
\quad\Rightarrow\quad
\dot f+3Hf=\Gamma v_{\mathrm{M}}.
\]
Demand \(\dot f=0\) and \(f=f_\ast\):
\[
\Gamma=\frac{3Hf_\ast}{v_{\mathrm{M}}}=3Hn_{\mathrm{M}}.
\]
**Key:** this is not a guess at a prefactor. It is the unique \(\Gamma\) that makes \(f\) a constant of motion given frozen \(r_{\mathrm{M}}\).

Off the gates, creation is forbidden, so \(\Gamma=0\) and \(f\) dilutes *locally* until a wall / void satisfies the thetas. Globally Branch A holds because voids and walls dominate the volume growth that would have diluted \(n_{\mathrm{M}}\).

---

## 3. Gates from the two-scalar sector

Equilibrium of \(V_{\mathrm{n}}\):
\[
\varphi_{\mathrm{n}}=\Omega^{-\nu}.
\]
Stiffness gate \(\varphi_{\mathrm{n}}<\varphi_{\mathrm{crit}}=1\) is
\[
\Omega>1\qquad(\nu>0).
\]
That is “inside a void” in the conformal slicing.

Wall gate: homogeneous Hubble flow has \(\lvert\nabla\log\Omega\rvert=0\). The only cosmological inverse-length already in the theory that distinguishes a wall from a uniform void interior is \(H/c\). Require
\[
\lvert\nabla\log\Omega\rvert>\frac{H}{c}
\]
so that creation sits on gradients (void walls), matching the earlier fractal-tree / wall preference.

Product of gates:
\[
\Gamma
=
3Hn_{\mathrm{M}}
\,G_{\mathrm{n}}\,G_\Omega
=
3Hn_{\mathrm{M}}
\,\Theta(1-\varphi_{\mathrm{n}})
\,\Theta\bigl(\lvert\nabla\log\Omega\rvert-H/c\bigr).
\]

---

## 4. Relaxation form (what is and is not derived)

If packing is not slaved instantly, a linear relaxation
\[
\Gamma_{\mathrm{rel}}=\frac{1}{\tau_{\mathrm{rel}}}\frac{\delta f}{v_{\mathrm{M}}}
=\frac{f_\ast-f}{\tau_{\mathrm{rel}}v_{\mathrm{M}}}
\]
would apply on the gate support. Branch A is the limit
\[
\tau_{\mathrm{rel}}\ll H^{-1}
\quad\Rightarrow\quad
f\to f_\ast
\quad\Rightarrow\quad
\Gamma\to 3Hn_{\mathrm{M}}.
\]
**Derived:** the attractor current \(3Hn_{\mathrm{M}}\) once \(\tau_{\mathrm{rel}}\) is short compared with expansion.  
**Not derived:** the instanton action for one new \(\Sigma_{\mathrm{M}}\), and therefore \(\tau_{\mathrm{rel}}\) from \(\mu_{\mathrm{n}}\). If \(\tau_{\mathrm{rel}}\gtrsim H^{-1}\), Branch A fails and clocks constrain \(\xi\tau_{\mathrm{rel}}\).

The nucleation current used in the two-scalar system is this attractor plus gates, not a Schwinger formula \(\propto\mu_{\mathrm{n}}^4 e^{-S_E}\).

---

## 5. Stress that accompanies the current

Creating one mirror in the rest frame adds energy \(\Delta_{\mathrm{TEP}}\) and no extra momentum. The source in Einstein’s equation (with \(G_{\mathrm{N}}\) data) is
\[
\nabla_\mu T^{\mu\nu}_{\mathrm{M}}
=
\Delta_{\mathrm{TEP}}\,\Gamma\,u^\nu
=
\Delta_{\mathrm{TEP}}(\nabla_\mu J^\mu)\,u^\nu
\]
for dust-like mirrors. **Key:** \(T^{\mu\nu}_{\mathrm{M}}=n_{\mathrm{M}}\Delta_{\mathrm{TEP}}u^\mu u^\nu\) if mirrors are at rest and non-relativistic as a fluid. The scalar / conformal sector must lose the same energy (void budget). No \(F_{\mu\nu}\) current.

---

## 6. Covariant statement

\[
J^\mu=n_{\mathrm{M}}u^\mu,
\qquad
\nabla_\mu J^\mu
=
3\,(u^\lambda\nabla_\lambda\ln a)\,n_{\mathrm{M}}\,G_{\mathrm{n}}G_\Omega
=
3Hn_{\mathrm{M}}\,G_{\mathrm{n}}G_\Omega.
\]
**Key:** \(H=u^\lambda\nabla_\lambda\ln a\) in FLRW; the first form is the same scalar on a general congruence if \(a\) is replaced by the local expansion \(\theta/3=\nabla_\lambda u^\lambda/3\):
\[
\nabla_\mu J^\mu
=
(\nabla_\lambda u^\lambda)\,n_{\mathrm{M}}\,G_{\mathrm{n}}G_\Omega
\quad\text{on the Branch A attractor.}
\]
In FLRW \(\nabla_\lambda u^\lambda=3H\), recovering \(3Hn_{\mathrm{M}}\).

---

## 7. Direct statement

The nucleation current is the packing-constraint current
\[
\nabla_\mu(n_{\mathrm{M}}u^\mu)=(\nabla_\lambda u^\lambda)\,n_{\mathrm{M}}\,\Theta(1-\varphi_{\mathrm{n}})\,\Theta\bigl(\lvert\nabla\log\Omega\rvert-H/c\bigr),
\]
derived from frozen \(r_{\mathrm{M}}\) + Branch A + two-scalar gates. The microscopic \(\tau_{\mathrm{rel}}(\mu_{\mathrm{n}})\) is not derived.

---

*End of session note — 2026-09-18 nucleation current.*
