# Attempt to derive \(m_0\)

**Date:** 2026-09-20  
**Constraint:** live frame only. No \(\tau\), no \(S^1_\tau\), no fitted exponent dressed as geometry.  
**Result:** no derivation. Two identifications, one near miss, one phenomenology.

---

## 0. What would count

A derivation is a formula

\[
m_0
=
M_{\rm Pl}\,
F(\text{F7, B_lin, }h,\{m_j\},|W|)
\]

with \(F\) fixed by the algebra, no extra real parameter. \(m_0=313.1\,\mathrm{MeV}\) and \(\lambda_{m_0}=0.6302\,\mathrm{fm}\) are the same input (\(\hbar c/\lambda_{m_0}\)). Deriving one derives the other.

**Key.** \(M_{\rm Pl}=1.22089\times 10^{19}\,\mathrm{GeV}\). \(h=30\). \(|W(E_8)|=696729600\).

---

## 1. Integers do not make MeV

\[
\frac{M_{\rm Pl}}{m_0}
=
3.899\times 10^{19},
\qquad
\ln\frac{M_{\rm Pl}}{m_0}
=
45.110.
\]

Group powers:

| formula | value |
|---|---|
| \(M_{\rm Pl}/\|W\|\) | \(1.75\times 10^{16}\,\mathrm{MeV}\) |
| \(M_{\rm Pl}/\|W\|^2\) | \(25.15\,\mathrm{GeV}\) |
| \(M_{\rm Pl}/\|W\|^3\) | \(3.6\times 10^{-5}\,\mathrm{MeV}\) |
| \(M_{\rm Pl}/h^{13}\) | \(766\,\mathrm{MeV}\) |
| \(M_{\rm Pl}/h^{14}\) | \(25.5\,\mathrm{MeV}\) |
| \(M_{\rm Pl}\,e^{-2\ln\|W\|}\) | \(25.15\,\mathrm{GeV}\) |
| \(M_{\rm Pl}\,e^{-45}\) | \(349\,\mathrm{MeV}\) |

Nothing in that table is \(313.1\,\mathrm{MeV}\). \(e^{-45}\) is the nearest exponential, and \(45=\dim\mathfrak{so}(10)\), which F7 does not select. Using it would be a new freeze, not a derivation from the live one. \(h^{13}\) is in the ρ region, not the floor.

B_lin’s \(\gamma\)-sum \(5.4015\) and Weight-6 amplitude \(R=2.328\) are dimensionless. Multiplying them into the table does not land on \(313.1\).

**There is no live-algebra formula for \(m_0\).**

---

## 2. Identification A — Compton tautology

\[
m_0
=
\frac{\hbar}{\lambda_{m_0}c}
\]

is the definition of the kernel’s UV length. It is not a derivation.

---

## 3. Identification B — nucleon third

\[
\frac{m_n}{3}=313.188\,\mathrm{MeV},
\qquad
\frac{m_p}{3}=312.757\,\mathrm{MeV}.
\]

The quoted floor \(313.1\,\mathrm{MeV}\) *is* the neutron third to the quoted digits. That is a phenomenological name: constituent-quark / IR-QCD scale. It becomes a Superblock theorem only if the kernel’s floor is proved to be the three-quark mass. Six domains do not by themselves make a factor \(1/3\). Not a derivation.

---

## 4. Paths that could still derive it (open)

1. **Emergent YM gap.** If Planck–Kerr / Mirron produces a Yang–Mills theory whose mass gap equals \(m_0\), that is the derivation. It is the Millennium problem. Not done.
2. **Extremal ring mode.** Lowest standing wave on the shared Kerr ring, \(m=n\hbar c/(\alpha a)\), with \(a\) the ring radius. Needs \(a\) from geometry. Live frame leaves \(R_{\rm int}\) unnamed. Setting \(a\sim\ell_{\rm Pl}\) gives \(M_{\rm Pl}\), not \(313\,\mathrm{MeV}\).
3. **New freeze.** Replace or extend F7 so that \(\ln(M_{\rm Pl}/m_0)\) is an integer the group actually owns. That is a different frame.
4. **Leave the floor.** Honest default of the live paper.

---

## 5. Decision for the standing theory

\(m_0\) stays an IR floor. Today’s calculation shows why: F7 and B_lin have no MeV. Do not write \(m_0=M_{\rm Pl}\,e^{-\dim\mathfrak{so}(10)}\) or \(m_0=m_N/3\) as if they were theorems. The first is a different group. The second is QCD phenomenology.

---

## Master key

| Symbol | Role |
|---|---|
| \(m_0,\lambda_{m_0}\) | same input, two units |
| \(M_{\rm Pl},h,\|W\|\) | only dimensionful and integer data available |
| \(m_N/3\) | numerical name of the quoted floor, not a proof |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_derive_m0_2026-09-20.md`
