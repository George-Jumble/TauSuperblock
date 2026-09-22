# Full empirical-test pipeline — rollup verdict

**Session date:** 2026-09-22  
**Tests:** light quarks, neutron lifetime, glueball 0++. BBN not in this bundle.

Pipeline flags all three PASS. Ledger reading:
- Light quarks: TEP floor 313.1 MeV is IN. The 0.01 sigma vs 313.0 ± 8 MeV is consistency inside a coarse constituent band, not a current-quark confirmation.
- Neutron: printed target 0.0094 is underived. Replace with HOLD BR_0 = 1/(gamma_d gamma_s) = 0.010616. J-PARC 877.2 s is a live fail of s=0 appearance. Not live-tool.
- Glueball: 1700 MeV is rounded 2 m0 e = 1702.19 from the 2026-09-10 pack. Scale check only. Kill the joint-fit-beta2 sentence. Factor e is not IN.
- BBN (other run): integrator fail. Do not fold those sigmas into the TeX.

Three green flags share m0 by construction. They are not a joint likelihood.

TeX must not say three PASSes confirm Superblock.
