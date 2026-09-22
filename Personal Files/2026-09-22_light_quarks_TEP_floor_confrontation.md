# Superblock Empirical Tests — Light Quarks Confrontation

**Session date:** 2026-09-22  
**Author context:** Superblock / Mirron corpus only (Tau / Tav layer OUT of live analyses)  
**Engine label in pasted log:** TAV ENGINE / SUPERBLOCK EMPIRICAL TESTS PIPELINE v3  
**Theory anchor in log:** \(m_0 = \Delta_{\mathrm{TEP}} = 313.1\,\mathrm{MeV}\)  
**Corpus status of this number:** IN — TEP floor \(313.1\,\mathrm{MeV}\) on \((\mathrm{domain}_i,\mathrm{phase}_k)\); Yang–Mills mass gap via Planckian mirrors; \(r_M=\lambda_{313}\)

This note records the pasted pipeline output, restates every symbol, separates *current* (Lagrangian) quark masses from the *constituent / TEP* floor, and scores what the PASS actually measures.

---

## 1. Raw pipeline output (as received)

```
[TAV ENGINE] Superblock Empirical Tests — Light Quarks Confrontation
[TAV ENGINE] Theory anchor m₀ = 313.1 MeV
[TAV ENGINE] Output directory: /home/wyle-e/Storage7TB/Research/scripts/research_tool/menus/empirical_tests/artifacts
========================================================================
SUPERBLOCK EMPIRICAL TESTS PIPELINE v3
Theory: Prime Past Harmonic + Tav-Superblock Cosmology (June 2026)
========================================================================
[Loading] pdg_light_quarks — PDG light quark masses & hadron data (best via `particle` package)
  Loaded 4 points.
[Loading] lattice_qcd — FLAG / lattice quark mass averages
  Loaded 2 points.
--- Light Quarks & Prime Past Harmonic ---
Status: PASS
  Constituent mass floor (u/d): theory=313.1, exp=313.0 ± 8.0, tension=0.01σ
  plot: .../artifacts/light_quarks_test.png
JSON report saved: .../artifacts/superblock_test_report.json
[TOPOLOGICAL ANCHOR] 313.1 MeV mass-gap signal is independent of empirical confrontation parameters.
```

### Branding note (corpus hygiene)

The banner still says “TAV ENGINE” and “Prime Past Harmonic + Tav-Superblock Cosmology (June 2026)”.  
Live ledger (`CORPUS.md`, 2026-09-22): **Tau Universe / Tav Topology is OUT**. Live language is Superblock / Mirron. The numeric test itself (TEP floor vs a constituent-scale estimate) does not depend on the retired compact-\(S^1_\tau\) layer. The topological-anchor line in the log is the correct corpus statement.

---

## 2. Variable and function key

| Symbol | Meaning | Value / definition used here |
|---|---|---|
| \(\Delta_{\mathrm{TEP}}\) or \(m_0\) | Topological energy / mass-gap floor. Geometric, not a fit parameter. Assigned to each \((\mathrm{domain}_i,\mathrm{phase}_k)\) cell. | \(313.1\,\mathrm{MeV}\) |
| \(m_q^{\mathrm{curr}}(\mu)\) | *Current* (Lagrangian) quark mass in the \(\overline{\mathrm{MS}}\) scheme at scale \(\mu\). PDG / FLAG. | \(\mu=2\,\mathrm{GeV}\) for \(u,d,s\) |
| \(m_u, m_d, m_s\) | Current light-quark masses | PDG 2025/2026: \(m_u=2.16\pm0.07\,\mathrm{MeV}\), \(m_d=4.70\pm0.07\,\mathrm{MeV}\), \(m_{ud}=3.49\pm0.07\,\mathrm{MeV}\), \(m_s=93.5\pm0.8\,\mathrm{MeV}\) |
| \(M_q^{\mathrm{const}}\) | *Constituent* (effective, infrared) quark mass. Phenomenological; includes dynamical chiral-symmetry breaking. Not a Standard-Model parameter. | Pipeline “exp”: \(313.0\pm8.0\,\mathrm{MeV}\) for \(u/d\) |
| \(M_N, m_p, m_n\) | Nucleon / proton / neutron rest masses | \(m_p=938.272\,\mathrm{MeV}\), \(m_n=939.565\,\mathrm{MeV}\) |
| \(\hbar c\) | Reduced-Planck-constant × speed of light, MeV·fm conversion | \(197.3269718\,\mathrm{MeV\cdot fm}\) |
| \(\lambda_{313}=r_M\) | Compton length of the TEP floor; locked Mirron / Planck–Kerr 2-surface radius | \(r_M=\hbar c/\Delta_{\mathrm{TEP}}=0.630236\,\mathrm{fm}\) |
| \(\ell_P\) | Planck length (seed, **not** clock radius) | \(1.616255\times10^{-35}\,\mathrm{m}\) |
| \(\beta_i, \gamma_i\) | Domain orbital speed and Lorentz factor (V_orb Scheme A) | Prime \(u\): \(\beta_0=0\), \(\gamma_0=1\). See table below. |
| \(V_{\mathrm{orb}}\) | Six-domain velocity assignment. Scheme A: PDG mass increments on \(m_u\); E6 \(\subset\) E8 weights supply axes. | `sb_engine/constants.py` |
| \(\omega_1,\omega_5,\omega_2,\omega_4,\omega_6,\omega_3\) | E6 fundamental-weight axis map onto \(u,d,s,c,b,t\) | corpus IN |
| \(n_{\mathrm{hier}}\) | Superblock hierarchical binding index | \(45.8\) in engine constants; **not** \(\log_7(R_\tau/r_M)\) |
| \(\sigma\) | Tension in units of the quoted experimental uncertainty | \(\sigma=\lvert m_{\mathrm{th}}-m_{\mathrm{exp}}\rvert/\delta m_{\mathrm{exp}}\) |
| PASS | Pipeline flag when \(\sigma < 3\) on the chosen comparator | here \(\sigma=0.0125\) |

