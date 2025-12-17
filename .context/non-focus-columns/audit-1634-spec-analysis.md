# Audit: Non-FOCUS Column Requirements in FOCUS Spec 1.3

**Issue:** #1634  
**Date:** 2025-12-15  
**Author:** AI Audit (per TF-2 discussion 2025-11-19)

## Executive Summary

This audit identifies all locations in the FOCUS 1.3 specification where requirements or expected behaviors for custom (non-FOCUS) columns are mentioned or alluded to. The findings reveal that custom column requirements are currently distributed across **10+ files**, creating potential for inconsistency and making it difficult for implementers to understand the full set of requirements.

**Recommendation:** Consolidate all custom column requirements into the existing `column_handling.md` attribute, with cross-references from other locations where custom columns are mentioned.

---

## Audit Findings

### 0. Supporting Content: Historical Context & Deferred Proposals

**File:** `supporting_content/attributes/column_handling.md`

This file contains critical historical context about the design decisions for custom columns and a **deferred proposal** that was removed from 1.2 for future discussion:

#### Deferred Proposal (removed from 1.2)

> When the provider publishes a non-FOCUS cost and usage dataset, the following applies:
> * Custom columns MUST be included for all information not covered by FOCUS columns that exists in the latest version of non-FOCUS cost and usage datasets.
> * Data generators SHOULD allow practitioners to select a subset of FOCUS or custom columns.
> * Data generators SHOULD provide conformance documentation that indicates whether the *FOCUS dataset* fully, partially, or does not conform to each requirement.
>   * Data generators SHOULD include an explanation of what does not conform when a requirement is not fully conformant so practitioners will know they need to handle the difference.

**Status:** This was explicitly removed to "discuss further in a future release."

#### Design Decision Rationale

The supporting content also documents the rationale for key design decisions:

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Prefix vs. Suffix | **Prefix** | Easier to identify as custom column even with limited space |
| Separator character | **Underscore** (`_`) | Works in variable names, common in spreadsheet/database columns |
| Identifying string | **`x_`** | Short, distinguishes from FOCUS columns, keeps custom columns together when sorted |

**Key insight:** "Prefixing custom columns establishes FOCUS as _the_ schema and custom columns as the exceptional thing that should be caveated."

---

### 1. Primary Location: Column Handling Attribute

**File:** `specification/attributes/column_handling.md`

This is the current home for custom column requirements. Contains:

| Requirement | Keyword | Description |
|-------------|---------|-------------|
| `x_` prefix | MUST | Custom columns MUST be prefixed with `x_` |
| Naming rules | SHOULD | Custom columns SHOULD follow FOCUS column naming rules |
| Column order | SHOULD | Custom columns SHOULD be listed after all FOCUS columns |
| No intermixing | SHOULD NOT | Custom columns SHOULD NOT be intermixed with FOCUS columns |
| Alphabetical sort | MAY/SHOULD | Columns MAY be sorted alphabetically, but custom columns SHOULD be after FOCUS columns |

**Additional context in intro paragraphs:**
- Supplemental columns may enable deeper analysis
- Data generators responsible for ensuring accuracy without duplicating FOCUS data
- Rows may be aggregated/split differently than non-FOCUS datasets
- Providers must maintain integrity of FOCUS-defined dimensions and metrics
- Must ensure accuracy of all dimensions and metrics (especially summable values)

---

### 2. Format/Handling Attributes with Custom Column References

#### 2.1 Null Handling
**File:** `specification/attributes/null_handling.md`

> "Custom columns SHOULD also follow the same formatting requirements."

**Expected Behavior:** Custom columns should use NULL for missing values, not empty strings or placeholders.

---

#### 2.2 Numeric Format  
**File:** `specification/attributes/numeric_format.md`

> "Custom numeric value capturing columns SHOULD adopt the same format requirements over time."

**Expected Behavior:** Custom numeric columns should follow the same integer/decimal formatting rules.

---

#### 2.3 String Handling
**File:** `specification/attributes/string_handling.md`

