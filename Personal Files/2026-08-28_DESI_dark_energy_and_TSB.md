# DESI, Dark Energy, and Tau-Superblock (TSB) Theory

**Session date:** Friday, 28 August 2026  
**Author of session note:** Grok 4.6 (working session with William Brown / William Wylde)  
**Scope:** How DESI observables connect to the TSB account of dark energy, and a re-examination of how the framework posits dark energy to work.  
**Status of this note:** Working synthesis, not a new derivation. Claims of the theory are those already stated in the June 2026 TSB corpus; observational numbers are from DESI DR2 and subsequent 2025–2026 combinations.

---

## 1. What DESI actually measures

DESI does not measure “dark energy” directly. It measures the baryon acoustic oscillation (BAO) ruler in several tracer samples across \(0 \lesssim z \lesssim 2.5\), plus a Lyman-\(\alpha\) forest anchor near \(z_{\mathrm{eff}} = 2.33\).

The two geometric BAO distances are:

\[
D_H(z) = \frac{c}{H(z)}, \qquad D_M(z) = c \int_0^z \frac{dz'}{H(z')}.
\]

DESI reports them in units of the sound-horizon scale \(r_d\):

\[
\frac{D_H(z)}{r_d}, \qquad \frac{D_M(z)}{r_d}, \qquad F_{\mathrm{AP}}(z) \equiv \frac{D_M(z)}{D_H(z)}.
\]

### Variable key (BAO geometry)

| Symbol | Meaning |
|---|---|
| \(z\) | Redshift of the tracer sample |
| \(H(z)\) | Hubble expansion rate at redshift \(z\) |
| \(c\) | Speed of light |
| \(D_H(z)\) | Hubble distance (line-of-sight BAO) |
| \(D_M(z)\) | Comoving angular-diameter distance (transverse BAO) |
| \(r_d\) | Comoving sound horizon at the drag epoch (early-universe standard ruler) |
| \(F_{\mathrm{AP}}(z)\) | Alcock–Paczyński ratio; independent of \(r_d\) |

To turn those distances into a statement about dark energy one must assume a background Friedmann equation and an equation-of-state parametrization. The industry standard is Chevallier–Polarski–Linder (CPL):

\[
w(a) = w_0 + w_a(1-a), \qquad a = \frac{1}{1+z}.
\]

The dark-energy density then evolves as

\[
\frac{\rho_{\mathrm{DE}}(a)}{\rho_{\mathrm{DE},0}} = a^{-3(1+w_0+w_a)}\, e^{-3 w_a(1-a)}.
\]

### Variable key (CPL)

| Symbol | Meaning |
|---|---|
| \(a\) | Scale factor (\(a=1\) today) |
| \(w(a)\) | Dark-energy equation of state \(P_{\mathrm{DE}}/\rho_{\mathrm{DE}}\) |
| \(w_0\) | Present-day value, \(w(a=1)\) |
| \(w_a\) | Slope of \(w\) with scale factor |
| \(\rho_{\mathrm{DE}}(a)\) | Dark-energy energy density |
| \(\rho_{\mathrm{DE},0}\) | Present-day dark-energy density |
| \(\Lambda\mathrm{CDM}\) | The special case \(w_0 = -1\), \(w_a = 0\) |

DESI’s scientific claim is therefore not “we detected a new field.” It is: *when the BAO distance ladder is combined with CMB and/or supernovae, the preferred \((w_0, w_a)\) point sits off \((-1, 0)\) in a specific quadrant.*

---

## 2. Observational status as of late August 2026

The numbers below are the public combination results, not TSB fits.

### 2.1 DESI DR2 official cosmology paper (March 2025; PRD Oct 2025)

- Flat \(\Lambda\mathrm{CDM}\) still fits DESI BAO *by itself*.
- DESI BAO vs CMB-preferred \(\Lambda\mathrm{CDM}\) parameters: mild \(\simeq 2.3\sigma\) mismatch.
- DESI BAO + CMB in \(w_0 w_a\mathrm{CDM}\): preference for dynamical DE at **\(3.1\sigma\)**, in the quadrant

\[
w_0 > -1, \qquad w_a < 0.
\]

- DESI + CMB + SNe: preference ranges **\(2.8\sigma\)–\(4.2\sigma\)** depending on the supernova compilation (Pantheon+, Union3, DES-Y5). DES-Y5 gives the strongest pull.

