# Session 2026-09-26 — TEP floor from observables: constituent up mass vs 313.1 MeV

**Framework:** live Superblock frame after 2026-09-20 / 2026-09-21 repair (no Tau circle, no KK fifth dimension as load-bearing objects).  
**Convention:** Mirron, never soliton.  
**Charge:** Derive the IR floor from measured quantities. Answer: what is the constituent mass of the up quark, and can \(\Delta_{\mathrm{Tav}}=313.1\,\mathrm{MeV}\) be derived from it as the energy input?  
**Standing lock this session confirms:** there is still no theorem that \(313.1\,\mathrm{MeV}\) is the unique residue of a named Vălean weight-6 identity plus a Mirron radius \(r_{\mathrm{M}}\). Which series, which factor, and why an MeV IR scale rather than another scale remain open if one starts from Euler sums.

This file: `Personal_Files/Session_2026-09-26_TEP_floor_from_observables_up_constituent.md`  
Also copied to `Personal Files/`, `personal_files/`, `Tau-Superblock-Universe/Personal Files/`, and `Tau-Superblock_Universe/Personal_Files/`.

---

## 0. One-line answers

1. **Current (QCD Lagrangian) up mass** is a PDG observable:  
   \(m_u^{\overline{\mathrm{MS}}}(2\,\mathrm{GeV})=2.16\pm 0.07\,\mathrm{MeV}\).  
   That number is **not** \(313.1\,\mathrm{MeV}\). It cannot be the energy input that *is* the floor.

2. **Constituent up mass** is not a PDG elementary parameter. It is a model scale. Two common estimators disagree:
   - equal-share nucleon: \(m_u^{\mathrm{const}}\simeq M_N/3\simeq 313\,\mathrm{MeV}\);
   - magnetic-moment / NRQM: \(m_u^{\mathrm{const}}\simeq 330\)–\(336\,\mathrm{MeV}\).

3. **Can \(313.1\,\mathrm{MeV}\) be derived from the up quark as energy input?**  
   - From the *current* up mass: **no**.  
   - From the *constituent* up mass: only by **identifying** the floor with the nucleon-third (or with the dressing \(M_N/3-m_u^{\mathrm{cur}}\)). That is a protocol, not a Vălean theorem and not a TEP algebra output.  
   - The magnetic-moment constituent mass \(\approx 336\,\mathrm{MeV}\) does **not** produce \(313.1\). Relative gap \(\approx 6.8\,\%\).

4. Honest protocol step 1 from observables is therefore  
   \(\Delta_{\mathrm{Tav}}:=M_n/3=313.188\,\mathrm{MeV}\)  
   (or the charge-averaged third \(312.973\,\mathrm{MeV}\)), then \(r_{\mathrm{M}}=\hbar c/\Delta\).  
   The printed corpus value \(313.1\,\mathrm{MeV}\) is that neutron-third rounded to \(0.1\,\mathrm{MeV}\).

---