> "Custom string value capturing columns SHOULD adopt the same requirements over time."

**Expected Behavior:** Custom string columns should maintain casing, spacing, and consistency; preserve immutable values across billing periods.

---

#### 2.4 JSON Object Format
**File:** `specification/attributes/json_object_format.md`

> "Data Generator-defined custom columns whose contents contain a JSON object MUST have their object schema documented by the data generator."

**Expected Behavior:** Custom JSON columns require schema documentation. Also implies 3-level nesting limit SHOULD apply.

---

### 3. Invoice Handling (Mandatory Custom Column Scenario)
**File:** `specification/attributes/invoice_handling.md`

> "If an invoice-level charge appears on a customer invoice but cannot be expressed using existing FOCUS columns, data generators MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice charges reconciliation using the FOCUS dataset."

**Expected Behavior:** This creates a MUST requirement for custom columns in specific situations—when FOCUS columns cannot express invoice details.

---

### 4. Discount Handling
**File:** `specification/attributes/discount_handling.md`

> "If a service provider applies a discount that cannot be represented by a FOCUS column, they SHOULD include additional columns to identify the source of the discount."

**Expected Behavior:** Custom columns SHOULD be used to identify discount sources when FOCUS columns are insufficient.

---

### 5. Glossary Definition of FOCUS Dataset
**File:** `specification/glossary.md`

The "FOCUS Dataset" definition includes:

> "In addition to these standardized columns, data generators may include custom columns (prefixed with `x_`) where additional context is needed beyond what is captured in the defined FOCUS columns. If custom columns introduce record-splitting (i.e., a single original charge results in multiple rows), the data generator is responsible for ensuring that all cost and quantity metrics still meet the aggregation and consistency rules required by the specification."

**Expected Behavior:** 
- Custom columns require `x_` prefix
- Record-splitting via custom columns must maintain aggregation/consistency of cost and quantity metrics

---

### 6. Dataset Instance Definition
**File:** `specification/glossary.md`

> "A Data Generator may provide multiple dataset instances of the same FOCUS dataset, each with different properties such as time granularity or differing custom column inclusions."

**Expected Behavior:** Different dataset instances can have different custom column sets.

---

### 7. JSON Column Property Prefixing (Multiple Locations)

#### 7.1 SkuPriceDetails
**File:** `specification/datasets/cost_and_usage/columns/skupricedetails.md`

> "Property key MUST begin with the string 'x_' unless it is a FOCUS-defined property."

**Expected Behavior:** Properties within SkuPriceDetails JSON must use `x_` prefix for custom keys.

---

#### 7.2 ContractApplied
**File:** `specification/datasets/cost_and_usage/columns/contractapplied.md`

> "Contract application property custom key-value pairs MUST be prefixed with a consistent `x_` prefix..."
> "Contract application property custom key-value pairs MUST be documented by the data generator."
> "Contract application property custom key-value pairs MUST NOT be nested."
> "Contract application property keys MUST begin with the string 'x_' unless it is a FOCUS-defined allocation property."

**Expected Behavior:** Custom properties within ContractApplied JSON require `x_` prefix, documentation, and cannot be nested.

---

#### 7.3 AllocatedMethodDetails
**File:** `specification/datasets/cost_and_usage/columns/allocatedmethoddetails.md`

> "Allocation property keys MUST begin with the string 'x_' unless it is a FOCUS-defined allocation property."
> "AllocatedMethodDetails root object MAY contain additional data generator-defined items, in addition to 'Elements'."

**Expected Behavior:** Custom properties in AllocatedMethodDetails require `x_` prefix.

---

### 8. Overview Document
**File:** `specification/overview.md`

> "The specification supports extensibility through structured naming conventions (e.g., x_ custom columns), conditional requirements, and a version-aware schema approach."

**Expected Behavior:** High-level acknowledgment of extensibility mechanism.

---

### 9. Supported Features: Custom Columns
**File:** `specification/supported_features/custom_columns.md`

References `x_CustomColumn` as a placeholder for custom columns in SQL examples.