### 2.2 Low-redshift-only combinations (DES Y6 + DESI DR2, Aug 2026)

All DES probes (SN + BAO + \(3\times 2\mathrm{pt}\)) + DESI DR2 BAO, *no CMB*:

\[
w_0 = -0.84^{+0.06}_{-0.07}, \qquad w_a = -0.53^{+0.33}_{-0.28}
\]

(\(2.3\sigma\) from \(\Lambda\mathrm{CDM}\)).

Adding primary CMB (Planck + ACT + SPT):

\[
w_0 = -0.82 \pm 0.05, \qquad w_a = -0.63^{+0.21}_{-0.18}
\]

(\(\simeq 3.0\sigma\) from \(\Lambda\mathrm{CDM}\)).

The preferred region is *always* \(w_0 > -1\), \(w_a < 0\). That is a **weakening** effective dark energy: more negative \(w\) in the past, less negative today.

### 2.3 The July 2026 Lyman-\(\alpha\) full-shape wrinkle

A later DESI DR2 Ly\(\alpha\) *full-shape* (not BAO-peak-only) analysis tightened the high-\(z\) Alcock–Paczyński measurement and moved the central value **toward** Planck \(\Lambda\mathrm{CDM}\). The BAO-only Ly\(\alpha\) point had sat between \(\Lambda\mathrm{CDM}\) and the \(w_0 w_a\) best fit; the full-shape point is closer to \(\Lambda\mathrm{CDM}\).

This does not erase the galaxy-BAO + SN pull at \(z \lesssim 1\), but it is an important internal DESI nuance: the *highest-redshift* DESI probe is no longer helping the dynamical-DE story as much as the March 2025 BAO-only papers suggested.

### 2.4 What the data pattern actually is

A fair one-sentence summary:

> Low- and intermediate-redshift distances prefer a slightly larger late-time expansion (or slightly lower \(\Omega_m\)) than Planck \(\Lambda\mathrm{CDM}\); allowing \(w(z)\) to become less negative toward \(z=0\) absorbs that mismatch. The significance is real but still compilation-dependent, and high-\(z\) Ly\(\alpha\) full-shape has since drifted back toward \(\Lambda\mathrm{CDM}\).

That is the observational target TSB has to hit — not a confirmed detection of a new substance.

---

## 3. How TSB posits dark energy to work

The TSB corpus (May–June 2026) does **not** treat dark energy as a single cosmological-constant term. It splits the late-time acceleration into two geometrically distinct pieces.

### 3.1 Layer A — static Tav Casimir baseline (\(w \equiv -1\))

Gatlin’s May 2026 unification paper and Brown’s 17 June 2026 DESI note both state that a macroscopic compact fifth dimension

\[
\tau = 7\, h^{-1}\,\mathrm{Mpc}
\]

on the manifold \(\mathbb{R}^3 \times S^1\) generates a topological Casimir / vacuum pressure. Because the \(S^1\) radius is a rigid geometric feature, that pressure is locked at

\[
P_{\mathrm{Tav}} = w_{\mathrm{Tav}}\, \rho_{\mathrm{Tav}}, \qquad w_{\mathrm{Tav}} \equiv -1.
\]

This is the TSB replacement for a fine-tuned \(\Lambda\). It is *not* a fitted vacuum energy; it is supposed to be fixed by the Tav conformal scale (the same \(7\,h^{-1}\,\mathrm{Mpc}\) cylinder that also sets the 1/7 harmonic and the \(m_0 \approx 313.1\,\mathrm{MeV}\) IR mass-gap anchor).

### Variable key (Layer A)

| Symbol | Meaning |
|---|---|
| \(\tau\) | Radius of the compact fifth dimension; Tav conformal scale |
| \(h\) | Reduced Hubble parameter, \(h = H_0 / (100\,\mathrm{km\,s^{-1}\,Mpc^{-1}})\) |
| \(S^1\) | Compact circle in the 5D Einstein–Kaluza–Klein substrate |
| \(P_{\mathrm{Tav}}\) | Casimir / vacuum pressure generated by the rigid \(\tau\)-circle |
| \(\rho_{\mathrm{Tav}}\) | Associated vacuum energy density |
| \(w_{\mathrm{Tav}}\) | Equation of state of the Tav vacuum; identically \(-1\) |
| \(\Lambda_{\mathrm{Tav}}\) | Effective cosmological term sourced by that vacuum |

