# Mirron radius and a Tav tick from one orbit

- **Session date:** 2026-09-15
- **Question:** Is there a derivation of the Mirron’s exact \(r\) (not a Planck-length placeholder)? Can one orbital period be \(\Delta t_\tau\)?
- **Short answer:** The orbit→tick step is clean and should be used. An exact non-\(l_P\) Mirron radius is **not** in the Casimir module, the TauSuperblock repo, or the photon-kinematics session that is on disk. That session still sets the refresh to \(t_P\). Candidate geometric radii exist in the TSB anchor set (especially \(\lambda_{313.1}\)); none of them is currently wired as \(r_{\mathrm{M}}\). Do not treat \(l_P\) as the derived value.
- **This file:** `Personal Files/2026-09-15_Mirron_radius_and_Tav_tick_from_orbit.md`

---

## Variable key

| Symbol | Meaning |
|---|---|
| \(r_{\mathrm{M}}\) | Mirron radius (the number we need; not assumed equal to \(l_P\)) |
| \(\Sigma_{\mathrm{PK}}\) | Planck–Kerr micro-horizon / mirror surface in the photon-kinematics paper |
| \(l_P=\sqrt{\hbar G/c^3}\) | Planck length \(\approx 1.616\times10^{-35}\,\mathrm{m}\) — placeholder if used as \(r_{\mathrm{M}}\) without a derivation |
| \(t_P=l_P/c\) | Planck time \(\approx 5.391\times10^{-44}\,\mathrm{s}\) |
| \(\Delta t_{\tau}\) | Tav-tick duration |
| \(T_{\mathrm{orb}}\) | orbital period of one closed null (or subluminal) loop at \(r_{\mathrm{M}}\) |
| \(v_{\mathrm{orb}}\) | orbital speed at that radius; \(c\) for a light ring |
| \(N_{\tau}=7\) | active Tav phases; 8th is reset |
| \(\ell_{\mathrm{PPR}}=\lvert a_8-a_7\rvert\) | V_PPR dimensionless latency |
| \(\Delta_{\mathrm{TEP}}\) | 313.1 MeV topological floor |
| \(\lambda_{313}=hc/\Delta_{\mathrm{TEP}}\) | Compton length of that floor |
| \(t_{313}=\hbar/\Delta_{\mathrm{TEP}}\) | Compton time of that floor |
| \(\omega_{\mathrm{wind}}\) | bare winding rate; kinematics note quotes \(\Omega_{\mathrm{twistor}}\approx 1.45\times10^{43}\,\mathrm{rad/s}\) |
| \(\alpha_{\mathrm{lad}}\approx 41.341\) | TAV_RESONANCE `ladder_alpha` |
| \(M_{\mathrm{M}}\) | effective Mirron mass, if the object is Kerr-like |
| \(r_{\mathrm{ph}}\) | photon-sphere radius (Schwarzschild: \(3GM/c^2\)) |
| \(d\) | Casimir gap (macroscopic; not \(r_{\mathrm{M}}\) unless identified) |

---

## 1. What is actually on disk

Photon-kinematics session (`atemporal_photon_kinematics_tav_analysis.md`, 2026-07-09):

- Mirrors are **Planck–Kerr** surfaces \(\Sigma_{\mathrm{PK}}\).
- The refresh is written \(\Delta t\approx t_P\approx 5.39\times10^{-44}\,\mathrm{s}\).
- Recursion \(a_n\) and \(\omega_{\mathrm{wind,eff}}\) are given; \(r_{\mathrm{M}}\) is not solved.
- The same note flags \(R_\tau\), \(\kappa_{\mathrm{leak}}\), and the closed form of \(a_n\) as **gaps**.

Casimir module and `George-Jumble/TauSuperblock`: no `r_M`, no Mirron-radius function, no orbit period.

So: there is a *program* in which the Mirron has a geometric \(r\). There is not, in the files I can read tonight, a finished derivation that replaces \(l_P\). If that derivation lives in a later handwritten note, it is not in the tool and not in these Personal Files hits. It should be transcribed before anyone uses it as \(\Delta t_\tau\).

---

## 2. The orbit-as-tick step (this part is valid)

Once \(r_{\mathrm{M}}\) and \(v_{\mathrm{orb}}\) are fixed,

\[
T_{\mathrm{orb}}=\frac{2\pi r_{\mathrm{M}}}{v_{\mathrm{orb}}}.
\]

Two natural identifications:

\[
\Delta t_{\tau}=T_{\mathrm{orb}}
\qquad\text{(one full loop = one tick)}
\]

