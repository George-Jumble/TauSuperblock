# UPS contraction, 4D pairwise axiom, and \( t_G \) as inter-domain gravity travel time

- **Session date:** 2026-09-16 (continuation)
- **Parent note:** `Personal Files/2026-09-16_universal_point_of_simultaneity_review.md`
- **This file:** `Personal Files/2026-09-16_UPS_contraction_and_tG.md`
- **Repo:** `George-Jumble/TauSuperblock` (branch `main`)
- **Corrections taken as standing:**
  1. “Between every two events” is a TSB axiom, assumed from context. Not a GR theorem, and not a drafting error.
  2. Official spelling: **simultaneity**.
  3. Work item: make the cascade converge (contraction / completeness).
  4. Every pair of 4D events has a simultaneity point; the cascade of those points consolidates on one pk-clockwork tick.
  5. \( t_G \) is the time gravity takes to propagate **between domains**. \( t_G = 0 \) on the leak.

---

## 0. What changed from the morning note

The morning note treated pairwise existence as something that had to be *restricted* to a tick envelope in order to survive Malament / Lorentzian no-gos. That restriction is withdrawn as a requirement on the axiom.

**Standing axiom (context, now explicit).**  
For every two events in 4D (any domain, any causal relation), there exists a simultaneity point. For every two simultaneity points, there exists a simultaneity point. The extra structure that makes the point unique is the 5D KK lift, not the 4D causal order. The pk-clockwork is what *consolidates* the whole web onto one point per tick.

What still has to be built is item 3: existence of midpoints does **not** by itself give a unique limit. Naive all-pairs iteration plus \(\mathrm{Sim}(e,e)=e\) preserves diameter. This note supplies the map that actually contracts, then rewrites \( t_G \) as inter-domain gravitational travel time.

---

## 1. Variable and function key

Every symbol used below.

