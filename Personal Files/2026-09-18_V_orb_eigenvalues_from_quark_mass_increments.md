# Session log: Staggered \(V_{\mathrm{orb}}\) eigenvalues from quark-family relativistic increments on the up quark

- **Session date:** Friday, 2026-09-18
- **Question:** The \(V_{\mathrm{orb}}\) eigenvalues were not in the readable corpus. Derive them using the quark-family masses as relativistic increments to the up-quark value.
- **Short answer:** Treat the up current-quark mass as the Prime-domain rest increment and every other flavour mass as the same increment seen from a boosted domain,
  \[
  m_i=\gamma_i\,m_u,\qquad
  \beta_i=\sqrt{1-\Bigl(\frac{m_u}{m_i}\Bigr)^2},\qquad
  V_{\mathrm{orb},i}=\beta_i\,c.
  \]
  PDG 2025 (Navas et al., 2024 review + 2025 update) then gives a unique six-tuple. Prime (up) sits at rest in this gauge: \(\beta_u=0\). Down is mildly relativistic (\(\beta_d=0.888\pm 0.008\)). Strange through top are ultra-relativistic (\(\beta_s=0.999733\), \(\beta_c=1-1.44\times 10^{-6}\), \(\beta_b=1-1.33\times 10^{-7}\), \(\beta_t=1-7.83\times 10^{-11}\)). These are **phenomenological** eigenvalues read off measured masses. They are not \(E_8\) projection eigenvalues. The two constructions must not be silently identified.
- **This file:** `Personal Files/2026-09-18_V_orb_eigenvalues_from_quark_mass_increments.md`
- **Uses:** PDG 2025 quark summary; TSB six-domain lock; 2026-09-18 \(\Phi\) cell (domain-edge weights).

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(m_u,m_d,m_s,m_c,m_b,m_t\) | Quark masses. Central values and errors: PDG 2025 update. Scheme stated per flavour below. |
| \(m_u=2.16\pm 0.07\,\mathrm{MeV}\) | \(\overline{\mathrm{MS}}\) mass at \(\mu=2\,\mathrm{GeV}\). Baseline rest increment. |
| \(m_d=4.70\pm 0.07\,\mathrm{MeV}\) | \(\overline{\mathrm{MS}}\) at \(2\,\mathrm{GeV}\). |
| \(m_s=93.5\pm 0.8\,\mathrm{MeV}\) | \(\overline{\mathrm{MS}}\) at \(2\,\mathrm{GeV}\). |
| \(m_c=1.2730\pm 0.0046\,\mathrm{GeV}\) | \(\overline{\mathrm{MS}}\) at \(\mu=m_c\). |
| \(m_b=4.183\pm 0.007\,\mathrm{GeV}\) | \(\overline{\mathrm{MS}}\) at \(\mu=m_b\). |
| \(m_t=172.56\pm 0.31\,\mathrm{GeV}\) | Direct (kinematic) top mass. |
| \(\gamma_i=m_i/m_u\) | Domain-\(i\) Lorentz factor in Scheme A (preferred). |
| \(\beta_i=v_i/c=\sqrt{1-\gamma_i^{-2}}\) | Dimensionless orbital speed of domain \(i\) on the internal \(S^3\). |
| \(V_{\mathrm{orb},i}=\beta_i c\) | Staggered orbital velocity eigenvalue. SI speed. |
| \(1-\beta_i=1/\bigl[\gamma_i^2(1+\beta_i)\bigr]\) | Stable form for ultra-relativistic domains. |
| \(c\) | Prime-domain invariant speed. |
| Scheme A | \(m_i=\gamma_i m_u\). Mass *is* the boosted up increment. Preferred reading of “increments to the up quark.” |
| Scheme C | \(\gamma_i=1+m_i/m_u\). Increment is purely kinetic; a leftover rest sits under every flavour. Control only. |
| Prime domain | Identified with the up flavour. Gauge choice: \(\gamma_u=1\), \(\beta_u=0\). |
| \(\langle\gamma\rangle_6=N_{\mathrm{dom}}^{-1}\sum_i\gamma_i\) | Arithmetic mean of the six Lorentz factors. |
| \(\langle\beta\rangle_6\) | Arithmetic mean of the six \(\beta_i\). |
| \(\gamma_{ij}^{\\|}=\gamma_i\gamma_j(1-\beta_i\beta_j)\) | Collinear same-direction relative Lorentz factor. |
| \(\gamma_{ij}^{\\mathrm{opp}}=\gamma_i\gamma_j(1+\beta_i\beta_j)\) | Collinear opposite-direction (antipodal) relative Lorentz factor. |
| \(N_{\mathrm{dom}}=6\) | Co-located 3+1D domains. |
| \(\Delta_{\mathrm{TEP}}\approx 313.1\,\mathrm{MeV}\) | TEP floor. Not used as \(m_u\). Control only (constituent column). |
| \(w_{ij}\) | Domain-edge weight on \(G_{\mathrm{cell}}\) of the 2026-09-18 \(\Phi\) note. |

