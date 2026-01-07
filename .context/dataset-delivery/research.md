# Research: Dataset Delivery (Column Selection)

> Summary of research findings for the Dataset Delivery attribute.
>
> **Historical context:** The decision to create Dataset Delivery as a separate attribute was made during the Scenario Completeness (#1094) work. See `.context/non-focus-columns/research.md` for the full analysis that led to this decision.

---

## Why a Separate Attribute?

### The Question

Should column selection be part of Scenario Completeness attribute, a separate attribute, or excluded entirely?

### Analysis

**Issue #1091 Context:**

- Column selection is a separate, open feature request with its own acceptance criteria
- It focuses on allowing practitioners to select subsets of columns before/during export
- Categorized as "Supporting Content" not an attribute refinement
- Has its own set of supporting organizations (FinOps Foundation, Caligo)
- Level of ambiguity rated 4/5 (high complexity)

**Feature Request #1094 Reference:**

- feature-request.md lists column selection as a SHOULD, not MUST
- Lists #1091 as "Blocking dependency" in Related Work section
- plan.md explicitly states "Column selection: NOT a blocker; keep separate from this work"

**Key Considerations:**

1. **Scope Mixing:** Scenario Completeness defines what data generators must produce; column selection defines what practitioners can request. These are different actors and different directions of requirement.
2. **Broader Scope:** Column selection applies to ALL columns (FOCUS + custom), not just custom columns.
3. **Discoverability:** "Scenario Completeness" doesn't suggest column selection capability; practitioners wouldn't find it there.
4. **Conceptual Gap:** The spec currently has no concept for "how practitioners configure what they receive" - this is a new category.

### FOCUS Spec Conceptual Layers

| Layer | Purpose | Direction | Examples |
|-------|---------|-----------|----------|
| Columns | WHAT data fields exist | Generator → Practitioner | BilledCost, ResourceId |
| Attributes | HOW columns behave | Generator → Practitioner | ColumnHandling, NullHandling |
| Metadata | WHAT describes the dataset | Generator → Practitioner | DatasetInstanceMetadata |
| Supported Features | WHAT you can do with it | Practitioner → Data | CostComparison, EffectiveCost |
| **Dataset Delivery (new)** | **HOW you receive the dataset** | **Practitioner → Generator** | **Column selection** |

Column selection is the first **practitioner-to-generator** requirement. Everything else flows the other direction.

### Decision: SEPARATE ATTRIBUTE - "Dataset Delivery"

**Rationale:**

1. Column selection doesn't fit in Scenario Completeness conceptually (different actors, different direction)
2. Naming it clearly ("Dataset Delivery") makes it discoverable
3. Separates concerns: Scenario Completeness = what must be available; Dataset Delivery = how practitioners access it
4. Allows future expansion (format selection, etc.) without renaming
5. Follows the narrow-scope, single-concern attribute pattern

**Relationship to Scenario Completeness:**

- Scenario Completeness ensures all scenario-enabling columns **exist**
- Dataset Delivery ensures practitioners can **choose which ones to receive**
- Together they address: "Include everything needed, but let me pick what I want"

---

## Attribute Design Patterns

### Existing Attribute Patterns

Based on review of existing FOCUS attributes:

**Format Attributes** (the majority):

- `StringHandling`, `NumericFormat`, `CurrencyFormat`, `DateTimeFormat`, `JsonObjectFormat`, `KeyValueFormat`, `UnitFormat`
- Each addresses ONE specific data format requirement
- Apply to columns of that type across the entire dataset

**Structural Attributes** (equally narrow):

- `ColumnHandling`: Covers ONLY naming conventions and column ordering
- `NullHandling`: Covers ONLY how to represent missing values
- `InvoiceHandling`: Covers ONLY invoice-level completeness and charge representation
- `DiscountHandling`: Covers ONLY how discounts are applied to rows and amortized

**Key Pattern:** Attributes are highly focused, narrow-scope, single-concern.

### Dataset Delivery Follows the Pattern

- Single concern: column selection capability
- Narrow scope: SHOULD provide selection, support all column types, allow custom exclusion
- Not mixing: doesn't combine with format, handling, or completeness requirements

---

## Provider Support

### Current State

| Provider | Column Selection Support | Notes |
|----------|-------------------------|-------|
| AWS | Yes | CUR 2.0 allows column selection |
| GCP | Yes | BigQuery export allows column selection |
| Microsoft | Partial | Some selection capability in Cost Management |
| OCI | Unknown | Needs research |

**Implication:** Column selection is not controversial from a provider implementation perspective - major providers already support it.

---

## Scope Decisions

### In Scope for Dataset Delivery Attribute

1. **Column selection capability** - SHOULD provide mechanism
2. **All column types** - Must support FOCUS standard + custom columns
3. **Custom column exclusion** - Allow excluding x_ columns while keeping FOCUS columns

### Out of Scope (Deferred)

1. **Predefined column groups/presets** - Implementation detail, not spec requirement
2. **UI/API requirements** - How selection is exposed is provider choice
3. **Column dependency documentation** - Could be supporting content
4. **Mandatory vs. optional column distinction** - Complex topic, needs more discussion
5. **Selection persistence** - Implementation detail

### Rationale for Narrow Scope

The #1091 feature request has extensive acceptance criteria (UI, presets, groups, persistence). These are valuable but represent **implementation guidance** rather than **specification requirements**.

The attribute should establish:

- That column selection SHOULD be available
- That it applies to all column types
- That practitioners can get FOCUS-only if desired

How providers implement this is their choice.

---

## Files Required for Implementation

Based on the Scenario Completeness implementation pattern:

### Specification Files

| File | Purpose | Action |
|------|---------|--------|
| `specification/attributes/dataset_delivery.md` | Attribute definition | CREATE |
| `specification/attributes/attributes.mdpp` | Attributes index | UPDATE (add include) |
| `specification/datasets/cost_and_usage/dataset.md` | Dataset conformance | UPDATE (add conformance line) |
| `specification/requirements_model/model_rules/attributes/datasetdelivery.json` | Requirements model | CREATE |
| `specification/requirements_model/model_rules/datasets/costandusage.json` | Dataset rules | UPDATE (add dependency) |

### Supporting Content Files

| File | Purpose | Action |
|------|---------|--------|
| `supporting_content/attributes/dataset_delivery.md` | Design rationale, examples | CREATE |

### Validation

- Build succeeds
- Requirements model tests pass
- Attribute follows existing patterns

---

## Future Scope: What Else Fits in Dataset Delivery?

The name "Dataset Delivery" was chosen intentionally to allow expansion beyond column selection. This section explores what else conceptually fits within this attribute category.

### The Conceptual Boundary

Dataset Delivery covers **how practitioners configure what they receive** from data generators. This is distinct from:

- **What data exists** (Columns, Scenario Completeness)
- **How data is formatted** (Format attributes like NumericFormat, DateTimeFormat)
- **What the data describes** (Metadata)

Dataset Delivery is about the **delivery mechanism and practitioner choice**.

### Candidates for Future Inclusion

#### 1. Format Selection

**Concept:** Allow practitioners to choose output format (Parquet, CSV, JSON, etc.)

| Aspect | Analysis |
|--------|----------|
| Fits Dataset Delivery? | Yes - practitioner choice about how to receive data |
| Provider support | AWS (Parquet/CSV), GCP (BigQuery/CSV), Azure (various) |
| Complexity | Low - straightforward capability |
| Value | High - format affects storage costs, query performance, tooling compatibility |

**Possible requirement:** "Data generators SHOULD provide format selection capability allowing practitioners to choose the output format for exported datasets."

#### 2. Delivery Frequency / Scheduling

**Concept:** Allow practitioners to configure how often data is delivered (hourly, daily, on-demand)

| Aspect | Analysis |
|--------|----------|
| Fits Dataset Delivery? | Yes - practitioner choice about when/how to receive data |
| Provider support | Variable - some providers offer scheduling, others don't |
| Complexity | Medium - involves infrastructure considerations |
| Value | Medium - affects data freshness vs. cost tradeoff |

**Possible requirement:** "Data generators SHOULD provide delivery frequency options allowing practitioners to balance data freshness with processing costs."

#### 3. Incremental vs. Full Export

**Concept:** Allow practitioners to receive only changed/new data vs. full dataset refresh

| Aspect | Analysis |
|--------|----------|
| Fits Dataset Delivery? | Yes - practitioner choice about data scope |
| Provider support | Variable - some support incremental, others full only |
| Complexity | High - requires change tracking infrastructure |
| Value | High - massive impact on data transfer volumes |

**Possible requirement:** "Data generators SHOULD provide incremental export capability allowing practitioners to receive only new or modified data."

#### 4. Compression Options

**Concept:** Allow practitioners to choose compression (gzip, snappy, none)

| Aspect | Analysis |
|--------|----------|
| Fits Dataset Delivery? | Yes - practitioner choice about delivery optimization |
| Provider support | Generally supported across providers |
| Complexity | Low - straightforward capability |
| Value | Medium - affects transfer time and storage |

**Possible requirement:** "When providing file-based exports, data generators SHOULD support compression options."

#### 5. Partitioning Strategy

**Concept:** Allow practitioners to configure how data is partitioned (by date, by account, etc.)

| Aspect | Analysis |
|--------|----------|
| Fits Dataset Delivery? | Borderline - affects both delivery and data structure |
| Provider support | Variable - some offer partitioning options |
| Complexity | Medium - involves data organization decisions |
| Value | High - affects query performance significantly |

**Assessment:** This might be better as a separate attribute or supporting content, as it affects data structure not just delivery.

### Candidates That Don't Fit

#### Data Filtering / Row Selection

**Concept:** Allow practitioners to filter rows (e.g., only certain accounts, date ranges)

**Why it doesn't fit:** This crosses into data content/completeness territory. A filtered dataset may not meet Scenario Completeness requirements. Row filtering is fundamentally different from column selection because:

- Column selection: You get all rows, fewer columns
- Row filtering: You get fewer rows, potentially missing data

Row filtering could break data integrity (e.g., missing commitment rows that explain discounts).

#### Data Transformation

**Concept:** Allow practitioners to request transformed data (aggregated, pivoted, etc.)

**Why it doesn't fit:** Transformation changes what the data IS, not how it's delivered. This would conflict with FOCUS column definitions and data integrity requirements.

#### Access Control / Authentication

**Concept:** Define how practitioners authenticate to receive data

**Why it doesn't fit:** This is security/infrastructure, not data delivery configuration. It's outside FOCUS scope.

### Recommended Phasing

| Phase | Capability | Rationale |
|-------|------------|-----------|
| 1.4 | Column selection | Core need, well-understood, addresses Scenario Completeness burden |
| Future | Format selection | Low complexity, high value, natural extension |
| Future | Compression options | Low complexity, pairs well with format selection |
| Future | Incremental export | High value but higher complexity, needs more provider input |
| Evaluate | Delivery frequency | Depends on provider architecture, may be too implementation-specific |

### Supporting Content Implications

The supporting content for Dataset Delivery should:

1. Explain the conceptual boundary (what fits vs. doesn't)
2. Describe current scope (column selection) and why
3. Acknowledge future expansion possibilities
4. Provide guidance on common selection patterns
5. Include provider-specific examples of how selection is implemented

---

## Open Questions

1. **Mandatory columns:** Should some columns be non-excludable? (e.g., BilledCost, ChargePeriodStart)
2. **Conformance impact:** If a practitioner excludes columns, is the subset still "FOCUS conformant"?
3. **Format selection timing:** Should format selection be added now or in a future version?

These can be addressed in TF discussion or deferred to future versions.
