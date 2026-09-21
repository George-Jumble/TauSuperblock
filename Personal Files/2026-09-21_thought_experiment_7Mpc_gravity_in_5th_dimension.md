# Thought experiment only (explicitly *not* TSB unification)

**Session:** 2026-09-21  
**Author context:** aside requested by William Brown  
**Scope:** What if gravity at the observational ~7 Mpc scale worked differently because a fifth spatial dimension becomes dynamically available there?  
**Status:** speculative kinematics / modified-gravity sketch. No claim that this is part of Tau-Superblock / Mirron / Tav Topology.

---

## 1. What “7 Mpc gravity” already means in the data

Three nearby scales sit on top of each other and are easy to conflate:

| Scale | Typical number | What is measured |
|---|---|---|
| Local Group zero-velocity surface | \(R_0^{\rm LG}\simeq 0.96\pm 0.03\,\mathrm{Mpc}\) | Bound pair MW+M31; cold local Hubble flow just outside |
| Local Sheet / “quiet Hubble flow” edge | \(\sim 5{-}7\,\mathrm{Mpc}\) | Peculiar-velocity dispersion drops to \(\sigma_v\sim 15{-}40\,\mathrm{km\,s^{-1}}\); linear Hubble flow despite lumpy matter |
| Virgo zero-velocity / zero-gravity radii | \(R_0^{\rm Virgo}\sim 5{-}7.5\,\mathrm{Mpc}\), \(R_{\rm ZG}\sim 9{-}11\,\mathrm{Mpc}\) | Infall vs. Hubble expansion around Virgo; Λ antigravity vs. cluster gravity |

The puzzle that makes the thought experiment interesting is the **coldness** of the flow inside ~7 Mpc: the matter field is lumpy, yet the velocity field is almost laminar. Standard explanations invoke dark energy’s antigravity (Chernin et al.) plus the flattened Local Sheet geometry (Tully / Karachentsev). The aside asked here is different: *suppose the fifth dimension, not Λ, is what changes the force law at that scale.*

Observational anchors used below (not TSB-derived):

- Karachentsev 2009: \(H_{\rm loc}=(78\pm 2)\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\), \(\sigma_v\simeq 25\,\mathrm{km\,s^{-1}}\) for \(0.7 < D_{\rm LG} < 3\,\mathrm{Mpc}\), \(R_0^{\rm LG}=0.96\,\mathrm{Mpc}\).
- Karachentsev & Nasonova 2010: Virgo \(R_0 \simeq 5{-}7.5\,\mathrm{Mpc}\).
- Tully 2008 “Local Velocity Anomaly”: coherent peculiar-velocity pattern only begins *beyond* ~7 Mpc; inside the Local Sheet the flow is Hubble-like.
- Chernin / Teerikorpi: zero-gravity radius \(R_Q\) where \(Λ\) repulsion overtakes a mass concentration; for LG, \(R_Q\sim 1.5\,\mathrm{Mpc}\); for Virgo, \(R_{\rm ZG}\sim 10\,\mathrm{Mpc}\).

---

## 2. The thought-experiment rule

Keep 4D Einstein gravity *inside* galaxies and *inside* virialized groups. Allow a fifth dimension to change the force law only once the 3D proper separation reaches

\[
r_c \;\equiv\; 7\,\mathrm{Mpc}.
\]

Two concrete 5D mechanisms, then a third more exotic option.

### Variable key for the whole note

