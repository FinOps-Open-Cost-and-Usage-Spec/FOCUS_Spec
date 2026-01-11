# Dataset Delivery (Column Selection) Initiative

> **Status:** Planning
> **Target Release:** 1.4
> **Primary Issue:** [#1091](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1091)
> **Related Issues:** #1094 (scenario completeness - references column selection as SHOULD)

---

## Problem Statement

Currently, not all FOCUS providers give Practitioners the ability to select which columns are provided in the FOCUS dataset _prior_ to exporting the report. Without clear mandates, generators implement divergent approaches, forcing practitioners to perform bespoke data cleaning and slowing adoption.

This becomes especially important with the Scenario Completeness attribute (#1094), which requires data generators to include custom columns for all scenario-enabling information from native datasets. This could add potentially hundreds of additional columns, making column selection critical for practitioners who only need a subset.

---

## Use Cases

### 1. Cost Allocation Workflow
**As a** FinOps Practitioner performing cost allocation
**I need** to select only Tags, BilledCost, EffectiveCost, and account structure columns for my allocation workflow
**So that** I can reduce dataset size, improve query performance, and simplify ETL processes without irrelevant columns

### 2. FOCUS-Only Adoption
**As a** FinOps Practitioner with limited data engineering resources
**I need** to export only FOCUS standard columns (excluding x_ custom columns)
**So that** I can adopt FOCUS quickly without needing to accommodate provider-specific custom columns in my data pipelines

### 3. Commitment Analysis
**As a** FinOps Practitioner analyzing commitment optimization
**I need** to select only commitment-related columns plus core cost/usage metrics
**So that** I can focus on commitment analysis without processing dozens of unused columns

### 4. Multi-Use-Case Pipelines
**As a** Data Engineer building FOCUS data pipelines
**I need** to select different column subsets for different use cases (allocation vs. optimization vs. governance)
**So that** I can optimize storage costs, query performance, and data transfer volumes for each workflow

### 5. Bandwidth/Cost Constraints
**As a** FinOps Practitioner with bandwidth/cost constraints
**I need** to minimize FOCUS dataset size by excluding unused columns
**So that** I can reduce egress costs, data transfer times, and storage requirements for large billing datasets

### 6. Tooling Vendor Optimization
**As a** FinOps Tooling Vendor ingesting FOCUS data
**I need** to request only columns relevant to my product's functionality
**So that** I can optimize ingestion pipelines and reduce infrastructure costs for customers

### 7. Data Generator Clarity
**As a** FOCUS Data Generator
**I need** clear requirements for column selection capabilities
**So that** I can build consistent export experiences without guessing at practitioner needs or implementing bespoke solutions

---

## Acceptance Criteria (from #1091)

### Column Selection Capabilities
- [ ] FOCUS datasets provide column selection mechanism before/during export
- [ ] Practitioners can select specific columns to include in exported datasets
- [ ] Practitioners can select predefined column groups (e.g., "core cost metrics," "commitment columns," "account structure")
- [ ] Column selection supports both FOCUS standard columns and custom (x_) columns
- [ ] Selection mechanism distinguishes between mandatory columns (always included) and optional columns (practitioner choice)

### Selection Granularity
- [ ] Practitioners can select individual columns by name
- [ ] Practitioners can select column groups/categories (e.g., all cost columns, all commitment columns)
- [ ] Selection mechanism supports "all FOCUS standard" vs. "all FOCUS standard + custom" distinction
- [ ] Minimum viable selection includes columns necessary for data integrity (e.g., row identifiers, charge periods, costs)

### User Experience
- [ ] Column selection interface is discoverable and accessible (UI, API, configuration file)
- [ ] Default selections cover common use cases (e.g., "allocation essentials," "commitment analysis")
- [ ] Selection is preserved across exports (practitioners don't re-select every time)
- [ ] Clear indication of dataset completeness when subset selected (practitioners understand what's excluded)

### Data Integrity
- [ ] Row-level data integrity maintained regardless of column selection
- [ ] Summable metrics (costs, quantities) remain accurate when columns excluded
- [ ] Selection doesn't break FOCUS conformance (selected columns still follow FOCUS requirements)
- [ ] Documentation clarifies dependencies between columns (e.g., CommitmentDiscountId requires CommitmentDiscountStatus for meaningful analysis)

### Documentation & Transparency
- [ ] Available columns documented (what can be selected)
- [ ] Column dependencies documented (which columns are typically needed together)
- [ ] Impact of column exclusion explained (what analysis becomes impossible with subset)
- [ ] Examples provided for common selection patterns

### Practitioner Impact
- [ ] Reduced dataset size (measured in % reduction from full dataset)
- [ ] Faster data transfer and query performance
- [ ] Lower storage and egress costs
- [ ] Simplified ETL pipelines (fewer columns to transform/map)
- [ ] Ability to adopt FOCUS incrementally (start with core columns, add others as needed)

---

## Proposed Solution

### Attribute: Dataset Delivery

Create a new attribute focused on how practitioners receive/configure their datasets.

**Core Requirements:**

| Requirement | Keyword |
|-------------|---------|
| Data generators SHOULD provide column selection capability allowing practitioners to choose which columns to include in exported datasets | SHOULD |
| Column selection SHOULD support both FOCUS standard columns and custom columns | SHOULD |
| When column selection is provided, data generators SHOULD allow practitioners to exclude custom columns while retaining all FOCUS standard columns | SHOULD |

### Scope Decisions

**In Scope for Dataset Delivery attribute:**
- Column selection capability (SHOULD)
- Support for both FOCUS and custom columns
- Ability to exclude custom columns while keeping FOCUS columns

**Out of Scope (may be addressed separately or later):**
- Predefined column groups/presets (implementation detail)
- UI/API requirements (implementation detail)
- Column dependency documentation (could be supporting content)
- Mandatory vs. optional column distinction (complex, may need more discussion)

---

## Impact on FOCUS Specification

- Adds a new attribute category: practitioner-to-generator requirements
- Complements Scenario Completeness by allowing practitioners to manage the additional columns it introduces
- Provides clear guidance for data generators on column selection expectations

---

## Supporting Organizations

- FinOps Foundation
- Caligo

---

## Related Work

| Issue | Title | Status | Relationship |
|-------|-------|--------|--------------|
| #1091 | Add column selection as NFR | Open | Primary FR |
| #1094 | Add non-FOCUS columns to FOCUS datasets | Open | Creates need for column selection |
| #1018 | (Referenced in #1091) | - | Related community discussion |

---

## GDrive Resources (FOCUS Working Group Members Only)

- [1091 Column selection as a NFR Ideation Doc](https://docs.google.com/document/d/1AYF1amJRVU0y6bJWmi05GWOJYqCe2rLTDRRmheFkRqo/edit?usp=drive_link)
- [1091 Column selection as a NFR](https://drive.google.com/drive/folders/1lGHQXsnI_ueDAhKSpv0jY8ekb7zI6yzB?usp=drive_link)
