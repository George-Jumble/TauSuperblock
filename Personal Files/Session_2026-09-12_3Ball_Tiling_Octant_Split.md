# Session 2026-09-12 — Fixed 3-ball tiling (octant split)

**Decision:** Daughter number \(q\) is not free. Working tiling is the **orthant / octant decomposition of \(\mathbb{R}^3\)**.

**Status:** Geometry locked. \(\tau\) still not derived.

**Depends on:** `Session_2026-09-12_Envelope_Expansion_Tau_Circle_Mirron_Proliferation.md`

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(\mathcal{B}(t,y)\) | Bound 3-ball (envelope interior) centred at comoving site \(y\) on slice \(t\) |
| \(E(t,y)\) | Envelope 2-sphere \(\partial\mathcal{B}\) |
| \(R\) | Physical radius of a parent ball at the instant it hits the cap |
| \(\ell_{\mathrm{cap}}\) | Exhaustion cap; at split, \(R=\ell_{\mathrm{cap}}\) |
| \(q\) | Number of daughter balls |
| \(r\) | Physical radius of each daughter immediately after split |
| \(\rho\) | Ratio \(r/R\) |
| \(f\) | Volume fill fraction \(q\rho^3\) |
| \(\mathbf{n}_k\) | Unit vector toward the \(k\)-th octant diagonal |
| \(y_k\) | Comoving centre of daughter \(k\) |
| \(a(t)\) | Prime scale factor |
| \(N_\tau\) | Number of bound Tau fibers |
| \(N_{\mathrm{M}}\) | Number of PK-Mirrons |
| \(\mu\) | Mirrons per fiber (working value \(1\)) |
| \(g\) | Generation index (number of completed global splits from the Past pack) |
| \(O_k\) | \(k\)-th closed octant of \(\mathbb{R}^3\) |
| \(\Phi_7\) | Seventh-phase evaluation map |
| \(\mathcal{C}_{\mathcal{PF}}\) | Atemporal Past–Future circle |

---

## 2. Why the tiling was free, and what fixes it

A 3-ball cannot be filled by smaller equal 3-balls without gaps. Volume ratio \((R/r)^3\) is only an upper bound. So \(q\) had to be chosen by a **configuration**, not by volume.

Two regular candidates:

| Configuration | \(q\) | Why it is geometric |
|---------------|-------|---------------------|
| Regular tetrahedron | 4 | Minimal isotropic point set in \(\mathbb{R}^3\) |
| Orthants of \(\mathbb{R}^3\) | 8 | Unique decomposition of the envelope’s 3-space by three orthogonal planes through the centre |

**Working lock: octants, \(q=8\).**  
Reason: the envelope lives in Prime 3-space. That 3-space has a unique (up to rotation) splitting into eight orthants. The number 8 is \(\dim\mathbb{O}\) and the clockwork tick count, obtained here from \(\mathbb{R}^3\) orthants, not from inserting \(7\,h^{-1}\mathrm{Mpc}\).

Tetrahedral \(q=4\) remains the minimal alternative. It is not the working rule.

---

## 3. Octant split

Parent at the cap:

\[
\mathcal{B}_{\mathrm{parent}}
=
\bigl\{\mathbf{x}:\ |\mathbf{x}-\mathbf{c}|\le R\bigr\},
\qquad
R=\ell_{\mathrm{cap}}.
\]

**Key:** \(\mathbf{c}\) = physical centre at split; \(R\) = parent radius; \(\ell_{\mathrm{cap}}\) = cap.

Three mutually orthogonal planes through \(\mathbf{c}\) cut \(\mathbb{R}^3\) into eight closed octants \(O_k\), \(k=1,\ldots,8\). Each daughter is the **largest ball contained in** \(\mathcal{B}_{\mathrm{parent}}\cap O_k\).

Place the daughter centre on the octant space diagonal and let it touch the three coordinate planes of that octant. If those planes are the coordinate planes in a frame at \(\mathbf{c}\), the centre sits at \((c,c,c)\) up to signs, with daughter radius equal to \(c\) (distance to each plane).

Stay inside the parent:

\[
\sqrt{3}\,c + c \le R
\qquad\Rightarrow\qquad
c\le \frac{R}{1+\sqrt{3}}.
\]

**Key:** \(\sqrt{3}\,c\) = distance from parent centre to daughter centre; \(c\) = daughter radius.

Equality is the largest daughter:

\[
r
=
\frac{R}{1+\sqrt{3}}
=
\frac{\sqrt{3}-1}{2}\,R,
\qquad
\rho
=
\frac{r}{R}
=
\frac{\sqrt{3}-1}{2}.
\]

**Key:** \(r\) = daughter physical radius at birth; \(\rho\) = ratio.  
Numerically \(\rho\approx 0.366025\).

The eight centres (physical, at the split instant):

\[
\mathbf{c}_k
=
\mathbf{c}
+
r\,\mathbf{n}_k,
\qquad
\mathbf{n}_k
=
\frac{1}{\sqrt{3}}
\bigl(\varepsilon_1,\varepsilon_2,\varepsilon_3\bigr),
\quad
\varepsilon_i=\pm 1.
\]

