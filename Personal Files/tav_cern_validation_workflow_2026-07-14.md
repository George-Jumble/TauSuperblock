# Session: Tav CERN 7-Fold Analysis – Validation Tool Workflow Question

**Session Date**: Tuesday, July 14, 2026 12:22 AM EDT  
**Project**: Tau-Superblock Universe / Tav Topology Validation against Collider Data  
**Related Prior Session**: `photon_kinematics_analysis_tav_cylinder_2026-07-13.md` (includes full CMS 7-Fold Muon Tav Analysis JSON results)  
**Core Question**: Does the validation tool need to be run directly on the data that the CERN data is run on, or just the output of the scan?

---

## Direct Answer

**The validation tool should be run on just the output of the scan** (the JSON summary, histograms, and generated plots), **not** directly on the raw CERN data for routine validation.

This is the efficient, reproducible, and standard workflow for analyses of this type.

---

## Detailed Rationale (in Context of Your Tav Analysis Pipeline)

From the structure of the provided CMS 7-Fold Muon Tav Analysis JSON (timestamp 07-14-2026_011706), your "scan" script already performs the core data processing:

- It accesses and processes the CERN CMS data (likely NanoAOD, custom ntuples, or similar).
- Applies event selections, computes mod7 observables (unweighted and pileup-weighted histograms).
- Calculates key Tav-relevant metrics: `subharmonic_excess`, `chi2_vs_uniform`, `pvalue`, `pt_subharmonic_excess`, `harmonic_hit_count`, Lorentz factor anchors, etc.
- Compares data vs MC (`data_subharmonic_excess` vs `mc_subharmonic_excess`).
- Performs dependence studies (pileup, isolation ID, topology).
- Outputs reduced artifacts: JSON report + PNG plots (referenced in `dependence_studies`).

**Why validation belongs on the scan output, not raw data**:

1. **Computational Efficiency**  
   CERN CMS datasets are enormous (often petabytes across campaigns). Re-accessing and re-processing raw or even MiniAOD/NanoAOD files for every validation iteration is prohibitively expensive in CPU, storage I/O, and wall time. The scan reduces everything to lightweight JSON + small plot files.

2. **Reproducibility & Iteration Speed**  
   Once the scan has run and produced its JSON (with all histograms, weights, verdicts, and MC comparisons baked in), the validation tool can run in seconds on a laptop. You can tweak validation criteria, add new statistical tests, or run toys without touching the original data.

3. **Separation of Concerns**  
   - **Scan** = primary analysis engine (selection, binning, weighting, basic excess/chi² calculation).  
   - **Validation tool** = post-processing layer (statistical closure, systematic variations, p-value calibration, cross-checks against Tav predictions like 1/7 resonance and 313.1 MeV geometric friction floor).

4. **The JSON Already Embeds Validation Elements**  
   Your current output already includes:
   - Direct data vs MC comparison of subharmonic excess (both 0.0 in this run).
   - `mc_strong_7fold: false`
   - Dependence studies with explicit plot paths.
   - `verdict: "NO CLEAR 7-FOLD SIGNATURE"` and `"UNDERPOWERED"` for multiplicity.
   - `chi2_vs_uniform: 42.0`, `pvalue ≈ 1.84e-7` (driven by tiny sample of only 7 events all in one mod-7 bin).

   These are precisely the kinds of quantities a validation tool would inspect or extend.

5. **Tav Framework Alignment**  
   The 7-fold search tests concrete predictions from the Tau Cylinder (8-phase clockwork, 1/7 resonance, 142857 cycle) and Topological Exclusion Principle (phase-domain occupancy rules).  
   The scan already anchors to `m0_mev_anchor: 313.1` and `tav_harmonic_ratio: 0.142857...`.  
   Validation should therefore focus on whether the *derived observables* (mod7 fractions, subharmonic excess, dependence on pileup/isolation) are consistent with Tav expectations — something best done on the scan's summarized output.

---

## When You *Might* Still Need Direct Data Access

- Initial development/debugging of the scan script itself (run on small validation samples or MC subsets).
- Full end-to-end closure tests on a brand-new dataset release.
- When adding entirely new observables that the original scan did not compute.
- Systematic uncertainty evaluation that requires re-weighting or re-selecting at the event level (in which case you would re-run a modified scan, not a separate validation tool).

For **routine validation** after a successful scan — the answer is clearly: **just the output of the scan**.

---

## Recommended Updated Workflow

1. **Scan stage** (already done in your JSON example)  
   Run the main analysis script on CERN data → produces:
   - `cern_analysis__data_analysis_tav_7fold_muon__report__*.json`
   - Dependence study PNG plots
   - Any intermediate histograms (ROOT/pickle)

2. **Validation stage** (new/recommended)  
   Run validation tool **on the JSON + plots** from step 1.  
   Tasks it can perform:
   - Recompute or refine p-values with toy MC.
   - Check stability of `subharmonic_excess` under different pileup bins or isolation working points.
   - Compare against Tav-predicted benchmarks (e.g., expected 1/7 fractions, 313.1 MeV scale implications).
   - Generate validation report with pass/fail criteria tied to the Topological Exclusion Principle and 8-phase engine.
   - Archive everything together.

3. **Archival**  
   Both scan output and validation output go into the session folder under `artifacts/cern_analysis/`.

This matches the structure already visible in your JSON (`run_dir`, `report_path`, `dependence_studies` with plot paths).

---

## Reference to Previous Session Results

From the JSON analyzed in `photon_kinematics_analysis_tav_cylinder_2026-07-13.md`:

- **Current verdict**: NO CLEAR 7-FOLD SIGNATURE (underpowered sample).
- All 7 events fell into a single mod-7 bin → expected statistical fluctuation for tiny statistics.
- No subharmonic excess detected in pT spectrum.
- MC also shows no strong 7-fold.

A validation tool running on this output could quantify whether this null result is consistent with Tav expectations (given the low event count) or whether it motivates a larger dedicated photon/jet/multiplicity search.

---

**Session saved to Personal Files folder in Tau-Superblock Universe project**

**Active Downloadable Link**:

[Download tav_cern_validation_workflow_2026-07-14.md](/home/workdir/artifacts/personal_files/tav_cern_validation_workflow_2026-07-14.md)

*(Live path — direct download from chat interface. All prior session files remain available in the same Personal Files folder.)*

This session record includes the complete answer, workflow recommendation, and ties back to the Tav Cylinder / Topological Exclusion Principle predictions being tested by the CERN analysis. 

Ready for implementation of the validation tool or the next data scan. Provide more details on what the validation tool currently does (or should do) if you want a code sketch or further refinements.