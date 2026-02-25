# Non-FOCUS Columns Initiative

> **Status:** In Development  
> **Target Release:** 1.4  
> **Primary Issue:** [#1094](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1094)  
> **Related Issues:** #1091 (column selection), #1098 (provider mappings), #1634 (audit)

---

## Problem Statement

FOCUS standardizes cost and usage data with a consistent set of required columns. However, the diversity of provider offerings and the pace of change in services mean that some data necessary for accurate analysis may not map neatly into existing FOCUS columns. Without a clear expectation for providers to include supplemental columns, practitioners risk losing critical context that is available in non-FOCUS datasets.

---

## Use Cases

### 1. Migrating from Native to FOCUS Datasets
**As a** FinOps Practitioner migrating from native to FOCUS datasets  
**I need** all information from my native billing dataset available in FOCUS (either as standard or custom columns)  
**So that** I can adopt FOCUS without losing critical billing context needed for accurate analysis and decision-making

### 2. Analyzing Provider-Specific Features
**As a** FinOps Practitioner analyzing provider-specific features  
**I need** custom columns for provider-unique attributes (e.g., capacity type, marketplace metadata, service-specific configurations)  
**So that** I can perform provider-native optimizations and cost attribution that FOCUS standard columns don't yet support

### 3. Validating FOCUS Data Completeness
**As a** FinOps Practitioner validating FOCUS data completeness  
**I need** explicit confirmation that all native dataset columns are mapped to FOCUS standard or custom columns  
**So that** I can trust FOCUS data has no information loss and confidently retire native dataset queries

### 4. Implementing FOCUS as a Data Generator
**As a** FOCUS Data Generator implementing FOCUS alongside native exports  
**I need** clear requirements for when to include custom columns  
**So that** I can ensure completeness without duplicating data already standardized in FOCUS columns

### 5. Building FOCUS-Compatible Analytics
**As a** FinOps Tooling Vendor building FOCUS-compatible analytics  
**I need** to know which custom columns exist across providers  
**So that** I can support provider-specific features while maintaining FOCUS-based core functionality

### 6. Correlating FOCUS and Proprietary Datasets
**As a** FinOps Practitioner correlating FOCUS and proprietary datasets  
**I need** custom columns that enable reliable joining between FOCUS and native datasets (e.g., `x_ChargeId` or documented correlation keys)  
**So that** I can cross-reference FOCUS data with proprietary details without maintaining duplicate large datasets or building fragile correlation logic

---

## Acceptance Criteria

### Completeness Requirements
- [ ] FOCUS datasets include custom columns (x_ prefix) for all information present in native datasets but not covered by FOCUS standard columns
- [ ] No native dataset information is lost when practitioners adopt FOCUS datasets
- [ ] Custom columns maintain same granularity and accuracy as native dataset equivalents
- [ ] Practitioners can achieve parity between FOCUS and native dataset analyses using combination of standard and custom columns

### Data Integrity & Consistency
- [ ] Custom columns do NOT duplicate data already captured in FOCUS standard columns
- [ ] When native data transforms into FOCUS standard columns, custom columns are NOT added for the native representation
- [ ] FOCUS-defined metrics and dimensions (particularly summable values like costs and quantities) maintain integrity when custom columns are added
- [ ] Row-level aggregation and splitting to align with FOCUS requirements preserves accuracy across all custom columns
- [ ] Providers include custom columns that enable reliable correlation between FOCUS and proprietary datasets:
  - [ ] Providers with existing unique charge identifiers (e.g., `ChargeId`) include them as custom columns (e.g., `x_ChargeId`)
  - [ ] Providers without existing identifiers document correlation guidance and include minimal custom columns required for dataset joins
  - [ ] Correlation columns serve as linking mechanisms; uniqueness within FOCUS datasets is not required

### Naming & Documentation
- [ ] Custom columns follow x_ prefix naming convention consistently
- [ ] Custom column naming avoids conflicts with current or planned FOCUS standard columns
- [ ] Data generators provide documentation describing custom columns, their purpose, and relationship to native dataset columns
- [ ] Documentation clarifies which native columns map to FOCUS standard vs. custom columns (integration with FR #1098)

### Practitioner Impact
- [ ] Practitioners can migrate from native to FOCUS datasets without analytical capability loss
- [ ] Provider-specific optimization opportunities remain accessible via custom columns
- [ ] Practitioners understand which capabilities require custom columns vs. FOCUS standard columns
- [ ] Cross-provider analysis uses FOCUS standard columns; provider-specific analysis supplements with custom columns

---

## Proposed Solution

### Normative Requirements

When publishing a non-FOCUS dataset alongside a FOCUS dataset:

* **MUST** include provider-defined custom columns for all information present in the non-FOCUS dataset but absent from FOCUS columns.
* **SHOULD** allow practitioners to select a subset of FOCUS and custom columns.
* **SHOULD** provide conformance documentation indicating whether the dataset fully, partially, or does not conform to each requirement.
* **SHOULD** include explanations for partial or non-conformance so practitioners can adjust their workflows accordingly.

### Custom Column Guidelines

**When to Include Custom Columns:**
- Native dataset contains information with no FOCUS standard column equivalent
- Provider-specific features or attributes require additional context beyond FOCUS standard columns
- Marketplace metadata or publisher information not captured in FOCUS columns
- Service-specific configuration or capacity details needed for optimization

**When NOT to Include Custom Columns:**
- Information is already captured in FOCUS standard column (avoid duplication)
- Native column is transformed/aggregated into FOCUS standard column (document in mapping, don't duplicate)
- Data would violate FOCUS metrics integrity (e.g., would break cost summation)

---

## Impact on FOCUS Specification

* Adds clarity that provider-defined columns are expected, not optional, to ensure comprehensive datasets.
* Creates a balance: providers retain flexibility to enrich datasets, while practitioners gain predictability in how supplemental data appears.

---

## Supporting Organizations

- Neos
- Twilio
- Microsoft
- FinOps Guys
- Electronic Arts

---

## Related Work

| Issue | Title | Status | Relationship |
|-------|-------|--------|--------------|
| #1094 | Add non-FOCUS columns to FOCUS datasets as NFR | Open | Primary FR |
| #1091 | Add column selection as NFR | Open | Blocking dependency |
| #1098 | Add provider column to FOCUS column mappings as NFR | Open | Related (documentation) |
| #1634 | Audit spec for existing mentions of non-focus column requirements | Open | Task (this audit) |
| #617 | Revise glossary definition for FOCUS dataset | Closed | Completed in 1.2 |
| #602 | Is inclusion of custom/native columns recommended | Closed | Original discussion |

---

## Tasks

- [ ] #1634 - Audit spec for existing mentions of non-focus column requirements
- [ ] #1635 - Review and provide feedback on supported features section
- [ ] #1636 - Format use case descriptions into acceptance criteria
- [ ] Consolidate custom column requirements into column_handling.md
- [ ] Update cross-references in related attribute files
- [ ] Draft enhanced "Custom Columns" supported feature content
