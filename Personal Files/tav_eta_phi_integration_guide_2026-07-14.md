# Integration Guide: Adding Muon_eta and Muon_phi to the Tav Validation Pipeline

**Session Date**: Tuesday, July 14, 2026 10:07 AM EDT  
**Question**: How do I integrate the `Muon_eta` and `Muon_phi` branches into the validation pipeline so that `scan_pt_thresholds_with_recoil_cuts()` (and geometric floor isolation) can run?

**Answer**: Use the new helper `extract_dimuon_kinematics()` + graceful failure handling already built into the module.

---

## 1. Minimal Integration Pattern (Recommended)

Add this at the top of your TAV ENGINE data-loading phase (or inside the enhanced validation call):

```python
from tav_superblock_cms_validation_enhanced_v2 import (
    extract_dimuon_kinematics,
    scan_pt_thresholds_with_recoil_cuts,
    tav_enhanced_validation_suite
)

# === Phase: Load dimuon kinematics (eta + phi required) ===
events = uproot.open(data_file)["Events"]   # or your existing loader

# Extract per-event dimuon kinematics (leading two muons)
dimuon_kinematics = extract_dimuon_kinematics(events)

if dimuon_kinematics is None:
    # Graceful failure exactly as requested
    validation_report["geometric_floor_scan"] = {
        "status": "GEOMETRIC_FLOOR_SCAN_FAILED",
        "reason": "missing required branches: Muon_eta and/or Muon_phi",
        "recommendation": "Re-skim with Muon_eta and Muon_phi branches included. "
                          "Standard 7-fold pT + multiplicity analysis will still run."
    }
else:
    # Proceed with geometric floor isolation
    geometric_results = scan_pt_thresholds_with_recoil_cuts(
        data_events=dimuon_kinematics,
        pt_thresholds=np.array([0,10,20,30,40,50,60,70,80,90,
                                100,110,120,130,140,150,160,170,180,190,200]),
        angular_cuts={
            "delta_phi_min": 2.5,      # tight back-to-back suppression
            "delta_r_max": 0.8,        # collimated pairs (geometric leakage)
            "recoil_pt_max": 15.0      # low recoil = minimal SM activity
        },
        winding_rate_params={
            "omega_wind": 1.45e43,
            "kappa_leak": 0.01,
            "rho_aeon": 1.0,
            "R": 7.0,
            "I": 1.0
        },
        track_winding_rate=True
    )
    validation_report["geometric_floor_scan"] = geometric_results
```

---

## 2. What `extract_dimuon_kinematics()` Does

It safely checks for the required branches (`Muon_pt`, `Muon_eta`, `Muon_phi`) and, if present, returns a clean list of dicts with:

- `leading_pt`, `subleading_pt`
- `delta_phi` (folded 0–π)
- `delta_r`
- `recoil_pt` (vector sum pT of the dimuon system)
- `n_muon`

If any required branch is missing, it returns `None` → triggers `GEOMETRIC_FLOOR_SCAN_FAILED` exactly as you specified.

---

## 3. Full Graceful Failure Behavior (Already Implemented)

When `Muon_eta` or `Muon_phi` are missing, the report will contain:

```json
{
  "geometric_floor_scan": {
    "status": "GEOMETRIC_FLOOR_SCAN_FAILED",
    "reason": "missing required branches: Muon_eta and/or Muon_phi",
    "recommendation": "Ensure the dimu skim contains Muon_eta and Muon_phi. "
                      "The standard 7-fold pT/multiplicity analysis can still run."
  }
}
```

The rest of the pipeline (classic 7-fold pT + multiplicity, enhanced v2 amplitude, pileup reweighting, etc.) continues normally.

---

## 4. Files

**Updated module** (contains `extract_dimuon_kinematics()` + `scan_pt_thresholds_with_recoil_cuts()` with graceful failure):  
**Download tav_superblock_cms_validation_enhanced_v2.py**

**This integration guide**:  
**Download tav_eta_phi_integration_guide_2026-07-14.md**

---

**Summary**:  
Just call `extract_dimuon_kinematics(events)` early in your data-loading phase. If the branches exist, the geometric floor scan runs automatically with winding-rate tracking. If they are missing, you get a clean `GEOMETRIC_FLOOR_SCAN_FAILED` flag and the rest of the validation continues.

This is the minimal, robust way to integrate `Muon_eta` and `Muon_phi` into the full Tav pipeline while preserving backward compatibility with existing histogram-based runs.

Ready to test on the next skim that includes the angular branches. Let me know when you have it and I’ll help generate the exact execution command.