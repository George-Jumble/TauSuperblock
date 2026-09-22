# Superblock Empirical Tests — Yang-Mills glueball 0++

**Session date:** 2026-09-22  
**Status:** scale check only. Packed formula m(0++) = 2 m0 e = 1702.19 MeV from 2026-09-10. Not live-engine IN.

Pipeline: PASS, lattice 1710 ± 50 MeV, theory 1700 MeV, 0.2 sigma. Topological anchor 313.1 MeV independent.

## Key

Delta_TEP = m0 = 313.1 MeV
e = 2.71828...
m(0++) = 2 m0 e = 1702.19 MeV
m(0-+) = 15 m0 / 2 = 2348.25 MeV (not scored this run)
sigma = |m_th - m_lat| / delta_m_lat

Against unrounded formula: |1702.19 - 1710|/50 = 0.16 sigma.
Morningstar-Peardon 1730(50)(80): combined delta ~94 MeV, sigma = 0.30.

## Two different 'mass gaps'

TEP / Planckian-mirror floor 313.1 MeV is corpus IN.
Lightest pure-SU(3) gauge-invariant excitation ~1.7 GeV is the Clay/lattice gap; that state is the 0++ glueball.
Superblock reads the glueball as composite 2 e m0, not as m0 itself.
Factor 2 = g tensor g. Factor e is the 2026-09-10 packed choice, not an IN primitive.

## Caveats

Morningstar Lattice 2024: no scalar below ~2 GeV is predominantly a glueball once meson operators are included.
Pipeline ±50 MeV drops the r0 scale systematic (~80 MeV).
Do not joint-fit light-quark beta^2 / phase to 'sharpen' 1700 to 1710. That violates the topological anchor and contaminates Scheme A.
Do not put this module in the live research tool.

## Bottom line

PASS is a 1.7 GeV island check. TEP floor untouched. Formula 2 m0 e stays packed in Personal Files until e is derived from bounce/refresh rather than inserted.