| Symbol | Meaning | Typical value in this note |
|---|---|---|
| \(r\) | 3D proper distance between two masses | variable |
| \(r_c\) | 4D↔5D crossover / leakage scale | \(7\,\mathrm{Mpc}\) |
| \(R_0\) | zero-velocity (turnaround) radius of a group/cluster | LG \(\sim 1\,\mathrm{Mpc}\), Virgo \(\sim 7\,\mathrm{Mpc}\) |
| \(R_{\rm ZG}\) or \(R_Q\) | zero-gravity radius (attraction = Λ repulsion) | Virgo \(\sim 10\,\mathrm{Mpc}\) |
| \(G_4\) | 4D Newton constant | \(6.67430\times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}\) |
| \(G_5\) | 5D Newton constant | \(G_5 = G_4 \cdot r_c\) in the simplest matching |
| \(M\) | source mass | LG \(\sim 2\times 10^{12}\,M_\odot\), Virgo \(\sim 10^{15}\,M_\odot\) |
| \(r_S = 2G_4 M/c^2\) | Schwarzschild radius of \(M\) | — |
| \(r_V\) | Vainshtein radius (screening radius) | computed below |
| \(\Phi_4, \Phi_5\) | Newtonian gravitational potentials in 4D / 5D | — |
| \(F_4, F_5\) | force on a test mass \(m\) | — |
| \(H_0\) | present Hubble parameter | \(70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) used for numbers |
| \(c\) | speed of light | \(2.99792458\times 10^8\,\mathrm{m\,s^{-1}}\) |
| \(\sigma_v\) | 1-D peculiar-velocity dispersion | observed \(\sim 15{-}40\,\mathrm{km\,s^{-1}}\) inside 7 Mpc |
| \(\lambda_g\) | graviton Compton wavelength | set equal to \(r_c\) in Mechanism B |
| \(m_g\) | graviton mass | \(m_g = \hbar/(\lambda_g c)\) |
| \(\Omega_m, \Omega_\Lambda\) | present density parameters | only used for comparison with ΛCDM \(R_{\rm ZG}\) |
| \(\rho_\Lambda = \Lambda c^2/(8\pi G_4)\) | dark-energy density | \(\simeq 6\times 10^{-27}\,\mathrm{kg\,m^{-3}}\) |
| \(a(t)\) | FRW scale factor | not evolved here; thought experiment is local |
| \(y\) | extra-dimensional coordinate | Mechanism A, DGP-like |
| \(r_* = (G_5 M)^{1/2}\) | 5D gravitational radius | Mechanism A |

Unit conversion used:

\[
1\,\mathrm{Mpc} = 3.085677581\times 10^{22}\,\mathrm{m},
\qquad
7\,\mathrm{Mpc} = 2.160\times 10^{23}\,\mathrm{m}.
\]

---

## 3. Mechanism A — DGP-like leakage at \(r_c = 7\,\mathrm{Mpc}\)

### 3.1 Force law

In the Dvali–Gabadadze–Porrati construction a 3-brane (our 3+1 world) has an induced 4D Einstein–Hilbert term. Gravity stays 4D at short distance and leaks into a 5D Minkowski bulk beyond \(r_c\).

Newtonian limits on the brane (weak field, quasi-static):

\[
\Phi_4(r) = -\frac{G_4 M}{r}
\qquad (r \ll r_c),
\]

\[
\Phi_5(r) = -\frac{G_5 M}{r^2} = -\frac{G_4 M\, r_c}{r^2}
\qquad (r \gg r_c).
\]

Corresponding forces on a test mass \(m\):

\[
F_4 = -\frac{G_4 M m}{r^2},
\qquad
F_5 = -\frac{2 G_4 M m\, r_c}{r^3}.
\]

Matching \(G_5 = G_4 r_c\) is the standard DGP interpolation so that \(\Phi\) and the 4D Planck mass are continuous at \(r\sim r_c\). A smooth interpolating potential often used in phenomenology is

\[
\Phi(r) = -\frac{G_4 M}{r}\left[1 + \frac{2}{3}\left(\sqrt{1+\frac{4r_c}{r}}-1\right)^{-1}\right]^{-1}
\]

(up to Vainshtein corrections; the exact DGP Green function is more involved). The qualitative content is enough: **beyond 7 Mpc the force falls faster than Newton**, \(\propto r^{-3}\).

### 3.2 Vainshtein screening — why the Solar System and galaxy disks can survive

DGP (and massive gravity) screens the extra scalar polarization inside

\[
r_V \;\sim\; \bigl(r_S\, r_c^2\bigr)^{1/3}
\;=\;
\left(\frac{2G_4 M}{c^2}\, r_c^2\right)^{1/3}.
\]

