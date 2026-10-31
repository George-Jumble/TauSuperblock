# Session: Gravitation on proper time — early universe vs now

- **Session date:** 2026-09-21
- **Source prompt (verbatim):** “Look at the effects of gravitation on proper time in the early universe as compared to the current universe--”
- **Parent module:** Bang Distance Clock (BDC), `2026-09-21_bang_distance_privileged_clock.md`
- **Corpus status:** *Live companion to BDC.* Bounce remains conformal aeon crossover + Mirron / Planck–Kerr refresh. No 7 Mpc / seventh-phase clock slot. Gatlin compact-S¹ layer not used. “Mirron,” never “soliton.”
- **This file:** `Personal Files/2026-09-21_gravitation_on_proper_time_early_vs_now.md`
- **Repo:** `George-Jumble/TauSuperblock` (branch `main`)
- **Drive folder:** Personal Files (`1Q8kRH_SrMUM-aBtyIIVq2nHgZWh9SJnk`)

---

## 0. The question, split into three questions

“Did gravity make clocks run slower in the early universe?” is three different claims.

| # | Claim | Verdict |
|---|---|---|
| Q1 | Did the *background* gravitational field of FLRW make comoving proper time lag cosmic time? | **No.** For the Hubble-flow congruence, proper time *is* cosmic time. There is no leftover Newtonian well of “the universe as a whole.” |
| Q2 | Were *potential perturbations* deeper then, so clocks in overdensities lagged more? | **Opposite of popular intuition.** Linear \(\Phi/c^2\sim 10^{-5}\) then and on large scales now. Deep wells (\(\Phi/c^2\sim 10^{-6}\) to \(0.2\)) are a *late* product of collapse. Early universe is the smoother clock environment. |
| Q3 | Was spacetime curvature larger then, so gravitational physics ran hotter? | **Yes, by many orders of magnitude — but it is Ricci curvature of a nearly homogeneous fluid, not Weyl curvature of bound wells.** That is the Penrose split, and it is the TSB split. |

The BDC (D2) already *is* the proper time of the orthogonal congruence from \(\mathcal{B}\). Gravitation enters that number only through the Friedmann function \(E(a)\). Spatial gravitational time dilation is a *correction* \(\tau_{\mathrm{obs}}-T_{\mathrm{BB}}\).

---

## 1. Variable key

| Symbol | Meaning |
|---|---|
| \(\tau\) | Proper time along a worldline, \(\mathrm{d}\tau=\sqrt{-g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu}/c\) |
| \(t\) | Cosmic time = proper time of the Hubble-flow congruence (BDC D2) |
| \(T_{\mathrm{BB}}(p)=t_\perp(p)\) | Bang-distance physical age of event \(p\) |
| \(\eta\) | Conformal time; BDC D3 is \(\ell_{\mathrm{BB}}^{\mathrm{conf}}=c\eta\) |
| \(a(t)\) | Scale factor, \(a(t_0)=1\) |
| \(H=\dot a/a\) | Hubble parameter (1/s when used in SI) |
| \(H_0\) | Present Hubble parameter. Working value \(67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}=2.184\times 10^{-18}\,\mathrm{s^{-1}}\) |
| \(E(a)\) | \(H(a)/H_0=\sqrt{\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda}\) |
| \(\Omega_r,\Omega_m,\Omega_\Lambda\) | Present density parameters. Working: \(9\times 10^{-5}\), \(0.315\), \(0.685\) |
| \(\rho,p\) | Energy density and pressure of the cosmic fluid |
| \(\rho_{c0}=3H_0^2/(8\pi G)\) | Present critical density \(\approx 8.53\times 10^{-27}\,\mathrm{kg\,m^{-3}}\) |
| \(R\) | Ricci scalar of the background |
| \(C_{\alpha\beta\gamma\delta}\) | Weyl tensor (tidal / conformal curvature) |
| \(\Psi,\Phi\) | Newtonian-gauge metric potentials. Line element below |
| \(\Phi_N=-GM/(rc^2)\) | Dimensionless Newtonian potential (same order as \(\Psi\)) |
| \(z\) | Redshift, \(1+z=1/a_{\mathrm{emit}}\) |
| \(c\) | \(2.99792458\times 10^8\,\mathrm{m\,s^{-1}}\) |
| \(G\) | \(6.67430\times 10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}\) |
| \(\Lambda\) | Cosmological constant. Working \(\Lambda\approx 1.09\times 10^{-52}\,\mathrm{m^{-2}}\) |
| \(u^\mu\) | 4-velocity of the clock |
| \(v_{\mathrm{pec}}\) | Peculiar 3-velocity relative to Hubble flow |
| \(\gamma_{\mathrm{pec}}=(1-v_{\mathrm{pec}}^2/c^2)^{-1/2}\) | Special-relativistic factor from peculiar motion |
| \(\Delta\tau/\tau\) | Fractional clock-rate offset versus the cosmic-mean slice |
| \(\Sigma_{\mathrm{M}}\) | Mirron 2-surface |
| \(\Delta t_\tau\) | Local PK / Tav tick (engine period; not the cosmic clock) |
| \(\mathcal{B}\) | Bang 3-surface of the present aeon |
| \(t_0\) | Present cosmic age \(\approx 13.79\,\mathrm{Gyr}\) |
| \(\eta_0\) | Present conformal time \(\approx 46.14\,\mathrm{Gyr}\) (so \(c\eta_0\approx 46.14\,\mathrm{Gly}\)) |