### Functions used

\[
r_M \;=\; \frac{\hbar c}{\Delta_{\mathrm{TEP}}}
\]

\[
\gamma(\beta) \;=\; \frac{1}{\sqrt{1-\beta^2}}, \qquad 0\le\beta<1
\]

\[
\sigma \;=\; \frac{\lvert \Delta_{\mathrm{TEP}} - M_{u/d}^{\mathrm{const}}\rvert}{\delta M_{u/d}^{\mathrm{const}}}
\]

\[
\lambda \;=\; \frac{\hbar c}{E}
\quad\text{(Compton length of energy }E\text{)}
\]

No other fitted function enters the TEP floor. That is the content of the pipeline’s topological-anchor line.

---

## 3. What was loaded vs what was compared

The loaders named in the log are:

1. `pdg_light_quarks` — 4 points (likely \(m_u, m_d, m_s\) plus one hadron-scale stand-in, via the `particle` package).
2. `lattice_qcd` — 2 points (FLAG averages; almost certainly \(m_{ud}\) and \(m_s\) in \(\overline{\mathrm{MS}}\) at \(2\,\mathrm{GeV}\)).

Those loaders supply **current** masses. The PASS line does **not** compare \(\Delta_{\mathrm{TEP}}\) to \(m_u\simeq 2.2\,\mathrm{MeV}\). It compares \(\Delta_{\mathrm{TEP}}\) to a **constituent-floor estimator** written as \(313.0\pm8.0\,\mathrm{MeV}\).

That distinction is mandatory. PDG itself states that constituent masses “only make sense in the limited context of a particular quark model, and cannot be related to the quark mass parameters \(m_q\) of the Standard Model.” FLAG averages are current masses.

### Current-mass ledger (not the PASS comparator)

| Quantity | PDG 2025 tables / 2026 review | FLAG 2024 \(N_f=2+1+1\) | FLAG 2024 \(N_f=2+1\) |
|---|---|---|---|
| \(m_u(2\,\mathrm{GeV})\) | \(2.16\pm0.07\,\mathrm{MeV}\) | \(2.14(8)\,\mathrm{MeV}\) | \(2.27(9)\,\mathrm{MeV}\) |
| \(m_d(2\,\mathrm{GeV})\) | \(4.70\pm0.07\,\mathrm{MeV}\) | \(4.70(5)\,\mathrm{MeV}\) | \(4.67(9)\,\mathrm{MeV}\) |
| \(m_{ud}=(m_u+m_d)/2\) | \(3.49\pm0.07\,\mathrm{MeV}\) | \(3.427(51)\,\mathrm{MeV}\) | \(3.387(39)\,\mathrm{MeV}\) |
| \(m_s(2\,\mathrm{GeV})\) | \(93.5\pm0.8\,\mathrm{MeV}\) | \(93.46(58)\,\mathrm{MeV}\) | \(92.4(1.0)\,\mathrm{MeV}\) |
| \(m_s/m_{ud}\) | \(27.33^{+0.18}_{-0.14}\) | \(27.227(81)\) | \(27.42(12)\) |

A confrontation of \(\Delta_{\mathrm{TEP}}=313.1\,\mathrm{MeV}\) against any of these current-mass numbers would be a category error and would fail at hundreds of \(\sigma\). The pipeline did not do that.

### Constituent-scale ledger (the PASS comparator)

