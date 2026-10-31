# Derivation of the Mirron current

**Date:** 2026-09-20  
**Request:** derive \(J^\nu_{\rm Mirron}[K,\rho_{\rm vac},\{\beta_i\}]\).  
**Rule:** 4D. Bianchi first. No creation from nothing. Live frame owns F7, B_lin, \(K\), \(m_0\) as floor.  
**Convention:** Mirron, never “soliton.”

---

## 0. What can be derived

Einstein plus the contracted Bianchi identity forbid a net source:

\[
\nabla_\mu G^{\mu\nu}=0
\quad\Rightarrow\quad
\nabla_\mu T^{\mu\nu}_{\rm tot}=0.
\]

**Key.** \(G^{\mu\nu}\): Einstein tensor. \(T^{\mu\nu}_{\rm tot}\): total stress-energy that sources \(G^{\mu\nu}\). \(\nabla\): Levi-Civita connection of the Prime 4-metric.

If one piece of \(T_{\rm tot}\) gains energy-momentum, another piece loses it. The Mirron current is that transfer, written on Prime.

---

## 1. Split

\[
T^{\mu\nu}_{\rm tot}
=
T^{\mu\nu}_{\rm vis}
+
T^{\mu\nu}_{K}
+
T^{\mu\nu}_{\rm vac}
+
T^{\mu\nu}_{M}.
\]

- \(T_{\rm vis}\): visible Prime matter and radiation (baryons, CMB, …).
- \(T_{K}\): Prime-effective tensor produced by the kernel from all six copies.
- \(T_{\rm vac}\): vacuum piece with \(\rho_{\rm vac}\) constant on the patch (Λ-like).
- \(T_{M}\): bookkeeping tensor of the refresh engine — whatever the Mirron moves into or out of the visible sector.

Conservation of the sum:

\[
\nabla_\mu T^{\mu\nu}_{M}
=
-
\nabla_\mu T^{\mu\nu}_{\rm vis}
-
\nabla_\mu T^{\mu\nu}_{K}
-
\nabla_\mu T^{\mu\nu}_{\rm vac}.
\]

**Definition.**

\[
J^\nu_{\rm Mirron}
:=
\nabla_\mu T^{\mu\nu}_{M}.
\]

So

\[
J^\nu_{\rm Mirron}
=
-
\nabla_\mu T^{\mu\nu}_{\rm vis}
-
\nabla_\mu T^{\mu\nu}_{K}
-
\nabla_\mu T^{\mu\nu}_{\rm vac}.
\]

That is the current. Everything below names the three terms.

**Key.** \(J^\nu_{\rm Mirron}\): transfer current into the engine account. Index \(\nu\) is Prime spacetime.

---

## 2. Vacuum term — usually zero

For a cosmological-constant piece

\[
T^{\mu\nu}_{\rm vac}
=
-\rho_{\rm vac}\,g^{\mu\nu},
\qquad
\rho_{\rm vac}=\mathrm{const},
\]

one has \(\nabla_\mu T^{\mu\nu}_{\rm vac}=0\). Strict Λ cannot feed the engine.

If, in the isolated patch, one allows a slow leak

\[
\rho_{\rm vac}=\rho_{\rm vac}(x),
\qquad
T^{\mu\nu}_{\rm vac}
=
-\rho_{\rm vac}g^{\mu\nu},
\]

then

\[
\nabla_\mu T^{\mu\nu}_{\rm vac}
=
-
(\nabla^\nu\rho_{\rm vac}).
\]

That leak is *not* derived from F7 or from B_lin. It is an extra hypothesis (vacuum decay). Default in this derivation: **off**.

\[
\nabla_\mu T^{\mu\nu}_{\rm vac}=0
\quad\text{(default).}
\]

Integrated vacuum energy \(\rho_{\rm vac}\mathrm{Vol}\) still grows with volume at constant density. That growth is geometry, not a current into rest mass.

**Key.** \(\rho_{\rm vac}\): vacuum energy density. Default \(\nabla\rho_{\rm vac}=0\).

---

## 3. Visible term — isolation kills the wall flux

Ordinary visible conservation in the presence of an external flux \(F^\nu_{\rm wall}\) (EM and matter from the walls) reads, schematically,

