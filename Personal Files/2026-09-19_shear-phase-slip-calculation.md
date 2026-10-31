# Shear phase slip: calculation

**Session date:** 19 September 2026  
**Task:** Compute domain-embedding shear phase slip and the coherence length it implies.  
**Inputs used:** geometry of relative velocity and a wave / kernel mode. No locked SBT table of \(V_{\rm orb}^{(i)}\) is in the public notes, so \(\beta=\Delta V_{\rm orb}/c\) is scanned.  
**Result:** A Hubble-scale gradient with \(\beta\le 1\) does **not** lose coherence at \(7h^{-1}\,\mathrm{Mpc}\). Slip across that length is \(\lesssim 0.015\,\mathrm{rad}\) even at \(\beta=1\).

---

## Variable key

| Symbol | Meaning |
|---|---|
| \(V_{\rm orb}^{(i)}\) | embedding orbital velocity of domain \(i\) |
| \(\Delta V_{\rm orb}\) | characteristic stagger \(\|V_{\rm orb}^{(i)}-V_{\rm orb}^{(j)}\|\) |
| \(\beta=\Delta V_{\rm orb}/c\) | dimensionless stagger (must be \(<1\) if it is a relative speed in a metric sense) |
| \(L\) | comoving 4D separation |
| \(\lambda\) | comoving wavelength of the mode the kernel is carrying |
| \(k=2\pi/\lambda\) | corresponding wavenumber |
| \(\delta\phi\) | relative phase between two domains across \(L\) |
| \(\ell_C\) | coherence length, defined here by \(\delta\phi(\ell_C)=1\,\mathrm{rad}\) |
| \(d_H=c/H_0\) | Hubble length \(\approx 3000\,h^{-1}\,\mathrm{Mpc}\) |
| \(h\) | \(H_0/(100\,\mathrm{km\,s^{-1}\,Mpc^{-1}})\); numbers below use \(h=0.7\) |

---

## 1. Slip law

A relative embedding boost \(\beta\) tilts null cones and Doppler-shifts a mode of wavelength \(\lambda\). The accumulated phase difference across a comoving interval \(L\) is

\[
\delta\phi
= k\,\beta\,L
= 2\pi\beta\,\frac{L}{\lambda}.
\]

**Key:** this is the leading small-tilt, single-gradient law. It assumes the stagger is spatially uniform in direction over \(L\) and that the kernel inherits the domain cone tilt. No metric fifth circle is used.

Coherence convention used here (order-one, not fitted):

\[
\delta\phi(\ell_C)=1
\qquad\Rightarrow\qquad
\ell_C=\frac{\lambda}{2\pi\beta}.
\]

A \(\pi\)-radian convention only multiplies \(\ell_C\) by \(\pi\).

---

## 2. Hubble-only carrier (the model that fails)

If the only cosmological gradient available is the Hubble scale, set \(\lambda=d_H\approx 3000\,h^{-1}\,\mathrm{Mpc}\). Then

\[
\ell_C=\frac{d_H}{2\pi\beta}.
\]

Wait: \(\ell_C=\lambda/(2\pi\beta)=d_H/(2\pi\beta)\). Even more important is the inverse question: what \(\beta\) would make \(\ell_C=7h^{-1}\,\mathrm{Mpc}\) if one used the cruder estimate \(\ell_C\sim d_H/\beta\)?

| Target \(\ell_C\) | \(\beta\) required by \(\ell_C=d_H/\beta\) |
|---|---|
| \(1h^{-1}\,\mathrm{Mpc}\) | \(3000\) |
| \(5h^{-1}\,\mathrm{Mpc}\) | \(600\) |
| \(7h^{-1}\,\mathrm{Mpc}\) | \(428\) |
| \(10h^{-1}\,\mathrm{Mpc}\) | \(300\) |

All of those \(\beta\) are superluminal if \(\beta=\Delta V/c\). Relativistic SBT stagger (\(\beta\sim 1\)) in this model gives \(\ell_C\sim d_H\sim 3000h^{-1}\,\mathrm{Mpc}\), not 7.

Slip actually accumulated across \(7h^{-1}\,\mathrm{Mpc}\) when \(\lambda=d_H\):

\[
\delta\phi
=2\pi\beta\,\frac{7}{3000}
\approx 0.0147\,\beta
\quad\text{radians}.
\]