**Physical content.** A Casimir pressure on a circle of radius \(\tau\) scales as \(\sim \hbar c / \tau^4\) (or a 5D-reduction variant). TSB’s claim is that the *macroscopic* choice \(\tau \sim 7\,h^{-1}\,\mathrm{Mpc}\) produces an IR vacuum of the observed cosmic density rather than the usual Planck-scale disaster. That is the proposed solution of the cosmological-constant problem inside the framework: vacuum energy is set by the Tav scale, not by the UV cutoff.

### 3.2 Layer B — rotational / centrifugal term (the evolving piece)

A static \(w = -1\) term cannot produce DESI’s \(w_a < 0\). The 17 June 2026 note therefore adds a second, time-dependent contribution from the rotation of the six-domain supersphere.

The modified Friedmann equation as written in that note is

\[
H^2 = \frac{8\pi G}{3}\,\rho_{\mathrm{matter}} + \frac{\Lambda_{\mathrm{Tav}}}{3} + \Omega_{\mathrm{rot}}(t).
\]

*(Dimensional remark: as printed, \(\Omega_{\mathrm{rot}}\) must carry units of \(H^2\). A cleaner writing is \(\Omega_{\mathrm{rot}}(t)\, H_0^2\), or equivalently an extra effective density \(\rho_{\mathrm{rot}}(t) = 3\Omega_{\mathrm{rot}}(t)/(8\pi G)\). The physics intended is an additive centrifugal source.)*

The rotational source is summed over the six co-located \(3+1\)D domains:

\[
\Omega_{\mathrm{rot}}(t) = \frac{1}{2} \sum_{i=1}^{6} \gamma_i \, \omega^2(t)\, R_{\mathrm{SB}}^2,
\qquad
\gamma_i = \frac{1}{\sqrt{1-\beta_i^2}}.
\]

### Variable key (Layer B)

| Symbol | Meaning |
|---|---|
| \(H(t)\) | Hubble parameter |
| \(G\) | Newton’s constant |
| \(\rho_{\mathrm{matter}}\) | Ordinary + (phase-hidden) matter density in the visible domain |
| \(\Lambda_{\mathrm{Tav}}\) | Static Casimir term from Layer A |
| \(\Omega_{\mathrm{rot}}(t)\) | Dimensionless-or-\(H^2\) centrifugal contribution |
| \(i = 1\ldots 6\) | Index of the six co-located spacetime domains |
| \(\beta_i = v_{\mathrm{orb},i}/c\) | Dimensionless orbital speed of domain \(i\) on the supersphere |
| \(\gamma_i\) | Lorentz factor of domain \(i\) |
| \(\omega(t)\) | Angular velocity of the 5D superblock |
| \(R_{\mathrm{SB}}\) | Effective supersphere / superblock radius |
| \(V_{\mathrm{orb},i}\) | E\(_8\)-projected staggered orbital velocity of domain \(i\) |

**Physical content.** The six domains are causally separated on an internal supersphere, with staggered speeds inherited from an E\(_8\) projection. Their orbital motion produces an outward centrifugal stress. In the visible domain that stress is seen as an extra accelerating term — “dark energy” that is actually kinematics of the multi-domain geometry, not a new 4D field.

### 3.3 Why DESI should see *weakening*

The 17 June note models the rotational piece over a conformal-cyclic lifetime \(T_{\mathrm{cycle}}\):

\[
\Omega_{\mathrm{rot}}(t) = \Omega_{\max}\, \sin\left(\frac{\pi t}{T_{\mathrm{cycle}}}\right).
\]

Then

\[
\frac{d\Lambda_{\mathrm{eff}}}{dt} = \frac{d\Omega_{\mathrm{rot}}}{dt} = \Omega_{\max}\, \frac{\pi}{T_{\mathrm{cycle}}}\, \cos\left(\frac{\pi t}{T_{\mathrm{cycle}}}\right).
\]

### Variable key (cyclic decay)

