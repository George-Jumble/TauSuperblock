# Session: Time as distance from the Big Bang — a universal privileged clock for any event

- **Session date:** 2026-09-21
- **Source prompt (verbatim):** “Let's measure time as a distance from the big bang as a universal privileged clock for any given event-”
- **Corpus status:** *Candidate module, live.* Compatible with the standing bounce (conformal aeon crossover + Mirron / Planck–Kerr dynamic refresh). Does **not** revive the rejected 2026-09-21 7 Mpc / seventh-phase aside line. Does **not** treat the Gatlin τ = 7 h⁻¹ Mpc compact S¹ layer as a live clock. Uses “Mirron,” never “soliton.”
- **Parent notes:** `2026-09-16_universal_point_of_simultaneity_review.md`, `2026-09-16_UPS_contraction_and_tG.md`, `2026-09-16_Mirron_nature_and_finite_c.md`, `2026-09-21_conformal_hard_wall_as_Kerr_ring_horizon.md`
- **This file:** `Personal Files/2026-09-21_bang_distance_privileged_clock.md`
- **Repo:** `George-Jumble/TauSuperblock` (branch `main`)
- **Drive folder:** Personal Files (`1Q8kRH_SrMUM-aBtyIIVq2nHgZWh9SJnk`)

---

## 0. What is being proposed

Assign to **every event** \(p\) in the present aeon a single scalar

\[
\ell_{\mathrm{BB}}(p)
\]

with the dimension of **length**, equal to a geometrically unique distance from the Big Bang 3-surface \(\mathcal{B}\) to \(p\). Convert to a time only when a local observer needs a ticking clock:

\[
T_{\mathrm{BB}}(p) \;=\; \frac{\ell_{\mathrm{BB}}(p)}{c}.
\]

That scalar is the **Bang Distance Clock** (BDC). It is privileged because \(\mathcal{B}\) is a distinguished surface (conformal compactification of the bang / previous-aeon \(\mathscr{I}\), Weyl curvature hypothesis), not because some observer declared a preferred Lorentz frame.

This is *not* a return to Newtonian absolute time. It is a **cosmological complete observable**: a relational label built from the geometry of one aeon.

---

## 1. Variable key

Every symbol used in this note.

