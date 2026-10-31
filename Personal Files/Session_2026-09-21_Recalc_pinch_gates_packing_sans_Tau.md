# Session 2026-09-21 — Recalculate the pinch, gates, packing, ξ, fold, Weyl, and aeon jump without Tau / KK inputs

**Framework:** live Superblock frame after the 2026-09-20 repair  
**Charge:** Re-calculate the 2026-09-18 expanding-space / 5D-pinch stack using the updated corpus *sans* Tau inputs.  
**Governing locks:** `TSB_Superblock_fixed_frame_2026-09-20.md`, `Session_2026-09-20_TEP_Without_Tau_Circle_and_KK5.md`, `TSB_standing_state_summary_2026-09-20.md`  
**Convention:** Mirron, never soliton.

This file: `Personal_Files/Session_2026-09-21_Recalc_pinch_gates_packing_sans_Tau.md`  
Also copied to `Personal Files/` and `Tau-Superblock-Universe/Personal Files/`.

---

## 0. What was stripped (do not reload)

These objects carried the 18 September numbers. They are **out** of the live algebra.

| Retired input | Where 18 Sep used it | Status now |
|---|---|---|
| \(R_\tau=7\,h^{-1}\mathrm{Mpc}\) | \(n_{\mathrm{hier}}\), \(\Lambda_\Omega\), \(f_{\mathrm{void}}\), cosmic bolt, \(G_5\) | optional catalogue hook only; not load-bearing |
| Metric \(S^1_\tau\), \(\theta\), \(\varphi_\tau\) | 5D line element, KK stiffness | forbidden as unbound fifth dimension |
| \(n_{\mathrm{hier}}=\log_7(R_\tau/\lambda_{313})\) | Hierarchical Binding stretch, decade-18 packing coincidence | not a TEP premise; not used |
| \(\Lambda_\Omega=7/R_\tau\) | conformal gate | minted from dual-role 7; out |
| \(f_{\mathrm{void}}=127/343=1-(6/7)^3\) | wall fraction of a Tav cell | used \(R_\tau/7\) as wall thickness; out |
| Cosmic bolt at \(R_\tau/2\) | “image” of the clock pinch | 5D KK cousin; out |
| \(G_5=2\pi R_\tau G_N\) | 5D action bookkeeping | out |
| Casimir of \(S^1_\tau=\rho_\Lambda\) | vacuum density | archived prior |
| \(\Gamma\) parked at \(7\,h^{-1}\mathrm{Mpc}\) | “BOOM!” / void disconnect | not a theorem of the repaired frame |
| Dual-role exponent 7 as a length | wall scale, packing decades | exponent 7 is clock phase only |

**Allowed primitives (locked):**

- four dimensions; six co-located \(3+1\) copies on internal \(S^3_{\mathrm{int}}\)
- F7 freeze \(\{1,7\}\); moving exponents \(\{11,13,17,19,23,29\}\)
- \(\beta_i=(m_i-11)/30\) (frame convention)
- kernel \(K=\sum_i\gamma_i\overline{G}_i(\beta_i,\lambda_{m_0})\)
- IR floor \(m_0=313.1\,\mathrm{MeV}\) as **input**, not derived
- \(\lambda_{m_0}=\hbar/(m_0 c)\approx 0.6302\,\mathrm{fm}\)
- \(R_{\mathrm{int}}=\ell_P\) (F7 radius slot filled, not derived)
- TEP from \(e_i^2=-1\), \((\mathbb{Z}/7\mathbb{Z})^\times\), \(\Phi_7\) scrape / \(\Phi_8\) reset, empty twistor \(H^1\) for local reset overlap
- bound vs unbound bounce
- Mirron \(\in\mathrm{Conf}(S^3)\simeq\mathrm{SO}(4,1)\); phase-8 bounce is time/null reflection, not a spacelike KK circle
- \(\rho_{\mathrm{vac}}\) as chamber input (not computed from a circle)
- womb horizon \(r_{\mathrm{eh}}=c/H_\Lambda\) as 4D de Sitter scale (catalogue cosmology, not Tau)

---