Typical infrared values in the literature:

- Quark-model / NJL ballpark: \(M_{u,d}\sim 300\text{–}350\,\mathrm{MeV}\), \(M_s\sim 450\,\mathrm{MeV}\).
- Nucleon one-third estimator: \(\bar M_N/3 = (m_p+m_n)/6 = 312.97\,\mathrm{MeV}\).
- Pipeline “exp”: \(313.0\pm8.0\,\mathrm{MeV}\).

The \(\pm 8\,\mathrm{MeV}\) envelope is a *model-dispersion* band, not a PDG uncertainty. It is the right order of magnitude for “how well anyone knows a constituent \(u/d\) mass,” and it is the only reason the tension can print as \(0.01\sigma\).

---

## 4. Arithmetic of the PASS

\[
\sigma
= \frac{\lvert 313.1 - 313.0\rvert}{8.0}
= 0.0125
\;\approx\;
0.01
\]

as printed.

Naive three-floor sums (diagnostic only; not a nucleon mass formula):

\[
3\Delta_{\mathrm{TEP}} = 939.3\,\mathrm{MeV},
\qquad
3\Delta_{\mathrm{TEP}}-m_p = +1.028\,\mathrm{MeV},
\qquad
3\Delta_{\mathrm{TEP}}-m_n = -0.265\,\mathrm{MeV}.
\]

The nucleon one-third estimator \((m_p+m_n)/6=312.97\,\mathrm{MeV}\) sits \(0.13\,\mathrm{MeV}\) under \(\Delta_{\mathrm{TEP}}\), inside the same \(\pm8\,\mathrm{MeV}\) band.

Locked Mirron radius:

\[
r_M
= \frac{197.3269718\,\mathrm{MeV\cdot fm}}{313.1\,\mathrm{MeV}}
= 0.630236\,\mathrm{fm}
= 6.30236\times 10^{-16}\,\mathrm{m}.
\]

Corpus lock: \(r_M=\lambda_{313}\approx 0.630\,\mathrm{fm}\). \(\ell_P\) remains seed, not clock radius.

Explicit (current) content of the proton:

\[
2m_u+m_d \approx 9.02\,\mathrm{MeV} \approx 0.96\%\text{ of }m_p.
\]

The remaining \(\sim 99\%\) is dynamical. In Superblock language that remainder is the TEP / Mirron / Planck–Kerr dressing of the Prime and near-Prime domains, not a fitted condensate parameter.

---

## 5. V_orb Scheme A (why light quarks sit on the floor)

Prime \(= u\) at rest. Heavier flavours are the same TEP floor seen from boosted domains. Engine table (`sb_engine/constants.py`):

| domain \(i\) | flavour | role | \(\beta_i\) | \(\gamma_i\) | E6 weight |
|---|---|---|---|---|---|
| 0 | \(u\) | Prime | \(0\) | \(1\) | \(\omega_1\) |
| 1 | \(d\) | near | \(0.8881\) | \(2.176\) | \(\omega_5\) |
| 2 | \(s\) | mid | \(0.999733\) | \(43.29\) | \(\omega_2\) |
| 3 | \(c\) | fast | \(1-1.44\times10^{-6}\) | \(589.4\) | \(\omega_4\) |
| 4 | \(b\) | fast | \(1-1.333\times10^{-7}\) | \(1936.6\) | \(\omega_6\) |
| 5 | \(t\) | ultrarel | \(1-7.83\times10^{-11}\) | \(7.989\times10^{4}\) | \(\omega_3\) |

Scheme A is phenomenological stand-in speeds from PDG mass increments on \(m_u\); E6 \(\subset\) E8 supplies axes and angles, not the speed eigenvalues. A linear E8 root projection cannot produce this \(\gamma\) hierarchy (radii only in \(\{0,1,\sqrt{2}\}\)).

The light-quark test is therefore a test of the **Prime rest-frame floor**, not of the boost ladder. The ladder is a different confrontation (flavour spectrum / increments) and was not scored in this log.

---

## 6. How to read the PASS (multiple angles)

### What it *does* show

1. The infrared \(u/d\) constituent scale that quark models and nucleon one-third estimators have used for decades sits on the same \(310\pm10\,\mathrm{MeV}\) island as the geometric TEP floor.
2. The engine did not retune \(\Delta_{\mathrm{TEP}}\) to chase the comparator. The topological-anchor line is consistent with the corpus: the \(313.1\,\mathrm{MeV}\) number is independent of this confrontation’s inputs.
3. \(r_M=\hbar c/\Delta_{\mathrm{TEP}}\) remains locked at \(0.630\,\mathrm{fm}\). Any later hadron-size or Casimir-shape test that uses that radius is using the same object.

