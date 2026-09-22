from __future__ import annotations

import math
from typing import Any

CANON = (
    "Bounce stays in original Superblock / CCC form: conformal aeon crossover "
    "plus Mirron / Planck–Kerr dynamic refresh. Not a Φ7 pin-drop, not a "
    "Coleman instanton, not Biquaternion M+."
)


def bounce_cycle(n: int = 64) -> dict[str, Any]:
    frames = []
    for i in range(n):
        t = i / (n - 1)
        phase = t * 8.0
        k = min(7, int(phase))
        local = phase - k
        if k == 7:
            omega = math.sin(math.pi * local) ** 2 * 0.08
            refresh = 1.0 - math.cos(2.0 * math.pi * local) * 0.5
            aeon = "bridge"
        else:
            omega = 0.25 + 0.75 * math.sin(math.pi * (k + local) / 8.0) ** 2
            refresh = 0.15 + 0.1 * math.sin(2.0 * math.pi * local)
            aeon = "past" if k < 3 else "future"
        frames.append(
            {"phase": phase, "k": k, "conformal": omega, "refresh": refresh, "aeon": aeon}
        )
    return {"canon": CANON, "frames": frames}
