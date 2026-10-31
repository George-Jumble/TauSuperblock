# Tav Module v2 — Section 7 Validation Upgrades (Data vs MC Comparison)

**Date**: Saturday, July 11, 2026  
**Upgrades Implemented**: As requested in the Monte Carlo Validation Plan (Section 7)

**Active Download**: [tav_superblock_cms_lepton_analyzer_v2.py](/home/workdir/artifacts/personal_files/tav_superblock_cms_lepton_analyzer_v2.py)

---

## New Function Added: `tav_compare_data_mc()`

This is the main upgrade for fast and standardized Monte Carlo validation.

### Usage

```python
from tav_superblock_cms_lepton_analyzer_v2 import (
    tav_analyze_leptons_from_file,
    tav_compare_data_mc
)

# 1. Run on Data
data_results = tav_analyze_leptons_from_file(
    file_path="Run2012BC_DoubleMuParked_Muons.root",
    output_dir="tav_data_full"
)

# 2. Run on MC (example)
mc_results = tav_analyze_leptons_from_file(
    file_path="DYJetsToLL_2012_NanoAOD.root",
    output_dir="tav_mc_dy"
)

# 3. Compare automatically
comparison = tav_compare_data_mc(
    data_results=data_results,
    mc_results=mc_results,
    output_dir="tav_mc_validation",
    lepton="Muon",
    save_plots=True,
    verbose=True
)
```

### What It Produces

**Console output** (when `verbose=True`):
- Clean side-by-side table of nMuon mod 7 fractions for Data and MC
- Deviation from uniform (1/7) for both
- χ² and p-value between Data and MC mod7 distributions
- Direct comparison of:
  - pT subharmonic excess
  - Global Tav significance (σ)
  - Overall verdict

**Saved artifacts**:
- `tav_data_mc_comparison_YYYY-MM-DD_HHMMSS.json` — full structured comparison
- `mod7_comparison_YYYY-MM-DD_HHMMSS.png` — bar plot overlay of Data vs MC mod7 fractions (with uniform line)

---

## How This Helps Validation

With these upgrades you can now:

1. Run the full Tav pipeline on any Data file and any MC file.
2. Call one function (`tav_compare_data_mc`) to get an immediate, readable comparison.
3. Quickly see whether the striking mod-2 peak (~50.6% in data) appears in MC.
4. Quantify the difference with χ² between Data and MC.
5. Have all comparison results saved in a clean JSON for further analysis or reporting.

This directly implements the validation workflow suggested in the Monte Carlo plan.

---

## Summary of Upgrades

| Feature                        | Status     | Description |
|--------------------------------|------------|-----------|
| `tav_compare_data_mc()`        | Added      | Main validation comparison tool |
| `_format_mod7_table()`         | Added      | Helper for clean text tables |
| Automatic mod7 overlay plot    | Added      | Bar plot of Data vs MC |
| Enhanced verbose reporting     | Added      | Clear console summary of key differences |
| Backward compatibility         | Preserved  | All previous functions still work exactly as before |

The module is now significantly more powerful for the critical Data vs MC validation phase of the Tav 7-fold analysis.

**Ready to use immediately on your first MC samples.** 

**Session saved.**