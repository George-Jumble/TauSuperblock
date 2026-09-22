# Neutron BR module vs the research tool

**Session date:** 2026-09-22  
**Question:** Does the derived BR_X / epsilon module need to be put into the research tool?  
**Answer:** No. Not in the live engine path. It may stay in the repo as a HOLD sandbox.

CORPUS.md policy: live engines may only see IN entries.

Already in the tree from the derivation commit: sb_engine/neutron.py, CLI `python research_tool.py neutron`, HOLD line in CORPUS.md. That wiring is convenience, not a requirement.

Keep: the Personal Files derivation, neutron.py as a file, the HOLD ledger line.
Do not: import br0() into SPARC / DESI / CMS / Casimir / bounce; retune Delta_TEP from this BR; move HOLD to IN.

Optional: leave the neutron subparser only because snapshot() already prints status HOLD, or unhook the subparser and keep the module importable. Same physics.
