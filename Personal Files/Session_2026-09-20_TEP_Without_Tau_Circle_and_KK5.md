# Session 2026-09-20 — Topological Exclusion Principle without the Tau 7.5 Mpc Circle and without a KK Fifth Dimension

**Framework**: Unified Tav–Superblock (TSB) Cosmology  
**Date**: 2026-09-20  
**Task**: Derive the Topological Exclusion Principle (TEP) from locked algebraic and bounce structure only.  
**Explicitly excluded as load-bearing objects**:
- the survey / Gatlin cell \(S^1_\tau\) of radius \(\tau \approx 7\,h^{-1}\mathrm{Mpc}\) (or \(7.5\,\mathrm{Mpc}\));
- any compact or dynamical Kaluza–Klein fifth coordinate \(\theta\), \(R_5(t)\), \(S^1_\infty\), or \(\rho_\Lambda = \hbar c/\tau^4\);
- the stretch formula \(n_{\rm hier}=\log_7(\tau/\lambda_{313.1})\) (that formula *uses* \(\tau\); it cannot justify TEP if \(\tau\) is demoted).

**Allowed primitives (already locked in the corpus)**:
- octonions \(\mathbb{O}\) and \(\mathrm{Aut}(\mathbb{O})\cong G_2\);
- eight clockwork letters \(\Phi_1,\ldots,\Phi_8\) with \(6+1+1\) assignment (six domains, scrape, reset);
- order-6 cycle \((\mathbb{Z}/7\mathbb{Z})^\times\) and digit block \(142857\);
- six co-located \(3+1\)D domains on the internal supersphere \(\mathbb{S}_{\mathrm{SB}}\cong S^3\);
- PK-Mirron as \(\Phi_7\) scrape / Planck–Kerr mirror (not a seventh spacetime);
- bound vs unbound bounce (stopped rebound vs completed Absolute Past \(\leftrightarrow\) Absolute Future);
- twistor waveform \(f(Z)\) on the conformal 2-sphere of a null generator;
- dressing floor \(\Delta_{\mathrm{Tav}}=E_g\approx 313.1\,\mathrm{MeV}\) as inertial colour dressing, not a \(0^{++}\) glueball pole;
- anomalous dimension \(\alpha=1-\log_7 6\approx 0.079218\).

**Standing unification rule (2026-09-14)**: unbound is the photon conformal sphere only. \(\tau\) may remain an optional bound-lattice *hook*. It is not used below.

---

## 1. Complete symbol key (every symbol used in this derivation)

