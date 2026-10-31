#!/usr/bin/env python3
"""
TSB Casimir Test Framework
Implements statistical tests for the 5 novel TSB (Tav/Superblock) predictions
against standard Casimir/Lifshitz equations.

Predictions tested:
1. Discrete thresholds & hysteresis in tunable force (vs smooth Lifshitz)
2. Arrow-of-time / dissipative asymmetry in dynamic Casimir (vs symmetric)
3. Hierarchical scale-dependent modulations vs separation (vs smooth power-law)
4. Domain multiplicity anisotropy + emergent gravity back-reaction (vs isotropic short-range)
5. Non-local topological correlations in multi-cavity systems (vs local/weak)

Usage:
- python TSB_Casimir_Test_Framework.py --data path/to/data.csv --param_col B --value_col F
- Or load example Zenodo/GitHub datasets (modify loaders)

Requires: pandas, numpy, scipy, matplotlib (available in environment)
"""

import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.stats import chi2, norm
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = "tsb_test_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==================== COMPLETE KEY TO VARIABLES ====================
"""
Global variables and functions used in tests:
- df: pandas DataFrame with Casimir data
- param_col: str, e.g. 'magnetic_field_mT' or 'separation_nm'
- value_col: str, e.g. 'force_pN'
- x, y: numpy arrays of sorted parameter and force values
- dy: first differences (for step detection)
- freqs, power: from periodogram (for periodicity)
- peaks: indices of significant peaks
- p_value: statistical significance (lower = more evidence for TSB feature)
- TSB vs Standard: Standard = smooth Lifshitz prediction; TSB = discrete/periodic/asymmetric features
"""

def load_data(file_path: str) -> pd.DataFrame:
    """Load and standardize Casimir CSV data."""
    df = pd.read_csv(file_path)
    col_map = {
        'B': 'magnetic_field_mT', 'B_mT': 'magnetic_field_mT',
        'F': 'force_pN', 'Force': 'force_pN',
        'd': 'separation_nm', 'distance': 'separation_nm',
        'time': 'time_s'
    }
    df = df.rename(columns={k: v for k, v in col_map.items() if k in df.columns})
    return df

def detect_steps(x: np.ndarray, y: np.ndarray, threshold_sigma: float = 2.0):
    """Test for discrete steps (Prediction 1). Returns step locations and p-value."""
    dy = np.diff(y)
    std_dy = np.std(dy)
    step_mask = np.abs(dy) > threshold_sigma * std_dy
    step_indices = np.where(step_mask)[0]
    n_steps = len(step_indices)
    
    # Simple significance: binomial test against expected random fluctuations
    expected_steps = len(dy) * 0.05  # ~5% false positive under null
    p_value = 1 - norm.cdf((n_steps - expected_steps) / np.sqrt(expected_steps))
    return step_indices, p_value, n_steps

def test_periodicity(x: np.ndarray, y: np.ndarray):
    """Test for 7-phase / 1/7 harmonic periodicity (Predictions 1 & 5)."""
    if len(x) < 20:
        return None, 1.0
    sort_idx = np.argsort(x)
    x_clean = x[sort_idx]
    y_clean = y[sort_idx]
    
    # Periodogram
    fs = 1.0 / np.mean(np.diff(x_clean))
    freqs, power = signal.periodogram(y_clean, fs=fs)
    
    # Look for peaks near expected 1/7 harmonics (heuristic)
    peaks, _ = signal.find_peaks(power, height=np.max(power)*0.2)
    if len(peaks) == 0:
        return None, 1.0
    
    dominant_freq = freqs[peaks[np.argmax(power[peaks])]]
    period = 1.0 / dominant_freq if dominant_freq > 0 else np.inf
    
    # Rough p-value using chi2 for peak power
    p_value = 1 - chi2.cdf(np.max(power), df=2)  # approximate
    return period, p_value

def test_hysteresis(x: np.ndarray, y: np.ndarray):
    """Test for hysteresis/asymmetry (Prediction 2)."""
    if len(y) < 10:
        return 0.0, 1.0
    mid = len(y) // 2
    diff = np.mean(np.abs(y[:mid] - y[mid:][::-1]))
    std_y = np.std(y)
    effect_size = diff / std_y if std_y > 0 else 0
    p_value = 1 - norm.cdf(effect_size)  # rough
    return effect_size, p_value

def test_log_modulations(x: np.ndarray, y: np.ndarray):
    """Test for hierarchical Δn modulations in log-d (Prediction 3)."""
    pos_mask = x > 0
    if np.sum(pos_mask) < 10:
        return None, 1.0
    log_x = np.log10(x[pos_mask])
    y_pos = y[pos_mask]
    
    def sin_model(t, a, f, p, c):
        return a * np.sin(2 * np.pi * f * t + p) + c
    
    try:
        p0 = [np.std(y_pos), 1/7, 0, np.mean(y_pos)]
        popt, _ = curve_fit(sin_model, log_x, y_pos, p0=p0, maxfev=5000)
        fitted_freq = popt[1]
        residuals = y_pos - sin_model(log_x, *popt)
        chi2_val = np.sum((residuals / np.std(residuals))**2)
        p_value = 1 - chi2.cdf(chi2_val, df=len(y_pos)-4)
        return fitted_freq, p_value
    except:
        return None, 1.0