| Symbol | Meaning |
|---|---|
| \(p\) | An arbitrary spacetime event in the present aeon |
| \(\mathcal{M}\) | 4-dimensional spacetime manifold of the present aeon |
| \(\mathcal{B}\) | Bang 3-surface: conformal compactification of the Big Bang; identified in CCC/TSB with previous-aeon future infinity \(\mathscr{I}^-\) after the crossover |
| \(\mathscr{I}^+\) | Future conformal infinity of the present aeon (spacelike if \(\Lambda>0\)) |
| \(g_{\mu\nu}\) | Physical 4-metric on \(\mathcal{M}\) |
| \(\tilde{g}_{\mu\nu}=\Omega^2 g_{\mu\nu}\) | Unphysical conformal metric that remains regular across \(\mathcal{B}\) |
| \(\Omega\) | Conformal factor; \(\Omega\to 0\) at \(\mathcal{B}\) and at \(\mathscr{I}^+\) in the CCC picture |
| \(a(t)\) | FLRW scale factor; \(a=0\) at the bang in the physical metric; \(a(t_0)=1\) today by convention |
| \(t\) | Cosmic proper time of the Hubble-flow congruence (comoving observers), \(t=0\) on \(\mathcal{B}\) |
| \(t_0\) | Present cosmic age. Planck 2018 working value used here: \(t_0 \approx 13.787\,\mathrm{Gyr}\) |
| \(\eta\) | Conformal time, \(\mathrm{d}\eta = \mathrm{d}t / a(t)\). Units of time, or of length/\(c\) |
| \(\eta_{\mathcal{B}}\) | Value of \(\eta\) on \(\mathcal{B}\). Set \(\eta_{\mathcal{B}}=0\) in this aeon |
| \(\chi\) | Comoving radial coordinate (dimensionless, or length if \(c=1,a_0=1\)) |
| \(c\) | Invariant speed of light in the Prime domain, \(c=2.99792458\times 10^8\,\mathrm{m\,s^{-1}}\) |
| \(H(t)=\dot{a}/a\) | Hubble parameter |
| \(H_0\) | Present Hubble parameter. Working value \(67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) |
| \(t_H=1/H_0\) | Hubble time \(\approx 14.51\,\mathrm{Gyr}\) at that \(H_0\) |
| \(d_{\mathrm{lt}}(p)=c\,t(p)\) | Light-travel (particle-age) distance of a comoving event |
| \(d_H(t)=a(t)\int_0^t c\,\mathrm{d}t'/a(t')\) | Particle-horizon proper distance at cosmic time \(t\) |
| \(\chi_H(\eta)=\eta-\eta_{\mathcal{B}}\) | Comoving particle horizon (= conformal time elapsed, \(c=1\)) |
| \(\gamma_p\) | Unique past-directed geodesic from \(\mathcal{B}\) to \(p\) that is orthogonal to \(\mathcal{B}\) |
| \(\ell_{\mathrm{BB}}(p)\) | Bang-distance of event \(p\): proper length of \(\gamma_p\) |
| \(\ell_{\mathrm{BB}}^{\mathrm{conf}}(p)\) | Conformal bang-distance: length of \(\gamma_p\) in \(\tilde{g}\) (equals \(c\eta(p)\) on FLRW) |
| \(T_{\mathrm{BB}}(p)=\ell_{\mathrm{BB}}(p)/c\) | Time read of the BDC |
| \(u^\mu\) | 4-velocity of the Hubble-flow (comoving) congruence, \(u_\mu \propto \nabla_\mu t\) |
| \(\tau_{\mathrm{obs}}\) | Proper time along an arbitrary observer worldline (generally \(\neq T_{\mathrm{BB}}\)) |
| \(z\) | Cosmological redshift, \(1+z=1/a_{\mathrm{emit}}\) |
| \(t_L(z)\) | Lookback time from here-and-now to redshift \(z\) |
| \(\Sigma_{\mathrm{M}}\) | Mirron 2-surface (Planck–Kerr topological mirror) |
| \(\Delta t_\tau\) | Tav / PK tick (local engine period; *not* the cosmic clock) |
| \(\chi_{\mathrm{M}}\) | Mirron presence parameter (\(1\) = engine on) |
| \(\mathrm{Sim}(p,q)\) | Simultaneity point of two events (UPS note, 2026-09-16) |
| \(\mathrm{UPS}_n\) | Universal point of simultaneity of one PK-clockwork tick \(n\) |
| \(t_G\) | Inter-domain gravity travel time; \(t_G=0\) on a UPS layer |
| \(C_{\alpha\beta\gamma\delta}\) | Weyl tensor. Standing hypothesis: \(C_{\alpha\beta\gamma\delta}\to 0\) on \(\mathcal{B}\) |
| \(\Lambda\) | Cosmological constant (positive \(\Rightarrow\) spacelike \(\mathscr{I}^+\)) |
| \(k\) | FLRW spatial curvature index \(\in\{-1,0,+1\}\) |
| \(\Omega_r,\Omega_m,\Omega_\Lambda\) | Present density parameters (radiation, matter, \(\Lambda\)) |
| \(E(a)=\sqrt{\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_k a^{-2}+\Omega_\Lambda}\) | Normalized Friedmann function |
| \(\Phi_8^P,\Phi_8^F\) | Absolute Past / Absolute Future nodes of the 8-phase engine (local, not cosmic) |
| \(N_{\mathrm{aeon}}\) | Aeon index. Present aeon \(N_{\mathrm{aeon}}=0\); previous \(=-1\) |
| \(\ell_{\mathrm{stack}}\) | Optional stacked clock that adds conformal lengths of completed previous aeons |

---

## 2. Why “time as a distance” is the natural move

