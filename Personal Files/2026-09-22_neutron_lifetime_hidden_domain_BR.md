# Superblock Empirical Tests — Neutron Lifetime (Bottle vs Beam)

**Session date:** 2026-09-22  
**Engine label in log:** Superblock Residual Engine  
**Ledger line in log:** Superblock TEP floor (\(m_0=\Delta_{\mathrm{TEP}}=313.1\,\mathrm{MeV}\))  
**Corpus status of \(\Delta_{\mathrm{TEP}}\):** IN — independent of this confrontation (topological anchor)  
**Corpus status of the hidden-domain neutron branch:** **not IN**. This note records the test. It does not promote the branch to the live ledger.

---

## 1. Raw pipeline output (as received)

```
[Superblock Residual Engine] Superblock Empirical Tests — Neutron Lifetime Test
[Superblock Residual Engine] Superblock TEP floor m₀ = 313.1 MeV
========================================================================
SUPERBLOCK EMPIRICAL TESTS
Ledger: Superblock TEP floor (m₀ = 313.1 MeV)
========================================================================
[Loading] neutron_lifetime — Neutron lifetime (Bottle vs Beam) — PDG-style curated anchors
  Loaded 3 points.
--- Neutron Lifetime Anomaly → Hidden Domain Branching ---
Status: PASS
  observed_BR: 0.0107
  observed_BR_unc: 0.0006
  theory_target_BR: 0.0094
  compatibility_sigma: 1.3
  interpretation: ~1% branching to hidden domains via Planck-Kerr tunneling
  falsifiable_prediction: Magnetic field orientation dependence (octonionic phase overlap)
  plot: .../artifacts/neutron_lifetime_test.png
JSON report saved: .../artifacts/superblock_test_report.json
[TOPOLOGICAL ANCHOR] 313.1 MeV mass-gap signal is independent of empirical confrontation parameters.
```

Banner hygiene is improved relative to the light-quark log (no “TAV ENGINE”, no June-2026 Tav cosmology line). Keep it that way.

---

## 2. Variable and function key

| Symbol | Meaning |
|---|---|
| \(\tau_n\) | Free-neutron mean life |
| \(\tau_{\mathrm{bottle}}\) | Disappearance lifetime (UCN storage: material or magnetic / magneto-gravitational trap). Counts neutrons that *leave*. |
| \(\tau_{\mathrm{beam}}^{(p)}\) | Appearance lifetime from *proton* counting in a cold-neutron beam. Sensitive only to channels that yield a proton. |
| \(\tau_{\mathrm{beam}}^{(e)}\) | Appearance lifetime from *electron* counting (J-PARC TPC). Sensitive to channels that yield an electron. |
| \(\Gamma_{\mathrm{tot}}\) | Total disappearance width \(=1/\tau_{\mathrm{bottle}}\) |
| \(\Gamma_\beta\) | Charged \(\beta\) width inferred from proton (or electron) appearance \(=1/\tau_{\mathrm{beam}}\) |
| \(\Gamma_X\) | Extra width not producing the tagged charged particle |
| \(\mathrm{BR}_X\) | Branching fraction \(\Gamma_X/\Gamma_{\mathrm{tot}}\) |
| \(\Delta_{\mathrm{TEP}}=m_0\) | Geometric TEP / mass-gap floor. \(313.1\,\mathrm{MeV}\). **Not used as a fit knob in this test.** |
| \(r_M=\lambda_{313}\) | Mirron / Planck–Kerr 2-surface radius \(=\hbar c/\Delta_{\mathrm{TEP}}\approx 0.630\,\mathrm{fm}\) |
| \(\beta_i,\gamma_i\) | V_orb Scheme A domain speeds. Prime \(=u\) at rest. Neutron valence content \(udd\): one Prime + two near-Prime. |
| \(\mathrm{Aut}(\mathbb{O})\cong G_2\) | 8-phase clockwork. \(\Phi_8\) is Past ⇄ Future reset, not a CMS bin. |
| \(\sigma\) | Compatibility of observed BR with theory target, in units of the pipeline uncertainty |

### Functions

Total vs tagged widths (hidden-branch hypothesis):

\[
\Gamma_{\mathrm{tot}}
=\Gamma_\beta+\Gamma_X
=\frac{1}{\tau_{\mathrm{bottle}}},
\qquad
\Gamma_\beta
=\frac{1}{\tau_{\mathrm{beam}}}
\]