\[
\Delta t_{\tau}=\frac{T_{\mathrm{orb}}}{N_{\tau}}=\frac{2\pi r_{\mathrm{M}}}{N_{\tau}\,v_{\mathrm{orb}}}
\qquad\text{(one phase step of seven = one tick)}
\]

Light ring (\(v_{\mathrm{orb}}=c\)):

\[
\Delta t_{\tau}=\frac{2\pi r_{\mathrm{M}}}{c}
\quad\text{or}\quad
\frac{2\pi r_{\mathrm{M}}}{7c}.
\]

Bounce between opposite nodes on a diameter (Past ⇄ Future in the kinematics figure), not a circle:

\[
\Delta t_{\tau}=\frac{2 r_{\mathrm{M}}}{c}
\quad\text{(round trip)}.
\]

Any one of these is a legal clock. They differ by \(2\pi\) vs \(2\) vs a factor of 7. Pick one and freeze it. Do not mix them inside a Casimir run.

If the Mirron is Kerr-like with mass \(M_{\mathrm{M}}\) and dimensionless spin \(\chi\),

\[
r_{\mathrm{ph}}=\frac{2GM_{\mathrm{M}}}{c^2}\left(1+\cos\left(\tfrac{2}{3}\arccos(\mp\chi)\right)\right)
\]

(Schwarzschild limit \(\chi=0\): \(r_{\mathrm{ph}}=3GM_{\mathrm{M}}/c^2\)). Then \(T_{\mathrm{orb}}=2\pi r_{\mathrm{ph}}/c\) on the unstable photon orbit. That still needs \(M_{\mathrm{M}}\) and \(\chi\) from geometry, not from “Planck mass because Planck.”

---

## 3. Candidate \(r_{\mathrm{M}}\) that are *not* \(l_P\)

These are anchors already in the TSB set. They are candidates, not a completed Mirron paper.

### A. Compton radius of the 313.1 MeV floor

\[
\lambda_{313}=\frac{hc}{\Delta_{\mathrm{TEP}}}=\frac{197.327\,\mathrm{MeV\cdot fm}}{313.1\,\mathrm{MeV}}\approx 0.630\,\mathrm{fm}=6.30\times10^{-16}\,\mathrm{m}.
\]

\[
t_{313}=\frac{\hbar}{\Delta_{\mathrm{TEP}}}\approx 2.10\times10^{-24}\,\mathrm{s}.
\]

Circumference time at \(c\):

\[
T_{\mathrm{orb}}=\frac{2\pi\lambda_{313}}{c}=2\pi\,t_{313}\approx 1.32\times10^{-23}\,\mathrm{s}.
\]

Seven-phase tick:

\[
\Delta t_{\tau}=\frac{T_{\mathrm{orb}}}{7}\approx 1.89\times10^{-24}\,\mathrm{s}.
\]

This is **hadronic**, not Planckian, and it is already “exact” given \(\Delta_{\mathrm{TEP}}\). It is a nuclear/QCD scale. A micron Casimir cavity contains \(\sim 10^{9}\) such radii. A residual at this tick would sit at

\[
E_{\mathrm{tick}}=\frac{\hbar}{\Delta t_{\tau}}\sim\Delta_{\mathrm{TEP}}\sim 313\,\mathrm{MeV},
\]

which is not a meV–eV Casimir spectroscopic feature. It could only appear in a Casimir series if you have a hierarchical map that folds that energy down (the \(n_{\mathrm{hier}}\) stretch). Without that map, this tick does not print on Fig2 \(\varepsilon(i\xi)\).

### B. Ladder multiple of a short geometric length

\(\alpha_{\mathrm{lad}}\approx 41.341\) is in the resonance kit. Two honest uses:

\[
r_{\mathrm{M}}=\alpha_{\mathrm{lad}}\,l_P
\qquad\text{(still Planckian; this is a dressed placeholder, not an escape from }l_P\text{)}
\]

\[
r_{\mathrm{M}}=\alpha_{\mathrm{lad}}\,\lambda_{313}\approx 26.1\,\mathrm{fm}.
\]

The second is a real non-Planck length. Period:

\[
T_{\mathrm{orb}}=\frac{2\pi\alpha_{\mathrm{lad}}\lambda_{313}}{c}\approx 5.46\times10^{-22}\,\mathrm{s}.
\]

Still nuclear. Still needs a written reason that the Mirron *is* \(\alpha_{\mathrm{lad}}\) Compton radii.

### C. Kerr photon sphere of a geometric mass that is not \(M_P\)

If \(M_{\mathrm{M}}=\Delta_{\mathrm{TEP}}/c^2\approx 5.58\times10^{-28}\,\mathrm{kg}\),