## 1. Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(m_u^{\mathrm{cur}}=m_u^{\overline{\mathrm{MS}}}(2\,\mathrm{GeV})\) | Current (Lagrangian, running) up-quark mass. PDG 2026 summary: \(2.16\pm 0.07\,\mathrm{MeV}\). |
| \(m_d^{\mathrm{cur}}\) | Current down mass. PDG 2026: \(4.70\pm 0.07\,\mathrm{MeV}\). |
| \(m_u^{\mathrm{const}}\) | Constituent (dressed, IR effective) up mass. Model-dependent. Not a PDG listing. |
| \(E_{q\leftarrow g}\) | Dressing energy transmitted from stopped colour bounce to a valence quark. TSB name for the IR inertia of one bound gluon quantum. |
| \(E_g\) | Same object as \(E_{q\leftarrow g}\). Not a \(0^{++}\) glueball pole. |
| \(\Delta_{\mathrm{Tav}}\) | TEP / TSB IR floor. Corpus print \(313.1\,\mathrm{MeV}\). Role: inertial colour dressing. |
| \(M_p\) | Proton mass. CODATA 2022 / PDG 2026 constants: \(938.27208943(29)\,\mathrm{MeV}\). |
| \(M_n\) | Neutron mass. \(939.56542194(48)\,\mathrm{MeV}\). |
| \(\overline{M}_N=(M_p+M_n)/2\) | Isospin-averaged nucleon mass. \(938.91875569\,\mathrm{MeV}\). |
| \(r_{\mathrm{M}}\) | Candidate Mirron 2-surface / clock Compton length of the floor. |
| \(\lambda_{m_0}=\hbar/(m_0 c)=\hbar c/\Delta_{\mathrm{Tav}}\) | Same length written as a reduced Compton wavelength. |
| \(\hbar c\) | \(197.3269804\,\mathrm{MeV\,fm}\) (exact conversion in the SI/CODATA sense used by PDG). |
| \(\lambda_p=\hbar c/M_p\) | Reduced Compton wavelength of the proton. \(0.210309\,\mathrm{fm}\). |
| \(\Phi_7\) | Scrape / Higgs fabric / PK-Mirron channel. Not a seventh spacetime. |
| \(\Phi_8\) | Reset / identity / \(\mathcal{P}\leftrightarrow\mathcal{F}\) seam. |
| TEP | Occupancy rule: no two same-irrep excitations in one \((D_a,\Phi_k)\) slot unless the 142857 projector accepts and the reset projector annihilates. Forced reset overlap costs the dressing quantum. |
| \(H_k\) | Harmonic number. Appears in Vălean alternating Euler sums. Dimensionless. |
| \(\psi(z)\) | Digamma function. Dimensionless combination in Vălean closed forms. |
| \(\gamma\) | Euler–Mascheroni constant (in Vălean identities). Not a Lorentz factor here. |
| \(S_{\mathrm{tw}}\) | Twistor-averaged effective action. Can be evaluated by Euler sums. Does not mint an MeV unit. |
| \(\Lambda_{\mathrm{QCD}}\) | QCD infrared scale. Scheme-dependent, typically \(200\)–\(300\,\mathrm{MeV}\). A cousin of the floor, not identical to \(313.1\). |

**Not used as premises:** \(R_\tau\), \(S^1_\tau\), \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_{313})\), \(G_5\), glueball pole at \(313\,\mathrm{MeV}\), any claim that a named Vălean identity outputs MeV by itself.

---

## 2. Two different “up masses”

QCD has one Lagrangian mass and one IR effective mass. They are not interchangeable.

### 2.1 Current mass (observable, scheme-named)

\[
m_u^{\mathrm{cur}}
=
m_u^{\overline{\mathrm{MS}}}(\mu=2\,\mathrm{GeV})
=
2.16\pm 0.07\,\mathrm{MeV}.
\]

**Key.** \(m_u^{\mathrm{cur}}\) is the Higgs / Yukawa mass parameter of the up field after QCD running to \(2\,\mathrm{GeV}\). PDG 2026 quark summary (Takahashi et al., Int. J. Mod. Phys. A **41**, 2630011 (2026)). Down companion \(m_d^{\mathrm{cur}}=4.70\pm 0.07\,\mathrm{MeV}\).

This is \(\approx 0.69\,\%\) of \(313.1\,\mathrm{MeV}\). It is the *bare* energy input of the up flavour. It is not the floor.

### 2.2 Constituent mass (model scale, two estimators)

A constituent quark is the current quark plus the IR cloud of gluons and sea pairs that a valence line carries inside a hadron. TSB language for the added piece is \(E_{q\leftarrow g}\):

\[
m_u^{\mathrm{const}}
=
m_u^{\mathrm{cur}}
+
E_{q\leftarrow g}
+
\kappa_{\mathrm{bind}},
\]

**Key.** \(E_{q\leftarrow g}\) inertial colour dressing; \(\kappa_{\mathrm{bind}}\) residual binding / kinetic / hyperfine bookkeeping, model-dependent, can be absorbed into the definition of \(m^{\mathrm{const}}\).

