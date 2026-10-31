# Session 2026-09-12 — Envelope expansion, Tau-circle formation, Mirron proliferation

**Claim under study:** Many bound Tau circles and many PK-Mirrons appear as 3+1D spatial envelopes expand, while an atemporal Tau cylinder is the same object as the Absolute-Past → Absolute-Future 4D circle.

**Status:** Process geometry stated. Counting relation derived. Value of \(\tau\) not derived.

**Depends on:**  
`Session_2026-09-12_Unbound_4D_Absolute_Past_Future_Bound_KK.md`  
`2026-09-02_Seventh_Phase_Unbound_Circle_Integration.md`  
`2026-09-05_TSB_Core_Geometry_v0.1b_Global_Manifold_and_Local_Fibers.md`

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(\mathcal{P}\) | Absolute Past (packed slice) |
| \(\mathcal{N}\) | Present / Prime now-slice |
| \(\mathcal{F}\) | Absolute Future (horizon-exit slice) |
| \(\mathcal{C}_{\mathcal{PF}}\) | Atemporal 4D circle: the closed bounce \(\mathcal{P}\leftrightarrow\mathcal{F}\) |
| \(\mathcal{M}_{\mathrm{Tav}}\) | Global Tav total space (not automatically an infinite circle) |
| \(M_4\) | Observable 3+1 base |
| \(\pi\) | Projection \(\mathcal{M}_{\mathrm{Tav}}\to M_4\) if a bundle is used |
| \(S^1_\tau(x)\) | Bound compact KK fiber at event \(x\in M_4\) |
| \(\tau\) | Frozen radius of that fiber (lattice input; not an output of this note) |
| \(\theta\) | Fiber angle, \(\theta\sim\theta+2\pi\) |
| \(A_\mu\) | Graviphoton |
| \(\kappa\) | Coupling of \(A_\mu\) to \(d\theta\) |
| \(g_{\mu\nu}\) | Prime 3+1 metric |
| \(a(t)\) | Prime scale factor |
| \(H\) | \(\dot a/a\) |
| \(E(t,y)\) | Spatial envelope of a bound cell or of a PK-Mirron, labelled by comoving centre \(y\) |
| \(\mathcal{B}(t,y)\) | Interior of that envelope (3-ball in the Prime spatial slice) |
| \(r_{\mathrm{phys}}(t,y)\) | Physical radius of \(E(t,y)\) |
| \(\chi\) | Comoving radial coordinate |
| \(\ell_{\mathrm{cap}}\) | Maximum physical radius at which one envelope remains a single bound cell |
| \(V_{\mathrm{env}}(t)\) | Physical 3-volume of one envelope |
| \(V_{\mathrm{avail}}(t)\) | Physical 3-volume of the Prime patch still inside the relevant causal cutoff |
| \(N_\tau(t)\) | Number of written bound Tau fibers on the slice at \(t\) |
| \(N_{\mathrm{M}}(t)\) | Number of PK-Mirrons on that slice |
| \(\mu\) | Mean number of Mirrons per written fiber (geometric incidence) |
| \(\Phi_7\) | Seventh-phase map (atemporal Higgs / Planckian-mirror fabric) |
| \(\Phi_8\) | Dynamic Refresh tick |
| \(\phi_{1\ldots 6}\) | Six co-located Superblock domains |
| PK-Mirron | Planck–Kerr mirror entity (not “soliton”) |
| \(K(\mathcal{P},\mathcal{F})\) | Bounce kernel from Past to Future |
| \(L\) | Residual angular momentum of a bounce stopped at \(\mathcal{N}\) |
| \(R_{\mathrm{EH}}(t)\) | Cosmic event-horizon proper radius |
| \(c\) | Prime-metric speed of light |
| \(\mathrm{Hol}_\tau\) | Holonomy once around a bound fiber |

Do not use “soliton.” The proliferating objects are PK-Mirrons.

---

## 2. Two objects that must stay distinct

**Atemporal cylinder / 4D circle \(\mathcal{C}_{\mathcal{PF}}\).**  
One closed 3+1 history from packed Past to Future horizon. It does not expand. Expansion is a *parameter along the 4D metric*, not a change of \(\mathcal{C}_{\mathcal{PF}}\) itself. Phase 7 reads this object into local physics.