Newtonian-gauge line element used for wells:

\[
\mathrm{d}s^2=-(1+2\Psi)c^2\mathrm{d}t^2+a^2(1-2\Phi)\delta_{ij}\mathrm{d}x^i\mathrm{d}x^j.
\]

**Key.** \(\Psi\): Newtonian-gauge lapse perturbation (negative in a well). \(\Phi\): spatial curvature perturbation. At linear order, no anisotropic stress \(\Rightarrow\Phi=\Psi\). A clock at fixed spatial coordinate has

\[
\mathrm{d}\tau=\sqrt{1+2\Psi}\,\mathrm{d}t\approx\bigl(1+\Psi\bigr)\,\mathrm{d}t.
\]

Synchronous-comoving gauge: the same Hubble-flow clock is defined to have \(\mathrm{d}\tau=\mathrm{d}t\) exactly. The two statements are compatible: \(\Psi\) is the offset of that clock *relative to a coordinate \(t\) that is not its proper time*. The BDC uses the synchronous-comoving reading as the privileged stamp, and files \(\Psi\) under \(\tau_{\mathrm{obs}}-T_{\mathrm{BB}}\).

---

## 2. Background gravity: what “stronger then” actually means

Einstein equation on FLRW (flat, \(\Lambda\) kept):

\[
H^2=\frac{8\pi G}{3}\rho+\frac{\Lambda c^2}{3},\qquad
\frac{\ddot a}{a}=-\frac{4\pi G}{3}\Bigl(\rho+\frac{3p}{c^2}\Bigr)+\frac{\Lambda c^2}{3}.
\]

Ricci scalar of the background:

\[
R=\frac{8\pi G}{c^2}\Bigl(\rho-\frac{3p}{c^2}\Bigr)+4\Lambda.
\]

**Key.** Radiation: \(p=\rho c^2/3\Rightarrow\rho-3p/c^2=0\), so \(R\) is *small* in a pure radiation fluid (only \(\Lambda\) and small matter leftovers). Matter: \(p=0\Rightarrow R=8\pi G\rho/c^2+4\Lambda\). Early *matter* and the brief windows around equality produce large \(R\). Early *radiation* produces large \(H\) and large \(\rho+3p\) (strong deceleration) with a comparatively suppressed \(R\).

Computed on the working background (integrals from \(a=10^{-14}\) to the named slice):