## 1. Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(m_0\) | IR dressing floor \(313.1\,\mathrm{MeV}\). Input. Not a \(0^{++}\) pole. Not derived from a cell. |
| \(\lambda_{m_0}=\hbar/(m_0 c)\) | Compton length of that floor. \(\approx 6.302\times 10^{-16}\,\mathrm{m}\). This is the clock / kernel UV length formerly written \(r_{\mathrm{M}}\). |
| \(r_{\mathrm{M}}\) | Same number as \(\lambda_{m_0}\), kept as the proper radius of the Mirron 2-surface when a 2-surface is named. |
| \(\Delta_{\mathrm{Tav}}=E_g=m_0 c^2\) | Same floor as an energy. Inertial colour dressing. Local cost of a forced \(\Phi_7\to\Phi_8\) slot insertion. |
| \(\ell_P=R_{\mathrm{int}}\) | Planck length. Internal \(S^3\) / extremal Kerr-ring radius. F7 radius slot. |
| \(S^3_{\mathrm{int}}\) | Internal occupancy three-sphere. Not a large extra dimension. |
| \(L_{\mathrm{Hopf}}=2\pi R_{\mathrm{int}}\) | Hopf fibre length on \(S^3_{\mathrm{int}}\). |
| \(\Phi_7\) | Scrape / Higgs fabric / PK-Mirron channel. Not a seventh spacetime. |
| \(\Phi_8\) | Reset / identity / \(\mathcal{P}\leftrightarrow\mathcal{F}\) seam. |
| \(\mathcal{P},\mathcal{F},\mathcal{N}\) | Absolute Past, Absolute Future, Present stop-slice. |
| \(K\) | 4D averaging kernel of the six copies. |
| \(\Omega\), \(\hat\Omega\), \(\check\Omega\) | Local conformal factor of one womb / aeon. Reciprocal \(\hat\Omega\check\Omega=-1\) on a bandage. |
| \(\mathcal{X}\) | Crossover 3-surface (Penrose/Tod import, working). |
| \(r_{\mathrm{eh}}=c/H_\Lambda\) | Future event horizon of a \(\Lambda\)-owned womb. \(\approx 5156\,\mathrm{Mpc}\) at \(H_0=70\), \(\Omega_\Lambda=0.69\). |
| \(H_\Lambda=H_0\sqrt{\Omega_\Lambda}\) | de Sitter rate of the chamber. |
| \(n_{\mathrm{M}}\) | Proper number density of Mirrons (clock-scale engines). |
| \(v_{\mathrm{M}}=\tfrac43\pi\lambda_{m_0}^3\) | Bookkeeping 3-volume of one equivalent sphere. |
| \(f=n_{\mathrm{M}}v_{\mathrm{M}}\) | Packing fraction. |
| \(f_{\mathrm{geom}}\) | Local lattice efficiency when two engines touch. |
| \(\xi=\partial\ln Z_0/\partial\ln n_{\mathrm{M}}\) | Impedance susceptibility. |
| \(J^\nu_{\mathrm{Mirron}}=-\nabla_\mu T^{\mu\nu}_{K}-\cdots\) | Transfer current. Does not mint energy. |
| \(\Gamma\) | Bookkeeping name for \(\nabla_\mu(n_{\mathrm{M}}u^\mu)\) only where a number current is written. Not \(e^{-S_E/\hbar}\). |
| \(S_E\) | Euclidean action of one refresh tick. |
| \(\Delta t_\tau\) | Diameter tick \(2\lambda_{m_0}/c\). The subscript is historical; it is not a metric \(\tau\). |
| \(W(E_8)\), \(h=30\), \(\{m_j\}\) | Weyl group, Coxeter number, exponents. |
| \(\alpha=1-\log_7 6\) | Fractal deficit of the 6-of-7 graph. Scale-free. |
| \(\rho_{\mathrm{vac}}\) | Chamber vacuum density. Input / data on the patch. |

**Not in any equation below:** \(R_\tau\), \(S^1_\tau\), \(\varphi_\tau\), \(n_{\mathrm{hier}}\), \(G_5\), \(\rho_\Lambda=\hbar c/\tau^4\).

---

## 2. Layer-by-layer recalculation

### Layer 0 — lengths that survive

Two lengths, two jobs. Do not glue them with a logarithm.

\[
\lambda_{m_0}
=\frac{\hbar}{m_0 c}
=6.302\times 10^{-16}\,\mathrm{m}
=0.6302\,\mathrm{fm}.
\]

