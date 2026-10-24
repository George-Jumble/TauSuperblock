# Session 2026-10-24: Can the Free Parameters of the Information-Carrying Force Be Tested by the Research Tool?

**Date**: 2026-10-24  
**Framework**: Tau-Superblock (TSB / Superblock) — live 4D frame. Free parameters added by the information-carrying harmonic force: coupling function \(f(\{\phi_n\})\), optional screening length \(\lambda_{\rm screen}\), optional synchronization strength \(\kappa_{\rm sync}\). Live research tool is George-Jumble/TauSuperblock research_tool.py (modules: geometry, corpus, bounce, neutron, sparc, desi, cms, casimir). Prior audit (2026-10-07) notes that CMS, SPARC, and Casimir CLIs plant the signal they recover.  
**Question**: Can any of the free parameters provide predictions which can be tested through the research tool?  
**Answer**: Not with the current tool.  
**Status**: Clarification.

## Plain-language summary

No. None of the free parameters is implemented in the existing research tool, and none of the present modules is designed to test an information-carrying force or a Mirron synchronization strength. The tool’s SPARC, DESI, CMS, and Casimir modules either plant the signals they recover or are calibrated so that residuals vanish. Adding a test would require new code that is not present.  

Until such code exists and is independently verified, the free parameters remain untested phenomenological numbers.

## Analytical note

**Key to symbols**  
- \(f(\{\phi_n\})\), \(\lambda_{\rm screen}\), \(\kappa_{\rm sync}\): free parameters of the proposal.  
- research_tool.py: current analysis engine.  

No module accepts these parameters as input, and no module outputs a residual or a significance that isolates them. Planted-signal behavior in the existing CLIs further prevents a clean test. A genuine prediction would require a new, non-planting module that is not yet written.

## Repercussions and locks

- Free parameters remain untested.  
- Does not alter residual-L laboratory \(G\) match.  
- Does not restore the rejected Tau package.  
- Research-tool planted-signal note stands.

## References

- Preceding note listing the free parameters.  
- Research-tool falsification checklist (2026-10-07).  
- Live locks.

---  
*Saved under Personal Files in the Tau-Superblock-Universe project (George-Jumble/TauSuperblock).*