| Epoch | \(a\) | \(H/H_0\) | Hubble time \(1/H\) | \(R\,(\mathrm{m^{-2}})\) | \(R/R_0\) | \(\rho\,(\mathrm{kg\,m^{-3}})\) |
|---|---|---|---|---|---|---|
| Now | \(1\) | \(1\) | \(14.51\,\mathrm{Gyr}\) | \(9.2\times 10^{-52}\) | \(1\) | \(8.5\times 10^{-27}\) |
| \(a=0.5\) | \(0.5\) | — | — | — | — | — |
| Recombination | \(9.17\times 10^{-4}\) | \(2.3\times 10^{4}\) | \(6.3\times 10^5\,\mathrm{yr}\) | \(6.5\times 10^{-44}\) | \(7\times 10^{7}\) | \(4.6\times 10^{-18}\) |
| Equality | \(2.94\times 10^{-4}\) | \(1.6\times 10^{5}\) | \(9.3\times 10^4\,\mathrm{yr}\) | \(2.0\times 10^{-42}\) | \(2\times 10^{9}\) | \(2.1\times 10^{-16}\) |
| BBN (\(a\sim 10^{-9}\)) | \(10^{-9}\) | \(9.5\times 10^{15}\) | \(\sim 50\,\mathrm{s}\) | \(5.0\times 10^{-26}\) | \(5\times 10^{25}\) | \(7.7\times 10^{5}\) |
| QCD (\(a\sim 10^{-12}\)) | \(10^{-12}\) | \(9.5\times 10^{21}\) | \(\sim 50\,\mu\mathrm{s}\) | \(5.0\times 10^{-17}\) | \(5\times 10^{34}\) | \(7.7\times 10^{17}\) |

So: the *expansion rate* and the *background curvature* were enormous. That is real gravitation. It does **not** translate into “every clock ran slow relative to now,” because there is no external observer sitting outside the FLRW fluid with a reference Minkowski clock. The only global comparison is along one worldline from \(\mathcal{B}\) to here: that comparison *is* \(T_{\mathrm{BB}}\).

### How much proper time had elapsed by each epoch (BDC D2 vs D3)

| Epoch | \(t/t_0\) (D2) | \(\eta/\eta_0\) (D3) |
|---|---|---|
| BBN | \(\sim 6\times 10^{-17}\) | \(\sim 3\times 10^{-8}\) |
| Equality | \(3.7\times 10^{-6}\) | \(8.0\times 10^{-3}\) |
| Recombination | \(2.7\times 10^{-5}\) | \(2.0\times 10^{-2}\) |
| \(a=0.1\) | \(0.039\) | \(0.336\) |
| \(a=0.5\) | \(0.424\) | \(0.760\) |
| Now | \(1\) | \(1\) |

Almost all *proper* time (D2) is late. A much larger fraction of *conformal* time (D3) is early, because \(a\) is small and \(\mathrm{d}\eta=\mathrm{d}t/a\). Gravitation in the Friedmann sense is packed into the early sliver of D2 and the early chunk of D3. That is why BBN and recombination are gravitationally violent epochs that occupy almost none of a Hubble-flow clock’s life.

---

## 3. Spatial gravitational time dilation: early vs now

Rate offset versus the cosmic-mean slice:

\[
\frac{\mathrm{d}\tau}{\mathrm{d}t}=\sqrt{1+2\Psi}\approx 1+\Psi,\qquad
\frac{\Delta\tau}{\tau}\approx\Psi\sim\frac{\Phi_N}{c^2}.
\]

| Environment | \(\Phi/c^2\) | Clock vs cosmic mean |
|---|---|---|
| Primordial / CMB large-scale potential | \(\sim 10^{-5}\) | \(10\,\mu\mathrm{s}\) per second \(\times 10^{-3}\)? No: \(10^{-5}\) is \(10\,\mu\mathrm{s}\) per **second** would be \(10^{-5}\) s/s \(=10\,\mu\mathrm{s/s}\). Yes: \(10\,\mu\mathrm{s}\) of lag per second of cosmic time, *if* a clock sat in a \(\Phi=-10^{-5}\) well for that second. Over the age of the universe that would integrate to \(\sim 10^{-5}t_0\approx 4\times 10^5\,\mathrm{yr}\) — but primordial wells are *not* static deep holes a clock lives in; they are superhorizon ripples. |
| Galaxy cluster (\(\sigma_v\sim 1000\,\mathrm{km\,s^{-1}}\)) | \(\sim 1\times 10^{-5}\) | same order as primordial \(\Phi\), now *collapsed* |
| Milky Way disk (\(v\sim 220\,\mathrm{km\,s^{-1}}\)) | \(\sim 5\times 10^{-7}\) | \(0.5\,\mu\mathrm{s}\) per second |
| Sun, photosphere | \(-2.1\times 10^{-6}\) | \(2\,\mu\mathrm{s}\) per second |
| Earth surface | \(-7.0\times 10^{-10}\) | \(0.7\,\mathrm{ns}\) per second (GPS scale) |
| Neutron-star surface | \(\sim -0.17\) | clock rate \(\sim 0.83\) of cosmic mean |
| Black-hole horizon | \(\to-\infty\) in Schwarzschild lapse | clock freezes versus infinity |

