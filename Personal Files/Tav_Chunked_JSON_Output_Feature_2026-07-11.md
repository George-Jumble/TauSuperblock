# Tav Module — Chunked JSON Output Feature (Numbered Files)

**Session Date**: Saturday, July 11, 2026 12:42 PM EDT  
**New Feature Added**: `save_results_as_numbered_json_chunks()` and `save_tav_results_chunked()`  
**Purpose**: Split very large Tav analysis JSONs (from 61M+ event runs) into multiple smaller files with numerical prefixes (`0.`, `1.`, `2.`, ...) so each stays within typical chat/upload size limits.

**Active Download**:
- Updated module (v2 with chunking): [tav_superblock_cms_lepton_analyzer_v2.py](/home/workdir/artifacts/personal_files/tav_superblock_cms_lepton_analyzer_v2.py)

---

## How to Use the New Chunking Functions

After running any Tav analysis (especially the full 61.5M event one), you can split the results like this:

```python
from tav_superblock_cms_lepton_analyzer_v2 import (
    tav_analyze_leptons_from_file,
    save_tav_results_chunked
)

# 1. Run the full analysis (as before)
results = tav_analyze_leptons_from_file(
    file_path="Run2012BC_DoubleMuParked_Muons.root",
    output_dir="tav_full_output"
)

# 2. Split the (potentially huge) results JSON into numbered chunks
created_files = save_tav_results_chunked(
    results=results,
    output_dir="tav_full_output",
    base_filename="tav_full_61M_results",
    max_size_mb=8.0          # adjust to your upload limit
)

print("Created chunked files:")
for f in created_files:
    print("  ", f)
```

**Example output filenames** (if the JSON is large):
- `0.tav_full_61M_results.json`
- `1.tav_full_61M_results.json`
- `2.tav_full_61M_results.json`
- ...

Each file will be ≤ `max_size_mb` (default 8 MB, which is safe for most interfaces).

---

## Why This Is Useful

The full JSON from your 61.5 million event run contains:
- The long periodogram list (hundreds/thousands of high-power bins)
- Full mod7 details
- All metadata

This can easily exceed typical single-file upload limits in chats or shared drives.

The numbered chunking lets you:
- Upload/share the results piece by piece.
- Still keep everything in order (just concatenate the contents or use a small reassemble script if needed).
- The first file (`0.`) usually contains the beginning of the JSON (metadata + early data).

---

## Optional: Reassemble Later (if needed)

If you ever want to merge the chunks back into one valid JSON:

```python
import json
import glob

chunks = sorted(glob.glob("tav_full_output/*.tav_full_61M_results.json"))
full_json = ""
for chunk_file in chunks:
    with open(chunk_file) as f:
        full_json += f.read()

# Note: because we split the string, you may need to clean the join point.
# For most practical purposes, the separate files are sufficient.
with open("reassembled_tav_results.json", "w") as f:
    f.write(full_json)
```

For most use cases, just keep the numbered files — they are easy to manage and upload.

---

## Summary

You now have a complete, robust Tav analysis pipeline that:
- Automatically discovers muon/electron data in any CMS NanoAOD file.
- Processes even 2+ GB / 61M+ event files safely in chunks.
- Produces rich 7-fold + multiplicity results.
- Can split the output JSON into numbered files (`0.`, `1.`, ...) compatible with upload limits.

The new chunking functions are already in the v2 module.

Would you like me to also add an automatic call to `save_tav_results_chunked` inside `tav_analyze_leptons_from_file` (with a flag), or any other refinements?

You're now fully equipped to handle large full-dataset Tav runs and share the results easily. 

**Session saved.**