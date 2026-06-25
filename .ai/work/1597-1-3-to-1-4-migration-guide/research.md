# Research: Issue 1597 — Add 1.3 to 1.4 Version Migration Guide

## 1. Issue summary

* **Title:** [FR] Add 1.3 to 1.4 Version Migration Guide
* **Type:** Enablement/Supporting Content (non-normative)
* **Milestone:** v1.5 | **Assignee:** Matt-Cowsert | **Label:** feature
* **Story points:** 6.1 (Matt flagged as likely overstated after SQL examples were deferred; pending re-estimation)
* **Ambiguity (maintainer):** 2 of 5 (low) — authoring against a known template with a locked change set, not design.

### What the FR asks for (MVP, per maintainer assessment)

Add a "1.3 to 1.4" section to the existing `supporting_content/appendix/version_migration_guidance.md`, following the established 1.2-to-1.3 structure. Three deliverable components:

1. **Change inventory** — every 1.4 schema change categorized by the CHANGELOG's impact classification (Compatible / Migration Compatible / Incompatible).
2. **Generator section** — recommended implementation sequence, phasing guidance for a multi-change release, common edge cases, cross-references to changes.
3. **Practitioner section** — which Supported Features are affected, backward-compatibility expectations, guidance for staggered (mixed-version) provider adoption.

**Explicitly deferred (out of MVP):** SQL migration examples, a cross-version compatibility matrix, and a generator FAQ. These are North Star items.

### Timing check

FR phasing: "authored during 1.5 development after the 1.4 change set is locked." v1.4 is "Announced June 2026" (CHANGELOG); today is 2026-06-25; this FR sits in the v1.5 milestone. The 1.4 change set appears locked. Timing is correct. *Confidence: High.*

## 2. The template (existing 1.2-to-1.3 guide)

File: `supporting_content/appendix/version_migration_guidance.md` (~12 KB). Structure:

* **Document Structure** — audience routing table (All readers / Practitioners / Data Generators). *Written assuming a single migration; will need generalizing.*
* **Migrating from FOCUS 1.2 to FOCUS 1.3**
  * Overview (Change Impact Classification table)
  * What's Unchanged
  * What's New in FOCUS 1.3
  * What Requires Migration
* **Provider and Publisher Column Changes** (the one deep migration topic)
  * Before You Begin (Practitioners) checklist
  * Why This Change Was Made
  * Migration Decision Tree (Practitioners)
  * New Column: HostProviderName
  * Query Migration Examples (Practitioners) — SQL before/after
  * Verification (Practitioners)
* **Guidance for Data Generators** — Dual-Column Support, Deprecation Metadata, Deprecation Timeline
* **Affected Supported Features**
* **Additional Resources**

Ordering rule (stated in the file): reverse chronological, most recent migration first. The new 1.3-to-1.4 section is inserted **above** the 1.2-to-1.3 section, after the Document Structure intro.

The 1.2-to-1.3 guide links **only to spec content** (columns, appendix, supported features, CHANGELOG). It contains **no GitHub issue/PR references**.

## 3. The 1.4 change set (from CHANGELOG v1.4)

Headline: 2 new datasets, 47 new columns, 6 new attributes, 2 new supported features, 17 new glossary entries. This is materially larger and multi-topic compared to 1.3.

### Migration Compatible (require practitioner/generator action)

| Change | Audience | Migration action |
|--------|----------|------------------|
| `ProviderName` + `PublisherName` **removed** (deprecated 1.3, gone in 1.4) | Practitioner | Must migrate any remaining queries. The 1.2-to-1.3 section already documents the decision tree and successor columns — reference it, do not duplicate. |
| `ContractApplied` format changed to JSON Object Schema | Practitioner | Queries that parse the `ContractApplied` JSON structure must adopt the new schema. |
| `ColumnHandling` attribute removed | Generator | Requirements shifted to `FocusColumnHandling` + `CustomColumnHandling`. |
| `DiscountHandling` attribute removed | Generator | Content moved to the Discount Handling appendix. |
| `InvoiceHandling` attribute removed | Generator | Requirements shifted to `DeliveryHandling` + `DatasetCompleteness`. |

### Compatible (additive or clarifying; no required action, but notable)

| Change | Notes |
|--------|-------|
| New datasets `BillingPeriod`, `InvoiceDetail` | Support Invoice Reconciliation feature. Additive. |
| New columns for Commitment Program Eligibility Details | Additive. |
| `BilledCost` + `EffectiveCost` requirements heavily revised | Covered/covering charges, amortization rules, cross-record sum validation, Rounding Variance Tolerance for invoice matching. Classified Compatible, but the *semantics* of cost interpretation shifted — practitioners doing reconciliation should be aware. |
| `InvoiceId` feature level Recommended -> Conditional | MUST when the invoice issuer supports payable invoices. Changes presence expectations. |
| 2 new supported features | Invoice Reconciliation, Commitment Program Eligibility Details. |
| Attribute requirement changes | `CurrencyFormat` (ISO 4217 only, virtual-currency allowance removed), `NumericFormat` (precision tables), `UnitFormat` (expanded base/compound/ratio units), `StringHandling`, `NullHandling`, `JsonObjectFormat`. Mostly generator-facing. |
| Keyword `RECOMMENDED` deprecated in favor of `SHOULD` | Editorial; no conformance change. |
| Column presence rules relocated to dataset level | Generator/spec-reader facing. |