**Expected Behavior:** Documents that FOCUS supports custom columns for reporting not covered by standard columns.

---

### 10. Metadata Examples
**File:** `specification/appendix/metadata_examples/adding_new_columns_example.md`

Example scenario using `x_awesome_column1`, `x_awesome_column2`, `x_awesome_column3`.

**Expected Behavior:** Demonstrates proper `x_` prefixing in metadata scenarios.

---

### 11. Data CSV Examples
**Files in:** `specification/data/commitment_discount_flexibility/` and `specification/data/commitment_discount_scenarios/`

Multiple CSV files include example columns like `x_CommitmentDiscountUnitPrice`.

**Expected Behavior:** Sample data demonstrates proper `x_` prefixing.

---

### 12. Additional Supporting Content Files

#### 12.1 supporting_content/attributes/null_handling.md
Notes discussion of "two main classes - user-controlled columns and provider-controlled columns"

#### 12.2 supporting_content/attributes/string_handling.md
Documents discussion around:
- Provider-controlled columns: consistency for provider-specified String values
- End-user-controlled columns: consistency for user-controlled String columns  
- Provider-defined vs user-input String value handling

---

### 13. Google Drive (Not Audited)

**Note:** Additional relevant content may exist in Google Drive documents that are not included in this repository. This could include:
- Working group meeting notes
- Design decision documents
- Historical proposals and discussions
- Implementation guidance drafts

⚠️ **Action Required:** Manual review of Google Drive content is needed to complete this audit.

---

## Summary of All Custom Column Requirements

| Requirement | Keyword | Current Location(s) |
|-------------|---------|---------------------|
| Prefix with `x_` | MUST | column_handling.md, glossary.md, skupricedetails.md, contractapplied.md, allocatedmethoddetails.md |
| Follow FOCUS naming rules | SHOULD | column_handling.md |
| Place after FOCUS columns | SHOULD | column_handling.md |
| Don't intermix with FOCUS columns | SHOULD NOT | column_handling.md |
| Use NULL for missing values | SHOULD | null_handling.md |
| Follow numeric format rules | SHOULD | numeric_format.md |
| Follow string handling rules | SHOULD | string_handling.md |
| Document JSON object schemas | MUST | json_object_format.md |
| Include for invoice reconciliation when needed | MUST | invoice_handling.md |
| Include to identify discount sources when needed | SHOULD | discount_handling.md |
| Maintain aggregation consistency for record-splitting | MUST | glossary.md (FOCUS Dataset definition) |
| Custom JSON properties must be documented | MUST | contractapplied.md |
| Custom JSON properties must not be nested | MUST NOT | contractapplied.md |

### Deferred/Proposed Requirements (not yet normative)

| Requirement | Keyword | Source |
|-------------|---------|--------|
| Include all info from non-FOCUS datasets | MUST | supporting_content (deferred from 1.2) |
| Allow column subset selection | SHOULD | supporting_content (deferred from 1.2) |
| Provide conformance documentation | SHOULD | supporting_content (deferred from 1.2) |

---

## Recommendation

### Consolidate Requirements in Column Handling Attribute

All custom column requirements should be consolidated in `specification/attributes/column_handling.md` with the following structure:

#### Proposed Structure for column_handling.md