| Symbol | Meaning |
|---|---|
| \(T_{\mathrm{cycle}}\) | Duration of one Superblock / CCC-style aeon |
| \(t\) | Cosmic time since the beginning of the present aeon |
| \(\Omega_{\max}\) | Peak rotational contribution, at mid-cycle |
| \(\Lambda_{\mathrm{eff}}\) | Effective dark-energy term seen by a 4D observer (\(\Lambda_{\mathrm{Tav}} + 3\Omega_{\mathrm{rot}}\), up to units) |

Interpretation inside the framework:

- For \(t < T_{\mathrm{cycle}}/2\), the cosine is positive: rotational DE is still *strengthening*. That is the era of “classic” accelerating expansion.
- Near \(t = T_{\mathrm{cycle}}/2\), \(d\Lambda_{\mathrm{eff}}/dt \to 0\): inflection, maximum domain separation on the supersphere.
- For \(t > T_{\mathrm{cycle}}/2\), the cosine is negative: rotational DE *decays*. Domains begin geometric re-convergence toward the next conformal refresh.

The June 17 claim is that DESI’s \(w_0 > -1\), \(w_a < 0\) quadrant is the 4D shadow of that mid-to-late-cycle decay: we are no longer on the rising half of the sine, we are on or past the crest.

### 3.4 Layer C — the late-time “BOOM!” (v2.0, 25 June 2026)

The 12-page v2.0 update does not replace Layers A–B. It adds a possible *threshold* event when Tav harmonics accumulate and domain phases realign:

- a sudden shift in effective gravitational coupling or \(H(z)\),
- a burst of gravitational waves / extra relativistic species,
- or a CCC-style conformal boundary (“aeon crossover”) modulated by the 1/7 and 142857 algebraic structure.

This is the framework’s internal climax, not a fit parameter. It is the piece that is *most* falsifiable with Euclid, Rubin, LISA, and a completed DESI sample — and also the piece that is still the most schematic.

### 3.5 How the three layers sit together

```
5D Einstein–KK substrate   R³ × S¹,  τ = 7 h⁻¹ Mpc
        │
        ├── Layer A: rigid Casimir pressure     w_Tav ≡ −1
        │             (baseline acceleration; solves CC fine-tuning *if* τ really sets ρ_DE)
        │
        ├── Layer B: 6-domain centrifugal term  Ω_rot(t) = Ω_max sin(π t / T_cycle)
        │             (the DESI-visible evolution; w_eff drifts)
        │
        └── Layer C: late Tav-BOOM / CCC refresh
                      (possible sharp feature in H(z) or a GW background)
```

Gatlin’s May paper emphasizes Layer A and says “dark energy has \(w=-1\).” Brown’s 17 June DESI note keeps Layer A and *adds* Layer B precisely so the theory can speak to DESI’s evolving \(w(z)\). Those two sentences are not in contradiction if one distinguishes **baseline vacuum** from **effective 4D equation of state**. They *are* in tension if Layer A is taken as the whole story.

A clean TSB statement, restated:

> The true vacuum equation of state is locked at \(w_{\mathrm{Tav}}=-1\) by the rigid \(\tau\)-circle. What DESI calls “dynamical dark energy” is not a change in that vacuum. It is the time-dependent centrifugal stress of the rotating six-domain supersphere, now past the rising half of the present aeon.

---

## 4. Mapping TSB onto DESI observables

### 4.1 The \(w_0\)–\(w_a\) quadrant

CPL is a *local* two-parameter compression of \(w(z)\) around \(a\sim 1\). TSB’s sine-decay of \(\Omega_{\mathrm{rot}}\) is a *global* function of \(t/T_{\mathrm{cycle}}\). Near the present they can look alike.

If we are slightly past mid-cycle:

- \(\Omega_{\mathrm{rot}}\) is still large, so acceleration is still happening \(\Rightarrow\) \(w_{\mathrm{eff}}\) still near \(-1\).
- \(d\Omega_{\mathrm{rot}}/dt < 0\), so the extra term is fading \(\Rightarrow\) \(w_{\mathrm{eff}}\) is *less* negative than it was at \(z\sim 0.5\)–\(1\).

That is exactly the DESI-preferred quadrant \(w_0 > -1\), \(w_a < 0\).

A first-order translation (not a published TSB fit, an orientation):

\[
w_{\mathrm{eff}}(a) \approx -1 + \delta w_{\mathrm{rot}}(a),
\]

