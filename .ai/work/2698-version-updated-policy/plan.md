# Plan: Issue 2698 - Version Updated policy

Status: draft for task force discussion. Nothing implemented.

## Options and cost

| Option | Files touched | Ongoing cost | Rule text needed |
|---|---|---|---|
| A. `Version Updated` on every file | about 172 additions (files with a content change after introduction), 192 if link-only changes count; 227 if the section is mandatory | Every content PR bumps it; sweeps touching 100+ files all need bumps; no way to lint "substantive" | Definition of a substantive change, bump value during a draft, placement and wording in editorial guidelines, a change-guidelines step |
| B. Supported features only | 14 additions + verify 4 existing (`participating_entity_identification` needs a check) | Features change slowly (about 17 of 24 ever) but the same definition problem applies | Same definition, scoped to supported features; explain why features and not columns |
| C. Drop it | 4 files (remove the section); no other file changes | None | One sentence in editorial guidelines Section Structure: the change history lives in CHANGELOG.md and release notes, not in per-file sections |

## Recommendation

C for 1.5, with a backlog Feedback issue to revisit once change history can be generated from git rather than hand-maintained.

* Both A and B depend on a definition of "substantive change" the repo does not have. The four existing values are only consistent with a rule that excludes formatting and link-only changes; counting link-only changes puts two of them a release behind.
* Nothing can enforce a bump. A linter cannot tell a content change from a formatting change, so any rule decays the way this one did.
* CHANGELOG.md already records per-release changes to supported features by impact class, including `cost_comparison` and `effective_cost` in 1.4.
* The churn that would drive bumps is mostly repo-wide sweeps (`511773f2` alone is 145 files), which say little about any one entity.
* C is the only option that finishes inside the 1.5 consistency review window (ends 2026-10-29) with a uniform result across all 227 files.

Fallback if the task force wants to keep the field: B, with the rule "present only when a content change (not formatting, links or editorial wording) changed a requirement after the Introduced release".

## 1.5 consistency review vs backlog

1.5 consistency review PR:

* Decision recorded on #2698.
* Option C: remove the 4 sections, add the guideline sentence.
* Option A or B: add the rule text and the missing sections in one PR, or split by file group.

Backlog Feedback issue (not 1.5):

* Generated per-entity change history.
* Version Introduced cleanup: 18 columns still say 0.5, `ServiceProviderName` free text, per-dataset values for shared columns.
* The renamed-column and deprecated-column sections required by spec-change-guidelines.md that no column file has.
* The 126 vs 127 column count.

## Open points

* Confirm with the task force whether Introduced cleanup is in scope for #2698 or only Updated.
* Check `participating_entity_identification` Updated 1.3 against its history before any option relies on it.
