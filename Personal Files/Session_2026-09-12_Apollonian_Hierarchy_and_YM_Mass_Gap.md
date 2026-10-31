# Session 2026-09-12 — Apollonian hierarchy tied to the geometric Yang–Mills mass gap

**Purpose:** Put the octant write, the optional Soddy foam, and the existing TSB mass-gap claim on one chain. Do not treat Hausdorff \(\delta\) as the gap.

**Depends on:**  
`Session_2026-08-20_Six_Numbers_142857_Cycle_Mass_Gap_Sequence.md`  
`Session_2026-09-12_3Ball_Tiling_Octant_Split.md`  
`Session_2026-09-12_Apollonian_Gasket_Investigation.md`  
`Session_2026-09-12_Apollonian_Hausdorff_Dimension_Numeric.md`

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(\Delta\) | Yang–Mills mass gap (smallest excitation energy above the vacuum of the bound sector) |
| \(\Delta_{\mathrm{Tav}}\) | TSB claimed geometric floor; corpus value \(313.1\,\mathrm{MeV}\) (input to this note, not output) |
| \(\Phi_7\) | Seventh-phase evaluation / Planckian-mirror scrape |
| PK-Mirron | Planck–Kerr mirror that implements \(\Phi_7\) |
| \(\ell_{\mathrm{PK}}\) | Characteristic radius of a PK-Mirron seed |
| \(\ell_{\mathrm{cap}}\) | Exhaustion cap of a first-generation envelope |
| \(\tau\) | Frozen KK fiber radius (lattice input) |
| \(S^1_\tau(x)\) | Bound compact fiber at written centre \(x\) |
| \(q=8\) | Locked octant daughter count |
| \(g_{\mathrm{oct}}\) | Number of octant generations |
| \(k=1/r\) | Soddy / Descartes curvature of an envelope sphere |
| \(k_{\mathrm{cap}}=1/\ell_{\mathrm{cap}}\) | Curvature of a cap-scale envelope |
| \(k_{\mathrm{PK}}=1/\ell_{\mathrm{PK}}\) | Curvature of a Mirron-scale sphere |
| \(K_{\mathrm{cut}}\) | Hierarchy cutoff in curvature |
| \(\delta_2,\delta_3\) | Residual-set Hausdorff dimensions (\(\approx 1.306\), \(\approx 2.474\)) |
| \(N_\tau\) | Survey-scale Tau-fiber count |
| \(N_{\mathrm{M}}^{\mathrm{(hier)}}\) | Hierarchical (sub-cap) Mirron count |
| \(\alpha\) | Anomalous dimension \(1-\log_7 6\approx 0.079218\) (corpus; not re-derived here) |
| \(n_{\mathrm{hier}}\) | Corpus logarithmic depth \(\log_7(\tau/\lambda_{\Delta})\) |
| \(\lambda_{\Delta}\) | Compton length associated with \(\Delta\) if one is formed |
| \(L\) | Residual angular momentum of a bounce stopped at Present |
| \(\mathcal{C}_{\mathcal{PF}}\) | Atemporal Past–Future circle |
| \(G\) | Number of Soddy generations from cap to PK |

---

## 2. What the TSB mass gap already is

The corpus does **not** set

\[
\Delta = \frac{\hbar c}{\tau}.
\]

That combination is \(\sim 10^{-30}\,\mathrm{eV}\) and is the KK gap of the survey fiber, not a hadronic gap.

The claimed geometric gap is the **exclusion cost of a \(\Phi_7\) scrape**: a bound bounce that tries to complete \(\mathcal{P}\to\mathcal{F}\) is stopped at the Planckian-mirror fabric. The stopped rebound deposits residual \(L\). The smallest stable deposit is \(\Delta\).

In that language:

\[
\Delta
=
\min
\bigl\{\,
E
\;\big|\;
K(\mathcal{P},\mathcal{N})\text{ exists and }K(\mathcal{P},\mathcal{F})\text{ does not}
\,\bigr\}.
\]

