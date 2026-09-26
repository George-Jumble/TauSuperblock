# How to close the three TEP OPEN slots

**Session date:** 2026-09-26  
**Status:** method note — not a closure, not a theorem  
**Repo path:** `Personal Files/2026-09-26_how_to_close_TEP_OPEN_slots.md`  
**Depends on:** protocol step 1 (`Personal Files/2026-09-26_TEP_floor_protocol_step1_no_Valean_uniqueness.md`), `CORPUS.md` 2026-09-26

Protocol step 1 stays in force while this work runs:

\[
\Delta \;=\; \frac{\hbar c}{r_M} \;=\; 313.1\,\mathrm{MeV}
\]

is an assignment. Closing a slot promotes a *theorem candidate*. It does not silently rewrite step 1.

---

## Variable and function key

| Symbol | Meaning |
|---|---|
| \(\Delta\) | TEP floor. Protocol value \(313.1\,\mathrm{MeV}\). |
| \(r_M\) | Mirron / Planck–Kerr 2-surface radius. \(r_M=\hbar c/\Delta=0.630236256\,\mathrm{fm}\). |
| \(\lambda_{313}\) | Compton length of \(313.1\,\mathrm{MeV}\). Identity \(r_M=\lambda_{313}\). |
| \(\hbar c\) | \(197.3269718\,\mathrm{MeV\cdot fm}\). |
| \(\ell_P\) | Planck length, seed only. Not the clock radius. \(1.616255\times10^{-35}\,\mathrm{m}\). |
| \(E_P\) | Planck energy. The illegal reading of \(\hbar c/\ell_P\). OUT as a stand-in for \(\Delta\). |
| \(S\) | A cited series, modular form, character expansion, or generating function. |
| \(\mathrm{Res}\) | A named residue map (constant term, \(q^1\) coefficient, special value, pairing, …). |
| \(\rho\) | Dimensionless output of \(\mathrm{Res}(S)\). |
| \(f\) | Dimensionless factor sitting between \(\rho\) and an energy. |
| \(\Lambda\) | An infrared energy scale with dimensions of mass. The “why MeV” object. |
| \(W_k\) | Modular weight. \(M_6(\mathrm{SL}_2(\mathbb{Z}))=\mathbb{C}\,E_6\). |
| \(E_6(q)\) | \(E_6(q)=1-504\sum_{n\ge1}\sigma_5(n)q^n\). |
| \(\sigma_5(n)\) | Sum of fifth powers of positive divisors of \(n\). |
| \(B_6\) | Bernoulli number \(B_6=-1/42\). |
| \(\Delta_{\mathrm{mod}}\) | Modular discriminant \((E_4^3-E_6^2)/1728\), weight 12, not 6. |
| \(n_{\mathrm{hier}}\) | Superblock hierarchical binding index. Engine value \(45.8\). Not \(\log_7\) of a Tau cylinder. |
| Aut(\(\mathbb{O}\))\(\cong G_2\) | 8-phase clockwork automorphism group. IN. |
| \(\Phi_8\) | Past ⇄ Future inversion in the 8-phase clock. IN. |
| \(m_p,m_n\) | Nucleon masses. Diagnostics only. |
| \(M_{u/d}^{\mathrm{const}}\) | Constituent-band comparator. Not \(\Delta\)’s definition. |
| \(m_\pi\) | Charged-pion mass. Different object. |
| \(\Lambda_{\mathrm{QCD}}\) | Typical QCD infrared scale \(\sim200\)–\(300\,\mathrm{MeV}\). Same island, not a theorem. |

Template identity that any closure must write explicitly:

\[
\Delta \;\stackrel{?}{=}\; f\cdot\rho\cdot\Lambda
\qquad\text{or}\qquad
\Delta \;\stackrel{?}{=}\; \frac{\hbar c}{r_M^{\mathrm{(derived)}}}.
\]

The first form is series-first. The second is length-first. Mixing them without saying which side is derived is how the slots stay pretend-closed.

---

## Diagnostic arithmetic this session (not a selection)

\[
\frac{r_M}{\ell_P}=3.899362\times10^{19}.
\]

\[
\log_7\!\left(\frac{r_M}{\ell_P}\right)=23.1819,\quad
\log_8\!\left(\frac{r_M}{\ell_P}\right)=21.6933,\quad
\ln\!\left(\frac{r_M}{\ell_P}\right)=45.1099.
\]

Ratios of listed factors to the protocol number (fishing table; **do not use as a selection rule**):