```markdown
## Requirements

### Column Names
[existing FOCUS column naming rules]

### Custom Column Requirements

Custom (e.g., service-provider-defined) columns that are not defined by FOCUS 
but included in a FOCUS dataset MUST follow these rules:

#### Naming
* Custom columns MUST be prefixed with a consistent `x_` prefix...
* Custom columns SHOULD follow the same naming rules as FOCUS columns.

#### Ordering
* Custom columns SHOULD be listed after all FOCUS columns.
* Custom columns SHOULD NOT be intermixed with FOCUS columns.
* Columns MAY be sorted alphabetically, but custom columns SHOULD be after all FOCUS columns.

#### Data Formats
* Custom columns SHOULD follow [NullHandling](#nullhandling) requirements.
* Custom columns capturing numeric values SHOULD follow [NumericFormat](#numericformat) requirements.
* Custom columns capturing string values SHOULD follow [StringHandling](#stringhandling) requirements.
* Custom columns containing JSON objects MUST have their object schema documented by the data generator.
* Custom columns containing JSON objects SHOULD NOT exceed 3 levels of nesting.

#### Data Integrity
* If custom columns introduce record-splitting (i.e., a single original charge 
  results in multiple rows), the data generator is responsible for ensuring 
  that all cost and quantity metrics still meet the aggregation and consistency 
  rules required by the specification.
* Data generators MUST NOT duplicate data in FOCUS columns when adding custom columns.

#### Documentation
* Data generators MUST document custom columns in their FOCUS implementation guide.

### Custom Properties in JSON Columns

Custom properties within FOCUS-defined JSON columns adhere to the following:
* Property keys MUST begin with the string "x_" unless it is a FOCUS-defined property.
* Custom properties MUST be documented by the data generator.
* Custom properties MUST NOT be nested (for columns that specify this requirement).
```

### Update Other Files with Cross-References

Other files that currently mention custom column requirements should be updated to reference the consolidated requirements in column_handling.md:

1. **null_handling.md** - Add: "See [Column Handling](#columnhandling) for custom column requirements."
2. **numeric_format.md** - Add: "See [Column Handling](#columnhandling) for custom column requirements."
3. **string_handling.md** - Add: "See [Column Handling](#columnhandling) for custom column requirements."
4. **json_object_format.md** - Add cross-reference to column handling
5. **invoice_handling.md** - Keep the specific MUST for invoice reconciliation, add cross-reference
6. **discount_handling.md** - Keep the specific SHOULD for discount sources, add cross-reference
7. **glossary.md (FOCUS Dataset)** - Simplify to reference column_handling.md

### Benefits of Consolidation

1. **Single source of truth** - Implementers can find all custom column requirements in one place
2. **Consistency** - Reduces risk of conflicting requirements across files
3. **Maintainability** - Easier to update requirements in one location
4. **Clarity** - Clear separation between FOCUS column requirements and custom column requirements

---

## Files to Update (Implementation Checklist)

### Specification Files
- [ ] `specification/attributes/column_handling.md` - Add consolidated custom column requirements
- [ ] `specification/attributes/null_handling.md` - Add cross-reference
- [ ] `specification/attributes/numeric_format.md` - Add cross-reference  
- [ ] `specification/attributes/string_handling.md` - Add cross-reference
- [ ] `specification/attributes/json_object_format.md` - Add cross-reference
- [ ] `specification/attributes/invoice_handling.md` - Add cross-reference (keep specific MUST)
- [ ] `specification/attributes/discount_handling.md` - Add cross-reference (keep specific SHOULD)
- [ ] `specification/glossary.md` - Simplify FOCUS Dataset definition, add cross-reference
- [ ] `specification/requirements_model/model_rules/attributes/columnhandling.json` - Update model rules

### Supporting Content Files
- [ ] `supporting_content/attributes/column_handling.md` - Review deferred proposals for inclusion in consolidated requirements
- [ ] `supporting_content/attributes/null_handling.md` - Update if needed
- [ ] `supporting_content/attributes/string_handling.md` - Update if needed

### External Sources (Manual Review Required)
- [ ] Google Drive documents - Review for additional custom column requirements or discussions

---

## GitHub Issue Research

### Related Issues Overview

| Issue | Title | Status | Relevance |
|-------|-------|--------|-----------|
| #1094 | Add non-FOCUS columns to FOCUS datasets as NFR | Open | **Primary FR** - defines completeness requirement |
| #1091 | Add column selection as NFR | Open | Blocking dependency for #1094 |
| #1098 | Add provider column to FOCUS column mappings as NFR | Open | Related - provider documentation |
| #1634 | Audit spec for existing mentions (this audit) | Open | Task from TF-2 |
| #617 | Revise glossary definition for FOCUS dataset | Closed | Completed work in 1.2 |
| #602 | Is inclusion of custom/native columns recommended | Closed | Original discussion that started this |
| #1129 | Add ability to add non-FOCUS provider columns | Closed | Duplicate of #1094 |