PDG citation: S. Navas et al. (Particle Data Group), Phys. Rev. D **110**, 030001 (2024) and 2025 update, quark summary tables.

---

## 1. What is being derived, and what is not

The corpus says the six domains carry staggered \(V_{\mathrm{orb}}\) “from \(E_8\) projections,” parameter-free. Those projection eigenvalues are **not** in any readable file. This session does **not** compute an \(E_8\) weight diagram.

The instruction is a different construction: read the six speeds off the quark masses, taking the up mass as the rest increment. That is a phenomenological map

\[
\{\text{six flavours}\}\;\longrightarrow\;\{\text{six }\beta_i\}.
\]

It can *stand in* for the missing \(E_8\) six-tuple in the \(\Phi\) cell and in any formula that only needs the numbers. It cannot be cited as an \(E_8\) result.

---

## 2. Relativistic-increment law

**Scheme A (preferred).**  
In the Prime rest frame the up current-quark mass is a rest energy. Every other flavour is that same increment, viewed from a domain that moves at \(\beta_i\) on the internal supersphere:
\[
m_i c^2=\gamma_i\, m_u c^2,\qquad
\gamma_i=\frac{m_i}{m_u},\qquad
\beta_i=\sqrt{1-\frac{m_u^2}{m_i^2}}.
\]
**Key:** \(m_i\) PDG mass of flavour \(i\); \(m_u\) up mass; \(\gamma_i\) Lorentz factor of domain \(i\) relative to Prime; \(\beta_i=V_{\mathrm{orb},i}/c\).

Up is the zero of velocity by gauge choice on \(S^3\):
\[
\gamma_u=1,\qquad \beta_u=0,\qquad V_{\mathrm{orb},u}=0.
\]
A rigid rotation of the whole six-tuple on \(S^3\) can give every domain a nonzero speed without changing any *relative* \(\gamma_{ij}\). The eigenvalues that matter for domain-edge weights are the relatives, not the Prime-frame zeros.

**Scheme C (control).**  
“Increment” read as kinetic energy only,
\[
\gamma_i=1+\frac{m_i}{m_u}.
\]
Then even the up domain moves (\(\gamma_u=2\), \(\beta_u=\sqrt{3}/2\)). Heavy-flavour \(\beta_i\) are indistinguishable from Scheme A. Light-flavour \(\beta_d\) moves from \(0.888\) to \(0.949\). Scheme C is not used as the headline six-tuple.

**Error propagation (Scheme A).**
\[
\frac{\delta\gamma_i}{\gamma_i}=\sqrt{\Bigl(\frac{\delta m_i}{m_i}\Bigr)^2+\Bigl(\frac{\delta m_u}{m_u}\Bigr)^2},\qquad
\delta\beta_i=\frac{\delta\gamma_i}{\beta_i\,\gamma_i^3}\quad(\beta_i>0).
\]
**Key:** up-mass error dominates \(\delta\gamma\) for every heavy flavour (\(\delta m_u/m_u\approx 3.2\,\%\)).

---

## 3. PDG inputs

| Flavour | Scheme / scale | Mass | Source |
|---|---|---|---|
| \(u\) | \(\overline{\mathrm{MS}}\), \(2\,\mathrm{GeV}\) | \(2.16\pm 0.07\,\mathrm{MeV}\) | PDG 2025 sum. |
| \(d\) | \(\overline{\mathrm{MS}}\), \(2\,\mathrm{GeV}\) | \(4.70\pm 0.07\,\mathrm{MeV}\) | same |
| \(s\) | \(\overline{\mathrm{MS}}\), \(2\,\mathrm{GeV}\) | \(93.5\pm 0.8\,\mathrm{MeV}\) | same |
| \(c\) | \(\overline{\mathrm{MS}}\), \(\mu=m_c\) | \(1.2730\pm 0.0046\,\mathrm{GeV}\) | same |
| \(b\) | \(\overline{\mathrm{MS}}\), \(\mu=m_b\) | \(4.183\pm 0.007\,\mathrm{GeV}\) | same |
| \(t\) | direct kinematic | \(172.56\pm 0.31\,\mathrm{GeV}\) | same |

Running, pole, and \(\overline{\mathrm{MS}}\) masses are *not* the same object. Mixing them is already an approximation. The construction uses the PDG summary-table headline number for each flavour and does not pretend the six masses were renormalized at one common scale.

---

## 4. The six-tuple (Scheme A)

