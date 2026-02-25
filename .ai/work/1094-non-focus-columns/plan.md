# Implementation Plan: Non-FOCUS Columns

## Goal

Increase FOCUS adoption by enabling customers to achieve the same analysis and reporting scenarios with FOCUS datasets that are currently only possible with native datasets.

---

## Phased Approach

### Phase 1: Research & Analysis
Gather evidence and confirm alignment before drafting.
- **Spec audit:** Identify all existing mentions of custom column requirements across the specification
- **Alignment review:** Confirm the proposed supported features content aligns with the new attribute vision
- Define precise normative requirements to propose
- **Evidence collection:** Document missing columns and the scenarios they enable

**Purpose:** Build the foundation and evidence needed for drafting.

#### Evidence Needed
To support the proposal, we need to demonstrate:
1. **Scenario Gap Examples** - What analyses/workflows require native columns that aren't in FOCUS?
   - Document specific scenarios enabled by missing columns
   - Example: "Azure Resource Group analysis requires x_ResourceGroup column"
2. **Missing Column Inventory** - What columns from provider docs should become x_ columns?
   - Copy columns and descriptions from AWS, Azure, GCP documentation
   - Focus on columns referenced in practitioner discussions (see `provider-columns-referenced.md`)
   - Not exhaustive - just enough to show scope
3. **Practitioner Column Usage** - What columns does your company use vs. what FOCUS provides?
   - Compare your company's native dataset columns with FOCUS columns
   - Identify gaps that block adoption
4. **Positive Example** - Microsoft already provides comprehensive x_ columns
   - Document Microsoft as model implementation

### Phase 2: Draft & TF Approval
- Consolidate research notes into single location
- Draft spec changes (see Implementation Deliverables)
- Work with TF-2 to refine the proposal
- TF-2 approves draft; maintainers agree on next steps

### Phase 3: Concern Resolution
If there are potential concerns outside TF-2 (e.g., AWS, GCP):
- Maintainers get involved and drive to closure
- Goal: full agreement to scoped version, or at least no blocking pushback
- Pre-socialize with provider representatives as needed

### Phase 4: Member Review & Merge
- Present final draft for member review (2-week review period)
- Address any blockers raised
- If no blockers, PR is approved and merged (can be implicit approval)

---

## Approval Process

```
Research & Analysis
        ↓
Draft & TF Approval
        ↓
Concern Resolution (if needed)
        ↓
Member Review & Merge
```

---

## Provider Engagement Strategy