In an FLRW line element

\[
\mathrm{d}s^2 = -c^2\mathrm{d}t^2 + a(t)^2\bigl(\mathrm{d}\chi^2 + f_k(\chi)^2\mathrm{d}\Omega_2^2\bigr)
\]

the substitution \(\mathrm{d}\eta=\mathrm{d}t/a(t)\) produces

\[
\mathrm{d}s^2 = a(\eta)^2\bigl(-c^2\mathrm{d}\eta^2 + \mathrm{d}\chi^2 + f_k(\chi)^2\mathrm{d}\Omega_2^2\bigr).
\]

**Key to this equation.**  
\(s\): proper interval. \(t\): cosmic time. \(a(t)\): scale factor. \(\eta\): conformal time. \(\chi\): comoving radial coordinate. \(f_k(\chi)=\sinh\chi,\;\chi,\;\sin\chi\) for \(k=-1,0,+1\). \(\mathrm{d}\Omega_2^2\): metric on the unit 2-sphere.

On the conformal metric the time coordinate and the radial coordinate have **identical units**. A photon with \(\mathrm{d}s=0\) obeys

\[
c\,\mathrm{d}\eta = \pm\mathrm{d}\chi.
\]

So “how long since the bang,” measured in conformal time, *is* “how far a photon could have run since the bang,” measured in comoving distance. That is the precise sense of the prompt.

Penrose’s CCC uses the same identity: after conformal rescaling, \(\mathcal{B}\) is a finite 3-surface and the “age” of an event is a finite conformal distance from that surface. TSB inherits that structure and adds the Mirron refresh that *generates* the physical metric as a time-average of bounce deposits.

Two clocks must not be confused:

| Clock | What it measures | Lives on |
|---|---|---|
| Local PK / Tav tick \(\Delta t_\tau\) | One Mirron Past⇄Future bounce | \(\Sigma_{\mathrm{M}}\) at a point |
| Bang Distance Clock \(\ell_{\mathrm{BB}}\) | Distance of an event from \(\mathcal{B}\) | The whole aeon |

The local tick is the *engine*. The BDC is the *odometer from the last crossover*.

---

## 3. Four candidate definitions (freeze one)

All four assign a number to every event. They agree on the Hubble-flow congruence and split for boosted / bound / horizon-crossing events.

### D1. Cosmic-time length (light-travel age)

\[
\ell_{\mathrm{BB}}^{(1)}(p) \;=\; c\, t(\pi_{\mathrm{flow}}(p))
\]

where \(\pi_{\mathrm{flow}}(p)\) is the unique event on the Hubble-flow worldline that lies on the same constant-\(t\) slice as \(p\).

- Today: \(\ell_{\mathrm{BB}}^{(1)}(\mathrm{here,now}) = c t_0 \approx 13.79\,\mathrm{Gly}\).
- Simple. Not a true geodesic distance from \(\mathcal{B}\) to a non-comoving event.
- Fails to be geometric at first order in peculiar velocity.

### D2. Orthogonal proper length (recommended physical clock)

Let \(\gamma_p:[0,1]\to\mathcal{M}\) be the unique past-directed geodesic with \(\gamma_p(0)\in\mathcal{B}\), \(\gamma_p(1)=p\), and \(\dot{\gamma}_p(0)\;\perp\;\mathcal{B}\).

\[
\ell_{\mathrm{BB}}^{(2)}(p)
\;=\;
\int_{\gamma_p}\sqrt{-g_{\mu\nu}\,\mathrm{d}x^\mu\mathrm{d}x^\nu}
\;=\;
\int_0^{t_\perp(p)} c\,\mathrm{d}\tau.
\]

**Key.** \(\tau\) is proper time along \(\gamma_p\). For a comoving event, \(\gamma_p\) *is* the Hubble-flow worldline and \(\ell_{\mathrm{BB}}^{(2)}=c t\). For a boosted event, \(t_\perp(p)\) is the cosmic time of the slice through \(p\), so D2 reduces to D1 on a hypersurface-orthogonal foliation. The geodesic language is what survives when the metric is only *approximately* FLRW.

