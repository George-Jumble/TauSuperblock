from __future__ import annotations

import math
from typing import Any

from .constants import GAMMA_HEX, R_M_LOCKED_FM, R_M_LOCKED_M, ELL_P_M, V_ORB


def lorentz_gamma(beta: float) -> float:
    b = min(max(beta, 0.0), 1.0 - 1e-18)
    return 1.0 / math.sqrt(1.0 - b * b)


def domain_table() -> list[dict[str, Any]]:
    weights = ["ω1", "ω5", "ω2", "ω4", "ω6", "ω3"]
    rows = []
    for i, d in enumerate(V_ORB):
        rows.append(
            {
                **d,
                "beta2": d["beta"] ** 2,
                "gamma_from_beta": lorentz_gamma(d["beta"]),
                "e6_weight": weights[i],
            }
        )
    return rows


def harmonic_mean_gamma() -> float:
    return len(V_ORB) / sum(1.0 / d["gamma"] for d in V_ORB)


def snapshot() -> dict[str, Any]:
    return {
        "r_M_fm": R_M_LOCKED_FM,
        "r_M_m": R_M_LOCKED_M,
        "ell_P_m": ELL_P_M,
        "log7_rM_over_lp": math.log(R_M_LOCKED_M / ELL_P_M) / math.log(7.0),
        "gamma_hex": GAMMA_HEX,
        "harmonic_mean_gamma": harmonic_mean_gamma(),
        "domains": domain_table(),
    }