**Key:** \(E\) = energy of the stopped bounce; \(K(\mathcal{P},\mathcal{N})\) = kernel truncated at Present; \(K(\mathcal{P},\mathcal{F})\) = completed unbound kernel.

The number \(313.1\,\mathrm{MeV}\) is the corpus identification of that minimum with the constituent-quark / glueball-adjacent IR floor. It is **not** produced by the Apollonian fit \(\delta_{\mathrm{fit}}=1.302\), and it is not produced by \(q=8\).

---

## 3. Three scales, three packings

| Scale | Geometric object | Count rule |
|-------|------------------|------------|
| Survey cell | Envelope that hits \(\ell_{\mathrm{cap}}\) | Octant split \(N_\tau=8^{g_{\mathrm{oct}}}\) |
| Interstitial / interior foam | Unequal tangent spheres | Soddy recursion; \(N_{\mathrm{M}}^{\mathrm{(hier)}}\sim K^{\delta_3}\) |
| Gap floor | PK-Mirron / \(\Phi_7\) scrape | One smallest allowed stopped bounce |

Yang–Mills in this picture is the **bound-sector spectrum inside a cell**, not the survey lattice. Glueball-like excitations are hierarchical Mirrons: bound envelopes that never reach \(\ell_{\mathrm{cap}}\). The gap is the **bottom** of that tower, not the Hausdorff dimension of the residual set.

\(\delta_2\) and \(\delta_3\) tell how the *number* of sub-cells grows as the radius cutoff is lowered. They do not have dimension of energy.

---

## 4. Where Apollonian meets the gap

Seed a Soddy packing with the cap container (negative curvature) plus the eight octant daughters:

\[
k_0 = -\frac{1}{\ell_{\mathrm{cap}}},
\qquad
k^{(8)} = \frac{2}{(\sqrt{3}-1)\ell_{\mathrm{cap}}}.
\]

**Key:** \(k_0\) = bounding envelope; \(k^{(8)}\) = equal-daughter curvature from the octant lock.

Further spheres:

\[
k_{n+1}
=
\sum_{j\in T}k_j
\pm
2\sqrt{\sum_{i<j\in T}k_ik_j}.
\]

**Key:** \(T\) = an already tangent 4-tuple.

The hierarchy runs until a sphere reaches the Mirron scale:

\[
k \le K_{\mathrm{cut}}
\quad\text{with the working identification}\quad
K_{\mathrm{cut}} = k_{\mathrm{PK}} = \frac{1}{\ell_{\mathrm{PK}}}.
\]

**Key:** \(K_{\mathrm{cut}}\) is named as the PK curvature, not as \(1/\lambda_{\Delta}\) unless a separate Compton map is written.

Number of Soddy generations from cap to PK is logarithmic in the radius ratio:

\[
G
\sim
\log
\Bigl(
\frac{\ell_{\mathrm{cap}}}{\ell_{\mathrm{PK}}}
\Bigr)
\Big/
\log b,
\]

**Key:** \(b>1\) = typical Descartes magnification of curvature per generation (order a few; packing-dependent, not \(7\) unless inserted).

The corpus depth

\[
n_{\mathrm{hier}}
=
\log_7\Bigl(\frac{\tau}{\lambda_{\Delta_{\mathrm{Tav}}}}\Bigr)
\approx 45.8
\]

**Key:** uses base \(7\) and both \(\tau\) and \(\Delta_{\mathrm{Tav}}\) as inputs.  
That is a **register of the same logarithmic depth**, not a derivation of \(\Delta\). Replacing base \(7\) by the Descartes factor \(b\) changes the integer label of \(G\); it does not compute MeV.

---

## 5. Spectrum statement (geometric, not QCD Lagrangian)

Inside one survey cell, after option-B packing:

