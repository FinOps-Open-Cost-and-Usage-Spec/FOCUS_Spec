# Plan: Issue 1597 — Add 1.3 to 1.4 Version Migration Guide

## Approach

Add a "Migrating from FOCUS 1.3 to FOCUS 1.4" section to
`supporting_content/appendix/version_migration_guidance.md`, inserted **above** the
existing 1.2-to-1.3 section (reverse-chronological rule). Inventory-led structure;
spec-content links only (no GitHub issue refs); SQL examples deferred.

This is **non-normative supporting content**. No new normative requirements, no Rule
IDs, no requirements-model JSON, no `.mdpp` or column/attribute files. The standard
Phase-3 requirements table (# / MUST-SHOULD-MAY / Rule ID) does not apply; the
"requirements" of this deliverable are content sections, listed below. Any BCP-14
keyword appears only when quoting an existing spec requirement.

## Content outline (the deliverable)

### A. Generalize the existing "Document Structure" intro
Currently written for a single migration. Update the audience routing table so it
covers multiple migrations (the table should describe section *types*, not the
1.2-to-1.3 topics specifically). Small edit, above both version sections.

### B. New section: "Migrating from FOCUS 1.3 to FOCUS 1.4"

1. **Overview** — Change Impact Classification table (Compatible / Migration
   Compatible / Incompatible), inheriting CHANGELOG v1.4 labels verbatim. One-line
   summary per bucket. State that there are no Incompatible changes.
2. **What's Unchanged** — everything from 1.3 carries forward except the removed
   columns/attributes; queries not touching the migration items keep working.
3. **What's New in FOCUS 1.4** (additive, no action required) — table:
   `BillingPeriod` + `InvoiceDetail` datasets, 47 columns, 6 new attributes
   (`CorrectionHandling`, `CustomColumnHandling`, `DatasetCompleteness`,
   `DatasetConfiguration`, `DeliveryHandling`, `FocusColumnHandling`), 2 supported
   features (Invoice Reconciliation, Commitment Program Eligibility Details), new
   appendix entries. Link each to its spec file.
4. **What Requires Migration** — the action-requiring (Migration Compatible) items,
   summarized, with a pointer to the audience subsections below.

### C. Practitioner migration topics
* **Provider/Publisher removal** — short subsection: these were deprecated in 1.3 and
  are removed in 1.4. Point to the 1.2-to-1.3 "Provider and Publisher Column Changes"
  decision tree and successor-column mapping below. Do not duplicate.
* **`ContractApplied` JSON format change** — describe the move to JSON Object Schema
  format; note that queries parsing the structure need updating. Link to
  `contractapplied.md` and the JSON Object examples appendix. (No SQL; deferred.)
* **Brief awareness note** — `BilledCost`/`EffectiveCost` requirement revisions
  (covered/covering charges, rounding variance tolerance, cross-record validation)
  and `InvoiceId` Recommended -> Conditional. Classified Compatible, but flagged so
  reconciliation-sensitive practitioners review the updated definitions. Link to the
  column files and Rounding Variance Tolerance appendix.

### D. Guidance for Data Generators
* **Attribute restructuring** — table mapping removed -> successor:
  `ColumnHandling` -> `FocusColumnHandling` + `CustomColumnHandling`;
  `DiscountHandling` -> Discount Handling appendix;
  `InvoiceHandling` -> `DeliveryHandling` + `DatasetCompleteness`.
* **New datasets/attributes adoption** — brief; link to dataset overviews.
* **Recommended implementation sequence & phasing** — for a multi-change release:
  e.g., adopt additive columns/datasets first (no consumer impact), then complete the
  attribute remap, then confirm removed columns are dropped. Note staggered-adoption
  handling for mixed-version consumers.

### E. Affected Supported Features
List the 1.4-affected supported features (Invoice Reconciliation, Commitment Program
Eligibility Details, Contract Commitments, Effective Cost, Billed Cost and Invoice
Alignment, Cost Comparison, Participating Entity Identification). Link each.

### F. Additional Resources
CHANGELOG v1.4, key new spec files, the 1.2-to-1.3 section.

## Deliverables

| # | Deliverable | Path | Reference |
|---|-------------|------|-----------|
| 1 | New 1.3-to-1.4 section + generalized intro | `supporting_content/appendix/version_migration_guidance.md` | Template = same file's 1.2-to-1.3 section |
| 2 | research.md migrated to supporting_content (if valuable) | `supporting_content/` | Per feature.md cleanup |
| 3 | Draft PR against `working_draft` | — | `.github/pull_request_template.md` |

## Editorial guardrails

* Lists use `*`; two-space nested indentation.
* Column/attribute IDs in PascalCase backticks; values in double quotes.
* No em/en dashes anywhere.
* Link entity/glossary terms on first occurrence per file.
* Spec-content links only; verify every link path resolves against the 1.4 tree.
* Notes use `> **Note:**` blockquote format.
* Supporting content: no new MUST/SHOULD/MAY except when quoting the spec.

## Validation

* `python3 enhanced_markdown_lint.py --config markdownlnt.cfg scan supporting_content/appendix/version_migration_guidance.md` (from `specification/`).
* Manual link-resolution check on every spec path referenced.
* `validate_includes.py` is **not** applicable (file is not in a `.mdpp`-driven dir);
  confirm no include expectation exists for `supporting_content/`.

## Out of scope (deferred / North Star)

* SQL migration examples.
* Cross-version compatibility matrix; generator FAQ.
* Discovery link from the spec/appendix to this guide (optional follow-up).
* Establishing the migration guide as a formal standing release line item (process change).

## Execution phases (for tasks.md)

1. Draft the generalized intro edit.
2. Draft the 1.3-to-1.4 section (B–F) in order.
3. Self-review against editorial guardrails + verify all links resolve.
4. Lint.
5. Migrate useful research to `supporting_content/`; PR body from template; create **draft** PR vs `working_draft`.
