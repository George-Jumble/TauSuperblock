# Session 2026-09-30 — Nap Theory aggregator vs the source papers (CMB tilt, 3d Ising η, Dreyer discreteness)

**Date:** 2026-09-30  
**Query:** Analyze the listed papers and the conclusion the aggregator has drawn from them.  
**Aggregator:** YouTube channel *Nap Theory*, video *The Hidden Number Inside the Big Bang... And Why Physicists Refuse to Explain It* (`v=X9fTGr9PA4A`, uploaded 2026-09-28).  
**Status vs TSB locks:** Take as *constraint / analogue only*. Do **not** lock \(1-n_s=\eta_{\mathrm{Ising}}\), do **not** lock Dreyer discreteness as the TSB floor, do **not** retire inflation-tilt language by slogan.

---

## 1. What the aggregator actually concludes

The video’s chain is:

1. The CMB scalar spectrum is almost scale-invariant but not quite. The “lean” is
   \[
   1-n_s \approx 0.035\text{–}0.04.
   \]
2. The same number appears as the 3d Ising anomalous dimension \(\eta\) of a boiling / critical fluid (Wilson RG; conformal bootstrap).
3. Olaf Dreyer (2013) identified the two numbers and proposed that the early universe *froze through a phase transition* rather than stretching through inflation.
4. That freeze-out would leave a fundamental grain of space. Gravity would be emergent (“why things fall,” internal relativity).
5. “Physicists refuse to explain it this way” because inflation already occupies the chair.

That is a *narrative identification*, not a derivation that the listed observational papers themselves draw.

---

## 2. Variable key (complete)

| Symbol | Meaning |
|---|---|
| \(n_s\) | Scalar spectral index of the primordial curvature power spectrum \(\mathcal{P}_\mathcal{R}(k)\propto k^{n_s-1}\) |
| \(1-n_s\) | Tilt away from exact Harrison–Zeldovich scale invariance (\(n_s=1\)) |
| \(A_s\) | Amplitude of \(\mathcal{P}_\mathcal{R}\) at the pivot scale (usually \(k_*=0.05\,\mathrm{Mpc}^{-1}\)) |
| \(r\) | Tensor-to-scalar ratio |
| \(r_{0.002}\) | \(r\) evaluated at \(k=0.002\,\mathrm{Mpc}^{-1}\) |
| \(\eta\) | Anomalous dimension of the spin operator in a critical theory; for a scalar \(\sigma\), \(\eta=2\Delta_\sigma-d+2\) in \(d\) spatial dimensions. In 3d Ising, \(\eta=2\Delta_\sigma-1\) |
| \(\Delta_\sigma\) | Scaling dimension of the 3d Ising spin operator |
| \(\Delta_\varepsilon\) | Scaling dimension of the 3d Ising energy operator |
| \(c\) | Central charge of a 2d CFT, or the analogue used in the 3d bootstrap \(c\)-minimization conjecture |
| \(\mathcal{P}_\mathcal{R}(k)\) | Dimensionless primordial curvature power spectrum |
| \(N\) | Number of e-folds of inflation remaining after a given mode exits the Hubble radius |
| \(w\) | Equation-of-state parameter \(p/\rho\) |
| \(1+w\) | Deviation of the inflating fluid from a pure cosmological constant |
| KZM | Kibble–Zurek mechanism: defect (or domain) density \(\sim\tau_Q^{-\nu/(1+\nu z)}\) after a finite-rate quench |
| \(\tau_Q\) | Quench time through criticality |
| \(\nu,z\) | Correlation-length and dynamical critical exponents |
| QNM | Quasi-normal mode of a perturbed black hole |
| \((\ell,m,n)\) | Angular, azimuthal, and overtone indices of a QNM |
| \(M,a\) | Black-hole mass and dimensionless spin (Kerr) |
| \(\alpha_{\mathrm{TSB}}\) | TSB anomalous dimension \(1-\log_7 6\approx 0.079218\) (locked 2026-07-20; *not* \(\eta_{\mathrm{Ising}}\)) |
| \(\Delta_{\mathrm{Tav}}\) | Inserted nucleon-third scale \(313.1\,\mathrm{MeV}\) (not derived from this stack) |
| \(\Phi_7,\Phi_8\) | TSB scrape / reset phases |
| Mirron | Unbound Planck–Kerr topological defect; preferred TSB term (soliton deprecated) |

Power spectrum convention used by Planck / ACT:

\[
\mathcal{P}_\mathcal{R}(k)=A_s\left(\frac{k}{k_*}\right)^{n_s-1}.
\]

Harrison–Zeldovich: \(n_s=1\). Observed lean: \(n_s<1\).

3d Ising anomalous dimension:

\[
\eta_{\mathrm{Ising}}=2\Delta_\sigma-1.
\]

El-Showk et al. (2014) quote \(\Delta_\sigma=0.518154(15)\), hence

\[
\eta_{\mathrm{Ising}}\approx 0.03631.
\]

Later bootstrap tightenings stay in the same ballpark (\(\eta\approx 0.0363\)).

---

## 3. Paper-by-paper: what each source actually says

### 3.1 Dreyer 2013, “The world is discrete” — arXiv:1307.6169

**Claim in the paper:** The nearly scale-free CMB spectrum is the two-point function of an order parameter at a *phase transition*, not the frozen vacuum fluctuation of an inflaton. The measured tilt \(\approx 0.04\) *is* the anomalous dimension of that correlator. The existence of a tilt is then read as evidence for a fundamental short-distance cutoff that has not been seen any other way.

**What it does not do:**
- It does not compute \(A_s\sim 2.1\times 10^{-9}\).
- It does not produce the acoustic-peak structure, TE/EE, lensing, or Gaussianity.
- It does not specify the 3d Ising CFT as the unique early-universe CFT; the number 0.04 is taken from the then-current CMB tilt and *matched* to a critical exponent.
- It does not replace the need for a horizon / flatness solution; it *asserts* that a critical quench can do the same jobs.

This is the aggregator’s load-bearing citation. It is a short conceptual paper, not a likelihood analysis.

### 3.2 Planck 2018 X, “Constraints on inflation” — arXiv:1807.06211

**Measured, not interpreted as Ising:**

\[
n_s=0.9649\pm 0.0042\quad(68\%\,\mathrm{CL})
\quad\Rightarrow\quad
1-n_s=0.0351\pm 0.0042.
\]

No running of \(n_s\) is required. Combined with BICEP2/Keck BK15:

\[
r_{0.002}<0.056\quad(95\%\,\mathrm{CL}).
\]

The paper’s *own* conclusion is that single-field slow-roll with a *concave* potential \(V''(\phi)<0\) is favoured, that non-parametric reconstructions of \(\mathcal{P}_\mathcal{R}(k)\) are consistent with a pure power law, and that there is no evidence for features, oscillations, or non-adiabatic modes at the sensitivity of Planck 2018.

Planck does **not** mention 3d Ising, Wilson, or Dreyer. The number \(0.035\) is a fit parameter of \(\Lambda\)CDM + power-law primordial spectrum.

### 3.3 ACT DR6 — arXiv:2503.14452 (2025)

Joint P-ACT (+ lensing + DESI DR1) gives

\[
n_s=0.974\pm 0.003
\quad\Rightarrow\quad
1-n_s=0.026\pm 0.003,
\]

with \(H_0=68.22\pm 0.36\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) (tightens to \(68.43\pm 0.27\) with DESI DR2). Spectra are well fit by \(\Lambda\)CDM. No excess lensing, no departure from flatness.

**This is the single most important update against the aggregator’s 2013 matching.**  
Dreyer used “the tilt has been measured to be 0.04.” Planck 2018 still sat at \(0.035\pm 0.004\), compatible with \(\eta_{\mathrm{Ising}}\approx 0.0363\). ACT DR6 moved \(n_s\) *up*. The lean is now \(\approx 0.026\), about \(3\sigma\) below \(\eta_{\mathrm{Ising}}\) if one pretends the identification is a sharp prediction. The coincidence that the video treats as a frozen fingerprint has *moved*.

### 3.4 Mukhanov 2013, “Quantum cosmological perturbations” — arXiv:1303.3925

Hydrodynamical, model-independent inflation: the inflating stage is completely characterized by a smooth function \(1+w\) of the remaining e-folds \(N\). Result:

- \(n_s\) must deviate from 1 by *at least* \(\sim 3\%\), irrespective of the particular inflaton potential, because inflation has to *end*.
- Given the observed \(n_s\), there is a lower bound on tensors.

This is the opposite framing of Dreyer. The tilt is not a mysterious leftover of a discrete grain; it is the *minimal* scar left by the fact that a quasi-de Sitter phase cannot last forever. Starobinsky \(R^2\) inflation, which the video itself mentions, predicts