\[
\nabla_\mu T^{\mu\nu}_{\rm vis}
=
F^\nu_{\rm wall}
+
S^\nu_{\rm loc},
\]

where \(S^\nu_{\rm loc}\) is local non-gravitational exchange (already inside \(T_{\rm vis}\) if included). After the walls have left the event horizon of the void observer,

\[
F^\nu_{\rm wall}=0.
\]

On the isolated patch, with default vacuum,

\[
J^\nu_{\rm Mirron}
=
-
\nabla_\mu T^{\mu\nu}_{\rm vis}
-
\nabla_\mu T^{\mu\nu}_{K}.
\]

If visible matter in the interior is already gone, \(\nabla_\mu T^{\mu\nu}_{\rm vis}\approx 0\) as well, and the only remaining channel is the kernel.

**Key.** \(F^\nu_{\rm wall}\): incoming visible flux from Prime walls. Isolation: \(F^\nu_{\rm wall}=0\).

---

## 4. Kernel term — the Superblock channel

Live-frame kernel (Prime chart):

\[
T^{00}_{K}(x)
=
\sum_{i=1}^{6}
\gamma_i
\int
\overline{G}_i(x,x';\beta_i,\lambda_{m_0})\,
T^{00}_{(i)}(x')\,d^{3}x'
+\cdots
\]

with \(\gamma_i=(1-\beta_i^2)^{-1/2}\), \(\beta_i=(m_i-11)/30\), and \(\overline{G}_i\) the period-averaged Yukawa of range \(\lambda_{m_0}\).

Promote the far-zone, slow-motion piece to a tensor in Prime:

\[
T^{\mu\nu}_{K}(x)
=
\sum_{i=1}^{6}
\gamma_i
\bigl(K_i\ast T_{(i)}\bigr)^{\mu\nu}(x).
\]

**Key.** \(K_i\ast\): integral operator whose kernel is \(\overline{G}_i\). \(T_{(i)}\): stress tensor of domain \(D_i\), pulled to the Prime chart. \(\lambda_{m_0}=\hbar/(m_0 c)\).

The Yukawa operator is not the massless Green function of \(\nabla_\mu\nabla^\mu\). Its divergence on Prime does not vanish when the hidden sources move or when the boost \(\beta_i\) fails to be a Killing flow of the Prime metric.

Define the kernel defect

\[
\Delta^\nu_{K}
:=
\nabla_\mu T^{\mu\nu}_{K}.
\]

Then, on the isolated empty-of-visible patch with default vacuum,

\[
J^\nu_{\rm Mirron}
=
-
\Delta^\nu_{K}.
\]

That is the derived equation.

---

## 5. Explicit defect (weak-field, far zone)

In the Prime Minkowski chart used for the Poisson theorem, the leading piece of \(T^{00}_{K}\) is \(\rho_{\rm eff}=\sum_i\gamma_i(K_i\ast\rho_i)\). The associated current at \(O(\beta)\), after time average, has spatial part

\[
\Delta^{j}_{K}
=
\sum_{i=2}^{6}
\gamma_i
\int
\bigl(\partial_{x^j}\overline{G}_i\bigr)
\rho_i(x')\,d^{3}x'
+
O(\beta^2,\lambda_{m_0}/R).
\]

(Prime \(i=1\) with \(\beta_1=0\) drops out of the dipole sum if \(\rho_1=0\) in the empty interior.)

If hidden densities are quasi-static on Prime time,

\[
\Delta^0_{K}
=
\sum_{i=2}^{6}
\gamma_i
\int
\overline{G}_i\,
\partial_t\rho_i\,d^{3}x'.
\]

**Key.** \(\Delta^\nu_{K}\): four-divergence of the kernel tensor. Empty interior: \(\rho_1\approx 0\). Hidden \(\rho_{i\ge 2}\) need not vanish.

Interpretation: after EM cutoff, Prime can still gain or lose energy-momentum because the five hidden copies continue to stress it through \(K\). The engine account \(T_{M}\) is where that imbalance is booked if it is not already visible matter.

---

## 6. Eight-phase projector

Mirron ticks in eight internal phases \(\varphi_n=n\pi/4\), \(n=0,\ldots,7\).

\[
(\mathcal{P}_8 X)
:=
\frac18\sum_{n=0}^{7}
X\bigl(\varphi_n\bigr).
\]

**Key.** \(\mathcal{P}_8\): average over one Mirron cycle. \(\varphi\): internal 8-phase, not a spacetime coordinate.

Split the defect into a secular piece and a tick piece:

\[
\Delta^\nu_{K}
=
\mathcal{P}_8\Delta^\nu_{K}
+
(1-\mathcal{P}_8)\Delta^\nu_{K}.
\]

- \(\mathcal{P}_8\Delta_{K}\): change that survives a full refresh cycle. Candidate for a slow transfer into rest mass or vacuum-occupation.
- \((1-\mathcal{P}_8)\Delta_{K}\): eight-tick ripple. Averages to zero over a cycle. Not secular mass production.

The current that could source *new* standing rest mass is therefore

\[
J^\nu_{\rm Mirron,\,sec}
=
-
\mathcal{P}_8\Delta^\nu_{K}.
\]

The ripple is refresh noise.

This projector is kinematics of the 8-phase engine. It is not a derivation of \(m_0\).

---

## 7. Master equation

Default vacuum, isolated Prime interior, live-frame kernel:

\[
\boxed{
J^\nu_{\rm Mirron}
=
-
\nabla_\mu T^{\mu\nu}_{K}
=
-
\Delta^\nu_{K},
\qquad
J^\nu_{\rm Mirron,\,sec}
=
-
\mathcal{P}_8\Delta^\nu_{K}.
}
\]

With the operator written out:

\[
J^\nu_{\rm Mirron}(x)
=
-
\nabla_\mu
\sum_{i=1}^{6}
\gamma_i
\bigl(K_i\ast T_{(i)}\bigr)^{\mu\nu}(x).
\]

Arguments promised in the schematic \(J[K,\rho_{\rm vac},\{\beta_i\}]\):

- \(K\) enters as \(\{K_i\}\).
- \(\{\beta_i\}\) enter as \(\gamma_i\) and as the boost inside \(\overline{G}_i\).
- \(\rho_{\rm vac}\) does **not** enter unless vacuum decay is switched on. Default: it does not.

---

## 8. Charge and Bianchi

If the visible sector carries Maxwell current \(j^\mu_{\rm EM}\),

\[
\nabla_\mu j^\mu_{\rm EM}=0
\]

must hold separately. \(J_{\rm Mirron}\) is a *stress* current, not an electric current. Pair production booked through \(J_{\rm Mirron}\) must be charge-neutral or accompanied by a balancing \(j_{\rm EM}\). Isolation already set incoming wall photons to zero; it does not license charged unbalance.

Bianchi remains intact because \(T_{\rm tot}\) is still divergenceless. We only split the books.

---

## 9. What this is not

- Not a derivation of new baryon density from \(\rho_{\rm vac}\times\mathrm{Vol}\).
- Not a running Higgs VEV.
- Not Casimir of a megaparsec circle.
- Not a number. \(\Delta_K\) still depends on hidden \(\rho_i(x)\) in the isolated era, which this note does not compute.
- Not a trophy.

---

## 10. What would make it a production formula

Specify hidden \(\rho_i\) on the isolated patch (ansatz A does this only while densities stay equal and present). Then \(\mathcal{P}_8\Delta_K\) is a definite four-vector field. Integrate \(J^0_{\rm Mirron,\,sec}\) over the patch to get a power into the engine account. That integral is the next calculation. It is not done here.

---

## Master key

| Symbol | Meaning |
|---|---|
| \(T_{\rm tot},T_{\rm vis},T_K,T_{\rm vac},T_M\) | split of the source tensor |
| \(J_{\rm Mirron}^\nu\) | \(\nabla_\mu T^{\mu\nu}_M\) |
| \(\Delta_K^\nu\) | \(\nabla_\mu T^{\mu\nu}_K\) |
| \(K_i\ast\) | Yukawa average at \(\beta_i,\lambda_{m_0}\) |
| \(\mathcal{P}_8\) | 8-phase average |
| \(F_{\rm wall}\) | visible flux from walls; \(0\) after isolation |
| \(\rho_{\rm vac}\) | default constant; no current |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_Mirron_current_derivation_2026-09-20.md`
