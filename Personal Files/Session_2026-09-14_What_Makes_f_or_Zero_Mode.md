# Session 2026-09-14 — What is needed to write \(f(Z)\) or the \(\Phi_8\circ\Phi_7\) zero mode

**Why this is first:** \(T_{00}\) acts on a field. No field, no density.

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(Z^\alpha=(\omega^A,\pi_{A'})\) | Twistor, \(\alpha=0,1,2,3\) |
| \(\mathbb{PT}\) | Projective twistor space \(\mathbb{CP}^3\) |
| \(f(Z)\) | Holomorphic twistor function (or cohomology class) |
| \(n\) | Homogeneity \(f(\lambda Z)=\lambda^n f(Z)\) |
| \(s\) | Helicity of the spacetime field |
| \(a=1,\ldots,6\) | Superblock domain index |
| \(\psi_a\) | Restriction of \(f\) to domain \(a\) |
| \(\Phi_7,\Phi_8\) | Scrape and refresh, as operators on the twistor space |
| \(\ker(\Phi_8\circ\Phi_7-\lambda I)\) | Zero / eigenmodes of one refresh-scrape |
| \(\mathcal{R}_x\cong\mathbb{CP}^1\) | Celestial sphere at \(x\) (line in \(\mathbb{PT}\)) |

---

## 2. Two routes (pick one and finish it)

**Route A — write \(f\).**  
A twistor function is specified by:

1. The space: \(\mathbb{PT}\) (or \(\mathbb{PT}^+\) / primed dual).  
2. Homogeneity \(n\). For a photon, standard Penrose is \(n=-4\) or \(n=0\) depending on whether one uses \(f\) or the dual potential; **state which**. Helicity \(s=\pm 1\) must match.  
3. Domain copies: one \(f\) on \(\mathbb{PT}\) with six evaluations, or six functions \(f_a\). How a line in \(\mathbb{PT}\) maps to domain \(D_a\) must be named (six \(\mathbb{CP}^1\)s in one \(\mathbb{CP}^3\), or six charts).  
4. Reality / positive-frequency conditions so \(T_{00}\) is a real density, not a contour accident.  
5. What “completed / unbound” means as a support condition: poles only on generators that reach \(\mathscr{I}\), not on stopped (bound) lines.

Until (1)–(5) are written, “twistor waveform” is a label.

**Route B — write the zero mode of \(\Phi_8\circ\Phi_7\).**  
Then you do not invent \(f\) first. You invent the operators:

1. Realize \(\mathbb{O}\) (or \(\mathbb{R}^8\)) as the fiber of phases.  
2. Give \(\Phi_7\) and \(\Phi_8\) as explicit \(8\times 8\) real matrices (or left multiplications \(L_u\) by named unit octonions).  
3. Form \(W=\Phi_8\Phi_7\).  
4. Compute \(\ker(W-\lambda I)\) for the eigenvalue that is the identity tick (\(\lambda=1\) or \(\lambda=-1\) if the word is an inversion).  
5. Interpret that 8-vector as coefficients of a mode on \(\mathbb{PT}\) (a map \(\mathbb{R}^8\to\) functions on \(\mathbb{CP}^1\), stated). That mode *is* \(f\) for the vacuum.

Route B is the one that stays inside clockwork. Route A is the one that stays inside the photon paper. They must meet: the kernel vector of \(W\) should be the same object as the lowest \(f\).

---

## 3. Concrete missing objects (checklist)

| Item | Have now | Need |
|------|----------|------|
| \(\mathbb{PT}\) incidence \(\omega^A=ix^{AA'}\pi_{A'}\) | standard | keep |
| Homogeneity / helicity of unbound light | not fixed in this thread | one pair \((n,s)\) |
| Six-domain embedding in \(\mathbb{PT}\) | verbal “supersphere” | a map \(a\mapsto\) line or chart |
| \(\Phi_7\) as \(8\times 8\) | name only | matrix or \(L_u\) |
| \(\Phi_8\) as \(8\times 8\) | name only | matrix or \(L_u\) |
| \(W=\Phi_8\Phi_7\) spectrum | no | eigenvalues + kernel |
| Map kernel \(\to f(Z)\) | no | stated isomorphism |
| Support = completed generators only | verbal | contour / pole rule |

---

## 4. What you can do next without new physics

Start Route B, because it is finite:

- Choose a basis \(e_0,\ldots,e_7\) of \(\mathbb{O}\).  
- Set \(\Phi_8=L_{e_7}\) or another named unit (refresh).  
- Set \(\Phi_7\) to the letter that implements the scrape (a \(G_2\) element or a reflection through the mirror unit).  
- Diagonalize \(W\).  
- The invariant subspace is the candidate vacuum mode.

Do not tune the matrices so that \(\langle T_{00}\rangle\) equals \(5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\). If the kernel is unique (up to scale), \(f\) is unique (up to scale) and \(U\) still has to come from PK geometry later.

---

## 5. Done when

You can write either

\[
f(Z)
=
\text{(formula in }Z^\alpha\text{, homogeneity }n\text{, index }a\text{)}
\]

or

\[
W v= \lambda v,
\qquad
f
=
\iota(v),
\]

**Key:** \(W=\Phi_8\Phi_7\); \(v\in\mathbb{R}^8\); \(\iota\) = named map into twistor functions.

and a stranger can recompute \(v\) from the matrices alone.

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
