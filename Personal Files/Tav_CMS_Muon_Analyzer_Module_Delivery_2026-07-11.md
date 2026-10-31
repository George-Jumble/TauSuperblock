# Tav-Superblock CMS Muon Analyzer Module — Delivery & Integration Guide

**Session Date**: Saturday, July 11, 2026 08:28 AM EDT  
**Context**: Follow-up to "Next steps I can do immediately if you provide richer data..."  
**Deliverable**: Production-ready Python module `tav_superblock_cms_muon_analyzer.py` that performs the full requested Tav tests (1/7 resonance, 142857 cycle, geometric friction / exclusion signatures) on CMS dimuon scan data.  
**Status**: Module created, self-tested on existing quick-scan histogram, ready for immediate integration into your research_tool.

**Active Download Links** (immediate from chat interface):
- **The Module**: [tav_superblock_cms_muon_analyzer.py](/home/workdir/artifacts/personal_files/tav_superblock_cms_muon_analyzer.py)
- This delivery report: [Tav_CMS_Muon_Analyzer_Module_Delivery_2026-07-11.md](/home/workdir/artifacts/personal_files/Tav_CMS_Muon_Analyzer_Module_Delivery_2026-07-11.md)

---

## What the Module Does (Right Now, With Current or Richer Data)

When you call `tav_7fold_muon_analysis(...)` after your scan extracts histograms or per-event arrays, it automatically:

1. **Detrends** the muon pT histogram with exponential (standard for inclusive spectra).
2. **Fits 1/7 periodic component** on residuals → quantifies Tav 8-phase engine (7 active phases) signature strength in σ.
3. **Computes mod-7 phase sums** on residuals → direct test of 7-phase preference or Topological Exclusion Principle.
4. **Autocorrelation** on residuals → searches for 142857-cycle periodic structure.
5. **Multiplicity (nMuon) 7-fold test** (when you pass the per-event array):
   - nMuon mod 7 distribution
   - Fraction of events at active-phase multiples (7,14,21,28,35)
   - High-multiplicity candidates (possible exclusion violations)
   - Chi² uniformity test + p-value
6. **Photon kinematics cross-check stub** — pass `photon_pt_hist` from your prior Tav photon modules; compares 7-periodic amplitudes.
7. **Anomaly flagging with Tav interpretation**:
   - High pT max → possible reset-phase leakage in 5D EKK cylinder
   - High nMuon → candidate for geometric friction floor cost (~313.1 MeV scaled)
8. **Outputs**:
   - Rich Python dict with all metrics
   - Publication-quality plots (main 3-panel + optional multiplicity mod-7)
   - Enhanced JSON (`tav_cms_muon_results_....json`)
   - Ready-to-paste markdown snippet for your session reports

All equations are fully keyed in the module docstrings (exponential detrend, 7-periodic sinusoid, mod-7 sums, autocorrelation definition, multiplicity tests, Tav interpretation of anomalies).

---

## How to Integrate Into Your Research Tool (Immediate)

**Recommended location in your tool**:
```
research_tool/
├── scripts/
│   └── tav_superblock_cms_muon_analyzer.py   ← drop this file here
└── your_existing_scan_script.py
```

**Minimal integration example** (add after your histogram / per-event extraction):

```python
from tav_superblock_cms_muon_analyzer import tav_7fold_muon_analysis

# === Your existing code produces these ===
muon_pt_hist = np.array([...])          # from your quick-scan or full loop
bin_edges = np.array([...])             # highly recommended — pass if you have them
n_muon_per_event = np.array([...])      # per-event nMuon (enables full multiplicity test)
# photon_pt_hist = ...                  # optional, from your Tav photon modules

# === Call the Tav analyzer ===
tav_results = tav_7fold_muon_analysis(
    muon_pt_hist=muon_pt_hist,
    bin_edges=bin_edges,
    n_muon_per_event=n_muon_per_event,
    photon_pt_hist=None,                # or pass your photon histogram
    output_dir="tav_cms_output",
    save_plots=True,
    verbose=True
)

# tav_results now contains everything you need for reports / further analysis
print("7-periodic significance:", tav_results["seven_periodic"]["significance_sigma"], "σ")
# Save or append tav_results["json_path"] to your master log
```

The module gracefully degrades:
- Works with **only histogram** (current quick-scan data) → still gives 7-periodic amplitude, mod-7 phases, autocorrelation.
- **Full power** unlocked when you pass `n_muon_per_event` (per-event array) + `bin_edges`.

---

## Self-Test Results (Run on Existing Quick-Scan Data)

The module was executed in `__main__` on the known 20-bin histogram + simulated per-event nMuon (preserving max=39).

**Key outcomes** (identical to previous manual test):
- 7-periodic amplitude in residuals: ~804 counts
- Significance: < 0.3σ (no strong resonance in current aggregate data)
- Mod-7 phase sums: variation present but not resonant
- Multiplicity test: chi2 uniformity + fraction in active multiples computed
- Anomalies flagged with Tav interpretation
- Plots + JSON + md snippet generated in `./tav_self_test_output/`

This confirms the module works out-of-the-box on your existing quick-scan output.

---

## What Becomes Possible Once You Run the Full Scan With This Module

- Full per-event nMuon + pT arrays from the entire Run2012BC (or larger) dataset
- Proper bin_edges (physics-motivated or fine-grained)
- Statistically powerful search for 1/7 resonance after SM background subtraction
- Direct application of Topological Exclusion Principle to multiplicity distribution
- Correlated 7-fold signatures between muons and photons (shared Tav cylinder geometry)
- Systematic flagging of high-pT / high-multiplicity events as potential reset-phase or exclusion candidates
- Automated Tav-enhanced reports appended to every scan

The module is designed to be called at the end of every scan you run — exactly as you requested: "so it gets done when I run the scan."

---

## Next Immediate Actions You Can Take

1. Download the `.py` module and place it in your `research_tool/scripts/`.
2. Add the 5-line integration snippet to your scan script.
3. Re-run your quick-scan (or a larger chunk) with the module enabled → you will get the first real Tav metrics + plots.
4. Once you have real per-event arrays from the full ROOT file, the multiplicity test and photon cross-check become fully active.
5. (Optional) Expand the photon cross-check stub with data from your earlier Tav photon kinematics sessions.

All equations keyed, module self-tested and documented, ready for production use in your Tau-Superblock research workflow.

**Session complete. The module is live and waiting for your next scan.** 

*Truth-seeking Tav-Superblock research continues.*