| listed \(f\) | \(\Delta/f\) | \(f/\Delta\) |
|---|---|---|
| \(504\) | \(0.621230\) | \(1.609709\) |
| \(1728\) | \(0.181192\) | \(5.519004\) |
| \(7\) | \(44.728571\) | \(0.022357\) |
| \(8\) | \(39.137500\) | \(0.025551\) |
| \(1/7\) | \(2191.700\) | \(0.000456\) |
| \(n_{\mathrm{hier}}=45.8\) | \(6.836245\) | \(0.146279\) |
| \(\lvert B_6\rvert=1/42\) | \(13150.200\) | \(0.000076\) |
| \(240\) | \(1.304583\) | \(0.766528\) |
| \(42\) | \(7.454762\) | \(0.134142\) |

None of these ratios is an integer forced by IN geometry. That is the point of the table: listed is not selected.

---

## What “closed” means

A slot is **closed** only when all of the following are true.

1. A written candidate exists in Personal Files, with citation, formula, and gates passed.
2. The candidate does not take \(313.1\,\mathrm{MeV}\) or \(r_M=0.630\,\mathrm{fm}\) as an *input*. It may use them as a *check after* the derivation.
3. CORPUS is updated by a separate decision note: candidate → IN, or candidate → failed / archive.
4. Protocol step 1 is either (a) left as the lock and the candidate is tagged *explanation*, or (b) explicitly retired in favour of the new derivation. Those are different acts. Do not blur them.

A slot is **not** closed by: proximity to \(m_p/3\), a famous Eisenstein coefficient, a log-base that used to belong to the Tau layer, or a sentence that concatenates “Vălean,” “weight 6,” and “\(r_M\).”

---

## Recommended order: close Slot 3 first

Two programs exist. They are not equivalent.

### Program L — length-first (recommended)

1. Construct \(r_M\) from objects already IN, without feeding in \(313.1\,\mathrm{MeV}\).
2. Set \(\Delta=\hbar c/r_M\). “MeV” is then only the lab unit in which that energy is tabulated.
3. Series and factor become optional structure notes. They are no longer required to *generate* the floor.

This program can close Slot 3 even if Slots 1 and 2 remain empty. That is allowed. Empty-and-honest is better than filled-and-circular.

### Program S — series-first (harder, optional)

1. Cite \(S\) and \(\mathrm{Res}\), get dimensionless \(\rho\).
2. Force \(f\) from IN geometry.
3. Still need an independent \(\Lambda\). Program S cannot skip Slot 3.

Program S is the uniqueness-theorem path that is currently OUT as a *claim*. It may be reopened as a *candidate* if every gate below passes. It must not be treated as already done.

Do not run a Program F — factor-first fishing trip (\(504\), \(1728\), \(7\), \(8\), \(B_6\)) against \(313.1\). That is the table above, and it is not a method.

---

## Slot 3 — why MeV (close this first)

### Split the question

“Why MeV” hides two different questions.

- **Q3a. Unit convention.** MeV is the unit PDG uses for hadron and constituent-scale masses. Changing to GeV is a rewrite: \(0.3131\,\mathrm{GeV}\) is the same lock. Closing Q3a is cheap: say the unit is conventional.
- **Q3b. Scale selection.** Why is the infrared object the hadronic / constituent island (\(\sim 0.63\,\mathrm{fm}\), \(\sim 313\,\mathrm{MeV}\)) rather than \(m_\pi\), raw \(\Lambda_{\mathrm{QCD}}\) as an independent definition, \(E_P\), or a cosmological length? This is the real slot.

Only Q3b is worth a theorem candidate.

### Gates for Q3b

| Gate | Demand |
|---|---|
| S1 | One of \(\{r_M,\Delta,\Lambda\}\) is constructed from IN objects with no numerical feed-in of \(313.1\) or \(0.630\,\mathrm{fm}\). |
| S2 | Unit convention (MeV vs GeV vs J) is written separately from scale selection. |
| S3 | OUT scales are excluded by the construction itself: \(\ell_P\) as clock radius, \(E_P\) as \(\Delta\), Tau-cylinder megaparsecs. |
| S4 | Category errors excluded: current \(\overline{\mathrm{MS}}\) masses, \(m_\pi\) as the definition of \(\Delta\), Casimir \(\Delta E\) (shape tests only). |
| S5 | If \(r_M\) is the constructed object, Compton duality is the *only* step to \(\Delta\). No extra \(f\). |
| S6 | \(m_p/3=312.757\,\mathrm{MeV}\) and \((m_p+m_n)/6=312.973\,\mathrm{MeV}\) are post-hoc checks, not inputs. |
| S7 | A named falsifier exists: a geometric output that would have landed on \(m_\pi\), on \(E_P\), or on a cosmological length. |

