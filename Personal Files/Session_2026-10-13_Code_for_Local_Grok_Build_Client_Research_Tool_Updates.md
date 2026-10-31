# Session 2026-10-13: Code for Local Grok Build Client — Research Tool Updates

**Date**: 2026-10-13  
**Purpose**: Ready-to-paste code / file contents for the local Grok build client to apply the suggested changes to George-Jumble/TauSuperblock.  
**Hard rule**: 3+1D Superblock Cosmology frame.  

## Build Instruction (paste into local Grok build client)

Update the TauSuperblock research tool to align with live 4D locks:

1. Change printed working mass floor from 313.1 MeV to 309.3 MeV (neutron dressing protocol). Recalculate r_M.
2. Remove N_HIER = 45.8 from live constants and from DESI calibration.
3. Add explicit synthetic / illustration warnings to cms, casimir, and sparc modules.
4. Update README.md and CORPUS.md accordingly.

Apply the following file contents.

---

## File: sb_engine/constants.py

```python
"""Superblock / Mirron constants. No Tau cylinder, no 142857 comb."""

from __future__ import annotations

HBAR_C_MEV_FM = 197.3269718
# Printed working floor: neutron dressing share protocol (insertion, not a derivation).
# Old print was 313.1 MeV (rounded M_n/3).
DELTA_TEP_MEV = 309.3
R_M_LOCKED_FM = HBAR_C_MEV_FM / DELTA_TEP_MEV
R_M_LOCKED_M = R_M_LOCKED_FM * 1e-15
ELL_P_M = 1.616255e-35
# N_HIER retired with the Tau metric package. Do not use in live engines.
RD_OBSERVED_MPC = 147.09
RD_OBSERVED_ERR_MPC = 0.26
DELTA_N_PLASMA = 10.74
LATE_UNIVERSE_DELTA_N = 0.33
GAMMA_HEX = 1.405
Z0_OHM = 376.730313461
CORPUS_DATE = "2026-10-13"

V_ORB = (
    {"domain": 0, "flavour": "u", "role": "Prime", "beta": 0.0, "gamma": 1.0},
    {"domain": 1, "flavour": "d", "role": "near", "beta": 0.8881, "gamma": 2.176},
    {"domain": 2, "flavour": "s", "role": "mid", "beta": 0.999733, "gamma": 43.29},
    {"domain": 3, "flavour": "c", "role": "fast", "beta": 1 - 1.44e-6, "gamma": 589.4},
    {"domain": 4, "flavour": "b", "role": "fast", "beta": 1 - 1.333e-7, "gamma": 1936.6},
    {"domain": 5, "flavour": "t", "role": "ultrarel", "beta": 1 - 7.83e-11, "gamma": 7.989e4},
)
```

---

## File: sb_engine/desi.py

```python
from __future__ import annotations

from typing import Any

from .constants import (
    DELTA_N_PLASMA,
    RD_OBSERVED_ERR_MPC,
    RD_OBSERVED_MPC,
)


def sound_horizon(gamma: float) -> dict[str, Any]:
    """r_d = ΔN_plasma * r_d,obs / γ. Residual is identically zero when γ = ΔN_plasma (by construction). No Tau compact period. No n_hier."""
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
        "note": "residual identically zero when gamma equals DELTA_N_PLASMA (by construction)",
    }


def calibrate_gamma() -> float:
    """Default calibration. No n_hier factor."""
    return DELTA_N_PLASMA
```

---

## File: sb_engine/cms.py

```python
from __future__ import annotations

import math
import random
from typing import Any


def run_cms(n: int = 4000, amp: float = 0.18, seed: int = 7) -> dict[str, Any]:
    """SYNTHETIC ILLUSTRATION ONLY.
    Generates counts from a 7-fold modulation and recovers it.
    Not a real CMS Open Data analysis. Do not treat chi2 as a detection.
    """
    n = max(200, min(int(n), 20000))
    amp = min(max(float(amp), 0.0), 0.8)
    rng = random.Random(seed)
    weights = [1.0 + amp * math.cos(2.0 * math.pi * k / 7.0) for k in range(7)]
    total = sum(weights)
    cdf = []
    acc = 0.0
    for w in weights:
        acc += w / total
        cdf.append(acc)
    counts = [0] * 7
    for _ in range(n):
        u = rng.random()
        slot = next((i for i, c in enumerate(cdf) if u <= c), 6)
        counts[slot] += 1
    expected = n / 7.0
    chi2_null = sum((c - expected) ** 2 / expected for c in counts)
    pred = [n * w / total for w in weights]
    chi2 = sum((c - p) ** 2 / p for c, p in zip(counts, pred))
    return {
        "status": "SYNTHETIC",
        "warning": "This module plants the 7-fold signal it recovers. Not real CMS data.",
        "n": n,
        "amp": amp,
        "counts": counts,
        "chi2_clockwork": chi2,
        "chi2_uniform": chi2_null,
        "note": "7 active clockwork slots; Φ8 is reset and is not a CMS bin",
    }
```

---

## File: sb_engine/casimir.py