| Symbol | Meaning |
|--------|---------|
| \(\mathbb{O}\) | Octonion algebra; \(\dim_{\mathbb{R}}\mathbb{O}=8\) |
| \(e_0=1\) | Octonion identity; identified with reset letter \(\Phi_8\) |
| \(e_1,\ldots,e_7\) | Imaginary octonion units; \(e_i^2=-1\), \(e_i e_j=-e_j e_i\) (\(i\neq j\)) |
| \([x,y,z]=(xy)z-x(yz)\) | Associator; vanishes on associative triples, nonzero otherwise |
| \(G_2=\mathrm{Aut}(\mathbb{O})\) | Exceptional automorphism group; preserves the octonion product |
| \(\Phi_k\) | Clockwork letter, \(k=1,\ldots,8\) |
| \(\Phi_1,\ldots,\Phi_6\) | Active domain-capable phases (locked to the six residues of \((\mathbb{Z}/7\mathbb{Z})^\times\)) |
| \(\Phi_7\) | Scrape / Higgs fabric / PK-Mirron channel. **Not a seventh spacetime.** |
| \(\Phi_8\) | Reset / identity / Absolute-Past \(\leftrightarrow\) Absolute-Future inversion seam |
| \((\mathbb{Z}/7\mathbb{Z})^\times=\{1,2,3,4,5,6\}\bmod 7\) | Multiplicative group of order 6; generator \(3\) or \(10\) yields the \(142857\) cycle |
| \(142857\) | Repeating block of \(1/7\); six cyclic permutations label the six domains |
| \(D_a\), \(a=1,\ldots,6\) | Co-located \(3+1\)D domains on \(\mathbb{S}_{\mathrm{SB}}\) |
| \(\mathbb{S}_{\mathrm{SB}}\cong S^3\) | Internal supersphere; domains are co-located, not extra large dimensions |
| \(\mathcal{R}_\gamma\cong\mathbb{CP}^1\) | Conformal (celestial) 2-sphere of a null generator \(\gamma\) |
| \(f(Z)\) | Twistor waveform of an excitation; \(Z\) homogeneous coordinates on \(\mathbb{CP}^3\) or \(\mathbb{CP}^1\) |
| \(\mathcal{P}\) | Absolute Past node (packed, time-canceled) |
| \(\mathcal{F}\) | Absolute Future node (geometrically identical to \(\mathcal{P}\) under \(\Phi_8\)) |
| \(\mathcal{N}\) | Present / now-slice at which a *bound* rebound is stopped |
| Mirron / PK-Mirron | Unbound topological defect; Planck–Kerr mirror sourcing the six-phase cloud |
| \(n_{a,k}\) | Occupation number of domain \(D_a\) in clockwork letter \(\Phi_k\) |
| \(\psi_{a,k}\) | Excitation transforming in a fixed irrep of \(G_2\ltimes S_6^{\mathrm{dom}}\) occupying slot \((a,k)\) |
| \(\mathcal{F}_{\mathrm{TEP}}\) | Selection / suppression factor implementing TEP in residual-\(L\) formulae |
| \(L\) | Residual angular momentum of a rebound stopped at \(\mathcal{N}\) |
| Unbound EM | Completes \(\mathcal{P}\leftrightarrow\mathcal{F}\); \(L=0\); light-like |
| Bound EM | Reaches \(\mathcal{P}\), rebound toward \(\mathcal{F}\) halted at \(\mathcal{N}\); \(L\neq 0\) |
| \(\Delta_{\mathrm{Tav}}=E_g\approx 313.1\,\mathrm{MeV}\) | Minimal inertial dressing of a stopped colour bounce; IR cost of forcing scrape\(\to\)reset |
| \(\alpha=1-\log_7 6\) | Fractal deficit of the 6-of-7 bounce graph |
| \(d_H=\log_7 6\) | Similarity dimension of a 6-branching graph with contraction \(1/7\) |
| \(S_6^{\mathrm{dom}}\) | Permutation action on the six domain labels (not spacetime diffeomorphisms) |
| \(\mathrm{Gr}_{\mathrm{phys}}\) | Physical Grassmann / occupancy algebra on allowed slots |
| \(\hat{P}_{142857}\) | Projector onto configurations whose cycle labels lie in \((\mathbb{Z}/7\mathbb{Z})^\times\) |
| \(\hat{P}_8\) | Projector onto reset-letter overlap |
| \(S_{\mathrm{tw}}\) | Twistor-averaged effective action of a configuration |

**Not used**: \(\tau\), \(R_\tau\), \(S^1_\tau\), \(\theta\), \(A_\mu^{\mathrm{KK}}\), \(R_5(t)\), \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_{313.1})\), \(\rho_\Lambda=\hbar c/\tau^4\).

---

## 2. What is being derived, and what is *not* being assumed

**Target statement (revised, \(\tau\)-free, KK-free)**:

> On the TSB internal algebra, no two excitations transforming under the same irreducible representation of \(G_2\ltimes S_6^{\mathrm{dom}}\) may occupy the same domain–phase slot \((D_a,\Phi_k)\) unless their joint configuration lies in the image of \(\hat{P}_{142857}\) and is annihilated by \(\hat{P}_8\). A forced reset overlap is algebraically the identity channel \(e_i^2=-1\to\Phi_8\) and is projected out of the physical twistor cohomology. The local energy cost of attempting the forbidden overlap is the dressing quantum \(\Delta_{\mathrm{Tav}}\). Fermionic antisymmetry is the exchange cost of that channel; bosonic degeneracy is cycle closure that never enters \(\Phi_8\).

