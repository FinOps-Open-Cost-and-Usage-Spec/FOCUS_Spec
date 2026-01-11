# Research: Dataset Configuration (Column Selection)

> Summary of research findings for the Dataset Configuration attribute.
>
> **Naming Note:** This attribute was originally called "Dataset Delivery" but was renamed to "Dataset Configuration" after analysis showed "delivery" implies push semantics, which doesn't account for datasets accessed via APIs, database tables, or query interfaces.

---

## Attribute Naming Analysis

### The Problem with "Delivery"

"Dataset Delivery" implies:
- Push semantics (data is sent to you)
- Export-centric model (files delivered to storage)
- Doesn't account for: APIs, database tables, query interfaces, in-place access

### The Problem with "Access"

"Dataset Access" could imply:
- Permissions/authorization (who can access)
- Authentication mechanisms
- Security controls

### Terminology from Other Standards

| Standard/Technology | Term | What It Describes |
|---------------------|------|-------------------|
| **GraphQL** | Selection Set | Client specifies which fields to return |
| **OData** | $select Query Option | Clients request specific properties |
| **SQL/Relational Algebra** | Projection | Selecting specific columns (attributes) |
| **Parquet/Arrow** | Projection Pushdown, Column Pruning | Reading only needed columns |
| **FHIR** | _elements Parameter | Subset of elements to return |
| **Data Mesh (DPDS)** | Output Port | How data product exposes data |
| **AWS CUR** | Report Configuration, Data Export | Settings for what/how data is delivered |
| **Azure Cost Management** | Export Configuration | Settings for exported data |

### Key Observations

1. **GraphQL/OData use query-time terms** - "selection" happens at query time, not configuration time
2. **Parquet/Arrow use optimization terms** - "pruning" and "pushdown" are implementation details
3. **Cloud providers use configuration/export terms** - AWS uses "Data Exports", Azure uses "Export Configuration"
4. **Data Mesh uses "Output Port"** - describes how a data product exposes data

### Candidate Names

| Name | Pros | Cons |
|------|------|------|
| **Dataset Configuration** | Matches cloud provider patterns (AWS/Azure use "configuration"); clearly about settings; mechanism-neutral; expandable for future options | Generic - "configuration of what?" without context |
| **Dataset Options** | Simple; clearly about choices available to practitioners | Very generic; sounds like preferences rather than capabilities |
| **Dataset Availability** | Neutral about mechanism; encompasses all access patterns | Could be confused with uptime/reliability/SLA |
| **Dataset Access** | Mechanism-neutral; common term that works for APIs, databases, exports | Strong implication of permissions/authorization |
| **Dataset Customization** | Implies practitioner control; clear intent | Suggests modifying the data itself, not selecting what you get |
| **Dataset Retrieval** | About getting data | Implies pull semantics; doesn't fit database table scenario |
| **Dataset Output** | Matches Data Mesh "Output Port" concept | Sounds like the data itself rather than options for it |
| **Dataset Selection** | Matches GraphQL/OData patterns | Could be confused with selecting which dataset |
| **Column Selection** | Direct, specific to current scope | Too narrow if we add other capabilities later |

### Decision: "Dataset Configuration"

**Why "Configuration" was chosen:**

1. **Matches industry patterns**: AWS uses "Report Configuration", Azure uses "Export Configuration"
2. **Clearly about settings**: "Configure" unambiguously means "set options for"
3. **Mechanism-neutral**: Works for APIs, exports, database tables, query interfaces
4. **Expandable**: Can include column selection, format options, compression, etc.
5. **No permission connotation**: Unlike "access", doesn't imply authorization
6. **Practitioner-focused**: Configuration is something the practitioner does

**Why other options were rejected:**

- **Dataset Options**: Too generic, sounds like preferences
- **Dataset Availability**: Confusion with uptime/reliability
- **Dataset Access**: Strong permission/authorization connotation
- **Dataset Customization**: Implies modifying the data
- **Column Selection**: Too narrow for future expansion

**Usage examples:**
- "Dataset Configuration defines options available to practitioners when accessing FOCUS datasets."
- "CostAndUsage MUST conform to [DatasetConfiguration](#datasetconfiguration) requirements."
- "FOCUS datasets SHOULD support column selection."

### Attribute ID

`DatasetConfiguration` (following existing patterns like `ColumnHandling`, `NullHandling`)

### Rule ID Pattern