### Live construction routes for \(r_M\) (candidates only)

These are routes to *try*. None of them is IN as a derivation of \(r_M\).

1. **Planck–Kerr 2-surface from \(\ell_P\) plus IN clockwork.**  
   Write a map \(\ell_P \mapsto r_M\) whose multiplier is forced by Aut(\(\mathbb{O}\))\(\cong G_2\), the 8-phase clock, or the six-domain supersphere, *without* using \(\log_7\) of a Tau cylinder.  
   Diagnostic only: \(r_M/\ell_P=3.899362\times10^{19}\). \(\log_7\) of that ratio is \(23.1819\), which is the retired Tau-era count and is not a live input. \(\log_8\) is \(21.6933\), not an integer. \(\ln\) is \(45.1099\), near the engine \(n_{\mathrm{hier}}=45.8\) but not equal. Near is not closed.

2. **Prime-domain confinement radius.**  
   If the Prime domain (\(u\), \(\beta_0=0\)) carries a unique IR 2-surface whose area or curvature radius is fixed by the Planck–Kerr construction plus six-domain packing, that radius *is* \(r_M\). Then “why the hadronic island” becomes “why the Prime-domain 2-surface sits at femtometres,” which is a geometry problem, not a units problem.

3. **Casimir *shape* only as a consistency check.**  
   Corpus IN: Casimir 7-phase impedance shape tests, not \(\Delta E\). A shape peak at \(r\sim0.63\,\mathrm{fm}\) would support the lock. It would not derive it. Bound-energy residual search stays OUT.

4. **Yang–Mills gap via Planckian mirrors.**  
   Mechanism *claim* is already IN. Closing Slot 3 along this route means exhibiting a gap equation whose unique IR eigenvalue is \(\Delta\), with \(r_M\) as the mirror radius that enters the kernel, and with no hand-set \(313.1\). Until that equation is written and solved, this route is a slogan.

### What does *not* close Slot 3

- Saying “MeV is the natural hadronic unit.” That closes Q3a only.
- Pointing at the constituent band \(300\)–\(350\,\mathrm{MeV}\). Coherence, already recorded, not a construction.
- Setting \(r_M=\ell_P\). OUT. That moves \(\Delta\) to \(E_P\).
- Using \(R_\tau\) or \(7\,h^{-1}\,\mathrm{Mpc}\). OUT.
- Folding WilfiCon / \(\varphi\)-contact in as a metrological root. HOLD / external file.

### If Slot 3 closes

CORPUS addendum would read, schematically: *\(r_M\) derived from [named map]; \(\Delta=\hbar c/r_M\) recovered; protocol step 1 demoted from assignment to theorem, or kept as the lock with the map tagged explanation.* That sentence is written only after S1–S7 pass.

If Slot 3 cannot be closed without circularity, leave it OPEN and do not pretend Slots 1–2 can manufacture a scale.

---

## Slot 2 — which factor

A factor is a dimensionless number forced by IN geometry or by the same modular object used in Slot 1. It is not “a famous integer near a ratio of \(\Delta\).”

### Gates

| Gate | Demand |
|---|---|
| F1 | \(f\) is an invariant of an IN object, or of the cited \(S\) of Slot 1. |
| F2 | A written selection rule makes \(f\) unique among the listed competitors. |
| F3 | \(f\) is dimensionless. |
| F4 | Computing \(f\) does not use \(313.1\) or \(0.630\,\mathrm{fm}\). |
| F5 | The template \(\Delta=f\cdot\rho\cdot\Lambda\) (or the length-first form) is written, and \(f\)’s slot in it is fixed before numbers are compared. |
| F6 | Each rejected competitor (\(504\), \(1728\), \(7\), \(8\), \(1/7\), \(n_{\mathrm{hier}}\), \(B_6\), \(240\)) is rejected *by the rule*, not by worse proximity to \(\Delta\). |

### Lawful sources of \(f\)

From objects already IN:

- six domains → \(6\) or \(1/6\), only if a written pairing says the floor is a six-cell mean or a one-cell share
- 8-phase clockwork / Aut(\(\mathbb{O}\))\(\cong G_2\) → \(8\), \(14=\dim G_2\), \(7=\mathrm{rank}\) relations of \(G_2\), only if the same pairing is written
- E6 \(\subset\) E8 weight assignment → index, Coxeter number, or fundamental-weight pairing of the Prime axis \(\omega_1\), not a PDG increment
- CMS 7-fold occupancy → \(7\) or \(1/7\), only as an occupancy weight, and only if that occupancy is shown to multiply an energy rather than a count

From a Slot-1 series, if one exists:

- Eisenstein leading coefficient of \(E_6\) → \(504\), only if \(\mathrm{Res}\) is defined to return that coefficient
- Bernoulli \(B_6=-1/42\), only if the same Euler–Maclaurin / zeta-value identity that produces \(E_6\) is the cited \(S\)
- \(1728\), only if the object is actually \(\Delta_{\mathrm{mod}}\) (weight 12). Using \(1728\) while saying “weight 6” is a weight error

### Unlawful sources

- \(n_{\mathrm{hier}}=45.8\) used as if it were \(\log_7(R_\tau/r_M)\). The Tau cylinder is OUT. If \(n_{\mathrm{hier}}\) is ever a factor, it must be re-derived as Superblock hierarchical binding with no \(R_\tau\).
- Any \(f\) chosen because \(\Delta/f\) “looks like” \(n_{\mathrm{hier}}\) or \(\gamma_s\).
- \(\varphi\) from the external WilfiCon file.

### Practical work sequence for Slot 2

1. Write the selection rule *before* looking at the fishing table.
2. List every IN integer that the rule could have produced.
3. If the list has more than one entry, the slot is not closed.
4. If the list has one entry, run F4: recompute \(f\) with \(313.1\) deleted from the workspace. If the number changes, fail F4.
5. Only then compare \(f\cdot\rho\cdot\Lambda\) to \(313.1\,\mathrm{MeV}\) as a check.

---

## Slot 1 — which series

“Series” means a cited analytic object plus a residue map. Weight 6 is a *space*, not a series. “Informal Vălean weight-6” is a pointer with no formula; it cannot close anything until it is replaced by a citation and an equation.

### Gates

| Gate | Demand |
|---|---|
| V1 | Citation: paper / book / identity number, page, year. |
| V2 | Formula for \(S\), written in the note. |
| V3 | Named map \(\mathrm{Res}\). Examples that count: constant term, coefficient of \(q^1\), value at \(\tau=i\) or \(i\infty\), Petersson pairing against a specified form, contour integral around a specified pole. |
| V4 | Output \(\rho=\mathrm{Res}(S)\) is dimensionless, or its dimensions are written and then cancelled by \(f\) and \(\Lambda\) in a stated way. |
| V5 | Uniqueness *of the form in its space* is not smuggled as uniqueness of \(313.1\,\mathrm{MeV}\). \(\dim M_6=1\) means \(E_6\) is the unique normalized weight-6 Eisenstein form on \(\mathrm{SL}_2(\mathbb{Z})\). It does not mean \(504\) times something equals the TEP floor. |
| V6 | \(S\) and \(\mathrm{Res}\) do not take \(\Delta\) or \(r_M\) as arguments. |
| V7 | \(S\) is compatible with the OUT list. No compact \(S^1_\tau\), no 142857 KK comb as the \(q\)-index, no WilfiCon module. |
| V8 | A falsifier is named: another form of the same weight, or another residue map on the same form, that the candidate would have to beat. |

### Candidate classes, with what each still lacks

**A. Eisenstein \(E_6\).**  
Has a citation in every modular-forms text. Has a formula. Natural \(\mathrm{Res}\) options: constant term \(1\) (useless), leading cusp coefficient \(504\), special values of \(E_6(\tau)\).  
Still missing: a map from that coefficient to an energy that does not invent \(\Lambda\), and a reason that weight 6 rather than weight 4 (\(E_4\), coefficient \(240\)) or weight 12 (\(\Delta_{\mathrm{mod}}\), \(1728\)) is the TEP object. Dimensional uniqueness of \(M_6\) is not that reason by itself.

**B. Named Vălean identity.**  
Currently a blank. Closing path: pick one identity, quote it, define \(\mathrm{Res}\), produce \(\rho\), then stop. Do not append “plus \(r_M\)” until Slots 2 and 3 exist. If no identity is found that yields a unique \(\rho\) relevant to the Prime-domain floor, this class is retired as a name and removed from the OPEN list (the name dies; the slot can stay empty).

