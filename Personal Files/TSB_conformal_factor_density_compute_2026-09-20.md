# Compute the conformal-factor density

**Date:** 2026-09-20  
**Asked:** density belonging to the local bridging factor \(\Omega_A\).  
**Status:** calculation. Not entered as live-frame dark energy. Circularity is part of the result.

---

## 1. 4D transformation

Physical metric of a womb relative to a bridge \(g_{\mu\nu}\):

\[
\tilde g_{\mu\nu}=\Omega^2 g_{\mu\nu}.
\]

Set \(\omega=\ln\Omega\). In four dimensions

\[
\tilde G_{\mu\nu}-G_{\mu\nu}
=
-2\nabla_\mu\nabla_\nu\omega
+2g_{\mu\nu}\Box\omega
+2\nabla_\mu\omega\nabla_\nu\omega
+g_{\mu\nu}(\nabla\omega)^2.
\]

If the Einstein equation is read on the bridge as

\[
G_{\mu\nu}
=
8\pi G_N
\bigl(T_{\mu\nu}+T^{(\Omega)}_{\mu\nu}\bigr),
\]

the conformal piece is

\[
8\pi G_N\,T^{(\Omega)}_{\mu\nu}
=
\tilde G_{\mu\nu}-G_{\mu\nu}
\]

when matter is not double-counted (bridge empty of extra fluids). Then

\[
T^{(\Omega)}_{\mu\nu}
=
\frac{1}{8\pi G_N}
\Bigl[
-2\nabla_\mu\nabla_\nu\omega
+2g_{\mu\nu}\Box\omega
+2\nabla_\mu\omega\nabla_\nu\omega
+g_{\mu\nu}(\nabla\omega)^2
\Bigr].
\]

**Key.** \(\Omega\): local bridging factor of one womb. \(\omega=\ln\Omega\). \(G_N\): Newton constant. \(T^{(\Omega)}\): effective stress of \(\Omega\) as seen on the bridge.

---

## 2. Homogeneous patch, \(\Omega=\Omega(t)\) only

Bridge FLRW, cosmic time \(t\), \(\dot\omega=\dot\Omega/\Omega\).

Energy density and pressure of the conformal piece:

\[
\rho_\Omega
=
\frac{3\dot\omega^2}{8\pi G_N},
\qquad
p_\Omega
=
\frac{1}{8\pi G_N}
\bigl(-2\ddot\omega-\dot\omega^2\bigr).
\]

Equation of state:

\[
w_\Omega
=
\frac{p_\Omega}{\rho_\Omega}
=
-\frac13
-
\frac{2\ddot\omega}{3\dot\omega^2}
\quad(\dot\omega\neq 0).
\]

Slow, almost-exponential \(\Omega\propto e^{Ht}\) with constant \(H\) gives \(\ddot\omega=0\) and \(w_\Omega=-1/3\), **not** \(-1\).  
de Sitter-like \(\dot\omega=H_\Lambda\) constant on this chart is the same: \(w=-1/3\) for a pure \(\dot\omega\) fluid of this split.

To get \(w=-1\) you need the \(\ddot\omega\) term to cancel to

\[
\ddot\omega
=
-\dot\omega^2
\quad\Rightarrow\quad
w_\Omega=-1.
\]

That is \(\dot\omega=1/(t-t_*)\) or a chart in which \(\Omega\) tracks the reciprocal pair through the bandage, not a free constant \(\dot\omega\).

**Key.** \(\rho_\Omega\): conformal-factor density. \(w_\Omega\): its equation of state on this split. \(H_\Lambda=c\sqrt{\Lambda/3}\).

---

## 3. Number that matches \(\rho_\Lambda\)

Observed

\[
\rho_\Lambda
\approx
0.7\,\rho_c
=
\frac{3H_0^2}{8\pi G_N}\times 0.7
\approx
6\times 10^{-10}\,\mathrm{J\,m^{-3}}.
\]

Set \(\rho_\Omega=\rho_\Lambda\):

\[
|\dot\omega|
=
H_0\sqrt{\Omega_\Lambda}
=
H_\Lambda
\approx
1.8\times 10^{-18}\,\mathrm{s^{-1}}.
\]

So the conformal factor supplies the observed vacuum density **if and only if** it changes on the Hubble time of \(\Lambda\).

That is the matching condition. It is not a derivation of \(\Lambda\).

---

## 4. Rates the tree actually owns