### Incompatible

* None.

## 4. Key scoping findings

1. **Standalone supporting content, not built into the spec.** `version_migration_guidance.md` is referenced by no `.mdpp` and linked from no spec file. It will not appear in spec.html/pdf and has no build/include dependency. (Markdown lint still applies via repo tooling.) Implication: low build risk; but the guide is only discoverable by direct navigation. Whether to add a discovery link is a separate question (see Open Decisions).

2. **The change set is multi-topic; the template is single-topic.** 1.2-to-1.3 had one deep migration section (Provider/Publisher). 1.4 has at least five action-requiring changes split across practitioner and generator audiences, plus several notable Compatible changes. A faithful clone of the single-topic deep-dive does not fit; the FR's own MVP (inventory + generator section + practitioner section) points to an inventory-led structure. *This is the main structural decision.*

3. **The deprecation arc closes neatly.** The 1.2-to-1.3 guide deprecated Provider/Publisher and its Deprecation Timeline table already says "1.4+ Removed." The 1.3-to-1.4 section can close that loop with a short pointer back, avoiding duplication of the decision tree.

4. **Convention tension on issue references.** The FR MVP text asks for "cross-references to GitHub issues." The precedent guide and the project changelog convention link only to spec content, never to issues/PRs. Following precedent (spec-content links) is the safer default; needs confirmation.

5. **SQL examples deferred, but the template is example-heavy.** The 1.2-to-1.3 section leans on SQL before/after blocks. With SQL deferred, the 1.3-to-1.4 section will be lighter on query examples and heavier on the change inventory and prose guidance. Consistent with the FR.

6. **Story-point re-estimation.** Matt's comment flags 6.1 SP as overstated. Authoring against a locked change set and an existing template is the bulk of the work. The breadth of 1.4 (vs. 1.3's single topic) is the main thing pushing effort back up; the deferred items pull it down.

## 5. Files in play

| Action | Path | Notes |
|--------|------|-------|
| **Update** | `supporting_content/appendix/version_migration_guidance.md` | Add the 1.3-to-1.4 section above the 1.2-to-1.3 section; generalize the Document Structure intro to cover multiple migrations. |
| Reference (read) | `CHANGELOG.md` (v1.4) | Source of the change inventory. |
| Reference (read) | `guidelines/contributors/spec-change-guidelines.md` | Change Impact Classification definitions. |
| Reference (read) | new 1.4 spec files (datasets/attributes/columns) | For accurate links in the inventory. |
| Possibly update | a discovery link from spec/appendix to this guide | Only if we decide the guide should be discoverable (Open Decision). |

No requirements-model JSON, no `.mdpp`, no column/attribute files: this is non-normative supporting content only.

## 6. Risks, dependencies, cascading impacts

* **Link accuracy.** The inventory will carry many spec links. Each must resolve to a real 1.4 path. Risk of stale/hallucinated links; verify against the tree.
* **No normative language.** This is supporting content. Avoid introducing MUST/SHOULD/MAY as new requirements; describe what the spec already requires. BCP-14 keywords only when quoting the spec.
* **Mixed-version framing.** The practitioner staggered-adoption guidance touches messaging (coexistence, calibration). Keep framing consistent with FOCUS messaging norms.
* **Dependency: 1.4 must stay locked.** If a late 1.4 erratum lands during 1.5, the inventory may need a touch-up. Low risk; errata are non-material.
* **Active-work conflict check.** No other open `.ai/work/` folders in this worktree. Low collision risk.

## 7. Decisions (resolved 2026-06-25)

* **D1 (structure): RESOLVED -> Inventory-led multi-topic guide.** Change-inventory table by impact, then focused practitioner + generator subsections for action-requiring changes; reference the 1.2-to-1.3 section for Provider/Publisher.
* **D2 (issue refs): RESOLVED -> Spec-content links only.** No GitHub issue/PR links; matches precedent and changelog convention.
* **D3 (semantic-change depth): default -> brief practitioner awareness note** for the Compatible-but-revised `BilledCost`/`EffectiveCost` and `InvoiceId` changes. Not a deep section. Revisit if Matt wants more or less.
* **D4 (discovery): default -> leave standalone** (matches precedent; the 1.2-to-1.3 guide was never linked). Optional discovery link noted as a deferred follow-up to keep the PR focused on the MVP.

Classification note: the CHANGELOG v1.4 already assigns every change a Compatible / Migration Compatible / Incompatible label. The inventory inherits those labels verbatim (per FR MVP) rather than re-deriving them.
