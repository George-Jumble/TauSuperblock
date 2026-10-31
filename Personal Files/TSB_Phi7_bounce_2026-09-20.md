# \(\Phi_7\) bounce

**Date:** 2026-09-20  
**Field:** slot-7 Higgs / twistor fabric.  
**Trigger:** isolated chamber, \(|P_{\rm vac}|\gg P_{\rm rad}\), \(V_{\rm pin}\to 0\).  
**Not derived:** \(\lambda\), \(\Phi_\star\), identity with \(v_{\rm EW}\). Scale available: \(m_0\).

---

## 1. Potential

\[
V(\Phi_7)
=
V_{\rm well}(\Phi_7)
+
V_{\rm pin}(P_{\rm rad};\Phi_7)
+
V_{\rm fric}.
\]

Working well (double well, one real field):

\[
V_{\rm well}
=
\frac{\lambda}{4}
\bigl(\Phi_7^2-\Phi_\star^2\bigr)^2.
\]

Pin (radiation stimulus of Phase-7):

\[
V_{\rm pin}
=
\frac12\kappa_{\rm pin}P_{\rm rad}\,\Phi_7^2,
\qquad
\kappa_{\rm pin}>0.
\]

While \(P_{\rm rad}\) is not negligible the quadratic pin holds \(\Phi_7\) near \(0\). In the chamber \(P_{\rm rad}\to 0\) and \(V_{\rm pin}\to 0\). Friction is the schematic \(m_0\) damping of the old notes, not used in the Euclidean bounce.

**Key.** \(\Phi_7\): fabric field. \(\Phi_\star\): deep-well value. \(\lambda\): quartic, not live. \(\kappa_{\rm pin}\): pin coupling, not live.

False vacuum \(\Phi_7\approx 0\). True vacuum \(\Phi_7=\pm\Phi_\star\) once the pin is off.

---

## 2. Euclidean bounce

Wick-rotate the chamber interior. O(4)-symmetric bounce \(\Phi_7=\phi(\rho)\), \(\rho=\sqrt{\tau_E^2+\mathbf{x}^2}\).

\[
\frac{d^2\phi}{d\rho^2}
+
\frac{3}{\rho}\frac{d\phi}{d\rho}
=
\frac{dV}{d\phi},
\qquad
\phi'(0)=0,
\quad
\phi(\infty)=0.
\]

Action:

\[
S_E
=
2\pi^2
\int_0^\infty
\rho^3
\Bigl(
\tfrac12\phi'^2
+
V(\phi)
\Bigr)
d\rho.
\]

Nucleation rate per volume

\[
\Gamma/V
\sim
m^4\,e^{-S_E/\hbar},
\]

with \(m\) the curvature of \(V\) at the false vacuum.

**Key.** \(\rho\): Euclidean radius. \(S_E\): bounce action. \(\Gamma/V\): rate.

---

## 3. Case R — pin gone, no remnant barrier

\(V_{\rm pin}=0\) and \(V_{\rm well}\) has no barrier between \(0\) and \(\Phi_\star\) if the false point is a *maximum* once the pin drops (the \(\Phi^2\) term in \(V_{\rm well}\) is negative for \(|\Phi|<\Phi_\star\)).

Then \(0\) is unstable. There is **no bounce**. The field rolls classically,

\[
\ddot\Phi_7+3H\dot\Phi_7
=
-V'_{\rm well}(\Phi_7).
\]

Time scale

\[
t_{\rm roll}
\sim
\frac{1}{m_{\rm tach}}
=
\frac{1}{\sqrt{\lambda}\,\Phi_\star}.
\]

If the only live IR scale is used as a stand-in, \(\Phi_\star\sim m_0/c^2\) in mass units, \(t_{\rm roll}\sim\hbar/(m_0 c^2)\sim 2\times 10^{-24}\,\mathrm{s}\). Instant on any cosmological clock. Binding \(B_{7\to i}\) may open as soon as \(|\Phi_7-\Phi_\star|<\varepsilon\).

This is the default chamber story: radiation left, pin off, roll, bind.

---

## 4. Case T — remnant first-order barrier

If a barrier of height \(\varepsilon_{\rm bar}\) and wall tension \(S_1\) remains after the pin drops (extra physics, not in \(V_{\rm well}\) above), thin-wall Coleman:

\[
S_E
=
\frac{27\pi^2 S_1^4}{2\varepsilon^3},
\qquad
\varepsilon
=
V(0)-V(\Phi_\star).
\]

\(\Gamma/V\) is then exponentially small unless \(\varepsilon\) is not small compared with \(S_1^{4/3}\). No live values of \(S_1,\varepsilon\). Do not quote a lifetime.

---

## 5. What is written / what is not

Written: the ODE, \(S_E\), the roll equation, the two cases.  
Not written: a number for \(S_E\), an identity \(\Phi_\star=v_{\rm EW}\), a derivation of \(\lambda\).  
Default for the expansion event: **Case R**. The “bounce” is then a name for the roll off the unpinned origin, not an instanton.

---

## Master key

| Symbol | Meaning |
|---|---|
| \(\Phi_7,\Phi_\star,\lambda\) | fabric, deep well, quartic |
| \(V_{\rm pin}\) | radiation pin \(\propto P_{\rm rad}\) |
| \(S_E\) | Euclidean bounce action |
| \(t_{\rm roll}\) | classical roll time |

---

## Session metadata

- 2026-09-20
- `Personal_Files/TSB_Phi7_bounce_2026-09-20.md`