**Early-universe wells.** Before collapse, \(\Phi\) is the almost scale-invariant primordial potential, rms a few \(\times 10^{-5}\). There are no neutron stars, no galaxies, no Earth. The *maximum* gravitational time-dilation contrast between two comoving clocks at recombination is the Sachs-Wolfe scale, \(\mathcal{O}(10^{-5})\). That *is* observed, as \(\delta T/T\) on large scales, which is the gravitational offset of last-scattering “clock events.”

**Late-universe wells.** Nonlinear collapse builds \(\Phi/c^2\) from \(10^{-5}\) up to \(10^{-4}\) (clusters), \(10^{-6}\) (galaxies), \(10^{-9}\) (planets), and \(\mathcal{O}(0.1)\) (compact objects). The *deepest* gravitational slowing of proper time that exists in this aeon is a late-time phenomenon.

So the comparison, stated bluntly:

- Early universe: background Ricci / \(H\) huge; spatial \(\Delta\tau/\tau\) tiny and linear.
- Current universe: background Ricci / \(H\) tiny; spatial \(\Delta\tau/\tau\) small for most baryons, order-unity only inside compact remnants.

A hydrogen atom at BBN and a hydrogen atom in intergalactic space today have gravitational-well corrections that differ by \(\lesssim 10^{-5}\). A hydrogen atom in the photosphere of a white dwarf today is the one that is actually running slow.

---

## 4. Photons are not clocks, and \(1/a\) is not well-dilation

A photon has \(\mathrm{d}\tau=0\). What it *does* carry is frequency. Two contributions get conflated in popular accounts.

**Background (expansion) redshift**

\[
\frac{\nu_{\mathrm{obs}}}{\nu_{\mathrm{emit}}}=\frac{a_{\mathrm{emit}}}{a_{\mathrm{obs}}}=\frac{1}{1+z}.
\]

This is the stretching of the conformal null geodesic. It is gravitational in the sense that \(a(t)\) is a solution of Einstein’s equation. It is *not* the \(\sqrt{1+2\Psi}\) factor.

**Perturbative gravitational redshift (Sachs-Wolfe + ISW)**

\[
\frac{\delta\nu}{\nu}\supset \Psi_{\mathrm{emit}}-\Psi_{\mathrm{obs}}+\int(\dot\Psi+\dot\Phi)\,\mathrm{d}\eta.
\]

**Key.** First two terms: clocks / potentials at emission and observation. Integral: time-varying potentials along the ray (ISW; late-time \(\Lambda\) or decaying potentials after equality).

CMB large-scale anisotropy \(\delta T/T\sim 10^{-5}\) *is* the early-universe gravitational effect on a standard-clock event (last scattering). It is a snapshot of Q2, not of Q1.

Tolman law for a photon gas, \(T\propto 1/a\), is the thermal version of the background redshift. Early “hot” is not “clocks in a deeper well.” It is a smaller scale factor on the same BDC worldline.

---

## 5. Special-relativistic companion: peculiar velocities

A clock moving at \(v_{\mathrm{pec}}\) versus Hubble flow has

\[
\mathrm{d}\tau=\frac{\mathrm{d}t}{\gamma_{\mathrm{pec}}}\sqrt{1+2\Psi}\;\approx\;\bigl(1+\Psi-\tfrac12 v_{\mathrm{pec}}^2/c^2\bigr)\mathrm{d}t.
\]

| Epoch | Typical peculiar / thermal speed | \(v^2/2c^2\) |
|---|---|---|
| Recombination, thermal baryon | \(\sim 5\,\mathrm{km\,s^{-1}}\)? actually \(v_{\mathrm{th}}\sim\sqrt{kT/m_p}\) at \(T\approx 0.3\,\mathrm{eV}\) is \(\sim 7\,\mathrm{km\,s^{-1}}\) | \(\sim 3\times 10^{-10}\) |
| Today, Milky Way in CMB frame | \(370\,\mathrm{km\,s^{-1}}\) (dipole) | \(\sim 8\times 10^{-7}\) |
| Today, cluster galaxy | \(\sim 10^3\,\mathrm{km\,s^{-1}}\) | \(\sim 6\times 10^{-6}\) |
| Relativistic electron at BBN | \(kT\sim 0.1\,\mathrm{MeV}\), \(e^-\) ultrarelativistic | order-unity for *electrons*, not for baryon clocks |

