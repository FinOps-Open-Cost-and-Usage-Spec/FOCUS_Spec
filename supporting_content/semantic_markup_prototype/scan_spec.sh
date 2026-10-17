#!/usr/bin/env bash
# Run the semantic-reference lint over every Markdown source file in the
# specification and summarize the findings. This reproduces the spec-wide
# counts cited in issue #2779.
#
# The scan uses a registry built from specification/ alone (no front matter
# demo overlay), so the counts reflect the specification as it is.
#
# Writes build/spec-scan.txt (every finding) and prints a summary.
# Set PYTHON to an interpreter with panflute installed (default: python3 on PATH).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SPEC="$HERE/../../specification"
BUILD="$HERE/build"
PYTHON="${PYTHON:-python3}"
FILTER="$HERE/focus_semantic.py"
REGISTRY="$BUILD/spec-scan-registry.json"
OUT="$BUILD/spec-scan.txt"

mkdir -p "$BUILD"
export PATH="$(dirname "$("$PYTHON" -c 'import sys; print(sys.executable)')"):$PATH"

"$PYTHON" "$HERE/build_registry.py" --spec-dir "$SPEC" --out "$REGISTRY" >/dev/null 2>&1

cd "$SPEC"
: > "$OUT"
files=0
while IFS= read -r f; do
  files=$((files + 1))
  pandoc -f gfm -t gfm -F "$FILTER" -M "focus-registry=$REGISTRY" -M "focus-file=$f" "$f" -o /dev/null 2>>"$OUT"
done < <(find supported_features attributes appendix datasets metadata schemas operating_model_conditions \
           -name '*.md' | sort; printf '%s\n' glossary.md overview.md)

count() { grep -c "$1" "$OUT" || true; }
hard=$(count 'FOCUS007')
untagged=$(( $(count 'FOCUS004') + $(count 'FOCUS005') + $(count 'FOCUS006') ))
with_findings=$(grep 'FOCUS' "$OUT" | awk -F' § ' '{print $1}' | sort -u | wc -l | tr -d ' ')

echo "Scanned $files files; findings in $with_findings"
echo "Hard-coded entity links (FOCUS007):        $hard"
echo "  to columns and datasets (#datamodel...): $(grep FOCUS007 "$OUT" | grep -c '#datamodel' || true)"
echo "  to glossary terms (#glossary:...):       $(grep FOCUS007 "$OUT" | grep -c '#glossary:' || true)"
echo "Formatting-only references:                $untagged"
echo "  untagged ColumnIds (FOCUS004):           $(count 'FOCUS004')"
echo "  italic glossary terms (FOCUS005):        $(count 'FOCUS005')"
echo "  untagged display names (FOCUS006):       $(count 'FOCUS006')"
echo "Errors:                                    $(count ' ERROR ')"
echo "Details: $OUT"
