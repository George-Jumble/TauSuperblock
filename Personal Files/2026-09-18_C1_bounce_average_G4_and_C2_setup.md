# Session log: C1 bounce average for \(G_4\); C2 setup

- **Session date:** Friday, 2026-09-18
- **Charge:** Execute C1. Name \(N_{\mathrm{dom}}\), tick, deposit, and which \(\langle\gamma\rangle\). Hit or miss. Only then C2.
- **Short answer:** C1 is a **miss** for the measured Newton constant. The only dimensionally legal bounce+cylinder formula that does not smuggle \(\ell_P\) or \(G\) is
  \[
  G_4^{\mathrm{C1}}=\frac{G_5}{2\pi R_\tau},\qquad
  G_5=\frac{c^3 r_{\mathrm{M}}^3}{\hbar},
  \]
  i.e. 5D Planck length \(=r_{\mathrm{M}}\), compactified on the Tav circle with standard period \(2\pi\). Numerically
  \[
  G_4^{\mathrm{C1}}/G_{\mathrm{N}}\approx 0.49\quad(h=0.70).
  \]
  Off by a factor two. \(\langle\gamma\rangle_{\mathrm{C1}}=1\) (Prime-frame deposit; Scheme A \(\gamma_u=1\)). Quark \(\langle\gamma\rangle_6\) is **not** this symbol (T7 stays split). Because C1 misses, **\(G_4\) is data** under the resolution note. C2 at leading order is \(f=0\). Prime-frame clocks do not see a TSB \(\dot\alpha\) from staggered \(\beta_i\). A dipole / other-domain residual remains a search, not a derivation of \(\alpha_{\mathrm{fs}}\).
- **This file:** `Personal Files/2026-09-18_C1_bounce_average_G4_and_C2_setup.md`

---

## Complete variable and function key

| Symbol | Meaning |
|---|---|
| \(G_{\mathrm{N}}\) | Measured Newton constant \(6.67430\times 10^{-11}\,\mathrm{m}^3\mathrm{kg}^{-1}\mathrm{s}^{-2}\). |
| \(G_4^{\mathrm{C1}}\) | Bounce / cylinder candidate. |
| \(G_5\) | 5D Newton constant. Units \(L^4 M^{-1}T^{-2}\). |
| \(r_{\mathrm{M}}=\hbar c/\Delta_{\mathrm{TEP}}\) | Clock radius. Only short length allowed in C1. |
| \(R_\tau=7\,h^{-1}\,\mathrm{Mpc}\) | Cylinder radius. Only long length allowed in C1. |
| \(h\) | \(H_0\) in units \(100\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\). Corpus default \(0.70\). |
| \(N_{\mathrm{dom}}=6\) | Domain count. Not used in the headline \(2\pi\) reduction. |
| \(N_{\mathrm{ph}}=8\) | Phase count. Not used in C1 (tick already encoded in \(r_{\mathrm{M}}\)). |
| \(\Delta_{\mathrm{TEP}}\) | Deposit energy of one bounce in the Prime rest frame. |
| \(\Delta t_\tau=2r_{\mathrm{M}}/c\) | Diameter tick. Sets the clock; cancelled against \(\Delta_{\mathrm{TEP}} r_{\mathrm{M}}=\hbar c\) and does not appear in \(G_5\). |
| \(\langle\gamma\rangle_{\mathrm{C1}}\) | Lorentz factor of the deposit that enters C1. Set to \(1\). |
| \(\langle\gamma\rangle_6^{\mathrm{q}}\) | Quark-increment arithmetic mean \(\approx 1.37\times 10^4\). **Not** used in C1. |
| \(\langle\gamma^{-1}\rangle_6^{\mathrm{q}}\approx 0.247\) | Inverse-mass average. Control only. |
| \(\ell_P=\sqrt{\hbar G_{\mathrm{N}}/c^3}\) | **Output side only.** Not an input to \(G_4^{\mathrm{C1}}\). |
| \(f(\beta_i,\theta_{ij})\) | C2 residual \(\delta\alpha_i/\alpha\). |
| \(G_4^{\mathrm{C1}}/G_{\mathrm{N}}\) | Hit if \(=1\) with a prefactor that is derived, not chosen. |

---

## C1. Named average

### Inputs (no \(G\), no \(\ell_P\))

\[
\hbar,\; c,\; r_{\mathrm{M}},\; R_\tau,\; N_{\mathrm{dom}}=6.
\]
Deposit: one bounce in Prime carries \(\Delta_{\mathrm{TEP}}=\hbar c/r_{\mathrm{M}}\).  
Tick: \(\Delta t_\tau=2r_{\mathrm{M}}/c\).  
These two fix the Mirron scale. They do not add a second short length.

### 5D coupling from that scale

The only 5D Newton constant with the right units built from \(c,\hbar,r_{\mathrm{M}}\) is
\[
G_5=\frac{c^3 r_{\mathrm{M}}^3}{\hbar}.
\]
**Key:** this says the 5D Planck length *is* \(r_{\mathrm{M}}\). That is an axiom of C1, not a fit.

### Compactification on the cylinder