\[
n_s\approx 1-\frac{2}{N},\qquad
r\approx\frac{12}{N^2},
\]

so for \(N\sim 50\)–\(60\) one has \(1-n_s\sim 0.033\)–\(0.040\) *without any reference to Ising*.

### 3.5 El-Showk et al. 2014, 3d Ising bootstrap II — arXiv:1403.4545

Precision CFT, not cosmology. Conjecture: the 3d Ising spectrum *minimizes* the analogue of \(c\) among unitary crossing-symmetric solutions. They reconstruct the first \(\mathbb{Z}_2\)-even operators and find a sharp spectral transition at

\[
\Delta_\sigma=0.518154(15).
\]

This is the clean modern source for \(\eta_{\mathrm{Ising}}\approx 0.0363\). The paper contains no CMB sentence. Universality says: *any* system in the 3d Ising class, at equilibrium criticality, has this \(\eta\). It does not say: the primordial curvature correlator is that operator.

### 3.6 Wilson, Nobel 1982

RG + \(\varepsilon\)-expansion + block-spin: critical exponents are universal and can be computed from a fixed-point field theory. Necessary background for why \(\eta\) is a real, reproducible number. Not a cosmology paper.

### 3.7 Nobel 2006 “speedread” (COBE / CMB)

Mather and Smoot: the CMB is a \(2.725\,\mathrm{K}\) blackbody with \(\sim 10^{-5}\) anisotropies. Historical arena for the “oldest light,” Penzias–Wilson horn, COBE, later WMAP/Planck. Does not fix \(n_s\) at 0.04 and does not mention Ising.

### 3.8 Du et al., Nature Physics 2023 — Kibble–Zurek of Ising domains

Lab result: cooling-rate dependence of *topologically trivial* 3d structural Ising domains (NiTiO\(_3\) ferro-rotation; BiTeI polar) follows a KZM power law. NiTiO\(_3\) slope matches 3d Ising; BiTeI slope is *steeper* because of long-range dipoles.

**Use:** KZM is real for Ising domains.  
**Do not use:** as a measurement of CMB \(n_s\), or as evidence that the universe is a 3d Ising quench. KZM predicts *defect / domain density versus quench rate*, not the tilt of a superhorizon curvature spectrum.

### 3.9 Dreyer et al. 2003, “Black hole spectroscopy” — gr-qc/0309007

Proposal: a ringdown that is a sum of damped sinusoids can test the GR no-hair theorem, because a Kerr hole’s QNM frequencies are fixed by \((M,a)\) alone. Statistical test against noisy data. This is a *continuum GR* paper.

### 3.10 LVK, GW250114 spectroscopy — arXiv:2509.08099 (2025)

Loudest event to date. At least two QNMs required. Dominant \((\ell=m=2)\) mode and first overtone match Kerr to tens of percent; \((\ell=m=4)\) constrained; suite of IMR tests as tight as (sometimes tighter than) the stacked GWTC-4 sample.

**Aggregator use:** establish that Dreyer is a serious gravitational-wave physicist, then transfer authority to the 2013 discreteness paper.  
**Actual implication:** the best single-event ringdown we have is *consistent with classical Kerr*. That is evidence *against* a large, astrophysically visible grain of spacetime at horizon scales, not for it. Discreteness, if it exists, is pushed below the scale these QNMs probe.

### 3.11 Dreyer 2012, “Internal relativity” — arXiv:1203.2641

Equivalence principle implemented by gluing *vacua of an underlying solid-state-like quantum model*, not by a metric connection on Minkowski fibers. Gravity is emergent; \(G\) is in principle calculable. Companion to “Why things fall” (arXiv:0710.4350, listed in the video sources but not in the user’s raw URL dump).

This is a research program, not a completed derivation of Einstein equations plus the observed \(n_s\).

---

## 4. Verdict on the aggregator’s conclusion