**Bound fiber \(S^1_\tau(x)\).**  
Compact fifth circle at a written node. Radius frozen. Many copies appear because many *base points* \(x\) are written as envelopes split, not because \(\tau(t)\) grows.

\[
d\tilde s^2
=
g_{\mu\nu}(x)\,dx^\mu dx^\nu
+
\tau^2\bigl(d\theta+\kappa A_\mu\,dx^\mu\bigr)^2.
\]

**Key:** \(g_{\mu\nu}\) = Prime metric; \(x^\mu=(t,\mathbf{x})\); \(\tau\) = frozen fiber radius; \(\theta\) = fiber angle; \(A_\mu\) = graviphoton; \(\kappa\) = coupling.

Unification is **incidence**: every written fiber and every Mirron is a sample of the same \(\mathcal{C}_{\mathcal{PF}}\) through \(\Phi_7\). It is not two radii becoming one.

---

## 3. Spatial envelope

On a Prime slice of time \(t\), a bound cell is a 3-ball whose boundary is the envelope:

\[
E(t,y)
=
\bigl\{\,
\mathbf{x}
\;\big|\;
a(t)\,d_{\mathrm{com}}(\mathbf{x},y)
=
r_{\mathrm{phys}}(t,y)
\,\bigr\}.
\]

**Key:** \(E\) = 2-sphere envelope; \(y\) = comoving centre; \(d_{\mathrm{com}}\) = comoving distance; \(r_{\mathrm{phys}}\) = physical radius; \(a(t)\) = scale factor.

Interior:

\[
\mathcal{B}(t,y)
=
\bigl\{\,
\mathbf{x}
\;\big|\;
a(t)\,d_{\mathrm{com}}(\mathbf{x},y)
\le
r_{\mathrm{phys}}(t,y)
\,\bigr\},
\qquad
V_{\mathrm{env}}(t,y)
=
\frac{4\pi}{3}r_{\mathrm{phys}}(t,y)^3.
\]

**Key:** \(\mathcal{B}\) = interior 3-ball; \(V_{\mathrm{env}}\) = physical volume of that ball.

At \(\mathcal{P}\) there is one envelope (or one overlapping pack counted as one coherent ball). Its physical radius is below the cap:

\[
r_{\mathrm{phys}}(t_{\mathcal{P}},y_0)
<
\ell_{\mathrm{cap}}.
\]

**Key:** \(t_{\mathcal{P}}\) = Past-slice time; \(y_0\) = unique early centre; \(\ell_{\mathrm{cap}}\) = exhaustion cap.

---

## 4. Expansion of envelopes (3+1 process)

Comoving centres do not move. Physical envelopes grow because \(a(t)\) grows.

If an envelope **comoves** (material boundary fixed in \(\chi\)):

\[
r_{\mathrm{phys}}(t,y)
=
a(t)\,\chi_E(y).
\]

**Key:** \(\chi_E(y)\) = comoving envelope radius of cell \(y\).

If instead the cell tries to keep a **fixed physical** size, \(r_{\mathrm{phys}}=\ell_{\mathrm{cap}}\) constantly, new centres must be written when the available patch outgrows one cap. That is the formation rule. The standing convention is the second reading at the *cap*, the first reading *between* writes: after a write, sites stay comoving; when a physical radius would exceed \(\ell_{\mathrm{cap}}\), the envelope splits.

Split rule (geometric, not biological):

\[
\text{if }
r_{\mathrm{phys}}(t,y)
=
\ell_{\mathrm{cap}}
\text{ then }
\mathcal{B}(t,y)
\text{ is replaced by }
\bigcup_{k=1}^{q}
\mathcal{B}(t,y_k)
\text{ with }
r_{\mathrm{phys}}(t,y_k)
<
\ell_{\mathrm{cap}}.
\]

**Key:** \(q\) = number of daughter interiors; \(y_k\) = new comoving centres.  
Minimal tiling of a 3-ball by equal smaller balls is not unique; the **count** that is unique is the volume ratio, not the packing graph.

---

## 5. Formation of many Tau circles (derived count)

A bound fiber \(S^1_\tau(x)\) is written when and only when a new envelope centre \(y\) is written. One fibre per centre on the Prime slice:

\[
N_\tau(t)
=
\#\{\,y : E(t,y)\text{ is a maximal bound envelope}\,\}.
\]

