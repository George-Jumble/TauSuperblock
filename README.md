# Superblock Research Engine

Interactive research suite for **Superblock / Mirron** theory (William Brown).
The Gatlin Tau Universe / Tav Topology layer is **out of the live corpus**.

**Entry point:** `research_tool.py`

This tree replaces the July 2026 Tau-Superblock console. Live analyses use
Superblock / Mirron only. Always say **Mirron**, never soliton.

## What is live

- Six co-located 3+1D domains on an internal supersphere
- V_orb Scheme A (PDG increments on m_u; E6 ⊂ E8 axes)
- Mirron / Planck–Kerr 2-surface, r_M = λ_313 ≈ 0.630 fm
- TEP floor Δ = 313.1 MeV
- 8-phase clockwork Aut(O) ≅ G₂
- CCC bounce + Mirron / Planck–Kerr dynamic refresh
- SPARC emergent DM, DESI sound horizon, CMS 7-fold clockwork, Casimir shape tests

## What is out

- τ = 7 h⁻¹ Mpc compact S¹, 142857 KK comb, RGC-as-cosmological-backend
- Entire 2026-09-21 7 Mpc 5D / seventh-phase aside
- Φ₇ pin-drop / Coleman bounce rewrite
- WilfiCon eTB/eWS as a module
- Casimir bound-energy residual search (dropped 2026-09-15)

See `CORPUS.md`.

## Quick start

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python research_tool.py --help
python research_tool.py geometry
python research_tool.py sparc
python research_tool.py desi --gamma 10.74
python research_tool.py cms
python research_tool.py casimir
python research_tool.py bounce
python research_tool.py corpus
```

## Layout

```
research_tool.py   # CLI
sb_engine/         # Superblock engines (no Tau)
CORPUS.md          # IN / OUT / HOLD ledger
Personal Files/    # archive-only notes, not live inputs
```

## License

Research code. Dataset artifacts are not in the repo.