### D3. Conformal bang-distance (recommended geometric / CCC clock)

\[
\ell_{\mathrm{BB}}^{(3)}(p)
\;=\;
c\int_{\gamma_p}\frac{\mathrm{d}t}{a(t)}
\;=\;
c\,\eta(p).
\]

On flat FLRW with \(a(t_0)=1\), this equals the **comoving particle horizon** at that event:

\[
\chi_H(p)=\eta(p)-\eta_{\mathcal{B}}.
\]

- Today: \(\ell_{\mathrm{BB}}^{(3)}(\mathrm{here,now})\approx 46.1\,\mathrm{Gly}\) (standard particle-horizon figure).
- Photons from \(\mathcal{B}\) to \(p\) travel exactly this comoving length.
- Regular across a conformal crossover: \(\eta\) stays finite when \(a\to 0\).
- This is the definition that treats time *as* a distance in the strictest sense.

### D4. Particle-horizon proper distance at the slice of \(p\)

\[
\ell_{\mathrm{BB}}^{(4)}(p)
\;=\;
a\bigl(t(p)\bigr)\cdot c\cdot\eta(p)
\;=\;
d_H\bigl(t(p)\bigr).
\]

- Today: \(\approx 46.1\,\mathrm{Gly}\) (same number as D3 because \(a_0=1\)).
- At recombination (\(z\approx 1090\), \(a\approx 1/1091\)): D3 is still tens of Gly comoving; D4 is a few hundred thousand light-years proper.
- D4 is what an observer *on that slice* would call “the radius of the observable universe *then*.”
- D3 is what a conformal diagram calls “how far from the bang.”

### Freeze for the corpus

| Role | Definition |
|---|---|
| Geometric / CCC / manuscript diagrams | **D3** \(\ell_{\mathrm{BB}}^{\mathrm{conf}}(p)=c\eta(p)\) |
| Physical age read by a Hubble-flow clock | **D2** \(\ell_{\mathrm{BB}}(p)=c\,t_\perp(p)\) |
| Do not mix | D1 is D2 on FLRW; D4 is D3 rescaled by \(a\) |

Working pair: quote **D2 in years**, quote **D3 in Gly**, and always name which one.

---

## 4. Privileged clock for *any* event

### 4.1 Existence and uniqueness (FLRW and mild perturbations)

Assume:

1. \(\mathcal{B}\) is a spacelike 3-surface (true for a radiation-era bang and for CCC with \(\Lambda>0\) on the previous \(\mathscr{I}\)).
2. The congruence of geodesics orthogonal to \(\mathcal{B}\) is irrotational and fills a neighborhood of \(\mathcal{B}\) (standard Gauss lemma / normal exponential map).
3. That congruence remains a global foliation up to the event \(p\) (true in FLRW; true in TSB at linear order if the Mirron-averaged metric stays close to FLRW).

Then every event \(p\) not on a caustic of the congruence has a unique \(\gamma_p\), hence a unique \(\ell_{\mathrm{BB}}(p)\).

This is the cosmological analogue of GPS time: the bang surface plays the role of the satellite constellation’s common epoch.

### 4.2 Events that are *not* on the Hubble flow

A detector in a galaxy, a muon in CMS, a photon at last scattering, a clock in a gravitational well:

- The BDC value is the label of the **slice** through that event, not the detector’s proper time.
- Proper time \(\tau_{\mathrm{obs}}\) along the detector worldline and \(T_{\mathrm{BB}}\) differ by special-relativistic and gravitational time dilation plus the integral of peculiar velocity.
- The twin-paradox content is kept: two worldlines that meet at \(p\) have different \(\tau_{\mathrm{obs}}\) and the *same* \(\ell_{\mathrm{BB}}(p)\). That is the point of a privileged clock.

