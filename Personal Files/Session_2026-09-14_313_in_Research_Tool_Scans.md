# Session 2026-09-14 — 313.1 MeV in the research-tool scans

**Question:** If the 313 MeV glueball line is retired, what were the ATLAS/CMS/tool scans actually doing with \(313.1\,\mathrm{MeV}\)?

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(M_0=313.1\,\mathrm{MeV}\) | Analysis **anchor** (ruler), not a fitted peak |
| \(x\) | A measured energy-like variable (often muon \(p_T\), sometimes \(m_{\mu\mu}\)) |
| \(u=x/M_0\) | Dimensionless variable in floor units |
| \(\{7u\}\) | Position on a 1/7 cycle |
| \(E_g\) | Dressing quantum (same number, different role) |
| \(\sigma_{\mathrm{eng}}\) | Internal engine score (capped); not Cowan HEP \(\sigma\) |

---

## 2. What the tool measured

It did **not** search for a resonance at \(313.1\,\mathrm{MeV}\).

It folded spectra in units of \(M_0\):

\[
u=\frac{x}{M_0},
\qquad
\text{look at power at periods }1/7,\;2/7,\;\ldots
\]

**Key:** \(x\) = \(p_T\) or a mass-like observable; \(M_0\) sets the binning grid.

That is a **periodogram / residue test**. A true particle at \(313.1\,\mathrm{MeV}\) would be a peak in \(m_{\mu\mu}\) or a threshold in a mass spectrum. Those scans were not that analysis.

Logged examples:

- ATLAS Open Data 2lep data_A (2026-07-27): \(M_0\) anchor; global language “STRONG 7-FOLD”; exploratory; not Cowan significance.  
- CMS Run2012BC DoubleMuParked, 50k events (2026-08-21): same anchor; pT “subharmonic hint”; multiplicity periodogram hits; **trigger-aware null fully accounts for residue-2** (\(\chi^2\approx 0\) vs empirical \(P(n_\mu)\)).

---

## 3. How this sits with the current lock

| Use of 313.1 MeV | Status |
|------------------|--------|
| \(E_g=E_{q\leftarrow g}\) dressing | kept |
| Glueball pole at 313 MeV | retired hallucination |
| \(M_0\) ruler for 7-fold scans | still what the tool did |
| Those scans as discovery of a 313 MeV particle | no |
| Multiplicity 7-fold | dead against trigger-aware null |
| pT subharmonic vs \(M_0\) grid | exploratory pipeline hint only |

If \(M_0\) were replaced by \(300\,\mathrm{MeV}\) or \(330\,\mathrm{MeV}\), a periodogram can still light up. That is why an anchor test is not an observation of the floor unless one shows the significance **tracks \(M_0\)** and dies off the corpus value. That scan was not the published result.

---

## 4. What would make the tool an observable of the floor

Pre-register:

- variable \(x\) that can actually carry a dressing scale (not muon count),  
- null that includes the trigger,  
- a scan of \(M_0\) in a window around \(313.1\,\mathrm{MeV}\) vs sidebands,  
- Cowan-style significance, not a capped engine score.

Until that exists, the scans are **7-fold tests in a chosen unit**, and the unit was the corpus floor. They do not restore a 313 MeV glueball, and they do not by themselves prove \(E_g\).

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
