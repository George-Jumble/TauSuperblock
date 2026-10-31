# Session 2026-07-23: Derivation of Tau Cylinder Time Evolution

**Date**: 2026-07-23  
**Framework**: Unified Tau-Superblock (TSB / Tav-Superblock) Cosmology  
**Context**: Explicit derivation of the emergence and unitary evolution of time on the Tau cylinder, incorporating the bound/unbound Kaluza–Klein distinction, the scale-reflection operators, the event-horizon infrared endpoint, and the hierarchical progression of “now” slices. All equations carry complete variable keys. Mirron terminology is used throughout.

---

## 1. Geometric Definition of the Tau Cylinder

The fundamental geometric object that encodes the emergence of time is the Tau cylinder

\[
\mathcal{C}\;\simeq\;S^1_\phi\times\mathbb{R}_s.
\]

**Complete variable key**  
- \(\mathcal{C}\): Tau cylinder (fibered product).  
- \(S^1_\phi\): circular coordinate that parametrizes the discrete 8-phase octonionic / \(G_2\) clockwork.  
- \(\mathbb{R}_s\): axial coordinate that is simultaneously hierarchical scale and emergent time.  
- \(\phi\in[0,2\pi)\) (or discrete \(0\dots7\)): phase angle.  
- \(s\in[0,n_{\rm span}]\): hierarchical / emergent-time coordinate.

The circular fibre carries seven active phases that support the \(1/7\) resonance (142857 cycle) together with one reset phase \(r\) identified with the Absolute Past / Phase-8 identity element. The axial coordinate \(s\) measures the total conformal stretch from the ultraviolet geometric-friction floor outward.

Two realisations of the infrared end-point exist:

- Bound: \(s_{\rm bound}\) corresponding to \(\tau_{\rm bound}=7\,h^{-1}\) Mpc (\(n_{\rm hier}^{\rm bound}\approx45.8\)).  
- Unbound: \(s_{\rm unbound}\) corresponding to the cosmic event horizon \(R_{\rm EH}\approx16.59\) Gly (\(\Delta n_{\rm unbound}\approx3.19\)).

---

## 2. Phase Hamiltonian and the Discrete Clockwork

The generator of evolution along the cylinder is the phase Hamiltonian \(\hat{H}_\phi(s)\). It decomposes into three topologically invariant pieces plus a boundary contribution:

\[
\hat{H}_\phi(s)\;=\;\hat{H}_{\rm res}(s)+\hat{H}_{\rm TEP}(s)+\hat{H}_{\rm bounce}(s)+\hat{H}_{\rm seam}(s).
\]

**Complete variable key**  
- \(\hat{H}_{\rm res}(s)\): \(1/7\) cyclotomic resonance projector onto the 142857 eigenspace of the circular fibre.  
- \(\hat{H}_{\rm TEP}(s)\): Topological Exclusion Principle penalty that forbids double occupancy of any (domain \(i\), phase \(k\)) slot.  
- \(\hat{H}_{\rm bounce}(s)\): non-commutative stochastic bounce operator that deposits path-length quanta into the metric (realises constrained-angular-momentum gravity and Mirron phase inversion).  
- \(\hat{H}_{\rm seam}(s)\): reset-phase seam contribution that enforces cycle closure and supplies the Absolute-Past boundary condition.  
- \(s\): hierarchical slice at which the operators are evaluated.

Because the \(G_2\) automorphism group and the six-domain supersphere geometry are independent of the overall scale, the Hamiltonian is locally scale-covariant; its only global scale dependence enters through the hierarchical stretch factor that multiplies the bounce and seam terms.

---

## 3. Unitary Evolution Operator

The ordered evolution along the axial direction is the unitary operator