| Aggregator sentence | Status |
|---|---|
| CMB has a lean \(1-n_s\sim 0.03\)–\(0.04\) | **True as of Planck 2018.** Softened by ACT DR6 to \(0.026\pm 0.003\). |
| 3d Ising \(\eta\approx 0.0363\) is a real, precise number | **True.** Wilson + bootstrap. |
| The two numbers being close is interesting | **Fair as a coincidence to notice.** Not a theorem. |
| Therefore the universe froze rather than inflated | **Not licensed by the data papers.** Planck and ACT fit \(\Lambda\)CDM + inflation-compatible \(n_s\). Mukhanov shows inflation *must* tilt. Starobinsky produces the same 0.03–0.04 from \(2/N\). |
| The lean is the fingerprint of a discrete grain | **Hypothesis of Dreyer 2013, not a result of Planck/ACT/Ising/KZM.** ACT movement of \(n_s\) weakens the numerical hook. |
| KZM / boiling CO\(_2\) “is” the Big Bang | **Category error.** Universality equates *exponents of the same class at criticality*, not entire histories. A critical fluid correlator \(\langle\sigma(x)\sigma(0)\rangle\sim 1/|x|^{1+\eta}\) is not \(\mathcal{P}_\mathcal{R}(k)\). |
| GW ringdown confirms the same physicist, hence the discrete paper | **Authority transfer, not a deduction.** GW250114 confirms Kerr continuum spectroscopy. |
| Physicists “refuse to explain it” | **Rhetoric.** The 2013 paper was public. It was not adopted because it does not compute the rest of the CMB, because inflation already predicts the tilt window, and because a naive early-universe phase transition overproduces defects unless something else dilutes them. |

**Fair residual:** it is legitimate to keep “critical quench / KZM / emergent gravity from an underlying discrete medium” on the analogue shelf. It is not legitimate to treat \(1-n_s=\eta_{\mathrm{Ising}}\) as an observed equality after ACT DR6.

---

## 5. Why the numerical match was always weaker than the narration

Write the two quantities with their operational definitions side by side.

CMB tilt (operational):

\[
n_s-1
=\frac{\mathrm{d}\ln\mathcal{P}_\mathcal{R}}{\mathrm{d}\ln k}\Big|_{k_*}.
\]

Ising \(\eta\) (operational):

\[
\langle\sigma(x)\sigma(0)\rangle
\sim\frac{1}{|x|^{d-2+\eta}}
\quad(d=3)
\;\Rightarrow\;
\eta=2\Delta_\sigma-1.
\]

To identify them one must argue that the primordial curvature perturbation *is* (or is linearly slaved to) a 3d Ising order-parameter field evaluated on a constant-time slice, and that the Fourier transform of \(1/|x|^{1+\eta}\) *is* \(\mathcal{P}_\mathcal{R}(k)\propto k^{\eta-1}\) after the appropriate projection onto superhorizon \(\mathcal{R}\). Dreyer sketches this; he does not carry it through the transfer functions, the radiation-to-matter transition, or the acoustic physics that actually set the observed \(C_\ell\).

Even granting the sketch, a 3d critical correlator gives a *power-law two-point function*, not automatically:
- the observed \(A_s\),
- adiabatic growing mode,
- vanishing isocurvature,
- small \(f_{\mathrm{NL}}\),
- the measured \(r\) bound,
- \(H_0\) and \(\Omega_b h^2\) consistency with BBN and BAO.

Inflation, whatever one thinks of its UV completion, *does* produce that package from one slow-roll trajectory.

---

## 6. Relation to current TSB locks (do not conflate)

| Quantity | Value | Lock status |
|---|---|---|
| \(\alpha=1-\log_7 6\) | \(\approx 0.079218\) | Locked 2026-07-20 as 6-domain / 142857 shear anomalous dimension. **Different number from \(\eta_{\mathrm{Ising}}\).** |
| \(\Delta_{\mathrm{Tav}}\) | \(313.1\,\mathrm{MeV}\) | Inserted nucleon-third scale, not a Vălean output, not a CMB-tilt output (2026-09-26). |
| \(\tau=7\,h^{-1}\,\mathrm{Mpc}\) KK circle | — | **Retired** as TEP / pinch premise (2026-09-20, 2026-09-21). The attached V2.0 TeX still carries it; that is historical. |
| Gravity | residual-\(L\) spatial compression of bound EM; no fundamental graviton | Locked. Compatible *in spirit* with Dreyer’s “emergent \(G\) from an underlying medium,” but the TSB medium is the 8-phase / six-domain clockwork, not 3d Ising. |
| Mirron / Kerr seam | apparent seam, bounce, not Kerr-at-infinity as the physical compact object | Constrained by the 2026-09-30 CCBH stack. GW250114 Kerr QNMs constrain the *exterior* ringdown, which TSB already treats as the local chart near a seam, not as a theorem that the interior is a classical Kerr disk. |
| Dynamic Refresh | binding-floor protocol only, not a universal COM pin | Locked 2026-09-30 after Pedalino. A cosmological “freeze” is *not* DR of isolated COMs. |