**Key.** \(m_0=313.1\,\mathrm{MeV}\) is an input floor. \(\lambda_{m_0}\) is its Compton length. This is the kernel UV cutoff and the candidate Mirron 2-surface radius.

\[
R_{\mathrm{int}}
=\ell_P
=\sqrt{\frac{\hbar G_N}{c^3}}
=1.616\times 10^{-35}\,\mathrm{m}.
\]

**Key.** F7 radius slot filled by naming, not derived. Occupancy space of the Planck–Kerr engine. Extremal ring \(a=GM_{\mathrm{Pl}}/c^2=\ell_P\).

\[
\frac{\lambda_{m_0}}{\ell_P}=3.899\times 10^{19}.
\]

**Key.** Ratio of two independent floors. Not \(7^{n}\) for an integer \(n\). Do not define \(n_{\mathrm{hier}}=\log_7(\lambda_{m_0}/\ell_P)\) and treat it as TEP. TEP does not need it.

**Dropped.** \(n_{\mathrm{hier}}=\log_7(R_\tau/\lambda_{m_0})\approx 45.78\). That number is not in the live frame. A similar logarithm of the *de Sitter* radius, \(\log_7(r_{\mathrm{eh}}/\lambda_{m_0})\approx 49.0\), is the same class of temptation and is **not promoted**.

**Plain language.** We still have a fermi clock and a Planck seed. We no longer have a megaparsec hoop that was supposed to be the same hoop seen through a 46-step mirror.

---

### Layer 1 — local packing \(f_{\mathrm{geom}}\) (unchanged)

This layer never used \(R_\tau\). Six domains, six neighbours:

\[
f_{\mathrm{geom}}=\frac{\pi}{6}\approx 0.5236,
\qquad
\ell_{\mathrm{pack}}^{\mathrm{(loc)}}=2\lambda_{m_0}.
\]

**Key.** Simple-cubic coordination matches \(N_{\mathrm{dom}}=6\). Local tile only.

FCC \(0.7405\) remains an upper bound, not preferred.

---

### Layer 2 — cosmological packing (C0 survives; decade-18 talk dies)

Nuclear SC packing is still a neutron-star vacuum and is still vetoed.

C0 does **not** use Tau. It uses \(\rho_{\mathrm{vac}}\) as chamber data and \(\Delta_{\mathrm{Tav}}\) as the floor:

\[
n_{\mathrm{M}}^{(0)}
=\frac{\rho_{\mathrm{vac}}}{\Delta_{\mathrm{Tav}}}
=11.38\,\mathrm{m}^{-3},
\qquad
\ell_{\mathrm{pack}}^{(0)}=0.445\,\mathrm{m},
\qquad
f_{\ast}^{(0)}=1.19\times 10^{-44}.
\]

**Key.** \(\rho_{\mathrm{vac}}\approx 5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\) at \(H_0=70\), \(\Omega_\Lambda=0.69\). This *uses* dark energy; it does not explain it. Live frame: \(\rho_{\mathrm{vac}}\) is an input on the patch, default \(\nabla\rho_{\mathrm{vac}}=0\).

**Dropped.** “Spacing sits between Tav decades 17 and 18.” There are no Tav decades. \(7^{18}\lambda_{m_0}\approx 1\,\mathrm{m}\) is numerology once \(R_\tau\) is gone.

**Dropped.** Residuals \(7^{-6}\), \(6^{-6}\) as *cosmic* suppression factors tied to a cylinder. \(7^{-6}\) as an *algebraic* occupancy weight on six letters remains legal as combinatorics; it is not a derived \(\Xi\) for \(\rho_{\mathrm{vac}}\).

**Plain language.** A handful of engines per cubic metre is still the conservative mean if each engine’s dressing quantum *is* the vacuum energy. That sentence is bookkeeping. It is not a derivation of \(\Lambda\).

---

### Layer 3 — fold / “pinch” without a fifth circle

#### 3.1 What is forbidden

The 18 September Ricci-flat metric

\[
\mathrm{d}s_5^2
=\mathrm{d}\tau^2
+\frac{\mathrm{d}r^2}{1-r_s/r}
+r^2\mathrm{d}\Omega_2^2
+\alpha^2\bigl(1-r_s/r\bigr)\mathrm{d}\theta^2
\]

