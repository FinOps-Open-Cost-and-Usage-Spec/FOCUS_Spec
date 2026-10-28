#!/usr/bin/env bash
# Build the semantic markup prototype outputs into build/.
#
#   1. Check the definitions in specification/ and generate the entity registry,
#      with the front matter snippets in samples/front_matter/ applied.
#   2. Lint the ORIGINAL BilledCost and ChargeClass files (legacy markup).
#   3. Resolve the semantic samples/ versions, joined with file markers the
#      way markdown-pp would join them, into Markdown and an HTML preview.
#   4. Diff the resolved Markdown against the original files.
#
# Set PYTHON to an interpreter with panflute installed (default: python3 on PATH).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SPEC="$HERE/../../specification"
BUILD="$HERE/build"
PYTHON="${PYTHON:-python3}"
FILTER="$HERE/focus_semantic.py"
COLS="datasets/cost_and_usage/columns"
FILES=(billedcost chargeclass)

mkdir -p "$BUILD"
# pandoc runs a .py filter with "python3" from PATH, so put $PYTHON's directory first
export PATH="$(dirname "$("$PYTHON" -c 'import sys; print(sys.executable)')"):$PATH"

# Front matter demo: prepend each samples/front_matter/ snippet to a fresh copy of the
# spec file at the same path, so the overlay never goes stale against specification/.
OVERLAY="$BUILD/overlay"
rm -rf "$OVERLAY"
(cd "$HERE/samples/front_matter" && find . -name '*.md') | while read -r rel; do
  mkdir -p "$OVERLAY/$(dirname "$rel")"
  cat "$HERE/samples/front_matter/$rel" "$SPEC/$rel" > "$OVERLAY/$rel"
done

echo "== Definition checks and registry =="
"$PYTHON" "$HERE/build_registry.py" --spec-dir "$SPEC" --overlay "$OVERLAY" --out "$BUILD/registry.json" \
  2>&1 | tee "$BUILD/definition-checks.txt"
META=(-M "focus-registry=$BUILD/registry.json")

echo
echo "== Lint of the original (legacy) files =="
for f in "${FILES[@]}"; do
  pandoc -f gfm -t gfm -F "$FILTER" "${META[@]}" -M "focus-file=$COLS/$f.md" \
    "$SPEC/$COLS/$f.md" -o /dev/null 2>&1 | tee "$BUILD/lint-original-$f.txt"
done

# Join the semantic samples with file markers, as a patched markdown-pp would.
COMBINED="$BUILD/combined.md"
: > "$COMBINED"
for f in "${FILES[@]}"; do
  printf '<!-- focus:file %s/%s.md -->\n\n' "$COLS" "$f" >> "$COMBINED"
  cat "$HERE/samples/$f.md" >> "$COMBINED"
  printf '\n' >> "$COMBINED"
done

echo
echo "== Lint of the semantic samples =="
pandoc -f gfm -t gfm -F "$FILTER" "${META[@]}" -M focus-strict=true \
  "$COMBINED" -o "$BUILD/resolved.md" 2>&1 | tee "$BUILD/lint-semantic.txt"

# Same source, three renderings. The preview inlines its CSS and script so it is one file.
{ printf '<style>\n'; cat "$HERE/preview.css"; printf '</style>\n'; cat "$HERE/preview-head.html"; } > "$BUILD/head.html"
pandoc -f gfm -t html -s -F "$FILTER" "${META[@]}" -M focus-annotate=true \
  --metadata pagetitle="Semantic markup preview" -H "$BUILD/head.html" \
  "$COMBINED" -o "$BUILD/preview.html" 2>/dev/null
for f in "${FILES[@]}"; do
  pandoc -f gfm -t gfm -F "$FILTER" "${META[@]}" -M focus-link-mode=source \
    -M "focus-file=$COLS/$f.md" "$HERE/samples/$f.md" -o "$BUILD/$f.source-links.md" 2>/dev/null
done

echo
echo "== Resolved output vs. hand-written original =="
"$PYTHON" - "$BUILD/resolved.md" "$BUILD" <<'EOF'
import re, sys
from pathlib import Path
text = Path(sys.argv[1]).read_text()
build = Path(sys.argv[2])
for chunk in re.split(r"(?m)^(?=# )", text):
    if chunk.strip():
        name = chunk.split("\n", 1)[0][2:].replace(" ", "").lower()
        (build / f"{name}.resolved.md").write_text(chunk.rstrip() + "\n")
EOF
for f in "${FILES[@]}"; do
  pandoc -f gfm -t gfm "$SPEC/$COLS/$f.md" -o "$BUILD/$f.original.md"
  diff -u "$BUILD/$f.original.md" "$BUILD/$f.resolved.md" --label "original/$f.md" --label "resolved/$f.md" \
    > "$BUILD/$f.diff" || true
  echo "$f: $(grep -c '^[-+][^-+]' "$BUILD/$f.diff" || true) changed lines (build/$f.diff)"
done
