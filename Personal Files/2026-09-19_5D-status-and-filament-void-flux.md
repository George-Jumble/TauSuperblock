# 5D status, and filaments vs voids as flux

**Session date:** 19 September 2026  
**Constraints from this turn:** Do not hard-code “Tau circle = product of time” into the framework. Ask whether the 5D superstructure is dead, and what would correlate \(7h^{-1}\,\mathrm{Mpc}\) with hot filaments and cold voids.  
**Short answer:** The *metric 5D circle* is dead as laboratory gravity. The *internal* Superblock superstructure (supersphere, six domains, phase labels) is not. Filament heat / void cold is already partly ordinary hydro. A TSB-specific account has to be extra dissipation where the inter-domain kernel chokes at the coherence scale — and that is a hypothesis, not a locked axiom.

---

## Variable key

| Symbol | Meaning |
|---|---|
| \(g_{\mu\nu}^{(i)}\) | 3+1 metric of domain \(i\) |
| supersphere | internal space on which the six domains are co-located |
| \(\phi\) | internal phase label (not a locked time-product) |
| \(\tau_{\rm web}\) | observed web scale \(\sim 7h^{-1}\,\mathrm{Mpc}\) |
| \(\mathcal K_{ij}(x,x')\) | inter-domain impulse kernel |
| \(\ell_C\) | coherence / exhaustion length of \(\mathcal K\) or of a phase correlator |
| \(\Pi\) | dissipative stress (bulk / shear) in the effective fluid |
| \(\theta=\nabla\cdot u\) | expansion scalar |
| \(T_{\rm fil},T_{\rm void}\) | characteristic IGM temperatures |
| WHIM | warm–hot intergalactic medium, standard web gas |

---

## 1. The time-product reading stays provisional

The previous note is a *possible* ontology for \(\tau_{\rm web}\). It is not framework law. Do not put it in an action, a preregistration, or a public abstract until a correlator actually computes 7 in \(h^{-1}\) units.

Until then \(\tau_{\rm web}\) is an observed clustering scale that TSB would like to name. Naming is not deriving.

---

## 2. Which 5D is dead, which is not

Do not collapse this to “only 4D works.” There are three different extra structures in the corpus.

**Dead as TSB gravity**

\[
S_5=\frac{1}{16\pi G_5}\int d^5x\sqrt{-g_5}\,R_5,
\qquad
y\in[0,2\pi\tau],
\qquad
\tau=7h^{-1}\,\mathrm{Mpc},
\qquad
G_4=G_5/(2\pi\tau).
\]

That object is a metric extra *spacetime* dimension of laboratory-illegal size. Inverse-square-law tests kill it unless gravitational influence does not propagate in \(y\). If it does not propagate in \(y\), this action was the wrong picture of that gravity.

**Not dead**

- Each domain is still 3+1 dimensional.
- The six domains still need an *internal* space in which they are co-located without sharing Maxwell rays. That internal space is the supersphere. It is extra structure. It is not a fifth lab direction.
- Phase labels, twistor space, octonionic clocks, Mirron cells: internal. They do not have to be 4D fields on Minkowski space.
- A 5D (or higher) *action on internal coordinates* remains allowed if those coordinates are not arguments of the Cavendish kernel.

So: **4D spacetime for local light and local gravity. Higher-D internal geometry for domains and phases.** That is not “only 4D.” It is “no large metric extra dimension in the gravitational kernel.”

A slogan that is accurate:

> The 5D KK circle is dead. The Superblock superstructure is internal, not compactified spacetime.

If a later calculation *derives* an effective 5th metric direction that gravity does not wrap, that is a new paper. It is not the default.

---

## 3. Filaments hot, voids cold: what is already explained

In ordinary cosmology, with no TSB:

- Matter streams out of voids into walls and filaments.
- Gas falling into filaments shock-heats. The WHIM sits at \(10^5\)–\(10^7\,\mathrm{K}\).
- Voids are underdense, little shocking, adiabatic cooling. They are cold.

So “heated filaments / cold voids” is not, by itself, a TSB signature. Any theory with gravity plus baryons plus a web gets that qualitative split. A referee will say “that is the cosmic web.”

TSB only has a new explanation if it adds a *scale* and a *channel* that ΛCDM hydro does not already use.

The interesting correlation is not “filaments are hot.” It is:

> the heating / choking scale sits at the same \(\sim 7h^{-1}\,\mathrm{Mpc}\) as the web fracture, *and* the extra heat is from flux in \(\mathcal K_{ij}\) (or Phase-7 / Mirron flux), not only from baryonic accretion shocks.

Until that “and” is measured or at least defined, do not treat WHIM as evidence for Tav.

---

## 4. A TSB-native account that is allowed as a hypothesis

Keep this labeled **hypothesis**, not framework.

Suppose the inter-domain kernel (or the phase correlator) has a coherence length \(\ell_C\). On scales \(\ll\ell_C\), impulse is smooth: flux can be transported with little dissipation. On scales \(\sim\ell_C\), the kernel can no longer stay coherent: flux must redirect. Redirection plus a bulk viscous piece \(\Pi\) thermalizes.

Then, schematically:

- **Voids.** Density and phase gradients small. Kernel unencumbered. \(\theta>0\), little shocking, little \(\Pi\). Cold.
- **Filaments.** Matter and phase gradients packed into sheets and threads at the exhaustion scale. Kernel chokes. \(\Pi\neq 0\). Heat.

That is a *transport* statement:

\[
\nabla_b T^{ab}_{\rm eff}
=0,
\qquad
T^{ab}_{\rm eff}
=(\rho+p)u^a u^b+p g^{ab}+\Pi\Delta^{ab},
\qquad
\Pi
=-\zeta\theta+\Pi_{\rm choke}(\ell_C,\nabla\phi).
\]

**Key:** \(\Pi_{\rm choke}\) is extra dissipation turned on where the phase / kernel gradient varies on \(\ell_C\). \(\zeta\theta\) is ordinary bulk viscosity. The TSB increment is \(\Pi_{\rm choke}\).

If \(\ell_C\) is later identified with \(\tau_{\rm web}\), filaments heat at that scale because that is where flux is forced to turn. Voids stay cold because flux there never hits the choke.

What this needs before it is more than a picture:

1. A definition of “flux” — impulse in \(\mathcal K\), Phase-7 Mirron current, conformal current, or baryons. Pick one.
2. A choke condition, e.g. \(|\nabla\phi|\,\ell_C\sim 1\) or \({\rm Re}_{\mathcal K}\sim 1\), frozen *before* looking at a catalogue.
3. A prediction that is not just “overdense gas is hot”: for example a characteristic WHIM temperature–scale relation, a preferred filament width, or a heating term that does not track \(\rho\) the way shocks do.
4. A null: if DESI / simulations show the heat scale tracking ordinary virial / shock physics with no extra feature at \(7h^{-1}\,\mathrm{Mpc}\), \(\Pi_{\rm choke}\) is out.

Item 4 is mandatory. The web is already hot in the right places without TSB.

---

## 5. How this sits next to the time-product idea (still not locked)

If someone later *does* derive \(\ell_C=7h^{-1}\,\mathrm{Mpc}\) from a clock average, filament choking would be the dissipative face of the same correlator that prints the web scale. That would be one object doing two jobs: length and heat.

That identification is attractive and not licensed yet. Today the inventory is:

- internal superstructure: alive,
- metric 5D circle: dead,
- \(\tau_{\rm web}\): observed,
- filament/void thermal split: mostly standard hydro,
- extra choke at \(\ell_C\): optional hypothesis,
- time-product origin of \(\ell_C\): optional hypothesis, not coded.

Two optional hypotheses stacked are not a unification.

---

## 6. What to compute if you want the flux picture

Not another slogan. One diagnostic.

Define a scalar

\[
Q_{\rm choke}(x)
=\Pi_{\rm choke}(x)\,u_a\nabla^a s
\]

or, simpler, the work term \(-\Pi\theta\). Map it on a simulation or on a DESI web catalogue as a function of distance to the nearest filament, binned in \(h^{-1}\,\mathrm{Mpc}\). If \(Q_{\rm choke}\) peaks at \(\sim 7\) *after* ordinary shock heating is subtracted, you have a TSB handle. If it peaks wherever \(\rho\) peaks, you have ΛCDM hydro in new clothes.

That test does not require locking the time-product story. It does not require resurrecting \(S_5\). It does require saying what flux is.

---

## File location

`Tau-Superblock-Universe/Personal-Files/2026-09-19_5D-status-and-filament-void-flux.md`