`DatasetConfiguration-A-000-M`, `DatasetConfiguration-A-001-O`, etc.
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

## Future Scope: Multiple Attributes

Analysis of configuration options revealed they naturally group into separate attributes based on the delivery medium they apply to. This follows the existing FOCUS pattern where columns have feature levels based on provider capabilities.

### The Conceptual Boundary

Dataset configuration options cover **how practitioners configure what they receive** from FOCUS datasets. This is distinct from:

- **What data exists** (Columns, Scenario Completeness)
- **How data is formatted** (Format attributes like NumericFormat, DateTimeFormat)
- **What the data describes** (Metadata)

### Delivery Mediums

FOCUS datasets can be delivered through different mediums, analogous to cloud service models:

| Medium | Analogy | Examples |
|--------|---------|----------|
| **Files** | IaaS - raw materials | S3 exports, file downloads, API file responses |
| **Tables** | PaaS - managed platform | Database tables, BigQuery, data warehouse |
| **UX** | SaaS - application | Dashboards, reports, cost management portals |

### Applicability Matrix

| Option | Files | Tables | UX |
|--------|:-----:|:------:|:--:|
| **All Mediums** | | | |
| Column selection | ✓ | ✓ | ✓ |
| Row aggregation | ✓ | ✓ | ✓ |
| Time granularity | ✓ | ✓ | ✓ |
| Schema versioning | ✓ | ✓ | ✓ |
| Row filtering | ✓ | ✓ | ✓ |
| **Files + Tables** | | | |
| Partitioning | ✓ | ✓ | - |
| Incremental refresh | ✓ | ✓ | - |
| Overwrite vs append | ✓ | ✓ | - |
| Scheduling | ✓ | ✓ | - |
| **Files Only** | | | |
| File format | ✓ | - | - |
| Compression | ✓ | - | - |

### Proposed Attribute Organization

Based on applicability, configuration options should be split into separate attributes with appropriate feature levels:

| Attribute | Options | Feature Level | Est. Requirements |
|-----------|---------|---------------|-------------------|
| **DatasetConfiguration** | Column selection, row aggregation, time granularity, schema versioning, row filtering | None (all datasets) | 10-15 |
| **DatasetDelivery** | Scheduling, incremental refresh, overwrite vs append, partitioning | Files or Tables | 8-12 |
| **DatasetFileHandling** | File format, compression | Files only | 5-8 |

**Rationale:**

1. **Feature levels**: Just like CommitmentDiscount columns are conditional on provider capability, delivery-specific options should only apply when the provider supports that delivery medium
2. **Discoverability**: Separate attributes make it clear which requirements apply to which scenarios
3. **Flexibility**: Providers only need to implement attributes relevant to their delivery mechanisms

### Configuration Options Summary

| Option | Requirement | Complexity | Value | Provider Support |
|--------|-------------|------------|-------|------------------|
| **Column selection** | MUST | Low | High | AWS, GCP, Azure |
| **Row aggregation** | SHOULD (default), SHOULD (opt-in/out) | Low | High | All |
| **Time granularity** | MUST (daily, hourly when applicable), SHOULD (monthly) | Low | High | AWS, Azure |
| **Schema versioning** | SHOULD | Low | High | All |
| **Row filtering** | SHOULD | Medium | High | All |
| **Metadata** | MUST | Low | High | All |

### Future Options (Deferred)

| Option | Proposed Attribute | Complexity | Value | Provider Support |
|--------|-------------------|------------|-------|------------------|
| **Partitioning** | DatasetDelivery | Medium | High | AWS, Azure |
| **Scheduling** | DatasetDelivery | Medium | Medium | Variable |
| **Incremental refresh** | DatasetDelivery | High | High | Variable |
| **Overwrite vs append** | DatasetDelivery | Low | Medium | AWS |
| **File format** | DatasetFileHandling | Low | High | AWS, GCP, Azure |
| **Compression** | DatasetFileHandling | Low | Medium | AWS, most tools |

### Final 1.4 Requirements

The following requirements were finalized for Dataset Configuration in FOCUS 1.4:

#### Column Selection (MUST)

- FOCUS datasets MUST allow selecting which columns to include
- FOCUS datasets MUST produce conformant column values regardless of which columns are included
- FOCUS datasets SHOULD sum metric columns by default when the selected dimension columns result in rows with identical values