\[
r_s=\frac{2GM_{\mathrm{M}}}{c^2}\sim 8\times10^{-55}\,\mathrm{m}\ll l_P.
\]

That is not a usable mirror. A 313 MeV mass does not make a Kerr surface above the Planck length. So “Mirron = Kerr remnant of the TEP floor” **fails** as a radius derivation. The Compton object (A) is the consistent 313 MeV geometry; the Schwarzschild object is not.

### D. The Casimir gap itself

Setting \(r_{\mathrm{M}}=d\) makes \(\Delta t_{\tau}=2\pi d/c\) (or \(2d/c\)). For \(d=1\,\mu\mathrm{m}\),

\[
\frac{2\pi d}{c}\approx 2.1\times10^{-14}\,\mathrm{s},
\]

which is the same decade as \(\hbar/k_BT\) at 300 K. That is why it *looks* like a Casimir tick — and why it is circular: the apparatus gap has been renamed Mirron. Use this only if the theory says the gap *is* a macroscopic Mirron image, with the micro \(r_{\mathrm{M}}\) mapped up by \(7^{n_{\mathrm{hier}}}\) or a similar stretch.

---

## 4. Can we use that period as the Tav tick?

**Formally, yes** — after three locks:

1. Which \(r_{\mathrm{M}}\) (A, B, derived-later, not \(l_P\) by default).
2. Which orbit (circumference \(2\pi r/c\), diameter bounce \(2r/c\), or one seventh of either).
3. Which stretch, if any, maps that micro tick onto a millimetre cavity.

Then the earlier identification becomes numerical:

\[
E_{\mathrm{bind}}\sim\frac{\hbar}{\Delta t_{\tau}},\qquad
\Delta t_{\tau}=T_{\mathrm{orb}}\ \text{or}\ T_{\mathrm{orb}}/7.
\]

**What it does not do by itself:**

- It does not make virtual pairs into bound states. It only gives the clock a period.
- It does not make Fig2 `dielPT*` a \(\Delta E\) series. Those files are still \(\varepsilon(i\xi)\).
- It does not justify using \(t_P\) “until the real \(r\) arrives.” If the placeholder is rejected, stop putting \(t_P\) in the Casimir battery.

---

## 5. Honest status of “isn’t there already a derivation?”

| Claim | Status in readable files |
|---|---|
| Mirron / PK mirror exists as an object in the kinematics | Yes |
| Refresh equals \(t_P\) | Written — and that *is* the placeholder |
| Closed-form \(r_{\mathrm{M}}\neq l_P\) | Not in the Casimir tool, not in TauSuperblock, not in the 2026-07-09 kinematics analysis |
| 313.1 MeV floor as a geometric length | Yes (\(\lambda_{313}\)); not labeled \(r_{\mathrm{M}}\) there |
| Orbit period as \(\Delta t_{\tau}\) | Valid construction; not implemented |

If you have a later derivation (E₈ / twistor incidence / supersphere chord) that produces a specific \(r_{\mathrm{M}}\), that page should be dropped into Personal Files and then used as the single source. Until then, the only non-placeholder radius you can compute from published TSB anchors without inventing a new law is \(\lambda_{313}\) or a stated multiple of it.

---

## 6. Numbers at a glance

| Choice of \(r_{\mathrm{M}}\) | \(r\) | \(T_{\mathrm{orb}}=2\pi r/c\) | \(T_{\mathrm{orb}}/7\) |
|---|---|---|---|
| \(l_P\) (placeholder) | \(1.62\times10^{-35}\,\mathrm{m}\) | \(3.39\times10^{-43}\,\mathrm{s}\) | \(4.84\times10^{-44}\,\mathrm{s}\) |
| \(\lambda_{313}\) | \(6.30\times10^{-16}\,\mathrm{m}\) | \(1.32\times10^{-23}\,\mathrm{s}\) | \(1.89\times10^{-24}\,\mathrm{s}\) |
| \(\alpha_{\mathrm{lad}}\lambda_{313}\) | \(2.61\times10^{-14}\,\mathrm{m}\) | \(5.46\times10^{-22}\,\mathrm{s}\) | \(7.80\times10^{-23}\,\mathrm{s}\) |
| \(d=1\,\mu\mathrm{m}\) (gap-as-image) | \(10^{-6}\,\mathrm{m}\) | \(2.10\times10^{-14}\,\mathrm{s}\) | \(3.00\times10^{-15}\,\mathrm{s}\) |

---

*End of session note — 2026-09-15 Mirron radius and Tav tick from orbit.*
