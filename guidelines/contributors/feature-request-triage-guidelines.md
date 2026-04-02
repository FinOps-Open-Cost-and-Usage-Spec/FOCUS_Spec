# Feature Request Triage and Improvement Guidelines

This document defines the quality bar, label system, and workflow for triaging Feature Requests (FRs) in the FOCUS specification backlog. It applies to both new submissions and existing backlog grooming. Existing backlog FRs will be triaged in batches following these guidelines.

This document does not cover spec design decisions, editorial standards, or PR review. For those, see [spec-design-guidelines.md](spec-design-guidelines.md), [editorial-guidelines.md](editorial-guidelines.md), and [github-guidelines.md](github-guidelines.md).

## Quality Bar by Section

### Title

FR titles must start with `[FR]` and follow these conventions. During triage, mechanical title issues (casing, length, filler words) should be corrected directly by the triager. If the title has a substantive problem that requires the author's input (e.g., describes an implementation rather than an outcome), apply `weak title`.

* **Start with a standard verb.** Choose one or use a verb similar to: Add, Clarify, Standardize, Enable, Define, Remove, Rename
* **Use correct sentence structure.** Pick whichever reads best between: Verb + Target + Qualifier OR Verb + Qualifier + Target (e.g., "Add data generator-calculated shared cost allocation" vs. "Standardize tag export across clouds")
* **Describe the outcome, not the implementation.** "Add daily amortized cost" > "Create SQL to amortize daily"
* **Sentence case; acronyms uppercase; no ALL-CAPS words.** "Add RI coverage metric" not "ADD RI COVERAGE METRIC"
* **Use canonical FOCUS terminology; stay service-provider-agnostic.** Vendor specifics belong in examples, not the title
* **Express one concept per title.** If you need two independent changes, create two issues. "And" and "or" are indications that multiple issues are needed
* **Trim filler words unless they improve clarity.** Drop "the," "of," "for," etc., where possible to save space
* **Keep titles ≤ 75 characters (aim for ~60).** Short enough to fit in GitHub lists, change logs, and slides without wrapping
* **Don't end with a trailing period**

### Sections

Each required section of the [Feature Request template](../../.github/ISSUE_TEMPLATE/feature-request.yml) has a defined quality bar. A section can fail in two ways:

* **Missing**: The section is absent, empty, or contains only placeholder text.
* **Below bar**: The section is present but does not meet the standard.

### Problem Statement

The problem statement describes a gap in what FOCUS can do today. It does not prescribe a solution.

| Outcome | Criteria |
|:--------|:---------|
| Passes | Identifies a specific limitation or ambiguity in the current specification. Written from the perspective of a practitioner or data generator encountering the gap. Does not embed a solution direction. |
| Fails (below bar) | Describes a solution instead of a problem (e.g., "add column X to the dataset"). Too vague to act on (e.g., "improve billing"). Restates the use case instead of identifying the underlying gap. Contains implementation language (column names, data types, JSON structures) rather than describing what practitioners cannot do. |

### Use Case / User Story

The use case follows the "As a / I need / So that" format. It is scoped to a single capability and describes a practitioner need, not an implementation detail.

| Outcome | Criteria |
|:--------|:---------|
| Passes | Follows the As a / I need / So that structure. Scoped to one capability. Describes what the practitioner needs to accomplish, not how the spec should change. The "I need" clause references data or analysis, not spec mechanics. |
| Fails (below bar) | Solution-oriented: describes spec changes or column additions rather than practitioner needs. Too broad: bundles multiple capabilities into a single use case (e.g., "I need commitment tracking, optimization, and renewal planning"). Mixes dimensions and metrics in a single request. The "So that" clause is missing or generic (e.g., "so that I can use the data"). |

### Success Criteria

Success criteria are testable statements focused on what practitioners can do once the FR is implemented. Each criterion must pass five quality checks:

1. **Practitioner-centric**: States what a practitioner, data engineer, or finance team can do. Not "FOCUS adds a column for X."
2. **Testable**: A reviewer can verify yes/no against a FOCUS-compliant dataset.
3. **Outcome-focused**: Describes the end state, not the implementation path.
4. **Specific**: Tied to this FR's domain, not generic to any FR (e.g., not "data is available from all supporting data generators").
5. **Non-redundant**: Each criterion covers a distinct facet of success.

Good criteria typically fall into one of these lenses:

* **Data availability**: "Practitioners can [identify/query/segment] [specific data point] for [purpose]"
* **Cross-provider consistency**: "[Data/concept] is consistently [represented/structured] across data generators that support this capability"
* **Actionability**: "Practitioners can [perform analysis/build report] using [the data] without [manual step/external data]"
* **Clarity**: "[Concept A] is clearly [distinguishable/defined] relative to [Concept B]"
* **Guidance**: "Data generators have clear guidance on [how to represent/when to populate] [the data]"

| Outcome | Criteria |
|:--------|:---------|
| Passes | Contains 2-4 criteria that satisfy the five quality checks above. Each criterion uses one of the lenses to describe a practitioner outcome. |
| Fails (below bar) | Describes implementation changes instead of outcomes (e.g., "Column X is added to the dataset"). Contains solution content misplaced from the Proposed Solution section. Not testable against a dataset. Too vague to verify (e.g., "improved consistency"). Criteria are redundant with each other. |

### Organizations Requesting

At least one organization is listed with a priority signal (blocker or nice-to-have).

| Outcome | Criteria |
|:--------|:---------|
| Passes | At least one named organization. Each entry includes whether the feature is a blocker or nice-to-have. |
| Fails (below bar) | Organizations listed but without blocker/nice-to-have classification. |

### Optional Sections

Data Generator Support, Supporting Documentation, and Proposed Solution are not triaged for quality. Their presence is encouraged but not required for an FR to advance.

## Label System

Labels use two prefixes to signal the type of issue. Both prefixes use spaces (no dashes) and alpha-sort into contiguous blocks in GitHub.

### `needs` Labels (Section Missing)

These labels indicate a required section is absent or empty.

| Label | When to apply |
|:------|:--------------|
| `needs problem statement` | Problem Statement section is missing or empty |
| `needs use case` | Use Case / User Story section is missing or empty |
| `needs success criteria` | Success Criteria section is missing or empty |
| `needs org requesting` | Organizations Requesting section is missing or empty |

The following existing `needs` labels are unchanged and continue to serve their current purpose:

* `needs triage`
* `needs backlog review`
* `needs stakeholder input`
* `needs examples`
* `needs work item`
* `needs supported features`
* `needs org support`

### `needs` Labels (Structural)

These labels indicate the FR has structural issues that must be resolved before it can be assessed.

| Label | When to apply |
|:------|:--------------|
| `needs scoping` | FR scope is unclear; ambiguity is too high to estimate |
| `needs splitting` | FR bundles multiple capabilities that should be separate issues |

### `weak` Labels (Below Quality Bar)

These labels indicate a section is present but does not meet the quality bar defined above.

| Label | When to apply |
|:------|:--------------|
| `weak problem statement` | Problem statement describes a solution, is too vague, or restates the use case |
| `weak use case` | Use case is solution-oriented, mixes dimensions and metrics, or has quality problems beyond scope bundling. If bundling is the primary issue, prefer `needs splitting` instead. |
| `weak success criteria` | Success criteria describe implementation changes rather than testable practitioner outcomes |
| `weak title` | Title does not follow conventions and requires author input to fix (e.g., describes implementation rather than outcome) |
| `weak org requesting` | Organizations are listed but lack blocker/nice-to-have classification |

### Lifecycle Label

| Label | When to apply |
|:------|:--------------|
| `stale` | FR has carried unresolved `needs` or `weak` labels for 3 or more releases without a substantive update |

### Reading the Labels

An FR with zero `needs` and `weak` labels has cleared the quality bar. No separate "ready" or "approved" label is needed. The absence of triage labels is the positive signal.

Any maintainer may remove a `needs` or `weak` label once the corresponding section meets the quality bar.