def test_anisotropy_or_backreaction(x: np.ndarray, y: np.ndarray):
    """Placeholder for anisotropy/back-reaction test (Prediction 4)."""
    # In real data with angle or large-d: fit extra term
    # Here: simple check for deviation from pure power-law at large x
    if len(x) < 10:
        return 0.0, 1.0
    log_x = np.log(x)
    log_y = np.log(np.abs(y) + 1e-10)
    slope, _ = np.polyfit(log_x, log_y, 1)
    deviation = abs(slope + 4)  # expect ~ -4 for Casimir
    p_value = 1 - norm.cdf(deviation)
    return deviation, p_value

def run_full_test_suite(df: pd.DataFrame, param_col: str = None, value_col: str = None):
    """Run all 5 TSB falsification tests and generate report."""
    if param_col is None or value_col is None:
        numeric = df.select_dtypes(include=[np.number]).columns.tolist()
        param_col = next((c for c in numeric if any(k in c.lower() for k in ['b','field','d','sep'])), numeric[0])
        value_col = next((c for c in numeric if any(k in c.lower() for k in ['f','force'])), numeric[1] if len(numeric)>1 else numeric[0])
    
    x = df[param_col].values
    y = df[value_col].values
    mask = ~np.isnan(x) & ~np.isnan(y)
    x, y = x[mask], y[mask]
    sort_idx = np.argsort(x)
    x, y = x[sort_idx], y[sort_idx]
    
    results = {}
    
    # Test 1: Discrete steps
    step_idx, p_steps, n_steps = detect_steps(x, y)
    results['discrete_steps'] = {'n_steps': n_steps, 'p_value': p_steps, 'evidence_for_TSB': p_steps < 0.05}
    
    # Test 2: Hysteresis / asymmetry
    effect_hyst, p_hyst = test_hysteresis(x, y)
    results['hysteresis'] = {'effect_size': effect_hyst, 'p_value': p_hyst, 'evidence_for_TSB': p_hyst < 0.05}
    
    # Test 3: Periodicity (1/7)
    period, p_period = test_periodicity(x, y)
    results['periodicity'] = {'dominant_period': period, 'p_value': p_period, 'evidence_for_TSB': p_period < 0.05}
    
    # Test 4: Log modulations (hierarchical)
    freq_log, p_log = test_log_modulations(x, y)
    results['log_modulations'] = {'fitted_frequency': freq_log, 'p_value': p_log, 'evidence_for_TSB': p_log < 0.05}
    
    # Test 5: Anisotropy / back-reaction (simplified)
    dev, p_dev = test_anisotropy_or_backreaction(x, y)
    results['anisotropy_backreaction'] = {'deviation_from_-4': dev, 'p_value': p_dev, 'evidence_for_TSB': p_dev < 0.05}
    
    # Generate summary plot
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    axes[0].plot(x, y, 'b.-', alpha=0.7)
    axes[0].set_title(f"Raw Data ({param_col} vs {value_col})")
    axes[0].set_xlabel(param_col)
    axes[0].set_ylabel(value_col)
    
    # Steps
    axes[1].plot(x[1:], np.diff(y), 'r.-')
    for idx in step_idx:
        axes[1].axvline(x[idx], color='green', linestyle='--', alpha=0.5)
    axes[1].set_title("Derivative + Detected Steps")
    
    # Periodogram
    if len(x) > 20:
        freqs, power = signal.periodogram(y)
        axes[2].semilogy(freqs, power)
        axes[2].set_title("Periodogram (look for 1/7 harmonics)")
    
    # Hysteresis placeholder
    axes[3].text(0.5, 0.5, f"Hysteresis effect: {effect_hyst:.3f}\np={p_hyst:.3g}", 
                 transform=axes[3].transAxes, ha='center', va='center')
    axes[3].set_title("Hysteresis Test")
    axes[3].axis('off')
    
    # Log modulations
    if len(x) > 10 and np.all(x > 0):
        log_x = np.log10(x)
        axes[4].plot(log_x, y, 'g.-')
        axes[4].set_title("Log-scale Data (check modulations)")
    
    # Summary
    summary_text = "\n".join([f"{k}: p={v['p_value']:.3g} {'(TSB evidence)' if v['evidence_for_TSB'] else ''}" 
                              for k, v in results.items()])
    axes[5].text(0.1, 0.5, summary_text, transform=axes[5].transAxes, fontsize=9, va='center')
    axes[5].set_title("TSB Falsification Summary")
    axes[5].axis('off')
    
    plt.tight_layout()
    plot_path = os.path.join(OUTPUT_DIR, "tsb_falsification_report.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    
    print("\n=== TSB Casimir Falsification Test Report ===")
    for test, res in results.items():
        print(f"{test}: p={res['p_value']:.4g} | Evidence for TSB: {res['evidence_for_TSB']}")
    print(f"\nPlot saved to: {plot_path}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="TSB Casimir Test Framework")
    parser.add_argument("--data", type=str, default=None, help="Path to Casimir CSV")
    parser.add_argument("--param_col", type=str, default=None)
    parser.add_argument("--value_col", type=str, default=None)
    args = parser.parse_args()
    
    if args.data:
        df = load_data(args.data)
        run_full_test_suite(df, args.param_col, args.value_col)
    else:
        print("No data provided. Example usage:")
        print("python TSB_Casimir_Test_Framework.py --data your_casimir_data.csv --param_col magnetic_field_mT --value_col force_pN")
        print("\nRecommended public datasets:")
        print("- Zenodo superconducting Casimir data (large zip with CSVs)")
        print("- GitHub magnetic fluid prediction datasets")

if __name__ == "__main__":
    main()