| Source of \(\dot\omega=\dot\Omega/\Omega\) | Rate | \(\rho_\Omega/\rho_\Lambda\) |
|---|---|---|
| Horizon / de Sitter remainder of the womb, \(\Delta\eta\sim c/(a H_\Lambda)\) | \(H_\Lambda\) | \(\sim 1\) |
| Catalogue void radius \(L\sim 30\,\mathrm{Mpc}\) as \(|\nabla\Omega|/\Omega\sim c/L\) | \(\sim 10\,H_0\) | \(\sim 10^2\) |
| IR floor \(m_0=313.1\,\mathrm{MeV}\), \(\dot\omega\sim m_0 c^2/\hbar\) | \(\sim 5\times 10^{23}\,\mathrm{s^{-1}}\) | \(\sim 10^{83}\) |
| Planck–Kerr tick \(\dot\omega\sim c/\ell_{\rm Pl}\) | \(\sim 2\times 10^{43}\,\mathrm{s^{-1}}\) | \(\sim 10^{122}\) |
| Eight-phase reset as a secular Hubble, unknown | \(J_{\rm sec}/\rho\) | not computed |

Spatial gradient on the wall interpolation, length \(L\):

\[
\rho_\Omega^{\rm (grad)}
\sim
\frac{3}{8\pi G_N}
\Bigl(\frac{c}{L}\Bigr)^2
\frac{|\nabla\Omega|^2}{\Omega^2}
\quad
(\text{order of magnitude}).
\]

If \(L=c/H_\Lambda\), again \(\rho\sim\rho_\Lambda\). If \(L=\lambda_{m_0}\), again \(10^{83}\) too large.

**Key.** Matching \(\rho_\Lambda\) picks the horizon scale. Every Superblock micro-scale explodes.

---

## 5. Reciprocal chart and \(w=-1\)

On one womb, \(\hat\Omega\check\Omega=-1\). Near the parent \(\mathscr{I}^+\), \(\hat\Omega\to 0\) linearly in remaining conformal time,

\[
\hat\Omega
\sim
\frac{\eta_\infty-\eta}{\ell_*}.
\]

If \(\ell_*\) is not given, set it equal to the only macroscopic length the isolated patch has, \(c/H_\Lambda\). Then \(\dot\omega\sim H_\Lambda\), \(\rho_\Omega\sim\rho_\Lambda\), and the reciprocal motion can be charted so that \(\ddot\omega\sim-\dot\omega^2\) and \(w_\Omega\sim-1\).

That calculation **succeeds** as a rewrite of a patch that is already de Sitter. It does **not** replace \(\rho_\Lambda\) with a new source. It writes \(\rho_\Lambda\) as a conformal factor whose rate is \(H_\Lambda\).

---

## 6. Verdict

\[
\rho_\Omega
=
\frac{3}{8\pi G_N}
\Bigl(\frac{\dot\Omega}{\Omega}\Bigr)^2
\quad\text{(homogeneous leading term).}
\]

Equals \(\rho_\Lambda\) iff \(\dot\Omega/\Omega=H_\Lambda\).

That equality is true when \(\Omega_A\) is the de Sitter remainder of the womb. It is false, by tens to a hundred orders, if \(\Omega_A\) is slaved to \(m_0\), to \(\ell_{\rm Pl}\), or to a 8-tick without a secular average that has been shown to equal \(H_\Lambda\).

Tau Casimir failed by \(\sim 10^{110}\) at \(7\,h^{-1}\,\mathrm{Mpc}\). This conformal density does not fail that way **if** the rate is the horizon rate. It also does not *explain* \(\Lambda\): it is \(\Lambda\) written as \(\dot\omega\).

Do not put \(\rho_\Omega=\rho_\Lambda\) in the live frame as a derived replacement. Put it as: the womb’s bridging factor carries density \(\rho_\Lambda\) when it tracks \(H_\Lambda\), which is the statement that the isolated patch is vacuum-dominated.

---

## Master key

| Symbol | Meaning |
|---|---|
| \(\Omega,\omega\) | bridging factor; \(\ln\Omega\) |
| \(T^{(\Omega)},\rho_\Omega,w_\Omega\) | conformal stress, density, EoS |
| \(H_\Lambda\) | de Sitter rate of the patch |
| \(\ell_*\) | conformal remainder scale in \(\hat\Omega\sim(\eta_\infty-\eta)/\ell_*\) |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_conformal_factor_density_compute_2026-09-20.md`
