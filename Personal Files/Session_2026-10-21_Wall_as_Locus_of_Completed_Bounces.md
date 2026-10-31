# Session 2026-10-21: Wall Defined as the Locus of Completed Bounces

**Date**: 2026-10-21  
**Query**: the wall is defined as the locus of completed bounces.  
**Context**: Refinement of the non-locking identification of the unbound bounce as energy source for the Mirron/Entropic wall potential. Live 4D Superblock locks unchanged.

## Definition

The conformal hard-wall (or the high-Weyl complement, or the photon-orbit world-tube in the open reading) is the locus at which unbound bounces complete.

\[
\text{Wall}
\equiv
\{\,x \mid \text{bounce completes at }x,\ L_{\rm res}(x)=0\,\}.
\]

Every completed unbound quantum deposits its energy on this locus and leaves no residual angular momentum.

**Variable key:**  
- Wall: geometric locus of completed unbound bounces.  
- \(L_{\rm res}\): residual angular momentum (vanishes on the wall by definition of unbound completion).  
- \(x\): point on the 4D chamber boundary or world-tube.

## Immediate consequences

1. Localization is definitional, not an extra assumption.  
   Free-streaming null quanta are unbound precisely when and where their bounce completes. Their energy is therefore on the wall by the definition of the wall. No auxiliary “localization factor” is required beyond the geometric identification itself.

2. Wall potential is the energy of completed bounces:
   \[
   V_{\rm wall}
   =
   \sum_{\rm completions\ on\ wall}
   E_{\rm unbound}^{(i)}.
   \]
   The entropic force remains
   \[
   \mathbf{F}_{\rm ent}
   =
   -\nabla V_{\rm wall},
   \]
   directed toward the high-Weyl / lack-of-mass side.

3. Bound sector is cleanly excluded.  
   Stopped rebounds occur in the interior globs and generate residual \(L\). They never complete, so they never sit on the wall. Residual-\(L\) gravity continues to match laboratory \(G\) with no contribution from the wall.

4. Laboratory Casimir stays distinct.  
   The local Lifshitz pressure between plates is a restricted vacuum fluctuation (floor object). It is not a completed unbound bounce on the cosmological wall, so the author cut is preserved.

5. Tau package remains rejected.  
   The wall is a 3-surface (or world-tube) inside the existing 3+1 geometry, not a metric \(S^1_\tau\).

## Scale status (unchanged)

Defining the wall as the locus of completed bounces removes the need for an extra localization parameter, but it does not evaluate the total energy on that locus. No existing lock computes
\[
E_{\rm unbound}^{\rm tot}
=
\sum_{\rm completions}
E_{\rm unbound}^{(i)}.
\]
Equating the resulting surface or volume density to the observed
\[
\rho_\Lambda
\sim
5\times10^{-10}\,\mathrm{J\,m^{-3}}
\]
remains a matching condition. The magnitude is still fitted.

## Relation to prior notes

- Extends the 2026-10-18 wall-as-sum-of-all-unbound-energy identification by making the geometric locus explicit.  
- Removes the parenthetical caveat in the preceding unbound-bounce note (“unless the wall is defined as the locus of completed bounces”). That condition is now the definition.  
- All other conclusions stand: residual-\(L\) preserved, Casimir cut preserved, Tau rejected, \(\rho_\Lambda\) not derived.

## Equations (complete key)

Wall as locus:
\[
\text{Wall}
=
\{x \in \mathcal{M}_4 \mid \text{unbound bounce completes at }x\}.
\]
- \(\mathcal{M}_4\): 4D chamber.  
- Completion \(\Leftrightarrow L_{\rm res}=0\).

Potential and force:
\[
V_{\rm wall}
=
\sum_{i\in\text{Wall}}
E_{\rm unbound}^{(i)},
\qquad
\mathbf{F}_{\rm ent}
=
-\nabla V_{\rm wall}.
\]
- \(E_{\rm unbound}^{(i)}\): energy deposited by the \(i\)-th completion.  
- \(\nabla\): gradient transverse to the wall (or on the world-tube).

Residual-\(L\) (interior only):
\[
L_{\rm res}
=
\int_{\partial\mathcal{B}_{\rm interior}}
\mathbf{J}_{\rm bound}
\cdot
d\mathbf{A}
\neq
0.
\]
- Bound rebounds never reach the wall.

Observed density (external input):
\[
\rho_\Lambda
\sim
5\times10^{-10}\,\mathrm{J\,m^{-3}}.
\]

## Conclusion

Defining the wall as the locus of completed bounces makes the unbound energy naturally resident on the wall. The Mirron/Entropic potential and its gradient toward the lack-of-mass side follow directly from that definition. Every live lock is preserved. The construction remains non-locking: the total energy on the locus is not calculated by existing protocols, so the strength of the entropic force relative to \(\rho_\Lambda\) is still fitted.

**File**: Tau-Superblock-Universe/Personal Files/Session_2026-10-21_Wall_as_Locus_of_Completed_Bounces.md