Standard circle, \(\theta\sim\theta+2\pi\), radius \(R_\tau\):
\[
G_4^{\mathrm{C1}}=\frac{G_5}{2\pi R_\tau}=\frac{c^3 r_{\mathrm{M}}^3}{2\pi\,\hbar\,R_\tau}.
\]
**Key:** \(2\pi\) is the period of \(\theta\), the same period used in the Einstein–dilaton hop. It is not replaced by \(\pi\) or by \(N_{\mathrm{dom}}\) to chase \(G_{\mathrm{N}}\).

### Which \(\langle\gamma\rangle\)

Prime is at rest in Scheme A. The deposit that we measure as 4D gravity in Prime is the Prime deposit:
\[
\langle\gamma\rangle_{\mathrm{C1}}=1.
\]
Quark \(\langle\gamma\rangle_6^{\mathrm{q}}\) stays in the \(V_{\mathrm{orb}}\) note. It is not inserted here (T7).

### Number (\(h=0.70\), \(R_\tau=10\,\mathrm{Mpc}\), \(r_{\mathrm{M}}=6.302\times 10^{-16}\,\mathrm{m}\))

\[
\frac{G_4^{\mathrm{C1}}}{G_{\mathrm{N}}}\approx 0.494.
\]
Equivalent: \(L_{\mathrm{eff}}=\sqrt{r_{\mathrm{M}}^3/(2\pi R_\tau)}\approx 1.13\times 10^{-35}\,\mathrm{m}\) versus \(\ell_P\approx 1.62\times 10^{-35}\,\mathrm{m}\).

\(h\) in \(\{0.674,\,0.70,\,0.73\}\) moves the ratio by \(\pm 5\,\%\). It does not close a factor two.

### Controls (not headline)

| Prefactor instead of \(1/(2\pi)\) | \(G_4/G_{\mathrm{N}}\) (\(h=0.70\)) | Status |
|---|---|---|
| \(1\) | \(3.11\) | drops the period |
| \(1/\pi\) | \(0.99\) | period halved; not derived |
| \(1/N_{\mathrm{dom}}=1/6\) | \(0.52\) | six copies, no \(2\pi\) |
| \(1/(2\pi N_{\mathrm{dom}})\) | \(0.082\) | both suppressions |
| \(1/(2\pi)\times\langle\gamma^{-1}\rangle_6^{\mathrm{q}}\) | \(0.12\) | uses the wrong \(\langle\gamma\rangle\) |

The row \(1/\pi\) looks like a hit and is **not used**. That would be T13-class.

### Verdict

**Miss.** Factor two with the derived \(2\pi\). The combination \(r_{\mathrm{M}}^3/R_\tau\) is the right *order* of Planck area. Order is not \(G_{\mathrm{N}}\). Under the resolution note, **\(G_4\) is data**.

C1 has named \(\langle\gamma\rangle_{\mathrm{C1}}=1\). C2 may run.

---

## C2. Residuals after \(\langle\gamma\rangle_{\mathrm{C1}}=1\)

\(\alpha_{\mathrm{fs}}\) is seed data. Prime is at rest. Leading residual:
\[
f(0,\theta)=0,\qquad
\frac{\delta\alpha_u}{\alpha}=0.
\]
Prime-frame clocks bound \(\dot\alpha/\alpha\) and do not constrain other-domain \(\alpha_i\) until there is a mixing channel.

A first non-zero ansatz (not fitted, for killing):
\[
\frac{\delta\alpha_i}{\alpha}=\eta\,(\gamma_{iu}-1)=\eta\bigl(\gamma_i\gamma_u(1-\beta_i\beta_u\cos\theta_{iu})-1\bigr)=\eta(\gamma_i-1)
\]
because \(\beta_u=0\), \(\gamma_u=1\). **Key:** \(\eta\) is a mixing amplitude, \(\lvert\eta\rvert\le 1\).

Then \(\delta\alpha_d/\alpha=\eta(2.176-1)\approx 1.18\eta\), and heavy flavours are \(\eta\gamma_i\gg\eta\). That is already excluded as a *visible* sector shift unless \(\eta\) is tiny (no other-domain QED in the lab). For a cosmic dipole from a small Prime contamination by domain \(d\),
\[
\Bigl\lvert\frac{\delta\alpha}{\alpha}\Bigr\rvert_{\mathrm{dip}}\sim\lvert\eta_{\mathrm{mix}}\rvert\times\mathcal{O}(1).
\]
Existing spatial \(\alpha\) bounds (white dwarfs / quasars, part in \(10^{6}\)–\(10^{7}\) at best; laboratory much tighter on *time* drift) then cap \(\eta_{\mathrm{mix}}\) in Prime. C2 does not produce \(\alpha_{\mathrm{fs}}\) and does not rescue C1.

---

## Ledger

| Item | Result |
|---|---|
| C1 formula | \(G_4=c^3 r_{\mathrm{M}}^3/(2\pi\hbar R_\tau)\) |
| \(\langle\gamma\rangle_{\mathrm{C1}}\) | \(1\) |
| \(G_4^{\mathrm{C1}}/G_{\mathrm{N}}\) | \(0.49\) (\(h=0.70\)) |
| Hit? | No |
| \(G_4\) status | Data |
| C2 leading \(f\) | \(0\) in Prime |
| C2 as \(\alpha_{\mathrm{fs}}\) derivation | No |

---

*End of session note — 2026-09-18 C1 miss; \(G\) data; C2 \(f=0\) at leading order.*