### The Challenge
AWS is the primary provider to convince. GCP concerns are unknown (awaiting Sarah McMullin's response).

**AWS Core Objection:**
- **"Columns should NEVER change"** - If AWS adds non-FOCUS columns that later become FOCUS columns, those columns would need to change names, breaking customers.

**AWS Contact:** Letian Feng

**Historical Context:**
- This concern led to removal of native column requirement (#617/#838) in v1.2
- AWS hasn't engaged in solution discussions yet

### Proposed Solutions for AWS
1. **Column Preservation Approach:**
   - Keep non-FOCUS versions of columns available even after FOCUS equivalents are introduced
   - Provide column selection capability so practitioners can choose old, new, or both columns
   - Enables migration on practitioners' own terms without breaking changes
   - Could add as SHOULD requirements or appendix guidance

2. **Practitioner Survey:**
   - Survey practitioners on importance of this capability
   - Gather input on how they'd like to see it addressed
   - Use results to inform requirement strength and implementation approach

### The Approach
1. **Be evidence-based** - Use audit findings, scenario gaps, and practitioner use cases
2. **Address AWS concern directly** - Propose column preservation approach
3. **Pre-socialize with Letian Feng** - Engage before formal TF-2 proposal
4. **Gather GCP input** - Wait for Sarah's response, then adapt strategy

### Evidence to Collect
- AWS objection documented (column stability concern)
- AWS solution approach documented (column preservation)
- GCP concerns (awaiting Sarah's response)
- Examples of native columns that should become `x_` columns (from provider docs)
- Practitioner column usage comparison (your company's dataset vs FOCUS)
- Scenario gap examples (what analyses require missing columns)

---

## Deliverables

New attribute: **Scenario Completeness** (`ScenarioCompleteness`)

- **Applies to:** Cost and Usage dataset only
- **Requirement strength:** MUST (let TF-2 discuss if adjustment needed)
- **Column selection:** NOT a blocker; keep separate from this work

---

### 1. Attribute File (CREATE)

**Path:** `specification/attributes/scenario_completeness.md`

Create attribute following structure in `guidelines/normative-requirements-guidelines.md`. Use `invoice_handling.md` as a reference for format.

**Requirements to include (order: MUST/MUST NOT first, then SHOULD):**

| # | Requirement | Keyword |
|---|-------------|---------|
| 1 | Data generators MUST include custom columns for all information present in their native cost and usage dataset that is not represented in FOCUS columns | MUST |
| 2 | Custom columns MUST NOT duplicate information already captured in FOCUS columns | MUST NOT |
| 3 | When native data is transformed into FOCUS columns, data generators MUST NOT add custom columns for the original native representation | MUST NOT |
| 4 | Custom columns MUST maintain the same granularity and accuracy as their native dataset equivalents | MUST |
| 5 | When rows are split or aggregated to conform to FOCUS requirements, custom column values MUST be handled consistently to preserve data integrity | MUST |
| 6 | Data generators SHOULD include custom columns that enable correlation between FOCUS and native datasets (e.g., native charge identifiers) | SHOULD |
| 7 | Data generators SHOULD provide documentation describing custom columns, their purpose, and relationship to native columns | SHOULD |
| 8 | Data generators SHOULD provide conformance documentation indicating full, partial, or non-conformance with explanations | SHOULD |
| 9 | Data generators MAY preserve non-FOCUS versions of custom columns even after FOCUS equivalents are introduced to enable migration without breaking changes | MAY |

**Reference:** `guidelines/editorial-guidelines.md` for formatting conventions.

---

### 2. Attributes Index (UPDATE)

**Path:** `specification/attributes/attributes.mdpp`

Add include directive after `invoice_handling.md`:
```
!INCLUDE "scenario_completeness.md",1
```

**Reference:** `guidelines/markdownpp-guidelines.md`

---

### 3. Dataset Reference (UPDATE)

**Path:** `specification/datasets/cost_and_usage/dataset.md`

Add conformance requirement in Business/Contextual Attributes Conformance group:
```
* CostAndUsage MUST conform to [ScenarioCompleteness](#scenariocompleteness) requirements.
```

**Reference:** `guidelines/normative-requirements-guidelines.md` § Dataset Requirements

---

### 4. Requirements Model - Attribute Rules (CREATE)

**Path:** `specification/requirements_model/model_rules/attributes/scenariocompleteness.json`

Create model rules for all 8 requirements:
- Composite root: `ScenarioCompleteness-A-000-M`
- Atomic rules: `ScenarioCompleteness-A-001-M` through `A-005-M` (MUST), `A-006-O` through `A-008-O` (SHOULD)
- Set `ModelVersionIntroduced: "1.4"`, `Status: "Active"`

**Reference:** `guidelines/writing-requirements-model-guidelines.md` for CRID format and templates. Use `columnhandling.json` as structural reference.

---

### 5. Requirements Model - Dataset Rules (UPDATE)

**Path:** `specification/requirements_model/model_rules/datasets/costandusage.json`

Add `ScenarioCompleteness-A-000-M` to Dependencies array in `CostAndUsage-D-000-M`.

---

### 6. Supporting Content (CREATE)

**Path:** `supporting_content/attributes/scenario_completeness.md`

Include these sections:
1. Design rationale (why attribute exists, relationship to Column Handling)
2. When to include custom columns (4 scenarios)
3. When NOT to include custom columns (3 anti-patterns)
4. Correlation guidance (FOCUS-to-native dataset joins)
5. Aggregation/splitting examples
6. Provider-specific examples (AWS, Azure, GCP, OCI)

**Reference:** `guidelines/editorial-guidelines.md`, existing files in `supporting_content/attributes/`

---

### 7. Supported Features (UPDATE - if needed)

**Path:** `specification/supported_features/custom_columns.md`

Reference the new Scenario Completeness attribute if appropriate.

---

### Build Validation

```bash
cd specification
python validate_includes.py spec.mdpp        # Verify includes
make clean && make                            # Build + lint
cd requirements_model && python -m pytest tests/  # Test model
```

---

## Success Criteria

- Customers who were blocked on FOCUS adoption due to missing native data are unblocked
- Practitioners can retire native dataset queries and use FOCUS exclusively for cost and usage analysis
- Provider FOCUS exports include custom columns that cover all native dataset information