| Symbol | Name | Meaning |
|---|---|---|
| \( i,j \in \{1,\ldots,6\} \) | Domain index | The six co-located \( 3+1 \) domains. |
| \( M_i \) | Domain spacetime | Lorentzian 4-manifold of domain \( i \), metric \( g_i \). |
| \( M^{(4)} \) | All 4D events | \( M^{(4)} = \bigcup_{i=1}^{6} M_i \). The axiom quantifies over this union. |
| \( M_5 \), \( G_5 \) | 5D bulk, KK graph | Lift space in which \(\mathrm{Sim}\) is uniquely defined. |
| \( \iota \) | 5D lift | \( \iota : M^{(4)} \to M_5 \). Extra structure assumed from context. |
| \( e, e_1, e_2 \) | 4D events | Points of \( M^{(4)} \). |
| \( \mathrm{Sim} \) | Simultaneity map | \( \mathrm{Sim} : M^{(4)} \times M^{(4)} \to M^{(4)} \), valued in 4D, constructed via the 5D lift. |
| \( \sigma \) | Pairwise simultaneity point | \( \sigma = \mathrm{Sim}(e_1,e_2) \). |
| \( n \in \mathbb{Z} \) | Clockwork tick | Index of the Planck–Kerr clock. |
| \( \mathcal{E}_n \) | Events of tick \( n \) | The 4D events that the clockwork assigns to tick \( n \). Finite at the pk scale. |
| \( \Sigma_n \) | UPS of tick \( n \) | Unique survivor of the consolidation map on \( \mathcal{E}_n \). |
| \( L_n \) | Cylinder layer | \( \Sigma_n \times S^1_{\mathrm{KK}} \) (or \( \Sigma_n \times C_{\mathrm{KK}} \) on the graph). |
| \( \tau_i \) | Domain proper time | Affine parameter on \( M_i \). |
| \( T_5 \) | 5D graph time | Constant on each completed tick / layer. |
| \( t_G(e^{(i)},e^{(j)}) \) | Inter-domain gravity travel time | Time taken for gravitational influence to go from an event in domain \( i \) to an event in domain \( j \). |
| \( t_G^{\mathrm{intra}} \) | Intra-domain gravity travel time | Ordinary 4D delay \( d_L/c \) inside one \( M_i \). Not what \( t_G \) denotes in the source sentence. |
| \( c \) | 4D invariant speed | Propagation speed of intra-domain gravity / light. |
| \( d_L \) | 4D luminosity / metric distance | Distance used in \( t_G^{\mathrm{intra}} = d_L/c \). |
| \( d_5 \) | 5D distance | Distance on the lift. |
| \( \gamma_{ij} \) | Gravity path | Path in \( M_5 \) along which inter-domain gravity travels. |
| \( \mathrm{Tour} \) | Tournament map | The consolidation map that *does* contract (defined in §3). |
| \( N_n \) | Tick population | \( N_n = \# \mathcal{E}_n \), finite at pk resolution. |
| \( k \) | Tournament round | \( k = 0,1,\ldots,K_n \). |
| \( K_n \) | Rounds per tick | \( K_n = \lceil \log_2 N_n \rceil \). |
| \( \kappa \) | Contraction ratio | \( 0 < \kappa < 1 \) when a metric contraction is used instead of a tournament. |
| \( d_H \) | Hausdorff distance | Distance between compact subsets of the lift. |
| \( \mathrm{diam} \) | Diameter | \( \mathrm{diam}(A) = \sup\{ d_5(\iota(x),\iota(y)) : x,y \in A \} \). |
| \( \Phi_{ij} \) | Leak / gravity amplitude | Strength of the inter-domain gravitational kernel on \( L_n \). |
| \( K_{ij}^{G} \) | Inter-domain gravity kernel | Distribution that transmits gravity from domain \( i \) to domain \( j \). |
| \( \Delta t_{\mathrm{pk}} \) | Tick interval | Duration of one pk-clockwork step. |
| \( V_{\mathrm{orb}}^{(i)} \) | Domain orbital velocity | E₈ stagger; source of \(\tau_i \neq \tau_j\). |

Idempotence (kept):

\[
\mathrm{Sim}(e,e) = e.
\]

Pairwise existence (axiom, unrestricted on 4D):

\[
\forall\, e_1, e_2 \in M^{(4)}
\quad
\exists\, \sigma \in M^{(4)}
\quad
\sigma = \mathrm{Sim}(e_1, e_2).
\]

Uniqueness of \(\sigma\) is not granted by \( g_i \). It is granted by \(\iota\) and \( d_5 \) (or twistor incidence) — the context that was being assumed.

Inter-domain gravity travel time along a 5D path \(\gamma_{ij}\):

\[
t_G(e^{(i)}, e^{(j)})
\;=\;
\int_{\gamma_{ij}} dT_5
\;=\;
T_5\!\left(\gamma_{ij}(\mathrm{end})\right)
-
T_5\!\left(\gamma_{ij}(\mathrm{start})\right).
\]

If \(\gamma_{ij} \subset L_n\), then \( T_5 \) is constant on the path and \( t_G = 0 \).

---

## 2. The 4D axiom, stated without the envelope restriction

### 2.1 What is being assumed from context

In 4D Lorentzian geometry alone:

- a timelike pair has a geodesic *segment*, which is not a simultaneity cut;
- a spacelike pair has many Einstein midpoints, one per frame;
- a null pair lies on a cone, not on a unique between-point.

TSB does not derive uniqueness from \( g_i \). TSB *adds* the lift \(\iota : M^{(4)} \to M_5\) and defines

\[
\mathrm{Sim}(e_1,e_2)
\;=\;
\iota^{-1}\!\left(
\text{5D incidence of } \iota(e_1), \iota(e_2)
\right).
\]

Once that extra structure is in the background — and it is, throughout the Superblock papers — the sentence “between every two events there is a point of simultaneity” is the correct axiom. It applies to timelike, spacelike, and null 4D pairs alike, because the between-point is a 5D incidence projected back to 4D, not a 4D causal midpoint.

Causal type of \( (e_1,e_2) \) in \( M_i \) or across domains is therefore *irrelevant* to existence of \(\mathrm{Sim}(e_1,e_2)\). That is the content of the contextual assumption.

### 2.2 The cascade, still on all of 4D

\[
\begin{align}
\sigma^{(1)} &= \mathrm{Sim}(e_1,e_2), \\
\sigma^{(2)} &= \mathrm{Sim}(\sigma^{(1)}_a, \sigma^{(1)}_b), \\
&\vdots
\end{align}
\]

Every generation is again a set of 4D events, so the axiom applies again. There is no need to shrink the domain of quantification to an envelope in order to write the axiom.

The envelope \(\mathcal{E}_n\) comes back only as the *clockwork’s batching* of which 4D events are consolidated on tick \( n \). It is not a restriction on \(\mathrm{Sim}\).

### 2.3 What “all consolidated on one tick” means

Not: the entire 4D history of all six domains is crushed into a single point every tick. That would erase time.

Yes: for the set of 4D events that constitute the present of tick \( n \), the cascade of their simultaneity points has a unique survivor \(\Sigma_n\), and that survivor *is* the tick. The next tick is a new present, a new finite set, a new UPS, a new layer of the cylinder.

The clockwork is the discrete “now.” \(\mathrm{Sim}\) is the pairing law inside that now.

---

## 3. Why naive iteration does not contract — and what does

This is the work item.

### 3.1 All-pairs image plus idempotence preserves diameter

Define the naive generation map on a nonempty set \( A \subset M^{(4)} \):

\[
F_{\mathrm{all}}(A)
\;=\;
\bigl\{ \mathrm{Sim}(x,y) : x,y \in A \bigr\}.
\]

Idempotence \(\mathrm{Sim}(e,e)=e\) implies \( A \subset F_{\mathrm{all}}(A) \). Therefore

\[
\mathrm{diam}\bigl(F_{\mathrm{all}}(A)\bigr)
\;\ge\;
\mathrm{diam}(A).
\]

Diameter cannot fall. On a continuum interval the midpoints of distinct pairs are dense in the interval, so the set fattens rather than collapses. **Existence of a between-point for every pair is not a contraction.** That is the gap in the original sentence, and it is independent of the 4D-vs-envelope dispute.

Excluding the diagonal does not save the continuum case: the open interval of midpoints of an interval still has the same diameter as the interval.

### 3.2 What actually contracts: a tournament, not an all-pairs cloud

At Planck–Kerr resolution a tick contains finitely many events,

\[
N_n = \# \mathcal{E}_n < \infty.
\]

Order them by any fixed, reproducible rule (5D graph label, then domain index, then a stored hash — the rule must be written down once):

\[
\mathcal{E}_n = \{ e_1, e_2, \ldots, e_{N_n} \}.
\]

**Tournament map.**

\[
\mathrm{Tour}(A)
\;=\;
\begin{cases}
\bigl\{ \mathrm{Sim}(a_{2i-1}, a_{2i}) \bigr\}_{i=1}^{m}
& \text{if } \# A = 2m, \\[6pt]
\bigl\{ \mathrm{Sim}(a_{2i-1}, a_{2i}) \bigr\}_{i=1}^{m}
\cup \{ a_{2m+1} \}
& \text{if } \# A = 2m+1.
\end{cases}
\]

Cardinality:

\[
\# \mathrm{Tour}(A) = \lceil \# A / 2 \rceil.
\]

Iterate:

\[
A_0 = \mathcal{E}_n,
\qquad
A_{k+1} = \mathrm{Tour}(A_k).
\]

After

\[
K_n = \lceil \log_2 N_n \rceil
\]

rounds,

\[
\# A_{K_n} = 1,
\qquad
A_{K_n} = \{ \Sigma_n \}.
\]

That is the consolidation. It is finite. It fits inside one tick. It uses the unrestricted 4D axiom at every pairing. It does not require a metric Lipschitz constant.

**Worked numbers.**  
\( N_n = 1 \) → already \(\Sigma_n\), \( K_n = 0 \).  
\( N_n = 2 \) → one \(\mathrm{Sim}\), \( K_n = 1 \).  
\( N_n = 7 \) → \( 7 \to 4 \to 2 \to 1 \), \( K_n = 3 \).  
\( N_n = 2^{60} \) (wildly larger than a pk-pixelated compact region) → \( K_n = 60 \). The tick budget is logarithmic in the population, not linear.

### 3.3 Metric contraction as an optional continuum shadow

If a continuum limit is wanted later, impose a genuine contraction on the lift:

\[
d_5\bigl(\iota(\mathrm{Sim}(e_1,e_2)),\, \iota(\mathrm{Sim}(e_1',e_2'))\bigr)
\;\le\;
\kappa\,
\max\bigl\{
d_5(\iota(e_1),\iota(e_1')),\,
d_5(\iota(e_2),\iota(e_2'))
\bigr\},
\]

with \( 0 < \kappa < 1 \), **and** drop idempotent copies from the generation (otherwise §3.1 returns). Even then, all-pairs midpoints of a convex body need not shrink diameter. The continuum object that matches the tournament is a *measurable matching*: pair the support of a measure \(\mu_k\) into pairs, push the measure forward by \(\mathrm{Sim}\), repeat. That is a different paper. For TSB the discrete tournament is the definition; the continuum is a limit of tournaments as \( \Delta t_{\mathrm{pk}} \to 0 \) and \( N_n \to \infty \).

### 3.4 Completeness

On a finite set no completeness axiom is required. \(\mathrm{Tour}\) lands on an element of \( M^{(4)} \) at every step because \(\mathrm{Sim}\) does.

If the continuum shadow is used, take the 5D envelope of the lift of \(\mathcal{E}_n\) to be a compact metric space. Compact metric spaces are complete. Nested closed sets with diameter \(\le \kappa^k \mathrm{diam}(A_0)\) meet in one point. That is the only place completeness is needed, and it is not needed for the clockwork as written.

### 3.5 The tick *is* the finished tournament

Two readings, both compatible with the source sentence:

**Definitional (recommended).**  
The cascade does not take 4D time. \( K_n \) rounds are a construction in \( M_5 \) at constant \( T_5 = n \). The tick is the name of the finished construction. “All occur simultaneously on the 5D KK graph” is then literal: every round of \(\mathrm{Tour}\) shares \( T_5 \).

**Processual.**  
Each round consumes a 5D process-time \(\delta_5\), and the tick interval must satisfy

\[
K_n \, \delta_5 \;\le\; \Delta t_{\mathrm{pk}}.
\]

Because \( K_n \) is logarithmic this is an easy bound at pk resolution. Use this reading only if the clockwork is being implemented as an actual graph algorithm with a step cost.

Recommended manuscript choice: definitional. Processual is the code picture.

### 3.6 What this does to the original wording

Original: “this cascades to one single point of simultaneity for one tick of the pk-clockwork.”

Revised, still short:

> Every pair of 4D events has a simultaneity point. At each Planck–Kerr tick the finite present \(\mathcal{E}_n\) is paired by \(\mathrm{Tour}\) until one event \(\Sigma_n\) remains. That event is the universal point of simultaneity of the tick. The pairing uses the 4D axiom at every round; the uniqueness of each pair’s point uses the 5D lift.

No envelope restriction on \(\mathrm{Sim}\). The envelope is only the clock’s present.

---

## 4. \( t_G \): time for gravity to propagate between domains

### 4.1 The correction

\( t_G \) is not a generic conformal-average coordinate. It is the **travel time of gravity from one domain to another.**

Intra-domain gravity is ordinary and is *not* \( t_G \):

\[
t_G^{\mathrm{intra}}(e,e')
\;=\;
\frac{d_L(e,e')}{c}
\qquad
(e,e'\in M_i).
\]

That delay stays. Light cones inside \( M_i \) are untouched.

Inter-domain gravity cannot use those light cones. The domains are co-located on \(\mathcal{S}\) but causally separated as 4-manifolds. A 4D graviton leaving \( M_i \) does not arrive in \( M_j \). The only available path is the 5D path \(\gamma_{ij}\) through the KK graph.

### 4.2 Evaluation on a layer

Take two events of the same tick, already consolidated by \(\mathrm{Tour}\) so that both participate in \(\Sigma_n\), and connect them through the compact fibre:

\[
\gamma_{ij}
\;\subset\;
L_n
\;=\;
\Sigma_n \times S^1_{\mathrm{KK}}.
\]

On \( L_n \), \( T_5 \equiv n \), so

\[
t_G(e^{(i)}, e^{(j)})
\;=\;
\int_{\gamma_{ij}} dT_5
\;=\;
0.
\]

That is the source parenthetical: inter-domain leaks (here, gravitational influence) are transmitted at \( t_G = 0 \).

Gravity between domains does not “travel fast.” It travels on a path along which the clock that measures gravitational delay does not increment. The delay is zero because the path is confined to one layer, not because \( c = \infty \).

### 4.3 Kernel

\[
K_{ij}^{G}(e^{(j)}, e^{(i)})
\;=\;
\Phi_{ij}(\Sigma_n, \theta)\,
\delta\bigl( t_G(e^{(i)}, e^{(j)}) \bigr)\,
\delta_{T_5}(e^{(i)}, e^{(j)})\,
\rho\bigl( d_{\mathcal{S}}(e^{(i)}, e^{(j)}) \bigr).
\]

The first delta is now literally “zero inter-domain gravity travel time.” The second delta keeps the transmission inside one tick. The form factor \(\rho\) keeps it on co-located attachments.

A 4D observer in domain \( j \) does not see a superluminal 4D wave. They see an additional gravitational source that is already present at the tick, with no inter-domain wait. Intra-domain response after that source appears is still causal in \( g_j \).

### 4.4 Why the UPS is required for \( t_G = 0 \)

If there is no unique \(\Sigma_n\), there is no unique layer \( L_n \), and “the path stays at constant \( T_5 \)” is not a statement. Many candidate 5D paths between \( e^{(i)} \) and \( e^{(j)} \) would change \( T_5 \), and those paths would carry a nonzero \( t_G \). The tournament’s job, from the gravity side, is to pick the unique meeting point whose compact fibre is the zero-delay channel.

So:

- \(\mathrm{Sim}\) on all 4D pairs = the pairing law;
- \(\mathrm{Tour}\) on one tick = the consolidation;
- \(\Sigma_n \times S^1_{\mathrm{KK}} = L_n\) = the zero-\( t_G \) channel;
- \( t_G = 0 \) = gravity between domains has no travel time on that channel.

### 4.5 Contrast table

| Channel | Path | Clock that measures delay | Delay |
|---|---|---|---|
| Intra-domain gravity / light | 4D geodesic in \( M_i \) | \( \tau_i \) or \( t_i \) | \( d_L/c > 0 \) (generic) |
| Inter-domain gravity via a 5D path that climbs the cylinder | path with \( \Delta T_5 \neq 0 \) | \( T_5 \) | \( t_G = \Delta T_5 \neq 0 \) (forbidden by the kernel) |
| Inter-domain gravity via \( L_n \) | path in \( \Sigma_n \times S^1_{\mathrm{KK}} \) | \( T_5 \) | \( t_G = 0 \) |

The kernel’s \(\delta(t_G)\) *selects the third row*. The first row is ordinary GR inside a domain. The second row is a leak that would mix ticks; it is switched off.

---

## 5. Assembled statement (revision)

**Universal point of simultaneity.**  
Between every two events of the six 4D domains there is a simultaneity point, and between every two simultaneity points there is a simultaneity point. Uniqueness of each point is supplied by the 5D KK lift, which is part of the standing context. At each tick \( n \) of the Planck–Kerr clockwork the finite present \(\mathcal{E}_n\) is consolidated by the tournament map \(\mathrm{Tour}\) in \( \lceil \log_2 \#\mathcal{E}_n \rceil \) pairings, leaving a single event \(\Sigma_n\). All pairings of that tournament share the 5D graph time \( T_5 = n \). The product \( L_n = \Sigma_n \times S^1_{\mathrm{KK}} \) is the next layer of the KK cylinder. Inter-domain gravity travels in \( L_n \), so the time gravity takes to propagate between domains is \( t_G = 0 \). Intra-domain gravity is unchanged and still propagates at \( c \).

**One line.**  
Any two 4D events have a simultaneity point; the pk-clock pairs those points down to one UPS per tick; that UPS times the compact circle is the layer on which gravity crosses domains with no travel time.

---

## 6. Edge cases for the tournament

1. **Odd population.** The leftover event is carried forward unchanged. It is not a second UPS; it is paired on the next round.
2. **Ordering rule.** \(\mathrm{Tour}\) is not unique until the present is ordered. Freeze one rule. Changing the order can change \(\Sigma_n\) if \(\mathrm{Sim}\) is not associative. If associativity of \(\mathrm{Sim}\) is later proved, the order drops out. Until then, the rule is part of the definition.
3. **Associativity (open).** \(\mathrm{Sim}(\mathrm{Sim}(a,b),c) \stackrel{?}{=} \mathrm{Sim}(a,\mathrm{Sim}(b,c))\). If true, every binary tree on \(\mathcal{E}_n\) has the same root and the tournament is only a convenience. If false, the tournament *is* the definition of \(\Sigma_n\) and must be kept. This is the next algebraic question, not assumed here.
4. **Events that arrive mid-tick.** Assign them to \(\mathcal{E}_{n+1}\). Do not reopen a finished tournament.
5. **Empty present.** No tick. The clock does not emit a layer.
6. **One event present.** \( K_n = 0 \), \(\Sigma_n\) is that event. Idempotence covers it.

---

## 7. What to compute next

No engine run this session. The contraction question is now a finite algorithm:

1. On a 6-sheet graph, implement \(\mathrm{Tour}\) with a frozen ordering, print \( N_n \), \( K_n \), and \(\Sigma_n\).
2. Shuffle the ordering and measure how often \(\Sigma_n\) moves. That is the associativity test.
3. Connect two marked vertices on different sheets *only* through \( L_n \) and confirm the path has \(\Delta T_5 = 0\). That is the \( t_G = 0 \) test.
4. Connect the same vertices by a path that increments \( T_5\) and confirm the kernel weight is zero. Negative control.

---

## 8. Session inventory

Standing corrections from the user, applied:

- Pairwise 4D existence is contextual axiom, not a restriction to an envelope.
- Spelling: simultaneity.
- Item 3 worked: naive \( F_{\mathrm{all}} \) does not contract; \(\mathrm{Tour}\) does, in \( \lceil \log_2 N_n \rceil \) rounds, one tick.
- All 4D pairs participate in \(\mathrm{Sim}\); consolidation is per tick via \(\mathrm{Tour}\).
- \( t_G \) = inter-domain gravity travel time; \( t_G = 0 \) on \( L_n \).

Local + project copies:

- Workspace: `/home/workdir/artifacts/Personal Files/2026-09-16_UPS_contraction_and_tG.md`
- Intended GitHub path: `Personal Files/2026-09-16_UPS_contraction_and_tG.md` on `George-Jumble/TauSuperblock` (`main`)

Parent morning note remains at  
`/home/workdir/artifacts/Personal Files/2026-09-16_universal_point_of_simultaneity_review.md`.

---

*End of session note — 2026-09-16 UPS contraction and \( t_G \).*
