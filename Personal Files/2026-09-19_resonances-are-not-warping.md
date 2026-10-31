# Harmonic resonances on a circle are not warping

**Session date:** 19 September 2026  
**Question:** Aren’t harmonic resonances on the circle “warping the circle”?  
**Short answer:** No. On a metric \(S^1\), harmonics *are* the Kaluza–Klein tower. Warping is a change in the background metric. Naming the tower does not hide it.

---

## Variable key

| Symbol | Meaning |
|---|---|
| \(R\) or \(\tau\) | proper radius / circumference scale of a metric circle |
| \(\phi\) or \(y\) | coordinate along the extra dimension |
| \(n\) | integer harmonic / KK index |
| \(m_n\) | four-dimensional mass of mode \(n\) |
| \(ds^2\) | line element |
| \(A(y)\) | warp factor in a Randall–Sundrum–type metric |
| \(\psi_n(y)\) | extra-dimensional wavefunction of mode \(n\) |
| \(\Phi(x)\) | four-dimensional field after reduction |
| \(V_{\rm Cas}(R)\) | Casimir / one-loop potential that can stabilize \(R\) |
| \(h_{\mu\nu}\) | 4D graviton perturbation |

---

## 1. Two different operations

**Resonance / harmonic on a circle**

A field on a flat circle of radius \(R\) has a complete set of standing waves

\[
\Phi(x,\phi)=\sum_{n\in\mathbb{Z}}\Phi_n(x)\,e^{in\phi},\qquad \phi\sim\phi+2\pi.
\]

Each coefficient \(\Phi_n(x)\) is a 4D field with mass

\[
m_n=\frac{|n|}{R}\qquad\text{(natural units; restore \(\hbar c\) as needed).}
\]

Those \(\Phi_n\) *are* the Kaluza–Klein particles. “7-fold harmonic” just means “keep the \(n=\pm 7\) terms, or a \(\mathbb{Z}_7\) selection rule.” It does not change the background geometry and it does not move \(R\).

**Warping**

Warping is a property of the *metric*, not of the excitations. The standard warped extra-dimension line element is

\[
ds^2=e^{-2A(y)}\,g_{\mu\nu}(x)\,dx^\mu dx^\nu+dy^2.
\]

The function \(A(y)\) multiplies the 4D metric by a position-dependent redshift. A mode’s 4D mass then comes from an overlap integral

\[
m_n^2=\frac{\displaystyle\int dy\,e^{-2A(y)}\,(\partial_y\psi_n)^2+\cdots}
{\displaystyle\int dy\,e^{-2A(y)}\,\psi_n^2},
\]

not from \(n/R\) on a flat circle. That is why Randall–Sundrum can put a TeV threshold on a slice even when the proper length of the extra dimension is not a TeV inverse. The warp factor changes the measure and the wavefunction overlap with our slice.

Resonances live *on* a geometry. Warping *is* the geometry.

---

## 2. Why the slogan fails numerically

Take Tav as a metric circle with

\[
\tau=7h^{-1}\,\mathrm{Mpc}\approx 10\,\mathrm{Mpc}.
\]

Flat harmonics then have

\[
m_n=\frac{n\,\hbar c}{\tau}\sim n\times 6\times 10^{-31}\,\mathrm{eV}.
\]

A “7-fold resonance” is

\[
m_7\sim 4\times 10^{-30}\,\mathrm{eV}.
\]

Laboratory gravity needs the lightest extra-dimensional gravitational mode heavier than about

\[
\frac{\hbar c}{30\,\mu\mathrm{m}}\sim 7\times 10^{-3}\,\mathrm{eV}
\]

or else Newton’s law is modified inside the torsion-balance window. The 7-fold harmonic is still thirty orders of magnitude too light. Selecting \(n=7\) instead of \(n=1\) gains a factor of 7, not a factor of \(10^{28}\).

Harmonics do not warp the circle. They populate it.

---

## 3. What resonances *can* do, honestly

These are real effects. None of them is RS warping.