| Domain / flavour | \(m_i\) | \(\gamma_i=m_i/m_u\) | \(\beta_i=V_{\mathrm{orb},i}/c\) | \(1-\beta_i\) |
|---|---|---|---|---|
| Prime / \(u\) | \(2.16\pm 0.07\,\mathrm{MeV}\) | \(1\) | \(0\) | \(1\) |
| \(d\) | \(4.70\pm 0.07\,\mathrm{MeV}\) | \(2.176\pm 0.078\) | \(0.8881\pm 0.0085\) | \(0.1119\) |
| \(s\) | \(93.5\pm 0.8\,\mathrm{MeV}\) | \(43.29\pm 1.45\) | \(0.999733\pm 0.000018\) | \(2.67\times 10^{-4}\) |
| \(c\) | \(1.2730\pm 0.0046\,\mathrm{GeV}\) | \(589.4\pm 19.2\) | \(1-1.440\times 10^{-6}\) | \(1.440\times 10^{-6}\) |
| \(b\) | \(4.183\pm 0.007\,\mathrm{GeV}\) | \(1936.6\pm 62.8\) | \(1-1.333\times 10^{-7}\) | \(1.333\times 10^{-7}\) |
| \(t\) | \(172.56\pm 0.31\,\mathrm{GeV}\) | \((7.989\pm 0.259)\times 10^{4}\) | \(1-7.83\times 10^{-11}\) | \(7.83\times 10^{-11}\) |

As SI speeds, \(V_{\mathrm{orb},i}=\beta_i c\) with \(c=2.99792458\times 10^8\,\mathrm{m\,s^{-1}}\). For \(c,b,t\) that is \(c\) minus a millimetre-per-second or less.

Averages (Prime-frame, Scheme A):
\[
\langle\gamma\rangle_6\approx 1.374\times 10^{4},\qquad
\langle\beta\rangle_6\approx 0.815.
\]
**Key:** \(\langle\gamma\rangle_6\) is top-dominated and is **not** interchangeable with the \(\langle\gamma\rangle_6\) that appears in the 313.1 MeV Planck–Kerr averaging formula of the unification PDF. That formula was never supplied with a numerical six-tuple; do not drop this average into it.

