"""Superblock / Mirron constants. No Tau cylinder, no 142857 comb."""

from __future__ import annotations

HBAR_C_MEV_FM = 197.3269718
DELTA_TEP_MEV = 313.1
R_M_LOCKED_FM = HBAR_C_MEV_FM / DELTA_TEP_MEV
R_M_LOCKED_M = R_M_LOCKED_FM * 1e-15
ELL_P_M = 1.616255e-35
N_HIER = 45.8  # Superblock binding; not log7(R_tau / r_M)
RD_OBSERVED_MPC = 147.09
RD_OBSERVED_ERR_MPC = 0.26
DELTA_N_PLASMA = 10.74
LATE_UNIVERSE_DELTA_N = 0.33
GAMMA_HEX = 1.405
Z0_OHM = 376.730313461
CORPUS_DATE = "2026-09-22"

V_ORB = (
    {"domain": 0, "flavour": "u", "role": "Prime", "beta": 0.0, "gamma": 1.0},
    {"domain": 1, "flavour": "d", "role": "near", "beta": 0.8881, "gamma": 2.176},
    {"domain": 2, "flavour": "s", "role": "mid", "beta": 0.999733, "gamma": 43.29},
    {"domain": 3, "flavour": "c", "role": "fast", "beta": 1 - 1.44e-6, "gamma": 589.4},
    {"domain": 4, "flavour": "b", "role": "fast", "beta": 1 - 1.333e-7, "gamma": 1936.6},
    {"domain": 5, "flavour": "t", "role": "ultrarel", "beta": 1 - 7.83e-11, "gamma": 7.989e4},
)
