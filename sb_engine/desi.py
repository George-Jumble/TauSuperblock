from __future__ import annotations

from typing import Any

from .constants import (
    DELTA_N_PLASMA,
    LATE_UNIVERSE_DELTA_N,
    N_HIER,
    RD_OBSERVED_ERR_MPC,
    RD_OBSERVED_MPC,
)


def sound_horizon(gamma: float) -> dict[str, Any]:
    """r_d = ΔN_plasma * r_d,obs / γ. No Tau compact period."""
    g = max(float(gamma), 1e-6)
    rd = (DELTA_N_PLASMA * RD_OBSERVED_MPC) / g
    residual = rd - RD_OBSERVED_MPC
    return {
        "gamma": g,
        "rd_predicted_mpc": rd,
        "rd_observed_mpc": RD_OBSERVED_MPC,
        "residual_mpc": residual,
        "residual_sigma": residual / RD_OBSERVED_ERR_MPC,
        "delta_n_plasma": DELTA_N_PLASMA,
        "n_hier": N_HIER,
    }


def calibrate_gamma(n_hier: float = N_HIER) -> float:
    hier = 1.0 + LATE_UNIVERSE_DELTA_N * (n_hier / N_HIER - 1.0)
    return DELTA_N_PLASMA * hier