**Milky Way** (\(M\simeq 10^{12}\,M_\odot\)):

\[
r_S(M) = 2.95\,\mathrm{km}\times\frac{M}{M_\odot}.
\]

\[
r_S^{\rm MW}(10^{12}M_\odot) = 2.95\times 10^{12}\,\mathrm{km} = 9.6\times 10^{-2}\,\mathrm{pc} = 2.95\times 10^{15}\,\mathrm{m}.
\]

Then

\[
r_V^{\rm MW}
= \bigl(2.95\times 10^{15}\times (2.16\times 10^{23})^2\bigr)^{1/3}
= \bigl(1.38\times 10^{62}\bigr)^{1/3}
\simeq 5.2\times 10^{20}\,\mathrm{m}
\simeq 17\,\mathrm{kpc}.
\]

**Virgo cluster** (\(M\simeq 10^{15}\,M_\odot\)): \(r_S\) is \(10^3\) times larger, so \(r_V\) scales as \(M^{1/3}\):

\[
r_V^{\rm Virgo} \simeq 170\,\mathrm{kpc}.
\]

**Local Group as a whole** (\(M\simeq 2\times 10^{12}\,M_\odot\)): \(r_V^{\rm LG}\simeq 21\,\mathrm{kpc}\).

Interpretation of the thought experiment:

- Inside a galactic disk (\(r\sim 10\,\mathrm{kpc}\)) one is at or inside \(r_V\). 4D Newton / GR is recovered. Rotation curves, lensing inside galaxies, Solar-System PPN tests are *not automatically destroyed*.
- The space *between* galaxies in the Local Sheet (\(0.5{-}7\,\mathrm{Mpc}\)) is far outside every individual \(r_V\). Gravity there is the leaked 5D law.
- Virgo’s virial core (\(\sim 1\,\mathrm{Mpc}\) is still \(\gg r_V^{\rm Virgo}\)). The cluster interior would itself feel a partially leaked force unless one adds a density-dependent screening (chameleon / k-mouflage) on top of Vainshtein. That is an extra assumption, not given by vanilla DGP.

So the “7 Mpc fifth dimension” is *not* a statement about extra dimensions of micron or TeV size. It is a statement that **the induced 4D Einstein term is so weak that leakage already happens on group scales**, with Vainshtein hiding the extra force only inside individual galaxies.

### 3.3 What the leaked force does to the quiet Hubble flow

In 4D Newtonian cosmology the peculiar acceleration of a test galaxy at distance \(r\) from a lump of mass \(M\) is

\[
\ddot r = -\frac{G_4 M}{r^2} + \frac{\Lambda c^2}{3}\, r
\qquad\text{(plus the background Hubble drag)}.
\]

Replace the first term by the 5D force for \(r\gtrsim r_c\):

\[
\ddot r\Big|_{5D} = -\frac{2 G_4 M r_c}{r^3} + \frac{\Lambda c^2}{3}\, r.
\]

Compare magnitudes at \(r = r_c = 7\,\mathrm{Mpc}\) for a Virgo-like mass \(M=10^{15}M_\odot\):

\[
\frac{G_4 M}{r_c^2}
\;\text{vs}\;
\frac{2 G_4 M r_c}{r_c^3} = \frac{2 G_4 M}{r_c^2}.
\]

At the matching surface the 5D force is *twice* the 4D Newton force (the factor 2 from \(d(1/r^2)/dr\)). Just outside \(r_c\) it then drops *faster* than Newton, so the gravitational tug of Virgo on a galaxy at 15–20 Mpc is weaker than in 4D.

Consequences that are actually useful for the 7 Mpc puzzle:

1. **Weaker long-range pull from Virgo and the Great Attractor.** The Local Sheet would be less stirred. That helps the observed small \(\sigma_v\).
2. **A sharper kinematic edge near 7 Mpc.** Inside \(r_c\) one still has 4D \(1/r^2\) (modulo screening). Crossing \(r_c\) the force law changes slope. That is a possible origin of the “pattern of peculiar velocities only begins beyond ~7 Mpc” reported by Tully.
3. **A shifted zero-velocity surface.** Setting \(\dot r = 0\) in a spherical collapse model with a 5D exterior force moves \(R_0\). Because the exterior force is steeper, turnaround can sit closer to the mass — qualitatively in the direction of the compact observed \(R_0^{\rm Virgo}\sim 7\,\mathrm{Mpc}\).
4. **Dark-energy is no longer required to “cool” the local flow.** Chernin’s argument was that \(Λ\) repulsion dominates outside \(R_Q\) and laminarizes the flow. Here the fifth dimension *removes* the long-range \(1/r^2\) tail instead of cancelling it with a \(+r\) term. Same phenomenological cooling, different agent.

### 3.4 The price

Vanilla DGP with \(r_c = 7\,\mathrm{Mpc}\) is not a viable global cosmology. The modified Friedmann equation on the brane is

\[
H^2 \pm \frac{H}{r_c} = \frac{8\pi G_4}{3}\rho,
\]

where the sign chooses the normal / self-accelerating branch. With \(r_c \ll c/H_0 \simeq 4300\,\mathrm{Mpc}\), the \(H/r_c\) term dominates the entire expansion history. One would need:

- a different bulk (warped AdS, cascading extra dimensions, or a mass term that is environment-dependent), or
- to treat \(r_c = 7\,\mathrm{Mpc}\) as a *local, density-triggered* scale rather than a fundamental constant.

That last option is the honest version of the thought experiment: the fifth dimension is always there, but the 4D induced term plus Vainshtein make it invisible until one looks at underdense, group-scale separations.

---

## 4. Mechanism B — a 5D graviton whose Compton wavelength is 7 Mpc

Give the 4D graviton a mass from the extra dimension (KK reduction, or a resonance of finite width as in some infinite-volume extra-dimension models).

\[
\lambda_g = r_c = 7\,\mathrm{Mpc},
\qquad
m_g = \frac{\hbar}{\lambda_g c}.
\]

Numerically

\[
\hbar c = 1.973269804\times 10^{-13}\,\mathrm{MeV\cdot m},
\]

\[
m_g c^2 = \frac{\hbar c}{\lambda_g} = \frac{1.973\times 10^{-13}}{2.160\times 10^{23}}\,\mathrm{MeV}
= 9.13\times 10^{-37}\,\mathrm{MeV}
= 9.13\times 10^{-31}\,\mathrm{eV}.
\]

Yukawa–plus–scalar potential of a massive graviton (Fierz–Pauli, linearized):

\[
\Phi(r) = -\frac{G_4 M}{r}\,e^{-r/\lambda_g}\left(1 + \frac{r}{\lambda_g}\right)
\quad\text{plus a scalar polarization \(\frac13\) that must be screened}.
\]

(The exact tensor structure is \(\propto (\bar h_{\mu\nu} - \tfrac12 \bar h \eta_{\mu\nu})\) with five degrees of freedom.)

At \(r\ll \lambda_g\) one recovers Newton (after Vainshtein eats the extra scalar). At \(r\gg \lambda_g\) gravity is exponentially shut off. That is a *stronger* modification than Mechanism A: Virgo would not pull at all on the Local Sheet if the Sheet–Virgo separation is \(\gtrsim\lambda_g\). Observed Virgocentric infall of \(\sim 180\,\mathrm{km\,s^{-1}}\) at ~17 Mpc would then have to be reassigned to 4D screened gravity *inside* a larger Vainshtein radius, or to a different mass. This mechanism is therefore harsher and easier to kill with existing peculiar-velocity data, unless \(\lambda_g\) is several tens of Mpc rather than 7.

LIGO/Virgo/KAGRA bound \(m_g \lesssim 10^{-22}\,\mathrm{eV}\) from GW170817 assumes an unscreened, Lorentz-invariant massive graviton propagating on the same background as photons. A 5D origin with Vainshtein and a brane-localized matter sector is not the same theory; the bound does not apply off the shelf. Still, any concrete model must say how gravitational waves of 100 Hz stay massless while a static 7 Mpc mode is massive — typically by making the mass a resonance with width \(\Gamma \sim H_0\), not a hard Pauli–Fierz mass.