is a **5D** geometry. The last term is a metric circle. Under the 2026-09-14 / 09-20 locks that term is not a live object, whether \(\alpha=R_\tau\) or \(\alpha=\lambda_{m_0}\). A “clock-scale KK circle” is still KK.

Scale Reflection \(\varphi_\tau/R_\tau=\psi/\lambda_{m_0}\) is the merger slide that identified a Tau object with a Superblock object. Out.

#### 3.2 What replaces it (4D, algebraic + conformal)

**A. Algebraic pinch (TEP, load-bearing).**  
Double occupancy of one domain–phase slot is left multiplication twice by the same imaginary unit:

\[
e_k(e_k v)=-e_0 v
\quad\text{or a \(G_2\)-image}.
\]

**Key.** \(e_k\): active letter; \(e_0=\Phi_8\): reset. That *is* the pinch: the active hoop squares to the identity seam. No metric fifth coordinate. Local energy cost of forcing the insertion while remaining a *bound* slot:

\[
E_{\mathrm{violation}}\ge\Delta_{\mathrm{Tav}}=m_0 c^2.
\]

Unbound completed \(\mathcal{P}\leftrightarrow\mathcal{F}\) bounces *are* the seam globally and do not pay this as a local slot.

**B. Conformal / phase-8 pinch (geometry of one engine, 4D).**  
A point of 4-spacetime is a celestial \(\mathbb{CP}^1\) of null generators. Phase 8 is the reflection of those generators (future-directed \(\leftrightarrow\) past-directed), a map on the same 4-world. The Mirron is that reflection as an element of \(\mathrm{Conf}(S^3)\simeq\mathrm{SO}(4,1)\).

The 2-surface that 18 September called the bolt is, in 4D language, the celestial 2-sphere of the engine (or the spatial 2-sphere of the Planck–Kerr ring, Hopf-projected). Its *dressing* scale is \(\lambda_{m_0}\). Its *ring* scale is \(\ell_P\). Two scales, one engine.

**C. Optional 4D Euclidean section (not KK, not used as \(G_N\)-horizon).**  
The purely 4D Euclidean Schwarzschild section

\[
\mathrm{d}s_4^2
=\Bigl(1-\frac{r_s}{r}\Bigr)\mathrm{d}\tau_E^2
+\frac{\mathrm{d}r^2}{1-r_s/r}
+r^2\mathrm{d}\Omega_2^2
\]

has a bolt \(S^2(r_s)\) and regularity period \(\beta_E=4\pi r_s/c\). Setting \(r_s=\lambda_{m_0}\) makes \(\beta_E=2\pi\Delta t_{\mathrm{diam}}\). That metric is 4D. It is **not** licensed as a laboratory-\(G_N\) black hole of radius \(\lambda_{m_0}\) (that reading again assigns a mountain of mass). It is a conformal picture of a capped 2-sphere, not a derivation of \(G_N\).

#### 3.3 Stiffness gate without \(\varphi_\tau\)

The two-scalar action’s \(\varphi_\tau\) is gone. The packing / nucleation switch is \(\varphi_{\mathrm{n}}\) slaved to the *local* conformal factor of a womb:

\[
\varphi_{\mathrm{n}}=\Omega^{-\nu},
\qquad
\nu=2,
\qquad
\varphi_{\mathrm{crit}}=1
\quad\Longleftrightarrow\quad
\Omega>1.
\]

**Key.** Mean living wall: \(\Omega=1\). Interior of an isolated womb: \(\Omega\) runs. Soft side is still “void-like / womb-owned.” No KK modulus.

Width of the 4D \(\tanh\) profile, when one is written, is still the only IR length in the kernel:

\[
\mu_{\mathrm{n}}=\frac{\hbar c}{\lambda_{m_0}}=m_0 c^2=\Delta_{\mathrm{Tav}}.
\]

**Key.** Same identification as 18 September, now justified by \(K\)’s UV length, not by a 5D fold width.

#### 3.4 Action of one tick (survives; no \(G_5\))

Diameter tick \(\Delta t_{\mathrm{diam}}=2\lambda_{m_0}/c\). Rest energy one dressing quantum:

\[
\frac{S_E}{\hbar}
=\frac{\Delta_{\mathrm{Tav}}\,\Delta t_{\mathrm{diam}}}{\hbar}
=\frac{m_0 c^2\cdot 2(\hbar/(m_0 c))/c}{\hbar}
=2.
\]

**Key.** Uses only \((m_0,\lambda_{m_0},\Delta t_{\mathrm{diam}})\). No \(G_5\), no \(R_\tau\). Light-ring tick \(2\pi\lambda_{m_0}/c\) would give \(2\pi\); seven-phase tick \(2\pi\lambda_{m_0}/(7c)\) would give \(2\pi/7\). Frozen diameter choice gives \(2\).

This is *not* \(e^{-S_E/\hbar}\) as a nucleation rate. \(\Gamma\) is not an instanton exponent. Permanent engines pay TEP; ordinary unbound refresh does not.

---

### Layer 4 — conformal gate \(\Lambda_\Omega\) rebuilt in 4D

**Dropped.** \(\Lambda_\Omega=7/R_\tau=1/(1.43\,h^{-1}\mathrm{Mpc})\). Dual-role 7.

**4D candidates, live-frame legal:**

| Candidate | Value (numbers at \(H_0=70\), \(\Omega_\Lambda=0.69\)) | Meaning |
|---|---|---|
| \(1/\lambda_{m_0}\) | \(1.59\times 10^{15}\,\mathrm{m}^{-1}\) | nuclear crease only; cosmic walls fail |
| \(H_0/c\) | \(7.57\times 10^{-27}\,\mathrm{m}^{-1}\) | Hubble length; gate almost always on |
| \(H_\Lambda/c=1/r_{\mathrm{eh}}\) | \(6.29\times 10^{-27}\,\mathrm{m}^{-1}\) | womb horizon. \(r_{\mathrm{eh}}\approx 5156\,\mathrm{Mpc}\) |

The only *4D geometric* wall scale the repaired womb picture actually names is the future event horizon of a \(\Lambda\)-owned chamber,

\[
r_{\mathrm{eh}}=\frac{c}{H_\Lambda}=\frac{c}{H_0\sqrt{\Omega_\Lambda}}\approx 5156\,\mathrm{Mpc}.
\]

**Key.** \(H_\Lambda\): de Sitter rate of the isolated womb. This is catalogue GR + \(\rho_{\mathrm{vac}}\) as input. It is not minted from exponent 7.

A gate that fires on *finite* walls inside a womb, not on the horizon itself, is **not computed**. Options left open (not locked):

1. \(\Lambda_\Omega=H_\Lambda/c\). Then almost every super-Hubble gradient passes. Weak.
2. \(\Lambda_\Omega\) from \(\lvert\nabla\log\Omega\rvert\) on the living wall where \(\Omega\to 1\). That needs the local-\(\Omega\) profile per superblock, written but not integrated (`TSB_local_conformal_factor_per_superblock_2026-09-20.md`).
3. No Heaviside gate. Nucleation / refresh is the transfer current \(J_{\mathrm{Mirron}}=-\Delta_K^\nu\), support wherever the kernel has a defect. Gates were a 18 September schema.

**Working lock for this session.** Do not quote a megaparsec rational as if it were F7. Until the local-\(\Omega\) profile is integrated,

\[
\Lambda_\Omega
\quad\text{is unnamed as a number.}
\]

The qualitative sentence that survives: homogeneous FLRW (\(\nabla\Omega=0\)) does not write new engines; isolated wombs and their walls can.

**Plain language.** We used to say “sharper than one-seventh of the Tau circle.” That ruler is gone. The only big 4D ruler left is the de Sitter horizon of the chamber, and it is too blunt to be a wall thickness. The wall gate is therefore an open 4D calculation, not a recycled 7.

---

### Layer 5 — \(\xi\) (unchanged in substance)

Generator G1′ (self-similar cell, voltage and current set by the same scale) still gives

\[
\xi^{(0)}=0
\]

at sparse C0 packing. No Tau input.

Branch A (replenish engines as proper volume grows, *on the support of whatever 4D gates survive*) is still required by frozen \(\lambda_{m_0}\) plus growing 3-volume, not by the ohm. Branch B is still the control in which the mean lattice thins.

