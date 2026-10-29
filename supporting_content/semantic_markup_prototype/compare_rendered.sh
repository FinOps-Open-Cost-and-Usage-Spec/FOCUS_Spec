#!/usr/bin/env bash
# Compare how the specification publishes before and after semantic tagging
# (migration step 3). Builds the assembled spec.md for a base git ref and for
# the working tree, then lists every changed line word by word.
#
# Usage: compare_rendered.sh [BASE_REF]
#   (default: where this branch left origin/working_draft, so later changes to
#   working_draft do not show up as differences)
#
# Writes build/compare/{base,current}-spec.md and build/compare/changes.txt.
# Set PYTHON to an interpreter with panflute installed (default: python3 on PATH).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/../.." && pwd)"
BASE_REF="${1:-$(git -C "$REPO" merge-base HEAD origin/working_draft)}"
OUT="$HERE/build/compare"
PYTHON="${PYTHON:-python3}"
mkdir -p "$OUT"
export PATH="$(dirname "$("$PYTHON" -c 'import sys; print(sys.executable)')"):$PATH"

assemble() {  # $1 = checkout root, $2 = output file
  (cd "$1/specification" &&
     cp versions/working_draft.md version.md &&
     PYTHONPATH=../vendored/ "$PYTHON" ../vendored/bin/markdown-pp spec.mdpp -o "$2.raw")
}

# Base: a temporary worktree at BASE_REF, assembled as that ref builds it
BASE_DIR="$(mktemp -d)"
trap 'git -C "$REPO" worktree remove --force "$BASE_DIR" >/dev/null 2>&1 || true' EXIT
git -C "$REPO" worktree add --detach --quiet "$BASE_DIR" "$BASE_REF"
assemble "$BASE_DIR" "$OUT/base-spec.md"
if [ -f "$BASE_DIR/supporting_content/semantic_markup_prototype/resolve_semantic.py" ] &&
   grep -q 'focus:begin' "$OUT/base-spec.md.raw"; then
  (cd "$BASE_DIR/specification" &&
     "$PYTHON" ../supporting_content/semantic_markup_prototype/build_registry.py --spec-dir . --out "$OUT/base-registry.json" 2>/dev/null &&
     "$PYTHON" ../supporting_content/semantic_markup_prototype/resolve_semantic.py --registry "$OUT/base-registry.json" \
       "$OUT/base-spec.md.raw" -o "$OUT/base-spec.md")
else
  mv "$OUT/base-spec.md.raw" "$OUT/base-spec.md"
fi

# Current: the working tree, assembled and resolved as `make spec.md` does
assemble "$REPO" "$OUT/current-spec.md"
(cd "$REPO/specification" &&
   "$PYTHON" "$HERE/build_registry.py" --spec-dir . --out "$OUT/current-registry.json" 2>/dev/null &&
   "$PYTHON" "$HERE/resolve_semantic.py" --registry "$OUT/current-registry.json" \
     "$OUT/current-spec.md.raw" -o "$OUT/current-spec.md")
rm -f "$OUT"/*.raw

"$PYTHON" - "$OUT/base-spec.md" "$OUT/current-spec.md" <<'EOF' | tee "$OUT/changes.txt"
import difflib, re, sys
a = open(sys.argv[1]).read().splitlines()
b = open(sys.argv[2]).read().splitlines()
heading = ""
headings_b = {}
for n, line in enumerate(b):
    if line.startswith("#"):
        heading = line.lstrip("#").strip()
    headings_b[n] = heading
changed = 0
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if tag == "equal":
        continue
    if i2 - i1 != j2 - j1:
        print(f"line {i1 + 1}: {tag} {i2 - i1} line(s) -> {j2 - j1} line(s)")
        changed += 1
        continue
    for k, (x, y) in enumerate(zip(a[i1:i2], b[j1:j2])):
        changed += 1
        where = f"line {j1 + k + 1} ({headings_b.get(j1 + k, '')})"
        if x.split() == y.split():
            print(f"{where}: whitespace only")
            continue
        wa, wb = x.split(), y.split()
        parts = [f"'{' '.join(wa[p1:p2])}' -> '{' '.join(wb[q1:q2])}'"
                 for t, p1, p2, q1, q2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes()
                 if t != "equal"]
        print(f"{where}: " + " | ".join(parts))
print(f"{changed} changed line(s) between {sys.argv[1].rsplit('/', 1)[-1]} and {sys.argv[2].rsplit('/', 1)[-1]}")
EOF
