# Session 2026-09-20 — Neutrinos as Causal Stimulators of Transient Virtual-Pair Bonding via Three-Harmonic-Phase Braiding

**Framework**: Unified Tav–Superblock (TSB) Cosmology  
**Date**: 2026-09-20  
**Task**: Examine the neutrino as a possible *causal* element in the stimulation of *transient bonding* of a virtual pair. Convert the outside triple-helix braid paper into TSB language. Identify the braid with passage through three harmonic phases of a neutrino set relative to three harmonic phases of an anti-neutrino set.

**Outside paper (converted, not adopted as TSB premise)**:  
Robert Weber, *Geometric Unification of Neutrino Decoherence: The Triple-Helix Braid Framework*, Zenodo 20721653 / 20732605 (June 2026). Companion geometric-helix notes: neutrino as three force-lines at \(120^\circ\); photon as open double helix at \(180^\circ\); head-to-tail \(180^\circ\) opposition blocking annihilation; odd-number braid enforcing a chiral leftover.

**Locked TSB statements used**:
- Photons *and neutrinos* stimulate the Higgs field (Phase 7) to produce virtual particles whose angular momentum curves and compresses spacetime (2026-07-21).
- Bound EM = rebound stopped at the Present; unbound EM = completed \(\mathcal{P}\leftrightarrow\mathcal{F}\). Neutrinos sit near the unbound limit with a small residual \(L\) (geometric-lag mass, not a Higgs rest mass of the SM type).
- TEP without \(S^1_\tau\) and without a KK fifth dimension (session earlier today): local reset occupancy forbidden; \(\Phi_7\) is scrape / Mirron / Higgs fabric; \(\Phi_8\) is reset seam; six domain letters from \((\mathbb{Z}/7\mathbb{Z})^\times\).
- \(\Delta_{\mathrm{Tav}}=E_g\approx 313.1\,\mathrm{MeV}\) is inertial colour dressing, not a \(0^{++}\) glueball pole.
- \(\alpha=1-\log_7 6\approx 0.079218\).
- Mirron / PK-Mirron terminology.