---

## 5. Mechanism C — the fifth dimension carries a *different* gravitational coupling (including a possible sign flip)

This is the most “aside-like” reading of the question: gravity in the 5th dimension is not merely leaked 4D gravity; it is a different interaction.

Write a 5D Einstein–Hilbert term with its own cosmological constant and a possible 5D Einstein-tensor coupling to brane matter:

\[
S = \frac{1}{16\pi G_5}\int d^5x\sqrt{-g_5}\,(R_5 - 2\Lambda_5)
+ \frac{1}{16\pi G_4}\int d^4x\sqrt{-g_4}\,R_4
+ S_{\rm matter}[g_4].
\]

Three qualitatively different 5D behaviours, all still at the 7 Mpc threshold:

1. **Weaker 5D coupling** (\(G_5/r_c \ll G_4\)). Leakage *reduces* the effective \(G\) at \(r>r_c\). Quiet flow is even quieter. Structure growth on 10–50 Mpc is suppressed. This fights observed bulk flows (Watkins / CosmicFlows-4), which if anything want *more* pull on 50 Mpc scales, not less.
2. **Stronger 5D coupling.** Opposite problem: the Local Sheet would be more turbulent, contradicting \(\sigma_v\sim 25\,\mathrm{km\,s^{-1}}\).
3. **Sign-reversed 5D curvature / negative \(G_5\)** (a 5D “antigravity” mode). Then the leaked force at \(r>r_c\) is repulsive. That *is* a geometric stand-in for Chernin’s \(Λ\) term, but it switches on at a fixed *length* rather than a fixed *density*. The zero-gravity surface would lock to \(r_c\) itself:

\[
R_{\rm ZG} \;\approx\; r_c \;=\; 7\,\mathrm{Mpc},
\]

almost independent of the central mass — which is *not* what the Virgo vs. LG comparison shows (\(R_Q\) scales with \(M^{1/3}\)). A pure sign-flip therefore fails the mass-scaling test unless the 5D repulsion is itself sourced by the mass (a 5D Weyl or conformal piece). That last option starts to resemble conformal / twistor-inspired gravity and is the one place this aside brushes other work — flagged here only to keep the boundary explicit: **this note does not import TSB, Mirron, or twistor averaging**.

---

## 6. What would have to be true for the thought experiment to be interesting rather than immediately dead

A viable “7 Mpc fifth dimension” needs all four of the following at once:

1. **Screening inside \(\sim 20\,\mathrm{kpc}\)** so galaxy rotation curves and PPN parameters stay standard. Vainshtein with \(r_c=7\,\mathrm{Mpc}\) already gives this for MW-mass objects (Section 3.2). That is the least exotic part.
2. **A kinematic edge at 7 Mpc**, not at 0.7 Mpc and not at 70 Mpc. That requires the crossover to be a proper-distance threshold, not a redshift or density threshold alone. Density-triggered screening (chameleon) would put the transition at different radii around different masses and would smear the observed Local-Sheet edge.
3. **Enough residual 4D pull to keep Virgocentric infall.** Mechanism A (power-law leakage) can do this; Mechanism B (hard Yukawa at 7 Mpc) probably cannot.
4. **A bulk that does not wreck the Friedmann equation.** Either \(r_c\) is not a universal constant, or the extra dimension is warped / cascaded so that the *cosmological* leakage scale is \(c/H_0\) while a *local* resonance sits at 7 Mpc. That is a two-scale 5D model, not textbook DGP.

If those four hold, the observational payoffs would be:

- a predicted break in the two-point peculiar-velocity correlation at \(r\simeq 7\,\mathrm{Mpc}\);
- a scale-dependent effective \(G_{\rm eff}(r)\) measurable from the pairwise velocity statistic \(\langle v_{12}(r)\rangle\);
- a mismatch between lensing mass and dynamical mass that *grows* from 1 Mpc to 20 Mpc and then saturates (5D force falls faster, so the mismatch does not keep growing);
- no new force inside the Milky Way disk.

