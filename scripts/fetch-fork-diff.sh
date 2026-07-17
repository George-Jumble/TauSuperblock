#!/usr/bin/env bash
# fetch-fork-diff.sh
#
# Extract changed code from a fork without downloading the whole fork.
#
# USAGE
#   ./scripts/fetch-fork-diff.sh <fork-remote-url> [fork-branch] [upstream-branch]
#
# ARGUMENTS
#   fork-remote-url   Git remote URL of the fork (HTTPS or SSH)
#   fork-branch       Branch on the fork to inspect        (default: main)
#   upstream-branch   Local branch to compare against      (default: main)
#
# EXAMPLES
#   # Diff against your local main using the GitHub compare/patch URL approach
#   ./scripts/fetch-fork-diff.sh https://github.com/other-user/TauSuperblock.git
#
#   # Compare a specific branch on the fork
#   ./scripts/fetch-fork-diff.sh https://github.com/other-user/TauSuperblock.git dev main
#
# WHAT IT DOES (mirrors the 5-step plan)
#   Step 1 – Identify the fork branch/commit range
#   Step 2 – Export a .patch file from the GitHub compare view (no clone needed)
#   Step 3 – Targeted shallow fetch of only the fork branch/tip (minimal data)
#   Step 4 – List files changed vs. upstream and extract those paths
#   Step 5 – Offer sparse-checkout of selected directories/files (optional)
#
# REQUIREMENTS
#   git ≥ 2.25 (partial clone / blob filtering)
#   curl        (for Step 2 GitHub patch export)
#   Optional: gh CLI for Step 2 when the remote is a GitHub repo

set -euo pipefail

# ---------------------------------------------------------------------------
# Args / defaults
# ---------------------------------------------------------------------------
FORK_URL="${1:?Usage: $0 <fork-remote-url> [fork-branch] [upstream-branch]}"
FORK_BRANCH="${2:-main}"
UPSTREAM_BRANCH="${3:-main}"

FORK_REMOTE_NAME="fork-tmp-$$"          # temporary remote name (cleaned up on exit)
OUTPUT_DIR="artifacts/fork-diff-$$"    # where patch + file list are written

mkdir -p "$OUTPUT_DIR"

cleanup() {
    git remote remove "$FORK_REMOTE_NAME" 2>/dev/null || true
}
trap cleanup EXIT

echo "=== Step 1: Identify fork branch / commit range ==="
echo "Fork URL    : $FORK_URL"
echo "Fork branch : $FORK_BRANCH"
echo "Compare with: $UPSTREAM_BRANCH (local)"
echo ""

# ---------------------------------------------------------------------------
# Step 2 – Patch/diff export from GitHub compare view
#           Works when both sides live on GitHub and the fork URL ends in .git
# ---------------------------------------------------------------------------
echo "=== Step 2: Export .patch from GitHub compare view (no clone) ==="

PATCH_FILE="$OUTPUT_DIR/fork.patch"

# Derive the GitHub compare URL when the fork is a github.com repo.
# Pattern:  https://github.com/{owner}/{repo}.git  →  owner/repo
if [[ "$FORK_URL" =~ github\.com[:/]([^/]+)/([^/.]+)(\.git)?$ ]]; then
    FORK_OWNER="${BASH_REMATCH[1]}"
    FORK_REPO="${BASH_REMATCH[2]}"

    # Try to infer the upstream owner from origin remote (best-effort)
    UPSTREAM_REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
    if [[ "$UPSTREAM_REMOTE_URL" =~ github\.com[:/]([^/]+)/([^/.]+)(\.git)?$ ]]; then
        UPSTREAM_OWNER="${BASH_REMATCH[1]}"
        UPSTREAM_REPO="${BASH_REMATCH[2]}"
    else
        UPSTREAM_OWNER="$FORK_OWNER"
        UPSTREAM_REPO="$FORK_REPO"
    fi

    COMPARE_PATCH_URL="https://github.com/${UPSTREAM_OWNER}/${UPSTREAM_REPO}/compare/${UPSTREAM_BRANCH}...${FORK_OWNER}:${FORK_REPO}:${FORK_BRANCH}.patch"
    echo "Fetching : $COMPARE_PATCH_URL"

    HTTP_STATUS=$(curl -sL -o "$PATCH_FILE" -w "%{http_code}" "$COMPARE_PATCH_URL")
    if [[ "$HTTP_STATUS" == "200" ]] && [[ -s "$PATCH_FILE" ]]; then
        echo "Patch saved → $PATCH_FILE"
        PATCH_OK=true
    else
        echo "Note: GitHub compare URL returned HTTP $HTTP_STATUS (repo may be private or URL differs)."
        echo "Falling back to git fetch for diff generation."
        PATCH_OK=false
        rm -f "$PATCH_FILE"
    fi