**Explicitly not used as load-bearing**: \(\tau\approx 7\,h^{-1}\mathrm{Mpc}\), compact \(\theta\), \(R_5(t)\), Weber’s “5D gravitational shear across a KK circle” as a metric fifth dimension. Shear is rewritten as internal triad mismatch plus scrape coupling.

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(\nu_X\), \(\bar\nu_X\) | Neutrino / anti-neutrino of generation \(X\in\{e,\mu,\tau\}\) |
| \(\mathcal{T}_\nu=\{1,4,2\}\) | Neutrino harmonic triad; ordered 1-4-2 block of the \(142857\) cycle |
| \(\mathcal{T}_{\bar\nu}=\{8,5,7\}\) | Anti-neutrino harmonic triad; ordered 8-5-7 block of the same cycle |
| \(\Phi_k\) | Clockwork letter, \(k=1,\ldots,8\) |
| \(\Phi_7\) | Scrape / Higgs fabric / PK-Mirron channel (not a seventh spacetime) |
| \(\Phi_8\) | Reset / identity / \(\mathcal{P}\leftrightarrow\mathcal{F}\) seam |
| \(D_a\), \(a=1,\ldots,6\) | Co-located \(3+1\)D domains on \(\mathbb{S}_{\mathrm{SB}}\) |
| \(b_\nu(t)\) | Neutrino braid word: ordered occupancy of \(\mathcal{T}_\nu\) at clockwork step \(t\) |
| \(b_{\bar\nu}(t)\) | Anti-neutrino braid word on \(\mathcal{T}_{\bar\nu}\) |
| \(\sigma_j\) | Artin generator of \(B_3\) (crossing of strands \(j\) and \(j+1\)); \(j=1,2\) |
| \(B_3\) | Braid group on three strands |
| \(\mathrm{trefoil}\) | Closed \((2,3)\)-torus knot; image of a pure 3-braid with odd writhe |
| \(\gamma_{\nu}\) | Neutrino world-line / null-like generator (small residual \(L\)) |
| \(f_\nu(Z)\) | Twistor waveform of that generator |
| \(\lvert\langle H\rangle_7\rvert^2\) | Local intensity of the Phase-7 Higgs / scrape fabric |
| \(\Gamma_{\mathrm{virt}}^{(\nu)}\) | Rate of transient virtual-pair nucleation stimulated by a neutrino braid |
| \(\Pi_{\mathrm{pair}}(\Delta t)\) | Transient bonding projector; lives one scrape tick, then dissolves |
| \(e^-e^+\) (or \(q\bar q\)) | Prototype virtual pair; two strands, one from each triad, opposed by half-cycle |
| \(\theta_{\mathrm{opp}}=\pi\) | Opposition angle of a would-be annihilating pair (\(180^\circ\); three steps of a six-cycle) |
| \(\theta_{\mathrm{tri}}=2\pi/3\) | Intra-triad braid angle (\(120^\circ\); two steps of a six-cycle) |
| \(\Delta L_{\mathrm{virt}}\) | Angular momentum deposited by one transient pair into the Mirron / Weyl budget |
| \(\ell_0\) | Elementary Mirron-inversion angular-momentum quantum |
| \(\mathcal{C}_{\mathrm{constr}}\) | Local bound-field density constraint \(\lvert m\rvert/\lvert V\rvert\) |
| \(\mathcal{F}_{\mathrm{TEP}}\) | TEP selection factor (kills local \(\Phi_8\) occupancy) |
| \(\lambda_{\mathrm{H}\nu}\) | Geometric Higgs–neutrino scrape coupling (fixed by \(G_2\) + \(1/7\), not a free fit) |
| \(\Delta_{\mathrm{Tav}}=E_g\) | Dressing quantum \(\approx 313.1\,\mathrm{MeV}\) |
| \(D\) | Weber-style integrity parameter, rewritten without a KK radius |
| \(\xi_{\star}\) | Dimensionless triad-shear constant (defined below; IceCube knee used only as an optional IR anchor, not as a KK length) |
| \(E_\nu\) | Neutrino energy |
| \(w_\nu\) | Instantaneous writhe / winding of the neutrino 3-braid |
| \(w_0\) | Writhe that closes \(\mathcal{T}_\nu\) without local reset |
| \(\tau_{\mathrm{tick}}\) | Duration of one scrape tick (Phase-7 opening); not the Mpc circle |
| \(\mathcal{P},\mathcal{F},\mathcal{N}\) | Absolute Past, Absolute Future, Present stop-slice |
| \(L_\nu\) | Residual angular momentum of the neutrino itself (small; geometric lag) |

---

## 2. What the outside paper contributes, and what TSB keeps

Weber’s claims, in his own geometry:

1. A neutrino is three vibrational force-lines braided at \(120^\circ\) (electron / positron / electron in the water-detector companion; more generally three helical strands).
2. A photon is an *open* two-line helix locked at \(180^\circ\).
3. Head-to-tail \(180^\circ\) opposition stops a pair from annihilating while the braid remains closed and odd.
4. Flavor change is mechanical unbraiding under an external shear.
5. Energy stiffens the helix (larger amplitude / radius) against that shear.
6. IceCube \(\sim 30\,\mathrm{TeV}\) is offered as the stiffening knee for Earth-diameter transit.

TSB conversion (this session):

- The three strands are **not** extra force-fields and **not** a KK fifth coordinate. They are **ordered occupancy of one harmonic triad** of the \(142857\) cycle.
- The two interlocking triads \(\{1,4,2\}\) and \(\{8,5,7\}\) *are* the neutrino set and the anti-neutrino set.
- Braiding **is** passage through those three harmonic phases, relative to the opposite set.
- The photon’s open \(180^\circ\) pair *is* the virtual-pair topology in flight (unbound completed bounce).
- The neutrino’s closed odd braid *cannot* be that pair. It can only **stimulate** a transient pair when its triad faces the anti-triad at \(\Phi_7\).
- That stimulation is the causal role asked for here.
- Weber’s 5D shear is rewritten as triad mismatch + scrape coupling + TEP, without \(S^1_\tau\).

The \(142+857=999\) split is the arithmetic reason the two sets are opposite and complete: each triad sums to half of \(999\), and concatenation is the full repeating block of \(1/7\).

---

## 3. The two harmonic sets

The decimal cycle of \(1/7\) is the word
\[
142857\;=\;\underbrace{142}_{\mathcal{T}_\nu}\;\|\;\underbrace{857}_{\mathcal{T}_{\bar\nu}}.
\]

