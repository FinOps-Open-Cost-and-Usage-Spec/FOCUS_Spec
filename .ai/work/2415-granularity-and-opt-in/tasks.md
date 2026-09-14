# AI #2415 Tasks

## Original Research (Completed Under Old Approach)

* [x] Fetch and review issue #2415.
* [x] Fetch and review FR #2358.
* [x] Review PR #2351 for Conditions architecture relevance.
* [x] Review PR #2360 actor column approach.
* [x] Review prior attribute PR patterns (#1816, #1800, #1501).
* [x] Review local current spec files for DatasetConfiguration, DatasetCompleteness, split cost allocation, metadata, and dataset instance concepts.

## Redesign (New Approach — Scoped Detail)

* [x] Replace abstract granularity-configuration / applicability-filter approach with scoped detail configuration.
* [x] Update normative requirements in `specification/attributes/dataset_configuration.md`.
* [x] Update `supporting_content/attributes/dataset_configuration.md` with new Scoped Detail Configuration section.
* [x] Update `specification/attributes/attributes_overview.md` description.
* [x] Fix formatting violations: documentation-subject pattern, canonical subjects, version attribution.
* [x] Add requirement that detail levels may include dimension columns outside the column list.
* [x] Correct version attribution to 1.5; restore 1.4 table to base state.
* [x] Update pr_body.md and plan.md to reflect new approach.

## Pending

* [x] Replace granularity terminology with scoped detail configuration.
* [x] Add record-minimization requirements for identical delivered dimensions and non-summable metrics.
* [x] Clarify split cost allocation as a defined subset of scoped detail configuration.
* [x] Add detail-scope documentation disclosure for split cost allocation usage.
* [x] Clarify separately delivered detail as a provider-defined companion artifact unless FOCUS defines a standard dataset for that detail.
* [x] Replace service-specific detail terminology with scoped detail terminology.
* [x] Move PR #2473 out of draft.
* [x] Resolve stale outdated GitHub review threads.
* [ ] Requirements model JSON update (deferred until approach is agreed upon).

## Glossary and Alignment Review (2026-09-13)

* [x] Merge `working_draft` into the branch (17 commits behind; glossary anchors now `#datamodel.*`).
* [ ] Confirm with TF-2: term names, default output as a detail variant, PrincipalId default column set, Ledger interaction (listed under Open Questions for TF-2 in the PR description).
* [x] Decide selection granularity: either whole-dataset or per-scope selection satisfies the requirement (author decision 2026-09-13).
* [x] Add glossary entries: Companion Artifact, Detail Representation, Detail Scope, Detail Variant.
* [x] Restructure DatasetConfiguration requirements per review.md section 2.1, keeping record minimization at SHOULD, keeping the existing bullet order, and keeping the split cost allocation "uses" wording.
* [x] Update DatasetConfiguration intro bullet and Example.
* [ ] Undecided: review.md 2.3 B (sum preservation SHOULD to MUST) and 2.3 C ("contains allocated charges" wording).
* [ ] Requirements model A-002 text drifts further from the spec ("detail variant selection"); update with the deferred RM work.
* [x] Revert Version Introduced to 1.4.
* [x] Accept attributes_overview row suggestion.
* [x] Apply review fixes independent of TF-2: detail columns regardless of column selection, documentation condition, documentation accessibility.
* [ ] Align supporting content terminology and sections per review.md section 4.
* [ ] Migrate placement alternatives, embedded JSON option, AWS precedent, and privacy notes from research.md to supporting content.
* [ ] Resolve remaining open review threads (see Open Review Threads below).

## Open Review Threads (Status 2026-09-13)

Five review threads remain unresolved on PR #2473. All other threads are resolved.

* [ ] #3866728644 (Matt-Cowsert): terms undefined in shipped content. Glossary entries added; reply and leave open until TF-2 confirms the names.
* [ ] #3867990817 (Matt-Cowsert, TF-2 action item 2026-08-26): glossary entries added under the proposed names; reply and leave open until TF-2 confirms.
* [ ] #3917948166 (ijurica): renames and glossary entries adopted; reply and leave open until TF-2 confirms.
* [ ] #3866728652 (Matt-Cowsert): selection-granularity clause removed; either granularity satisfies the requirement. Reply and resolve.
* [ ] #3866728680 (Matt-Cowsert): merge criterion now uses FOCUS dataset columns, which include custom columns. Reply and resolve.

### Resolved This Session

* Threads #3800388224 and #3818143965: Version Introduced reverted to 1.4 (87c245c5).
* Thread #3800428211: anchor wording restored to `Dataset` (a978845c); confirming reply added.
* Thread #3866728656: detail-level columns included regardless of column selection (fcda8332).
* Thread #3866728667: documentation block nested under `When a detail scope is offered` (fcda8332, 1dd689e8).
* Thread #3866728674: documentation accessibility bullet added (fcda8332).
* Thread #3866728683: attributes overview row now reads scoped detail (fcda8332).

### Session Notes

* Branch merged with `working_draft` on 2026-09-13 (69b60415).
* Local branch `backup/pr-2473-pre-fix` (0a1405c5) is no longer needed and can be deleted.
* Thread replies use the `🤖 [AI][Claude Code]` prefix. Commits that apply reviewer wording include `Co-authored-by:` trailers.
