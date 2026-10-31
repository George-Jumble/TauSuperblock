# Session 2026-09-14 — \(\varphi[f_+]\) at generic \(x\), and \(T_{00}\) along \(\alpha_{\mathrm{res}}\to\Omega_{\mathrm{res}}\)

**Calculation A, as requested.**

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(f_+(\pi)=c\,(\pi_{0'}+\pi_{1'})^{-4}\) | Locked \(\iota(v_+)\); **depends only on \(\pi\)** |
| \(\omega^A=ix^{AA'}\pi_{A'}\) | Incidence at event \(x\) |
| \(\varphi_{A'B'}(x)\) | Self-dual Maxwell spinor |
| \(\zeta=\pi_{1'}/\pi_{0'}\) | Celestial chart |
| \(\pi\,d\pi\) | \(d\zeta\) in that chart (up to \(2\pi i\)) |
| \(T_{00}\) | Maxwell energy density of \(\varphi\) |

Penrose formula:

\[
\varphi_{A'B'}(x)
=
\oint
\pi_{A'}\pi_{B'}\,
f_+\bigl(\omega(x,\pi),\pi\bigr)
\,\pi\,d\pi.
\]

---

## 2. Result for the locked \(f_+\)

\(f_+\) does not depend on \(\omega\). The integrand at every \(x\) is the same:

\[
\varphi_{00}\propto\oint\frac{d\zeta}{(1+\zeta)^4},
\quad
\varphi_{01}\propto\oint\frac{\zeta\,d\zeta}{(1+\zeta)^4},
\quad
\varphi_{11}\propto\oint\frac{\zeta^2\,d\zeta}{(1+\zeta)^4}.
\]

**Key:** pole at \(\zeta=-1\), order 4.

Residues (computed): all three are **zero**. An order-4 pole of a monomial \(\zeta^k/(1+\zeta)^4\) with \(k\le 2\) has no \(1/\zeta\) term.

Therefore

\[
\varphi_{A'B'}(x)
=
0
\quad\text{for every }x,
\qquad
T_{00}(x)
=
0
\quad\text{along the whole }\alpha_{\mathrm{res}}\to\Omega_{\mathrm{res}}.
\]

**Key:** constant, yes; vacuum energy, no. It is the zero field.

So: with the present \(\iota\), Step A is finished and trivial. Constancy holds because nothing is there.

---

## 3. Why it vanished

\(\iota(v_+)=(v_0\pi_{0'}+v_7\pi_{1'})^{-4}\) never used \(\omega^A\). A photon cohomology class in \(H^1(\mathbb{PT}^+,\mathcal{O}(-4))\) that yields a nonzero Maxwell field must depend on the full twistor \(Z=(\omega,\pi)\), e.g. an elementary state

\[
f_A(Z)
=
\frac{1}{(Z\cdot A)^4}
=
\frac{1}{(\omega_A\alpha^A+\pi_{A'}\beta^{A'})^4}.
\]

**Key:** \(A=(\alpha^A,\beta_{A'})\) is a fixed dual twistor. Then \(\varphi(x)\) is the linearized field of that twistor and **does** depend on \(x\). Energy density of that field falls (Robinson / Coulomb-type), so \(T_{00}\) is **not** constant along a cosmological history.

---

## 4. Verdict

| Question | Answer for locked \(f_+\) |
|----------|---------------------------|
| Is \(\varphi\) defined at generic \(x\)? | Yes: it is \(0\) |
| Is \(T_{00}\) constant on \(\alpha_{\mathrm{res}}\to\Omega_{\mathrm{res}}\)? | Yes: \(0=0\) |
| Is that \(\rho_\Lambda\)? | No |

To go on, \(\iota\) must be enlarged so \(f\) depends on \(\omega\), or \(v_+\) must be mapped to a dual twistor \(A\), not only to a flag \(\pi\). Then recompute \(\varphi(x)\) and \(T_{00}(x)\). Expect a non-constant density unless a new average over \(A\) is introduced.

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