**Key:** \(\mathcal{T}_\nu=\{1,4,2\}\) is closed under doubling modulo the cycle order used by the digit permutation of \(1/7\) (the familiar \(1\to 2\to 4\to 1\) doubling map on the first triad). \(\mathcal{T}_{\bar\nu}=\{8,5,7\}\) is the complementary block.

Clockwork reading (letters, not megaparsecs):

- Neutrino set occupies three of the six domain-capable letters, in the order \(1\to 4\to 2\) (and cyclic).
- Anti-neutrino set occupies the complementary three letters in the order \(8\to 5\to 7\) (digit labels; internally these are three of \(\Phi_1,\ldots,\Phi_6\), *not* the reset letter \(\Phi_8\)). The digit “8” in \(142857\) is a cycle label, not the reset letter. Reset remains \(\Phi_8=e_0\) from the octonion identity. Do not conflate the two eights: one is a digit of the decimal block, the other is the identity letter. In occupancy language the anti-triad uses the three complementary *domain* letters.

Generations are the three cyclic orders of one triad:

\[
\nu_e \;\leftrightarrow\; 1\to 4\to 2,\qquad
\nu_\mu \;\leftrightarrow\; 4\to 2\to 1,\qquad
\nu_\tau \;\leftrightarrow\; 2\to 1\to 4.
\]

Anti-generations are the three cyclic orders of the complementary triad. That is the TSB replacement for a free PMNS matrix: three harmonics of one set, three of the other. Mixing is leakage from one order to another when a crossing opens at scrape.

Intra-set angle:
\[
\theta_{\mathrm{tri}}=\frac{2\pi}{3}.
\]

**Key:** two steps of a six-letter cycle, \(2\times(2\pi/6)=2\pi/3=120^\circ\). This is Weber’s \(120^\circ\) lock, now a clockwork fact.

Inter-set opposition:
\[
\theta_{\mathrm{opp}}=\pi.
\]

**Key:** three steps of a six-letter cycle, \(3\times(2\pi/6)=\pi=180^\circ\). This is Weber’s photon / annihilation-blocking angle, now the half-cycle that faces a \(\nu\)-strand at a \(\bar\nu\)-strand.

---

## 4. Braid word as passage through the three phases

Let \(B_3\) be the Artin braid group on three strands, generated by \(\sigma_1,\sigma_2\) with
\[
\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2.
\]

**Key:** \(\sigma_j\) exchanges strands \(j\) and \(j+1\) with a fixed handedness; the braid relation is the Yang–Baxter / Reidemeister-III move.

A neutrino braid word of one generation is a positive word that visits each letter of \(\mathcal{T}_\nu\) once per cycle:
\[
b_{\nu_e}(t)=\sigma_1^{n_1(t)}\sigma_2^{n_2(t)}\sigma_1^{n_3(t)},
\]
with the exponents stepped by the clockwork so that the *support* of the word at successive ticks is \(1\), then \(4\), then \(2\). That *is* the braid: not an extra ribbon in space, but the ordered passage through the three harmonic phases of the neutrino set.

The anti-neutrino word \(b_{\bar\nu}(t)\) is the complementary passage through \(\mathcal{T}_{\bar\nu}\).

Writhe of a closed 3-braid (trefoil class when the total exponent sum is odd):
\[
w_\nu=\sum_j n_j.
\]

**Key:** odd \(w_\nu\) is the fermionic / chiral leftover Weber called “odd-number braiding.” Even writhe can close into an unlink and is available to unbound photons (open 2-strand, \(180^\circ\)).

TEP (today’s \(\tau\)-free form) applied to the braid:

- No two identical bound modes occupy one \((D_a,\Phi_k)\) slot.
- The three strands of \(b_\nu\) must occupy *three distinct letters of one triad*. Same-letter double occupancy would square an imaginary unit into the reset and is forbidden.
- The opposite triad may be faced only through \(\Phi_7\) (scrape), not by parking a fourth strand on a \(\nu\)-letter.

That last clause is why a neutrino cannot *be* a virtual pair and can only *stimulate* one.

---

## 5. Virtual pair = transient inter-triad bond

A virtual pair, in this language, is a two-strand object with one foot in \(\mathcal{T}_\nu\) and one foot in \(\mathcal{T}_{\bar\nu}\), locked at \(\theta_{\mathrm{opp}}=\pi\), living for a single scrape tick.