Clocks bound \(\lvert\xi\rvert\lesssim 5\times 10^{-9}\) only *if* Branch B is assumed. With \(\xi=0\) that bound is idle.

---

### Layer 6 — \(f_{\mathrm{void}}\) (the rational dies)

**Dropped.** \(f_{\mathrm{void}}=127/343\) from \(\delta=R_\tau/7\).

What remains, qualitative:

- Isolated voids of a parent mother children (fractal tree, original Superblock).
- Living walls carry \(\Omega\to 1\).
- No derived volume fraction.

A spherical-shell guess using \(r_{\mathrm{eh}}\) as radius and an *unspecified* wall thickness \(\delta\) would be

\[
f_{\mathrm{void}}=1-\bigl(1-\delta/r_{\mathrm{eh}}\bigr)^3,
\]

which is empty until \(\delta\) is computed from local \(\Omega\). Not a number.

**Working lock.** \(f_{\mathrm{void}}\) unnamed. Do not recycle \(0.370\).

---

### Layer 7 — Weyl scars (micro estimate survives; wall budget does not)

One engine’s physical mass is the dressing quantum, not a \(G_N\)-horizon of radius \(\lambda_{m_0}\):

\[
\frac{r_s^{\mathrm{(phys)}}}{\lambda_{m_0}}
=\frac{2G_N(\Delta_{\mathrm{Tav}}/c^2)}{c^2\lambda_{m_0}}
\sim 10^{-38}.
\]

**Key.** Same order as 18 September. Independent of \(R_\tau\).

Volume filling at C0: \(n_{\mathrm{M}}v_{\mathrm{M}}\sim 10^{-44}\). Micro scars do not lens.

**Dropped.** Wall-scale Weyl budget that used \(\Gamma=3H n_{\mathrm{M}} f_{\mathrm{void}}\) with \(f_{\mathrm{void}}=0.370\). That product used the dead rational. Rebuild after \(\Lambda_\Omega\) and \(f_{\mathrm{void}}\) exist in 4D.

Transfer current (live) does not mint:

\[
J^\nu_{\mathrm{Mirron}}
=-\nabla_\mu T^{\mu\nu}_{K}
-\nabla_\mu T^{\mu\nu}_{\mathrm{vis}}
-\nabla_\mu T^{\mu\nu}_{\mathrm{vac}}.
\]

**Key.** Bianchi first. Default \(\nabla\rho_{\mathrm{vac}}=0\), so the vacuum piece vanishes and the current is kernel + visible transfer.

---

### Layer 8 — aeon jump without a fifth circle

4D Penrose/Tod bandage is legal. Reciprocal

\[
\hat\Omega\,\check\Omega=-1
\quad\text{on }\mathcal{X}.
\]

**Key.** Both metrics conformal to one bridge. Lightcones match. Rest mass is the fight with \(m_0\) (fade / exception / recover-after: not chosen).

Phase-8 bounce is the reflection map across \(\mathcal{X}\) or across \(\mathscr{I}^+\), time or null, not a CTC and not \(S^1_\tau\).

The integer \(X_\Omega\) (how many new clock-scale engines the stamp writes) is **still not computed**. Removing Tau does not compute it. It removes a wrong arena in which it was being visualised.

Completed unbound bounces may sit on the seam globally. Bound engines pay \(\Delta_{\mathrm{Tav}}\) to remain after the stamp if they occupy a local slot.

---

## 3. Scoreboard — 18 September vs live frame