**A. They are the KK spectrum.**  
If gravity propagates on the circle, every allowed \(n\) is a 4D spin-2 (or spin-0/1, depending on polarization) particle. Inverse-square-law tests, stellar cooling, and cosmological gravitational-wave backgrounds all see that tower unless the overlap with ordinary matter is almost zero.

**B. They can stabilize the radius.**  
A Casimir or winding sum

\[
V_{\rm Cas}(R)=\frac{C_{\rm spectrum}}{R^4}+\cdots
\]

can give \(V'(R)=0\). That freezes \(R\). It does not redshift the remaining modes down from \(1/R\). A stabilized 10 Mpc circle is still a 10 Mpc circle.

**C. They can impose selection rules.**  
A \(\mathbb{Z}_7\), octonionic, or CT boundary condition can project out some \(n\). The surviving masses remain \(n_{\rm allowed}/R\). Projection \(\neq\) warping.

**D. They can dress other fields.**  
A standing-wave condensate can generate an *effective* metric for a probe field, analog-gravity style. That is a legitimate research move — and it is a new derivation. You then owe:

- which field forms the condensate,
- the effective \(g_{\mu\nu}^{\rm (eff)}\) felt by gravitons,
- why ordinary matter does not source light KK gravitons,
- why the effective 4D Newton law is intact from microns to AU.

Until those four items exist, “the harmonics warp the circle” is a metaphor.

---

## 4. What an actual decoupling mechanism has to do

To keep a metric extra dimension of size \(\sim 10\,\mathrm{Mpc}\) and still pass torsion-balance tests, one of the following must be derived, not named.

**1. Warp the metric.**  
Write \(A(y)\) such that the graviton wavefunctions that couple to 4D stress-energy have \(m\gtrsim 10^{-2}\,\mathrm{eV}\) or exponentially small brane overlap. That is Randall–Sundrum / soft-wall language. A Fourier series on a flat \(S^1\) is not that metric.

**2. Localize gravity away from the circle.**  
Put ordinary matter on a brane or in a potential well so that \(\int dy\,\psi_n(y)\rho_4(y)\) is negligible for all light \(n\). Then you must explain how a 10 Mpc Tav scale still appears in the cosmic web — because the web is made of the same matter that was just decoupled from those modes.

**3. Deny that gravitons propagate in \(\phi\).**  
Then \(\phi\) is an internal phase / gauge / topological coordinate. Harmonics are internal quantum numbers, not extra-dimensional momenta. This evades the micron bound *because there is no metric \(S^1\) for gravity to wrap*. It also means the measure \(\int d^5x\sqrt{-g_5}R_5\) with \(g_{\phi\phi}=R^2\) is the wrong starting point, or must be rewritten so that \(g_{\phi\phi}\) is not a spacetime radius.

**4. Give the circle a tiny effective proper length for gravity only.**  
That is again a warped or disformal metric: gravity sees \(R_{\rm grav}\lesssim 30\,\mu\mathrm{m}\) while some other sector sees a 10 Mpc coherence length. Two scales, two couplings. Write both.

Option 3 is the internally consistent TSB reading. Options 1, 2, and 4 are possible metric theories, but they are extra structure. Harmonics alone are none of the four.

---

## 5. A sharp diagnostic sentence for drafts

Use this test in print:

> If the 4D mass of the first graviton harmonic is \(m=n\hbar c/\tau\) with \(\tau\sim 10\,\mathrm{Mpc}\), the extra dimension is flat and unwarped.  
> If the 4D mass is set by a warp factor \(A(y)\) or by a vanishing overlap \(\langle\psi_n|\rho_4\rangle\), a decoupling mechanism exists and must be shown.  
> If there is no graviton harmonic because \(\phi\) is not a metric direction, Tav is an internal coordinate.

Resonances decide *which integers appear*. They do not decide *which of those three sentences is true*.

---

## File location

`Tau-Superblock-Universe/Personal-Files/2026-09-19_resonances-are-not-warping.md`
