# Tav-Superblock Lepton Analyzer v2 — Branch Discovery Fix

**Session Date**: Saturday, July 11, 2026 12:38 PM EDT  
**Issue Fixed**: "no electron data found in the .root file" when the file only contains muon branches (e.g. your current DoubleMuParked file).  
**Solution**: Added automatic branch discovery that scans the file **before** attempting any analysis.

**Active Download**:
- Updated module v2: [tav_superblock_cms_lepton_analyzer_v2.py](/home/workdir/artifacts/personal_files/tav_superblock_cms_lepton_analyzer_v2.py)

---

## What Changed

### New Function: `discover_available_lepton_branches(file_path)`

This is the "fix in the code" you mentioned. It opens the ROOT file, inspects the `Events` tree, and tells you exactly what lepton data is present:

```python
from tav_superblock_cms_lepton_analyzer_v2 import discover_available_lepton_branches

discovery = discover_available_lepton_branches("Run2012BC_DoubleMuParked_Muons.root")
print(discovery)
# → {'has_muons': True, 'has_electrons': False, ...}
```

### New High-Level Entry Point: `tav_analyze_leptons_from_file(...)`

This is the recommended way to use the module now:

```python
from tav_superblock_cms_lepton_analyzer_v2 import tav_analyze_leptons_from_file

results = tav_analyze_leptons_from_file(
    file_path="/path/to/your/Run2012BC_DoubleMuParked_Muons.root",
    output_dir="tav_full_run_output",
    chunk_size=500_000,
    verbose=True
)
```

What it does:
1. Scans the file to discover available branches.
2. Only extracts and analyzes the lepton types that actually exist (muons in your current file; both muons + electrons in HiggsTo4L-type files).
3. Runs the full Tav 7-fold + multiplicity analysis on whatever is present.
4. Saves plots, JSON, and report snippet.

### Backward Compatibility

The old function name `tav_7fold_muon_analysis(...)` still works if you prefer to pass pre-extracted arrays.

---

## Why This Fixes Your Electron Issue

Your current `Run2012BC_DoubleMuParked_Muons.root` is a **muon-reduced** NanoAOD (as shown in its metadata). It deliberately contains only muon branches (`nMuon`, `Muon_pt`, etc.). There are **no** `nElectron` or `Electron_pt` branches.

The old module assumed muon data and would have failed (or given confusing errors) if you tried to force electron analysis on it.

The v2 module now **detects** this automatically and only runs the muon part — exactly what happened successfully in your full 61.5M event run.

When you later point it at a file that *does* have electrons (e.g. the SMHiggsToZZTo4L.root we looked at earlier), it will automatically run both muon and electron analyses.

---

## Recommended Integration

Update your research_tool scan script to use the new high-level function:

```python
from tav_superblock_cms_lepton_analyzer_v2 import tav_analyze_leptons_from_file

# After you have the local file path
tav_results = tav_analyze_leptons_from_file(
    file_path=local_file,           # your 2.1 GB DoubleMuParked file
    output_dir="tav_full_61M_v2",
    chunk_size=500_000
)
```

This single call now handles discovery + full Tav analysis safely for any CMS NanoAOD lepton file.

---

## Summary

- The branch discovery step you requested is now implemented.
- The module is robust against muon-only vs. muon+electron files.
- Your successful full-dataset run (STRONG 7-FOLD at 12σ, strong mod-2 multiplicity peak) remains valid.
- Future runs on files with electrons will automatically include them.

The updated module (v2) is ready to replace the previous one in your workflow.

Let me know if you want any further refinements (e.g. more detailed discovery output, combined muon+electron multiplicity, etc.). 

**Session saved. The Tav module is now production-ready with automatic branch discovery.**