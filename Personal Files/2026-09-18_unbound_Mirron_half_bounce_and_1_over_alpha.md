# Session log: Can the unbound Mirron absorb \(1/\alpha\) as it absorbs the half-bounce?

- **Session date:** Friday, 2026-09-18
- **Question:** Shouldn’t the \(1/\alpha\) value, like the kinematic value of the half-bounce, be absorbed by the unbound Mirron?
- **Short answer:** The half-bounce *is* absorbed: it is the statement \(r_{\mathrm{M}}=\hbar c/\Delta_{\mathrm{TEP}}\), so the kinematic action of a radial half-tick is \(1\) (in units of \(\hbar\)). The Coulomb self-energy of one charge \(e\) on the same isolated 2-surface, in units of \(\Delta_{\mathrm{TEP}}\), is \(\alpha_{\mathrm{fs}}\) (or \(\alpha_{\mathrm{fs}}/2\)). That identity holds for **any** radius. It does not let the unbound Mirron eat \(1/\alpha\) as a second kinematic factor. One surface cannot absorb both “action \(=1\)” and “action \(=1/\alpha\)” unless \(\alpha=1\). \(1/\alpha\) is the *ratio* of bounce energy to Coulomb dressing, not a length that disappears into \(r_{\mathrm{M}}\).
- **This file:** `Personal Files/2026-09-18_unbound_Mirron_half_bounce_and_1_over_alpha.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| Unbound Mirron | Isolated \(\Sigma_{\mathrm{M}}\), not packed; no lattice neighbours. |
| Half-bounce | Radial tick \(r_{\mathrm{M}}/c\) (centre to surface). Diameter tick remains \(2r_{\mathrm{M}}/c\). |
| \(S_{1/2}=\Delta_{\mathrm{TEP}}(r_{\mathrm{M}}/c)/\hbar\) | Kinematic action of the half-bounce. |
| \(U_{\mathrm{C}}\) | Electrostatic self-energy of charge \(e\) on a sphere of radius \(r_{\mathrm{M}}\). |
| \(C=4\pi\varepsilon_0 r_{\mathrm{M}}\) | Isolated-sphere capacitance (SI). |
| \(\alpha_{\mathrm{fs}}=e^2/(4\pi\varepsilon_0\hbar c)\) | Fine-structure constant. Input in this identity. |
| \(r_e=\alpha_{\mathrm{fs}}\hbar c/\Delta_{\mathrm{TEP}}=\alpha_{\mathrm{fs}} r_{\mathrm{M}}\) | Classical EM length attached to the same energy. Not equal to \(r_{\mathrm{M}}\). |

---

## 1. What the half-bounce absorbs

Lock \(r_{\mathrm{M}}=\hbar c/\Delta_{\mathrm{TEP}}\). Then
\[
S_{1/2}=\frac{\Delta_{\mathrm{TEP}}\,r_{\mathrm{M}}}{\hbar c}=1.
\]
**Key:** the kinematic factor of the half-bounce is absorbed *by the definition of the mirror radius*. That is why \(r_{\mathrm{M}}\) is the reduced Compton length of the TEP floor. There is nothing left to absorb on the kinematic side.

(If one uses \(hc\) instead of \(\hbar c\), \(S_{1/2}=2\pi\). Still \(\mathcal{O}(1)\), still used up in the same lock.)

---

## 2. What the Coulomb energy of the unbound mirror is

Isolated sphere, SI:
\[
U_{\mathrm{C}}=\frac{e^2}{8\pi\varepsilon_0 r_{\mathrm{M}}}\quad\text{(self-energy \(\tfrac12 QV\))}
\]
or
\[
U_{\mathrm{C}}'=\frac{e^2}{4\pi\varepsilon_0 r_{\mathrm{M}}}\quad\text{(omitting \(\tfrac12\))}.
\]
Divide by the bounce energy:
\[
\frac{U_{\mathrm{C}}'}{\Delta_{\mathrm{TEP}}}
=\frac{e^2}{4\pi\varepsilon_0 r_{\mathrm{M}}}\cdot\frac{r_{\mathrm{M}}}{\hbar c}
=\frac{e^2}{4\pi\varepsilon_0\hbar c}
=\alpha_{\mathrm{fs}}.
\]
**Key:** this is the *definition* of \(\alpha_{\mathrm{fs}}\), written on a sphere of radius \(r_{\mathrm{M}}\). The same ratio on a sphere of radius \(R\) is still \(\alpha_{\mathrm{fs}}\). The unbound Mirron does not compute \(137\). It hosts the same ratio every charged sphere hosts.

So
\[
\frac{\Delta_{\mathrm{TEP}}}{U_{\mathrm{C}}'}=\frac{1}{\alpha_{\mathrm{fs}}}\approx 137.
\]
That is what “\(1/\alpha\) on the unbound Mirron” *is*: bounce energy over Coulomb dressing. It is not a second kinematic lock.

---

## 3. Why it cannot be absorbed the same way

Absorption of the half-bounce used up the only short length:
\[
r_{\mathrm{M}}=\frac{\hbar c}{\Delta_{\mathrm{TEP}}}.
\]
Absorbing \(1/\alpha\) the same way would demand a *second* length,
\[
r_{\mathrm{EM}}=\frac{\alpha_{\mathrm{fs}}\hbar c}{\Delta_{\mathrm{TEP}}}=\alpha_{\mathrm{fs}} r_{\mathrm{M}},
\]
the classical radius attached to \(\Delta_{\mathrm{TEP}}\). Those two lengths differ by \(137\). One unbound 2-surface cannot be both unless \(\alpha_{\mathrm{fs}}=1\).

That is the classical-electron-radius lesson: electromagnetism plus a mass defines \(r_e=\alpha\lambda_{\bar{\mathrm{C}}}\), not \(\lambda_{\bar{\mathrm{C}}}\) itself.

---

## 4. Nearby number that is not a result

\[
\alpha_{\mathrm{fs}}\Delta_{\mathrm{TEP}}\approx 2.28\,\mathrm{MeV}
\]
sits next to \(m_u\approx 2.16\,\mathrm{MeV}\). Relative miss \(\approx 6\,\%\). Different objects (current-quark mass vs Coulomb dressing of the TEP). Logged as T13-class, not used.

\(\Delta_{\mathrm{TEP}}/\alpha_{\mathrm{fs}}\approx 43\,\mathrm{GeV}\) is not a locked TSB scale.

---

## 5. Direct answer

No. The unbound Mirron already absorbed the half-bounce by being Compton-sized. \(1/\alpha\) is the ratio of that bounce energy to the Coulomb self-energy of a charge \(e\) on the same surface. Writing the ratio on \(\Sigma_{\mathrm{M}}\) does not retire \(\alpha_{\mathrm{fs}}\) as data and does not give the mirror a second job as an EM fibre.

Status: T1 unchanged. \(\alpha_{\mathrm{fs}}\) remains seed data.

---

*End of session note — 2026-09-18 unbound Mirron and \(1/\alpha\).*