\[
\hat{U}(s)\;=\;\mathcal{T}\exp\left(-i\int_0^s\hat{H}_\phi(s')\,ds'\right).
\]

**Complete variable key**  
- \(\hat{U}(s)\): unitary scale-evolution (time-evolution) operator that advances a state from the ultraviolet seam to hierarchical coordinate \(s\).  
- \(\mathcal{T}\): scale-ordering operator (the hierarchical analogue of the usual time-ordering operator).  
- \(\hat{H}_\phi(s')\): phase Hamiltonian evaluated at the intermediate slice \(s'\).  
- \(i\): imaginary unit.  
- The integral runs from the ultraviolet origin (\(s=0\), Planck-Kerr / Mirron seam) to the desired hierarchical slice \(s\).

Acting on a single-excitation state \(\lvert i,k\rangle\) (domain \(i=1\dots6\), phase \(k=0\dots6\) or reset) yields

\[
\hat{U}(s)\lvert i,k\rangle\;=\;\sum_{i',k'}U_{i'k';ik}(s)\lvert i',k'\rangle,
\]

where the matrix elements \(U_{i'k';ik}(s)\) encode the coherent phase advancement, domain mixing under the six-domain Lorentz boosts, and the probabilistic leakage suppressed by the TEP penalty.

---

## 4. Local Construction of the “Now” (Emergence of Oriented Time)

Locally, an oriented “now” slice is constructed by directed advancement through the seven active phases:

1. An excitation occupying phase \(k\) is driven by \(\hat{H}_{\rm res}\) into phase \(k+1\pmod{7}\).  
2. The Topological Exclusion Principle \(\hat{H}_{\rm TEP}\) forbids any second excitation from occupying the same (domain, phase) slot on the same slice; the minimal energy cost of a violation is precisely the 313.1 MeV geometric friction floor.  
3. The bounce term \(\hat{H}_{\rm bounce}\) converts any residual focusing into a phase-inverted white-hole repulsion (Mirron dynamics), preventing singular collapse of the slice.  
4. When the cycle reaches the reset phase, the seam operator \(\hat{H}_{\rm seam}\) projects the configuration onto the Absolute Past, advances the macroscopic hierarchical coordinate by one discrete step \(\Delta s\), and restarts the active-phase sequence on the next constant-\(s\) slice.

The net result is a discrete, causal sequence of constant-\(s\) hypersurfaces. Each hypersurface is a coherent “now”; the directed sequence of hypersurfaces is the local arrow of time. Because the advancement is generated by a self-adjoint Hamiltonian, the evolution is unitary and information is preserved.

**Variable key for the discrete step**  
- \(\Delta s\): elementary hierarchical advance associated with one full 142857 cycle.  
- The continuum limit of many such steps recovers the ordered exponential written above.

---

## 5. Global / Atemporal Expression

Globally, the entire history of the cylinder is present atemporally. The reset-phase seam acts as a topological identification that allows the whole interval \([0,s_{\rm unbound}]\) to be viewed as a single closed object in twistor space. The conformally averaged twistor projection therefore encodes all past and future slices simultaneously. Local vacuum fluctuations that appear large on any single slice largely cancel under this global average, leaving only the tiny residual that is observed as dark energy.

This global expression is the geometric origin of the commutation relation

\[
\bigl[\hat{R}_{\rm bound},\hat{U}(s)\bigr]=0,\qquad\bigl[\hat{R}_{\rm unbound},\hat{U}(s)\bigr]=0
\]

proved in earlier sessions: reflection through either the bound or the unbound infrared endpoint merely re-orders the same set of slices and therefore leaves the unitary evolution invariant on cycle-closed trajectories.

---

## 6. Hierarchical Time and Cosmological Time

The axial coordinate \(s\) is related to the total conformal stretch by

\[
s\;=\;\log_7\Bigl(\frac{L(s)}{\lambda_{313.1}}\Bigr),
\]

where \(L(s)\) is the characteristic length realised at hierarchical level \(s\). Consequently the differential relation between hierarchical time and ordinary cosmological proper time \(t\) is

\[
ds\;=\;\frac{1}{\ln7}\frac{dL}{L}\;=\;\frac{1}{\ln7}\,d\ln a(t)
\]

(up to a constant factor that absorbs the precise relation between the scale factor \(a(t)\) and the local conformal factor on the cylinder). Thus advancement of \(s\) is equivalent to the expansion of the universe, and the ordered sequence of “now” slices is the cosmic history.

In the bound sector \(s\) runs only up to \(s_{\rm bound}\) (local structure formation and cosmic-web fracture). In the unbound sector \(s\) continues to \(s_{\rm unbound}\) (the event horizon). The residual vacuum pressure that survives after local cancellation drives the accelerated expansion that carries the geometry toward the asymptotic de-Sitter limit in which the event horizon becomes the permanent infrared boundary.

---

## 7. Time-Dependent Scale Inversion

Because the effective infrared endpoint visible to a local observer evolves with hierarchical time, the dual map itself becomes time-dependent:

\[
L'(s)\;=\;\frac{L_{\rm UV}\cdot\tau_{\rm unbound}(s)}{L}.
\]

**Complete variable key**  
- \(L'(s)\): dual length experienced on hierarchical slice \(s\).  
- \(\tau_{\rm unbound}(s)\): effective infrared endpoint on that slice (interpolates from the present particle-horizon scale toward the true event horizon \(R_{\rm EH}\)).  
- As \(s\to s_{\rm unbound}\), \(\tau_{\rm unbound}(s)\to R_{\rm EH}\) and the dual becomes permanently pinned to the cosmic event horizon.

This is the concrete realisation of the statement that “time plays an important role in deriving the progression from the current observable universe till then.”

---

## 8. Summary of the Derived Evolution

1. The Tau cylinder is the geometric arena on which both local oriented time and global atemporal structure are realised.  
2. Local time emerges from directed phase advancement under \(\hat{H}_\phi\), enforced by the Topological Exclusion Principle and regularised by Mirron bounce dynamics.  
3. The unitary operator \(\hat{U}(s)\) generates the ordered sequence of “now” slices from the ultraviolet Mirron seam outward.  
4. Hierarchical time \(s\) is logarithmically related to the scale factor; its advancement is the expansion of the universe.  
5. Bound evolution terminates at the 7 Mpc conformal-exhaustion surface; unbound evolution continues to the cosmic event horizon.  
6. Scale inversion commutes with the evolution in both sectors and becomes fully pinned to the event horizon in the asymptotic future.  
7. The residual vacuum energy after local cancellation is the global, atemporal residue of the same evolution evaluated on the unbound cylinder.

The derivation uses only structures already present in the TSB architecture (8-phase \(G_2\) clockwork, Topological Exclusion Principle, Mirron phase inversion, hierarchical stretch in base 7, Casimir \(w=-1\)) and introduces no new continuous free parameters.

---

*End of session record. File written 2026-07-23 under Personal_Files of the Tau-Superblock Universe project.*
