# Session 2026-09-30d — Center of mass (COM), explained

**Framework**: SBT as amended 2026-09-19; live TSB locks. Mirron, never soliton.  
**Follows**: `Session_2026-09-30_Macroscopic_Superposition_Implies_for_SBT.md`.  
**Charge**: Explain COM — what it is, what Pedalino superposed, why internals can stay bound, what SBT must say about that coordinate.

This file: `Tau-Superblock-Universe/Personal Files/Session_2026-09-30_COM_Explained.md`  
Mirrors: `Personal Files/`, `Personal_Files/`.

---

## 0. One sentence

The center of mass is the single point that moves as if the whole cluster’s mass sat there; Pedalino put **that point’s position** into a superposition, not the metallic bonds inside the cluster.

---

## 1. Complete key

| Symbol | Meaning |
|--------|---------|
| COM | Center of mass |
| \(N\) | Number of atoms in the cluster (\(\gtrsim 7000\)) |
| \(m_a, \mathbf{r}_a\) | Mass and lab position of atom \(a=1,\ldots,N\) |
| \(m=\sum_a m_a\) | Total mass |
| \(\mathbf{R}\) | COM position vector |
| \(\mathbf{r}'_a=\mathbf{r}_a-\mathbf{R}\) | Position of atom \(a\) relative to the COM (internal coordinate) |
| \(\mathbf{P}=m\dot{\mathbf{R}}\) | Total momentum; conjugate to \(\mathbf{R}\) |
| \(\psi_{\mathrm{COM}}(\mathbf{R},t)\) | Wavefunction of the COM coordinate |
| \(\Psi(\mathbf{r}_1,\ldots,\mathbf{r}_N)\) | Full many-body wavefunction |
| \(\lambda_{\mathrm{dB}}=h/(m v)\) | de Broglie wavelength of the COM, not of an electron |
| bound coordinate | Rebound of that degree of freedom stopped at Present; residual \(L\) |
| unbound coordinate | That degree of freedom completes Past \(\leftrightarrow\) Future; no residual \(L\) on it |
| envelope | A stopped-bounce cell at one generation (atomic, metallic, colour, …) |

---

## 2. What COM is, classically

For \(N\) pieces with masses \(m_a\) at positions \(\mathbf{r}_a\),

\[
\mathbf{R}
=
\frac{1}{m}\sum_{a=1}^{N} m_a\,\mathbf{r}_a,
\qquad
m=\sum_{a=1}^{N}m_a.
\]

**Key.** \(\mathbf{R}\): the unique point that carries the total mass for the purpose of *translation*. If every atom is shifted by the same vector \(\mathbf{d}\), then \(\mathbf{R}\mapsto\mathbf{R}+\mathbf{d}\) and every internal vector \(\mathbf{r}'_a\) is unchanged.

Two facts follow and both matter for SBT:

1. **Translation separates.** The kinetic energy splits exactly:

\[
T
=
\frac{1}{2}m\dot{\mathbf{R}}^{2}
+
T_{\mathrm{int}}(\{\mathbf{r}'_a,\dot{\mathbf{r}}'_a\}).
\]

**Key.** \(T\): total kinetic energy. First term: COM motion, as if one particle of mass \(m\). \(T_{\mathrm{int}}\): vibrations, rotations, electronic motion *around* \(\mathbf{R}\). No cross term if the internals are measured from \(\mathbf{R}\).

2. **Forces that are purely internal cancel from the COM equation.** By Newton’s third law (or by momentum conservation in an isolated system),

\[
m\ddot{\mathbf{R}}
=
\mathbf{F}_{\mathrm{ext}}.
\]

**Key.** \(\mathbf{F}_{\mathrm{ext}}\): sum of forces from *outside* the cluster (gravity, electric fields of the gratings, residual gas kicks). Na–Na metallic bonds, Coulomb forces among ions and electrons, colour-dressing inside nuclei — all of that is internal. It shapes \(T_{\mathrm{int}}\) and the bound envelopes. It does **not** accelerate \(\mathbf{R}\).

That is why a bound object can have a free packet motion. The object is glued together *internally* and still flies as one \(m\) through the lab.

---

## 3. What COM is, quantum-mechanically

The same split exists as operators. If the cluster is isolated enough,

\[
\Psi(\mathbf{r}_1,\ldots,\mathbf{r}_N)
\;\longrightarrow\;
\psi_{\mathrm{COM}}(\mathbf{R})\;\chi(\{\mathbf{r}'_a\}).
\]

**Key.** \(\Psi\): full wavefunction. \(\psi_{\mathrm{COM}}\): amplitude to find the *packet* centered at \(\mathbf{R}\). \(\chi\): internal state (electrons, phonons, metallic cohesion). The arrow is an approximation: it holds when the apparatus does not entangle internals with \(\mathbf{R}\) strongly enough to wash fringes.

Pedalino measures interference in \(\psi_{\mathrm{COM}}\). Visibility surviving means \(\chi\) stayed similar on both paths, or that path-dependent entanglement with \(\chi\) was small.

A spatial superposition of COM with separation \(d\) means: the amplitude to find the *whole packet* near \(x=0\) and the amplitude to find the *whole packet* near \(x=d\) are both nonzero, and they have a stable relative phase. Every atom is displaced with the packet. The bonds that hold atom \(a\) to atom \(b\) live in \(\chi\), which is the same description on both branches if the experiment worked.

So:

- “The cluster is in two places” = \(\psi_{\mathrm{COM}}\) has support at two packet locations.
- “The metal is still a metal” = \(\chi\) still describes a bound Na droplet on each branch.

Those two sentences do not fight.

---

## 4. What an interferometer does to COM

A Talbot–Lau interferometer is a machine that writes a phase onto \(\psi_{\mathrm{COM}}\) as a function of transverse \(\mathbf{R}\).

Rough sequence:

1. A source makes a beam of clusters, each with a fairly well-defined \(m\) and speed \(v\).
2. Grating G1 imposes a periodic amplitude/phase mask on \(\psi_{\mathrm{COM}}(x)\).
3. Free flight lets the COM wave shear. Near-field revival distance is the Talbot length

\[
L_T
=
\frac{d_g^{2}}{\lambda_{\mathrm{dB}}}
=
\frac{d_g^{2}\,m v}{h}.
\]

**Key.** \(L_T\): Talbot length. \(d_g\): grating period (\(133\,\mathrm{nm}\) in Pedalino). Larger \(m\) makes \(\lambda_{\mathrm{dB}}\) smaller and \(L_T\) longer; that is why heavy clusters need a compact near-field design rather than a far-field Young slit.

4. G2 and G3 read the revived periodic pattern. Fringes in the count rate versus G3 shift are the proof that \(\psi_{\mathrm{COM}}\) took more than one transverse history with a maintained phase.

Nothing in that sequence asks the metallic bonds to dissolve. It asks that no external record (gas collision, thermal photon, leaking electron) tags *which* transverse history \(\mathbf{R}\) took. A which-path tag on COM is entanglement of \(\psi_{\mathrm{COM}}\) with the environment; that is decoherence of COM, not “the object became bound.”

---

## 5. Bound internals, unbound COM — the SBT cut on this coordinate

Live SBT / TSB: a coordinate is bound when its rebound toward Absolute Future is stopped at Present and stores residual \(L\). It is unbound when that coordinate completes Past \(\leftrightarrow\) Future.

Apply that to the split in §2.

| Coordinate | In the Na cluster | Bound or unbound in the beam? |
|------------|-------------------|-------------------------------|
| \(\{\mathbf{r}'_a\}\), electrons, metallic cohesion | internals | **Bound.** Atoms stay a droplet. Residual \(L\) lives in those envelopes. Pedalino did not test whether those envelopes can themselves be cats. |
| \(\mathbf{R}\) | COM | **Unbound for the flight.** No external wall stopped the packet’s rebound on that coordinate. The interferometer *requires* that. |

The cluster is therefore not “a bound object” or “an unbound object.” It is a bound *body* with an unbound *packet coordinate*.

Older Dynamic Refresh language treated “the object” as one thing that is rewritten every tick. COM shows why that is the wrong grain: rewrite \(\chi\) if you must; you may not classically pin \(\mathbf{R}\) on an isolated flight, or the fringes die.

Photon analogue, same cut: the photon’s null coordinate is unbound; the bound charge that emitted it is not. COM of an isolated cluster is the massive version of the photon’s coordinate, not the massive version of the charge.

---

## 6. What COM is *not*

- Not the geometric centroid of a drawing unless all \(m_a\) are equal. It is mass-weighted.
- Not the nucleus of one atom. One Na nucleus has its own tiny COM; the cluster COM is the packet of all of them together.
- Not “consciousness,” not a microtubule, not \(\Delta_{\mathrm{Tav}}\). Those were other papers.
- Not a test of residual-\(L\) gravity. Gravity in the live frame couples to bound-sector residual \(L\). Isolated \(\mathbf{R}\) in vacuum carries almost none.
- Not two domains. The two peaks of \(\lvert\psi_{\mathrm{COM}}\rvert^{2}\) are two amplitudes for one coordinate in one lab domain, not a hop \(D_a\to D_b\).

A useful contrast:

\[
\underbrace{\mathbf{R}_{\mathrm{left}}\ \mathrm{and}\ \mathbf{R}_{\mathrm{right}}}_{\text{two supports of }\psi_{\mathrm{COM}}}
\quad\neq\quad
\underbrace{D_a\to D_b}_{\text{domain-cross, pays }E_{\times}=\theta_{ab}\Delta_{\mathrm{Tav}}}.
\]

**Key.** Left: one particle-coordinate, two amplitudes. Right: two co-located frames. Mixing those two “twos” is how people over-read interferometry into SBT.

---

## 7. Orders of magnitude, so the word “macroscopic” stays honest

Pedalino working point, order of magnitude:

| Quantity | Value |
|----------|--------|
| \(m\) | \(172\,\mathrm{kDa}\approx 2.82\times 10^{-22}\,\mathrm{kg}\) |
| \(N\) | \(\gtrsim 7000\) atoms |
| \(R\) (body size) | \(\sim 4\,\mathrm{nm}\) |
| \(d_g\) (COM slit scale) | \(133\,\mathrm{nm}\) |
| \(\lambda_{\mathrm{dB}}\) at \(150\,\mathrm{m\,s^{-1}}\) | \(\sim 16\,\mathrm{fm}\) |
| Body size / \(\lambda_{\mathrm{dB}}\) | \(\sim 3\times 10^{5}\) |
| Superposition baseline / body size | \(d_g/R\sim 30\) |

**Key.** The packet is “big” compared with an atom and “small” compared with a cell. The COM wave is enormous compared with a nucleon Compton wavelength and tiny compared with the grating. “Macroscopic superposition” here means: a body with thousands of atoms has a \(\psi_{\mathrm{COM}}\) whose support is many body-diameters across. It does not mean a cat, a rock, or a brain.

---

## 8. Status

COM is the translational collective coordinate \(\mathbf{R}\). Pedalino superposed \(\psi_{\mathrm{COM}}\). SBT must treat \(\mathbf{R}\) of an isolated packet as unbound and \(\{\mathbf{r}'_a\}\) as bound. That is the whole implication of “explain more about COM” for the previous question.

---

## 9. Related files

- `Session_2026-09-30_Macroscopic_Superposition_Implies_for_SBT.md`
- `Session_2026-09-30_URL_Correction_Three_Papers.md`
- Pedalino et al., Nature 649, 866–870 (2026), DOI 10.1038/s41586-025-09917-9