This is a statement about *occupancy of a discrete internal algebra*, not about a compact extra dimension and not about a megaparsec circle.

The original 2026-06-26 derivation used the Tau cylinder as the *arena* in which exclusion acts. That arena is demoted. The algebra already contains the occupancy rule. The cylinder was a visualisation, not a premise.

---

## 3. Algebraic partition (no extra dimension required)

### 3.1 Eight letters from \(\mathbb{O}\)

A real octonion is

\[
x = x_0 e_0 + \sum_{i=1}^{7} x_i e_i,\qquad e_0=1,\quad e_i^2=-1.
\]

**Key**: \(x_0,x_i\in\mathbb{R}\); \(\{e_0,\ldots,e_7\}\) is a real basis of \(\mathbb{O}\).  
\(G_2\) acts by algebra automorphisms and therefore permutes oriented imaginary frames while fixing \(e_0\).

The eight clockwork letters are this basis, named:

\[
\Phi_8 \;\longleftrightarrow\; e_0=1
\qquad\text{(reset / identity / inversion seam)},
\]
\[
\Phi_7 \;\longleftrightarrow\; \text{distinguished imaginary unit reserved as scrape / Mirron},
\]
\[
\Phi_k \;\longleftrightarrow\; \text{the remaining six imaginary units, }k=1,\ldots,6.
\]

This is the locked \(6+1+1\) count: six domain-capable letters, one scrape, one reset. There is no seventh spacetime and no fifth compact coordinate. Phase 7 is a *channel*, not a sister universe.

### 3.2 Why the identity letter is a reset, not a domain

For every imaginary unit,

\[
e_i^2 = -1 = -e_0.
\]

**Key**: squaring any active letter lands in the span of the identity, i.e. in \(\Phi_8\).  
Geometrically this is the Past\(\leftrightarrow\)Future inversion: the same node with opposite orientation. That is why \(\Phi_8\) is the reset seam and why it cannot be used as a *domain label*. A domain that occupied \(\Phi_8\) would be identified with its own inverse and would not support a directed phase advance.

### 3.3 Why there are six domains, not seven

The multiplicative group

\[
(\mathbb{Z}/7\mathbb{Z})^\times \;=\; \{1,2,3,4,5,6\}\pmod{7}
\]

has order \(6\). The residue \(0\bmod 7\) is *not a unit*. Powers of a generator (classically \(10\) or \(3\)) cycle through the six units and reproduce the block \(142857\) and its five rotations.

**Key**: residue \(0\) is the additive identity of \(\mathbb{Z}/7\mathbb{Z}\) and corresponds to the reset letter. It is excluded from the domain set by group law, not by a compactification radius.

The six domains \(D_a\) are the six units. They sit co-located on \(\mathbb{S}_{\mathrm{SB}}\cong S^3\) as an internal frame, exactly as six imaginary directions after one direction has been reserved for scrape. Co-location is an *internal* statement: six copies of \(3+1\)D, not six large extra dimensions and not a KK circle.

The same combinatorics give the locked anomalous dimension without any length:

\[
d_H = \log_7 6 = \frac{\ln 6}{\ln 7},\qquad
\alpha = 1 - \log_7 6 \approx 0.079218.
\]

**Key**: \(d_H\) is the similarity dimension of a graph that branches \(6\) ways under contraction ratio \(1/7\); \(\alpha\) is the deficit relative to a one-dimensional hierarchical coordinate. No megaparsec enters.

---

## 4. Occupancy rule from non-associativity and unit squaring

### 4.1 Slots

An elementary excitation carries a pair of discrete labels

\[
(a,k)\in\{1,\ldots,6\}\times\{1,\ldots,6\}
\]

plus optional coupling to the scrape letter \(\Phi_7\). The reset letter is *not* an allowed slot for a local bound excitation.

Occupation number:

\[
n_{a,k} \;=\; \psi_{a,k}^{\dagger}\psi_{a,k}.
\]

**Key**: \(\psi_{a,k}\) is a mode in one fixed irrep of \(G_2\ltimes S_6^{\mathrm{dom}}\); dagger is the octonion-compatible conjugation (the algebra involution that sends \(e_i\mapsto -e_i\) and fixes \(e_0\)).

### 4.2 Double occupancy forces the reset channel

Suppose two identical modes occupy the same slot, \(n_{a,k}\ge 2\). At the algebra level this is two left multiplications by the same imaginary unit on the same domain frame:

\[
L_{e_k}L_{e_k}(v) \;=\; e_k(e_k v).
\]

If the triple \((e_k,e_k,v)\) were associative this would be \((e_k^2)v=(-1)v\). In \(\mathbb{O}\) the associator

\[
[e_k,e_k,v] \;=\; (e_k e_k)v - e_k(e_k v)
\]

need not vanish for a general \(v\) that itself carries another imaginary factor (a second excitation, or a domain-frame element). Either evaluation lands in the identity channel:

\[
e_k^2 v \;=\; -e_0 v \qquad\text{or a \(G_2\)-image thereof}.
\]

**Key**: \(L_{e_k}\) = left multiplication by \(e_k\); \(v\) = internal frame vector of the second excitation.  
Double occupancy of one imaginary letter is algebraically a map into \(\mathrm{span}\{e_0\}=\Phi_8\). That is the forbidden reset overlap.

This step uses only the multiplication table. It does not use a fifth metric component.

### 4.3 The 142857 escape clause (bosonic cycle-closers)

A configuration whose domain–phase labels multiply inside \((\mathbb{Z}/7\mathbb{Z})^\times\) never hits residue \(0\). Define

\[
\hat{P}_{142857}\;=\;\text{spectral projector onto the six-dimensional regular representation of }(\mathbb{Z}/7\mathbb{Z})^\times,
\]
\[
\hat{P}_8\;=\;\text{projector onto the identity / reset letter}.
\]

Allowed occupancy:

\[
\hat{P}_8\,\Psi \;=\; 0
\qquad\text{or, if the state is a completed unbound bounce,}\qquad
\hat{P}_{142857}\Psi=\Psi
\text{ and the }\Phi_8\text{ component is the global } \mathcal{P}\leftrightarrow\mathcal{F}\text{ identification, not a local slot}.
\]

**Key**: \(\Psi\) is a multi-excitation state in the internal Fock / occupancy space.  
Photons (unbound EM) are the prototype of the second case: they *are* the \(\mathcal{P}\leftrightarrow\mathcal{F}\) generator. Their support may sit on the reset *seam as a global identification* because that is what a completed null bounce *is*. They do not occupy \(\Phi_8\) as a local bound slot.

### 4.4 Exchange = forced passage through reset

Swap two identical bound excitations in the same slot:

\[
\Psi_{\mathrm{swap}} \;=\; \tau_{(12)}\,\Psi.
\]

**Key**: \(\tau_{(12)}\) is the transposition in the occupancy labels.  
On a singly occupied slot the transposition is harmless. On a would-be double occupancy it is the composition of two \(L_{e_k}\) maps, hence a reset insertion. The only way to keep \(\hat{P}_8\Psi=0\) after the swap is

\[
\tau_{(12)}\Psi \;=\; -\Psi.
\]

That is fermionic exchange as a *topological* identity, not as a postulated spin-statistics axiom. Bosonic cycle-closers never enter the slot that would force the insertion, so \(\tau_{(12)}=+1\) is allowed.

Three-quark associator locking (corpus value \(3/4\)) is the same mechanism restricted to an associative triple inside \(\mathbb{O}\): three distinct imaginary units can close an associative \(G_2\) triple; a fourth identical insertion cannot.

---

## 5. Six-domain supersphere constraint (still no KK circle)

