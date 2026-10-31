# Session 2026-09-14 — Evaluation of \(N[f_+|_{\gamma_{\mathcal{P}x\mathcal{F}}}]\)

**Done as a calculation.** Result: the three-point restriction does **not** produce a unique finite \(t_{00}\).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(f_+(\pi)\propto(\pi_{0'}+\pi_{1'})^{-4}\) | Locked vacuum mode |
| \(\pi_{A'}\) | Primed spinor (point on \(\mathcal{R}_x\)) |
| \(n(\pi)\) | Invariant density \(\lvert\pi\rvert^{8}/\lvert\pi_{0'}+\pi_{1'}\rvert^{8}\) |
| \(\gamma_{\mathcal{P}x\mathcal{F}}\) | One completed ray through \(x\) |
| \(\pi_\gamma\) | Celestial point of that ray at \(x\) |
| \(N[\gamma]\) | \(n(\pi_\gamma)\) |
| \(\varepsilon\) | Angular cutoff around the pole |
| \(\theta_{\mathrm{p}}\) | Angle on the sky from the pole of \(f_+\) |

Pole of \(f_+\) is \(\pi_{0'}+\pi_{1'}=0\) (Hopf: \(\theta=\pi/2\), \(\phi=\pi\)).

---

## 2. Invariant integrand

\(f_+\) has weight \(-4\). The scalar density on \(\mathbb{CP}^1\) is

\[
n(\pi)
=
\frac{\bigl(\lvert\pi_{0'}\rvert^2+\lvert\pi_{1'}\rvert^2\bigr)^4}
{\lvert\pi_{0'}+\pi_{1'}\rvert^8}.
\]

**Key:** \(n(\lambda\pi)=n(\pi)\). This is \(N\) evaluated on a direction.

On a single completed chain \(\gamma\), there is one celestial point \(\pi_\gamma\) at \(x\):

\[
N\bigl[f_+\big|_{\gamma_{\mathcal{P}x\mathcal{F}}}\bigr]
=
n(\pi_\gamma).
\]

**Key:** no extra integral along the affine parameter; the ray is one point on \(\mathcal{R}_x\).

---

## 3. Values on a ray (computed)

| \(\theta_{\mathrm{p}}\) from the pole | \(n(\pi_\gamma)\) |
|--------------------------------------|-------------------|
| \(0^\circ\) (chain = vacuum axis) | \(\infty\) |
| \(0.5^\circ\) | \(\sim 4.8\times 10^{17}\) |
| \(10^\circ\) | \(\sim 1.9\times 10^{7}\) |
| \(90^\circ\) | \(1\) |
| \(180^\circ\) (antipode) | \(1/16=0.0625\) |

If \(\mathcal{P}\)–\(\mathcal{F}\) is identified with the \(v_+\) axis (\(e_0+e_7\)), the completed generator sits **on the pole** and \(N=\infty\).

If one adopts a convention “use the antipodal completed ray,” \(N=1/16\). That is a convention. \(t_{00}=1/16\) still gives \(U^4/16\), the Planck vacuum divided by 16, not \(\rho_\Lambda\).

---

## 4. Full-sky integral (all chains through \(x\))

\[
I(\varepsilon)
=
\int_{\lvert\pi_{0'}+\pi_{1'}\rvert\ge\varepsilon}
n(\pi)\,d\mu,
\qquad
d\mu=\frac{\sin\theta\,d\theta\,d\phi}{4\pi}.
\]

**Key:** \(\varepsilon\) cuts out the pole.

Computed:

| \(\varepsilon\) | \(I(\varepsilon)\) |
|-----------------|---------------------|
| \(0.50\) | \(\sim 10\) |
| \(0.10\) | \(\sim 1.7\times 10^{5}\) |
| \(0.02\) | \(\sim 2.7\times 10^{9}\) |
| \(0.01\) | \(\sim 3.0\times 10^{11}\) |

\(I(\varepsilon)\) runs as \(\sim\varepsilon^{-6}\) and diverges as \(\varepsilon\to 0\). There is no finite \(\varepsilon\to 0\) limit. A unique number from the sky integral requires a preferred \(\varepsilon\). That \(\varepsilon\) is a new scale. It is not in \(W\) or in \(\{\mathcal{P},x,\mathcal{F}\}\) alone.

---

## 5. Verdict

The remaining calculation **was performed**. It does not close \(\rho_\Lambda\).

- One aligned chain: \(N=\infty\).  
- One misaligned chain: \(N=n(\theta_{\mathrm{p}})\), angle-dependent, not unique.  
- All chains: divergent unless an extra cutoff \(\varepsilon\) is supplied.

The three-point restriction names *which* ray. It does not tame the pole. Finite unique \(t_{00}\) still needs a regulator that is not \(\rho_\Lambda\) and not an ad hoc \(\varepsilon\).

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