**Estimator A — equal-share nucleon (observable protocol).**  
Ignore current masses and binding split. Three valence lines carry the nucleon:

\[
m_{u,d}^{\mathrm{const,A}}
:=
\frac{M_N}{3}.
\]

Numbers from CODATA/PDG 2026 constants:

\[
\frac{M_p}{3}=312.757\,\mathrm{MeV},
\qquad
\frac{M_n}{3}=313.188\,\mathrm{MeV},
\qquad
\frac{\overline{M}_N}{3}=312.973\,\mathrm{MeV}.
\]

The corpus print \(313.1\,\mathrm{MeV}\) is \(M_n/3\) rounded to \(0.1\,\mathrm{MeV}\) (\(313.188\to 313.2\) would also be fair; \(313.1\) sits \(0.088\,\mathrm{MeV}\) below the neutron third).

**Estimator B — nucleon magnetic moments (NRQM / SU(6)).**  
Dirac moment \(\mu_q=e_q\hbar/(2 m_q^{\mathrm{const}} c)\) fitted to \(\mu_p=2.793\,\mu_N\), \(\mu_n=-1.913\,\mu_N\) gives the textbook pair

\[
m_u^{\mathrm{const,B}}\approx 336\,\mathrm{MeV},
\qquad
m_d^{\mathrm{const,B}}\approx 338\text{–}340\,\mathrm{MeV}.
\]

(De Rújula–Georgi–Glashow / Isgur–Karl working values are \(330\)–\(336\,\mathrm{MeV}\).) This estimator is **not** \(313.1\). Gap:

\[
\frac{336-313.1}{336}\approx 6.8\,\%.
\]

Estimator B is the better static-moment scale. Estimator A is the better mass-budget scale. They measure different combinations of dressing, kinetic energy, and binding. TSB’s printed floor tracks A, not B.

**Estimator C — subtract current masses from the nucleon.**  
This is the dressing that actually sits on the valence lines if one refuses to hide \(m^{\mathrm{cur}}\) inside \(m^{\mathrm{const}}\):

\[
E_{\mathrm{dress}}^{(p)}
=
M_p-2m_u^{\mathrm{cur}}-m_d^{\mathrm{cur}}
=
929.25\,\mathrm{MeV},
\qquad
\frac{E_{\mathrm{dress}}^{(p)}}{3}
=
309.75\,\mathrm{MeV}.
\]

\[
E_{\mathrm{dress}}^{(n)}
=
M_n-m_u^{\mathrm{cur}}-2m_d^{\mathrm{cur}}
=
928.01\,\mathrm{MeV},
\qquad
\frac{E_{\mathrm{dress}}^{(n)}}{3}
=
309.34\,\mathrm{MeV}.
\]

So “energy input of the up quark” in the strict additive sense is \(m_u^{\mathrm{cur}}+E_{q\leftarrow g}\). If \(E_{q\leftarrow g}\) is defined as one-third of the nucleon’s non-current mass, the input is \(\approx 312\,\mathrm{MeV}\), not exactly \(313.1\). The \(1\,\mathrm{MeV}\) drift is the current-mass correction plus the \(p/n\) split.

---

## 3. Protocol step 1 from observables (TEP floor)

TEP itself does not output MeV. TEP says a forced \(\Phi_7\to\Phi_8\) overlap is projected out of the physical twistor cohomology and that the local cost of attempting it is *a* dressing quantum. The unit of that quantum is fixed by naming an IR observable.

**Recommended lock (this session):**

\[
\Delta_{\mathrm{Tav}}
\;:=\;
\frac{M_n}{3}
=
313.188\,\mathrm{MeV}
\;\simeq\;
313.1\,\mathrm{MeV}
\quad\text{(corpus rounding)}.
\]

**Key.** \(M_n\) measured neutron mass; \(3\) is the valence occupancy of a nucleon, not the clock integer \(7\).

Compton / Mirron radius of that floor:

\[
r_{\mathrm{M}}
=
\lambda_{m_0}
=
\frac{\hbar c}{\Delta_{\mathrm{Tav}}}
=
\frac{197.3269804\,\mathrm{MeV\,fm}}{313.1\,\mathrm{MeV}}
=
0.63024\,\mathrm{fm}.
\]

**Key.** \(\hbar c\) conversion constant; \(\Delta_{\mathrm{Tav}}\) the named floor.

Identity that makes the same statement without introducing a new length:

\[
3\,\lambda_p
=
3\,\frac{\hbar c}{M_p}
=
0.63093\,\mathrm{fm}
\approx
r_{\mathrm{M}}(313.1).
\]

**Key.** \(\lambda_p\) proton reduced Compton wavelength. The numerical near-equality \(3\lambda_p\approx \hbar c/(M_n/3)\) is just \(M_n\approx M_p\). It is not an independent derivation.

**What this protocol is.**  
A definition of the TSB dressing quantum as the equal-share nucleon mass. It uses only \(M_n\) (or \(M_p\)) and the valence count \(3\).

**What this protocol is not.**
- Not a theorem that TEP algebra produces \(313.1\).
- Not a residue of a Vălean weight-6 sum.
- Not a glueball mass.
- Not \(\hbar c/\tau\) for any megaparsec \(\tau\).
- Not the current up mass.
- Not the magnetic-moment constituent mass.

The 2026-09-21 lock already said \(m_0=313.1\,\mathrm{MeV}\) is an **input**. This session names the observable that justifies that input: the neutron third.

---

## 4. Can the floor be derived *from the up quark*?

Write the candidate maps and score them.

### Map 1 — current up mass is the input

\[
\Delta \stackrel{?}{=} m_u^{\mathrm{cur}} = 2.16\,\mathrm{MeV}.
\]

Fails by two orders of magnitude. The current mass is the Higgs piece. The floor is the colour-dressing piece.

### Map 2 — constituent up mass *is* the floor

\[
\Delta \stackrel{?}{=} m_u^{\mathrm{const}}.
\]

True only after one chooses Estimator A and identifies \(\Delta\) with \(M_N/3\). That is circular if “constituent up mass” was already defined as \(313\,\mathrm{MeV}\). It is a dictionary entry, not a derivation from a smaller up-quark datum.

### Map 3 — dressing on the current up line

\[
\Delta
\stackrel{?}{=}
m_u^{\mathrm{const,A}}-m_u^{\mathrm{cur}}
=
\frac{M_n}{3}-2.16\,\mathrm{MeV}
=
311.03\,\mathrm{MeV}.
\]

This is the cleanest “energy added to the up quark.” It is \(2.07\,\mathrm{MeV}\) below the corpus print. If the floor is *dressing only*, the printed \(313.1\) still contains the current mass. TSB language \(E_g=E_{q\leftarrow g}\) is Map 3, not Map 2. Recommend:

\[
E_g
=
E_{q\leftarrow g}
\simeq
311\,\mathrm{MeV},
\qquad
m_u^{\mathrm{const,A}}
=
m_u^{\mathrm{cur}}+E_g
\simeq
313.2\,\mathrm{MeV}.
\]

Keep the corpus symbol \(\Delta_{\mathrm{Tav}}=313.1\,\mathrm{MeV}\) as the **constituent** equal-share scale (Map 2 / Estimator A). Do not also call it the dressing-only piece unless the \(2\,\mathrm{MeV}\) current-mass split is written.

### Map 4 — Vălean weight-6 residue times \(r_{\mathrm{M}}\)

A typical Vălean identity (from the 2026-06-28 Tau-cylinder note) is dimensionless on the left and produces a combination of \(\psi\), \(\gamma\), and \(\log 2\) on the right:

\[
\sum_{k=1}^\infty (-1)^{k-1}\frac{H_k}{k(k+n+1)}
=
\frac{1}{n}\Bigl(\psi(n+1)+\gamma+2\psi\bigl(\tfrac{n+1}{2}\bigr)-2\psi\bigl(\tfrac{n}{2}\bigr)-2\log 2\Bigr).
\]

