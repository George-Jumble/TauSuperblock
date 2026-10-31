# Superblock-only recalculation of Kuhn et al. (2024)
## Gatlin Tau / Tav layer removed (treated as falsified)

**Paper:** Kuhn et al., arXiv:2312.12389, *ApJL* 967, L15 (2024)  
**This note:** 2026-09-21 Superblock-only rewrite  
**Supersedes, for live use:**  
- `2026-09-18_TSB_analysis_Kuhn_JWST_spirals_2312.12389.md`  
- `2026-09-21_TSB_recalc_Kuhn_JWST_spirals_2312.12389.md` (those two mixed in Tau)  

**Corpus lock.** Live geometry is Superblock Theory / Mirron (William Brown / Wylde). Gatlin Tau Universe / Tav Topology — compact \(S^1\) of radius \(\tau=7\,h^{-1}\,\mathrm{Mpc}\), \(\Delta k=0.142857\,h\,\mathrm{Mpc^{-1}}\) KK comb, RGC as cosmological backend, \(n=\log_7(\tau/\lambda_{313})\), conformal exhaustion at \(7\,h^{-1}\,\mathrm{Mpc}\) — is **out**. JADES+DESI searches for that comb were already null at the sensitivity of 29 Mar 2026; the present instruction is to treat the Tau layer as falsified and not to rebuild Kuhn on it.

**Vocabulary.** Mirron, never soliton. A Mirron is a sub-quantum reflection of an entire aeon — the fractal landscape of the Superblock (PK / Mirron engines, Planckian mirrors).

---

## 0. What was stripped

| Removed (Gatlin Tau / Tav) | Kept (Superblock / Mirron) |
|---|---|
| \(\tau=7\,h^{-1}\,\mathrm{Mpc}\) compact fifth dimension | Six co-located \(3+1\)D domains on an internal \(S^3\) supersphere |
| \(P_{142857}\) / \(1/7\) as a cosmological projector from \(\tau\) | \(\mathrm{E}_8\)-projected staggered \(V_{\mathrm{orb}}^{(a)}\) |
| RGC / Tav graph as the engine of disks | Twistor-mediated conformal gravity; time-averaged coupling |
| Hierarchical BEC exhausting at \(7\,\mathrm{Mpc}\) walls | Emergent DM = gravitational shadow of five hidden domains |
| \(n=\log_7(\tau/\lambda_{313})\) as a galactic rung index | Softened Kerr-seed / phase-hidden **cored** profiles |
| Casimir \(w\equiv-1\) from a macroscopic \(S^1\) | Dynamic Refresh at PK / Mirron engines |
| FRB “Tau wall impedance” as architecture | \(m_0\approx 313.1\,\mathrm{MeV}\) as an SB geometric floor (Up-quark / PK conformal average; derived *before* the Tau merge) |
| “TSB unification” as Tau-backend + SB-UI | SGHB from Planckian mirrors upward |
| JWST/Rubin 7-fold *cosmological* harmonic gate tied to \(\tau\) | CCC bounce in original Superblock / conformal-aeon + Mirron form |
| | Cosmic dipole as a domain-orbit observable |
| | Color \(\leftrightarrow\) EM phase inversion across domains |

Octonionic 8-phase clockwork is kept only as Superblock block structure on the PK / Mirron tick (causality-safe CTCs inside the ergosphere). It is **not** re-derived from a 7 Mpc circle.

---

## 1. Kuhn numbers (observational layer; unchanged)

873 CEERS galaxies, \(M_\star\ge 10^{10}\,M_\odot\), \(0.5\le z\le 4\), six inspectors, rest-frame \(V\). 216 spirals.

| Layer | Value |
|---|---|
| Raw \(f_{\mathrm{obs}}\) | \(48\%\) at \(z\sim 0.75\) \(\to\) \(8\%\) at \(z\sim 2.75\) |
| Forward-model \(f_{\mathrm{int}}\) at \(z=2\)–\(3\) | \(\sim 35\%\) (median \(\sim 40\%\), flat to \(z\approx 2.75\)) |
| \(z\sim 3\) exclusions | \(<20\%\) out at \(2\sigma\); \(<10\%\) out at \(3\sigma\) |
| Correlates | spirals larger, higher SFR |
| Tail systematic | sample tail fraction \(5.8\)–\(10.2\%\) at \(z=2\)–\(3\) can pull \(z\sim 3\) toward \(\sim 20\%\) |

Shared time axis only (\(H_0=70\), \(\Omega_m=0.3\)):

