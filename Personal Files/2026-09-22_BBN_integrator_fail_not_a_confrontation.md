# BBN abundance confrontation — integrator fail, not a Superblock test

**Session date:** 2026-09-22  
**Status:** FAIL of the network. Do not score Superblock against the printed sigma values. Do not add this module to the live research tool.

Y_D = 0 in both standard and modified runs. Free Y_n = 0.046 still present at T = 0.01 MeV. Baseline Y_p = 0.2278 vs real SBBN ~0.247 and obs 0.245 ± 0.003. Baseline Li7/H = 1.34e-7 vs real SBBN ~5e-10 and Spite ~1.5e-10.

Printed 87.8 sigma / 6.1 sigma / 5103 sigma measure missing species, not theory.
Modified-vs-baseline shifts (+14.4% Li, -0.442% Y_p) are smaller than the integrator bias.

Banner still says Tav Framework Modified. Footer correctly says this is not a compact S1_tau residue. Drop the Tav name.

Acceptance test before any Superblock lever: Y_p in [0.246, 0.248], D/H in [2.4, 2.7]e-5, Li7/H in [4, 6]e-10, residual free Y_n(10 keV) < 1e-6. Use PRyMordial / AlterBBN / PArthENoPE.

TEP 313.1 MeV untouched (it was never in the ODE).
