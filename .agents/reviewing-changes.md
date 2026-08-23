# Reviewing Specification Changes

Instructions for reviewing pull requests and specification changes. AI agents reviewing content MUST act as strict technical editors enforcing the FOCUS standards.

When evaluating specification content, apply all content rules in `.agents/writing-specification.md`. The rules below govern how findings are reported.

## Review Conduct

* **Suggestion-first feedback:** When a concrete fix exists, post it as a GitHub `suggestion` block so the author can accept with one click. Use plain-text comments only when the feedback requires discussion rather than a specific replacement.
* **Self-contained comments:** Every review comment or suggestion MUST include all context needed for the author to evaluate it independently. Do not reference other comments (e.g., "same as above" or "see my comment on line X").
* **Diff-scope discipline:** Only flag issues on lines changed or added by the PR. Pre-existing problems are out of scope unless they create a direct inconsistency with new content in the same PR.
* **Deduplication:** If your tooling can read PR threads, do not flag already-raised issues or post competing suggestions. To add details, reply to the existing thread.
* **BCP-14 rule applicability:** When the BCP-14 keyword location rule does not apply, continue applying all other relevant Markdown, editorial, example-accuracy, and review-conduct rules.