Branching fraction that *does not* produce the tagged charged particle:

\[
\mathrm{BR}_X
=1-\frac{\tau_{\mathrm{bottle}}}{\tau_{\mathrm{beam}}}
=\frac{\tau_{\mathrm{beam}}-\tau_{\mathrm{bottle}}}{\tau_{\mathrm{beam}}}
\]

First-order uncertainty (independent errors):

\[
\delta\mathrm{BR}_X
=\sqrt{
\left(\frac{\delta\tau_{\mathrm{bottle}}}{\tau_{\mathrm{beam}}}\right)^2
+
\left(\frac{\tau_{\mathrm{bottle}}\,\delta\tau_{\mathrm{beam}}}{\tau_{\mathrm{beam}}^2}\right)^2
}
\]

Compatibility as printed:

\[
\sigma
=\frac{\lvert\mathrm{BR}_X^{\mathrm{obs}}-\mathrm{BR}_X^{\mathrm{th}}\rvert}{\delta_{\mathrm{comb}}}
\]

The pipeline reports \(\sigma=1.3\) with \(\mathrm{BR}_X^{\mathrm{obs}}=0.0107\pm0.0006\) and \(\mathrm{BR}_X^{\mathrm{th}}=0.0094\). Using only the quoted \(0.0006\) gives \(2.17\sigma\). The printed \(1.3\sigma\) therefore implies a combined uncertainty \(\delta_{\mathrm{comb}}\approx0.0010\) (theory-side width \(\approx0.0008\) folded in, or a different covariance). Both numbers are recorded below.

Planck–Kerr Compton lock (unchanged, not fitted here):

\[
r_M=\frac{\hbar c}{\Delta_{\mathrm{TEP}}}=\frac{197.3269718\,\mathrm{MeV\cdot fm}}{313.1\,\mathrm{MeV}}=0.630236\,\mathrm{fm}
\]

---

## 3. External anchors (what “3 points” sit on)

The loader says “PDG-style curated anchors, 3 points.” Those are almost certainly one bottle number, one proton-beam number, and one third comparator (material bottle, or J-PARC, or a PDG average). Public 2025–2026 values:

| Estimator | \(\tau_n\) (s) | Role |
|---|---|---|
| Magnetic-bottle average (CERN Courier / PSI 2025) | \(877.8\pm0.3\) | Disappearance, B-trap |
| Material-bottle average (Wietfeldt PSI 2025) | \(880.1\pm0.48\) | Disappearance, walls |
| Proton-beam average | \(888.1\pm2.0\) | Appearance of \(p\) |
| PDG 2026 UCN average (beam excluded) | \(878.3\pm0.4\) (\(S=1.8\)) | Official disappearance avg |
| UCNTτ combined | \(\approx 877.82\) | Most precise magneto-grav. |
| NIST / Yue-style in-beam \(p\) | \(887.7\pm2.2\) | Appearance of \(p\) |
| J-PARC electron-TPC beam | \(877.2\pm1.7^{+4.0}_{-3.6}\) | Appearance of \(e^-\) |

Magnetic bottle vs proton beam is still \(\approx 10.3\,\mathrm{s}\) / \(\approx 5\sigma\) at the quoted averages. That part of the anomaly is live.

J-PARC is the important third point: it is a *beam* method that tags electrons rather than protons, and it landed on the *bottle* number, with a still-large systematic. Combining J-PARC with other beam data pulls the beam average down and shrinks the gap.

PSI workshop (13 Sep 2025) and CERN Courier (14 Jan 2026): community lean is **systematics**, not a fully explanatory exotic channel.

---

## 4. Arithmetic of the printed PASS

Pipeline:

\[
\mathrm{BR}_X^{\mathrm{obs}}=0.0107\pm0.0006,
\qquad
\mathrm{BR}_X^{\mathrm{th}}=0.0094,
\qquad
\sigma_{\mathrm{printed}}=1.3
\]

Reconstructed \(\Delta\tau\) if \(\tau_{\mathrm{beam}}=888\,\mathrm{s}\):

\[
\Delta\tau^{\mathrm{obs}}\approx 0.0107\times 888 \approx 9.50\,\mathrm{s},
\qquad
\Delta\tau^{\mathrm{th}}\approx 0.0094\times 888 \approx 8.35\,\mathrm{s}.
\]