### Key Discussions from Issues

#### From #602 (Original Discussion - Oct 2024)

**Core Problem:** While the dataset is designed for standardized reporting across providers, there is increasing demand from practitioners to include custom or native columns specific to a provider's offerings.

**Resolution:** The group agreed to create a framework for including custom columns but emphasized the need for guidelines to prevent over-customization. The specification will recommend custom/native columns where necessary, but their inclusion will need to follow specific rules to maintain overall standardization.

**Important observation from @ahullah:**
> If a provider wants to extend a record with a proprietary field, we would expect them to recalculate the metric columns to ensure they accurately represent activity, or at the least divide the metric values by the number of rows they need to add. Otherwise, both usage hours and cost are artificially doubled.

#### From #617 (Work Item - Closed)

This led to the current glossary definition update (PR #682) which added:
> "In addition to these standardized columns, data generators may include custom columns (prefixed with `x_`) where additional context is needed beyond what is captured in the defined FOCUS columns. If custom columns introduce record-splitting (i.e., a single original charge results in multiple rows), the data generator is responsible for ensuring that all cost and quantity metrics still meet the aggregation and consistency rules required by the specification."

**Noted for future:** During meetings, it was suggested that in addition to the glossary term, this should be mentioned explicitly in the **Introduction** and/or adding an **appendix**.

#### From #1094 (Primary FR - TF-2 Nov 2024)

**TF-2 Meeting Nov 19, 2024 - Key Decisions:**
- Custom columns for correlation should NOT guarantee uniqueness within a FOCUS dataset (uniqueness claim only valid for source provider dataset)
- Scope confirmed: addressing correlation needs, not necessarily creating universal unique identifiers
- Custom columns remain appropriate location (not promoting to FOCUS standard columns)

**Use Cases Validated:**
1. **Providers with unique charge IDs**: Should include unique identifiers as custom columns (e.g., OCI reference numbers) to enable correlation
2. **Providers without unique identifiers**: Should provide columns (or recipe/documentation) enabling correlation between FOCUS and proprietary datasets

**Blocking Dependency:** FR #1091 (column selection) - addresses concerns about column proliferation across multiple SaaS providers

#### From #1091 (Column Selection NFR)

**Debate points from Sep 22 Maintainers:**
- Is this truly a prerequisite of #1094? "Could not the data generators elect to do this themselves?"
- Is this within current mandate of FOCUS? "Is not our spec currently a data delivery format, and not a definition of provider features?"

**Resolution:** Column selection doesn't enable new analysis - it improves dataset consumption experience. Every supported feature benefits equally from column selection.

#### From #1098 (Provider Mappings NFR)

**Key insight from @kk09v:**
> I'd support this as SHOULD and this almost feels necessary to support #1094. As a data provider: How would I certify that all columns are included in FOCUS as x_ columns if I'm not explicit about what existing columns are replaced by FOCUS columns?

**Resources identified:**
- FOCUS Converters repository has structured mapping configurations
- Microsoft's [conversion](https://learn.microsoft.com/en-us/cloud-computing/finops/focus/convert) and [validation](https://learn.microsoft.com/en-us/cloud-computing/finops/focus/validate) documentation cited as exemplary

### Action Items from TF-2 (Nov 19, 2024)

- [x] **Michael / Irena**: Audit spec for existing mentions of non-focus column requirements (#1634) - **This document**
- [ ] **Michael**: Review and provide feedback on supported features section (#1635)
- [ ] **Matt**: Format Irena's use case descriptions into acceptance criteria (#1636)

### Timeline

| Date | Event |
|------|-------|
| Oct 2024 | #602 discussion begins |
| Oct 2024 | #617 work item created |
| May 2025 | #1094 FR created with full problem statement |
| May 2025 | PR #682 merged (glossary update) |
| Nov 2025 | TF-2 validates use cases, creates audit task #1634 |
| Dec 2025 | Audit completed (this document) |