\[
\Pi_{\mathrm{pair}}(\Delta t)
=
\bigl\lvert \psi_{\mathcal{T}_\nu}\bigr\rangle
\bigl\langle \psi_{\mathcal{T}_{\bar\nu}}\bigr\rvert
\;\otimes\;
\hat{P}_7
\;\times\;
\Theta(\tau_{\mathrm{tick}}-\Delta t).
\]

**Key:**
- \(\lvert\psi_{\mathcal{T}_\nu}\rangle\) = amplitude on the neutrino triad;
- \(\langle\psi_{\mathcal{T}_{\bar\nu}}\rvert\) = amplitude on the anti-triad;
- \(\hat{P}_7\) = projector onto the scrape letter \(\Phi_7\) (the only legal bridge);
- \(\Theta(\tau_{\mathrm{tick}}-\Delta t)\) = step function that kills the bond after one scrape opening;
- \(\Delta t\) = proper duration of the transient bond, measured on the Present slice \(\mathcal{N}\), not on a compact fifth circle.

Why transient:

1. TEP forbids a lasting four-occupancy (three \(\nu\)-strands plus a parked anti-strand) on domain letters.
2. A lasting inter-triad bond with even total writhe *is* a photon: it completes \(\mathcal{P}\leftrightarrow\mathcal{F}\) and leaves. That is unbound EM, not a virtual pair in a mass-dressing channel.
3. A *virtual* pair is the same topology *stopped* at \(\mathcal{N}\) for less than one full unbound bounce. Residual \(L\) is therefore small and brief. That is the dressing / vacuum-polarization event.

Weber’s photon (open \(e^-+e^+\) helix at \(180^\circ\)) is the completed, on-shell version of this object. Weber’s water-detector snap (braid breaks, positron meets a lab electron, two \(511\,\mathrm{keV}\) gammas) is the *real* on-shell unbraiding of the same geometry. The present question is the off-shell, sub-tick version: the pair nucleates and dissolves inside the Higgs fabric.

---

## 6. Causal role of the neutrino

Locked chain from 2026-07-21, now specialized.

A photon *is* already an open inter-triad pair. When it crosses \(\Phi_7\) it can stimulate further pairs, but it is not a *new* causal topology; it is the same topology repeating.

A neutrino *is not* that pair. It is a closed odd 3-braid confined to one triad. The only legal way it can touch the opposite triad is a scrape event at \(\Phi_7\). That event is the cause.

Sequence, one clockwork cycle of \(\nu_e\):

1. Occupancy sits on letter \(1\) of \(\mathcal{T}_\nu\). No inter-triad foot. No pair.
2. Advance \(1\to 4\). Still intra-triad. Braid generators \(\sigma_1,\sigma_2\) act inside \(\mathcal{T}_\nu\).
3. Advance \(4\to 2\). Still intra-triad.
4. At the triad-closure, the word faces the complementary triad across \(\Phi_7\). Scrape opens.
5. If \(\lvert\langle H\rangle_7\rvert^2\neq 0\) and TEP allows a *temporary* inter-triad foot, \(\Pi_{\mathrm{pair}}\) fires for one tick.
6. The pair either
   - dissolves (vacuum fluctuation; net \(L\) deposited then cancelled), or
   - is captured as dressing of a nearby bound glob (\(\Delta L_{\mathrm{virt}}\) kept), or
   -, rarely, is promoted to a real pair if a laboratory or nuclear field supplies the missing energy (inverse-beta / detector snap).
7. The neutrino braid re-closes on \(\mathcal{T}_\nu\) and continues. Flavor stays if the word is unchanged; flavor changes if a generator was rewritten during scrape (leakage into another cyclic order of the same triad, or a brief visit toward the anti-triad that re-projects as \(\bar\nu\) appearance / disappearance).

Causal claim, stated sharply:

> The neutrino is causal for transient virtual-pair bonding because only an odd one-triad braid *must* use \(\Phi_7\) as a bridge to the opposite triad. The photon already *is* that bridge. The neutrino *makes* the bridge, tick by tick, as it finishes each three-phase passage.

That is the difference between “stimulates” (both species, 2026-07-21) and “is the causal clock of the bond” (neutrino only, this session).

---

## 7. Rate and angular-momentum deposit