Independent reconstruction from public averages (full error budget):

| Pair | \(\Delta\tau\) (s) | \(\mathrm{BR}_X\) |
|---|---|---|
| \(877.8\) vs \(888.1\) | \(10.30\) | \(0.01160\pm0.00225\) |
| PDG \(878.3\) vs \(888.1\) | \(9.80\) | \(0.01103\pm0.00227\) |
| \(878.4\) vs \(888.0\) | \(9.60\) | \(0.01081\pm0.00230\) |

The pipeline’s \(0.0107\pm0.0006\) matches \(\Delta\tau\approx 9.5\,\mathrm{s}\) on an \(888\,\mathrm{s}\) beam scale, with an uncertainty that looks like **bottle-only** propagation rather than the full \(\approx0.0023\) that includes the \(\pm2\,\mathrm{s}\) beam error.

**Scoring consequence:**  
- Against the pipeline’s own \(\pm0.0006\): \(|0.0107-0.0094|/0.0006=2.17\sigma\).  
- Against the printed \(1.3\sigma\): they are using a wider combined \(\delta\).  
- Against a full beam+bottle error \(\approx0.0023\): \(|0.0107-0.0094|/0.0023\approx0.6\sigma\), and the whole \(1\%\) island is inside one beam-error tick.

So the PASS is robust as “both numbers live near \(1\%\).” It is **not** a sharp confirmation of \(0.0094\) versus \(0.0107\).

---

## 5. Where \(0.0094\) comes from (not in the log)

The printed log does **not** derive \(\mathrm{BR}_X^{\mathrm{th}}=0.0094\) from \(\Delta_{\mathrm{TEP}}\), from \(r_M\), or from V_orb. The topological-anchor line correctly forbids fitting \(313.1\,\mathrm{MeV}\) to this BR.

Nearby numbers that must **not** be silently promoted:

| Expression | Value | Status |
|---|---|---|
| Pipeline target | \(0.0094\) | printed; derivation missing |
| \(4\alpha/3\) (external Schutza / Jordan-algebra note) | \(0.00973\) | **OUT** — not Superblock corpus |
| \(4\alpha/\pi\) | \(0.00929\) | numerology unless derived |
| \((\gamma_{\mathrm{hex}}-1)/\gamma_s=0.405/43.29\) | \(0.00936\) | coincidence until written as a module |
| \(1/n_{\mathrm{hier}}=1/45.8\) | \(0.0218\) | too large; binding, not a neutron BR |

Until a geometric formula for \(0.0094\) is written and accepted, treat the theory target as a **phenomenological 1% island**, not as a TEP theorem.

WilfiCon eTB/eWS and other external ontological files stay OUT. Do not fold \(4\alpha/3\) in through the back door.

---

## 6. Superblock reading (steelman, then constraints)

### Steelman

Bottle measures all ways a neutron can leave the Prime-domain trap. Proton-beam measures only \(n\to p\,e\,\bar\nu\). A \(\sim 1\%\) extra width that does not yield a proton reconciles the two averages.

In Superblock language that extra width is not a new particle species fitted to \(\Delta\tau\). It is **Planck–Kerr / Mirron tunneling** from the Prime \(udd\) cell into an off-Prime domain. The neutron already occupies mixed domains at the valence level (one Prime \(u\) + two near-Prime \(d\), \(\gamma_d=2.176\)). A small tunneling amplitude through the Mirron 2-surface (\(r_M=0.630\,\mathrm{fm}\)) is the same geometric object that, at galactic scales, is already IN as “SPARC emergent DM from off-Prime domains.” Laboratory branching is the short-distance end of that claim.

The printed falsifier is coherent with the 8-phase / octonion clockwork: magnetic-field orientation couples to phase overlap on \(\mathrm{Aut}(\mathbb{O})\cong G_2\). If the extra width is real and geometric, \(\mathrm{BR}_X\) should vary with \(\mathbf{B}\) orientation relative to the octonionic frame, not only with \(|\mathbf{B}|\).

That is a proper prediction. It is not yet a number.

### Constraints the steelman must survive