**Refuse as locks from this video:**
- \(1-n_s:=\eta_{\mathrm{Ising}}\),
- “inflation is replaced,”
- “the grain of space is the 3d Ising lattice spacing,”
- \(\alpha_{\mathrm{TSB}}=\eta_{\mathrm{Ising}}\) (they differ by a factor \(\sim 2\)),
- any claim that Planck/ACT *measured* a phase-transition cosmology.

**Keep as analogue:**
- Wilsonian universality: exponents can be discrete / combinatorial even when the IR field looks continuous.
- KZM: a finite-rate crossing of a critical surface leaves a density of domains / defects set by critical exponents. TSB already has domain walls \(W_{ab}\) and a domain-cross energy \(E_\times(a\to b)=\theta_{ab}\Delta_{\mathrm{Tav}}\) (2026-09-29). That is a *different* energy, not KZM.
- Emergent gravity from an underlying quantum medium (Dreyer internal relativity) is philosophically closer to residual-\(L\) gravity than to a fundamental graviton. It is not a derivation of the TSB residual-\(L\) formula.

---

## 7. Note on the attached TSB TeX (context, not the aggregator)

Three attachments rode along with the URL dump:

1. `Unified_Tav_Superblock_Cosmology__V2_0__main.tex` (2026-06-27) — historical V2.0 with \(\tau=7\,h^{-1}\,\mathrm{Mpc}\), \(M_{\mathrm{eff}}^{p-k}\approx 313.1\,\mathrm{MeV}\) written as a Planck-mass / bubble-count formula, \(\Omega_{\mathrm{DM}}/\Omega_b\approx 5.2\) as five hidden domains. Several of those clauses are now retired or reclassified (Tau circle, 313 as theorem, DM-as-five-domains as a lock).
2. `The_Tau_Cylinder as Geometric Arena...tex` (2026-06-28) — Tau cylinder plus Vălean alternating Euler sums plus Kerr chart at the reset seam. The cylinder-as-KK-fifth is the 2026-09-14 / 09-20 forbidden / optional-hook layer.
3. Two empty `Analytic_Derivation_of_the_Sterile_Branching_Ratio` TeX stubs (1 byte). No content to analyze.

They are *not* the aggregator’s sources. They are older TSB snapshots. Do not re-import \(\tau=7\,h^{-1}\,\mathrm{Mpc}\) from them on the back of this video.

---

## 8. Compact scorecard

| Source | What it establishes | What the aggregator adds |
|---|---|---|
| Planck 2018 X | \(n_s=0.9649\pm 0.0042\), \(r<0.056\), power-law \(\mathcal{P}_\mathcal{R}\) | “the hidden number is 0.04” |
| ACT DR6 2025 | \(n_s=0.974\pm 0.003\) | omitted / not used to update the hook |
| Mukhanov 2013 | inflation *must* tilt by \(\gtrsim 3\%\) | treated as background, not as a competing explanation of the same number |
| El-Showk et al. 2014 | \(\eta_{\mathrm{Ising}}\approx 0.0363\) | identified with \(1-n_s\) |
| Wilson 1982 | RG / universality | boiling CO\(_2\) = Big Bang |
| COBE / 2006 Nobel | CMB is real | mood-setting |
| Du et al. 2023 KZM | Ising domains obey KZM | quench = cosmological freeze |
| Dreyer 2013 | phase-transition alternative to inflation | load-bearing thesis |
| Dreyer 2003 + GW250114 | Kerr QNM spectroscopy works | authority transfer; actually supports continuum Kerr exteriors |
| Dreyer 2012 | emergent \(G\) from vacuum-gluing | “why things fall” as discrete-medium gravity |

**Bottom line:** the papers establish two precise, independent numbers and a well-defined alternative *hypothesis*. They do not establish the hypothesis. After ACT DR6 the numerical hook is worse, not better. TSB should keep \(\alpha=1-\log_7 6\) and the bound/unbound bounce language, and should not absorb \(1-n_s=\eta_{\mathrm{Ising}}\) as a lock.

---

## 9. Files / session trail

- This note: `Tau-Superblock-Universe/Personal Files/Session_2026-09-30_Nap_Theory_CMB_Tilt_vs_Ising_Eta.md`
- Mirror: `Personal Files/Session_2026-09-30_Nap_Theory_CMB_Tilt_vs_Ising_Eta.md`
- Related same-day notes: CCBH stack vs Superblock; Dynamic Refresh scope; Pedalino COM.
