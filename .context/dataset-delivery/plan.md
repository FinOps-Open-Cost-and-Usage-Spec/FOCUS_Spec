# Implementation Plan: Dataset Delivery

Add a Dataset Delivery attribute that establishes column selection as a recommended capability for FOCUS data generators.

**Attribute ID:** DatasetDelivery

**Requirements:**

| # | Requirement | Keyword | Rule ID |
|---|-------------|---------|---------|
| 1 | Data generators SHOULD provide column selection capability allowing practitioners to choose which columns to include in exported datasets | SHOULD | A-001-O |
| 2 | When column selection is provided, it SHOULD support both FOCUS standard columns and custom columns | SHOULD | A-002-O |
| 3 | When column selection is provided, data generators SHOULD allow practitioners to exclude custom columns while retaining all FOCUS standard columns | SHOULD | A-003-O |

---

## Phase 1: Research & Analysis (COMPLETE)

Reviewed #1091 feature request, analyzed placement options, and determined column selection belongs in a separate attribute rather than Scenario Completeness. Documented decision rationale and defined scope.

## Phase 2: Implementation

Create the attribute following existing patterns (e.g., DiscountHandling, ColumnHandling). This is a straightforward attribute with 3 SHOULD requirements and no column definitions.

- Create attribute file with requirements above
- Update attributes index (alphabetical order, after currency_format.md)
- Add dataset conformance reference
- Create requirements model JSON (composite root DatasetDelivery-A-000-M + 3 atomic rules)
- Update dataset rules to include dependency
- Create supporting content with design rationale and examples

## Phase 3: Validation

Build and test to ensure no regressions. Verify attribute follows existing patterns.

## Phase 4: Review & Merge

Create PR linked to #1091, complete TF review cycle, merge to working draft.