**Key.** \(H_k=\sum_{j=1}^k 1/j\); \(n\) a positive integer; \(\psi=\Gamma'/\Gamma\); \(\gamma\) Euler–Mascheroni. Every symbol is a pure number.

Multiplying that number by \(\hbar c/r_{\mathrm{M}}\) *assumes* \(r_{\mathrm{M}}\) and an MeV unit already. It cannot select \(313.1\,\mathrm{MeV}\) over \(140\,\mathrm{MeV}\) (pion), \(494\,\mathrm{MeV}\) (kaon), or \(\Lambda_{\mathrm{QCD}}\). The user statement stands:

> There is no theorem that this number is the unique residue of a named Vălean weight-6 identity plus \(r_{\mathrm{M}}\). Which series, which factor, and why MeV rather than another IR scale remain open.

Euler sums may still evaluate a twistor-averaged *phase weight*. They do not mint the IR unit.

### Map 5 — Planck–Kerr averaging formula from the V2 unification PDF

The old line

\[
M_{\mathrm{eff}}^{p\text{-}k}
=
\frac{M_{\mathrm{Pl}}}{6\,\langle\gamma\rangle_6\,\sqrt{N_{\mathrm{bubble}}}}
\stackrel{?}{\approx}
313.1\,\mathrm{MeV}
\]

is not an observable derivation. \(\langle\gamma\rangle_6\) and \(N_{\mathrm{bubble}}\) were never supplied as measured six-tuples in a way that *predicts* \(313.1\) before it is inserted. The 2026-09-18 quark-increment \(\langle\gamma\rangle_6\sim 10^4\) (current-mass ratios to \(m_u\)) is a different object and must not be dropped into that formula (already flagged 2026-09-18). Retired as a derivation of the floor.

---

## 5. What TEP actually contributes

From `Session_2026-09-20_TEP_Without_Tau_Circle_and_KK5.md`, the load-bearing sentence is occupancy, not a mass formula.

- Eight letters from \(\mathbb{O}\). \(\Phi_8\leftrightarrow e_0=1\), \(\Phi_7\) reserved as scrape / Mirron.
- Six domain letters \(\leftrightarrow(\mathbb{Z}/7\mathbb{Z})^\times=\{1,2,3,4,5,6\}\).
- \(e_i^2=-1\) is the algebraic reset insertion.
- Empty twistor \(H^1\) for local reset overlap.
- Bound bounce stops at the Present; unbound completes \(\mathcal{P}\leftrightarrow\mathcal{F}\).

TEP therefore predicts **that a smallest positive deposit exists** when a bound colour line is forced through scrape into reset. It does not compute the deposit in MeV. The deposit’s size is read from the lightest stable three-quark bound state by Estimator A.

That is the correct division of labour:

| Layer | Source | Output |
|---|---|---|
| Existence of a floor | TEP + bound vs unbound bounce | \(\Delta>0\) |
| Unit and value | nucleon mass / 3 | \(313.1\,\mathrm{MeV}\) |
| Length | \(\hbar c/\Delta\) | \(r_{\mathrm{M}}=0.6302\,\mathrm{fm}\) |
| Phase weights | \(142857\), optional Vălean sums | dimensionless |
| Glueball | lattice / spectroscopy | \(\sim 1.6\,\mathrm{GeV}\), not \(\Delta\) |
| Current up mass | PDG \(\overline{\mathrm{MS}}\) | \(2.16\,\mathrm{MeV}\) |

---

## 6. Why MeV rather than another IR scale

Once Estimator A is chosen, the unit is forced: nucleon masses are tabulated in MeV. That is the only reason the floor is an MeV number rather than an eV or a GeV.

Cousin IR scales that are *not* being identified with \(\Delta_{\mathrm{Tav}}\):

| Scale | Value | Why it is not the floor |
|---|---|---|
| \(m_u^{\mathrm{cur}}\) | \(2.16\,\mathrm{MeV}\) | Higgs piece, not dressing |
| \(m_{\pi^\pm}\) | \(139.57\,\mathrm{MeV}\) | Goldstone of chiral breaking; not three-valence share |
| \(f_\pi\) | \(92.2\,\mathrm{MeV}\) | decay constant, different operator |
| \(\Lambda_{\mathrm{QCD}}^{\overline{\mathrm{MS}}}\) | \(\sim 200\)–\(300\,\mathrm{MeV}\) | scheme/flavour dependent; same ballpark, not equal |
| \(m_u^{\mathrm{const,B}}\) | \(\sim 336\,\mathrm{MeV}\) | magnetic-moment estimator |
| \(\sqrt{\sigma}\) (string tension) | \(\sim 420\)–\(440\,\mathrm{MeV}\) | Wilson-loop scale |
| \(M_{0^{++}}\) glueball | \(\sim 1.6\)–\(1.7\,\mathrm{GeV}\) | retired identification (2026-09-14) |
| \(m_\rho/2\) | \(\sim 388\,\mathrm{MeV}\) | meson-side constituent bookkeeping |

The floor is the nucleon-third because TSB’s dressing story is “one stopped colour quantum per valence line in the lightest stable three-quark state.” If that story is rejected, \(313.1\) has no preferred observable home.

---

## 7. Recommended wording going forward

Use this sentence, not the Vălean-plus-radius sentence:

> The TEP floor is the inertial dressing of one valence colour line in the nucleon. Its value is the observable equal-share \(M_n/3=313.188\,\mathrm{MeV}\), printed as \(313.1\,\mathrm{MeV}\). The current up mass \(2.16\,\mathrm{MeV}\) is the Higgs remainder inside that share. The Mirron radius is the Compton length of the share, \(r_{\mathrm{M}}=\hbar c/\Delta=0.6302\,\mathrm{fm}\). Vălean identities may weight phases of the twistor action; they do not select the MeV unit.

Keep \(m_0=313.1\,\mathrm{MeV}\) as the 2026-09-21 input in every later formula that already uses it. When a derivation from observables is requested, cite this session and \(M_n/3\), not a weight-6 Euler sum.

---

## 8. Numerical digest (this query)

| Quantity | Value |
|---|---|
| \(m_u^{\mathrm{cur}}\) (PDG 2026) | \(2.16\pm 0.07\,\mathrm{MeV}\) |
| \(m_d^{\mathrm{cur}}\) (PDG 2026) | \(4.70\pm 0.07\,\mathrm{MeV}\) |
| \(M_p\) | \(938.27208943\,\mathrm{MeV}\) |
| \(M_n\) | \(939.56542194\,\mathrm{MeV}\) |
| \(M_p/3\) | \(312.757\,\mathrm{MeV}\) |
| \(M_n/3\) | \(313.188\,\mathrm{MeV}\) |
| \(\overline{M}_N/3\) | \(312.973\,\mathrm{MeV}\) |
| corpus \(\Delta_{\mathrm{Tav}}\) | \(313.1\,\mathrm{MeV}\) |
| \(\Delta_{\mathrm{Tav}}-M_n/3\) | \(-0.088\,\mathrm{MeV}\) |
| \(M_p-2m_u-m_d\) over \(3\) | \(309.75\,\mathrm{MeV}\) |
| \(m_u^{\mathrm{const,B}}\) (moments) | \(\approx 336\,\mathrm{MeV}\) |
| \(r_{\mathrm{M}}(313.1)\) | \(0.63024\,\mathrm{fm}\) |
| \(3\lambda_p\) | \(0.63093\,\mathrm{fm}\) |

---

## 9. Files and locks touched

- Confirms 2026-09-14: \(\Delta_{\mathrm{Tav}}=E_g=E_{q\leftarrow g}\), not a glueball.  
- Confirms 2026-09-20: TEP does not use \(\tau\) or KK.  
- Confirms 2026-09-21: \(m_0\) is an input to the pinch/packing stack. This session supplies the observable that names the input.  
- Does not reopen \(n_{\mathrm{hier}}\), \(R_\tau\), or Vălean-as-MeV.

---

*Saved 2026-09-26.*
