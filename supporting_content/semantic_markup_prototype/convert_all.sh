#!/usr/bin/env bash
# Convert every specification file the build includes to semantic tags
# (migration step 2, for the whole specification).
#
# Finds the files by assembling the specification with markdown-pp, which marks
# each included file, rebuilds the entity registry, and runs tag_sources.py over
# them. The script is idempotent: running it on converted files changes nothing.
#
# Skips the files that hold no references (version, license, contributors, and the
# abstract) and the .mdpp files that only list includes. schemas/schemas.mdpp has
# prose links, so it is converted too.
#
# Usage: convert_all.sh      (from any directory)
# Set PYTHON to an interpreter with panflute installed (default: python3 on PATH).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SPEC="$HERE/../../specification"
PYTHON="${PYTHON:-python3}"
export PATH="$(dirname "$("$PYTHON" -c 'import sys; print(sys.executable)')"):$PATH"

cd "$SPEC"
cp versions/working_draft.md version.md
PYTHONPATH=../vendored/ "$PYTHON" ../vendored/bin/markdown-pp spec.mdpp -o spec.semantic.md

list="$(mktemp)"
trap 'rm -f "$list"' EXIT
grep -o 'focus:begin [^ ]*' spec.semantic.md | sed 's/focus:begin //' | sort -u \
  | grep -E '\.md$' | grep -v -E '^(version|license|contributors|spec_abstract)\.md$' > "$list"
echo schemas/schemas.mdpp >> "$list"

"$PYTHON" "$HERE/build_registry.py" --spec-dir . --out semantic-registry.json > /dev/null 2>&1
echo "Converting $(wc -l < "$list" | tr -d ' ') files"
mkdir -p "$HERE/build"
xargs "$PYTHON" "$HERE/tag_sources.py" --registry semantic-registry.json < "$list" > "$HERE/build/convert-run.txt" 2>&1

echo "Tagged $(grep -c 'reference(s) tagged' "$HERE/build/convert-run.txt") files; $(grep -c NEEDS-REVIEW "$HERE/build/convert-run.txt") items need a decision"
echo "Details: $HERE/build/convert-run.txt"