\[
t_{\mathrm{age}}(z)=\frac{1}{H_0}\int_z^{z_{\max}}\frac{\mathrm{d}z'}{(1+z')E(z')},\qquad
E(z)=\sqrt{\Omega_m(1+z)^3+\Omega_\Lambda}.
\]

**Key.** \(t_{\mathrm{age}}\): comparison-metric age of the present aeon. \(E(z)\): normalized Hubble function. \(z_{\max}\): radiation-era cutoff of the integral.

| \(z\) | \(t_{\mathrm{age}}\) | Kuhn layer |
|---|---|---|
| \(0.75\) | \(6.89\,\mathrm{Gyr}\) | raw \(48\%\) |
| \(2.75\) | \(2.32\,\mathrm{Gyr}\) | raw \(8\%\); \(f_{\mathrm{int}}\) still flat |
| \(3.00\) | \(2.11\,\mathrm{Gyr}\) | \(2\sigma\) floor \(\ge 20\%\) |
| \(4.00\) | \(1.52\,\mathrm{Gyr}\) | their hot-gas-disk epoch |

\[
t_{\mathrm{settle}}(M_\star\gtrsim 10^{10}\,M_\odot)\;\le\; t_{\mathrm{age}}(z\approx 3)\;\approx\; 2.11\,\mathrm{Gyr}.
\]

**Key.** \(t_{\mathrm{settle}}\): time to a spiral-capable stellar sheet.

---

## 2. Superblock gravity on a disk

### 2.1 Architecture

Six domains share Prime’s macroscopic \((t,\vec{x})\) and differ by orbital velocity on the internal \(S^3\). EM does not couple across domains (causal separation). Gravity does, as a twistor-space conformal average.

Hidden-domain mass appears in Prime as a cold, collisionless shadow. Cosmic mean:

\[
\frac{\Omega_{\mathrm{DM}}}{\Omega_b}\;\approx\; 5.2 \;=\; \sum_{i=1}^{5}\gamma_i,
\qquad
\gamma_i=\bigl(1-V_{\mathrm{orb}}^{(i)\,2}/c^2\bigr)^{-1/2}.
\]

**Key.** \(\Omega_{\mathrm{DM}}\): effective shadow density in Prime. \(\Omega_b\): Prime baryons. \(\gamma_i\): Lorentz factor of hidden domain \(i\). \(V_{\mathrm{orb}}^{(i)}\): \(\mathrm{E}_8\)-projected orbital speed of that domain. \(c\): Prime light speed. This note does not invent a \(V_{\mathrm{orb}}\) table to force \(5.2\).

Locally the shadow is a **cored softened Kerr-seed / phase-hidden Mirron profile**, not an NFW cusp:

\[
V_{\mathrm{obs}}^2(R)=V_b^2(R)+V_{\mathrm{shadow}}^2(R),
\qquad
V_{\mathrm{shadow}}^2(R)=G_{\mathrm{N}}\frac{M_{\mathrm{Kerr-soft}}(<R)}{R}.
\]

**Key.** \(V_{\mathrm{obs}}\): observed circular speed. \(V_b\): Newtonian baryons (stars+gas). \(V_{\mathrm{shadow}}\): time-averaged hidden-domain contribution. \(M_{\mathrm{Kerr-soft}}(<R)\): enclosed mass of the cored Kerr-seed profile. \(G_{\mathrm{N}}\): Newton constant in Prime. \(R\): cylindrical radius.

Because the profile is cored,

\[
\lim_{R\to 0}\frac{M_{\mathrm{Kerr-soft}}(<R)}{M_b(<R)}\;\ll\; 5.2.
\]

**Key.** Inner optical disk can be baryon-dominated while the sky-mean ratio stays \(5.2\). That is the Superblock reading of ceers-2112 and of Kuhn’s large, high-SFR spirals.

Do **not** put \(6.2\,G_{\mathrm{N}}\) into Toomre. That was a Tau-merge habit (copy the cosmic ratio into local \(G\)). Superblock does not say that.

### 2.2 Why the well is already there at \(z\sim 3\)

Dynamic Refresh: Prime baryons and the conformal average are re-projected from PK / Mirron engines on the 8-phase tick. The five hidden domains are co-located *now*, at every \(z\). There is no WIMP merger tree that has to finish before the sheet feels a deep, organized well.

So \(t_{\mathrm{settle}}\) is a **cooling + sheet-selection** time, not a **halo-assembly** time. That is the Superblock answer to Kuhn’s \(2.11\,\mathrm{Gyr}\) budget.

### 2.3 Toomre, Superblock inputs only

\[
Q=\frac{\sigma_R\,\kappa}{\pi G_{\mathrm{N}}\Sigma},
\qquad
\kappa^2=R\frac{\mathrm{d}\Omega^2}{\mathrm{d}R}+4\Omega^2,
\qquad
\Omega=\frac{V_{\mathrm{obs}}}{R}.
\]

**Key.** \(Q\): Toomre parameter (\(Q\lesssim 1\) opens swing amplification). \(\sigma_R\): radial velocity dispersion. \(\kappa\): epicyclic frequency. \(\Sigma\): baryonic surface density of the sheet.

Superblock changes the inputs:

1. \(\sigma_R\) lower — no cusp heating, no required major-merger halo construction.  
2. \(\kappa\) more coherent — specific angular momentum inherited from \(\{V_{\mathrm{orb}}^{(a)}\}\), not a random tidal-torque draw.  
3. \(\Sigma\) organized into a thin sheet earlier — SGHB binds upward from PK / Mirron engines.

\[
\frac{Q_{\mathrm{SB}}}{Q_{\Lambda}}
=
\left(\frac{\sigma_{R,\mathrm{SB}}}{\sigma_{R,\Lambda}}\right)
\left(\frac{\kappa_{\mathrm{SB}}}{\kappa_{\Lambda}}\right)
\left(\frac{\Sigma_{\Lambda}}{\Sigma_{\mathrm{SB}}}\right).
\]

**Key.** SB vs \(\Lambda\): same baryonic galaxy in the Superblock well vs in a late-assembled NFW well.

Working interval only (\(\sigma\) halved, \(\kappa+10\%\), thin \(\Sigma+20\%\)):

\[
\frac{Q_{\mathrm{SB}}}{Q_{\Lambda}}\;\sim\; 0.46.
\]

Enough to open arms while ΛCDM still wants clumps. Not a derivation of \(f_{\mathrm{int}}=35\%\).

### 2.4 SPARC end of the same object

\[
g_{\mathrm{obs}}(R)=\frac{V_{\mathrm{obs}}^2}{R},
\qquad
g_b(R)=G_{\mathrm{N}}\frac{\partial\Phi_b}{\partial R}.
\]

**Key.** \(g_{\mathrm{obs}}\): observed centripetal acceleration. \(g_b\): baryonic acceleration. \(\Phi_b\): Newtonian baryonic potential.

Live Superblock claim: \(g_{\mathrm{obs}}(g_b)\) regularity plus Kerr-seed cores already at \(z\sim 2\)–\(3\) in Kuhn’s spiral subsample. Particle CDM plus late assembly wants more scatter and more cuspy inner \(g_{\mathrm{obs}}\) at that epoch. This is the highest-leverage follow-up. It does not use \(\tau\).

---

## 3. Hierarchical binding without a 7 Mpc wall

\[
\mathcal{B}_{n+1}=\mathcal{H}(\mathcal{B}_n;\mathcal{M}).
\]

**Key.** \(\mathcal{B}_n\): bound structure at hierarchy level \(n\) (PK / Mirron engine \(\to\) cloud \(\to\) galactic sheet \(\to\) group). \(\mathcal{H}\): hierarchical binding map. \(\mathcal{M}\): Mirron landscape. \(n\) here is an ordinary hierarchy index, **not** \(\log_7(\tau/R)\).

A \(z\sim 3\) spiral is a sheet that has already bound, in a universe \(2.11\,\mathrm{Gyr}\) old on the shared axis. Mergers perturb it. They do not have to build it. Residual \(f_{\mathrm{int}}\gtrsim 20\%\) after tail subtraction is what SGHB wants. A near-zero spiral population at \(z\sim 3\) would still be a Superblock problem.

There is **no** Superblock requirement that filaments cut at \(7\,h^{-1}\,\mathrm{Mpc}\), and no FRB wall-toll prediction attached to Kuhn.

---

## 4. Arms

Lin–Shu, swing amplification, tides, bars stay. Superblock adds a substrate: the arm is a crest of \(\Sigma(\theta)\) sitting on a Mirron sheet (aeonic reflection), not a hydrodynamic soliton and not a Tav \(1/7\) mode.

Do **not** predict seven-armed galaxies. Local grand design is two-armed; that would already be dead.

Do **not** stack a \(P_{142857}\) Fourier test as a Superblock necessity. That test belonged to the Tau comb. If a later SB-native pitch lock (golden-ratio / \(\mathrm{E}_8\)-projected angles) is derived from the supersphere geometry alone, that is a new calculation. It is not in Kuhn and it is not inherited from \(\tau\).

Optional CCC / Mirron memory: a Mirron can pass *geometry* through a conformal aeon crossover. It cannot pass a baryonic arm. Use that layer only if pitch or PA data demand a leftover template. Kuhn’s *fraction* does not require it.

---

## 5. Consistency check that is allowed — numerology that is not

Do not write \(f_{\mathrm{int}}=1/7\), \(2/6\), or \(\varphi^{-1}\). Those were Tau-merge numerology.

Allowed bookkeeping only:

\[
f_{\mathrm{int}}(z)\;\approx\; f_{\mathrm{disk}}(z)\times f_{\mathrm{spiral}|\mathrm{disk}}.
\]

**Key.** \(f_{\mathrm{disk}}\): morphological disk fraction (Ferreira et al. \(\sim 40\)–\(50\%\) at \(z=3\)–\(6\)). \(f_{\mathrm{spiral}|\mathrm{disk}}\): fraction of disks that show arms once the sheet is cold enough. Conservative high-\(z\) stand-in \(\sim 0.7\).

\[
0.40\times 0.70=0.28,\qquad 0.50\times 0.70=0.35.
\]

That lands on Kuhn’s forward-model window. It is the statement: once Superblock says the sheet exists at \(z\sim 3\), the product should look like (disk fraction)\(\times\)(spiral-among-disks), not like HST “almost none.” Not an \(\mathrm{E}_8\) eigenvalue.

---

## 6. Predictions for this sample (Superblock only)

1. Inner mass **cored**, not NFW, wherever a rotation curve exists.  
2. \(g_{\mathrm{obs}}(g_b)\) already regular at \(z\sim 2\)–\(3\) for the spiral subsample.  
3. \(\sigma_R\) colder than merger-heated ΛCDM disks of the same mass and \(z\).  
4. Larger \(R_e\) at fixed \(M_\star\) from the cored well (re-run Kuhn’s redshifting experiment with a cored size–mass–\(z\) law before freezing \(35\%\)).  
5. Weak disk-PA coupling to the cosmic dipole is *allowed* by domain-orbit inheritance. Null is allowed.  
6. Joint clump+arm fraction can stay high in \(1.5<z<3\) (dual-scale Mirron: PK engines at clump scale, aeonic sheet at arm scale).  
7. Spec-\(z\) plateau of \(f_{\mathrm{int}}\) at \(z_{\mathrm{sheet}}\gtrsim 2.75\). A spec-\(z\) collapse below \(10\%\) at \(z\sim 3\) after a cored-well transfer function fails the “shadow already present” claim.

Not on this list: 7-fold arm harmonics from \(\tau\), KK comb in CEERS clustering, FRB wall tolls, Casimir-\(S^1\) DE as a morphology driver.

---

## 7. What would kill the Superblock mapping

- Spec-\(z\) massive sample at \(z\sim 3\) with \(f_{\mathrm{int}}<10\%\) after a cored-well forward model.  
- Inner density slopes of Kuhn’s spirals that are NFW-cuspy as a population.  
- \(\sigma_R\) as hot as the most turbulent ΛCDM disks, with no core.  
- Treating a null Tau comb in JADES/DESI as a null of Superblock domains. Those are different claims. The comb was Tau. Superblock is not that comb.

---

## 8. Bottom line

Kuhn still says: after an honest transfer-function inversion, about one third of massive galaxies at \(z=2\)–\(3\) are spiral-capable, and a near-zero population at \(z\sim 3\) is excluded. Age on the shared axis: \(2.11\,\mathrm{Gyr}\).

Superblock, with Tau stripped, still makes that number cheap:

- the well is a **cored Kerr-seed shadow of five co-located domains**, present under Dynamic Refresh;  
- cosmic \(5.2\) is a domain-orbit invariant, **not** a local \(G\) rescaling;  
- binding runs **upward** from PK / Mirron engines;  
- arms are ordinary density waves on a **Mirron sheet**.

It does not derive \(0.35\) from an eigenvalue. It does not need a \(7\,\mathrm{Mpc}\) fifth circle. Cite Kuhn as an external morphological prior for early sheet formation. Do not cite it as a Tau result, and do not cite it as a derivation of Superblock \(V_{\mathrm{orb}}\) eigenvalues.

---

## 9. File location

Saved: `Tau-Superblock_Universe/Personal_Files/2026-09-21_SB_only_recalc_Kuhn_JWST_spirals_2312.12389.md`
