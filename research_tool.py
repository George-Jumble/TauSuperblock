#!/usr/bin/env python3
"""Superblock Research Engine — Tau layer out.

Run: python research_tool.py <geometry|sparc|desi|cms|casimir|bounce|corpus|neutron>
"""

from __future__ import annotations

import argparse
import json
import sys

from sb_engine import bounce, casimir, cms, corpus, desi, geometry, neutron, sparc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Superblock / Mirron research engine (no Tau)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("geometry")
    sub.add_parser("corpus")
    sub.add_parser("bounce")
    sub.add_parser("neutron")

    p_sp = sub.add_parser("sparc")
    p_sp.add_argument("--beta2", type=float, default=sparc.D_BETA2)
    p_sp.add_argument("--phase", type=float, default=0.4)

    p_d = sub.add_parser("desi")
    p_d.add_argument("--gamma", type=float, default=None)

    p_c = sub.add_parser("cms")
    p_c.add_argument("--n", type=int, default=4000)
    p_c.add_argument("--amp", type=float, default=0.18)
    p_c.add_argument("--seed", type=int, default=7)

    p_ca = sub.add_parser("casimir")
    p_ca.add_argument("--amp", type=float, default=0.04)
    p_ca.add_argument("--phase", type=float, default=0.0)

    args = parser.parse_args(argv)
    if args.cmd == "geometry":
        payload = geometry.snapshot()
    elif args.cmd == "corpus":
        print(corpus.text())
        return 0
    elif args.cmd == "sparc":
        payload = sparc.run_sparc(beta2=args.beta2, phase=args.phase)
        payload = {k: v for k, v in payload.items() if k != "points"} | {
            "n_points": len(payload["points"])
        }
    elif args.cmd == "desi":
        g = args.gamma if args.gamma is not None else desi.calibrate_gamma()
        payload = desi.sound_horizon(g)
    elif args.cmd == "cms":
        payload = cms.run_cms(n=args.n, amp=args.amp, seed=args.seed)
    elif args.cmd == "casimir":
        payload = casimir.shape_battery(amp=args.amp, phase=args.phase)
    elif args.cmd == "bounce":
        cyc = bounce.bounce_cycle()
        payload = {"canon": cyc["canon"], "n": len(cyc["frames"])}
    elif args.cmd == "neutron":
        payload = neutron.snapshot()
    else:
        parser.error(args.cmd)
        return 2

    json.dump(payload, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