#### Row Aggregation (SHOULD)

- FOCUS datasets SHOULD allow opting in or out of row aggregation (summing metrics)
- FOCUS datasets MUST sum metric column values when rows are aggregated
- FOCUS datasets SHOULD use case-insensitive matching when aggregating rows

#### Time Granularity (MUST)

- FOCUS datasets MUST allow selecting the time granularity based on ChargePeriodStart, when available
- FOCUS datasets MUST allow selecting daily granularity
- FOCUS datasets MUST allow selecting hourly granularity when the dataset includes costs priced at an hourly or lower grain
- FOCUS datasets SHOULD allow selecting monthly granularity
- FOCUS datasets MUST sum metric columns based on selected dimension columns with identical values when time granularity is changed

#### FOCUS Version Selection (SHOULD)

- FOCUS datasets SHOULD allow selecting the FOCUS version
- FOCUS datasets MUST NOT add or remove columns when a specific FOCUS version is selected

#### Row Filtering (SHOULD)

- FOCUS datasets SHOULD allow filtering rows by column values
- FOCUS datasets MUST use case-insensitive matching when filtering rows

#### Metadata (MUST)

- FOCUS datasets MUST include metadata describing the selected configuration options

### Candidates for Future Versions

#### Compression Options

**Concept:** Allow practitioners to choose compression (gzip, snappy, none)

- **Provider support:** Generally supported across providers
- **Complexity:** Low
- **Value:** Medium - affects transfer time and storage

**Assessment:** Natural pairing with format selection. Could be added when format selection is formalized, or left as implementation detail.

#### Partitioning Strategy

**Concept:** Allow practitioners to configure how data is partitioned (by date, by account, etc.)

- **Provider support:** AWS, Azure (partitionData option)
- **Complexity:** Medium - involves data organization decisions
- **Value:** High - affects query performance significantly

**Assessment:** Borderline - affects both configuration and data structure. May be better as supporting content guidance rather than a requirement.

#### Incremental vs. Full Export

**Concept:** Allow practitioners to receive only changed/new data vs. full dataset refresh

- **Provider support:** Variable - some support incremental, others full only
- **Complexity:** High - requires change tracking infrastructure
- **Value:** High - massive impact on data transfer volumes

**Assessment:** High value but high complexity. Needs more provider input before standardizing.

#### Delivery Frequency / Scheduling

**Concept:** Allow practitioners to configure how often data is delivered (hourly, daily, on-demand)

- **Provider support:** Variable
- **Complexity:** Medium - involves infrastructure considerations
- **Value:** Medium

**Assessment:** May be too implementation-specific for FOCUS to standardize.

#### File Versioning

**Concept:** Overwrite existing files vs. create new files on update

- **Provider support:** AWS CUR
- **Complexity:** Low
- **Value:** Medium - affects auditability vs. storage cost tradeoff

**Assessment:** Niche concern, may be better left to provider discretion.

#### Overwrite vs. Append

**Concept:** Whether new data overwrites existing files or appends to them

- **Provider support:** AWS CUR
- **Complexity:** Low
- **Value:** Medium - affects data pipeline design

**Assessment:** Related to file versioning. May be better left to provider discretion.

### Candidates That Don't Fit

#### Data Transformation (Pivoting/Reshaping)

**Concept:** Allow practitioners to request pivoted or reshaped data

**Why it doesn't fit:** Pivoting or reshaping changes what the data IS, not how it's made available. This would conflict with FOCUS column definitions.

**Note:** Row aggregation (summing metrics) IS supported as it produces mathematically equivalent data, just more efficiently represented.

#### Access Control / Authentication

**Concept:** Define how practitioners authenticate to receive data

**Why it doesn't fit:** This is security/infrastructure, outside FOCUS scope.

### Supporting Content Implications

The supporting content for Dataset Configuration should:

1. Explain the conceptual boundary (what fits vs. doesn't)
2. Describe current scope and rationale
3. Acknowledge future expansion possibilities
4. Provide guidance on common selection patterns
5. Include provider-specific examples

---

## Open Questions

1. **Mandatory columns:** Should some columns be non-excludable? (e.g., BilledCost, ChargePeriodStart)
2. **Conformance impact:** If a practitioner excludes columns, is the subset still "FOCUS conformant"?
3. **Format selection timing:** Should format selection be added now or in a future version?

These can be addressed in TF discussion or deferred to future versions.