If an FR still carries any `needs` or `weak` label, it cannot advance to "Under Consideration." The PM may begin Maintainer Assessment work in parallel while labels are being resolved, but the FR cannot exit triage until all `needs` and `weak` labels are cleared.

The specific failure mode behind a `weak` label (e.g., solution-oriented vs. too broad) belongs in the triage comment on the issue, not in the label. This reduces label proliferation and avoids the "which sub-label?" question during triage.

### When to Create Labels

Labels defined in this document will be created in GitHub after these guidelines are approved. No labels should be created, renamed, or deleted before approval.

The existing kebab-case labels `needs-scoping` and `needs-splitting` will be deleted and replaced by the space-separated equivalents defined above. Existing granular triage labels (e.g., `use-cases-solution-oriented`, `use-cases-too-broad`, `success-criteria-not-testable`, `blends-dimensions-metrics`) will be deprecated in favor of the `weak` prefix labels, with failure details captured in triage comments instead of label names.

## Triage Workflow

Triage follows four logical gates. An FR must clear all four before it can be considered for scope assignment. These gates are logical checks, not necessarily separate passes. A single triage pass can clear multiple gates. Any contributor with triage permissions can perform Gates 1-3. Gate 4 is completed by the PM.

### Gate 1: Completeness Check

Are all required sections present and non-empty?

* If not: apply the relevant `needs` label(s), comment on the issue explaining what is missing, and set the project status to "Needs More Info."
* If yes: proceed to Gate 2.

### Gate 2: Quality Check

Do present sections meet the quality bar defined above?

* If not: apply the relevant `weak` label(s), comment on the issue with specific feedback on what to improve.
* If yes: proceed to Gate 3.

### Gate 3: Structural Check

Is the FR well-scoped and actionable?

* If the FR bundles multiple capabilities: apply `needs splitting` and comment with a recommendation for how to decompose it.
* If the FR scope is unclear or ambiguity is too high to estimate: apply `needs scoping` and comment with what needs clarification.
* If the FR contains out-of-scope elements (e.g., telemetry, non-billing data): apply `needs scoping` and comment asking the submitter to revise the scope. This is rare but ensures the unresolved state is trackable.

**Ambiguity factors.** The following factors help assess whether an FR's scope is clear enough to proceed:

| Factor | Reduces ambiguity | Increases ambiguity |
|:-------|:------------------|:--------------------|
| Problem clarity | Well-defined gap with practitioner examples | Vague or conceptual problem statement |
| Solution maturity | Proposed solution exists, TF discussion captured | No solution direction, competing approaches |
| Scope boundaries | Clear FR boundary, no overlap with other FRs | Broad scope, overlaps other FRs or datasets |
| Data generator readiness | Providers already expose this data | Net new concept, no provider data exists |
| Spec impact breadth | Touches one column or one dataset | Touches multiple columns, datasets, or glossary |
| Community consensus | Agreement on approach in TF or community | Competing views, unresolved design questions |

FRs where multiple factors fall in the "increases ambiguity" column should receive `needs scoping` until the key questions are resolved.

### Gate 4: Maintainer Assessment

The PM fills the Maintainer Assessment sections of the FR template:

* Adoption Impact
* Supported Features Alignment
* Implementation Scope (MVP Definition, North Star Vision, Phasing Strategy)
* Impacted Parties
* Level of Ambiguity
* FinOps Scope Alignment

**Entry to "Under Consideration"** requires: zero `needs` or `weak` labels remaining AND Maintainer Assessment sections complete.

## Staleness Policy

Feature Requests that remain in an unresolved triage state accumulate staleness across release cycles. The release count starts from the FR's creation date.

| Threshold | Action |
|:----------|:-------|
| 3 releases with unresolved `needs` or `weak` labels | Apply `stale` label. Comment notifying the submitter of what is needed and that the FR will be closed if unaddressed. |
| 5 releases with unresolved `needs` or `weak` labels | Close the FR with a comment explaining the closure reason. |

A "substantive update" means the submitter edited the FR to address the labeled issues. A "still interested" comment without changes does not count.

Closed FRs may be reopened within one release of closure if the submitter provides the missing or improved content.
