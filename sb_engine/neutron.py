"""Hidden-domain neutron branching. HOLD test-module, not corpus IN.

BR_0 = 1 / (gamma_d * gamma_s)   two-clock coincidence on V_orb
epsilon in {1/7, 2/7}            one (or two-d) clockwork slot locks to B
"""

from __future__ import annotations

from typing import Any

from .constants import V_ORB

N7 = 7
TAU_BETA_S = 888.1
TAU_BETA_ERR_S = 2.0


def _gamma(flavour: str) -> float:
    for row in V_ORB:
        if row["flavour"] == flavour:
            return float(row["gamma"])
    raise KeyError(flavour)


def br0() -> float:
    return 1.0 / (_gamma("d") * _gamma("s"))


def br_sum() -> float:
    gd = _gamma("d")
    return sum(1.0 / (gd * _gamma(f)) for f in ("s", "c", "b", "t"))


def epsilon_values() -> dict[str, float]:
    return {"one_slot": 1.0 / N7, "two_d": 2.0 / N7}


def br_x(s: float = 0.0, epsilon: float | None = None) -> float:
    """s = 0 unpolarized / material / beam; s = +1 magnetic-bottle lock."""
    eps = epsilon_values()["one_slot"] if epsilon is None else float(epsilon)
    return br0() * (1.0 + eps * s)


def tau_tot_s(s: float = 0.0, epsilon: float | None = None, tau_beta: float = TAU_BETA_S) -> float:
    return float(tau_beta) * (1.0 - br_x(s=s, epsilon=epsilon))


def snapshot() -> dict[str, Any]:
    e7 = 1.0 / N7
    e27 = 2.0 / N7
    b0 = br0()
    return {
        "status": "HOLD",
        "formula_br0": "1/(gamma_d * gamma_s)",
        "gamma_d": _gamma("d"),
        "gamma_s": _gamma("s"),
        "BR_0": b0,
        "BR_sum_s_c_b_t": br_sum(),
        "epsilon_1_over_7": e7,
        "epsilon_2_over_7": e27,
        "tau_beta_s": TAU_BETA_S,
        "tau_isotropic_s": tau_tot_s(s=0.0, epsilon=e7),
        "tau_magnetic_eps7_s": tau_tot_s(s=1.0, epsilon=e7),
        "tau_magnetic_eps27_s": tau_tot_s(s=1.0, epsilon=e27),
        "delta_tau_pol_eps7_s": TAU_BETA_S * b0 * e7,
        "delta_tau_pol_eps27_s": TAU_BETA_S * b0 * e27,
        "jparc_prediction": "appearance methods must return ~888 s if s=0; 877.2 s is a live fail",
        "note": "Domain-internal leak. No on-shell chi gamma. TEP floor not fitted.",
    }
