#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <base-ref> [container-image]" >&2
  exit 2
fi

issue_base_ref=$1
issue_image=${2:-localhost/focus-spec-build:2240}
issue_repo_root=$(git rev-parse --show-toplevel)
issue_work_dir="$issue_repo_root/.ai/work/2240-backticks-for-string-column-values"
issue_lint_base="$issue_work_dir/.lint-base"
issue_lint_output=$(mktemp -d /tmp/focus-2240-lint.XXXXXX)

cleanup() {
  rm -rf "$issue_lint_base" "$issue_lint_output"
}
trap cleanup EXIT

if [[ -e "$issue_lint_base" ]]; then
  echo "Temporary baseline path already exists: $issue_lint_base" >&2
  exit 1
fi

mkdir "$issue_lint_base"
git archive "$issue_base_ref" | tar -x -C "$issue_lint_base"
git diff --name-only "$issue_base_ref" -- '*.md' > "$issue_lint_output/paths.txt"

issue_current_paths=()
issue_base_paths=()
while IFS= read -r issue_path; do
  issue_current_paths+=("/workspace/current/$issue_path")
  issue_base_paths+=("/workspace/current/.ai/work/2240-backticks-for-string-column-values/.lint-base/$issue_path")
done < "$issue_lint_output/paths.txt"

set +e
podman run --rm \
  --platform linux/amd64 \
  --userns keep-id \
  --volume "$issue_repo_root:/workspace/current:ro" \
  --workdir /workspace/current/specification \
  "$issue_image" \
  python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan \
  "${issue_current_paths[@]}" > "$issue_lint_output/current.txt" 2>&1
issue_current_status=$?

podman run --rm \
  --platform linux/amd64 \
  --userns keep-id \
  --volume "$issue_repo_root:/workspace/current:ro" \
  --workdir /workspace/current/specification \
  "$issue_image" \
  python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan \
  "${issue_base_paths[@]}" > "$issue_lint_output/base.txt" 2>&1
issue_base_status=$?
set -e

if [[ "$issue_current_status" -gt 1 || "$issue_base_status" -gt 1 ]]; then
  cat "$issue_lint_output/current.txt" "$issue_lint_output/base.txt" >&2
  exit 1
fi

sed -n -E \
    's#^/workspace/current/([^:]+):([0-9]+):[0-9]+: ([A-Z0-9]+):.*#\1:\2:\3#p' \
    "$issue_lint_output/current.txt" \
  | sort > "$issue_lint_output/current.keys.txt"
sed -n -E \
    's#^/workspace/current/.ai/work/2240-backticks-for-string-column-values/.lint-base/([^:]+):([0-9]+):[0-9]+: ([A-Z0-9]+):.*#\1:\2:\3#p' \
    "$issue_lint_output/base.txt" \
  | sort > "$issue_lint_output/base.keys.txt"

comm -13 \
  "$issue_lint_output/base.keys.txt" \
  "$issue_lint_output/current.keys.txt" \
  > "$issue_lint_output/new.keys.txt"

issue_base_count=$(wc -l < "$issue_lint_output/base.keys.txt" | tr -d ' ')
issue_current_count=$(wc -l < "$issue_lint_output/current.keys.txt" | tr -d ' ')
issue_new_count=$(wc -l < "$issue_lint_output/new.keys.txt" | tr -d ' ')

printf 'Base diagnostics: %s; current diagnostics: %s; new diagnostics: %s\n' \
  "$issue_base_count" "$issue_current_count" "$issue_new_count"

if [[ "$issue_new_count" -ne 0 ]]; then
  cat "$issue_lint_output/new.keys.txt"
  exit 1
fi

issue_work_paths=()
while IFS= read -r issue_path; do
  issue_work_paths+=("/workspace/current/${issue_path#"$issue_repo_root/"}")
done < <(find "$issue_work_dir" -maxdepth 1 -type f -name '*.md' -print)

podman run --rm \
  --platform linux/amd64 \
  --userns keep-id \
  --volume "$issue_repo_root:/workspace/current:ro" \
  --workdir /workspace/current/specification \
  "$issue_image" \
  python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan \
  "${issue_work_paths[@]}"

echo "Issue working Markdown: clean"