```python
from __future__ import annotations

import math
from typing import Any

from .constants import R_M_LOCKED_M

PREF = 1.299e-27  # N m^2, perfect-conductor |F/A| ~ 1/d^4


def casimir_curve(amp: float = 0.04, phase: float = 0.0, n: int = 48) -> list[dict[str, Any]]:
    """SYNTHETIC ILLUSTRATION ONLY. Adds a hand-injected log7 ripple."""
    out = []
    for i in range(n):
        d_nm = 20.0 * (400.0 / 20.0) ** (i / (n - 1))
        d = d_nm * 1e-9
        lif = -PREF / d**4
        log7 = math.log(d / R_M_LOCKED_M) / math.log(7.0)
        ripple = 1.0 + amp * math.sin(2.0 * math.pi * log7 + phase)
        out.append({"d_nm": d_nm, "lifshitz": lif, "mirron": lif * ripple})
    return out


def shape_battery(amp: float = 0.04, phase: float = 0.0) -> dict[str, Any]:
    """SYNTHETIC ILLUSTRATION ONLY.
    Injects a log7 modulation then measures steps and slope.
    Not a real dielectric-response analysis.
    """
    pts = casimir_curve(amp, phase, 64)
    y = [p["mirron"] for p in pts]
    x = [math.log10(p["d_nm"]) for p in pts]
    dy = [y[i + 1] - y[i] for i in range(len(y) - 1)]
    mu = sum(dy) / len(dy)
    var = sum((v - mu) ** 2 for v in dy) / len(dy)
    sd = math.sqrt(var)
    steps = sum(1 for v in dy if abs(v - mu) > 2 * sd)
    logy = [math.log10(abs(v)) for v in y]
    xbar = sum(x) / len(x)
    ybar = sum(logy) / len(logy)
    num = sum((x[i] - xbar) * (logy[i] - ybar) for i in range(len(x)))
    den = sum((x[i] - xbar) ** 2 for i in range(len(x)))
    slope = num / den
    return {
        "status": "SYNTHETIC",
        "warning": "This module plants a log7 ripple then recovers shape features. Not real Casimir data.",
        "discrete_steps": steps,
        "m_plus_4": abs(slope + 4.0),
        "note": "shape battery only; not ΔE = E_obs - E_Lifshitz (dropped 2026-09-15)",
    }
```

---

## File: sb_engine/sparc.py

```python
from __future__ import annotations

import math
from typing import Any

from .constants import GAMMA_HEX, V_ORB

G_KPC = 4.30091e-6
D_BETA2 = V_ORB[1]["beta"] ** 2


def _miyamoto(r: float, mass: float, a: float, b: float) -> float:
    den = (r * r + (a + b) ** 2) ** 1.5
    return math.sqrt(max(G_KPC * mass * r * r / den, 0.0))


def _nfw(r: float, rho_s: float, rs: float) -> float:
    x = r / rs
    f = math.log(1.0 + x) - x / (1.0 + x)
    v2 = 4.0 * math.pi * G_KPC * rho_s * rs**3 * f / max(r, 1e-6)
    return math.sqrt(max(v2, 0.0))


def emergent_dm(r: float, beta2: float, phase: float) -> float:
    r_c = 2.2 + 5.4 * beta2 + 0.7 * math.sin(phase)
    v_scale = 38.0 + 95.0 * math.sqrt(max(beta2, 0.0)) * (GAMMA_HEX / 1.4)
    ripple = 1.0 + 0.1 * math.sin(phase + r / 6.0)
    return v_scale * math.sqrt(r / (r + r_c)) * ripple


def run_sparc(beta2: float = D_BETA2, phase: float = 0.4) -> dict[str, Any]:
    """SYNTHETIC ILLUSTRATION ONLY.
    Generates synthetic NGC3198 velocities then fits them with emergent_dm.
    Not a confrontation with published SPARC rotation curves.
    """
    points = []
    chi2 = 0.0
    for i in range(28):
        r = 0.6 + i * 1.35
        v_disk = _miyamoto(r, 3.05e10, 3.14, 0.35)
        v_gas = _miyamoto(r, 1.15e10, 8.4, 0.25)
        v_bar = math.hypot(v_disk, v_gas)
        v_obs = math.hypot(v_bar, _nfw(r, 4.2e6, 16.5))
        e_obs = 6.5 + 0.04 * r
        v_dm = emergent_dm(r, beta2, phase)
        v_th = math.hypot(v_bar, v_dm)
        chi2 += ((v_obs - v_th) / e_obs) ** 2
        points.append(
            {
                "r_kpc": r,
                "v_obs": v_obs,
                "v_bar": v_bar,
                "v_dm": v_dm,
                "v_theory": v_th,
            }
        )
    ndof = max(len(points) - 2, 1)
    return {
        "status": "SYNTHETIC",
        "warning": "This module synthesizes NGC3198 data and fits it. Not real SPARC curves.",
        "galaxy": "NGC3198 (synthetic)",
        "beta2": beta2,
        "phase": phase,
        "chi2": chi2,
        "reduced_chi2": chi2 / ndof,
        "n": len(points),
        "points": points,
    }
```

---

## Suggested edits for README.md (replace the relevant lines)

Change:
- TEP floor Δ = 313.1 MeV → TEP floor Δ = 309.3 MeV (neutron dressing protocol)
- r_M = λ_313 ≈ 0.630 fm → r_M = ħc / 309.3 MeV

Add under “What is live”:
- Empirical CLIs (cms, casimir, sparc) are currently synthetic illustrations that plant the signal they recover.

## Suggested edits for CORPUS.md

In the IN section:
- Change “TEP floor Δ = ħc / r_M = 313.1 MeV” to “TEP floor Δ = 309.3 MeV (neutron dressing protocol; insertion)”
- Remove or move “n_hier Superblock hierarchical binding” to OUT or a retired note.

In the OUT section, add:
- n_hier = 45.8 (retired with Tau metric package)

---

## Notes for the build client
- Do not reintroduce τ, n_hier as a live count, or any 5D language.
- Neutron module can remain unchanged (already correctly HOLD).
- Geometry and bounce modules need only the floor-number update if they print r_M.
- After applying, run `python research_tool.py geometry` and `python research_tool.py desi` to verify residual is zero at default gamma and r_M has updated.

**File path**: Tau-Superblock-Universe/Personal Files/Session_2026-10-13_Code_for_Local_Grok_Build_Client_Research_Tool_Updates.md
