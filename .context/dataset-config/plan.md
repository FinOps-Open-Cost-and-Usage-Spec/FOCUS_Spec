# Implementation Plan: Dataset Configuration

Add a Dataset Configuration attribute that establishes how practitioners can configure the structure and content of a FOCUS dataset.

**Attribute ID:** DatasetConfiguration

**Requirements:**

| # | Requirement | Keyword | Rule ID |
|---|-------------|---------|---------|
| 1 | FOCUS datasets MUST allow selecting which columns to include | MUST | A-001-M |
| 2 | FOCUS datasets MUST produce conformant column values regardless of which columns are included | MUST | A-002-M |
| 3 | FOCUS datasets SHOULD sum metric columns by default when the selected dimension columns result in rows with identical values | SHOULD | A-003-O |
| 4 | FOCUS datasets MUST allow selecting the time granularity based on ChargePeriodStart, when available | MUST | A-004-M |
| 4.1 | FOCUS datasets MUST allow selecting daily granularity | MUST | A-004-1-M |
| 4.2 | FOCUS datasets MUST allow selecting hourly granularity when the dataset includes costs priced at an hourly or lower grain | MUST | A-004-2-M |
| 4.3 | FOCUS datasets SHOULD allow selecting monthly granularity | SHOULD | A-004-3-O |
| 4.4 | FOCUS datasets MUST sum metric columns based on selected dimension columns with identical values when time granularity is changed | MUST | A-004-4-M |
| 5 | FOCUS datasets SHOULD allow opting in or out of row aggregation (summing metrics) | SHOULD | A-005-O |
| 5.1 | FOCUS datasets MUST sum metric column values when rows are aggregated | MUST | A-005-1-M |
| 5.2 | FOCUS datasets SHOULD use case-insensitive matching when aggregating rows | SHOULD | A-005-2-O |
| 6 | FOCUS datasets SHOULD allow selecting the FOCUS version | SHOULD | A-006-O |
| 6.1 | FOCUS datasets MUST NOT add or remove columns when a specific FOCUS version is selected | MUST NOT | A-006-1-N |
| 7 | FOCUS datasets SHOULD allow filtering rows by column values | SHOULD | A-007-O |
| 7.1 | FOCUS datasets MUST use case-insensitive matching when filtering rows | MUST | A-007-1-M |
| 8 | FOCUS datasets MUST include metadata describing the selected configuration options | MUST | A-008-M |

---

## Phase 1: Research & Analysis (COMPLETE)

Reviewed #1091 feature request, analyzed placement options, and determined column selection belongs in a separate attribute. Renamed from "Dataset Delivery" to "Dataset Configuration" since "delivery" implies push semantics. Expanded scope to include row aggregation, time granularity, version selection, and row filtering.

## Phase 2: Implementation (COMPLETE)

Created the attribute following existing patterns (e.g., DiscountHandling, ColumnHandling, InvoiceHandling).

- Created attribute file with requirements above
- Updated attributes index (alphabetical order)
- Added dataset conformance reference
- Created requirements model JSON with composite and atomic rules
- Updated dataset rules to include dependency
- Created supporting content with design rationale and examples

## Phase 3: Validation

Build and test to ensure no regressions. Verify attribute follows existing patterns.

## Phase 4: Review & Merge

Create PR linked to #1091, complete TF review cycle, merge to working draft.
