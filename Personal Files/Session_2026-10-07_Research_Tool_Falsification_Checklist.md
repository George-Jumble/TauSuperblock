# Session 2026-10-07: Falsifiable tests the research tool can actually run

**Date:** 2026-10-07
**Query:** What falsifiable tests can be performed with the research tool to verify the current Superblock corpus? List and explain each one. Appendix: loose ends that need theoretical or mathematical work.
**Live engine audited:** `George-Jumble/TauSuperblock`, default branch `main`, tree SHA `6b6b07b3b0ffabf73f71ab267e7bf2ce525e59f9` (repo updated 2026-10-03). Entry point `research_tool.py`.
**Corpus ledger read:** `CORPUS.md` dated 2026-09-26 (IN / OUT / HOLD / OPEN).
**Governing frame:** live Superblock as of 2026-10-02. Mirron, not soliton. Tau circle, KK fifth, zero-parameter claim, and the 313 MeV glueball pole stay out.
**Status of this note:** inventory of what the tool can execute, plus the run printed on this date. Not a discovery claim. Not a new derivation.

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-10-07_Research_Tool_Falsification_Checklist.md`
Mirrors: `Personal Files/`, `Personal_Files/`, `Tau-Superblock_Universe/Personal_Files/`.

---

## 0. What “the research tool” is, and what it is not

The live research tool is the Superblock / Mirron engine. Eight subcommands exist:

```text
python research_tool.py geometry
python research_tool.py corpus
python research_tool.py bounce
python research_tool.py neutron
python research_tool.py sparc
python research_tool.py desi
python research_tool.py cms
python research_tool.py casimir
```

`kernels/g_avg.py` is in the tree and is not wired to the CLI.

The older repository `George-Jumble/tav-resonace-research-tool` looks for resonances at the Tau scale (FRB paths, a SPARC-ratio module, a harmonic ladder). That target is OUT of the live corpus (`τ ≈ 7 h⁻¹ Mpc` retired 2026-09-14). Running it does not verify the current frame. It is listed in section 4 only so it is not mistaken for an unfinished live test.

Prior ATLAS Open Data 2lep (2026-07-27) and CMS Run2012BC DoubleMuParked (2026-08-21) periodograms are not this CLI. The current `cms` command does not open those files.

---

## 1. Complete symbol key used below

| Symbol | Meaning in this note |
|---|---|
| \(\Delta_{\mathrm{Tav}}=m_0=313.1\,\mathrm{MeV}\) | Inserted nucleon-third floor. Printed protocol value \(M_n/3\). Not a derived pole. |
| \(\hbar c\) | Conversion constant. Engine value \(197.3269718\,\mathrm{MeV\,fm}\). |
| \(r_M=\lambda_{313}\) | Mirron Compton length, Compton dual of the floor. |
| \(\ell_P\) | Planck length used as seed, not as clock radius. Engine value \(1.616255\times 10^{-35}\,\mathrm{m}\). |
| \(\beta_i\) | Speed parameter of domain \(i\) in \(V_{\mathrm{orb}}\) Scheme A. Input. |
| \(\gamma_i\) | Lorentz factor stored for domain \(i\). Input, cross-checked against \(\beta_i\). |
| \(\gamma_{\mathrm{hex}}\) | Stored hex factor \(1.405\). Not the harmonic mean. |
| \(V_{\mathrm{orb}}\) | Six-row table. Prime = up at rest. Flavours \(u,d,s,c,b,t\) are labels. |
| \(\Phi_7\) | Phase-7 scrape. Not a CMS bin in the engine. |
| \(\Phi_8\) | Phase-8 reset. Engine note: not a CMS bin. |
| \(N_7=7\) | Active clockwork slots in the CMS toy. |
| \(n\) | Toy event count in `cms` (default 4000). |
| \(A\) | Planted cosine amplitude in `cms` (default 0.18). |
| \(\chi^2_{\mathrm{clock}}\) | Chi-squared of toy counts against the planted weights. |
| \(\chi^2_{\mathrm{unif}}\) | Chi-squared of toy counts against a flat \(1/7\) null. |
| \(d\) | Plate separation in the Casimir toy. |
| \(F/A\) | Force per area. Toy Lifshitz magnitude \(\mathrm{PREF}/d^4\). |
| \(\mathrm{PREF}\) | Perfect-conductor prefactor \(1.299\times 10^{-27}\,\mathrm{N\,m^2}\). |
| \(a_{\mathrm{rip}}\) | Planted log-7 ripple amplitude in `casimir` (default 0.04). |
| \(r_d\) | Comoving sound horizon. |
| \(r_{d,\mathrm{obs}}\) | Catalogue value stored in the engine, \(147.09\,\mathrm{Mpc}\), error \(0.26\,\mathrm{Mpc}\). |
| \(\Delta N_{\mathrm{plasma}}\) | Stored plasma factor \(10.74\). |
| \(\gamma\) | DESI divisor. Default calibration returns \(10.74\). |
| \(n_{\mathrm{hier}}\) | Number \(45.8\) still stored in `constants.py`. Corpus text says it is hierarchical binding, not \(\log_7(\tau/\lambda)\). The number is the retired stretch. |
| \(\mathrm{BR}_0\) | HOLD neutron branch \(1/(\gamma_d\gamma_s)\). Not corpus IN. |
| \(\varepsilon\) | HOLD clockwork slot factor in \(\{1/7,2/7\}\). |
| \(s\) | HOLD polarization switch. \(s=0\) isotropic; \(s=+1\) magnetic-bottle lock. |
| \(\tau_\beta\) | Stored beta-decay lifetime \(888.1\pm 2.0\,\mathrm{s}\). |
| \(\alpha\) | Anomalous dimension \(1-\log_7 6\). Not an engine input. |
| \(E_\times\) | Domain-cross work. Not an engine output. |
| \(\theta_{ab}\) | Domain-pair angle. Adjacent octahedron hop \(\pi/2\); antipodal \(\pi\). |
| \(G_{\mathrm{avg}}/G_N\) | Kernel ratio in `kernels/g_avg.py`. Not a CLI command. |

---

## 2. Run printed on 2026-10-07

Commands were executed from a fresh clone. Payloads below are the tool’s own JSON, trimmed only where a command returns no science number.

### 2.1 `geometry`

\[
r_M=\frac{\hbar c}{\Delta_{\mathrm{Tav}}}=\frac{197.3269718\,\mathrm{MeV\,fm}}{313.1\,\mathrm{MeV}}=0.630236\,\mathrm{fm}.
\]

**Key.** \(\hbar c\): engine conversion. \(\Delta_{\mathrm{Tav}}\): inserted floor. \(r_M\): printed Compton dual.

\[
\log_7(r_M/\ell_P)=23.1819.
\]

**Key.** \(\ell_P\): seed length. This log is a stretch count between seed and floor. It is not \(n_{\mathrm{hier}}\) and not a Tau-circle index.

Stored versus recomputed Lorentz factors:

| Domain | Flavour | \(\beta\) | Stored \(\gamma\) | \(\gamma(\beta)=1/\sqrt{1-\beta^2}\) |
|---|---|---:|---:|---:|
| 0 | \(u\) | 0 | 1 | 1 |
| 1 | \(d\) | 0.8881 | 2.176 | 2.1756 |
| 2 | \(s\) | 0.999733 | 43.29 | 43.277 |
| 3 | \(c\) | \(1-1.44\times 10^{-6}\) | 589.4 | 589.26 |
| 4 | \(b\) | \(1-1.333\times 10^{-7}\) | 1936.6 | 1936.73 |
| 5 | \(t\) | \(1-7.83\times 10^{-11}\) | \(7.989\times 10^4\) | \(7.991\times 10^4\) |

Harmonic mean of the six stored \(\gamma\) values: \(4.0407\). Stored \(\gamma_{\mathrm{hex}}=1.405\). They are not the same object. The command does not say which one a later formula is allowed to use.

### 2.2 `corpus`

Prints the 2026-09-26 ledger. Not a measurement. Confirms engines may see only IN entries. Neutron branch and Dirac freeze remain HOLD. Unique construction of \(r_M\) remains OPEN.

### 2.3 `bounce`

Returns the canon string and \(n=64\) frames. The frames are a hand-drawn \(\sin\) profile of conformal factor and refresh. No dataset. No residual.

### 2.4 `neutron` (HOLD)

\[
\mathrm{BR}_0=\frac{1}{\gamma_d\gamma_s}=\frac{1}{2.176\times 43.29}=0.0106158.
\]

**Key.** \(\gamma_d,\gamma_s\): stored \(V_{\mathrm{orb}}\) factors for the down and strange rows. \(\mathrm{BR}_0\): HOLD branch, not an IN claim.

\[
\tau(s)=\tau_\beta\bigl(1-\mathrm{BR}_0(1+\varepsilon s)\bigr).
\]

**Key.** \(\tau_\beta=888.1\,\mathrm{s}\). \(\varepsilon\in\{1/7,2/7\}\). \(s=0\) or \(s=+1\).

Printed values: isotropic \(878.67\,\mathrm{s}\); magnetic \(\varepsilon=1/7\) gives \(877.33\,\mathrm{s}\); magnetic \(\varepsilon=2/7\) gives \(875.98\,\mathrm{s}\). Polarization shifts \(1.347\,\mathrm{s}\) and \(2.694\,\mathrm{s}\). The module’s own sentence: appearance methods must return \(\sim 888\,\mathrm{s}\) if \(s=0\); \(877.2\,\mathrm{s}\) is a live fail of that appearance claim. It does not claim that \(877.2\,\mathrm{s}\) confirms \(s=+1\).

### 2.5 `sparc`

Toy galaxy labelled NGC3198. \(n=28\) radii. \(\beta^2=0.78872\) (down-row). Phase \(0.4\). \(\chi^2=26.56\), reduced \(\chi^2=1.021\). The “observed” curve is an NFW halo generated inside the same function, then compared with `emergent_dm`. No SPARC Rotmod file is read.

### 2.6 `desi`

Default and `--gamma 10.74` both return:

\[
r_d=\frac{\Delta N_{\mathrm{plasma}}\,r_{d,\mathrm{obs}}}{\gamma}=\frac{10.74\times 147.09}{10.74}=147.09\,\mathrm{Mpc},
\]

residual \(0\), residual in units of the stored error \(0\). **Key.** \(\Delta N_{\mathrm{plasma}}\): stored \(10.74\). \(\gamma\): divisor, calibrated to the same \(10.74\). \(r_{d,\mathrm{obs}}\): stored catalogue horizon. The zero is an identity.

### 2.7 `cms`

\(n=4000\), planted \(A=0.18\), seed \(7\). Counts \((705,653,550,464,443,573,612)\). \(\chi^2_{\mathrm{clock}}=6.97\). \(\chi^2_{\mathrm{unif}}=95.62\). Weights are \(1+A\cos(2\pi k/7)\). The command draws from those weights and then scores them. No CMS file is opened.

### 2.8 `casimir`

Planted ripple amplitude \(0.04\), phase \(0\). Discrete-step count \(4\). Deviation of log-log slope from \(-4\): \(0.00382\). Note in the payload: shape battery only; not \(\Delta E=E_{\mathrm{obs}}-E_{\mathrm{Lifshitz}}\) (dropped 2026-09-15). No dielectric file is read.

### 2.9 Kernel not on the CLI

\[
\frac{G_{\mathrm{avg}}}{G_N}=\frac{1}{6}\sum_{i=0}^{5}\frac{1}{\gamma_i^2}=0.20196.
\]

**Key.** \(\gamma_i\): the six stored factors. \(G_N\): Newton constant, appearing only as the unit of the ratio. The file does not compare this number to a lab or galactic datum.

---

## 3. Tests the tool can perform

Each item says what to run, what claim it can touch, what a fail looks like, and what today’s run already showed.

### T1. Geometry bookkeeping — runnable now, and it is a real internal check

**Command:** `python research_tool.py geometry`

**Claim touched.** The floor and its Compton dual are the same printed number, and Scheme A speeds match Scheme A gammas.

\[
r_M=\frac{\hbar c}{\Delta_{\mathrm{Tav}}},\qquad \gamma(\beta)=\frac{1}{\sqrt{1-\beta^2}}.
\]

**Key.** As in section 1. Fail condition: printed \(r_M\) disagrees with \(\hbar c/313.1\,\mathrm{MeV}\), or any row has \(|\gamma_{\mathrm{stored}}-\gamma(\beta)|\) larger than the rounding already visible in the table.

**What it cannot do.** It cannot show that \(313.1\,\mathrm{MeV}\) is derived. Corpus OPEN already says Program L failed uniqueness.

**Today.** Dual is consistent at \(0.630236\,\mathrm{fm}\). Row mismatches are at the last stored digit except the top row (\(79890\) stored, \(79911\) recomputed). That is a hygiene fail of the table, not a fail of the floor.

### T2. Corpus gate — runnable now, not a measurement

**Command:** `python research_tool.py corpus`

**Claim touched.** Engines are not allowed to reload OUT objects (Tau circle, 7 Mpc aside, Casimir bound-energy residual, 313 MeV glueball pole, Vălean weight-6 as a TEP generator).

**Fail.** A later engine import or a printed IN line that names an OUT object.

**Today.** Ledger matches the 2026-10-02 retirement list on the circle, the pole, and the bound-energy residual. It still lists “CMS 7-fold clockwork occupancy” and “SPARC emergent DM” as IN, which the corresponding commands do not measure (T5, T6).

### T3. Bounce canon lock — runnable now, not a falsification of the bounce

**Command:** `python research_tool.py bounce`

**Claim touched.** The bounce remains conformal aeon crossover plus Mirron / Planck–Kerr refresh, and is not a \(\Phi_7\) pin-drop, not a Coleman instanton, not a biquaternion \(M+\) rewrite.

**Fail.** Canon string changes, or a frame is labelled as one of the excluded rewrites.

**Today.** Canon string is the locked one. The 64 frames are a drawing. Passing this command does not support residual-\(L\) gravity or the black–white sign flip.

### T4. Neutron HOLD lifetime — the only command that names an external number

**Command:** `python research_tool.py neutron`

**Claim touched.** HOLD only. If a hidden-domain branch \(\mathrm{BR}_0=1/(\gamma_d\gamma_s)\) is real and \(s=0\) in appearance experiments, the appearance lifetime must sit on \(\tau_\beta\), not on the beam/bottle value the module calls \(877.2\,\mathrm{s}\).

**Fail already printed by the module.** \(877.2\,\mathrm{s}\) fails the \(s=0\) appearance sentence. A further fail of the HOLD formula itself would be a polarized shift outside \(\{1.35,2.69\}\,\mathrm{s}\) once a real bottle-minus-beam likelihood is attached. The CLI does not attach that likelihood.

**Today.** Numbers in section 2.4. Do not promote \(877.33\) versus \(877.2\) to a confirmation. The module does not.

### T5. CMS clockwork occupancy — command exists; the falsifying test does not

**Command as shipped:** `python research_tool.py cms`

**What the shipped command does.** Recovers a cosine it planted. \(\chi^2_{\mathrm{unif}}\gg\chi^2_{\mathrm{clock}}\) is guaranteed for \(A=0.18\) and \(n=4000\). This cannot verify the corpus line “CMS 7-fold clockwork occupancy.”

**Falsifying protocol the tool does not yet run.**

1. Read a public dimuon file (CMS Open Data or ATLAS Open Data), not a multinomial draw.
2. Choose one variable \(x\) that can carry a scale (transverse momentum or a mass-like observable). Multiplicity under a dimuon trigger is already dead: the 2026-08-21 trigger-aware null accounts for residue-2.
3. Fold \(u=x/M_0\) and scan \(M_0\) across a window around \(313.1\,\mathrm{MeV}\) and across sidebands. A hit that does not track \(M_0\) is not an observation of the floor.
4. Null must include the trigger. Score with a Cowan construction, not the capped engine score of the July–August notes.
5. Pre-register whether the occupancy is 7 slots with \(\Phi_8\) excluded, or 8. The engine currently assumes 7. That assumption is not a theorem (appendix A8).

**Fail.** No excess at periods \(1/7,2/7,\ldots\) after the trigger-aware null, or an excess that is stable when \(M_0\) is moved off \(313.1\,\mathrm{MeV}\).

### T6. SPARC emergent shadow — command exists; the falsifying test does not

**Command as shipped:** `python research_tool.py sparc`

**What the shipped command does.** Builds a synthetic NGC3198 from a Miyamoto disk plus gas plus an NFW halo, then fits a three-parameter emergent curve. Reduced \(\chi^2\approx 1.02\) is a self-fit.

**Falsifying protocol the tool does not yet run.**

1. Read SPARC Rotmod files. Freeze \(\beta^2\) and phase before looking at residuals. Do not retune per galaxy and then quote the retuned \(\chi^2\) as support.
2. Compare against NFW, Einasto, and Burkert on the same points, with the same baryonic \(\Upsilon\).
3. The live shadow ratio \(5.401514\) is ansatz A (equal proper density on six copies). It is not the \(V_{\mathrm{orb}}\) sum and not the `g_avg` kernel. A SPARC win for a softened halo does not verify ansatz A.

**Fail.** Emergent curve loses to the baseline on a pre-registered sample after baryonic nuisance is shared.

### T7. DESI sound horizon — command exists; residual is an identity

**Command:** `python research_tool.py desi`

**What it does.** Returns zero because \(\gamma\) is set equal to \(\Delta N_{\mathrm{plasma}}\).

\[
r_d-r_{d,\mathrm{obs}}=0\quad\text{whenever}\quad\gamma=\Delta N_{\mathrm{plasma}}.
\]

**Key.** Both factors are stored constants. Neither is computed from six domains or from \(r_M\).

**Falsifying protocol the tool does not yet run.** Predict \(r_d\) from IN objects without dividing by a factor defined to cancel \(r_{d,\mathrm{obs}}\). Until that formula exists, this command cannot verify anything. A non-zero residual appears only if the user passes a \(\gamma\) other than \(10.74\), which tests the arithmetic, not DESI.

### T8. Casimir shape battery — command exists; bound-energy search is correctly absent

**Command as shipped:** `python research_tool.py casimir`

**What the shipped command does.** Multiplies a perfect-conductor \(1/d^4\) curve by \(1+a_{\mathrm{rip}}\sin(2\pi\log_7(d/r_M))\) and counts outliers. Slope near \(-4\) is the Lifshitz input.

**Falsifying protocol the tool does not yet run.**

1. Read the public dielectric files (Ma et al. 2026; dielPT series). Do not plant the log-7 ripple.
2. Shape only: discrete thresholds, hysteresis asymmetry, hierarchical changepoints, power at \(1/7\) in \(\log(d/r_M)\). Bound-energy residual \(\Delta E\) stays dropped (2026-09-15, OUT).
3. Null is a smooth Lifshitz curve with the material’s own dielectric function and no \(1/7\) term. A detection that dies when the log base is changed from 7 is the actual test.

**Fail.** No \(1/7\) excess against that null, on more than one material, after look-elsewhere correction across the log base.

### T9. Kernel ratio — file exists, command does not

**File:** `kernels/g_avg.py`

**Printed here.** \(G_{\mathrm{avg}}/G_N=0.202\). This is not effective \(G\) of the dominant glob, and it is not the ansatz-A shadow ratio \(5.401514\). Wiring it to a CLI without a derivation that says which ratio is the observable would add a third, conflicting number. Do not treat T9 as a ready test.

---

## 4. Excluded on purpose

- `tav-resonace-research-tool` FRB path, harmonic ladder, and Tau-scale resonance scan. Target is the retired circle.
- Casimir \(\Delta E\) residual. Dropped 2026-09-15.
- Sterile branching-ratio TeX. Attachments are empty (1 byte). No engine.
- Vălean alternating-Euler action. Corpus: external literature, no energy map. Not an engine.
- Glueball pole at \(313\,\mathrm{MeV}\). Retired.
- Any scan whose null is “uniform \(1/7\)” under a dimuon trigger. Already the wrong null.

---

## Appendix. Loose ends that the tool cannot close

These need a derivation or a refusal. No current subcommand answers them.

### A1. Floor is inserted

\(\Delta_{\mathrm{Tav}}=313.1\,\mathrm{MeV}\) is the nucleon-third protocol, not a theorem. Program L (corpus OPEN, 2026-09-26) tried \(e^{45}\to 349.5\,\mathrm{MeV}\), \(2^{65}\to 330.9\,\mathrm{MeV}\), \(e^{46}\to 128.6\,\mathrm{MeV}\), and selected none. Slot 2 failed: the IN alphabet is not a singleton. No series-plus-residue maps to an energy without taking \(\Delta\) as input.

### A2. \(n_{\mathrm{hier}}=45.8\) is still in the engine

`constants.py` stores \(45.8\) and the comment says it is not \(\log_7(R_\tau/r_M)\). The retired stretch was \(\log_7(\tau/\lambda_{313})\approx 45.8\). The live frame (2026-09-20, 2026-09-21, 2026-10-02) removed that stretch. Either derive a new hierarchical count from binding depth, or delete the number. `desi` still prints it.

### A3. Three different “dark” ratios, no theorem saying which is observable

- Ansatz A shadow sum \(5.401514\) (frame output, not a detection).
- Kernel \(G_{\mathrm{avg}}/G_N=0.202\) from \(\sum 1/\gamma_i^2\).
- SPARC toy uses \(\beta_d^2\) and a hand-set velocity scale \(38+95\sqrt{\beta^2}\,(\gamma_{\mathrm{hex}}/1.4)\).

One derivation has to say which object couples to a rotation curve. Until then SPARC cannot verify the corpus.

### A4. DESI factor is not derived

\(\Delta N_{\mathrm{plasma}}=10.74\) and late \(\Delta N=0.33\) are stored. The identity \(r_d=\Delta N_{\mathrm{plasma}}\,r_{d,\mathrm{obs}}/\gamma\) cannot be confronted with DESI until \(\gamma\) is computed from something other than \(r_{d,\mathrm{obs}}\).

### A5. Vacuum density is an input

\(\rho_{\mathrm{vac}}\) is a chamber input. \(\Omega_\Lambda\) is not recovered from \(r_M\), from the Hopf fibre, or from \(\mathrm{Vol}(S^5)\). The 5-sphere analogue stays back-burner (2026-10-02) and is not an engine.

### A6. Residual-\(L\) gravity has no field equation in the tool

Live thesis: gravity is residual angular momentum of a rebound stopped at the Present, and bound fields tend toward the highest concentration of bound fields. Effective \(G\) belongs to the dominant glob’s centre of mass. No command computes that \(G\), the kernel assumptions A1–A5, or a Poisson solution.

### A7. Domain-cross work is derived and not encoded

\[
E_\times(a\to b)=\theta_{ab}\,\Delta_{\mathrm{Tav}}.
\]

**Key.** \(\theta_{ab}\): angle between domain charts. Adjacent hop \(\theta=\pi/2\) gives \(491.82\,\mathrm{MeV}\) at the printed floor. Antipodal \(\theta=\pi\) gives \(983.63\,\mathrm{MeV}\). Unbound light has \(E_\times=0\). A blocked target adds \(E_{\mathrm{violation}}\ge\Delta_{\mathrm{Tav}}\). This is not a pole. The tool does not compute it, and no public spectrum has been pre-registered against these two numbers.

### A8. Seven bins versus eight phases

The CMS toy excludes \(\Phi_8\) from the histogram by comment. Occupancy of a collider observable by the clock has no theorem. A derivation has to say which phases can appear in a Prime-chart muon sample.

### A9. \(V_{\mathrm{orb}}\) Scheme A is an input table

Betas and gammas are written in, then approximately consistent with each other. They are not computed from PDG masses in the engine. \(\gamma_{\mathrm{hex}}=1.405\) is a third input and is not the harmonic mean \(4.041\). Which one enters a cross section is open.

### A10. Neutron operator is HOLD and unexplained

\(\mathrm{BR}_0=1/(\gamma_d\gamma_s)\) and \(\varepsilon\in\{1/7,2/7\}\) are not derived from TEP or from empty twistor \(H^1\). The module says the leak is domain-internal and has no on-shell \(\chi\gamma\). That sentence needs a selection rule before the lifetime shift is a prediction rather than a parametrization.

### A11. Dynamic Refresh scope versus the bounce cartoon

User lock 2026-09-30: Dynamic Refresh acts on the binding floor, not on a coordinated refresh of higher globs. Isolated centre-of-mass phase persists. The bounce command draws a refresh knob on every frame of an aeon. The drawing is wider than the lock. The cartoon should be cut to the floor or marked as schematic.

### A12. Neutrino triad is not a tool claim and not a lock

The 2026-09-20 braid note (triad \(\{1,4,2\}\) versus anti-triad \(\{8,5,7\}\)) is an analogue. It is not IN. No command folds a neutrino observable. Do not scan \(\sum m_\nu\) for that triad.

### A13. Anomalous dimension is unused

\[
\alpha=1-\log_7 6\approx 0.079218.
\]

**Key.** \(\alpha\): anomalous dimension from the order-6 cycle and six-domain shear. \(\log_7\): logarithm base 7. It is not in `constants.py`. No observable in the tool depends on it. Either attach it to a pre-registered residual or leave it as algebra.

### A14. Associator lock, \(W/Z\), and sterile branch

The \(3/4\) associator remark for a three-quark configuration, and the empty sterile-branching TeX, have no engine and no branching-ratio formula. They are not tests.

### A15. Dirac freeze on the Mirron 2-surface

HOLD: \(\inf\mathrm{spec}(D_\Sigma^\ast D_\Sigma)=1/r_M^2\) on the round \(S^2(r_M)\). Marked TSB-internal, not the Clay problem. No command evaluates the spectrum.

### A16. \(\varphi\)-contact and the three-pair antimatter envelope

Both HOLD / open, non-binding. No formula to code.

### A17. What would make the tool able to verify rather than illustrate

A command verifies a corpus line only if all four are true: the file it reads is public data; the signal is not planted in that file by the command; the null is the one the selection actually imposes; the score is not capped and is tracked against the inserted scale when the claim is about that scale. T1 and T4 meet a weaker standard (internal consistency, and a named external lifetime). T5–T8 do not meet it as shipped.

---

*Saved 2026-10-07. Research engine tree SHA `6b6b07b3`. Not a discovery claim.*