Production rate of transient pairs stimulated by a neutrino braid:
\[
\Gamma_{\mathrm{virt}}^{(\nu)}
=
\lambda_{\mathrm{H}\nu}
\;
\lvert\psi_\nu\rvert^2
\;
\lvert\langle H\rangle_7\rvert^2
\;
\mathcal{F}_{\mathrm{TEP}}
\;
\mathcal{B}(b_\nu,b_{\bar\nu}).
\]

**Key:**
- \(\lambda_{\mathrm{H}\nu}\): geometric scrape coupling of a 3-braid to \(\Phi_7\), fixed by the \(G_2\) action on a three-letter subset (no continuous free parameter);
- \(\lvert\psi_\nu\rvert^2\): local neutrino probability density;
- \(\lvert\langle H\rangle_7\rvert^2\): local Higgs / scrape intensity;
- \(\mathcal{F}_{\mathrm{TEP}}\): \(1\) if the would-be pair does not park a local reset occupancy, else \(0\);
- \(\mathcal{B}(b_\nu,b_{\bar\nu})\): braiding kernel, defined next.

Braiding kernel (passage through three phases relative to the opposite set):
\[
\mathcal{B}(b_\nu,b_{\bar\nu})
=
\Bigl\lvert
\sum_{k=1}^{3}
e^{i\theta_{\mathrm{tri}}k}
\,
\langle \Phi_{\bar\nu,k}\lvert \hat{P}_7 \rvert \Phi_{\nu,k}\rangle
\Bigr\rvert^2.
\]

**Key:**
- \(k=1,2,3\) runs over the three harmonic steps of the neutrino word;
- \(\Phi_{\nu,k}\) = the letter of \(\mathcal{T}_\nu\) at step \(k\) (for \(\nu_e\): \(1,4,2\));
- \(\Phi_{\bar\nu,k}\) = the facing letter of \(\mathcal{T}_{\bar\nu}\) at that same step (for the complementary order: \(8,5,7\) as cycle digits);
- \(\hat{P}_7\) inserts the only legal bridge;
- the phase \(e^{i\theta_{\mathrm{tri}}k}\) is the \(120^\circ\) lock. Constructive interference of the three terms is a completed triad passage — maximum pair-stimulation. A single-step scrape (one term only) is a weaker, flavor-mixing leak.

Angular momentum of one transient pair:
\[
\Delta L_{\mathrm{virt}}
=
\gamma_{\mathrm{virt}}
\;
\ell_0
\;
\mathcal{C}_{\mathrm{constr}}
\;
\mathcal{F}_{\mathrm{TEP}}
\;
\sin\theta_{\mathrm{opp}}.
\]

**Key:**
- \(\gamma_{\mathrm{virt}}\): Lorentz / clockwork boost of the virtual pair in the Present frame;
- \(\ell_0\): elementary Mirron-inversion quantum;
- \(\mathcal{C}_{\mathrm{constr}}=\lvert m\rvert/\lvert V\rvert\): constraint of the bound glob that captures the deposit;
- \(\sin\theta_{\mathrm{opp}}=\sin\pi=0\) would kill a *completed* opposite pair that has already become a photon (\(L=0\) unbound). For a *virtual* pair the opposition is incomplete: the bond is stopped at \(\mathcal{N}\) before the angle finishes, so replace \(\sin\theta_{\mathrm{opp}}\) by the incomplete factor \(\sin(\pi\cdot\Delta t/\tau_{\mathrm{tick}})\). Then
\[
\Delta L_{\mathrm{virt}}
=
\gamma_{\mathrm{virt}}
\;
\ell_0
\;
\mathcal{C}_{\mathrm{constr}}
\;
\mathcal{F}_{\mathrm{TEP}}
\;
\sin\bigl(\pi\,\Delta t/\tau_{\mathrm{tick}}\bigr).
\]

**Key of the sine:** at \(\Delta t=0\) the pair has not formed (\(L=0\)); at \(\Delta t=\tau_{\mathrm{tick}}\) the pair has completed the half-cycle and left as unbound light (\(L=0\) again); the maximum residual \(L\) is at half a scrape tick. Transient bonding is therefore a mid-tick phenomenon. That is why it is a dressing / curvature source rather than a real photon.

This recovers the 2026-07-21 statement that neutrino-stimulated virtual particles supply the angular momentum that curves spacetime, now with an explicit mid-tick window and an explicit triad geometry.