**Key:** \(N_\tau(t)\) = number of bound Tau circles on the slice.

Available physical volume of the Prime patch still in play (inside the event horizon, not the particle horizon):

\[
V_{\mathrm{avail}}(t)
=
\frac{4\pi}{3}
\bigl[\min\bigl(R_{\mathrm{EH}}(t),\,a(t)\chi_{\mathrm{patch}}\bigr)\bigr]^3.
\]

**Key:** \(R_{\mathrm{EH}}\) = event-horizon proper radius; \(\chi_{\mathrm{patch}}\) = comoving radius of the original packed patch.

Volume of one allowed cell:

\[
V_{\mathrm{cell}}
=
\frac{4\pi}{3}\ell_{\mathrm{cap}}^3.
\]

**Key:** \(V_{\mathrm{cell}}\) = max bound-cell volume.

Then the only scale-free count this geometry produces is

\[
N_\tau(t)
=
\left\lfloor
\frac{V_{\mathrm{avail}}(t)}{V_{\mathrm{cell}}}
\right\rfloor
=
\left\lfloor
\left(
\frac{\min\bigl(R_{\mathrm{EH}}(t),\,a(t)\chi_{\mathrm{patch}}\bigr)}
{\ell_{\mathrm{cap}}}
\right)^3
\right\rfloor.
\]

**Key:** floor function because a partial cell is not a written node.

At \(\mathcal{P}\), \(V_{\mathrm{avail}}<V_{\mathrm{cell}}\) so \(N_\tau=1\) (packed).  
As \(a(t)\) grows, \(N_\tau\) jumps by integers when the cube of the radius ratio crosses the next integer. That is **proliferation of Tau circles during 3+1 expansion**.

This derives \(N_\tau(t)\) as a function of \(a(t)\), \(R_{\mathrm{EH}}(t)\), \(\chi_{\mathrm{patch}}\), and \(\ell_{\mathrm{cap}}\).  
It does **not** derive \(\ell_{\mathrm{cap}}=\tau\). Setting the cap equal to Gatlin’s \(7\,h^{-1}\mathrm{Mpc}\) is an identification, not a step in this counting.

---

## 6. Proliferation of PK-Mirrons

A PK-Mirron is the \(\Phi_7\) coupling point: the Planckian-mirror fabric at which the atemporal cylinder is sampled into a bound fiber.

Incidence axiom (geometric, minimal):

\[
N_{\mathrm{M}}(t)
=
\mu\,N_\tau(t).
\]

**Key:** \(N_{\mathrm{M}}\) = Mirron number; \(\mu\) = Mirrons per written fiber.

Default working value \(\mu=1\): one Mirron writes one fiber (one scrape of \(\Phi_7\) per cell). Then

\[
N_{\mathrm{M}}(t)
=
N_\tau(t)
=
\left\lfloor
\left(
\frac{\min\bigl(R_{\mathrm{EH}}(t),\,a(t)\chi_{\mathrm{patch}}\bigr)}
{\ell_{\mathrm{cap}}}
\right)^3
\right\rfloor.
\]

**Key:** same symbols as §5.

If a fiber requires a 6-domain handshake plus one mirror, \(\mu=1\) still (one mirror, six domain phases). \(\mu=6\) would mean one Mirron per domain per cell and must be justified by a named \(G_2\) incidence, not by taste.

Growth law between splits (smooth envelope expansion, discrete writes):

\[
\frac{dN_{\mathrm{M}}}{dt}
=
0
\quad\text{except at split times }t_*
\text{ where }
\frac{\min(R_{\mathrm{EH}},a\chi_{\mathrm{patch}})}{\ell_{\mathrm{cap}}}
\in\mathbb{Z}.
\]

**Key:** \(t_*\) = instants when the radius ratio is an integer; Mirron number is piecewise constant.

That is the geometric proliferation: Mirrons do not “breed.” New mirrors are **written** when a new envelope centre is required by the cap.

---

## 7. Atemporal unification with \(\mathcal{C}_{\mathcal{PF}}\)

On \(M_4\), writes are ordered by \(t\).  
On \(\mathcal{C}_{\mathcal{PF}}\), Past and Future are two cuts of one circle. The Tau cylinder that is “atemporal” is this circle, not a fifth radius that runs with \(a(t)\).

Identification:

\[
\mathcal{C}_{\mathcal{PF}}
\;\simeq\;
\text{atemporal Tau cylinder},
\qquad
\Phi_7
=
\text{evaluation map }
\mathcal{C}_{\mathcal{PF}}
\to
S^1_\tau(x).
\]

**Key:** \(\simeq\) = identification of the 4D bounce circle with the atemporal cylinder; \(\Phi_7\) = how a local fiber reads that cylinder.

Every Mirron at every \(t\) samples the **same** \(\mathcal{C}_{\mathcal{PF}}\). Proliferation in 3+1 is many evaluation points, not many cylinders.

Bounce language on that circle:

\[
K(\mathcal{P},\mathcal{F})
=
\text{completed unbound bounce},
\qquad
K(\mathcal{P},\mathcal{N})
=
\text{bounce stopped at Present}.
\]

**Key:** \(K(\mathcal{P},\mathcal{F})\) = full Past-to-Future kernel (light-like, no residual \(L\)); \(K(\mathcal{P},\mathcal{N})\) = truncated kernel; residual \(L\) sources spatial compression in \(\mathcal{B}(t,y)\).

A new envelope is written when the stopped bounce in a ball can no longer cover the grown 3-volume without exceeding \(\ell_{\mathrm{cap}}\). The extra covering is a new stopped bounce, hence a new Mirron, hence a new \(S^1_\tau\).

Holonomy of the bound fiber remains Loop A:

\[
\mathrm{Hol}_\tau
=
\mathcal{P}\exp\oint_{S^1_\tau}\omega_\theta\,d\theta
\quad\text{(frozen \(\tau\))}.
\]

**Key:** \(\omega_\theta\) = connection component along the fiber; \(\mathrm{Hol}_\tau\) does not run with \(a(t)\).

Loop B is still the discrete word \(\Phi_8\circ\cdots\circ\Phi_1\) with \(\Phi_7\) the scrape.

---

## 8. Process in one line

\[
\underbrace{1\text{ envelope at }\mathcal{P}}_{N_\tau=N_{\mathrm{M}}=1}
\;
\xrightarrow{\;a(t)\;}
\;
\underbrace{r_{\mathrm{phys}}\to\ell_{\mathrm{cap}}}_{\text{cap}}
\;
\xrightarrow{\;\text{split}\;}
\;
\underbrace{N_\tau=N_{\mathrm{M}}=\lfloor(R_{\mathrm{avail}}/\ell_{\mathrm{cap}})^3\rfloor}_{\text{many fibers, many Mirrons}}
\;
\xrightarrow{\;R_{\mathrm{EH}}\;}
\;
\underbrace{\text{nodes leave }\mathcal{C}_{\mathcal{PF}}\text{ of this observer}}_{\mathcal{F}}.
\]

**Key:** \(R_{\mathrm{avail}}=\min(R_{\mathrm{EH}},a\chi_{\mathrm{patch}})\).

---

## 9. What is derived / what is not

| Item | Status |
|------|--------|
| Envelope growth \(r_{\mathrm{phys}}=a\chi_E\) between writes | derived from 3+1 metric |
| Split when \(r_{\mathrm{phys}}=\ell_{\mathrm{cap}}\) | geometric cap rule (exhaustion) |
| \(N_\tau=\lfloor(R_{\mathrm{avail}}/\ell_{\mathrm{cap}})^3\rfloor\) | derived from volume tiling |
| \(N_{\mathrm{M}}=\mu N_\tau\) with working \(\mu=1\) | incidence axiom |
| \(\mathcal{C}_{\mathcal{PF}}\) = atemporal cylinder; \(\Phi_7\) = evaluation | unification rule |
| \(\ell_{\mathrm{cap}}=\tau=7\,h^{-1}\mathrm{Mpc}\) | **not** derived here |
| \(313.1\,\mathrm{MeV}\) as scrape cost | **not** derived here |
| Dynamical fifth radius \(R_5(t)\) | remains dropped |

---

## 10. Next calculation

1. Specify the split tiling: face-centred packing vs Voronoi of the Prime 3-geometry, so \(q\) is not free.  
2. Name \(\Phi_7\) as an \(8\times 8\) real matrix; check associator on the 8-letter word.  
3. Write \(K(\mathcal{P},\mathcal{F})\) and the stopped condition that outputs \(L\) with empty MeV/Mpc right-hand side.

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
