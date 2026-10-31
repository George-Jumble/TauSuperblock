# Session 2026-09-29 — Derivation of the domain-cross energy

**Framework**: Unified Tav–Superblock (TSB), live frame after 2026-09-20 / 2026-09-21 (no Tau circle, no KK fifth dimension as premises).  
**Convention**: Mirron, never soliton.  
**Charge**: Derive the domain-cross energy — the work required to drag space (the alien quantum fields) through the phase-wall of the colocated domains.  
**Follows**: `Session_2026-09-29_Domain_Cross_Phase_Wall_Protocol_Audit.md` (protocol had not been performed).

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-09-29_Domain_Cross_Energy_Derivation.md`  
Mirrors: `Personal Files/`, `Personal_Files/`.

---

## 0. Result in one block

The elementary domain-cross energy is the Compton-force work of one bound alien line along the internal arc that joins two domain frames:

\[
E_{\times}(a\to b)
=
\theta_{ab}\,\Delta_{\mathrm{Tav}}.
\]

**Key.** \(E_{\times}(a\to b)\): transit work to drag one bound alien line from domain \(D_a\) to domain \(D_b\). \(\theta_{ab}\): geodesic angle between the two domain frames on the internal occupancy sphere. \(\Delta_{\mathrm{Tav}}\): inserted IR dressing scale of one bound colour line (nucleon-third protocol).

On the locked six-vertex (octahedron) placement of the domains,

\[
\theta_{ab}=\frac{\pi}{2}
\quad\text{adjacent / distinct axis},
\qquad
\theta_{a\bar{a}}=\pi
\quad\text{antipodal / conjugate domain}.
\]

Printed floor \(\Delta_{\mathrm{Tav}}=313.1\,\mathrm{MeV}\):

\[
E_{\times}^{\mathrm{adj}}
=
\frac{\pi}{2}\times 313.1\,\mathrm{MeV}
=
491.816\,\mathrm{MeV},
\]

\[
E_{\times}^{\mathrm{ant}}
=
\pi\times 313.1\,\mathrm{MeV}
=
983.633\,\mathrm{MeV}.
\]

Unbound completed \(\mathcal{P}\leftrightarrow\mathcal{F}\) light does not drag space: \(E_{\times}^{\mathrm{(unbound)}}=0\).  
An occupied target slot adds the TEP insertion, not a replacement of the work:

\[
E_{\times}^{\mathrm{(blocked)}}
\ge
E_{\times}(a\to b)+\Delta_{\mathrm{Tav}}.
\]

What is derived: the *form* \(E_{\times}=\theta\Delta\), the two locked angles, the vanishing for unbound light, the TEP addendum.  
What is inserted: the MeV unit \(\Delta_{\mathrm{Tav}}\). TEP supplies \(\Delta>0\); it does not compute \(313.1\).

This is not a meson mass prediction. Do not shop \(491.8\,\mathrm{MeV}\) or \(983.6\,\mathrm{MeV}\) for a pole.

---

## 1. Complete key (every symbol used below)

| Symbol | Meaning |
|---|---|
| \(D_a\), \(a=1,\ldots,6\) | Co-located \(3+1\)D domains on the internal occupancy three-sphere |
| \(\mathbb{S}_{\mathrm{SB}}\cong S^3_{\mathrm{int}}\) | Internal arena. Domains share external \(3+1\) events and differ by an internal frame rotation |
| \(\Phi_k\), \(k=1,\ldots,8\) | Clockwork letters. \(\Phi_{1\ldots6}\) active residues of \((\mathbb{Z}/7\mathbb{Z})^\times\); \(\Phi_7\) scrape / PK-Mirron; \(\Phi_8\) reset |
| \(e_0=1\) | Octonion identity. Identified with \(\Phi_8\) |
| \(e_i\), \(i=1,\ldots,7\) | Imaginary octonion units. \(e_i^2=-1\) |
| \(e_7\) | Unit reserved as scrape. Not a seventh spacetime |
| \(\hat{e}_a\) | Unit internal vector of domain frame \(D_a\) |
| \(W_{ab}\) | Phase-wall: shared scrape channel through which occupancy of \(D_a\) meets occupancy of \(D_b\). Internal. Not a 4D Einstein domain wall. Not the reset seam \(\Phi_8\) |
| \(\Sigma\) | Mirron world-tube (containment 2-surface). Distinct from \(W_{ab}\) and from \(\Phi_8\) |
| \(\psi^{(b)}\) | Alien field on \(D_a\): a quantum whose slot is \((D_b,\Phi_k)\), read from inside \(D_a\). “Space of the sister” at elementary level is one such bound line |
| \(\psi^{(a)}\) | Local field on \(D_a\) |
| space (elementary) | One bound alien line together with the residual-\(L\) compression it sources |
| space (extensive) | Coherent sum of those lines in a region |
| \(T_{\mathrm{alien}\to\mathrm{local}}\) | Containment map: alien colour \(\to\) local EM, alien EM \(\to\) local colour |
| \(P_{\mathrm{(transit)}}\) | Projection from alien frame into local frame |
| \(M\) | Phase-invariant kinetic matrix of a domain transition |
| \(B_M\) | Mirron boundary operator |
| drag | Forced *bound* transport of \(\psi^{(b)}\) across \(W_{ab}\) |
| \(\times_{ab}\) | Domain cross: bound slot \((D_a,\Phi_k)\to(D_b,\Phi_{k'})\) without a completed unbound bounce |
| \(E_{\times}(a\to b)\) | Transit *work* of that drag |
| \(\theta_{ab}\) | Internal angle between \(\hat{e}_a\) and \(\hat{e}_b\) |
| \(D_{\bar{a}}\) | Antipodal / conjugate domain to \(D_a\) (matter \(\leftrightarrow\) antimatter pairing on one octahedron axis) |
| \(F_{\mathrm{C}}\) | Compton force of one dressed line, \(\Delta_{\mathrm{Tav}}/\lambda_{m_0}\) |
| \(\lambda_{m_0}=\hbar c/\Delta_{\mathrm{Tav}}\) | Compton length of the floor. \(0.63024\,\mathrm{fm}\) at printed \(313.1\,\mathrm{MeV}\) |
| \(\Delta_{\mathrm{Tav}}\) | Inserted TEP / dressing scale. Printed \(313.1\,\mathrm{MeV}\). Exact nucleon-third \(M_n/3=313.188\,\mathrm{MeV}\) |
| \(M_n\) | Neutron mass \(939.56542194\,\mathrm{MeV}\) |
| \(E_{\mathrm{violation}}\) | Extra cost of a forced local \(\Phi_8\) insertion. \(E_{\mathrm{violation}}\ge\Delta_{\mathrm{Tav}}\) |
| \(n_{a,k}\) | Occupation of slot \((D_a,\Phi_k)\). Bound modes: \(n_{a,k}\le 1\) |
| \(\hat{P}_{142857}\) | Projector onto \((\mathbb{Z}/7\mathbb{Z})^\times\) cycle labels |
| \(\hat{P}_8^{\mathrm{local}}\) | Projector onto local reset occupancy |
| \([x,y,z]\) | Octonion associator \((xy)z-x(yz)\) |
| \(S_E\) | Euclidean action of one allowed diameter tick. Locked \(S_E/\hbar=2\) |
| \(\Delta t_{\mathrm{tick}}=2\lambda_{m_0}/c\) | Duration of that tick |
| \(L\) | Residual angular momentum of a rebound stopped at the Present |
| bound bounce | Reaches Absolute Past; rebound toward Future stopped at Present. \(L\neq 0\) |
| unbound bounce | Completes \(\mathcal{P}\leftrightarrow\mathcal{F}\). \(L=0\). Light-like |
| \(\alpha=1-\log_7 6\) | Fractal deficit of the 6-of-7 graph. \(\approx 0.079218\). Not used as an extra MeV factor |
| \(\ell_P=R_{\mathrm{int}}\) | Planck / F7 radius slot. Mirron *core*. Not the IR path length of dressed space |
| \(\mathcal{F}_{\mathrm{TEP}}\) | \(1\) on an empty 142857-closed target; suppression / veto on a blocked slot |
| \(N_{\mathrm{lines}}\) | Number of bound alien lines dragged together |
| \(E_{\times}^{\mathrm{space}}\) | Extensive drag work \(N_{\mathrm{lines}}E_{\times}\) |

**Not used as premises:** \(\tau\), \(R_\tau\), \(S^1_\tau\), \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_{313})\), \(R_5\), \(G_5\), \(\rho_\Lambda=\hbar c/\tau^4\).

---

## 2. What is being derived

Three surfaces are distinct.

| Surface | What it is | What it is not |
|---|---|---|
| \(\Sigma\) | Mirron world-tube. Containment 2-surface that sources \(\mathbf{n}_{\mathrm{cont}}\) | Not the sister-domain wall |
| \(\Phi_8\) | Reset / identity / \(\mathcal{P}\leftrightarrow\mathcal{F}\) seam. \(e_i^2=-1=-e_0\) | Not a domain. Not \(W_{ab}\) |
| \(W_{ab}\) | Shared scrape \(\Phi_7\) as the internal interface of \(D_a\) with \(D_b\) | Not a 4D metric domain wall |

Co-location means the six domains share external events. The wall is therefore *internal*. Dragging space through it is an internal transport of bound alien fields, not a 4D bubble nucleation.

The elementary quantum of “space” in this protocol is one bound alien line: a stopped colour (or contained alien-EM) bounce that already carries residual \(L\) and already has IR inertia. Extensive space is a coherent set of such lines. The protocol is solved first per line, then extended.

---

## 3. Allowed transit versus forbidden insertion

A bound line may connect

\[
(D_a,\Phi_k)\;\longrightarrow\;(D_b,\Phi_{k'})
\]

only when the product of cycle residues remains a unit modulo \(7\) (2026-09-20 occupancy rule) and the target slot is empty:

\[
n_{b,k'}=0,
\qquad
\hat{P}_8^{\mathrm{local}}\Psi=0,
\qquad
\hat{P}_{142857}\Psi=\Psi.
\]

**Key.** \(\Psi\) is the occupancy state of the line plus the target slot.

The only shared holding channel that is not a domain slot is scrape:

\[
(D_a,\Phi_k)
\;\longrightarrow\;
\Phi_7
\;\longrightarrow\;
(D_b,\Phi_{k'}).
\]

That two-step path *is* the phase-wall crossing. Sharing \(\Phi_7\) is not double occupancy of a domain slot.

If the target is already occupied, the only algebraic sink for the second copy is local reset:

\[
e_k(e_k v)=-e_0 v
\qquad\text{or a \(G_2\)-image}.
\]

That is TEP violation. It is an *addendum* to the drag work, not a substitute for it.

Unbound light never occupies a local slot. It is the global \(\mathcal{P}\leftrightarrow\mathcal{F}\) identification. It does not drag bound space. \(E_{\times}^{\mathrm{(unbound)}}=0\).

---

## 4. Containment map at the wall

The locked transit operator (2026-07-21) is

\[
T_{\mathrm{alien}\to\mathrm{local}}
=
P_{\mathrm{(transit)}}
\cdot
M
\cdot
e^{i\Delta\phi}
\cdot
B_M.
\]

**Key.** On \(W_{ab}\), \(P_{\mathrm{(transit)}}\) changes the domain label \(a\to b\). \(B_M\) inverts the alien representation (colour\(\leftrightarrow\)EM) at the Mirron boundary. \(e^{i\Delta\phi}\) is the directed phase of that inversion. \(M\) is the kinetic matrix; it does not introduce a new continuous coupling.

Dragging space is applying \(T_{\mathrm{alien}\to\mathrm{local}}\) along an internal path from \(\hat{e}_a\) to \(\hat{e}_b\) while the line remains bound (\(L\neq 0\)).

---

## 5. Why the IR path length is \(\lambda_{m_0}\), not \(\ell_P\)

Two lengths remain after the 2026-09-21 recalc.

\[
\lambda_{m_0}
=
\frac{\hbar c}{\Delta_{\mathrm{Tav}}}
=
0.63024\,\mathrm{fm}
\quad\text{at printed }313.1\,\mathrm{MeV}.
\]

\[
R_{\mathrm{int}}=\ell_P=1.616\times 10^{-35}\,\mathrm{m}.
\]

**Key.** \(\ell_P\) is the Mirron *core* / F7 radius slot (named, not derived). \(\lambda_{m_0}\) is the Compton length of the dressed line — the size of the 6-phase cloud that *is* the elementary quantum of space being dragged.

Work computed along \(\ell_P\) would be a Planck energy. That is the core, not the cloud. An IR bound line cannot be localised to \(\ell_P\) without paying a UV cost that the protocol does not ask for. The path that drags *space* is the cloud path, length \(\theta_{ab}\lambda_{m_0}\).

Do not glue the two lengths with \(\log_7(\lambda_{m_0}/\ell_P)\). That logarithm is not a TEP premise.

---

## 6. Compton force and the work integral

The only IR force unit a single dressed line possesses is its Compton force

\[
F_{\mathrm{C}}
=
\frac{\Delta_{\mathrm{Tav}}}{\lambda_{m_0}}
=
\frac{(\Delta_{\mathrm{Tav}})^2}{\hbar c}.
\]

**Key.** \(F_{\mathrm{C}}\) has dimensions of force. It is the force whose work across one Compton length equals the line’s own inertia.

The internal path from frame \(a\) to frame \(b\) is the arc

\[
\mathrm{d}s=\lambda_{m_0}\,\mathrm{d}\theta,
\qquad
\int_{a}^{b}\mathrm{d}s=\theta_{ab}\,\lambda_{m_0}.
\]

**Key.** \(\theta\) is the angle between domain frames on the occupancy sphere whose physical radius, for a dressed line, is \(\lambda_{m_0}\).

Transit work:

\[
E_{\times}(a\to b)
=
\int_{W_{ab}} F_{\mathrm{C}}\,\mathrm{d}s
=
F_{\mathrm{C}}\cdot\theta_{ab}\lambda_{m_0}
=
\theta_{ab}\,\Delta_{\mathrm{Tav}}.
\]

**Key.** The Compton length cancels. The energy is the floor times a pure angle. No new continuous parameter enters.

This is the derivation. Everything after this section only evaluates \(\theta_{ab}\) and states addenda.

---

## 7. The two locked angles

### 7.1 Six domains as the octahedron on \(S^2\subset S^3_{\mathrm{int}}\)

Locked placement (2026-09-18 cell, kept as geometry of labels, not as an \(\alpha_{\mathrm{fs}}\) claim): six vertices of a regular octahedron. Three axes, two orientations per axis.

\[
\{D_1,\ldots,D_6\}
=
\{\pm\hat{x},\pm\hat{y},\pm\hat{z}\}
\quad\text{on a great }S^2\subset S^3_{\mathrm{int}}.
\]

Adjacent vertices (distinct axes) meet at

\[
\theta_{\mathrm{adj}}=\frac{\pi}{2}.
\]

Antipodal vertices (conjugate / matter–antimatter pair on one axis) meet at

\[
\theta_{\mathrm{ant}}=\pi.
\]

### 7.2 Fano / scrape check (why antipodes are the associative scrape hops)

Reserve \(e_7\) as scrape. The Fano plane has three lines through \(e_7\). Each such line is an associative triple

\[
\{e_7,\,e_a,\,e_{\bar{a}}\}.
\]

Those three lines *are* the three octahedron axes. Therefore:

- antipodal hop \(D_a\to D_{\bar{a}}\) is scrape-associative, \([e_a,e_7,e_{\bar{a}}]=0\);
- adjacent hop \(D_a\to D_b\) (\(b\neq\bar{a}\)) is scrape-nonassociative, \(|[e_a,e_7,e_b]|=2\) on unit imaginaries.

The associator is dimensionless. It does **not** mint a second MeV unit. It classifies the hop. It is not multiplied into \(E_{\times}\) unless one *chooses* a conversion convention (see §10). The primary energy is the work integral, which already used only \(F_{\mathrm{C}}\) and \(\theta\).

### 7.3 Evaluated energies

Printed insertion \(\Delta_{\mathrm{Tav}}=313.1\,\mathrm{MeV}\):

\[
E_{\times}^{\mathrm{adj}}
=
\frac{\pi}{2}\Delta_{\mathrm{Tav}}
=
491.816\,\mathrm{MeV},
\]

\[
E_{\times}^{\mathrm{ant}}
=
\pi\Delta_{\mathrm{Tav}}
=
983.633\,\mathrm{MeV}.
\]

Nucleon-third without rounding, \(M_n/3=313.188474\,\mathrm{MeV}\):

\[
E_{\times}^{\mathrm{adj}}
=
491.955\,\mathrm{MeV},
\qquad
E_{\times}^{\mathrm{ant}}
=
983.911\,\mathrm{MeV}.
\]

Relative shift from dropping the print-rounding: \(+2.8\times 10^{-4}\), the same shift already locked for all \(m_0\)-linear quantities (2026-09-26). Keep printed \(313.1\) in existing formulae; quote the unrounded pair when the floor is written as \(M_n/3\).

---

## 8. Consistency with the locked diameter-tick action

Allowed refresh of one bound line:

\[
\frac{S_E}{\hbar}=2,
\qquad
\Delta t_{\mathrm{tick}}=\frac{2\lambda_{m_0}}{c}.
\]

The energy that realises that action over that time is

\[
E_{\mathrm{tick}}
=
\frac{S_E}{\Delta t_{\mathrm{tick}}}
=
\frac{2\hbar}{2\lambda_{m_0}/c}
=
\frac{\hbar c}{\lambda_{m_0}}
=
\Delta_{\mathrm{Tav}}.
\]

**Key.** One allowed diameter tick of one bound line has energy-equivalent \(\Delta_{\mathrm{Tav}}\). That is why the Compton force built from \(\Delta_{\mathrm{Tav}}/\lambda_{m_0}\) is the same object as the tick energy over a Compton length. No second scale is introduced.

A domain cross is *not* a diameter tick. A diameter tick advances the 8-phase clock and returns the domain label. A domain cross changes the domain label and pays work \(\theta\Delta_{\mathrm{Tav}}\).

The Euclidean action *of the transit*, using the line’s standing inertia \(\Delta_{\mathrm{Tav}}\) over the dwell \(t=\theta_{ab}\lambda_{m_0}/c\), is

\[
\frac{S_{\times}}{\hbar}
=
\frac{\Delta_{\mathrm{Tav}}\cdot(\theta_{ab}\lambda_{m_0}/c)}{\hbar}
=
\theta_{ab}.
\]

**Key.** Do not multiply \(E_{\times}=\theta\Delta\) by the same dwell again. That would double-count \(\theta\). \(E_{\times}\) is the work. \(S_{\times}/\hbar=\theta\) is the action of standing inertia along the same arc.

Isochronous Minkowski process: phase \(e^{i\theta_{ab}}\).  
Euclidean / blocked estimate: suppression \(e^{-\theta_{ab}}\),

\[
e^{-\pi/2}\approx 0.2079,
\qquad
e^{-\pi}\approx 0.04321.
\]

Those numbers are *not* a neutron-lifetime claim. \(\Delta P_{\mathrm{leak}}\approx 10^{-3}\) remains a separate phenomenological sketch.

---

## 9. TEP addendum (blocked target)

If \(n_{b,k'}\ge 1\), the hop cannot land. The algebraic sink is local \(\Phi_8\). The live cost inequality (2026-09-26) is

\[
E_{\mathrm{violation}}\ge\Delta_{\mathrm{Tav}}.
\]

Total blocked-cross energy:

\[
E_{\times}^{\mathrm{(blocked)}}(a\to b)
\ge
\theta_{ab}\,\Delta_{\mathrm{Tav}}
+
\Delta_{\mathrm{Tav}}
=
\bigl(\theta_{ab}+1\bigr)\Delta_{\mathrm{Tav}}.
\]

**Key.** Adjacent blocked: \(\ge(1+\pi/2)\Delta_{\mathrm{Tav}}=804.916\,\mathrm{MeV}\) at printed floor. Antipodal blocked: \(\ge(1+\pi)\Delta_{\mathrm{Tav}}=1296.733\,\mathrm{MeV}\). These are lower bounds on a forbidden process, not poles.

Unbound light still pays nothing: it never tries to land in a local slot.

---

## 10. What is *not* being claimed

- Not \(E_{\times}=\Delta_{\mathrm{Tav}}\) by fiat. That was the 29 September audit’s conjectural identification. The work integral replaces it with \(\theta\Delta_{\mathrm{Tav}}\).
- Not a derivation of \(313.1\,\mathrm{MeV}\). The digits remain the nucleon-third insertion.
- Not a \(0^{++}\) glueball, not a current-up mass, not a Vălean residue.
- Not a meson-mass prediction at \(492\,\mathrm{MeV}\) or \(984\,\mathrm{MeV}\).
- Not an associator-to-MeV theorem. Standard octonions give \(|[e_i,e_j,e_k]|=2\) on a nonassociative unit triple. Converting that \(2\) into \(\Delta_{\mathrm{Tav}}\) is a convention, not a lock. If imposed, the adjacent hop would pick up an extra \(\Delta_{\mathrm{Tav}}\) and become \(E_{\times}^{\mathrm{adj,assoc-conv}}=(1+\pi/2)\Delta_{\mathrm{Tav}}\). That convention is hereby *not* locked; it is the same number as the *blocked* adjacent bound, for a different reason, and fusing them would be a bookkeeping accident.
- Not a use of \(\alpha=1-\log_7 6\) as a mass factor. \(\alpha\) remains the scale-free deficit of the 6-of-7 graph.
- Not a 4D GR domain-wall tension. \(W_{ab}\) is internal.
- Not a KK mode mass \(n\hbar c/R_5\).

---

## 11. Extensive space

If a coherent region drags \(N_{\mathrm{lines}}\) bound alien lines together,

\[
E_{\times}^{\mathrm{space}}(a\to b)
=
N_{\mathrm{lines}}\,\theta_{ab}\,\Delta_{\mathrm{Tav}}.
\]

**Key.** \(N_{\mathrm{lines}}=1\) is the elementary protocol. A three-line valence packet with associator locking \(3/4\) (corpus value for a stable fermion) still pays per line that actually crosses. Do not automatically set \(N_{\mathrm{lines}}=3\) and call the result a baryon mass.

Vacuum packing \(n_{\mathrm{M}}^{(0)}=\rho_{\mathrm{vac}}/\Delta_{\mathrm{Tav}}\) is chamber bookkeeping from 2026-09-21. It does not promote this section into a derivation of \(\Lambda\).

---

## 12. Summary table

| Process | \(\theta\) | \(E_{\times}\) at \(313.1\,\mathrm{MeV}\) | \(S_{\times}/\hbar\) | TEP extra |
|---|---|---|---|---|
| Unbound light | — | \(0\) | \(0\) | none |
| Adjacent allowed hop | \(\pi/2\) | \(491.816\,\mathrm{MeV}\) | \(\pi/2\) | \(0\) if target empty |
| Antipodal allowed hop | \(\pi\) | \(983.633\,\mathrm{MeV}\) | \(\pi\) | \(0\) if target empty |
| Adjacent, target blocked | \(\pi/2\) | \(\ge 804.916\,\mathrm{MeV}\) | \(\ge 1+\pi/2\) | \(\ge\Delta_{\mathrm{Tav}}\) |
| Antipodal, target blocked | \(\pi\) | \(\ge 1296.733\,\mathrm{MeV}\) | \(\ge 1+\pi\) | \(\ge\Delta_{\mathrm{Tav}}\) |

Primary lock:

\[
\boxed{
E_{\times}(a\to b)=\theta_{ab}\,\Delta_{\mathrm{Tav}}
}
\]

with \(\theta_{\mathrm{adj}}=\pi/2\), \(\theta_{\mathrm{ant}}=\pi\), \(\Delta_{\mathrm{Tav}}\) inserted, unbound \(E_{\times}=0\).

---

## 13. Query / computation log

| Item | Value |
|---|---|
| \(M_n\) | \(939.56542194\,\mathrm{MeV}\) |
| \(M_n/3\) | \(313.188474\,\mathrm{MeV}\) |
| Printed floor | \(313.1\,\mathrm{MeV}\) |
| \(\hbar c\) | \(197.3269804\,\mathrm{MeV\,fm}\) |
| \(\lambda_{m_0}(313.1)\) | \(0.630236\,\mathrm{fm}\) |
| \((\pi/2)\times 313.1\) | \(491.816330\,\mathrm{MeV}\) |
| \(\pi\times 313.1\) | \(983.632660\,\mathrm{MeV}\) |
| \((1+\pi/2)\times 313.1\) | \(804.916330\,\mathrm{MeV}\) |
| \(e^{-\pi/2}\) | \(0.207880\) |
| \(e^{-\pi}\) | \(0.043214\) |
| \(\alpha=1-\log_7 6\) | \(0.079218\) (not used as a mass factor) |

---

*Derived 2026-09-29. Floor digits remain an insertion.*