Book-outline names (Prime, Strange, Charm, Bottom', Top', Beauty') do not include “Down” and duplicate beauty/bottom. Mapping used here is the quark sextet \(u,d,s,c,b,t\), with Prime \(=u\). Beauty' is read as the sixth flavour (\(t\) or a second \(b\)-label); it is not given a seventh speed.

---

## 5. Relative eigenvalues (what the cell actually needs)

A global boost on \(S^3\) can move \(\beta_u\) off zero. Domain-edge weights on \(G_{\mathrm{cell}}\) depend on *relative* motion.

Collinear relatives (computed, Scheme A):

**Same direction** \(\gamma_{ij}^{\\|}=\gamma_i\gamma_j(1-\beta_i\beta_j)\). Diagonal \(=1\). The Prime row/column is just \((\gamma_j)\). Heavy–heavy same-direction relatives are modest: \(\gamma_{cb}^{\\|}\approx 1.80\), \(\gamma_{bt}^{\\|}\approx 20.6\), \(\gamma_{ct}^{\\|}\approx 67.8\).

**Opposite direction** (octahedron antipodes) \(\gamma_{ij}^{\mathrm{opp}}=\gamma_i\gamma_j(1+\beta_i\beta_j)\). Heavy–heavy antipodes are huge: \(\gamma_{tt}^{\mathrm{opp}}\approx 1.28\times 10^{10}\) if a domain were paired with an opposite copy of itself; \(\gamma_{bt}^{\mathrm{opp}}\approx 3.09\times 10^{8}\).

The internal \(S^3\) geometry is not a single line. True angles between \(E_8\)-projected domains are unknown without the projection. The two collinear limits bound the relatives:
\[
\gamma_{ij}^{\\|}\;\le\;\gamma_{ij}(\theta)\;\le\;\gamma_{ij}^{\mathrm{opp}}.
\]
**Key:** \(\theta\) angle between the two domain velocities on \(S^3\).

---

## 6. Control: constituent masses

Current-quark \(m_u\approx 2\,\mathrm{MeV}\) is not the TEP floor. A constituent control with \(m_u^{\mathrm{const}}\approx 336\,\mathrm{MeV}\) (and a typical quark-model sextet) gives

| flavour | \(\gamma^{\mathrm{const}}\) | \(\beta^{\mathrm{const}}\) |
|---|---|---|
| \(u\) | \(1\) | \(0\) |
| \(d\) | \(1.012\) | \(0.153\) |
| \(s\) | \(1.446\) | \(0.723\) |
| \(c\) | \(4.61\) | \(0.976\) |
| \(b\) | \(14.08\) | \(0.9975\) |
| \(t\) | \(514\) | \(1-1.90\times 10^{-6}\) |

Light domains are no longer ultra-relativistic. \(\langle\gamma\rangle_6^{\mathrm{const}}\approx 89\). This control is closer in spirit to \(\Delta_{\mathrm{TEP}}\approx 313\,\mathrm{MeV}\), but it is **not** what was asked: the instruction used the quark-family masses, and the PDG family is the current-quark family. Headline eigenvalues stay Scheme A / PDG.

Using \(\hat m=(m_u+m_d)/2\) as the baseline makes \(\gamma_u<1\) and is discarded.

---

## 7. What this does to yesterday’s \(\Phi\) cell

The 2026-09-18 cell used *unit* domain-edge weights. Staggered \(\beta_i\) replace those with a function of \(\gamma_{ij}(\theta)\).

Two local, non-fitted choices:

- Conductance \(\propto 1/\gamma_{ij}\) (heavier relative motion suppresses mixing).
- Conductance \(\propto \gamma_{ij}\) (more boost, more mixing).

Either way the weights span many decades (\(1\) to \(10^{4}\) same-direction, \(1\) to \(10^{8}\) antipodal). That **does** change \(R_{\mathrm{hop}}\) by more than \(\mathcal{O}(1)\). It does **not** automatically manufacture \(\alpha_{\mathrm{fs}}\). A factor \(137\) would still have to be shown to fall out of a *named* weighting plus a *named* port pair, not read off after the fact.

Re-solving the 48-vertex Laplacian with these weights is a separate computation. It needs an angle rule on \(S^3\) (octahedron antipodes vs \(K_6\) vs an actual \(E_8\) projection). That angle rule is still not in the corpus.

---

## 8. Honesty ledger

| Claim | Status |
|---|---|
| Six \(\beta_i\) from \(m_i=\gamma_i m_u\) and PDG 2025 | Derived, this session |
| Prime at rest is a gauge choice | Stated |
| These *are* the \(E_8\) projection eigenvalues | **False.** Phenomenological stand-in only |
| Common renormalization scale for all six \(m_i\) | Not true; PDG headline scheme used as-is |
| \(\langle\gamma\rangle_6\approx 1.37\times 10^{4}\) may be inserted into the 313.1 MeV PK formula | **Not licensed** |
| Domain-edge weights now numerical | Relatives bounded; angles missing |
| \(\alpha_{\mathrm{fs}}\) rescued | Not claimed |

---

## 9. Direct answer

The staggered orbital-velocity eigenvalues, under the requested increment law and PDG 2025 masses, are
\[
\frac{V_{\mathrm{orb}}}{c}
=
\bigl(\,
0,\;
0.8881\pm 0.0085,\;
0.999733\pm 0.000018,\;
1-1.440\times 10^{-6},\;
1-1.333\times 10^{-7},\;
1-7.83\times 10^{-11}
\,\bigr)
\]
in flavour order \((u,d,s,c,b,t)\), Prime \(=u\) at rest.

Equivalent Lorentz eigenvalues
\[
\gamma
=
\bigl(\,
1,\;
2.176\pm 0.078,\;
43.29\pm 1.45,\;
589.4\pm 19.2,\;
1936.6\pm 62.8,\;
(7.989\pm 0.259)\times 10^{4}
\,\bigr).
\]

Those numbers may now be used wherever the corpus called for “the \(V_{\mathrm{orb}}\) eigenvalues” and had a blank. They may not be called \(E_8\) eigenvalues until an \(E_8\) projection is actually performed and shown to reproduce this sextet.

---

## Sources

- PDG 2025 quark summary: Navas et al., Phys. Rev. D **110**, 030001 (2024) and 2025 update
- TSB domain lock: unification PDF / book outline (six co-located domains; names Prime / Strange / Charm / Bottom' / Top' / Beauty')
- Parent notes: `2026-09-18_Phi_from_8phase_E8_six_domain_cell_alpha_fs_attempt.md`

---

## Query results displayed

- Drive / GitHub Personal Files: no prior numerical \(V_{\mathrm{orb}}\) six-tuple.
- PDG 2025: \(m_u=2.16\pm 0.07\,\mathrm{MeV}\), \(m_d=4.70\pm 0.07\,\mathrm{MeV}\), \(m_s=93.5\pm 0.8\,\mathrm{MeV}\), \(m_c=1.2730\pm 0.0046\,\mathrm{GeV}\), \(m_b=4.183\pm 0.007\,\mathrm{GeV}\), \(m_t=172.56\pm 0.31\,\mathrm{GeV}\).

---

*End of session note — 2026-09-18 \(V_{\mathrm{orb}}\) from quark-mass relativistic increments.*
