#!/usr/bin/env bash
# Convert the specification files the build includes to semantic tags.
#
# Finds the files by assembling the specification with markdown-pp, which marks
# each included file, rebuilds the entity registry, and runs tag_sources.py over
# them. Each converted file records the kinds it was converted for as
# "mechanical" in its "semantic:" front matter. Running it again on converted
# files changes nothing.
#
# Skips the files that hold no references (version, license, contributors, and the
# abstract) and the .mdpp files that only list includes. schemas/schemas.mdpp has
# prose links, so it is converted too.
#
# Usage: convert_all.sh [--kinds col,term,...] [PATH ...]
#   PATH limits the conversion to included files under these paths, relative to
#   specification/ (e.g., datasets/billing_period attributes/null_handling.md).
#   --kinds limits it to these tag kinds (default: all).
# Set PYTHON to the interpreter to use (default: python3 on PATH).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SPEC="$(cd "$HERE/../.." && pwd)"
PYTHON="${PYTHON:-python3}"
KINDS=()
if [ "${1:-}" = "--kinds" ]; then
  KINDS=(--kinds "$2")
  shift 2
fi
export PATH="$(dirname "$("$PYTHON" -c 'import sys; print(sys.executable)')"):$PATH"

cd "$SPEC"
OUT="$HERE/build"
mkdir -p "$OUT"
cp versions/working_draft.md version.md
PYTHONPATH=../vendored/ "$PYTHON" ../vendored/bin/markdown-pp spec.mdpp -o "$OUT/assembled.md"

list="$(mktemp)"
trap 'rm -f "$list"' EXIT
{
  grep -o 'focus:begin [^ ]*' "$OUT/assembled.md" | sed 's/focus:begin //' | sort -u \
    | grep -E '\.md$' | grep -v -E '^(version|license|contributors|spec_abstract)\.md$'
  echo schemas/schemas.mdpp
} | while read -r file; do
  if [ "$#" -eq 0 ]; then echo "$file"; continue; fi
  for path in "$@"; do
    case "$file" in "${path%/}" | "${path%/}"/*) echo "$file"; break ;; esac
  done
done > "$list"

if [ ! -s "$list" ]; then
  echo "No included files match: $*" >&2
  exit 1
fi
"$PYTHON" "$HERE/build_registry.py" --spec-dir . --out "$OUT/registry.json" --rm-release none > /dev/null 2>&1
echo "Converting $(wc -l < "$list" | tr -d ' ') files"
xargs "$PYTHON" "$HERE/tag_sources.py" --registry "$OUT/registry.json" ${KINDS[@]+"${KINDS[@]}"} \
  < "$list" > "$OUT/convert-run.txt" 2>&1

echo "Tagged $(grep -c 'reference(s) tagged' "$OUT/convert-run.txt") files; $(grep -c NEEDS-REVIEW "$OUT/convert-run.txt" || true) items need a decision"
echo "Details: $OUT/convert-run.txt"