where \(\delta w_{\mathrm{rot}}\) is set by how fast \(\Omega_{\mathrm{rot}}\) is falling relative to the Casimir floor. If the fall-off is gentle, \(w_0 \approx -0.8\) to \(-0.9\) with \(w_a\) of order \(-0.5\) to \(-0.8\) is the natural ballpark — which happens to be where DES + DESI + CMB currently sit.

This is *not* yet a parameter-free TSB prediction of \((w_0, w_a)\). To make it one, \(\Omega_{\max}\) and \(T_{\mathrm{cycle}}\) (or equivalently \(\omega(t)\) and \(R_{\mathrm{SB}}\)) must be fixed by the same geometry that already fixes \(\tau\) and the \(\beta_i\). That matching is the open calculation.

### 4.2 BAO shape, not just \(w_0, w_a\)

Because TSB modifies \(H(z)\) through a *sum* of a constant term and a slow sine, it predicts a specific shape for \(D_M(z)/r_d\) and \(D_H(z)/r_d\), not an arbitrary CPL curve. The cleanest DESI-era observable for that is the \(r_d\)-free ratio

\[
F_{\mathrm{AP}}(z) = \frac{D_M(z)}{D_H(z)} = \frac{H(z)}{c}\int_0^z \frac{c\, dz'}{H(z')}.
\]

A TSB \(H(z)\) that is \(\Lambda\mathrm{CDM}\)-like at \(z\gtrsim 2\) (Casimir floor plus small \(\Omega_{\mathrm{rot}}\) early on) and slightly “faster-expanding / weaker-DE” at \(z\lesssim 0.5\) will:

- leave the Ly\(\alpha\) anchor near the Planck \(\Lambda\mathrm{CDM}\) track (consistent with the July 2026 full-shape shift),
- pull galaxy BAO at \(z\sim 0.3\)–\(0.8\) off the Planck track in the direction DESI actually sees.

That redshift-dependent pattern is a sharper test than a single \((w_0, w_a)\) point.

### 4.3 Hubble tension and \(S_8\)

TSB’s May paper already claimed that the macroscopic extra dimension adjusts low- and intermediate-redshift expansion enough to raise the inferred \(H_0\) and suppress clustering (\(S_8\)). Layer B strengthens that claim: a decaying rotational term changes the *growth function*

\[
f\sigma_8(z) \propto \Omega_m(z)^\gamma \sigma_8(z)
\]

as well as the distances. DESI full-shape RSD and DES/KiDS/HSC weak lensing are therefore not side issues. They are the perturbation-sector counterpart of the same \(\Omega_{\mathrm{rot}}(t)\).

If Layer B is real, one expects:

- geometry (BAO, SN) to prefer evolving \(w\),
- growth (RSD, \(3\times 2\mathrm{pt}\)) to prefer a slightly lower \(\sigma_8\) than Planck \(\Lambda\mathrm{CDM}\),
- *without* requiring a separate early-dark-energy or decaying-DM module.

Current DES Y6 \(3\times 2\mathrm{pt}\) + DESI combinations still land in the same \(w_0>-1,\, w_a<0\) quadrant, which is encouraging for a single-mechanism story, but the growth-sector errors are still large.

### 4.4 The Tav scale in the DESI map

The same \(\tau = 7\,h^{-1}\,\mathrm{Mpc}\) that sources Layer A is also a *comoving coherence scale*. TSB therefore predicts residual 7-fold / 142857 structure in large-scale clustering, not only in Planck \(D_\ell\) residuals. That is a different DESI observable from BAO distances: it is a feature in the broadband power spectrum or in marked correlation functions at \(\sim 7\,h^{-1}\,\mathrm{Mpc}\), not in the \(100\,h^{-1}\,\mathrm{Mpc}\) BAO bump.

Those two tests should not be conflated:

| Observable | What it tests in TSB |
|---|---|
| BAO \(D_M/r_d\), \(D_H/r_d\), \(F_{\mathrm{AP}}\) | Layers A+B (background \(H(z)\)) |
| Broadband \(P(k)\) or \(\xi(s)\) near \(7\,h^{-1}\,\mathrm{Mpc}\) | Tav resonance scale itself |
| RSD \(f\sigma_8(z)\) | Whether \(\Omega_{\mathrm{rot}}\) clusters or is smooth |
| SN Hubble diagram | Same background \(H(z)\), different systematics |
| CMB \(\theta_*\), \(\Omega_m h^2\) | Early-time Casimir floor + neutrino/sterile leakage |