Rovelli’s remark (two galaxies colliding with different elapsed proper times from the bang) is correct for **proper time**. It is not an objection to D2/D3: both galaxies, at the collision event \(p\), receive the *same* bang-distance. Their onboard clocks disagree with each other and with the BDC; the BDC does not care.

### 4.3 UPS compatibility (2026-09-16)

The UPS construction says: every pair of 4D events has a simultaneity point; those points tournament-collapse to one UPS per PK tick; inter-domain leaks ride the layer at \(t_G=0\).

BDC and UPS are different layers of the same clock tower:

- **BDC** labels *which cosmic slice* an event sits on. Coarse, aeon-scale.
- **UPS / PK tick** labels *which refresh* inside that slice. Fine, Mirron-scale.
- A BDC slice is a set of events with equal \(\ell_{\mathrm{BB}}\). The UPS of that slice is the simultaneity contraction of those events on the 5D envelope, with \(t_G=0\) for cross-domain gravity on that layer.

Do not identify \(\ell_{\mathrm{BB}}/c\) with \(\Delta t_\tau\). One is the odometer from \(\mathcal{B}\); the other is the engine period.

### 4.4 Multi-domain Superblock

Six co-located 3+1 domains share an internal supersphere. Causal separation is domain-wise; gravitational coupling is conformal / time-averaged.

Rule for this module:

- \(\mathcal{B}\) is a single conformal 3-surface of the *envelope*, not six separate bangs.
- Each domain event \(p_i\) still has its own 4D geodesic \(\gamma_{p_i}\) in its domain metric.
- The privileged label is the **envelope conformal time** \(\eta_{\mathrm{env}}(p)\), i.e. D3 pulled back from the conformal metric that is common after averaging.
- Domain-staggered \(V_{\mathrm{orb}}\) changes proper-time rates, not the envelope label.

This is how a CMS muon event and a SPARC galaxy event can share a clock without sharing a Lorentz frame.

---

## 5. Explicit FLRW formulae

Flat \(\Lambda\)CDM, \(a(t_0)=1\), \(c\) restored.

Hubble function:

\[
H(a)=H_0 E(a),\qquad
E(a)=\sqrt{\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda}.
\]

**Key.** \(H_0\): present Hubble parameter. \(\Omega_r,\Omega_m,\Omega_\Lambda\): present density parameters. Radiation may be dropped after \(z\ll 300\).

Cosmic time from the bang to scale factor \(a\):

