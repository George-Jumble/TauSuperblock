# Tau-Superblock Research Engine

Interactive curses-based research console for the **Tau Universe / Tav-Superblock** framework. Download scientific datasets, run τ-harmonic analyses across cosmology, particle physics, and empirical confrontations, and optionally review results with remote LLM providers.

**Entry point:** `research_tool.py`

## Features

- **Modular menus** — each domain lives in `menus/*/` with thin `*_extension.py` shims at the project root for backward compatibility
- **Dataset manager** — fetch, cache, and resume batch downloads (DESI, Planck, SPARC, FRB, LHCb, …)
- **Prime Past / BBN** — τ-Euler BBN interference scans, lithium confrontation, enhanced 5-state engine
- **Remote AI** — Grok, Gemini, OpenAI, Claude, OpenRouter, Ollama, NVIDIA NIM (`integrate.api.nvidia.com`)
- **Post-run LLM review** — set **AI verbose review = yes** on any module entry form

## Quick start

```bash
cd TauSuperblock
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp config/api_keys.env.example config/api_keys.env
# Edit config/api_keys.env with your API keys (optional; needed for Remote AI)

./venv/bin/python research_tool.py
```

Or use the helper script:

```bash
./research.sh
```

## Configuration

| File | Purpose |
|------|---------|
| `config/api_keys.env` | LLM provider keys (gitignored; copy from `api_keys.env.example`) |
| `.env` | Optional fallback for the same keys |
| `requirements-desi-production.txt` | Extra DESI MCMC dependencies (`emcee`, `ruptures`, …) |

**Never commit** `config/api_keys.env` or `.env`.

## Project layout

```
research_tool.py          # Thin entry → tav_research/runner.py
tav_research/             # Curses UI, menu tree, registry, data pull
tav_shared/               # LLM analysis, remote AI, run output, paths
menus/                    # Domain modules (prime_past, astronomical, particle, …)
config/                   # api_keys.env.example
scripts/                  # Maintenance utilities
```

## CLI tools (BBN)

| Script | Description |
|--------|-------------|
| `tav_bbn_confrontation.py` | RK45 BBN scanner with plots and JSON |
| `enhanced_tav_bbn_confrontation.py` | 5-state BBN, Li7 heatmap |
| `final_tav_bbn_confrontation_tool.py` | Best-config export and comparison plot |
| `tav_bbn_menu_module.py` | Tav BBN submenu engine |

## Dependencies

Core scientific stack: NumPy, SciPy, Matplotlib, Astropy, healpy, uproot/xrootd for ROOT/FITS I/O, plus [`tav-resonance`](https://pypi.org/project/tav-resonance/) for harmonic FRB/CMB analysis.

Large datasets and run artifacts are **not** in the repo — they are downloaded or written under `datasets/` and `artifacts/` at runtime (both gitignored).

## License

Research code — see individual module headers and the `tav-resonance` package for library licensing.
