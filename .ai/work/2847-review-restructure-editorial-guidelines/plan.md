# Plan: Review of the Editorial Guidelines Restructuring, Step 1

## Scope

* Only `supporting_content/guidelines/contributors/editorial-guidelines-restructuring-step-1.md`.
* Not in scope: `guidelines/contributors/editorial-guidelines.md` and `AGENTS.md` as changed by PR #2848, the NRG, and the specification fixes the rules imply.

## Approach

1. Raise the purpose and status of the step-1 document as the first finding (F-00).
2. Map all 78 rule IDs of the Editorial Guidelines Review to the step-1 document and back (`research.md`, Traceability Matrix).
3. Irena is the editor; this review supports her. Her text is kept as is everywhere (`research.md`, How Findings Were Judged):
   * No issue: `<!-- review: In agreement. -->`.
   * Issue (gap, ambiguity, conflict, duplicate, self-violation): `review(F-xx) [Type]` comment with the problem, the verdict status and an Alternative.
   * Open assumption: `review(F-xx) [Open]` comment with the question; no wording imposed.
   * Already in the PR #2848 Follow-ups: raised only where a step-1 "absorbs" comment is not carried out.
4. Insert the comments only; `git diff 82996ef2` must show added comment or blank lines and nothing else.
5. Verify: diff shape, rule IDs, comment syntax, characters, linter.

## Delivery

* Branch `2847-review-restructure-editorial-guidelines`, stacked on `2847-restructure-editorial-guidelines-and-agents-md` (PR #2848).
* Joaquin evaluates the changes, then commits, pushes and opens the PR.
* The PR description can reuse the Findings table in `research.md`.
* This folder is deleted after the PR is approved and before it is merged.