None of those is claimed as data. They are the checklist that would make the aside more than a metaphor.

---

## 7. Edge cases and related considerations

- **Anisotropic extra dimension.** If the fifth dimension has a preferred embedding relative to the Local Sheet (the Sheet is already a flattened structure in supergalactic coordinates), leakage could be anisotropic. Tangential peculiar velocities would then carry a handedness. CosmicFlows-4 analyses of tangential residuals exist; they are not evidence for a 5th dimension, but they are the right observable.
- **Time dependence.** If \(r_c\) tracks the Hubble radius, \(r_c(t)\propto 1/H(t)\), then at \(z\sim 1\) the crossover was \(\sim 3.5\,\mathrm{Mpc}\) proper and the “quiet flow” scale would have been smaller. High-\(z\) group kinematics could kill or support that.
- **Gravitational waves.** A 5D leakage scale of 7 Mpc does *not* change the 100 Hz wave speed. It can change the infrared propagator of the helicity-0 mode. Pulsar-timing arrays sit closer to the relevant band than LIGO does.
- **Relation to MOND.** MOND’s acceleration scale \(a_0\simeq 1.2\times 10^{-10}\,\mathrm{m\,s^{-2}}\) corresponds, for a \(10^{12}M_\odot\) galaxy, to a radius \(\sqrt{G_4 M/a_0}\sim 8\,\mathrm{kpc}\) — galactic, not 7 Mpc. A 7 Mpc fifth dimension is *not* MOND.
- **Relation to the Hubble tension.** A local 5D modification that only operates at 7–30 Mpc can change the local distance ladder’s peculiar-velocity corrections without touching the CMB sound horizon. That is a logically open door; it is not a calculation.
- **What this is not.** It is not a compactification at the Planck scale, not ADD extra dimensions (those modify gravity below 0.1 mm), not RS1 (hierarchy), not the “dark dimension” of micron size, and not TSB / Mirron / 7-fold Tav resonance. The number 7 here is megaparsecs, from Local-Sheet / Virgo kinematics, not from a discrete harmonic.

---

## 8. Compact summary of the aside

If gravity “worked differently in the 5th dimension” at 7 Mpc, the least immediately-dead version is:

> A DGP-like (or cascaded) extra dimension whose *local* leakage / resonance scale is the Local-Sheet edge, with Vainshtein radii of order 10–20 kpc around MW-mass galaxies. Inside galaxies, 4D GR. Between galaxies beyond ~7 Mpc, the force falls as \(1/r^3\) (or is partially Yukawa-suppressed). The quiet Hubble flow is then a 5D kinematic effect: the long-range Newtonian tails that would have stirred the Local Sheet are leaked into the bulk.

The same construction, taken as a universal \(r_c\), destroys the Friedmann equation. So the thought experiment is only coherent as a *two-scale* 5D theory: cosmological leakage at \(c/H_0\), group-scale leakage at 7 Mpc. That is allowed as a sketch. It is not a model, and it is not part of TSB.

---

## 9. Query / source log (results of searches used)

- Local 7 Mpc / quiet Hubble flow / Virgo \(R_0\): Karachentsev 2009 MNRAS 393, 1265; Karachentsev & Nasonova 2010; Tully 2008 “Local Velocity Anomaly”; Chernin et al. on \(R_Q\) and dark-energy laminarization.
- Extra-dimension gravity at cosmological / 100 Mpc scales: DGP; Afshordi, Geshnizjani, Khoury 2008 (they wanted \(r_c\sim 300{-}600\,\mathrm{Mpc}\), *not* 7); Wyman & Khoury on enhanced peculiar velocities in brane-induced gravity.
- Massive / resonant graviton cosmology and bulk-flow enhancement: arXiv:1004.2046 and related DGP peculiar-velocity papers.
- Dark dimension / micron extra dimension (explicitly *not* used as the 7 Mpc mechanism): Vafa et al.; noted only to keep scales distinct.

End of aside.
