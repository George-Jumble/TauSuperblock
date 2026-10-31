# Session 2026-09-14 — What is needed for a unique finite \(t_{00}\)

**Why the last evaluation failed:** pointwise \(n(\pi_\gamma)\) is \(\infty\) on the vacuum axis and a function of angle off-axis. The sky integral diverges as \(\varepsilon^{-6}\).

---

## 1. Complete symbol key

| Symbol | Meaning |
|--------|---------|
| \(n(\pi)\) | Pointwise invariant \(\lvert\pi\rvert^8/\lvert\pi_{0'}+\pi_{1'}\rvert^8\) |
| \(\varepsilon\) | Cap around the pole |
| \(\theta_{\mathrm{p}}\) | Sky angle from the pole |
| \(H^1(\mathbb{PT}^+,\mathcal{O}(-4))\) | Twistor cohomology of the photon |
| \(\langle f,f\rangle\) | Pairing on that class (not pointwise \(\lvert f\rvert^2\)) |
| \(\varphi_{A'B'}(x)\) | Penrose field at a generic event |

---

## 2. Three ways a unique finite number can appear

**A. Change the object.**  
Stop using pointwise \(n(\pi)\). Use a pairing on the **cohomology class** of \(f_+\), or the residue that already defines \(\varphi_{A'B'}(x)\). Those are built to be finite at a generic \(x\). Then \(t_{00}(x)=U^{-4}T_{00}[\varphi(x)]\).  
Still need: show this is **the same at every \(x\)** between \(\alpha_{\mathrm{res}}\) and \(\Omega_{\mathrm{res}}\), or you have a fluid, not \(\Lambda\).

**B. Change the locus.**  
Keep \(n(\pi_\gamma)\) but add a rule, from \(W\) only, that picks **one** \(\pi_\gamma\).  
Examples that would count: “the antipode of \(v_+\)” (\(N=1/16\)), or “the \(\pm i\) domain axes” (\(N\) computed at those six points and averaged).  
That is unique. It is **not** \(\rho_\Lambda\): \(N=\mathcal{O}(1)\) still leaves \(T_{00}\sim U^4\).

**C. Change the cutoff into an output.**  
Keep the sky integral and derive \(\varepsilon\) from named algebra (not from \(\rho_\Lambda\), not from \(86\,\mu\mathrm{m}\)). Then \(I(\varepsilon)\) is unique.  
No such \(\varepsilon\) is in \(\mathrm{spec}(W)\) or in \(\{\mathcal{P},x,\mathcal{F}\}\) today.

---

## 3. What will not work

- Taking \(\varepsilon\to 0\). There is no limit.  
- Leaving \(\theta_{\mathrm{p}}\) free. \(N\) then is a function, not a number.  
- Setting \(\varepsilon\) or \(\theta_{\mathrm{p}}\) so that \(U^4 I=5.71\times 10^{-10}\,\mathrm{J\,m^{-3}}\). That is a fit.

---

## 4. Recommended next

Do **A** at a generic \(x\): compute \(\varphi_{A'B'}[f_+]\) from the contour (already finite off the Robinson ray), then \(T_{00}(x)\). Report whether it is constant in \(x\). If it is not constant, \(\rho_\Lambda\) is not this pointwise Maxwell energy.

Do **B** only as a bookkeeping convention (antipode or six \(\pm i\) axes), and do not call \(\mathcal{O}(1)\) a derivation of dark energy.

---

*Saved 2026-09-14 to Tau-Superblock_Universe/Personal_Files.*