**Key:** \(\mathbf{n}_k\) = unit diagonal of octant \(k\); eight sign triples.

Comoving centres after the split (Prime slice, scale factor \(a(t_*)\)):

\[
y_k
=
y
+
\frac{r}{a(t_*)}\,\mathbf{n}_k.
\]

**Key:** \(y\) = parent comoving centre; \(t_*\) = split time; \(y_k\) = daughter comoving centre, thereafter fixed.

---

## 4. Fill fraction and the web

Daughter balls do not fill the parent.

\[
f
=
q\rho^3
=
8\left(\frac{\sqrt{3}-1}{2}\right)^3
=
\frac{8}{(1+\sqrt{3})^3}
=
\frac{8}{10+6\sqrt{3}}.
\]

**Key:** \(f\) = fraction of parent volume occupied by the eight daughter balls.  
Numerically \(f\approx 0.3923\).

The complementary fraction \(1-f\approx 0.6077\) is interstitial. In this tiling that remainder is the **web among nodes** (filaments / voids as unbound 3+1 regions between bound envelopes). It is a geometric leftover of packing balls in a ball, not an extra field.

---

## 5. Locked process

At each cap event, one parent \(\to\) eight daughters:

\[
q=8,
\qquad
r=\frac{\sqrt{3}-1}{2}\,\ell_{\mathrm{cap}}.
\]

**Key:** same as above, with \(R=\ell_{\mathrm{cap}}\) at the instant of split.

After the split, each daughter comoves and grows as

\[
r_{\mathrm{phys}}(t,y_k)
=
a(t)\,\chi_E(y_k)
\]

**Key:** \(\chi_E(y_k)=r/a(t_*)\) immediately after split, then fixed.

until \(r_{\mathrm{phys}}=\ell_{\mathrm{cap}}\) again, when that daughter octant-splits.

If the original Past pack splits in global generations (all cells of a generation hit the cap together),

\[
N_\tau^{(g)}
=
8^g,
\qquad
N_{\mathrm{M}}^{(g)}
=
\mu\,8^g
=
8^g
\quad(\mu=1).
\]

**Key:** \(g=0\) at Absolute Past (\(N=1\)); \(g\) = number of completed generations.

This replaces the earlier floor-of-volume formula as the **microscopic** write rule. The volume floor remains an **upper bound**:

\[
N_\tau(t)
\le
\left\lfloor
\left(
\frac{R_{\mathrm{avail}}(t)}{\ell_{\mathrm{cap}}}
\right)^3
\right\rfloor,
\qquad
R_{\mathrm{avail}}
=
\min\bigl(R_{\mathrm{EH}}(t),\,a(t)\chi_{\mathrm{patch}}\bigr).
\]

**Key:** \(R_{\mathrm{EH}}\) = event-horizon radius; \(\chi_{\mathrm{patch}}\) = original packed comoving radius.  
Because \(f<1\), octant generations undershoot the volume bound. That is consistent: bound balls do not tile space.

---

## 6. What was rejected

| Choice | Why not locked |
|--------|----------------|
| \(q=6\) from six domains | Inserts matter-sector counting into 3-geometry |
| \(q=7\) from Fano / \(1/7\) | Inserts Tav combinatorics into the envelope |
| Binary split \(q=2\) | Picks an axis; not isotropic |
| Kissing \(1+12=13\) | Packs around a surviving centre; parent would keep a core ball and never fully split |
| Volume-only \(q=(R/r)^3\) | Not a packing; \(q\) not integer without extra rules |

Tetrahedral \(q=4\) with \(\rho=1/(1+\sqrt{6}/2)\approx 0.4495\), fill \(\approx 0.363\), is the documented alternative if isotropy-plus-minimality is preferred later. It is not the working rule.

---

## 7. Tie to the atemporal cylinder

Each daughter centre is a new evaluation point of \(\Phi_7:\mathcal{C}_{\mathcal{PF}}\to S^1_\tau(y_k)\). The cylinder does not multiply. The octant frame at split is a Prime 3-space frame; it is not an octonion multiplication by itself. Compatibility with 8-phase clockwork is only the **count** \(q=8=\dim\mathbb{O}\). Identifying the eight octants with eight clockwork letters is an extra map, not part of this lock.

---

## 8. Status

| Item | Status |
|------|--------|
| \(q=8\) octant split | locked |
| \(r=(\sqrt{3}-1)\ell_{\mathrm{cap}}/2\) | locked |
| Fill \(f=8/(10+6\sqrt{3})\approx 0.392\) | locked |
| \(N_\tau=8^g\) in generational splitting | locked under synchronous cap |
| \(\ell_{\mathrm{cap}}=\tau\) | still not derived |
| Octant \(\leftrightarrow\) phase letter | not claimed |

---

*Saved 2026-09-12 to Tau-Superblock_Universe/Personal_Files.*