1. **Final-state exclusions.** Fornal–Grinstein dark decay (\(n\to\chi\gamma\), \(n\to\chi e^+e^-\), etc.) is tightly bounded. A hidden-domain branch that looks like a new on-shell particle plus a photon or \(e^+e^-\) is already in trouble. The Superblock channel has to stay *domain-internal* (no extra on-shell \(\gamma\) or \(e^+e^-\) at the 1% level).

2. **J-PARC electron beam.** A protonless *and* electronless hidden branch should make an electron-tagging beam look like a proton-tagging beam (long \(\tau\)). J-PARC instead sits on the bottle number. Escape routes: (a) J-PARC systematics (\(+4.0/-3.6\,\mathrm{s}\)) still cover a move toward \(888\,\mathrm{s}\); (b) the extra width is apparatus-dependent (the B-orientation falsifier). Route (b) then has to explain why *magnetic* bottles and *material* bottles are both short, and why J-PARC (no storage magnet) is also short.

3. **Three-way, not two-way.** Wietfeldt 2025: proton-beam vs magnetic bottle \(5.1\sigma\), proton-beam vs material bottle \(3.9\sigma\), material vs magnetic \(4.0\sigma\). A single 1% hidden branch does not automatically split material vs magnetic.

4. **Neutron-star / BBN / \(|V_{ud}|\).** A 1% invisible branch changes the effective weak lifetime that BBN and CKM fits want. Consistent assignment, if the branch is kept at all: \(\tau_{\mathrm{beam}}^{(p)}\) \(\approx\) inverse of SM \(\beta\) width; \(\tau_{\mathrm{bottle}}\) \(\approx\) inverse of \(\Gamma_\beta+\Gamma_X\); BBN / CKM use \(\Gamma_\beta\), not \(\Gamma_{\mathrm{tot}}\). That is the opposite of how most global fits ingest PDG’s UCN average. Flag it.

5. **Community systematics.** PSI 2025 / Courier 2026 lean against “new physics explains the whole gap.” The honest lead is: *the 1% island is the right size for a domain-tunnel reading; it is not a demonstrated channel.*

---

## 7. Falsifiable prediction — what would make it a real test

Printed: “Magnetic field orientation dependence (octonionic phase overlap).”

To leave HOLD and become a module, the engine needs a number:

\[
\mathrm{BR}_X(\hat{\mathbf{B}})
=\mathrm{BR}_0\bigl(1+\varepsilon\,\hat{\mathbf{B}}\cdot\mathbf{n}_{\mathbb{O}}\bigr)
\]

with a predicted \(\varepsilon\), a specified octonionic axis or a statement that only the modulation is predicted, a statement whether material bottles sit at \(\mathrm{BR}_0\) or at 0, and whether J-PARC’s guide-field counts as oriented.

---

## 8. Relation to the live corpus

Already IN and compatible in spirit: six domains, Mirron / Planck–Kerr, SPARC off-Prime DM, 8-phase clockwork.

Not automatically IN: a 1% free-neutron branch; laboratory Planck–Kerr tunneling as a decay operator; B-orientation coupling.

Keep OUT: Tav cylinder as the leak path; Fornal–Grinstein on-shell dark particle + \(\gamma\); external \(4\alpha/3\) as a Superblock theorem; any retuning of \(\Delta_{\mathrm{TEP}}\).

**Recommendation:** HOLD the hidden-domain neutron branch. Next action is a derived \(\mathrm{BR}_X^{\mathrm{th}}\) and a numeric \(\varepsilon\), not another PASS flag.

---

## 9. Session files

| Location | Path |
|---|---|
| This note (repo) | `Personal Files/2026-09-22_neutron_lifetime_hidden_domain_BR.md` |
| Local artifact | `/home/workdir/artifacts/2026-09-22_neutron_lifetime_hidden_domain_BR.md` |

Repo: `George-Jumble/TauSuperblock`, branch `main`.

---

## 10. Bottom line

**Printed status:** PASS at \(1.3\sigma\) (or \(2.2\sigma\) if only the quoted \(0.0006\) is used) between an observed extra branching \(0.0107\pm0.0006\) and a theory target \(0.0094\).

**What that means:** bottle-vs-proton-beam still differs by \(\sim 1\%\). Mapping that 1% onto off-Prime Mirron tunneling is a coherent Superblock *reading*. It is not yet a derived geometric result, and it is not yet ledger-IN.

**TEP floor:** untouched. \(313.1\,\mathrm{MeV}\) stays IN and independent.