- Vacuum of the bound sector = no extra Soddy sphere above the PK floor.  
- First excitation = smallest allowed sphere with \(k < k_{\mathrm{PK}}\) forbidden; next discrete Soddy root above \(k_{\mathrm{PK}}\) is the first massive mode.  
- Higher modes = the integral (or real) Descartes tower.  
- Continuum / glueball band = dense large-\(k\) foam with counting dimension \(\delta_3\).

Then the mass gap is

\[
\Delta
=
E\bigl[k_{\mathrm{first}}>k_{\mathrm{PK}}\bigr]
-
E\bigl[k_{\mathrm{PK}}\bigr].
\]

**Key:** \(E[k]\) = energy assigned to a hierarchical Mirron of curvature \(k\).

This equation is empty until \(E[k]\) is defined. Legal definitions that do **not** smuggle \(\Delta_{\mathrm{Tav}}\) onto the right-hand side:

1. \(E[k]\) from residual \(L\) of the stopped bounce on that envelope (clockwork output of \(\Phi_7\)).  
2. \(E[k]\) from the holonomy deficit \(\mathrm{Hol}_\tau\) evaluated on that small fiber, if a small fiber is written.

Illegal: \(E[k]=\hbar c\,k\) identified with \(313.1\,\mathrm{MeV}\) by choosing \(k\). That is matching.

---

## 6. What Hausdorff \(\delta\) contributes

Numeric 2D result of this session: \(\delta_{\mathrm{fit}}=1.302\) vs \(\delta_2^{\mathrm{lit}}=1.305686728\) (\(0.25\%\)).

Use:

\[
N_{\mathrm{M}}^{\mathrm{(hier)}}(K)
\sim
c\,K^{\delta_3}.
\]

**Key:** inventory of sub-cap Mirrons below curvature \(K\).

Do not use:

\[
\Delta \stackrel{?}{=} \delta_2\cdot(\text{anything in MeV}).
\]

\(\delta\) is dimensionless. The gap is an energy.

---

## 7. Full chain (Past → cell → foam → floor)

\[
\mathcal{C}_{\mathcal{PF}}
\;\xrightarrow{\Phi_7}\;
\text{PK-Mirron floor }(\Delta)
\;\xrightarrow{\text{Soddy}}\;
\text{hierarchical Mirrons inside a cell}
\;\xrightarrow{\text{octant }q=8}\;
\text{survey }S^1_\tau\text{ lattice}
\;\xrightarrow{R_{\mathrm{EH}}}\;
\text{nodes leave at }\mathcal{F}.
\]

**Key:** \(\mathcal{C}_{\mathcal{PF}}\) = atemporal cylinder; \(R_{\mathrm{EH}}\) = event horizon.

Yang–Mills lives on the first two arrows (floor + foam).  
Large-scale structure lives on the last two.  
\(\tau\) labels the survey fiber. It is not the gap.

---

## 8. Status

| Claim | Status |
|-------|--------|
| \(\Delta\) = \(\Phi_7\) exclusion / smallest stopped bounce | standing TSB identification |
| \(\Delta_{\mathrm{Tav}}=313.1\,\mathrm{MeV}\) | corpus number; **not** derived from \(\delta\) or from \(q=8\) |
| Apollonian foam = bound spectrum above the floor | optional geometric model |
| \(N_\tau=8^{g_{\mathrm{oct}}}\) | locked survey count |
| \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_\Delta)\) | bookkeeping of depth; circular if used to get \(\Delta\) |
| True derivation of \(\Delta\) | still requires \(E[k]\) from \(\Phi_7\) with empty MeV RHS |

---

## 9. Next calculation that would actually move the gap

Write \(\Phi_7\) as an explicit \(8\times 8\) real matrix. Take the smallest positive eigenvalue (or the associator norm on one Fano triple) as a *dimensionless* gap \(\hat\Delta\). Only then form

\[
\Delta = \hat\Delta\cdot E_{\mathrm{PK}}
\]

**Key:** \(E_{\mathrm{PK}}\) = energy unit of the Planck–Kerr seed, named from the seed geometry, not from \(313.1\). Compare to \(313.1\,\mathrm{MeV}\) after the fact.

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