else
    echo "Fork is not a github.com URL — skipping HTTP patch export."
    PATCH_OK=false
fi

# ---------------------------------------------------------------------------
# Step 3 – Targeted shallow fetch (single branch, no blobs until needed)
#           Uses partial-clone blob filter to keep download minimal.
# ---------------------------------------------------------------------------
echo ""
echo "=== Step 3: Targeted shallow fetch of fork tip ==="

git remote add "$FORK_REMOTE_NAME" "$FORK_URL"

# Fetch only the tip commit of the fork branch, filtering blobs (treeless).
# This means commit/tree objects arrive but file contents are lazy-loaded.
git fetch \
    --no-tags \
    --depth=1 \
    --filter=blob:none \
    "$FORK_REMOTE_NAME" \
    "${FORK_BRANCH}:refs/remotes/${FORK_REMOTE_NAME}/${FORK_BRANCH}"

FORK_COMMIT=$(git rev-parse "refs/remotes/${FORK_REMOTE_NAME}/${FORK_BRANCH}")
echo "Fork tip commit : $FORK_COMMIT"

UPSTREAM_COMMIT=$(git rev-parse "$UPSTREAM_BRANCH" 2>/dev/null || git rev-parse "origin/$UPSTREAM_BRANCH")
echo "Upstream commit : $UPSTREAM_COMMIT"

# ---------------------------------------------------------------------------
# Step 4 – List changed files and extract their paths
# ---------------------------------------------------------------------------
echo ""
echo "=== Step 4: List files changed vs. upstream ==="

CHANGED_FILES_LIST="$OUTPUT_DIR/changed-files.txt"
git diff --name-only "$UPSTREAM_COMMIT" "$FORK_COMMIT" > "$CHANGED_FILES_LIST"

CHANGED_COUNT=$(wc -l < "$CHANGED_FILES_LIST" | tr -d ' ')
echo "Changed files ($CHANGED_COUNT) → $CHANGED_FILES_LIST"
echo ""
cat "$CHANGED_FILES_LIST"

# If no patch yet (non-GitHub or private repo), generate one from the fetch
if [[ "$PATCH_OK" != "true" ]]; then
    echo ""
    echo "Generating patch from fetched objects …"
    git diff "$UPSTREAM_COMMIT" "$FORK_COMMIT" > "$PATCH_FILE"
    echo "Patch saved → $PATCH_FILE"
fi

# ---------------------------------------------------------------------------
# Step 5 – (Optional) Sparse-checkout of selected paths
#           Materialises the actual file contents for chosen paths only.
# ---------------------------------------------------------------------------
echo ""
echo "=== Step 5: (Optional) Sparse-checkout of selected paths ==="
echo ""
echo "To materialise the contents of specific changed files from the fork:"
echo ""
echo "  # In a fresh worktree (keeps your working tree clean):"
echo "  git worktree add /tmp/fork-worktree $FORK_COMMIT --detach"
echo "  git -C /tmp/fork-worktree sparse-checkout set \$(cat $CHANGED_FILES_LIST)"
echo ""
echo "Or, to extract a single file's content from the fork tip:"
echo "  git show ${FORK_COMMIT}:<path/to/file>"
echo ""
echo "Done.  Artefacts written to: $OUTPUT_DIR"
echo "  Patch file   : $PATCH_FILE"
echo "  Changed files: $CHANGED_FILES_LIST"