---

## 5. Points of genuine contact — and genuine tension

### Contact

1. DESI’s preferred quadrant is *qualitatively* what a mid-to-late-cycle decaying centrifugal term produces.
2. The two-layer split (rigid \(w=-1\) floor + decaying extra term) automatically avoids the worst phantom pathologies of a pure \(w<-1\) fluid: the Casimir floor cannot cross into \(w<-1\); only the *effective* sum can look phantom for a while.
3. A high-\(z\) Ly\(\alpha\) point sliding back toward \(\Lambda\mathrm{CDM}\) is natural if \(\Omega_{\mathrm{rot}}\) was smaller at early times (sine still climbing, or still small). The evolution is supposed to be a *late* effect.
4. The same geometry is already being asked to do Hubble-tension and dipole work. One mechanism, several anomalies, is the right kind of economy — if the numbers close.

### Tension / open problems

1. **Units and Friedmann bookkeeping.** Equation (1) of the 17 June note mixes \(H^2\), \(\Lambda/3\), and a raw \(\Omega_{\mathrm{rot}}\). A follow-up should write a single consistent 5D reduction:

   \[
   H^2 = \frac{8\pi G}{3}\bigl(\rho_m + \rho_{\mathrm{Tav}} + \rho_{\mathrm{rot}}(t)\bigr),
   \]

   with \(\rho_{\mathrm{Tav}}\) fixed by \(\tau\) and \(\rho_{\mathrm{rot}}\) fixed by \(\{\beta_i,\omega,R_{\mathrm{SB}}\}\).

2. **Is \(\rho_{\mathrm{Tav}}\) really the observed \(\rho_{\mathrm{DE}}\)?** A Casimir energy \(\hbar c/\tau^4\) with \(\tau \sim 7\,h^{-1}\,\mathrm{Mpc}\) is *far smaller* than the observed dark-energy density if taken as a 4D vacuum energy in the naive way. The framework must specify the 5D Einstein–Hilbert reduction factor (volume of \(S^1\), warp, number of domains) that lifts that Casimir energy up to \(\rho_{\mathrm{crit}}\). Without that factor, Layer A does not yet numerically replace \(\Lambda\).

3. **\(T_{\mathrm{cycle}}\) is not yet geometric.** The sine model is a phenomenological envelope. If TSB is parameter-free, \(T_{\mathrm{cycle}}\) should drop out of the same E\(_8\) / Tav / conformal-cell closure that produces \(m_0\) and \(\tau\). Until it does, Layer B is a well-motivated *ansatz*, not yet a zero-parameter prediction of \((w_0,w_a)\).

4. **Perturbations.** DESI + DES will not accept a background-only story. One must specify the sound speed \(c_s^2\) of \(\rho_{\mathrm{rot}}\) and the gravitational slip. A purely kinematic centrifugal term in a higher-dimensional geometry typically has \(c_s^2 \approx 1\) (smooth DE). That is testable against RSD and lensing, and it is a *prediction*, not a free function.

5. **“DESI mathematically confirms the re-convergence phase” is too strong.** DESI currently prefers a weakening effective \(w\) at \(2.3\)–\(4.2\sigma\) depending on the combination, with a high-\(z\) full-shape counter-pull. That is a *compatible hint*, not a confirmation. The honest TSB posture is: the data have moved into the quadrant the geometry said they should, and the next DESI/Euclid increments can throw them back out.

6. **Internal wording drift.** May 2026: “dark energy has \(w=-1\).” June 17: “static \(w=-1\) plus decaying \(\Omega_{\mathrm{rot}}\).” June 25: late “BOOM!” reconfiguration. Those can be stacked, but papers should say so explicitly so readers do not treat them as three rival models.

---

## 6. What would count as a TSB success — or a failure — in DESI-class data

### Success pattern (all of these together, not any one)