### What it does *not* show

1. It is **not** a precision confirmation. \(\delta M=8\,\mathrm{MeV}\) is \(\sim 2.6\%\) relative. A theory value anywhere in \(\approx 289\text{–}337\,\mathrm{MeV}\) would also PASS at \(<3\sigma\). The printed \(0.01\sigma\) is an artifact of placing the comparator mean at \(313.0\).
2. It does **not** confirm current-quark PDG/FLAG masses. Those are a different object.
3. It does **not** by itself solve the Yang–Mills mass-gap problem. Corpus IN still lists “Yang–Mills mass gap via Planckian mirrors” as the *mechanism claim*; this test only checks that the claimed gap scale is the same order as the constituent floor.
4. It does **not** rehabilitate the retired Tav / \(7\,h^{-1}\,\mathrm{Mpc}\) cylinder. The June-2026 banner in the log is stale.

### Edge cases

- If the pipeline’s “exp \(=313.0\pm8.0\)” was itself computed as \((m_p+m_n)/6\) rounded, the PASS is nearly tautological: one-third of the nucleon mass is being compared to a number chosen to sit next to one-third of the nucleon mass. That is consistency, not an independent measurement.
- If “exp” instead came from an NJL / QCD-sum-rule / quark-model average with a genuine extra-nucleon input, the test has more content — but the \(\pm8\,\mathrm{MeV}\) still dominates.
- Strange-quark constituent scale (\(\sim 450\,\mathrm{MeV}\) in many models) is **not** scored here. Under Scheme A the \(s\) domain is mid-boost (\(\gamma_s=43.29\)); a naive \(\gamma_s\Delta_{\mathrm{TEP}}\) is *not* \(M_s^{\mathrm{const}}\) and must not be used that way. Flavour increments live on the PDG current-mass ladder plus binding, not on raw \(\gamma_i\Delta_{\mathrm{TEP}}\).
- Lattice nucleon-mass calculations in physical-point QCD already *reproduce* \(m_p\) from current masses plus the gauge dynamics. Superblock’s claim is a geometric reading of that same infrared scale, not a competitor to the lattice spectrum at the few-MeV level.

---

## 7. Implications for the live corpus

Keep as IN, unchanged:

- TEP floor \(313.1\,\mathrm{MeV}\)
- \(r_M=\lambda_{313}\approx0.630\,\mathrm{fm}\)
- Prime \(=u\) at rest
- Yang–Mills mass gap via Planckian mirrors
- V_orb Scheme A as the flavour-boost table

Do not promote:

- “\(0.01\sigma\) light-quark confirmation” as a precision result
- Any folding of FLAG current masses into \(\Delta_{\mathrm{TEP}}\)
- Revival of Tav-layer language in the empirical-test banner

Recommended engine hygiene (not done in this session):

1. Rename the live banner from `TAV ENGINE` / “Tav-Superblock Cosmology (June 2026)” to `SB ENGINE` / “Superblock / Mirron corpus (2026-09-22)”.
2. In the JSON report, store two blocks: `current_masses` (PDG+FLAG, no PASS against \(313.1\)) and `constituent_floor` (this test), with an explicit provenance field for the \(313.0\pm8.0\) estimator.
3. Next independent confrontation in this sector: strange and charm *increments* against Scheme A, and the nucleon mass with hierarchical binding \(n_{\mathrm{hier}}\) written out — not another one-third estimator.

---

## 8. Session files

| Location | Path |
|---|---|
| This note (repo Personal Files) | `Personal Files/2026-09-22_light_quarks_TEP_floor_confrontation.md` |
| Local artifact copy | `/home/workdir/artifacts/2026-09-22_light_quarks_TEP_floor_confrontation.md` |
| Pipeline plot (user machine, not in this sandbox) | `/home/wyle-e/Storage7TB/Research/scripts/research_tool/menus/empirical_tests/artifacts/light_quarks_test.png` |
| Pipeline JSON (user machine) | `.../artifacts/superblock_test_report.json` |

Repo: `George-Jumble/TauSuperblock`, branch `main`.

---

## 9. Bottom line

**Status recorded:** PASS at \(0.01\sigma\) against a constituent \(u/d\) floor of \(313.0\pm8.0\,\mathrm{MeV}\).

**Corpus reading:** the geometric TEP / Mirron gap \(\Delta_{\mathrm{TEP}}=313.1\,\mathrm{MeV}\) sits on the historical constituent-mass island. That is the expected consistency check for a mass-gap floor that is *defined* to be the infrared \(u/d\) scale. It is not a high-precision empirical discovery, and it does not touch current-quark PDG/FLAG values.

**No corpus change.** TEP floor stays IN. Tav layer stays OUT.
