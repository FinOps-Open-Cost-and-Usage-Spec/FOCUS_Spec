# Plan

1. Fix a pre-change base commit and inventory every Markdown path tracked by that commit without modifying source files.
2. Classify candidates using repository-derived entity IDs and explicit value contexts.
3. Record a human-reviewable apply or skip decision and rationale for every occurrence.
4. Apply only approved replacements, preserving code syntax, JSON, property names, non-string values, format notation, and ordinary quotations.
5. Verify the base-to-worktree source changes exactly match the applied manifest, regardless of staging or commit state.
6. Regenerate the baseline and residual inventories and verify complete decision coverage.
7. Run classifier tests, Markdown linting, requirements-model tests, whitespace checks, and the full specification build.
8. Preserve the scanner, tests, manifests, validators, Linux/amd64 Podman recipe, and human workflow checkpoints for PR review.