- BAO + SN continue to prefer \(w_0 \in [-0.90,-0.75]\), \(w_a \in [-0.9,-0.3]\) as errors shrink, *and*
- Ly\(\alpha\) / high-\(z\) \(F_{\mathrm{AP}}\) stays close to the \(\Lambda\mathrm{CDM}\) track (evolution is late), *and*
- growth probes do not demand a clustering DE fluid (\(c_s^2 \ll 1\)), *and*
- a residual feature near \(7\,h^{-1}\,\mathrm{Mpc}\) appears in DESI/Euclid clustering after standard BAO + reconstruction, *and*
- the same \(\{\beta_i,\tau\}\) that fit SPARC / dipole also reproduce the BAO \(H(z)\) shape with no extra knobs.

### Failure pattern

- Final DESI + Euclid + Roman distances lock onto \(w_0=-1\), \(w_a=0\) at high significance, *or*
- \(w(z)\) reconstruction demands several independent wiggles that a single sine of \(t/T_{\mathrm{cycle}}\) cannot produce, *or*
- growth data require a clustering dark-energy fluid or a strongly scale-dependent slip that the 5D reduction does not give, *or*
- the Casimir-matching calculation shows \(\rho_{\mathrm{Tav}}\) off the observed density by many orders of magnitude with no remaining geometric factor to absorb.

The last of those is the sharpest *theoretical* risk and does not even need more survey data.

---

## 7. Re-examination, compressed

Putting the framework’s own sentences next to the data:

| TSB statement | DESI-era reading |
|---|---|
| Vacuum pressure from \(\tau=7\,h^{-1}\,\mathrm{Mpc}\) is locked at \(w=-1\) | Explains why a cosmological-constant *floor* is a good zeroth-order model, and why high-\(z\) distances should not wander far from Planck |
| Six-domain centrifugal term \(\Omega_{\mathrm{rot}}(t)\) is the evolving piece | Explains why low-\(z\) BAO+SN prefer \(w_0>-1\), \(w_a<0\) without introducing a quintessence potential |
| We are approaching / passing mid-cycle re-convergence | Explains *why now* — the weakening is a phase of the aeon, not a coincidence |
| Late BOOM! / CCC refresh | Predicts a possible sharp late feature beyond smooth CPL; not yet seen, and not required by current DESI |
| Same geometry sets \(m_0\), halos, dipole, \(H_0\) | The scientific bet: one rigid construction, many observables. DESI is only one slice |

The cleanest way to say how TSB posits dark energy to work is therefore:

> Dark energy is not a substance. It is the 4D appearance of (i) a rigid Casimir pressure fixed by the Tav circle and (ii) the centrifugal stress of six staggered domains on a rotating supersphere. DESI is watching the second term roll over.

That is the claim. The next quantitative job is to reduce Layer B to the same geometric numbers already used for \(m_0\) and \(\tau\), write a consistent perturbed 5D action, and confront the actual DESI DR2 \(D_M/r_d\), \(D_H/r_d\) vector rather than the compressed \((w_0,w_a)\) plane.

---

## 8. Sources used in this session

### TSB corpus

- William Brown, *The Rotational Decay of Effective Dark Energy: A Tav-Superblock Cosmological Evaluation of DESI Data*, Zenodo, 17 June 2026. https://zenodo.org/records/20732543
- William Wylde / William Brown, *The Unified Tau-Superblock Cosmology … Update v2.0*, Zenodo, 25 June 2026. https://zenodo.org/records/20849532
- Ernest C. Gatlin III, *The Unified Tav-Superblock Cosmology: Emergent Phenomenology from a Macroscopic 5D Kaluza-Klein Substrate*, Zenodo, May 2026. https://zenodo.org/records/20278556

### DESI / dark-energy data papers

- DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints*, arXiv:2503.14738, PRD 112, 083514 (2025).
- DESI DR2 results guide, 19 March 2025, https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/
- DES Y6 + DESI DR2 dynamical-DE combination, arXiv:2605.27221 (Aug 2026).
- Review: *Dark Energy After DESI DR2*, arXiv:2602.05368.
- DESI Ly\(\alpha\) full-shape update discussion, DESI site / Turner note, 30 July 2026.

Local copies of the three TSB PDFs used for quotation:

- `artifacts/tsb_desi/rotational_decay_de.pdf`
- `artifacts/tsb_desi/tau_superblock_update_v2.pdf`
- `artifacts/tsb_desi/unified_tav_sb_gatlin.pdf`

---

*End of session note. 28 August 2026.*