The internal supersphere \(\mathbb{S}_{\mathrm{SB}}\cong S^3\) carries six co-located \(3+1\)D frames. Co-location means they share the same external \(3+1\)D events and differ by an internal \(G_2\) / \(E_8\)-projected frame rotation. That is an *internal* \(S^3\), not a compact fifth length.

Allowed flux / pairing: a colour or EM line may connect

\[
(D_a,\Phi_k)\;\longrightarrow\;(D_b,\Phi_{k'})
\]

only when the pair of cycle residues \((r_a r_{k})(r_b r_{k'})\) remains a unit modulo \(7\). A pairing that multiplies to \(0\bmod 7\) is a reset insertion and is excluded.

This is why two identical fermionic modes cannot share one \((D_a,\Phi_k)\): the only internal channel that would absorb the second copy is \(\Phi_8\), which is not a domain.

Scrape \(\Phi_7\) is shared: every domain may couple to the Mirron / Higgs fabric. Sharing \(\Phi_7\) is *not* double occupancy of a domain slot. It is the common mirror off which bounces occur.

---

## 6. Enforcement by twistor cohomology, not by a fifth metric

The original derivation sent forbidden configurations to “infinite action in the conformally averaged twistor geometry.” That clause survives *without* Kaluza–Klein, because the twistor transform already lives on the conformal 2-sphere of a null generator — the unbound photon envelope \(\mathcal{R}_\gamma\cong\mathbb{CP}^1\), not \(S^1_\tau\).

A physical massless field of helicity \(s\) is a cohomology class

\[
f\in H^1(\mathbb{PT},\,\mathcal{O}(-2s-2))
\]

(or the equivalent primed sheaf). **Key**: \(\mathbb{PT}\) = projective twistor space; \(\mathcal{O}(n)\) = tautological line bundle.

A reset-overlap configuration fails to be holomorphic on the celestial sphere: the identity-channel insertion is a conjugation, \(e_i\mapsto -e_i\), which is anti-linear on the spinor flags. Anti-holomorphic sections do not represent on-shell helicity classes. Their Penrose transform vanishes. In the effective \(3+1\)D variational problem that is a configuration with no stationary point — the “prohibitive action” of the old language — without ever writing

\[
d\tilde s^2 = g_{\mu\nu}dx^\mu dx^\nu + \tau^2(d\theta+\kappa A_\mu dx^\mu)^2.
\]

That metric is optional later phenomenology. It is not the enforcement mechanism.

For bound (massive) modes the same obstruction appears after conformal compactification of the stopped-rebound generator: the residual \(L\) is a space-like insertion that keeps the section off the null sheaf unless TEP is respected.

Effective statement:

\[
S_{\mathrm{tw}}[\Psi] \;=\;
\begin{cases}
S_{\mathrm{phys}}[\Psi] & \text{if }\hat{P}_8\Psi=0\text{ or }\Psi\text{ is an unbound cycle-closer},\\
\text{no critical point in }H^1 & \text{if }\hat{P}_8\Psi\neq 0\text{ as a local slot}.
\end{cases}
\]

---

## 7. Bound versus unbound: statistics without a cylinder axis

The bound / unbound split already in the corpus is sufficient.

**Unbound EM (photon, and the completed neutrino-like null channel)**  
Completes \(\mathcal{P}\leftrightarrow\mathcal{F}\). Residual \(L=0\). The two nodes are the same geometric point under \(\Phi_8\). Occupying the seam *globally* is what the excitation *is*. These states are the bosonic cycle-closers. They may pile on the same null generator (photons in one mode).

**Bound EM (mass / gravity channel)**  
Reaches \(\mathcal{P}\); rebound toward \(\mathcal{F}\) is stopped at \(\mathcal{N}\). Residual

\[
\mathbf{L}_{\mathrm{bounce}} \;=\; \ell_0\cdot\mathcal{C}_{\mathrm{constr}}\cdot(\mathbf{r}\times\mathbf{n}_{\mathrm{stop}})\cdot\mathcal{F}_{\mathrm{TEP}}.
\]

**Key** (locked 2026-07-21 / 07-23):
- \(\ell_0\): elementary angular-momentum quantum of one Mirron-phase inversion;
- \(\mathcal{C}_{\mathrm{constr}}=\lvert m\rvert/\lvert V\rvert\): local bound-field density;
- \(\mathbf{r}\): position relative to the Mirron centre;
- \(\mathbf{n}_{\mathrm{stop}}\): unit normal to the Present slice;
- \(\mathcal{F}_{\mathrm{TEP}}\in\{0,1\}\) (or a projector) kills any amplitude with local \(\Phi_8\) occupancy.

If TEP is violated, \(\mathcal{F}_{\mathrm{TEP}}=0\) and there is no residual \(L\) from that channel — the would-be bound state cannot sit in the physical Hilbert space. That is exclusion as a condition for *having mass at all*, not as an extra-dimensional standing wave.

Gravity remains spatial compression from residual \(L\) of *allowed* stopped rebounds. No graviton, no fifth-dimensional Casimir.

---

## 8. Local cost of a forced violation: \(\Delta_{\mathrm{Tav}}\), not a stretch through \(\tau\)

The 2026-06-26 text made the \(313.1\,\mathrm{MeV}\) floor “the minimal energy cost of forcing a forbidden phase-domain overlap” and then transported that cost across scales with \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_{313.1})\). The second half is unavailable once \(\tau\) is demoted.

The first half remains, with the later correction that \(\Delta_{\mathrm{Tav}}\) is **gluon inertial dressing** \(E_g=E_{q\leftarrow g}\), not a \(0^{++}\) pole at \(313\,\mathrm{MeV}\) (retired 2026-09-14).

Operational meaning without \(\tau\):

\[
E_{\mathrm{violation}} \;\ge\; \Delta_{\mathrm{Tav}} \approx 313.1\,\mathrm{MeV}.
\]

**Key**: this is the energy that must be paid to drive a colour bounce off \(\Phi_7\) (scrape / Mirron) into \(\Phi_8\) (reset) while remaining a *local* slot occupation rather than a completed unbound null bounce. It is an infrared dressing quantum of the bound colour sector. It does not need a megaparsec to exist.

Hierarchical *repetition* of the same rule does not need \(\tau\) either. The pair \((6,7)\) is scale-free. Every Apollonian / fractal-globbing level copies the same 6-of-7 occupancy graph. The fractal deficit at every level is the same \(\alpha\). That is “preservation across scales” as self-similarity of a discrete graph, not as a logarithm of two dimensionful lengths.

---

## 9. Operator form (cylinder axis removed)

Replace the old evolution along a cylinder axis \(s\) with a clockwork step operator on the internal algebra:

\[
\hat{U}_{\circlearrowleft} \;=\; \hat{P}_{142857}\,\exp\bigl(-i\,\hat{H}_{\Phi}\bigr)\,\hat{P}_{142857},
\]
\[
\hat{H}_{\Phi} \;=\; \hat{H}_{\mathrm{res}} + \hat{H}_{\mathrm{scrape}} + \lambda_{\infty}\,\hat{P}_8^{\mathrm{local}}.
\]

**Complete key**:
- \(\hat{U}_{\circlearrowleft}\): one discrete advance of the \(G_2\) clockwork (one letter step, not a metric translation);
- \(\hat{P}_{142857}\): keeps the state inside the six units;
- \(\hat{H}_{\mathrm{res}}\): 1/7 resonance / cycle Hamiltonian on the six domain letters;
- \(\hat{H}_{\mathrm{scrape}}\): coupling of every domain to \(\Phi_7\) (Mirron / Higgs fabric);
- \(\hat{P}_8^{\mathrm{local}}\): projector onto *local* reset occupancy (does not include the global unbound \(\mathcal{P}\leftrightarrow\mathcal{F}\) identification);
- \(\lambda_{\infty}\): formal barrier; in any regularised calculation it is replaced by \(\Delta_{\mathrm{Tav}}\) per forced insertion.

No integral \(\int ds\,\hat{H}_\phi(s)\) along \(S^1_\tau\times\mathbb{R}_s\) is required. Time’s arrow, when needed, is the directed advance \(\Phi_k\to\Phi_{k+1}\) among the six active letters plus scrape ticks, as already used in the bound/unbound split.

Occupancy constraint:

\[
n_{a,k}\;\le\;1 \qquad\text{for bound (fermionic) modes},
\]
\[
n_{\gamma}\text{ unrestricted on a single null generator} \qquad\text{for unbound cycle-closers}.
\]

---

## 10. Worked micro-examples

### 10.1 Two identical bound quarks, same domain, same active letter

Labels: \((D_3,\Phi_2)\) twice. Product of residues \(2\cdot 2=4\bmod 7\) is still a unit, *but* the two left multiplications are by the *same* unit on the same frame, so \(e_2^2=-1\) inserts \(\Phi_8\). \(\hat{P}_8^{\mathrm{local}}\neq 0\). State is excluded. Exchange of the two quarks flips sign if one tries to keep them by deforming off the slot — standard baryon antisymmetry.

### 10.2 Three distinct quarks in one nucleon

Labels occupy three different units that form an associative \(G_2\) triple. Associator vanishes. No identity insertion. Associator-locking probability \(3/4\) is the fraction of oriented triples in the Fano plane that close associatively. Allowed. Colour singlet is the \(G_2\)-singlet contraction of that triple plus scrape dressing \(\Delta_{\mathrm{Tav}}\) per gluon inertial energy.

### 10.3 Two photons in one cavity mode

Each photon is an unbound \(\mathcal{P}\leftrightarrow\mathcal{F}\) generator. Their \(\Phi_8\) content is the *global* identification, not a local bound slot. \(\hat{P}_8^{\mathrm{local}}=0\). Bose occupation unrestricted.

### 10.4 Attempted seventh domain

A putative \(D_7\) would have to sit on residue \(0\) or on \(\Phi_7\) used as a spacetime. Residue \(0\) is \(\Phi_8\). \(\Phi_7\) is scrape, not a domain. Both violate \(6+1+1\). There is no seventh co-located universe in this derivation.

---

## 11. What dropped out when \(\tau\) and KK were removed

| Old load-bearing object | Status in this derivation |
|-------------------------|---------------------------|
| \(S^1_\tau\) of \(7\,h^{-1}\mathrm{Mpc}\) | Not used. Optional later lattice hook only. |
| 5D EKK line element | Not used. |
| \(n_{\mathrm{hier}}=\log_7(\tau/\lambda_{313.1})\) | Not used. Scale repetition is the self-similar \(6\)-of-\(7\) graph. |
| Cylinder axis \(s\) as time | Replaced by discrete clockwork advance. |
| Vacuum energy as Casimir \(A/\tau^4\) | Not derived here and not required for TEP. |
| “Infinite action on the cylinder” | Replaced by vanishing twistor cohomology of a local reset insertion. |

| Object that still carries TEP | Role |
|------------------------------|------|
| \(e_i^2=-1\) | Algebraic identity of double occupancy with reset |
| \((\mathbb{Z}/7\mathbb{Z})^\times\) | Six allowed domain residues |
| \(\Phi_7\) Mirron scrape | Shared mirror; dressing channel |
| \(\Phi_8\) | Reset seam; global only for unbound bounces |
| Twistor \(H^1\) | On-shell filter |
| Bound vs unbound split | Fermion vs boson |
| \(\Delta_{\mathrm{Tav}}\) | Local IR cost of a forced insertion |
| \(\alpha=1-\log_7 6\) | Fractal deficit of the allowed graph |

---

## 12. Relation to the 2026-06-26 statement

The 2026-06-26 sentence is recovered by *translation*, not by extra geometry:

- “Tav manifold” \(\to\) internal occupancy algebra of \(G_2\ltimes S_6^{\mathrm{dom}}\) plus scrape and reset letters.
- “identical domain-phase combinations” \(\to\) same \((D_a,\Phi_k)\).
- “closes under the full \(142857\) cycle without invoking the reset phase” \(\to\) \(\hat{P}_{142857}=1\) and \(\hat{P}_8^{\mathrm{local}}=0\).
- “infinite action in conformally averaged twistor geometry” \(\to\) empty \(H^1\) for a local identity insertion.
- “preserved across scales by conformal mapping” \(\to\) self-similarity of the \(6\)-of-\(7\) graph, measured by \(\alpha\).

Nothing in that translation requires a compact fifth circle or a \(7.5\,\mathrm{Mpc}\) radius. Those objects, if used later, must earn their keep as a lattice hypothesis. They are not premises of exclusion.

---

## 13. Falsifiers that do *not* depend on \(\tau\)

Because this derivation does not use the Mpc circle, it can fail without any survey-cell measurement.

1. **Algebra**: if a consistent real division-algebra construction with seven *domain* letters (not scrape) is forced by data, \(6+1+1\) is wrong and this TEP is wrong.
2. **Statistics**: if an elementary excitation that is bound (nonzero residual \(L\), nonzero rest frame) is observed to occupy one mode with \(n\ge 2\) at the same \((D_a,\Phi_k)\) labels, the occupancy rule fails.
3. **Dressing floor**: if the inertial colour-dressing quantum is not near \(313.1\,\mathrm{MeV}\) and no other local cost of scrape\(\to\)reset exists, the IR regularisation clause fails (the *selection rule* could still stand).
4. **Clockwork count**: if precision interferometry / Casimir / hadronic spectra show a stable period that is not \(7\) (or not \(6\) active plus one scrape), the partition fails.
5. **Twistor filter**: if an on-shell massless amplitude is measured whose little-group structure requires a local identity-channel insertion, the cohomology clause fails.

None of these tests is a measurement of \(7\,h^{-1}\mathrm{Mpc}\).

---

## 14. Compact restatement

**Premises**: octonion product, \(G_2\) automorphism, six units of \((\mathbb{Z}/7\mathbb{Z})^\times\), scrape letter \(\Phi_7\), reset letter \(\Phi_8\), bound vs unbound bounce, twistor on-shell filter.

**Lemma**. Squaring an imaginary unit is the reset letter.  
**Lemma**. Domain labels are the six units; residue \(0\) is not a domain.  
**Lemma**. Two identical left multiplications on one domain frame square into the reset.  
**Lemma**. A local reset insertion is anti-holomorphic on the celestial sphere and drops out of twistor cohomology.  
**Lemma**. Unbound null generators *are* the global Past\(\leftrightarrow\)Future identification; they do not occupy reset locally.

**Theorem (TEP, \(\tau\)-free, KK-free)**. Bound excitations in one \(G_2\ltimes S_6^{\mathrm{dom}}\) irrep obey \(n_{a,k}\le 1\). Unbound cycle-closers may pile. Forced local reset overlap costs at least the dressing quantum \(\Delta_{\mathrm{Tav}}\) and has no on-shell twistor representative.

Fermions and bosons are the two sides of that theorem. Gravity remains residual \(L\) of *allowed* stopped rebounds. No fifth dimension was required.

---

## 15. Session result

The Topological Exclusion Principle stands after removing the Tau \(7.5\,\mathrm{Mpc}\) circle and the Kaluza–Klein fifth dimension. Those objects were an arena, not a cause. The cause is the octonion identity channel plus the order-\(6\) unit group plus the bound/unbound split, filtered by twistor cohomology.

\(\tau\) remains an optional bound-lattice hook, consistent with the 2026-09-14 unification rule: unbound is the photon conformal sphere only.

**File created**: 2026-09-20  
**Location**: `Personal_Files/Session_2026-09-20_TEP_Without_Tau_Circle_and_KK5.md`

---

*This session supersedes the load-bearing use of \(S^1_\tau\) and the 5D EKK line element in the 2026-06-26 TEP derivation. It does not retire TEP. It retires those two premises.*