Baryonic clocks in the early universe are *colder kinematically* relative to \(c\) than galaxies are today. The SR correction to proper time of a proton clock is smaller at recombination than it is for a galaxy in a cluster now.

---

## 6. Weyl versus Ricci — the TSB / CCC cut

Penrose’s observation, used as-is:

- Early aeon interior: **Ricci-dominated**. Fluid density and pressure source \(R_{\mu\nu}\). Weyl \(C_{\alpha\beta\gamma\delta}\) is small (Weyl curvature hypothesis on \(\mathcal{B}\), and inflation / thermal smoothness after).
- Late aeon interior: **Weyl-dominated in bound objects**. Ricci of the mean fluid is tiny (\(R_0\sim 10^{-51}\,\mathrm{m^{-2}}\)). Tidal fields of galaxies, holes, and the Mirron-averaged deposits live in Weyl.

Gravitational time dilation of the Schwarzschild type is a *Weyl* (plus interior Ricci of the star) effect. That effect is therefore a late-universe effect.

Background expansion of proper time versus conformal time is a *Ricci / Friedmann* effect. That effect is an early-universe effect, and it is already built into \(t(a)\) and \(\eta(a)\).

TSB reading:

- Mirron bounce deposits path length into local Weyl \(\to\) emergent \(G\) of bound systems. Those deposits accumulate as structure forms. They are why D2 clocks in galaxies run slow versus the envelope BDC by \(\mathcal{O}(\Phi/c^2)\).
- The bang-to-now integral of Hubble-flow proper time is *not* a sum of those deposits. It is the envelope solution, Ricci-driven.
- Local PK tick \(\Delta t_\tau\) is unchanged as a geometric period of \(\Sigma_{\mathrm{M}}\). What changes is how many ticks fit in a given \(\mathrm{d}t\) once the clock sits in a late Weyl well: \(\mathrm{d}\tau<\mathrm{d}t\).

Do not say “the Mirron ran slower at BBN because gravity was stronger.” The engine period is local. The envelope expansion rate \(H\) was larger; that is a different sentence.

---

## 7. What a clock comparison would actually measure

Pick two Hubble-flow worldlines, start them on \(\mathcal{B}\), read them at a common BDC slice \(t=\mathrm{const}\).

- Ideal FLRW: both read \(t\). Difference \(=0\).
- Linear primordial \(\Phi\): difference \(\sim 10^{-5}t\) in synchronous time if one uses Newtonian-gauge \(t\) as the comparison coordinate; in the BDC (synchronous) stamp the difference is absorbed into the definition and reappears as a Sachs-Wolfe temperature when a photon is exchanged.
- After collapse: the clock that fell into a halo reads less proper time than the void clock by \(\int\Psi_{\mathrm{halo}}\,\mathrm{d}t\sim(\Phi/c^2)\times(\text{time since collapse})\). For a \(10^{-6}\) galactic well lived in for \(10\,\mathrm{Gyr}\), the missing proper time is \(\sim 3\times 10^3\,\mathrm{yr}\). Detectable in principle, irrelevant to BBN.

Pick one worldline and compare its proper-time *rate* at BBN versus now.

- Comoving baryon, no well: \(\mathrm{d}\tau/\mathrm{d}t=1\) at both epochs. The gravitational difference is not a rate; it is that \(\mathrm{d}t\) itself corresponds to a different \(\mathrm{d}a/a=H\mathrm{d}t\).
- Same baryon later sitting on Earth: extra \(-7\times 10^{-10}\) versus the cosmic mean, on top of solar and galactic wells.

---

## 8. Edge cases