| Quantity | 18 Sep (with Tau/KK) | 21 Sep (sans Tau/KK) |
|---|---|---|
| \(\lambda_{m_0}=r_{\mathrm{M}}\) | \(0.6302\,\mathrm{fm}\) | **same** (floor input) |
| \(R_{\mathrm{int}}\) | \(\ell_P\) as 5D seed | \(\ell_P\) as F7 / Kerr ring / \(S^3_{\mathrm{int}}\) |
| \(n_{\mathrm{hier}}\) | \(45.78\) | **retired** |
| \(f_{\mathrm{geom}}\) | \(\pi/6\) | **same** |
| \(n_{\mathrm{M}}^{(0)}\), \(f_{\ast}^{(0)}\) | \(11.4\,\mathrm{m}^{-3}\), \(10^{-44}\) | **same** (uses \(\rho_{\mathrm{vac}}\) as data) |
| decade-18 talk | recorded | **retired** |
| \(\varphi_{\mathrm{crit}}\) | \(1\) \(\Leftrightarrow\) \(\Omega>1\) | **same**, now on local womb \(\Omega\) |
| \(\mu_{\mathrm{n}}\) | \(\Delta_{\mathrm{Tav}}\) | **same** |
| 5D bolt metric | Ricci-flat with \(\mathrm{d}\theta^2\) | **retired as live geometry** |
| Algebraic pinch | implicit TEP | **load-bearing** (\(e_k^2\to\Phi_8\)) |
| Phase-8 bounce | identified with KK cap | 4D twistor / \(\mathrm{Conf}(S^3)\) reflection |
| \(S_E/\hbar\) | \(2\) per diameter tick | **same**, no \(G_5\) |
| \(\Lambda_\Omega\) | \(7/R_\tau\) | **unnamed**; \(r_{\mathrm{eh}}\approx 5156\,\mathrm{Mpc}\) is the only 4D big ruler |
| \(\xi^{(0)}\) | \(0\) | **same** |
| \(f_{\mathrm{void}}\) | \(127/343\) | **unnamed** |
| Micro Weyl | \(10^{-38}\) | **same** |
| Wall Weyl / \(\Gamma\) volume | used \(0.370\) | **open** |
| Aeon \(X_\Omega\) | identification | **open**, 4D bandage only |
| Cosmic bolt \(R_\tau/2\) | derived cousin | **retired** |

---

## 4. Expansion sentence, repaired

18 September:

> Expanding space creates room; frozen mirrors cannot stretch; a KK scalar nucleates new \(\Sigma_{\mathrm{M}}\) at rate \(3H n_{\mathrm{M}}\) on Tau-circle walls.

21 September, live frame:

> Proper 3-volume of an expanding 4-world grows. The dressing length \(\lambda_{m_0}\) is frozen. A fixed count would thin the mean lattice. New Mirrons are booked as *transfer* (\(J_{\mathrm{Mirron}}=-\Delta_K\)), not as minting from a fifth circle and not as \(e^{-S_E/\hbar}\). Support is wherever the kernel has a defect and the local conformal factor of a womb is off the living-wall value \(\Omega=1\). TEP (\(e_k^2=-1\to\Phi_8\)) is the occupancy rule that decides which bookings are bound engines and which are unbound refresh. Vacuum density on the patch is an input. No megaparsec is derived. No Casimir of a metric hoop is \(\rho_{\mathrm{vac}}\).

**Plain language.** The floor still gets bigger and the tiles still refuse to stretch. We no longer pretend a ten-megaparsec hoop is doing the tiling. The tiling rule is the 8-letter algebra and the 4D kernel. Dark energy is still put in by hand until someone integrates \(J_{\mathrm{sec}}\) or a non-circular \(\rho_\Omega\) on the tree.

---

## 5. What this session did *not* restore

Tau metric circle, Casimir-\(\Lambda\), 7 Mpc as derived length, dual-role exponent 7, 5D pinch as live geometry, Scale Reflection that glues \(\lambda_{m_0}\) to \(R_\tau\), \(f_{\mathrm{void}}=0.370\), \(\Lambda_\Omega=7/R_\tau\), prize language, zero continuous parameters, mined 7-fold detections.

---

## 6. What remains actually open (4D list)

1. Integrate local \(\Omega\) on one womb; then \(\Lambda_\Omega\) and \(f_{\mathrm{void}}\) can become numbers.
2. Integrate \(J_{\mathrm{sec}}\) on an isolated patch under ansatz A.
3. Choose fade / exception / recover-after for \(m_0\) on \(\mathcal{X}\).
4. Non-circular \(\rho_{\mathrm{vac}}\) from the tree, or leave it input.
5. Independent evaluation of a 4D Euclidean section *without* reading it as a \(G_N\)-hole of radius \(\lambda_{m_0}\).
6. Hopf linking constraint on \(B_{7\to i}\) (named 20 Sep, not evaluated).

---

*End of session — 2026-09-21 recalc sans Tau / KK.*
