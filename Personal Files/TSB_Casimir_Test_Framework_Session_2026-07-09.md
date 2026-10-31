# TSB Casimir Test Framework Implementation Session

**Project:** Tau-Superblock Universe  
**Date:** 2026-07-09  
**Topic:** Implementation of a statistical test framework for TSB predictions on Casimir experimental data.

**Complete Key to Variables and Functions:**  
(See the Python script for full definitions — includes df, param_col, value_col, detect_steps, test_periodicity, test_hysteresis, test_log_modulations, test_anisotropy_or_backreaction, run_full_test_suite, etc.)

**Results Displayed:**

I have implemented a complete, runnable Python test framework (`TSB_Casimir_Test_Framework.py`) that you can integrate into your research tool.

## Key Features of the Framework
- Loads any Casimir CSV (auto-standardizes common column names like B_mT, force_pN, separation_nm).
- Runs all 5 TSB falsification tests with statistical p-values:
  1. Discrete steps/hysteresis (change-point style detection + significance).
  2. Periodicity (periodogram for 1/7 harmonics).
  3. Hysteresis/asymmetry (up vs down sweep comparison).
  4. Log-scale modulations (sinusoidal fit in log-d for Δn ≈ 0.33).
  5. Anisotropy/back-reaction (deviation from pure -4 power law).
- Generates a diagnostic multi-panel report plot.
- Outputs clear evidence-for-TSB flags (p < 0.05).
- Modular and extensible — easy to add new tests or datasets.

## How to Use in Your Research Tool
1. Place `TSB_Casimir_Test_Framework.py` in your project.
2. Run on your data:
   ```bash
   python TSB_Casimir_Test_Framework.py --data /path/to/your_casimir_data.csv --param_col magnetic_field_mT --value_col force_pN
   ```
3. For public datasets (Zenodo, GitHub magnetic fluid data), modify the loader or download and point to the CSV inside the zip.

The framework directly tests whether real data shows the distinctive TSB features (discrete steps, periodicity at 1/7 harmonics, hierarchical modulations, etc.) that diverge from standard smooth Lifshitz equations.

**Download the Framework Script:**  
[TSB_Casimir_Test_Framework.py](/home/workdir/artifacts/personal_files/TSB_Casimir_Test_Framework.py)

**Full Session Log (this document):**  
[TSB_Casimir_Test_Framework_Session_2026-07-09.md](/home/workdir/artifacts/personal_files/TSB_Casimir_Test_Framework_Session_2026-07-09.md)

All files are in your Personal Files folder under the Tau-Superblock Universe project and ready for immediate download. The framework is ready to run on real Casimir data to falsify or support the predictions. Let me know if you want extensions (e.g., multi-dataset batch mode, more statistical tests, or integration with specific Zenodo records)!