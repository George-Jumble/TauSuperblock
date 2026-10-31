# Session 2026-09-14 — What is needed to complete the \(\rho_\Lambda\) derivation

**Slot already written:**
\[
\rho_\Lambda \stackrel{?}{=} V_\infty = \bigl\langle T_{00}\bigl[f|_{\mathscr{I}}\bigr]\bigr\rangle.
\]

**Status:** slot only. Below is the work that would make the last line a number.

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(f(Z)\) | Unbound twistor waveform |
| \(Z^\alpha=(\omega^A,\pi_{A'})\) | Twistor |
| \(\mathscr{I}\) | Conformal infinity (completed generators) |
| \(T_{00}\) | Energy density of that waveform |
| \(\langle\cdot\rangle\) | Average over the six domains on \(\mathbb{S}_{\mathrm{SB}}\) |
| \(\Phi_7,\Phi_8\) | Scrape and refresh letters |
| \(V_\infty\) | Zero-mode vacuum term |
| \(w\) | Equation of state |
| \(U\) | Single dimensionful seed (if any) |

---

## 2. Must have (in order)

**1. An explicit \(f\), or an explicit zero mode.**  
Either a twistor function / cohomology class \(f(Z)\) with stated homogeneity and domain indices \(a=1,\ldots,6\), or the constant mode of the word \(\Phi_8\circ\Phi_7\) acting on that space. Until one of those is a formula, \(T_{00}\) has nothing to eat.

**2. A rule for \(T_{00}[f]\).**  
How a completed (null, \(L=0\)) waveform sources energy density in Prime 3+1. Not \(\hbar c/\tau^4\). Not \(\hbar c/\ell_{\mathrm{Pl}}^4\). A bilinear in \(f\) (or in the zero mode) with stated index structure. If the only available scale is a seed \(U\), write

\[
T_{00}=U^4\,t_{00}[f],
\]

**Key:** \(t_{00}\) dimensionless; \(U\) named from PK geometry only, not from \(\rho_\Lambda\), \(\tau\), or \(313.1\,\mathrm{MeV}\).

**3. The average \(\langle\cdot\rangle\).**  
Say whether the six domains share one \(f\) or carry \(\psi_a\) with \(V_{\mathrm{orb}}^{(a)}\). The average must be defined on \(\mathbb{S}_{\mathrm{SB}}\) so that Prime sees one \(\rho_\Lambda\).

**4. Time-independence on slices.**  
Show \(\partial_t\langle T_{00}\rangle=0\) (or \(\propto a^{-0}\)) after \(\alpha_{\mathrm{res}}\). That is \(w=-1\). If it runs with \(a(t)\), you have derived a different fluid, not \(\Lambda\).

**5. Empty right-hand side until the last line.**  
No \(\rho_\Lambda\), no \(86\,\mu\mathrm{m}\), no \(\tau\), no \(313.1\,\mathrm{MeV}\) inside \(t_{00}\) or \(U\). Compare to \(5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\) *after* the evaluation.

---

## 3. Prerequisite that unblocks (1)

\(\Phi_7\) (and \(\Phi_8\)) as explicit \(8\times 8\) real matrices, or as named left multiplications on \(\mathbb{O}\). Without that, “zero mode of the refresh” is a phrase.

---

## 4. Not required for this derivation

- Octant \(q=8\) or Apollonian \(\delta\)  
- Deriving \(\tau\)  
- Clay / OS reconstruction  
- A glueball occupancy  

Those are other jobs. Mixing them back in is how \(A/\tau^4\) returned.

---

## 5. Done when

You can write one line

\[
\rho_\Lambda^{\mathrm{(TSB)}}
=
U^4\,\langle t_{00}[f|_{\mathscr{I}}]\rangle
=
\text{(a number in }\mathrm{J\,m^{-3}}\text{)}
\]

**Key:** every symbol on the middle expression already defined in §§2–3, and the number is not copied from Planck cosmology.

Then, and only then, compare to \(5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\). Agreement is a test. Disagreement is also a test. Either is a completed derivation.

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
