# Research: Issue 2698 - Decide Version Updated policy and apply consistently

Issue: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2698 (child of 2509, 1.5 Consistency Review, window 2026-10-08 to 2026-10-29).

Scanned `working_draft` at `9cc7bef0` (2026-10-08). Nothing here is classified yet.

## Issue requirements

* `## Version Updated` is used inconsistently (issue reports 0/126 column files, 4/24 supported feature files).
* No rule states when a change should bump it.
* Task force decides: add the section to every file with `Version Introduced` (supported features first, columns second), keep it on supported features only, or drop it.
* Task force also decides whether any of that lands in 1.5, goes to the backlog as Feedback, or is added to an existing issue.
* Definition of done: decision recorded; 1.5 consistency review PR and/or backlog issue per the decision.

## Where the sections appear

| File type | Files | With Version Introduced | With Version Updated |
|---|---|---|---|
| Columns, Cost and Usage | 69 | 69 | 0 |
| Columns, Contract Commitment | 30 | 30 | 0 |
| Columns, Invoice Detail | 22 | 22 | 0 |
| Columns, Billing Period | 6 | 6 | 0 |
| Dataset overviews (4 `dataset.md` + `data_model.md`) | 5 | 5 | 0 |
| Supported features | 24 | 24 | 4 |
| Attributes | 15 | 15 | 0 |
| Metadata | 32 | 32 | 0 |
| Operating model conditions | 24 | 24 | 0 |
| Total | 227 | 227 | 4 |

The scan finds 127 column files against the issue's 126. The cause is unexplained.

Files with `## Version Updated`:

| Supported feature | Introduced | Updated | Change kind at each release tag (vs previous tag) |
|---|---|---|---|
| `cost_comparison` | 0.5 | 1.4 | 1.2 first standalone file; 1.3 content; 1.4 content; 1.5 draft link only |
| `effective_cost` | 0.5 | 1.4 | 1.2 first standalone file; 1.3 content; 1.4 content; 1.5 draft link only |
| `participating_entity_identification` | 1.1 | 1.3 | 1.3 first standalone file; 1.4 formatting only |
| `resource_usage` | 1.0 | 1.5 | 1.2 first standalone file; 1.3 content; 1.4 formatting only; 1.5 draft content |

With formatting-only and link-only changes set aside, each Updated value equals the last release with a content change. If link-only changes count, `cost_comparison` and `effective_cost` are one release behind. Of the other 20 supported features, 14 have content changes after first appearing (1.3, 1.4 or 1.5) and no Updated section; 6 have none.

## Change kinds

Every commit and file pair, and every release-to-release pair, is tagged mechanically by comparing before and after text. The comparison removes whitespace, markup and punctuation, ignores case in headings, and sets the Version Introduced and Version Updated sections aside. Case outside headings and the words MUST, SHOULD, MAY and NOT are kept, so those edits count as content.

| Kind | Meaning | Commit and file pairs |
|---|---|---|
| `content` | Text differs after normalization | 1,673 |
| `links` | Identical once link targets are ignored | 464 |
| `format` | Identical after normalization, or identical text (renames) | 478 |
| `version` | Only the Introduced or Updated value changed | 21 |
| `new` | File first appears in its directory | 242 |

* `d2bdd594` (title-case rename, 197 files) is `format` for all 197 files.
* `511773f2` (conditions rows, 149 files) is `content` for 145 and `links` for 4.
* 18 of 345 commits are formatting only throughout.
* Display-name edits inside link text (for example "JsonObjectFormat" to "JSON Object Format") count as `content`.
* With `content` and `links` counted, 125 of 127 columns have a change after creation; ignoring commits that touch 10 or more files, 79 do.
* This is a mechanical aid for the later classification, not the change type or impact classification from the change guidelines.

## What the rules say

* No text in `README.md`, `CHANGELOG.md`, `RELEASE-PLANNING.md`, `guidelines/`, or `specification/` says when to populate or bump `Version Updated`.
* `guidelines/contributors/editorial-guidelines.md`, Section Structure: subsection order example ends with `Version Introduced`. `Version Updated` is not listed. The worked column example ends with `Version Introduced: 1.0-preview`.
* `guidelines/contributors/spec-change-guidelines.md`:
  * New column or feature: "Changelog indicates that the new feature/column has been added."
  * Rename: specification "is to include a section that indicates the previous name and the version in which it was changed". No column file has such a section.
  * Deprecation: specification MUST include the version that will remove the entity. No column file has such a section.
  * Change Type Classification: Addition, Deprecation, Removal, Improvement, Bug Fix, Editorial.
  * Change Impact Classification: Compatible, Migration Compatible, Incompatible.
* `README.md`: versioning is "inspired by Semantic Versioning 2.0" and not a strict compatibility guarantee.
* No linter rule, Makefile step, or JSON/schema file references either section.
* Issue 385 (closed 2024-04-12) asked that all columns and attributes be marked introduced in 1.0 because 0.5 was never formally approved.

## Version Introduced values

| Group | Distribution |
|---|---|
| Columns, Cost and Usage (69) | 0.5: 18, 1.0-preview: 15, 1.0: 8, 1.1: 7, 1.2: 7, 1.3: 8, 1.4: 2, 1.5: 4 |
| Columns, Contract Commitment (30) | 1.3: 13, 1.4: 17 |
| Columns, Invoice Detail (22) | 1.4: 22 |
| Columns, Billing Period (6) | 1.4: 6 |
| Supported features (24) | 0.5: 7, 1.0: 7, 1.1: 3, 1.3: 4, 1.4: 2, 1.5: 1 |
| Attributes (15) | 0.5: 4, 1.0-preview: 3, 1.0: 1, 1.3: 2, 1.4: 5 |
| Metadata (32) | 1.0: 14, 1.1: 1, 1.2: 2, 1.3: 15 |
| Operating model conditions (24) | 1.5: 24 |
| Dataset overviews (5) | 0.5: 2, 1.3: 1, 1.4: 2 |