**C. Clockwork characters.**  
IN objects: 8-phase clock, Aut(\(\mathbb{O}\))\(\cong G_2\), CMS 7-fold occupancy. A series here would be a character generating function or occupancy trace, not a modular form.  
Still missing: the generating function itself. CMS 7-fold occupancy is an empirical count. It is not yet a \(q\)-series. Do not relabel a histogram as \(E_6\).

**D. Nothing yet written.**  
This is a lawful state. Closing the slot *as empty* is allowed: write a decision that no series is required because Program L closed Slot 3 and \(\Delta=\hbar c/r_M\) needs no \(\rho\). That is a closure of the *demand*, not a closure by a series.

### Weight checklist (to stop category errors)

- Weight 4: \(E_4=1+240\sum\sigma_3(n)q^n\). Competitor, must be excluded by rule if weight 6 is chosen.
- Weight 6: \(E_6=1-504\sum\sigma_5(n)q^n\). Present candidate class A.
- Weight 8, 10, 14: also one-dimensional, generated by products of \(E_4,E_6\). If those are excluded, say why.
- Weight 12: \(\Delta_{\mathrm{mod}}\) and \(E_4^3\), \(E_6^2\). Source of \(1728\). Not a weight-6 identity.

---

## Combined acceptance test

A full series-first closure is the single written line

\[
\Delta_{\mathrm{pred}} \;=\; f\cdot\mathrm{Res}(S)\cdot\Lambda
\]

with all three pieces independently sourced, plus the numerical check

\[
\left\lvert\Delta_{\mathrm{pred}}-313.1\,\mathrm{MeV}\right\rvert
\]

reported as a *test*, not as the method that chose \(f\) or \(\Lambda\).

A full length-first closure is the single written line

\[
r_M^{\mathrm{(derived)}} \;=\; \mathcal{G}(\ell_P;\;\text{IN data}),
\qquad
\Delta_{\mathrm{pred}} \;=\; \frac{\hbar c}{r_M^{\mathrm{(derived)}}}
\]

with \(\mathcal{G}\) using no MeV input, plus the same numerical check against \(0.630236\,\mathrm{fm}\) and \(313.1\,\mathrm{MeV}\).

Either line, with gates attached, is enough to open a CORPUS review. Neither line exists today.

---

## Work order (practical)

1. Freeze protocol step 1. Do not retune \(313.1\) while hunting.
2. Attempt Program L, route 1 or 2, for Slot 3. Write \(\mathcal{G}\) or record that no \(\mathcal{G}\) was found.
3. Only if Program L fails and a series-first paper is still wanted: pick *one* class among A–C. Ban class-hopping inside a single note.
4. Write \(\mathrm{Res}\) and \(f\) selection rules with \(313.1\) deleted from the page.
5. Restore \(313.1\) as a check.
6. Publish the note as HOLD / theorem candidate. Do not edit CORPUS IN until a separate decision.

Edge cases:

- If two routes both pass and disagree numerically, neither is closed. That is a fork, not a floor.
- If Program L produces \(r_M\) at a different IR island (pion-sized, Planck-sized), the candidate *fails S7* rather than retuning the protocol.
- If a Vălean citation cannot be produced, drop the name from OPEN. Keep the slot as “no series required” or “Eisenstein only” or empty.

---

## What this session does *not* do

- Does not select \(E_6\), a Vălean identity, or clockwork characters.
- Does not select \(504\), \(1728\), \(7\), \(8\), \(1/7\), \(n_{\mathrm{hier}}\), or \(B_6\).
- Does not change \(\Delta=313.1\,\mathrm{MeV}\) or \(r_M=\lambda_{313}\).
- Does not move any OPEN line to IN.

CORPUS OPEN remains:

- Which series would map a Vălean / weight-6 object onto \(\Delta\)
- Which dimensionless factor would sit between that series and \(313.1\,\mathrm{MeV}\)
- Why the IR unit is MeV (hadronic / constituent island) rather than another IR scale

---

## Bottom line

Close Slot 3 first, length-first if possible: derive \(r_M\) from IN geometry, let Compton make \(\Delta\), treat MeV as the lab unit of that energy. Slots 1 and 2 then either stay empty on purpose or are filled by a cited \(S\), a named \(\mathrm{Res}\), and a factor forced by a rule written before the fishing table. Anything that uses \(313.1\,\mathrm{MeV}\) as an input has not closed a slot. It has restated protocol step 1.
