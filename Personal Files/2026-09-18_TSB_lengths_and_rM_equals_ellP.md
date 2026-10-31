# Session log: Lengths already in the theory, and whether \(r_{\mathrm{M}}=\ell_P\) fixes \(\alpha_{\mathrm{fs}}\)

- **Session date:** Friday, 2026-09-18
- **Questions:** What lengths are already in the theory? Could regressing the Mirron radius to the Planck length fix the EM-fibre problem?
- **Short answer:** Three proper lengths are locked: \(\ell_P\), \(r_{\mathrm{M}}=\lambda_{313}\), \(R_\tau\). Everything else is a ratio of those three (or a density-derived spacing). Setting \(r_{\mathrm{M}}=\ell_P\) does **not** fix \(\alpha_{\mathrm{fs}}\). The 5D hop is \(\alpha_{\mathrm{5D}}=4(\ell_P/\varphi)^2\); at \(\varphi=r_{\mathrm{M}}=\ell_P\) that is \(\alpha=4\), not \(1/137\). It also moves the TEP floor from \(313\,\mathrm{MeV}\) to the Planck energy and collapses \(n_{\mathrm{hier}}\). The only fibre that hits CODATA inside the derived prefactor is \(\varphi_{\mathrm{EM}}\approx 23.41\,\ell_P\), which is **not** a locked TSB length. \(\log_7(r_{\mathrm{M}}/\ell_P)\approx 23.18\) is numerically near \(23.41\) and is a different object (an exponent, not a ratio \(\varphi/\ell_P\)).
- **This file:** `Personal Files/2026-09-18_TSB_lengths_and_rM_equals_ellP.md`
- **Parent:** `2026-09-18_5D_Einstein_dilaton_hop_and_Phi.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(\ell_P=\sqrt{\hbar G/c^3}\) | 4D Planck length \(\approx 1.616\times 10^{-35}\,\mathrm{m}\). PK-seed scale. |
| \(E_P=\hbar c/\ell_P\) | Planck energy \(\approx 1.22\times 10^{19}\,\mathrm{GeV}\). |
| \(r_{\mathrm{M}}=\lambda_{313}=\hbar c/\Delta_{\mathrm{TEP}}\) | Mirron / clock radius \(\approx 6.302\times 10^{-16}\,\mathrm{m}\). Locked to the 313.1 MeV floor. |
| \(\Delta_{\mathrm{TEP}}\approx 313.1\,\mathrm{MeV}\) | TEP / conformal-mother floor. |
| \(R_\tau\approx 7\,h^{-1}\,\mathrm{Mpc}\) | Tav-cylinder radius. \(\approx 10\,\mathrm{Mpc}\) at \(h=0.7\). |
| \(\ell_{\mathrm{pack}}=n_{\mathrm{M}}^{-1/3}\) | Mean inter-Mirron spacing. Not a primitive; follows from density. |
| \(n_{\mathrm{hier}}=\log_7(R_\tau/r_{\mathrm{M}})\approx 45.78\) | Hierarchical stretch, base 7. |
| \(n_{P\mathrm{M}}=\log_7(r_{\mathrm{M}}/\ell_P)\approx 23.18\) | Decades from Planck seed to Mirron clock. Not previously used as a fibre ratio. |
| \(\varphi\) | 5D EM-fibre radius in the Einstein–dilaton hop. |
| \(\alpha_{\mathrm{5D}}=4(\ell_P/\varphi)^2\) | Fine-structure candidate from the 2026-09-18 reduction. |
| \(\varphi_{\mathrm{EM}}/\ell_P=2/\sqrt{\alpha_{\mathrm{fs}}}\approx 23.41\) | Fibre that hits CODATA *inside that prefactor*. Not a corpus lock. |
| \(7\pi\approx 21.99\) | Nearest primitive×\(\pi\) to \(23.41\). Miss \(6.4\,\%\). |

---

## 1. Lengths already in the theory

Three **proper lengths** are locked by geometry or by a named empirical anchor. All other TSB lengths are products, quotients, or logarithms of these.

### 1.1 Planck seed — \(\ell_P\)

\[
\ell_P=\sqrt{\frac{\hbar G}{c^3}}\approx 1.616\times 10^{-35}\,\mathrm{m}.
\]
**Key:** 4D Planck length. The book-outline PK seeds nucleate at this scale. It is the short end of the hierarchy.

### 1.2 Mirron clock — \(r_{\mathrm{M}}\)

\[
r_{\mathrm{M}}=\lambda_{313}=\frac{\hbar c}{\Delta_{\mathrm{TEP}}}\approx 6.302\times 10^{-16}\,\mathrm{m},
\qquad
\Delta_{\mathrm{TEP}}\approx 313.1\,\mathrm{MeV}.
\]
**Key:** reduced Compton length of the TEP floor. Diameter tick \(\Delta t_\tau=2r_{\mathrm{M}}/c\). This is the length that entered the old \(V/I\) hop (and cancelled). Ratio to the seed:
\[
\frac{r_{\mathrm{M}}}{\ell_P}\approx 3.90\times 10^{19},\qquad
\log_7\Bigl(\frac{r_{\mathrm{M}}}{\ell_P}\Bigr)\approx 23.18.
\]

### 1.3 Tav cylinder — \(R_\tau\)

\[
R_\tau\approx 7\,h^{-1}\,\mathrm{Mpc}\approx 10\,\mathrm{Mpc}\ (h=0.7)\approx 3.09\times 10^{23}\,\mathrm{m}.
\]
**Key:** macroscopic extra-dimension radius in the kinematics / unification notes. Ratio to the clock:
\[
\frac{R_\tau}{r_{\mathrm{M}}}\approx 4.90\times 10^{38},\qquad
n_{\mathrm{hier}}=\log_7\Bigl(\frac{R_\tau}{r_{\mathrm{M}}}\Bigr)\approx 45.78.
\]
Seed to cylinder:
\[
\frac{R_\tau}{\ell_P}\approx 1.91\times 10^{58},\qquad
\log_7\Bigl(\frac{R_\tau}{\ell_P}\Bigr)\approx 68.96\approx 23.18+45.78.
\]

### 1.4 Not primitives

| Object | Why it is not a fourth length |
|---|---|
| \(\ell_{\mathrm{pack}}=n_{\mathrm{M}}^{-1/3}\) | Density-derived. Branch A keeps \(n_{\mathrm{M}}\) fixed; the spacing is then a frozen multiple of \(r_{\mathrm{M}}\). |
| \(\tau=2\pi\) in rescaled cylinder coordinates | A normalization of the same \(R_\tau\), not a new metre. |
| \(\varphi_{\mathrm{EM}}\approx 23.41\,\ell_P\) | Chosen so that \(\alpha_{\mathrm{5D}}=\alpha_{\mathrm{fs}}\). Not in the corpus before the 5D hop. |
| Quark Compton lengths | Phenomenology of the \(V_{\mathrm{orb}}\) map, not TSB primitives. |
| Berard \(r_{\mathrm{norm}}\approx B\) | Dimensionless suture, not a metre. |

So when the last note said “the lengths already in the theory,” it meant the triple
\[
\bigl(\ell_P,\; r_{\mathrm{M}},\; R_\tau\bigr)
\]
and the two base-7 exponents that connect them.

---

## 2. What each length does as the EM fibre

From the 5D hop, \(\alpha_{\mathrm{5D}}=4(\ell_P/\varphi)^2\).

| If \(\varphi=\) | \(\alpha_{\mathrm{5D}}\) | Verdict for electromagnetism |
|---|---|---|
| \(\ell_P\) | \(4\) | Strong, not \(1/137\) |
| \(r_{\mathrm{M}}\) | \(2.63\times 10^{-39}\) | Far too weak |
| \(R_\tau\) | \(1.10\times 10^{-116}\) | Vacuum-catastrophe weak |
| \(23.41\,\ell_P\) | \(1/137.04\) | Hits CODATA by choice of \(\varphi\) |

None of the three locked lengths is the EM fibre.

---

## 3. Regressing \(r_{\mathrm{M}}=\ell_P\)

Read “regress” as the identification \(r_{\mathrm{M}}\leftarrow\ell_P\): the Mirron *is* the Planck seed. Two consequences, both fatal for a silent fix.

### 3.1 The 5D hop still misses \(\alpha_{\mathrm{fs}}\)

\[
\alpha_{\mathrm{5D}}=4\Bigl(\frac{\ell_P}{r_{\mathrm{M}}}\Bigr)^2=4\Bigl(\frac{\ell_P}{\ell_P}\Bigr)^2=4.
\]
**Key:** \(\varphi=r_{\mathrm{M}}=\ell_P\) produces \(\alpha=4\), \(\Phi_{\mathrm{5D}}=8\). CODATA needs \(23.41\,\ell_P\), not \(1\,\ell_P\). Regression to Planck does not land on \(1/137\).

An 8π-convention in Einstein’s equation moves \(4\) to \(1/(2\pi)\approx 0.16\), still not \(1/137\), and still \(\mathcal{O}(1)\) rather than the target.

### 3.2 The rest of TSB breaks

The TEP floor is defined by the same radius:
\[
\Delta_{\mathrm{TEP}}=\frac{\hbar c}{r_{\mathrm{M}}}.
\]
At \(r_{\mathrm{M}}=\ell_P\),
\[
\Delta_{\mathrm{TEP}}=E_P\approx 1.22\times 10^{19}\,\mathrm{GeV},
\]
not \(313.1\,\mathrm{MeV}\). The conformal-mother scale, the 313.1 MeV friction floor, the hadronic clock, and the diameter tick
\[
\Delta t_\tau=\frac{2r_{\mathrm{M}}}{c}\sim 10^{-43}\,\mathrm{s}
\]
all move to the Planck regime. Then
\[
n_{\mathrm{hier}}=\log_7(R_\tau/r_{\mathrm{M}})\to\log_7(R_\tau/\ell_P)\approx 69,
\]
and the 45.8-decade stretch that was locked to \(\lambda_{313}\) is gone.

So \(r_{\mathrm{M}}=\ell_P\) is not a local patch on \(\alpha\). It is a collapse of the middle scale.

### 3.3 Dynamical regression \(r_{\mathrm{M}}(t)\to\ell_P\)

If the clock radius shrinks toward \(\ell_P\) while the 5D formula holds,
\[
\alpha(t)=4\Bigl(\frac{\ell_P}{r_{\mathrm{M}}(t)}\Bigr)^2
\]
*grows*. Atomic-clock bounds \(|\dot\alpha/\alpha|\lesssim 10^{-18}\,\mathrm{yr}^{-1}\) then require
\[
\bigl|\dot r_{\mathrm{M}}/r_{\mathrm{M}}\bigr|\lesssim 5\times 10^{-19}\,\mathrm{yr}^{-1}.
\]
A regression that is fast enough to matter cosmologically is already ruled out by the same clocks that killed density-thinning of \(Z_0\). A regression that is slow enough to pass the clocks does not move \(\alpha\) from \(10^{-39}\) to \(1/137\) in a Hubble time.

---

## 4. The near-miss that is not a derivation

\[
\log_7\Bigl(\frac{r_{\mathrm{M}}}{\ell_P}\Bigr)\approx 23.18,
\qquad
\frac{\varphi_{\mathrm{EM}}}{\ell_P}\approx 23.41.
\]
Those numbers sit next to each other on the page. They are not the same quantity. The first is the number of base-7 decades between two locked lengths. The second is the dimensionless fibre radius that makes \(\alpha_{\mathrm{5D}}=\alpha_{\mathrm{fs}}\) given the prefactor \(4\). Equating them is a category error. Recorded so it is not reused as a “result.”

\(7\pi\approx 21.99\) versus \(23.41\) is the same kind of miss, already logged.

---

## 5. Direct answers

**What lengths are already in the theory?**
\[
\ell_P,\qquad r_{\mathrm{M}}=\lambda_{313},\qquad R_\tau,
\]
plus the two logarithms \(n_{P\mathrm{M}}\approx 23.18\) and \(n_{\mathrm{hier}}\approx 45.78\). No fourth metre.

**Does \(r_{\mathrm{M}}=\ell_P\) fix the EM fibre?**
No. It gives \(\alpha=4\), destroys \(\Delta_{\mathrm{TEP}}=313.1\,\mathrm{MeV}\), and is clock-forbidden as a cosmic drift. The fibre that hits CODATA inside the 5D prefactor is \(23.41\,\ell_P\), which is not among the locked lengths.

---

## Ledger

| Claim | Status |
|---|---|
| Locked proper lengths are \(\{\ell_P,r_{\mathrm{M}},R_\tau\}\) | Corpus |
| \(\varphi=r_{\mathrm{M}}=\ell_P\) \(\Rightarrow\alpha_{\mathrm{5D}}=1/137\) | False (\(\alpha=4\)) |
| \(\varphi=23.41\,\ell_P\) \(\Rightarrow\alpha_{\mathrm{5D}}=\alpha_{\mathrm{fs}}\) | True inside the derived prefactor, tautological as a prediction |
| \(\log_7(r_{\mathrm{M}}/\ell_P)=\varphi_{\mathrm{EM}}/\ell_P\) | False (23.18 vs 23.41, and different units of meaning) |
| Dynamical \(r_{\mathrm{M}}(t)\to\ell_P\) | Clock-bounded; cannot traverse \(10^{19}\) in a Hubble time |

---

## Sources

- Parent 5D hop: `2026-09-18_5D_Einstein_dilaton_hop_and_Phi.md`
- TSB locks: \(\Delta_{\mathrm{TEP}}\), \(\tau\approx 7\,h^{-1}\,\mathrm{Mpc}\), \(n_{\mathrm{hier}}\), PK seeds at \(\ell_P\)
- CODATA \(\ell_P\), \(\alpha_{\mathrm{fs}}\)

---

*End of session note — 2026-09-18 TSB lengths and \(r_{\mathrm{M}}=\ell_P\).*