| Case | Proper-time effect |
|---|---|
| On \(\mathcal{B}\) | No rest-mass frequency standard (CCC). \(\tau\) is not defined as a ticking clock. BDC is zero by fiat. |
| Planck / bounce layer | Ricci and (if the hard-wall picture is used) horizon-scale Weyl both huge. Classical \(\tau\) is an effective description only after the Mirron refresh writes a 4-metric. Not computed in this note. Standing bounce is *not* rewritten as a Kerr interior clock. |
| Radiation fluid | \(R\) suppressed relative to \(H^2\). Strong deceleration (\(\rho+3p>0\)) still crushes \(a(t)\). |
| Deep inside a late BH | Lapse versus infinity \(\to 0\). This is the largest gravitational proper-time effect in the present aeon, and it did not exist at BBN. |
| Void vs cluster “now” | \(\Delta\tau/\tau\sim 10^{-5}\). Cosmic chronometers (differential ages of galaxies) already work at that philosophy: they estimate \(\mathrm{d}t/\mathrm{d}z\), i.e. the background, not the well. |
| Domain stagger \(V_{\mathrm{orb}}\) | Changes domain proper-time *rates* versus the envelope. That is a Superblock effect, not an early-vs-late FLRW effect. Envelope BDC remains D2/D3. |

---

## 9. Implications for the BDC module

1. Quote early epochs in **D2 years** when talking about how long a baryon clock has ticked (\(t_{\mathrm{rec}}\approx 3.7\times 10^5\,\mathrm{yr}\)).
2. Quote them in **D3 Gly** when talking about how far gravity-plus-light could have run (\(\eta_{\mathrm{rec}}/\eta_0\approx 0.020\)).
3. File all \(\Psi\) wells under \(\tau_{\mathrm{obs}}-T_{\mathrm{BB}}\). Do not correct the BDC stamp itself by \(\Phi/c^2\) unless the manuscript is doing a relativistic number-count / clock-event paper.
4. The phrase “stronger gravity in the early universe” is allowed if and only if it means larger \(H\), larger \(\rho\), larger (matter-era) \(R\). It is not allowed as a synonym for deeper Schwarzschild wells.
5. Structure formation *increases* gravitational time-dilation contrast as the aeon ages. That is a Weyl-buildup prediction and a late-time prediction.

---

## 10. Session numerics (reproducible)

Working background: \(H_0=67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\), \(\Omega_m=0.315\), \(\Omega_\Lambda=0.685\), \(\Omega_r=9\times 10^{-5}\).

- \(t_0=4.352\times 10^{17}\,\mathrm{s}=13.79\,\mathrm{Gyr}\)
- \(\eta_0=1.456\times 10^{18}\,\mathrm{s}\equiv 46.14\,\mathrm{Gyr}\) of conformal time
- \(R_0=9.23\times 10^{-52}\,\mathrm{m^{-2}}\)
- \(R_{\mathrm{rec}}/R_0\approx 7\times 10^{7}\)
- \(H_{\mathrm{rec}}/H_0\approx 2.3\times 10^{4}\)
- Earth \(\Phi/c^2=-6.96\times 10^{-10}\)
- Solar photosphere \(\Phi/c^2=-2.12\times 10^{-6}\)
- Primordial / cluster-scale \(\Phi/c^2\sim 10^{-5}\)

Integrals are log-spaced trapezoid from \(a=10^{-14}\). BBN row is order-of-magnitude (\(a=10^{-9}\) is a proxy, not a nuclear-network time).

---

## 11. Decision line

> Background gravitation on proper time is already inside \(t(a)\) and \(\eta(a)\).  
> Spatial gravitational time dilation is a late, Weyl-built correction of size \(\Phi/c^2\), from \(10^{-5}\) (linear, both epochs) down to \(10^{-9}\) (planets) and up to \(\mathcal{O}(0.1)\) (compact objects, late only).  
> Early universe: huge Ricci / \(H\), tiny well contrast.  
> Current universe: tiny Ricci / \(H\), real wells.  
> BDC stamp stays D2/D3 of the envelope. Wells go in \(\tau_{\mathrm{obs}}-T_{\mathrm{BB}}\).

---

## 12. Query log

- Numerics: local Python, constants as in the variable key.
- Literature used as orientation, not as TSB authorities: Bonvin & Durrer / Challinor-style clock events and Sachs-Wolfe as cosmic-clock observables (review lineage of arXiv:1407.7979); Newtonian-gauge lapse \(\sqrt{1+2\Psi}\); Penrose Weyl/Ricci split already standing in the corpus.
- Related corpus files: BDC note of this date; UPS / \(t_G\) (2016-09-16); Mirron finite-\(c\) (2016-09-16); conformal hard wall as Kerr ring (candidate geometry only).

---

*End of session note — 2026-09-21 gravitation on proper time, early vs now.*