| \(\beta\) | \(\delta\phi\) across \(7h^{-1}\,\mathrm{Mpc}\) | degrees |
|---|---|---|
| \(1\) | \(1.47\times 10^{-2}\) | \(0.84^\circ\) |
| \(0.5\) | \(7.3\times 10^{-3}\) | \(0.42^\circ\) |
| \(0.1\) | \(1.47\times 10^{-3}\) | \(0.084^\circ\) |
| \(0.01\) | \(1.47\times 10^{-4}\) | \(0.008^\circ\) |
| \(1.2\times 10^{-3}\) (370 km/s dipole) | \(1.8\times 10^{-5}\) | \(0.001^\circ\) |

That is not kernel breakdown. Hubble-mode shear is negligible on web scales for any legal boost.

---

## 3. What carrier wavelength *would* put \(\ell_C\) at \(7h^{-1}\,\mathrm{Mpc}\)

Invert the slip law with \(L=7h^{-1}\,\mathrm{Mpc}\) and \(\delta\phi=1\):

\[
\lambda_{\rm need}
=2\pi\beta\,L
=2\pi\beta\times 7\,h^{-1}\,\mathrm{Mpc}.
\]

| \(\beta\) | \(\lambda\) that makes \(7h^{-1}\,\mathrm{Mpc}\) the 1-radian scale |
|---|---|
| \(1\) | \(44.0\,h^{-1}\,\mathrm{Mpc}\) |
| \(0.5\) | \(22.0\,h^{-1}\,\mathrm{Mpc}\) |
| \(0.3\) | \(13.2\,h^{-1}\,\mathrm{Mpc}\) |
| \(0.1\) | \(4.40\,h^{-1}\,\mathrm{Mpc}\) |

For a \(\pi\)-radian convention multiply \(\lambda_{\rm need}\) by \(\pi\).

So: shear produces a web-scale \(\ell_C\) only if the kernel is already carrying a mode of tens of \(h^{-1}\,\mathrm{Mpc}\) (if domains are relativistic) or a few \(h^{-1}\,\mathrm{Mpc}\) (if \(\beta\sim 0.1\)). That mode must come from somewhere else — embedding map, substratum occupation gradient, or the definition of \(\mathcal K_{ij}\). It does not come from \(H_0\) plus \(\beta<1\).

---

## 4. If the stagger itself has a spatial gradient

Replace uniform \(\beta\) by a shear rate. Let the embedding angle change across 4D as

\[
\beta_{\rm eff}(L)
=\frac{\Omega\alpha}{c}\,L,
\]

**Key:** \(\Omega\) is internal angular rate of the supersphere motion; \(\alpha=d\theta/d\ell\) is how many radians of embedding angle a comoving megaparsec maps to.

Then

\[
\delta\phi
=2\pi\frac{\Omega\alpha}{c}\frac{L^2}{\lambda},
\qquad
\ell_C
=\sqrt{\frac{\lambda c}{2\pi\Omega\alpha}}.
\]

This *can* produce a short \(\ell_C\) from a long \(\lambda\), because of the \(L^2\). It also introduces two new SBT quantities, \(\Omega\) and \(\alpha\), that are not yet fixed by a published \(V_{\rm orb}\) table. Without those numbers this line is a template, not a prediction.

---

## 5. What is actually calculated vs what is not

Calculated:

- the slip law \(\delta\phi=2\pi\beta L/\lambda\),
- \(\delta\phi(7h^{-1}\,\mathrm{Mpc})\) for a Hubble carrier: \(\approx 0.015\beta\) rad,
- \(\beta\) required in a Hubble-only model: \(\sim 400\), illegal as a speed,
- the carrier \(\lambda(\beta)\) that would put coherence at 7 \(h^{-1}\,\mathrm{Mpc}\).

Not calculated, because SBT has not locked them:

- the six numbers \(V_{\rm orb}^{(i)}\),
- the embedding gradient \(\alpha\),
- the internal rate \(\Omega\),
- which mode \(\lambda\) the kernel actually carries.

Until those exist, shear phase slip is a real mechanism with a failed Hubble-only evaluation. It is not yet a derivation of the web scale.

---

## 6. Sentence for drafts

> Relative domain boosts induce a phase slip \(\delta\phi=2\pi\beta L/\lambda\). On Hubble modes that slip is \(\sim 0.015\beta\) radians across \(7h^{-1}\,\mathrm{Mpc}\) and does not fracture the web. A shear origin of that scale requires a kernel carrier of order \(2\pi\beta\times 7h^{-1}\,\mathrm{Mpc}\), or a spatial gradient of the embedding velocity, neither of which is fixed by \(\beta\) alone.

---

## File location

`Tau-Superblock-Universe/Personal-Files/2026-09-19_shear-phase-slip-calculation.md`
