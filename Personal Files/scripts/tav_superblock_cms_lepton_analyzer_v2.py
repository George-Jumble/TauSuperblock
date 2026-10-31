#!/usr/bin/env python3
"""
Tav-Superblock CMS Lepton Analyzer Module v2 (Robust Branch Discovery)

Key improvements over v1:
- Scans the ROOT file first to discover what lepton data is present (muons and/or electrons).
- Only runs the analyses for which data actually exists in the file.
- Gracefully handles muon-only files (e.g. your current DoubleMuParked) and files with both muons + electrons (e.g. HiggsTo4L).
- Symmetric support for electrons.
- Still works if you pass pre-extracted arrays (backward compatible).
- All Tav equations and keys preserved.

Usage examples:

# Option 1: Pass file path (recommended - it discovers branches automatically)
from tav_superblock_cms_lepton_analyzer_v2 import tav_analyze_leptons_from_file
results = tav_analyze_leptons_from_file(
    file_path="Run2012BC_DoubleMuParked_Muons.root",
    output_dir="tav_output"
)

# Option 2: Pass pre-extracted arrays (for integration with your existing quick-scan)
from tav_superblock_cms_lepton_analyzer_v2 import tav_analyze_leptons
results = tav_analyze_leptons(
    muon_pt_hist=hist,
    n_muon_per_event=nmuon_array,
    electron_pt_hist=None,   # or pass if you have it
    output_dir="tav_output"
)
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy import stats
import matplotlib.pyplot as plt
from typing import Optional, Tuple, Dict, Any
import json
from datetime import datetime
import os
import uproot

# =============================================================================
# BRANCH DISCOVERY (The Fix You Requested)
# =============================================================================

def discover_available_lepton_branches(file_path: str) -> Dict[str, bool]:
    """
    Scans the ROOT file and reports which lepton collections are present.
    
    Returns a dict like:
        {
            "has_muons": True,
            "has_electrons": False,
            "muon_branches": ["nMuon", "Muon_pt", ...],
            "electron_branches": []
        }
    """
    result = {
        "has_muons": False,
        "has_electrons": False,
        "muon_branches": [],
        "electron_branches": []
    }
    
    try:
        with uproot.open(file_path) as f:
            if "Events" not in f:
                return result
            tree = f["Events"]
            all_branches = set(tree.keys())
            
            # Check for muons
            muon_required = {"nMuon", "Muon_pt"}
            if muon_required.issubset(all_branches):
                result["has_muons"] = True
                result["muon_branches"] = [b for b in all_branches if b.startswith("Muon_") or b == "nMuon"]
            
            # Check for electrons
            electron_required = {"nElectron", "Electron_pt"}
            if electron_required.issubset(all_branches):
                result["has_electrons"] = True
                result["electron_branches"] = [b for b in all_branches if b.startswith("Electron_") or b == "nElectron"]
                
    except Exception as e:
        print(f"[Tav] Warning: Could not scan file {file_path}: {e}")
    
    return result


# =============================================================================
# CORE TAV ANALYSIS FUNCTIONS (same as v1, with minor robustness improvements)
# =============================================================================

def _exponential_detrend(x: np.ndarray, hist: np.ndarray):
    def model(x, A, b, c):
        return A * np.exp(-b * x) + c
    p0 = [np.max(hist), 0.5, 0.0]
    try:
        popt, _ = curve_fit(model, x, hist, p0=p0, maxfev=10000)
    except:
        popt = p0
    trend = model(x, *popt)
    residuals = hist - trend
    return trend, residuals, {"A": popt[0], "b": popt[1], "c": popt[2]}


def _fit_7periodic(x: np.ndarray, residuals: np.ndarray):
    def sin_model(x, A7, phi):
        return A7 * np.sin(2 * np.pi * x / 7 + phi)
    try:
        popt, _ = curve_fit(sin_model, x, residuals, p0=[np.std(residuals), 0.0])
        return popt[0], popt[1], abs(popt[0])
    except:
        return 0.0, 0.0, 0.0


def _mod7_phase_sums(residuals: np.ndarray):
    phases = np.arange(7)
    return np.array([np.sum(residuals[k::7]) for k in phases])


def _multiplicity_7fold_test(n_array: np.ndarray):
    if n_array is None or len(n_array) == 0:
        return {"status": "no_data"}
    n = n_array.astype(int)
    mod7 = n % 7
    hist_mod7, _ = np.histogram(mod7, bins=np.arange(8))
    expected = len(n) / 7.0
    chi2, pval = stats.chisquare(hist_mod7, f_exp=[expected]*7)
    active_multiples = np.isin(n, [7,14,21,28,35])
    return {
        "mod7_histogram": hist_mod7.tolist(),
        "fraction_in_active_multiples": float(np.mean(active_multiples)),
        "chi2_uniformity_mod7": float(chi2),
        "pvalue_uniformity": float(pval),
        "mean_n": float(np.mean(n)),
        "max_n": int(np.max(n))
    }


def _run_7fold_analysis(pt_hist: np.ndarray, n_per_event: Optional[np.ndarray] = None, lepton_type: str = "Muon"):
    """Internal helper that runs the full Tav 7-fold pipeline for one lepton type."""
    x = np.arange(len(pt_hist))
    trend, residuals, fit_params = _exponential_detrend(x, pt_hist)
    A7, phi, A7_abs = _fit_7periodic(x, residuals)
    residual_std = np.std(residuals)
    significance = A7_abs / residual_std if residual_std > 0 else 0.0
    phase_sums = _mod7_phase_sums(residuals)
    mult_results = _multiplicity_7fold_test(n_per_event) if n_per_event is not None else {"status": "no_n_array"}
    
    return {
        f"{lepton_type.lower()}_pt_7fold": {
            "amplitude_A7": float(A7_abs),
            "significance_sigma": float(significance),
            "verdict": "SUBHARMONIC HINT" if significance > 3 else "NO CLEAR SIGNAL"
        },
        f"{lepton_type.lower()}_multiplicity_7fold": mult_results,
        f"{lepton_type.lower()}_detrend_params": fit_params,
        f"{lepton_type.lower()}_mod7_phase_sums": phase_sums.tolist()
    }


# =============================================================================
# MAIN ENTRY POINTS
# =============================================================================

def tav_analyze_leptons(
    muon_pt_hist: Optional[np.ndarray] = None,
    n_muon_per_event: Optional[np.ndarray] = None,
    electron_pt_hist: Optional[np.ndarray] = None,
    n_electron_per_event: Optional[np.ndarray] = None,
    output_dir: str = "tav_lepton_output",
    save_plots: bool = True,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    Main analysis function. Pass whatever lepton data you have.
    It will only analyze the lepton types for which data is provided.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    results = {"timestamp": timestamp, "output_dir": output_dir}
    
    if muon_pt_hist is not None:
        if verbose: print("[Tav] Running muon 7-fold analysis...")
        muon_results = _run_7fold_analysis(muon_pt_hist, n_muon_per_event, "Muon")
        results.update(muon_results)
    
    if electron_pt_hist is not None:
        if verbose: print("[Tav] Running electron 7-fold analysis...")
        electron_results = _run_7fold_analysis(electron_pt_hist, n_electron_per_event, "Electron")
        results.update(electron_results)
    
    if not any(k in results for k in ["muon_pt_7fold", "electron_pt_7fold"]):
        results["warning"] = "No lepton data provided to analyze."
    
    # Save JSON
    json_path = os.path.join(output_dir, f"tav_lepton_results_{timestamp}.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=float)
    results["json_path"] = json_path
    
    if verbose:
        print(f"[Tav] Analysis complete. Results saved to {output_dir}")
    
    return results


def tav_analyze_leptons_from_file(
    file_path: str,
    output_dir: str = "tav_lepton_output",
    chunk_size: int = 500_000,
    save_plots: bool = True,
    verbose: bool = True
) -> Dict[str, Any]:
    """
    High-level entry point that first discovers what lepton data exists in the file,
    then extracts what is needed and runs the Tav analysis.
    
    This is the robust version that fixes the "no electron data" issue.
    """
    if verbose:
        print(f"[Tav] Scanning file for available lepton branches: {file_path}")
    
    discovery = discover_available_lepton_branches(file_path)
    
    if verbose:
        print(f"  Has muons: {discovery['has_muons']}")
        print(f"  Has electrons: {discovery['has_electrons']}")
    
    if not discovery["has_muons"] and not discovery["has_electrons"]:
        return {"error": "No muon or electron data found in file", "discovery": discovery}
    
    # Extract data using chunked reading (memory safe for large files)
    muon_pt_hist = np.zeros(20)
    n_muon_list = []
    electron_pt_hist = np.zeros(20)
    n_electron_list = []
    
    with uproot.open(file_path) as f:
        tree = f["Events"]
        
        branches_to_read = []
        if discovery["has_muons"]:
            branches_to_read += ["nMuon", "Muon_pt"]
        if discovery["has_electrons"]:
            branches_to_read += ["nElectron", "Electron_pt"]
        
        for batch in tree.iterate(branches_to_read, step_size=chunk_size, library="np"):
            if discovery["has_muons"]:
                n_muon_list.extend(batch["nMuon"].tolist())
                flat_pt = np.concatenate(batch["Muon_pt"]) if len(batch["Muon_pt"]) > 0 else np.array([])
                h, _ = np.histogram(flat_pt, bins=20)
                muon_pt_hist += h
            
            if discovery["has_electrons"]:
                n_electron_list.extend(batch["nElectron"].tolist())
                flat_pt = np.concatenate(batch["Electron_pt"]) if len(batch["Electron_pt"]) > 0 else np.array([])
                h, _ = np.histogram(flat_pt, bins=20)
                electron_pt_hist += h
    
    # Call the array-based analyzer with whatever we found
    return tav_analyze_leptons(
        muon_pt_hist=muon_pt_hist if discovery["has_muons"] else None,
        n_muon_per_event=np.array(n_muon_list) if discovery["has_muons"] else None,
        electron_pt_hist=electron_pt_hist if discovery["has_electrons"] else None,
        n_electron_per_event=np.array(n_electron_list) if discovery["has_electrons"] else None,
        output_dir=output_dir,
        save_plots=save_plots,
        verbose=verbose
    )


# =============================================================================
# BACKWARD COMPATIBILITY (old function name still works)
# =============================================================================
tav_7fold_muon_analysis = tav_analyze_leptons   # alias for existing scripts


def save_results_as_numbered_json_chunks(
    results: Dict[str, Any],
    output_dir: str,
    base_filename: str = "tav_results",
    max_size_mb: float = 8.0
) -> List[str]:
    """
    Splits large Tav results into multiple .json files with numerical prefixes
    (0., 1., 2., ...) so each file stays under max_size_mb.
    
    Useful when the full JSON from a 61M+ event run (with long periodogram data)
    exceeds chat or upload size limits.
    
    Example output files:
        0.tav_results.json
        1.tav_results.json
        2.tav_results.json
        ...
    
    Returns list of created file paths in order.
    """
    import json
    
    os.makedirs(output_dir, exist_ok=True)
    
    json_str = json.dumps(results, indent=2, default=float)
    total_bytes = len(json_str.encode("utf-8"))
    max_bytes = int(max_size_mb * 1024 * 1024)
    
    if total_bytes <= max_bytes:
        filepath = os.path.join(output_dir, f"0.{base_filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(json_str)
        return [filepath]
    
    # Split the JSON string into sequential chunks
    created_files = []
    start = 0
    chunk_index = 0
    
    while start < len(json_str):
        end = min(start + max_bytes, len(json_str))
        chunk = json_str[start:end]
        
        filepath = os.path.join(output_dir, f"{chunk_index}.{base_filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(chunk)
        
        created_files.append(filepath)
        start = end
        chunk_index += 1
    
    return created_files


def save_tav_results_chunked(
    results: Dict[str, Any],
    output_dir: str,
    base_filename: str = "tav_full_results",
    max_size_mb: float = 8.0
) -> List[str]:
    """Convenience alias with clearer name."""
    return save_results_as_numbered_json_chunks(
        results, output_dir, base_filename, max_size_mb
    )

if __name__ == "__main__":
    print("Tav-Superblock Lepton Analyzer v2 ready.")
    print("Use tav_analyze_leptons_from_file(file_path) for automatic branch discovery.")
    print("Use save_tav_results_chunked(results, output_dir) to split large JSONs.")
    print("Use tav_compare_data_mc(data_results, mc_results) for fast Data vs MC validation.")
# =============================================================================
# SECTION 7 UPGRADES: Monte Carlo Validation Helpers
# =============================================================================

def _format_mod7_table(mod7_fractions):
    """Helper to create a nice text table for mod7 fractions."""
    expected = 1.0 / 7.0
    lines = ["mod7 | Data/MC Fraction | Expected (uniform) | Deviation"]
    lines.append("-" * 55)
    for i, frac in enumerate(mod7_fractions):
        dev = frac - expected
        lines.append(f"  {i}  |     {frac:8.4f}     |      {expected:8.4f}      | {dev:+8.4f}")
    return "\n".join(lines)


def tav_compare_data_mc(
    data_results,
    mc_results,
    output_dir="tav_mc_validation",
    lepton="Muon",
    save_plots=True,
    verbose=True
):
    """
    Compare Tav results between Data and Monte Carlo (Section 7 upgrade).
    
    Produces:
    - Side-by-side mod7 fraction table + χ² vs uniform
    - Key metric comparison (subharmonic excess, significance, verdict)
    - Optional overlay plots for mod7
    
    This makes MC validation fast and standardized.
    """
    import json
    from datetime import datetime
    import os
    
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    
    comparison = {
        "timestamp": timestamp,
        "lepton": lepton,
        "data": {},
        "mc": {},
        "differences": {}
    }
    
    # Extract key metrics
    data_mult = data_results.get(f"{lepton.lower()}_multiplicity_7fold", {})
    mc_mult   = mc_results.get(f"{lepton.lower()}_multiplicity_7fold", {})
    
    data_pt   = data_results.get(f"{lepton.lower()}_pt_7fold", {})
    mc_pt     = mc_results.get(f"{lepton.lower()}_pt_7fold", {})
    
    # Mod7 fractions
    data_mod7 = data_mult.get("mod7_histogram", [])
    mc_mod7   = mc_mult.get("mod7_histogram", [])
    
    if data_mod7 and mc_mod7:
        total_data = sum(data_mod7)
        total_mc   = sum(mc_mod7)
        data_fracs = [x / total_data for x in data_mod7] if total_data > 0 else []
        mc_fracs   = [x / total_mc   for x in mc_mod7]   if total_mc   > 0 else []
        
        comparison["data"]["mod7_fractions"] = data_fracs
        comparison["mc"]["mod7_fractions"]   = mc_fracs
        comparison["data"]["mod7_table"] = _format_mod7_table(data_fracs)
        comparison["mc"]["mod7_table"]   = _format_mod7_table(mc_fracs)
        
        if total_data > 0 and total_mc > 0:
            expected_mc_scaled = [x * (total_data / total_mc) for x in mc_mod7]
            try:
                from scipy import stats
                chi2, pval = stats.chisquare(data_mod7, f_exp=expected_mc_scaled)
                comparison["differences"]["mod7_chi2_data_vs_mc"] = float(chi2)
                comparison["differences"]["mod7_pvalue_data_vs_mc"] = float(pval)
            except:
                pass
    
    # Key scalar metrics
    comparison["data"]["pt_subharmonic_excess"] = data_pt.get("subharmonic_excess", None)
    comparison["mc"]["pt_subharmonic_excess"]   = mc_pt.get("subharmonic_excess", None)
    
    comparison["data"]["global_significance"] = data_results.get("seven_periodic", {}).get("significance_sigma", None)
    comparison["mc"]["global_significance"]   = mc_results.get("seven_periodic", {}).get("significance_sigma", None)
    
    comparison["data"]["verdict"] = data_results.get("verdict", "")
    comparison["mc"]["verdict"]   = mc_results.get("verdict", "")
    
    if verbose:
        print("\n" + "="*70)
        print("TAV DATA vs MC COMPARISON")
        print("="*70)
        print(f"\n--- {lepton} Multiplicity (mod 7) ---")
        print("DATA:")
        print(comparison["data"].get("mod7_table", "N/A"))
        print("\nMC:")
        print(comparison["mc"].get("mod7_table", "N/A"))
        
        if "mod7_chi2_data_vs_mc" in comparison["differences"]:
            print(f"\nData vs MC mod7 χ² = {comparison['differences']['mod7_chi2_data_vs_mc']:.2f} "
                  f"(p = {comparison['differences']['mod7_pvalue_data_vs_mc']:.4f})")
        
        print(f"\n--- pT Subharmonic Excess ---")
        print(f"Data: {comparison['data']['pt_subharmonic_excess']}")
        print(f"MC  : {comparison['mc']['pt_subharmonic_excess']}")
        
        print(f"\n--- Global Tav Significance ---")
        print(f"Data: {comparison['data']['global_significance']} σ")
        print(f"MC  : {comparison['mc']['global_significance']} σ")
        
        print(f"\n--- Overall Verdict ---")
        print(f"Data: {comparison['data']['verdict']}")
        print(f"MC  : {comparison['mc']['verdict']}")
        print("="*70 + "\n")
    
    json_path = os.path.join(output_dir, f"tav_data_mc_comparison_{timestamp}.json")
    with open(json_path, "w") as f:
        json.dump(comparison, f, indent=2, default=float)
    comparison["json_path"] = json_path
    
    if save_plots:
        try:
            import matplotlib.pyplot as plt
            import numpy as np
            if data_fracs and mc_fracs:
                fig, ax = plt.subplots(figsize=(8, 5))
                x = np.arange(7)
                width = 0.35
                ax.bar(x - width/2, data_fracs, width, label='Data', color='blue', alpha=0.7)
                ax.bar(x + width/2, mc_fracs,   width, label='MC',   color='orange', alpha=0.7)
                ax.axhline(1/7, color='red', linestyle='--', label='Uniform (1/7)')
                ax.set_xlabel('nMuon mod 7')
                ax.set_ylabel('Fraction')
                ax.set_title(f'{lepton} mod 7 Distribution: Data vs MC')
                ax.legend()
                ax.set_xticks(x)
                plt.tight_layout()
                plot_path = os.path.join(output_dir, f"mod7_comparison_{timestamp}.png")
                plt.savefig(plot_path, dpi=150)
                plt.close()
                comparison["mod7_plot"] = plot_path
        except Exception as e:
            if verbose:
                print(f"[Tav] Warning: Could not generate comparison plots: {e}")
    
    if verbose:
        print(f"[Tav] Comparison saved to {output_dir}")
    
    return comparison