---

## 8. Integrity parameter without a KK circle

Weber’s \(D=\Delta_{\mathrm{Tav}}/(\xi E_\nu)\) used a 5D shear and an Earth-diameter path. TSB can keep an integrity ratio without that path by comparing dressing energy to neutrino energy, times the braiding kernel:

\[
D_\nu
=
\frac{\Delta_{\mathrm{Tav}}}{E_\nu}
\;
\frac{\mathcal{B}(b_\nu,b_{\bar\nu})}{\mathcal{B}_0}.
\]

**Key:**
- \(\Delta_{\mathrm{Tav}}\approx 313.1\,\mathrm{MeV}\): local scrape-to-reset dressing quantum;
- \(E_\nu\): neutrino energy;
- \(\mathcal{B}_0\): kernel of a fully aligned, un-sheared triad passage (the three terms in phase);
- \(D_\nu>1\): scrape coupling dominates; crossings open; flavor leakage and pair-stimulation both rise;
- \(D_\nu\le 1\): the 3-braid is stiff; \(\mathcal{B}\) stays near \(\mathcal{B}_0\); flavor holds; pair-stimulation is rarer per tick but each captured pair can carry more organized \(L\).

The IceCube \(\sim 30\,\mathrm{TeV}\) knee, if used at all, is only an IR calibration of when \(D_\nu\) crosses unity for terrestrial column depth. It is *not* a derivation of \(\tau\) and not a fifth-dimensional radius. Optional. The causal mechanism above does not depend on it.

A winding correction, if wanted:
\[
D_\nu(w)
=
\frac{\Delta_{\mathrm{Tav}}}{E_\nu}
\;
\frac{\mathcal{B}}{\mathcal{B}_0}
\;
\bigl(1+\kappa_w\lvert w_\nu-w_0\rvert\bigr).
\]

**Key:** \(w_0\) odd integer that closes \(\mathcal{T}_\nu\) without local \(\Phi_8\); \(\kappa_w\) is an order-one \(G_2\) factor, not a fit to PMNS angles.

---

## 9. Why three phases, and why two sets

| Question | TSB answer |
|----------|------------|
| Why three strands? | A triad is the largest odd subset of a six-cycle that cannot contain its own opposite. Odd writhe \(\Rightarrow\) fermionic leftover. |
| Why two sets? | The \(142857\) word splits as \(142\|857\). One set cannot annihilate internally; annihilation (or virtual-pair nucleation) requires the complementary set. |
| Why \(120^\circ\)? | Two steps of six letters. Intra-set braid lock. |
| Why \(180^\circ\)? | Three steps of six letters. Inter-set opposition. Photon / pair angle. |
| Why neutrinos rather than photons as the *clock*? | Photons already occupy the inter-set angle. Neutrinos occupy only one set and must *open* the angle at \(\Phi_7\). |
| Why transient? | TEP plus the mid-tick sine: a finished half-cycle leaves as light; a lasting four-occupancy is forbidden; only the incomplete scrape bond remains off-shell. |
| Why Phase 7? | Only legal bridge between triads. Shared Mirron / Higgs fabric. Not a seventh spacetime. |
| Why not \(\tau\) / KK? | The relative geometry is the six-letter cycle and the scrape projector. No compact fifth length is required for the causal claim. |

---

## 10. Worked limits

**Solar / reactor (\(E_\nu\sim\mathrm{MeV}\), \(D_\nu\gg 1\)).**  
Triad passage is soft. \(\mathcal{B}\) has open crossings. Many scrape ticks fire \(\Pi_{\mathrm{pair}}\). Most pairs dissolve; a fraction dress nearby bound globs (solar plasma, reactor core). Flavor leakage is large (solar deficit / reactor oscillation as unbraiding into another cyclic order). This is Weber’s “topological shredding,” rewritten as high pair-stimulation plus word rewriting, not as a KK drag.

**Beam (\(E_\nu\sim\mathrm{GeV}\)).**  
Partial stiffening. \(\mathcal{B}\) still leaks. Oscillation lengths emerge as the number of triad passages needed to rewrite one generator \(\sigma_j\). Virtual-pair stimulation continues but with a narrower mid-tick window.