\[
t(a)=\frac{1}{H_0}\int_0^a \frac{\mathrm{d}a'}{a' E(a')}.
\]

Conformal time from the bang to scale factor \(a\):

\[
\eta(a)=\frac{1}{H_0}\int_0^a \frac{\mathrm{d}a'}{a'^2 E(a')}.
\]

Bang-distance clocks at that slice:

\[
\begin{aligned}
\ell_{\mathrm{BB}}^{(2)}(a) &= c\, t(a),\\
\ell_{\mathrm{BB}}^{(3)}(a) &= c\, \eta(a),\\
\ell_{\mathrm{BB}}^{(4)}(a) &= a\cdot c\cdot \eta(a).
\end{aligned}
\]

Lookback time from today to redshift \(z\) (this is *not* the BDC; it is an observer-centered derived quantity):

\[
t_L(z)=t_0-t\bigl(1/(1+z)\bigr).
\]

An event “at redshift \(z\) on our past light cone” has

\[
\ell_{\mathrm{BB}}^{(2)}=c\bigl(t_0-t_L(z)\bigr)=c\, t(z),
\]

which depends only on the slice, not on the fact that *we* see it.

### Working numbers (Planck-like, sufficient for the module)

| Epoch | \(z\) | \(a\) | D2 \(=c t\) | D3 \(=c\eta\) | D4 \(=a\,c\eta\) |
|---|---|---|---|---|---|
| Bang surface \(\mathcal{B}\) | \(\infty\) | \(0\) | \(0\) | \(0\) (conformal) | \(0\) |
| BBN (order of) | \(\sim 10^9\) | \(\sim 10^{-9}\) | \(\sim 3\,\mathrm{l-min}\) | large comoving | small proper |
| Recombination | \(1090\) | \(9.2\times 10^{-4}\) | \(\sim 380{,}000\,\mathrm{ly}\) | \(\sim 42\,\mathrm{Gly}\) | \(\sim 0.04\,\mathrm{Gly}\) |
| Here and now | \(0\) | \(1\) | \(13.79\,\mathrm{Gly}\) | \(\sim 46.1\,\mathrm{Gly}\) | \(\sim 46.1\,\mathrm{Gly}\) |
| Far future (\(\Lambda\)-dom.) | \(-1\) | \(\to\infty\) | \(\to\infty\) | \(\to\eta_\infty<\infty\) | \(\to\infty\) |

The last row is the CCC fact: conformal time to \(\mathscr{I}^+\) is finite, which is why a future aeon can be glued on. D3 stays the right clock through a crossover; D2 diverges and is the wrong glue variable.

---

## 6. TSB / CCC specific content

### 6.1 What “the Big Bang” is in this corpus

Not a curvature singularity that ends the geometry. In the standing bounce:

- Physical metric \(g_{\mu\nu}\) has \(a\to 0\).
- Conformal metric \(\tilde{g}_{\mu\nu}\) is regular.
- \(\mathcal{B}\) is the crossover 3-surface, previous-aeon \(\mathscr{I}\) identified with this-aeon bang.
- Mirron / Planck–Kerr dynamic refresh writes the new physical metric on the far side.
- Weyl curvature is reset (Weyl hypothesis), so \(\mathcal{B}\) is as close to a “universal epoch zero” as the theory allows.

The 2026-09-21 conformal-hard-wall = Kerr-ring identification remains a *candidate geometric picture of the wall*, not a replacement of this bounce, and not a new clock.

### 6.2 Why the BDC is privileged *inside TSB*

1. \(\mathcal{B}\) is selected by geometry (vanishing Weyl, conformal regularity), not by a coordinate choice.
2. The orthogonal congruence is the Hubble flow after Mirron averaging.
3. Local PK ticks generate \(c\) and the light cones (Mirron-impedance theorem, 2026-09-16) but do not choose a zero of time. \(\mathcal{B}\) does.
4. Envelope conformal time is common to the six domains after averaging, so one number labels events in every domain.

### 6.3 Stacked aeon clock (optional, off by default)

If a manuscript needs a clock that does not reset at crossover:

\[
\ell_{\mathrm{stack}}(p)
\;=\;
c\eta_{\mathrm{this}}(p)
\;+\;
\sum_{N<0} c\,\eta_\infty^{(N)}.
\]

**Key.** \(\eta_{\mathrm{this}}(p)\): conformal time of \(p\) since this \(\mathcal{B}\). \(\eta_\infty^{(N)}\): total conformal lifetime of completed aeon \(N\).

Default for the corpus: **do not stack**. Each aeon has its own BDC zero on its own \(\mathcal{B}\). Stacking is a bookkeeping device, not a physical extra dimension of time.

### 6.4 What this module does *not* do

- Does not set the cosmic clock equal to \(\Delta t_\tau\) or to \(t_P\).
- Does not import \(\tau=7\,h^{-1}\,\mathrm{Mpc}\) as a time unit (Gatlin layer falsified for live analyses).
- Does not use the rejected 7 Mpc / seventh-phase aside as a clock slot.
- Does not rewrite the bounce as a \(\Phi_7\) pin-drop or Coleman instanton.
- Does not claim that BDC removes the problem of time in canonical quantum gravity. It is a classical complete observable of one aeon.

---

## 7. Operational recipe — how to stamp an event

Given any event \(p\) specified by data a survey or a detector actually has:

1. **On our past light cone** (galaxy, SN, CMB last-scattering, BAO shell): measure \(z\). Compute \(a=1/(1+z)\). Integrate \(t(a)\) and \(\eta(a)\). Stamp
   - physical age \(T_{\mathrm{BB}}=t(a)\),
   - conformal distance \(\ell_{\mathrm{BB}}^{\mathrm{conf}}=c\eta(a)\).
2. **Local laboratory event** (CMS muon, clock comparison): take the cosmological time of *this* slice of Earth. At the precision of any collider timestamp that is just \(t_0\). Report residuals (gravitational redshift, special-relativistic \(\gamma\)) separately; they are not BDC corrections, they are \(\tau_{\mathrm{obs}}-T_{\mathrm{BB}}\).
3. **Event off our light cone** (a spacelike-separated galaxy “now”): use the same slice \(t=t_0\) (or the same \(\eta=\eta_0\)). That is the privileged “now” of the BDC. There is no other.
4. **Event in another domain:** use envelope \(\eta_{\mathrm{env}}\), not the domain’s raw proper time.
5. **Event in another aeon:** either refuse the stamp (default) or use \(\ell_{\mathrm{stack}}\) and declare it.

---

## 8. Edge cases

| Case | What the BDC does |
|---|---|
| Event on \(\mathcal{B}\) | \(\ell_{\mathrm{BB}}=0\) by definition. Local clocks do not exist there (Penrose: rest-mass suppressed, no frequency standard). |
| Event at \(\mathscr{I}^+\) | D3 finite, D2 infinite. Glue variable is D3. |
| Inside a black hole horizon | The cosmological foliation still labels the *exterior* slice from which the collapse started. Interior \(t_{\mathrm{Schwarz}}\) is a different coordinate. Stamp the exterior BDC of the collapse event; do not force \(\ell_{\mathrm{BB}}\) along the interior worldline past the horizon without a separate extension rule. |
| Caustic / shell-crossing | Uniqueness of \(\gamma_p\) fails. Use the earliest regular slice that still contains a unique normal geodesic, or switch to D3 computed from the conformal metric (usually better behaved). |
| Strong backreaction / void | Linear Hubble flow is approximate. BDC becomes a *best-fit* orthogonal time function. That is already how cosmic time is used in real catalogues. |
| Two colliding galaxies (Rovelli) | Same \(\ell_{\mathrm{BB}}\) at the meeting event; different onboard \(\tau_{\mathrm{obs}}\). |
| Photon | \(\mathrm{d}\tau=0\) along its worldline. BDC of the *emission event* and BDC of the *absorption event* differ by \(c\Delta\eta=\Delta\chi\). The photon does not carry a ticking BDC; the events on its path do. |
| Superluminal-looking coordinate charts | Irrelevant. BDC is built from geodesics / conformal time, not from an arbitrary \(t\)-coordinate. |

---

## 9. Implications

### 9.1 For the manuscript

A single sentence that can be dropped into a Superblock Universe chapter:

> Every event \(p\) of the present aeon carries a privileged scalar \(\ell_{\mathrm{BB}}(p)=c\eta(p)\), the conformal distance from the bang 3-surface \(\mathcal{B}\). Local proper time is the reading of a Mirron engine along a worldline; \(\ell_{\mathrm{BB}}\) is the reading of the aeon itself.

### 9.2 For observations

- CMB last scattering is one BDC slice, \(\ell_{\mathrm{BB}}^{(2)}\approx 380{,}000\,\mathrm{ly}\), \(\ell_{\mathrm{BB}}^{(3)}\approx 42\,\mathrm{Gly}\).
- DESI BAO shells are BDC slices labelled by \(z\), hence by \(\eta(z)\).
- A “cosmic dipole of clocks” would be a dipole in \(\tau_{\mathrm{obs}}-T_{\mathrm{BB}}\), not in \(T_{\mathrm{BB}}\) itself. \(T_{\mathrm{BB}}\) has no dipole by construction.
- Hubble tension is a tension in \(H(a)\), which *defines* how fast \(\ell_{\mathrm{BB}}\) grows with \(a\). The BDC does not resolve the tension; it is the language in which the tension is stated.

### 9.3 For the problem of time

Bamonti & Thébault (arXiv:2411.00541) treat cosmic time as a relational reference frame compatible with the clock hypothesis. D2 is exactly that frame. D3 is the same frame written in the units that CCC and TSB actually glue across aeons. Neither modifies the Friedmann equation.

### 9.4 For inter-domain leaks

A leak at \(t_G=0\) is a leak *on a BDC slice*. The slice supplies the “when”; the UPS construction supplies the “which tick of the engine on that when.”

---

## 10. Falsifiers / discipline

The module is wrong, or must be restricted, if any of the following holds:

1. No spacelike \(\mathcal{B}\) exists (e.g. a chaotic Mixmaster bang with no conformal regularization). Then uniqueness of \(\gamma_p\) dies.
2. The orthogonal congruence develops caustics before the events we care about, and the conformal metric cannot repair them.
3. Domain metrics after Mirron averaging do *not* share a common conformal time. Then “universal” fails and we only have six domain clocks.
4. Someone uses \(\ell_{\mathrm{BB}}/c\) as if it were \(\Delta t_\tau\). That is a category error, not a prediction.

---

## 11. Recommended next computations (not done this session)

1. Numerical table of D2, D3, D4 against a Planck 2018 / DESI DR2 background from \(a=10^{-12}\) to \(a=10\).
2. First-order correction \(\delta\ell_{\mathrm{BB}}\) in Newtonian gauge for a potential \(\Phi\), to see how a void shifts the stamp.
3. Explicit map \(\mathrm{UPS}_n \leftrightarrow \ell_{\mathrm{BB}}\) for one slice: how many PK ticks sit on the here-and-now slice.
4. Decide whether manuscript figures use D3 exclusively (cleaner conformal diagrams) or dual-label D2+D3.

---

## 12. Session query log (results)

Tools and lookups used to build this note:

- Workspace listing: `/home/workdir/artifacts` empty at start except this session’s writes.
- GitHub authenticated user: `George-Jumble` (william brown). Repos: `research-tool`, `TauSuperblock`, `tav-resonace-research-tool`.
- `TauSuperblock` tree confirms `Personal Files/` is the project folder for session notes. Live related files: UPS review, UPS contraction / \(t_G\), Mirron and finite \(c\), conformal hard wall as Kerr-ring horizon.
- Google Drive folder `Personal Files` id `1Q8kRH_SrMUM-aBtyIIVq2nHgZWh9SJnk` exists and already holds the 2026-09-15 through 2026-09-21 session notes.
- Literature touched: Bamonti & Thébault, arXiv:2411.00541 (cosmic time as reference frame); Rugh & Zinkernagel, arXiv:0805.1947 (physical basis of cosmic time); Penrose / Tod CCC conformal time; standard FLRW distance ladder (particle horizon \(\approx 46.1\,\mathrm{Gly}\), \(c t_0\approx 13.79\,\mathrm{Gly}\)).
- Numerical scratch:
  - \(1\,\mathrm{Gyr}=3.15576\times 10^{16}\,\mathrm{s}\)
  - \(1\,\mathrm{Gly}=9.46073\times 10^{24}\,\mathrm{m}=306.60\,\mathrm{Mpc}\)
  - \(t_H(H_0=67.4)=14.51\,\mathrm{Gyr}\), \(t_0/t_H\approx 0.950\)
  - \(d_H/(c t_0)\approx 3.34\)

---

## 13. Decision line (for the corpus ledger)

> Adopt the Bang Distance Clock as a live TSB module.  
> Geometric stamp of an event: \(\ell_{\mathrm{BB}}^{\mathrm{conf}}(p)=c\eta(p)\) (D3).  
> Physical age stamp: \(T_{\mathrm{BB}}(p)=t_\perp(p)\) (D2).  
> Zero of both is the present-aeon bang 3-surface \(\mathcal{B}\).  
> Local Mirron ticks remain a different object.  
> Default: no stacked multi-aeon odometer.

---

*End of session note — 2026-09-21 bang-distance privileged clock.*
