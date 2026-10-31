# Session 2026-09-14 — \(T_{00}[f_+]\) and the PK seed \(U\)

**Rule:** define both from objects already locked (\(f_+\), \(W\), Planck–Kerr seed). Do not solve for them from \(\rho_\Lambda\).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(f_+\) | Vacuum waveform \(\iota(v_+)\propto(\pi_{0'}+\pi_{1'})^{-4}\) |
| \(\varphi_{A'B'}(x)\) | Self-dual Maxwell spinor from the Penrose transform of \(f_+\) |
| \(F_{\mu\nu}\) | Maxwell 2-form of that field |
| \(T_{\mu\nu}\) | Maxwell energy-momentum |
| \(T_{00}\) | Energy density in a Prime frame |
| \(t_{00}\) | Dimensionless density after \(U\) is factored out |
| \(U\) | PK energy seed |
| \(\ell_{\mathrm{Pl}}\) | Planck length |
| \(M_{\mathrm{Pl}}\) | Planck mass |
| \(M_{\mathrm{PK}}\) | Corpus PK seed mass \(\sqrt{2}\,M_{\mathrm{Pl}}\) (not required for \(U\) below) |
| \(\ell_{\mathrm{PK}}\) | PK length; working lock \(\ell_{\mathrm{PK}}=\ell_{\mathrm{Pl}}\) |
| \(v_+\) | \(+1\)-eigenvector of \(W\) |
| \(\mathscr{I}\) | Conformal infinity (completed generators only) |

---

## 2. Seed \(U\)

The only dimensionful seed that is not \(\tau\), not \(313.1\,\mathrm{MeV}\), and not \(\rho_\Lambda\) is Planck–Kerr.

\[
U
=
\frac{\hbar c}{\ell_{\mathrm{PK}}},
\qquad
\ell_{\mathrm{PK}}
=
\ell_{\mathrm{Pl}}
=
\sqrt{\frac{\hbar G}{c^3}}.
\]

**Key:** \(U\) is an *energy*. Numerically \(U\approx 1.22\times 10^{19}\,\mathrm{GeV}\) (same order as \(M_{\mathrm{Pl}}c^2\)).

Using \(\ell_{\mathrm{PK}}=\ell_{\mathrm{Pl}}/\sqrt{2}\) from \(M_{\mathrm{PK}}=\sqrt{2}M_{\mathrm{Pl}}\) only rescales \(U^4\) by \(4\). It does not produce \(\rho_\Lambda\). Working lock is \(\ell_{\mathrm{PK}}=\ell_{\mathrm{Pl}}\).

---

## 3. Field from \(f_+\)

Penrose transform (helicity \(+1\), homogeneity \(-4\)):

\[
\varphi_{A'B'}(x)
=
\oint
\pi_{A'}\pi_{B'}\,
f_+\bigl(ix^{CC'}\pi_{C'},\,\pi\bigr)
\,\pi\,d\pi.
\]

**Key:** contour on the \(\mathbb{CP}^1\) of \(\pi_{A'}\) at the point \(x\); \(f_+\) as in the previous note.

Maxwell field from \(\varphi_{A'B'}\) in the usual way. Energy-momentum:

\[
T_{\mu\nu}
=
F_{\mu\alpha}F_{\nu}{}^{\alpha}
-
\tfrac14 g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}.
\]

**Key:** this is the stress of the *unbound* mode. Bound / stopped generators are excluded from \(f_+\) by construction.

---

## 4. Density to feed \(V_\infty\)

Factor the seed:

\[
T_{00}[f_+]
=
U^4\,
t_{00}[f_+].
\]

**Key:** \(t_{00}\) is dimensionless. In units \(\hbar=c=1\), \(U=1/\ell_{\mathrm{Pl}}\) and \(U^4=1/\ell_{\mathrm{Pl}}^4=\hbar c/\ell_{\mathrm{Pl}}^4\) when \(\hbar,c\) are restored as \(\hbar c/\ell_{\mathrm{Pl}}^4\).

Two evaluations of \(t_{00}\):

**Local Maxwell.** \(t_{00}(x)=U^{-4}T_{00}(x)\). For \(f_+\propto(\pi_{0'}+\pi_{1'})^{-4}\) this is the energy of a Robinson / fixed-flag field. It is **not** homogeneous on a cosmological slice. It is not \(\Lambda\).

**Zero mode at \(\mathscr{I}\) (the slot).** Keep only the completed-generator part and average on the celestial sphere and on the six domains:

\[
t_{00}[f_+]
=
\frac{1}{6}
\sum_{a=1}^{6}
\int_{\mathcal{R}}
\mathrm{d}\mu(\pi)\,
N\bigl[\iota(L_{e_a}v_+)\bigr].
\]

**Key:** \(\mathrm{d}\mu\) = Fubini–Study on \(\mathbb{CP}^1\); \(N\) = a dimensionless quadratic norm of the cohomology representative, regularized so the pole of \((\pi_{0'}+\pi_{1'})^{-4}\) is the completed-generator contour, not a spacetime point charge.

Until \(N\) and the contour are fixed, \(t_{00}\) is not a unique finite number.

Default (no extra structure): \(N=|v_+|^2=1\), one domain copy, then

\[
t_{00}=1
\qquad\Rightarrow\qquad
T_{00}
=
\frac{\hbar c}{\ell_{\mathrm{Pl}}^4}
\approx 4.63\times 10^{113}\,\mathrm{J\,m^{-3}}.
\]

**Key:** that is the Planck vacuum. Observed \(\rho_\Lambda\approx 5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\) would require

\[
t_{00}
\sim 1.23\times 10^{-123}.
\]

That factor is **not** produced by \(\mathrm{spec}(W)=\{+1,-1,\pm i\}\), by \(\alpha=1-\log_7 6\), or by \(q=8\). Writing \(8^{-136}\) or \(7^{-144}\) to hit \(10^{-123}\) is numerology and is not used.

---

## 5. What is now fixed vs what remains

| Object | Status |
|--------|--------|
| \(U=\hbar c/\ell_{\mathrm{Pl}}\) | locked |
| \(T_{00}=U^4 t_{00}[f_+]\) | locked as factorization |
| Penrose \(\varphi_{A'B'}[f_+]\) | formula locked |
| \(t_{00}=1\) default | Planck density, not \(\rho_\Lambda\) |
| Regularized celestial norm \(N\) at \(\mathscr{I}\) | **not** unique yet |
| \(t_{00}\sim 10^{-123}\) | **not** derived |

Completing \(\rho_\Lambda\) is no longer “missing \(U\)” or “missing the form of \(T_{00}\).” It is missing a **finite, unique** \(t_{00}\) from the completed-generator contour. That is the cosmological-constant problem in this language, not a missing seed.

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