**IceCube-scale (\(E_\nu\sim 10\,\mathrm{TeV}\) and above).**  
Stiff braid. \(\mathcal{B}\approx\mathcal{B}_0\). Flavor holds. Pair-stimulation per tick drops, but each captured pair is cleaner (sine closer to a definite mid-tick value). Residual \(L_\nu\) of the neutrino itself remains small; the neutrino is still not a Higgs rest-mass fermion in the SM sense.

**Detector snap (Weber water paper, on-shell).**  
If a laboratory electron supplies a real foot in \(\mathcal{T}_{\bar\nu}\), the transient bond can be promoted: one \(\nu\)-strand peels as a charged lepton track, the facing anti-strand annihilates, two \(511\,\mathrm{keV}\) photons leave as completed unbound pairs. That is the real-pair limit of the same \(\Pi_{\mathrm{pair}}\). It does not contradict the virtual mid-tick story; it is the same projector with \(\Delta t\) allowed to reach \(\tau_{\mathrm{tick}}\) because an external real foot is present.

---

## 11. Relation to TEP (this morning’s \(\tau\)-free form)

- The three strands of \(b_\nu\) occupy three distinct letters. Same-letter occupancy would be \(e_i^2=-1\to\Phi_8\) and is forbidden.
- The virtual pair’s anti-foot may exist only under \(\hat{P}_7\), never as a fourth domain-letter occupancy.
- A completed photon is an unbound cycle-closer: its \(\Phi_8\) content is the global \(\mathcal{P}\leftrightarrow\mathcal{F}\) identification, not a local slot. Allowed to pile.
- A neutrino is bound-ish (small \(L_\nu\)) and odd. It cannot pile in one slot and cannot park on the reset. It can only scrape.

Exclusion is therefore what *forces* the causal detour through \(\Phi_7\). Without TEP the 3-braid could simply sit on the anti-triad and become a real pair at will. With TEP the only legal contact is a transient scrape bond. That is the precise sense in which exclusion plus braiding makes the neutrino a cause of virtual-pair nucleation rather than a constituent of the pair.

---

## 12. What this does *not* claim

- It does not derive PMNS angles numerically in this session. It identifies their discrete origin (three cyclic orders per triad, leakage at scrape).
- It does not derive \(\tau\) or a fifth radius from IceCube.
- It does not replace the 2026-07-21 photon channel. Photons still stimulate pairs. Neutrinos are the additional *causal clock* because of the odd triad.
- It does not treat \(\Delta_{\mathrm{Tav}}\) as a glueball pole.
- It does not assert a laboratory discovery. The mechanism is a TSB conversion of an outside geometric braid paper plus the locked Higgs-stimulation chain.

---

## 13. Falsifiers

1. A neutrino species that stimulates virtual-pair / vacuum-polarization signatures *without* any scrape-scale energy deposit near \(\Delta_{\mathrm{Tav}}\) and *without* a three-step harmonic pattern would break the triad identification.
2. Flavor change that tracks a continuous \(1/E\) law with no 3-step or 6-step plateaus at high resolution would weaken the harmonic-phase claim (not kill the causal-stimulation claim by itself).
3. A bound charged lepton produced from a neutrino with no facing anti-triad foot available (no target electron, no scrape opening) would break the promotion picture.
4. If photons and neutrinos produced indistinguishable mid-tick \(\Delta L_{\mathrm{virt}}\) spectra, the “neutrino as clock, photon as completed pair” split would fail.

---

## 14. Compact statement

Weber’s triple helix, converted: a neutrino is an odd 3-braid whose support walks the harmonic triad \(\{1,4,2\}\) (or a cyclic order of it); an anti-neutrino walks \(\{8,5,7\}\). Braiding *is* that walk. A virtual pair is a mid-tick, scrape-mediated foot from one triad onto the other, opposed at half-cycle, killed by TEP if it tries to stay. The neutrino is causal because only the odd one-set braid is *obliged* to open that foot at \(\Phi_7\). The angular momentum of the incomplete pair is the locked dressing / curvature deposit. No megaparsec circle and no KK fifth dimension enter the causal chain.

---

**File created**: 2026-09-20  
**Location**: `Personal_Files/Session_2026-09-20_Neutrino_Causal_Virtual_Pair_Braiding_Three_Harmonic_Phases.md`

*Converts Weber 2026 (Zenodo 20721653 / 20732605) into TSB occupancy language and answers the causal-stimulation question with the \(142\|857\) split and the mid-tick scrape bond.*
