# Session 2026-09-14 — Convert 313 MeV “glueball” to gluon inertial energy on the quark

**Source under review:** Wylde video / sketch “Yang-Mills Mass Gap via Superblock Theory’s Planckian Mirrors” (2025-11-25), claiming \(\Delta=313\,\mathrm{MeV}\) as a \(0^{++}\) glueball and as the YM gap.

**Task:** Convert that number to the inertial energy of the gluon field transmitted to a quark (or as one share of a glueball).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(\Delta\) | Geometric floor (stopped-bounce / \(\Phi_7\) exclusion) |
| \(\Delta_{\mathrm{Tav}}\) | Corpus value \(313.1\,\mathrm{MeV}\) |
| \(M_{0^{++}}\) | Lightest scalar glueball mass |
| \(E_g\) | Inertial energy of one bound gluon quantum |
| \(n_g\) | Number of such quanta in a glueball |
| \(V_{\mathrm{bind}}\) | Binding correction (negative if bound) |
| \(m_q^{\mathrm{curr}}\) | Current-quark mass (few MeV for \(u,d\)) |
| \(m_q^{\mathrm{const}}\) | Constituent mass seen by the hadron |
| \(E_{q\leftarrow g}\) | Energy transmitted from the gluon field to one quark |
| \(\Phi_7\) | Seventh-phase scrape |
| \(L\) | Residual angular momentum of a stopped bounce |
| \(M_{\mathrm{PK}}\) | Planck–Kerr seed mass (sketch input) |
| \(\gamma,N_{\mathrm{dom}}\) | Sketch “domain drift” factors |
| \(\sqrt{\sigma}\) | QCD string tension scale |

---

## 2. What the sketch actually computes vs what it names

The sketch writes two different things as “313 MeV”:

1. A scaling  
   \(m_{\mathrm{QCD}}=m_{\mathrm{tors}}e^{-\gamma N_{\mathrm{dom}}}\)  
   with \(N_{\mathrm{dom}}=3\), \(\gamma=1.0607\). That is an **input exponential**, not an index theorem output.  
2. A flux formula \(\sqrt{\Phi_\tau/A_{\min}}\) also said to equal 313 MeV.

The Fredholm step, if taken at face value, only argues \(\inf\mathrm{spec}>0\). It does not output MeV. Index \(240\) is a dimension count, not a mass.

Lattice QCD (quenched) puts the lightest \(0^{++}\) glueball at \(\sim 1.6\)–\(1.7\,\mathrm{GeV}\), not \(313\,\mathrm{MeV}\). Naming 313 MeV a glueball **contradicts that spectrum**. The number sits at the constituent-quark / IR-dressing scale, which is the older TSB reading.

---

## 3. Conversion (requested)

Treat \(\Delta_{\mathrm{Tav}}\) as the inertial energy of **one** bound gluon quantum — the stopped colour bounce on a PK-Mirron — not as \(M_{0^{++}}\).

\[
E_g
=
\Delta_{\mathrm{Tav}}
=
313.1\,\mathrm{MeV}.
\]

**Key:** \(E_g\) = inertial energy stored in one bound gluon field quantum.

Transmitted to a light quark (dressing):

\[
E_{q\leftarrow g}
=
E_g,
\qquad
m_q^{\mathrm{const}}
=
m_q^{\mathrm{curr}}
+
E_{q\leftarrow g}.
\]

**Key:** current mass stays a few MeV; almost all of the constituent mass is the gluon inertial deposit.

For \(u,d\): \(m_q^{\mathrm{const}}\approx 315\)–\(318\,\mathrm{MeV}\) if \(m^{\mathrm{curr}}\approx 2\)–\(5\,\mathrm{MeV}\).

A glueball is \(n_g\) such quanta plus binding:

\[
M_{0^{++}}
=
n_g\,E_g
+
V_{\mathrm{bind}}.
\]

**Key:** \(n_g\) = gluon occupancy of the \(0^{++}\); \(V_{\mathrm{bind}}\le 0\) if the quanta attract.

If \(V_{\mathrm{bind}}=0\) (accounting identity, not a potential model):

| \(n_g\) | \(n_g\times 313.1\,\mathrm{MeV}\) | Comparison |
|--------|-------------------------------|-------------|
| 1 | \(313.1\) | dressing quantum; **not** a glueball |
| 2 | \(626.2\) | too light for \(0^{++}\) |
| 3 | \(939.3\) | nucleon ballpark, not glueball |
| 5 | \(1565.5\) | quenched \(0^{++}\) \(\sim 1.6\,\mathrm{GeV}\) |
| 8 | \(2504.8\) | near tensor \(2^{++}\sim 2.4\,\mathrm{GeV}\) |

The conversion that matches lattice without renaming PDG is:

\[
E_g=\Delta_{\mathrm{Tav}},
\qquad
M_{0^{++}}\simeq 5\,E_g
\quad(V_{\mathrm{bind}}\approx 0).
\]

**Key:** five dressing quanta, not one resonance at 313 MeV.

Five is a **matching integer**, not derived here from \(E_8\). Eight (clockwork) overshoots the scalar and is closer to the tensor if \(V_{\mathrm{bind}}\) is a few hundred MeV downward.

---

## 4. Relation to the sketch’s LHC prediction

“Excess glueball at 313 MeV in U+U” is the wrong channel if \(E_g\) is the quantum. Search objects:

- **Dressing / threshold:** structures or excess near \(2E_g\approx 626\,\mathrm{MeV}\) or \(3E_g\approx 939\,\mathrm{MeV}\) (multiplicity of stopped gluons on quarks), not a narrow \(0^{++}\) at 313.  
- **True glueball:** still the \(1.5\)–\(1.7\,\mathrm{GeV}\) scalar region.  
- Predicting a new \(0^{++}\) at 313 MeV is already in conflict with the established glueball window.

Sterile mixing \(\varepsilon_\nu\sim 10^{-6}\) is a separate claim; unused in this conversion.

---

## 5. Status relative to this thread

| Item | Status |
|------|--------|
| \(\Delta\) as \(\Phi_7\) stopped-bounce floor | kept |
| \(\Delta\) as \(M_{0^{++}}\) | rejected (lattice) |
| \(\Delta=E_g=E_{q\leftarrow g}\) | working conversion |
| \(M_{0^{++}}\simeq 5E_g\) | phenomenological match, not a derivation |
| Sketch index \(\Rightarrow 313\,\mathrm{MeV}\) | not established |
| Exponential \(e^{-\gamma N_{\mathrm{dom}}}\) | inserts the IR scale |

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