Inconsistencies noted:

* `ServiceProviderName` Introduced value is free text: "1.3 Introduced as a replacement for the removed ProviderName column".
* 18 columns still say 0.5 although 0.5 was never released.
* Shared columns carry a different Introduced value per dataset (for example `BillingCurrency`: 0.5, 1.3, 1.4).
* Introduced values were edited after file creation, for example `ca9211bb` (1.0 to 1.0-preview, 2024-04-12) and `dbaa0f14` (`ChargeClass` 0.5 to 1.0). An exact count needs the classification pass, because repo-wide commits such as `d2bdd594` also move these lines without changing the value.
* Headings were `Introduced (Version)` and `Updated (Version)` until `d2bdd594` (2026-04-30).
* `Updated (Version)` first appeared in `65484870` (2025-10-30), then `a9f5fe12` (2026-04-02), then `3d864b44` (2026-10-01, as `Version Updated`).

## Content change per release, columns

Counts of the 127 column files whose text differs from the previous release tag (any change, including formatting):

| Release | New files | Changed |
|---|---|---|
| 0.5 | 18 | not applicable |
| 1.0-preview | 15 | 18 |
| 1.0 | 8 | 33 |
| 1.1 | 7 | 41 |
| 1.2 | 7 | 48 |
| 1.3 | 21 | 55 |
| 1.4 | 47 | 76 |
| 1.5 draft | 4 | 123 |

123 of 127 columns changed at least once after introduction. 345 distinct commits touch these entity files; 173 touch one file and 56 touch ten or more.

## Method and caveats

* Entity files: every `.md` under `specification/` (excluding `requirements_model/`) with a `## Version Introduced` or `## Version Updated` heading.
* Release grid: file text at tags `v0.5-cr`, `v1.0-preview-cr`, `v1.0`, `v1.1`, `v1.2`, `v1.3`, `v1.4` and `origin/working_draft`, found by following renames. Shared columns only follow their own dataset directory.
* Per-commit release: first tag whose ancestry contains the commit. Cherry-picked content (for example some 1.1 columns) can show a later release; use the grid for content per release.
* The history was fetched with `git fetch --unshallow` because the checkout was shallow.

## Files in this folder

* `entity_versions.csv`: one row per file.
* `change_log.csv`: one row per commit and file, with a mechanical `change_kind` and blank `classification` and `notes` columns.
* `history_full.json`: full history with up to 80 changed lines per file per commit.

Interactive view: https://claude.ai/artifact/NoKnzn7KyHerVc8yBJMHww

## Verification (2026-10-13, against worktree at `9cc7bef0`)

Re-run against the repo, not taken from the first session:

* Counts confirmed: 227 files with `## Version Introduced` (222 plain, 5 with `<!--SkipTOC-->`), 4 with `## Version Updated` (`effective_cost`, `participating_entity_identification`, `cost_comparison`, `resource_usage`), 127 column files (69 / 30 / 22 / 6). The 127 files hold 111 distinct column names.
* `d2bdd594`: all 197 entity files change only by heading case and the `Introduced (version)` to `Version Introduced` rename. Body text is identical once headings and link targets are set aside. No Introduced or Updated value changed. `format` for all 197 is correct.
* 126 vs 127 remains unexplained. Two columns (`CredentialId`, `RequesterDetails`) were added on 2026-09-24 (`63cf0d6c`), which may explain part of the gap but not all of it.
* The release grid agrees with the four Updated values except `participating_entity_identification` (Introduced 1.1, Updated 1.3): the grid shows no content change after the 1.3 first standalone file. Check the 1.3 value before relying on it.

### Spot-check of `change_kind`

31 stratified rows plus a scan of all 179 `format` rows that have line changes (excluding `d2bdd594`). No row was found where substantive text is hidden under `format`. Systematic quirks:

* Display Name to Entity ID swaps that differ only by spaces or slashes (for example `Date/Time Format` to `DateTimeFormat`, `Charge Type` to `ChargeType`, `Resource Name` to `ResourceName`) are `format`, while swaps that differ by case are `content`. About 25 `format` rows. Inconsistent with the "display-name edits count as content" rule above.
* Link target changes that differ only by punctuation (`#date/timerequirements` to `#datetimerequirements`) land in `format`, not `links`.
* Punctuation edits that touch normative text (`e.g.` to `e.g.,`, comma to semicolon, `"Purchase"` to `'Purchase'`) are `format`.
* `95410524`: shared columns copied into a new dataset directory show as `format` or `content` instead of `new` (3 rows).
* `content` is coarse for repo-wide commits. `511773f2` adds a Conditions row to 145 files and is the main reason 123 of 127 columns show as changed in 1.5 draft. Treat commits touching 10 or more files as a separate pass.
* `version` rows are correct but include a wording-only edit (`f9fc86b9`, `ServiceProviderName` free text).

### Used for costing

Files with a content change after first appearing (release grid): 172 of 227 (columns 123 of 127, supported features 17 of 24, attributes 10 of 15, metadata 17 of 32, dataset overviews 5 of 5, conditions 0 of 24). With link-only changes counted: 192.
