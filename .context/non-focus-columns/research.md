# Research: Non-FOCUS Columns Initiative

> Summary of research findings for the non-FOCUS columns completeness requirement.

---

## Completed Research

### Spec Audit (#1634)

**Primary deliverable:** Consolidated list of provider-native columns already referenced in FOCUS discussions.

#### Provider Columns Referenced
**File:** [provider-columns-referenced.md](provider-columns-referenced.md)

Comprehensive audit of all 53 supporting content column files. Key findings:

| Provider | Mapped to FOCUS | NOT in FOCUS |
|----------|-----------------|--------------|
| AWS | ~30 columns | ~13 columns |
| GCP | ~25 columns | ~7 columns |
| Microsoft | ~35 columns | ~5 columns |
| OCI | ~15 columns | ~5 columns |

**Columns explicitly noted as NOT available / no FOCUS equivalent:**
- AWS: Account name, `lineItem/LegalEntity`, `bill/BillingEntity`, reservation/SP ARNs, ContractedCost/UnitPrice
- GCP: Provider name, Publisher name, `price.effective_price` (limited), List unit price
- Microsoft: Provider name (EA/MCA), PricingQuantity, some pricing columns
- OCI: SkuPriceId, List unit price, SubAccountName, ResourceName
- All: SubAccountType, BillingAccountType, ServiceCategory/Subcategory (native)

**Related GitHub issues:** #1030 (closed → #1094), #1041 (proposed commitment columns)

#### Where Custom Columns Are Currently Required

| File | Requirement | Context |
|------|-------------|---------|
| `attributes/invoice_handling.md` | **MUST** include x_ columns | When invoice charges can't be expressed using FOCUS columns |
| `attributes/discount_handling.md` | **SHOULD** include additional columns | When discounts can't be represented by FOCUS columns |
| `glossary.md` (FOCUS Dataset) | **MAY** include custom columns | When additional context is needed beyond FOCUS columns |

#### Deferred Proposal (removed from 1.2)
> Custom columns MUST be included for all information not covered by FOCUS columns that exists in the latest version of non-FOCUS cost and usage datasets.

**Key insight:** The spec currently only requires custom columns in specific scenarios. There is no general requirement to include all native dataset information - that's what this initiative proposes to add.

---

## Google Drive Research

### GDrive Sources Index

| Document | Type | Key Findings |
|----------|------|--------------|
| FOCUS Task Force 1 - Agenda & Minutes (v1.2) | Meeting minutes | Issue #617 / PR #838 - native column requirement removed |
| FOCUS Task Force 3 - Agenda & Minutes (v1.0 & v1.1) | Meeting minutes | PR #474 - native column glossary discussions |
| FOCUS Task Force 2 - Agenda & Minutes (v1.3) | Meeting minutes | #1094/#1030 overlap discussions |
| FOCUS Task Force 3 - Agenda & Minutes (v1.3) | Meeting minutes | #1094 strong support (Irena, Larry/Twilio, Microsoft) |
| VS4 - Meeting Notes | Squad notes | Azure hierarchy columns |
| SKU properties survey | Survey responses | Practitioner column parsing (AHBinfo, PEC, MPC) |
| GMT20250513 Chat (TF-1 May 2025) | Chat transcript | #963 SKU categorization, service subcategory |
| 24.05.14 FOCUS Spec Items v1.1 | Issue tracker | Historical context - SKU/pricing issues |
| FOCUS Potato Summary | Decisions log | PR #474 native column discussions |

### TF-3 Meeting Minutes (v1.0 & v1.1) - PR #474

**Topic:** FOCUS Dataset Consistency Review - defining native provider columns in glossary

**Key Quotes:**
- Q: "Should we specify that native columns must be included?" A: "Yes, to provide complete information."
- "Irena highlighted the absence of a definition for native provider columns within the FOCUS dataset in the current specification."
- Action: "Discuss and finalize the inclusion of native provider columns in the FOCUS dataset definition in the glossary."

### TF-2 Meeting Minutes (v1.3) - #1094

**Topic:** #1030 (JSON column for provider-native attributes)

**Key Findings:**
- "This topic overlaps with #1094, which outlines how custom or extended columns should be managed using the `x_` prefix."
- "Irena confirmed the FOCUS spec already allows for extensions, and 1094 formalizes that guidance."
- "The group agreed that this request is redundant if 1094 is implemented and communicated clearly."

### TF-3 Meeting Minutes (v1.3) - #1094

**Topic:** Define approach for adding non-FOCUS columns as NFR

**Strong Support From:**
- **Irena (Neos):** Guidance would enhance adoption and clarify expected behavior
- **Larry (Twilio):** Adoption is key motivation
- **Microsoft:** Prior efforts to include mappings in v1.2

**Key Insight:** Challenge of correlating two datasets (FOCUS + provider native) when unique record identifiers are missing. Providers like OCI already use internal IDs to link data sources.

### TF-1 Meeting Minutes (FOCUS 1.2)

The 1.2 discussions on **Issue #617 / PR #838** are the direct precursor to the current #1094 initiative.

#### Key Historical Context

| Fact | Detail |
|------|--------|
| Original proposal | Required providers to include ALL columns from native datasets |
| Outcome | Normative requirements **removed** due to lack of consensus |
| What remained | "Should include" (non-normative) in glossary definition |
| Microsoft success | FOCUS implementation includes all columns → **greater adoption** cited as evidence |

#### Outcome

- Broad support for including provider columns, but **no consensus on normative requirements**
- Deferred to future release with more discussion
- Column selection decision also deferred

---

### VS4 Meeting Notes - Azure Hierarchy Columns

**Native Azure columns discussed for FOCUS inclusion:**
- BillingProfile
- InvoiceSection
- Subscription
- ResourceGroup

**Quote:** "Provider columns - BillingAccount, BillingProfile, InvoiceSection, Subscription, ResourceGroup. Should we have a column that includes the full hierarchy path?"

### SKU Properties Survey

**Practitioners are parsing these native columns:**
- ProductName / ServiceType → Resource Type
- Tags / ResourceId → Role or Purpose
- UsageAmount, Performance Metrics → Usage
- Region → Location
- PricingPlanId → Pricing Model
- AHBinfo (Azure Hybrid Benefit info)
- PEC eligibility from Partner Center
- MPC data (not FOCUS aligned)

### Chat Transcript (TF-1 May 2025)

**Issue #963 (SKU hierarchy)** was discussed with strong practitioner interest in:
- SKU categorization columns
- Service subcategory

---

## Concerns

### AWS: Column Stability

**Contact:** Letian Feng (AWS)

**Concern:** AWS believes columns should NEVER change. If they add non-FOCUS columns (e.g., `x_ColumnName`) that later become FOCUS columns, those columns would need to change names, breaking customers who built workflows around the custom column names. Their policy is to not remove columns to avoid breaking changes.

**Counter-Argument:** Column Preservation Approach - Keep non-FOCUS versions of columns available even after FOCUS equivalents are introduced. Provide column selection capability so practitioners can choose old, new, or both columns. This enables migration on practitioners' own terms without breaking changes. Proposed as a MAY requirement in the attribute.

**Historical Context:** This concern led to removal of native column requirement (#617/#838) in v1.2.

---

### GCP: "Junk Drawer" Risk

**Contact:** Sarah McMullin (GCP)

**Concern:** Concern that requiring providers to include all native dataset information as custom columns could cause FOCUS to become a "junk drawer" - accumulating unnecessary, low-quality, or unfocused data that dilutes the specification's purpose and clarity.

**Counter-Argument:** Since FOCUS only asks providers to include data they already have in their native datasets, the only way FOCUS would become a "junk drawer" is if their existing dataset already is one. If providers are proud of their existing data quality and structure, this shouldn't be an issue. If providers feel their current native dataset contains unnecessary data or is poorly organized, they can opt to leave unnecessary datapoints out, choosing to provide a cleaner version that still meets their critical scenarios while maintaining data quality standards.

**Key Points:**
- FOCUS doesn't require providers to create new data - only to include what already exists
- Providers maintain control over what they include in their FOCUS datasets
- Quality standards are preserved by allowing providers to curate their data appropriately
- The specification's cleanliness depends on provider data quality, not on FOCUS requirements themselves

**Related Context:** This concern relates to the broader discussion about whether completeness requirements should be normative (MUST) versus recommended (SHOULD), and how to balance data completeness with specification clarity and purpose.

---

### General: Backwards Compatibility

**Concern:** What happens when a custom column gets standardized into FOCUS? If retained, there's data duplication. If removed, it breaks existing workflows.

**Context:** This general concern overlaps with AWS's specific column stability concern. The column preservation approach addresses both.

---

### General: Dataset Size

**Concern:** Including all columns makes datasets too large. Practitioners are split: some want all columns, others want minimal datasets. This led to the **column selection** proposal (Issue #1091).

**Context:** Column selection capability (allowing practitioners to choose which columns to include) could address this concern while still requiring providers to make all columns available.

---

### General: Scope Creep

**Concern:** FOCUS defines schema/data, not application-level features. Column selection represents a functional requirement, which could set a precedent for adding more application-level features to the specification.

**Context:** Column selection is being considered separately from this initiative and may be addressed as a separate feature or requirement.

---

## Implementation Gap Analysis

### Feature Request vs. Implementation Comparison

Systematic review of feature-request.md acceptance criteria against implemented Scenario Completeness attribute.

#### Completeness Requirements - ✅ ADDRESSED

| Criterion | Status | Implementation |
|-----------|--------|----------------|
| Include custom columns for info not in FOCUS | ✅ | MUST requirement (A-001-M) |
| No native dataset information lost | ✅ | Core attribute purpose |
| Maintain granularity and accuracy | ✅ | SHOULD requirement (A-003-O) |
| Achieve parity between FOCUS and native | ✅ | Core attribute purpose |

#### Data Integrity & Consistency - ⚠️ GAPS IDENTIFIED

| Criterion | Status | Notes |
|-----------|--------|-------|
| Custom columns do NOT duplicate FOCUS columns | ❌ GAP | Was in plan.md, removed during refinement |
| When transformed, don't add custom for native | ❌ GAP | Was in plan.md, removed during refinement |
| FOCUS metrics integrity maintained | ⚠️ Implicit | Covered by row handling |
| Row aggregation/splitting preserves accuracy | ✅ | MUST requirement (A-007-M) |
| Correlation columns included | ✅ | SHOULD requirement (A-005-O) |

**Analysis of Removed Requirements:**

The "MUST NOT duplicate" and "MUST NOT add transformed native" requirements were removed during user refinement. The user specifically identified these as conflicting with the "MAY preserve for migration" requirement.

**Decision:** The current framing is intentional. The user removed explicit anti-duplication requirements to avoid conflict with the migration preservation MAY. The supporting content's "When NOT to Include Custom Columns" section provides non-normative guidance covering these scenarios. This is acceptable because:
1. The user explicitly made this decision during refinement
2. Supporting content covers the anti-patterns
3. The migration use case (AWS column stability) takes priority

#### Naming & Documentation - ⚠️ PARTIAL

| Criterion | Status | Notes |
|-----------|--------|-------|
| Follow x_ prefix convention | ⚠️ Implicit | Mentioned in intro, not explicit requirement |
| Avoid conflicts with FOCUS columns | ❌ GAP | Not addressed anywhere |
| Documentation of custom columns | ✅ | SHOULD requirement (A-006-O) |
| Documentation clarifies mappings | ⚠️ | Related to separate FR #1098 |

**Analysis:** The x_ prefix is already required by Column Handling attribute, so adding it here would be redundant. Conflict avoidance is also implicit in the x_ prefix convention. No changes needed.

#### Practitioner Impact - ✅ ADDRESSED

All practitioner impact criteria are covered by the core attribute design.

### Proposed Solution Requirements Analysis

The feature-request.md "Proposed Solution" section lists 4 normative requirements:

| Requirement | Status | Decision |
|-------------|--------|----------|
| MUST include custom columns | ✅ Implemented | A-001-M |
| SHOULD allow column selection | ❌ Not in attribute | See analysis below |
| SHOULD provide conformance documentation | ❌ Not in attribute | See analysis below |
| SHOULD include explanations for non-conformance | ❌ Not in attribute | See analysis below |

---

## Column Selection Decision

### The Question
Should column selection be part of Scenario Completeness attribute, a separate attribute, or excluded entirely?

### Analysis

**Issue #1091 Context:**
- Column selection is a separate, open feature request with its own acceptance criteria
- It focuses on allowing practitioners to select subsets of columns before/during export
- It's categorized as "Supporting Content" not an attribute refinement
- Has its own set of supporting organizations (FinOps Foundation, Caligo)
- Level of ambiguity rated 4/5 (high complexity)

**Feature Request #1094 Reference:**
- feature-request.md lists column selection as a SHOULD, not MUST
- Lists #1091 as "Blocking dependency" in Related Work section
- plan.md explicitly states "Column selection: NOT a blocker; keep separate from this work"

**Key Considerations:**
1. **Scope Creep Risk:** FOCUS defines schema/data, not application-level features. Column selection is a functional/application requirement.
2. **Complexity:** #1091 has extensive acceptance criteria around UI, API, configuration, column groups, presets - far beyond Scenario Completeness scope.
3. **Independence:** Column selection applies to ALL columns (FOCUS + custom), not just custom columns.
4. **Separate Governance:** #1091 has its own supporting organizations and review process.

### Decision: EXCLUDE from Scenario Completeness

**Rationale:**
1. Column selection is explicitly tracked as separate issue #1091
2. plan.md explicitly excludes it: "Column selection: NOT a blocker; keep separate from this work"
3. Adding it to Scenario Completeness would conflate data completeness (what columns exist) with data access (which columns practitioners receive)
4. The feature request's SHOULD for column selection references #1091, indicating it should be addressed there
5. Column selection applies to all columns, not just custom columns from Scenario Completeness

**No changes to attribute needed.**

---

## Conformance Documentation Decision

### The Question
Should conformance documentation requirements be part of Scenario Completeness attribute?

### Analysis

**Feature Request Reference:**
- SHOULD provide conformance documentation indicating full/partial/non-conformance
- SHOULD include explanations for partial or non-conformance

**Related Issues:**
- #1098 covers provider column mappings as a separate NFR
- #1098 is explicitly about mapping documentation between native and FOCUS columns
- Has its own supporting organizations (Twilio, Caterpillar, American Express, Caligo, FinOps Foundation)

**Key Considerations:**
1. **Current Documentation Requirement:** Scenario Completeness already has A-006-O: "SHOULD provide documentation describing custom columns, their purpose, and relationship to native columns"
2. **Overlap with #1098:** Conformance documentation about column mappings is the core focus of #1098
3. **Scope:** Conformance documentation is broader than just custom columns - it covers all column mappings
4. **Existing Mechanism:** FOCUS has a separate Conformance Certification program

### Decision: PARTIALLY ADDRESSED, Remainder Deferred to #1098

**What's already covered:**
- A-006-O requires documentation of custom columns

**What should NOT be added to Scenario Completeness:**
- Full/partial/non-conformance indicators → This is conformance program scope
- Detailed column mapping documentation → This is #1098 scope

**Rationale:**
1. The feature request's conformance documentation SHOULD relates more to #1098's comprehensive mapping requirements
2. Adding conformance level indicators (full/partial/non-conformance) to an attribute is unusual - conformance is typically assessed at the certification level
3. Scenario Completeness focuses on what columns to include, not how to document compliance status
4. #1098 has strong organizational support and is the appropriate place for mapping documentation requirements

**No changes to attribute needed.** Add note to supporting content clarifying relationship to #1098.

---

## Missing Anti-Duplication Requirements

### The Question
Should explicit MUST NOT duplication requirements be added?

### Analysis

**Original plan.md requirements removed:**
- "Custom columns MUST NOT duplicate information already captured in FOCUS columns"
- "When native data is transformed into FOCUS columns, data generators MUST NOT add custom columns for the original native representation"

**User's Explicit Decision:**
During refinement, the user identified these as conflicting with "MAY preserve non-FOCUS versions for migration" and explicitly removed them.

**Current Coverage:**
- Supporting content "When NOT to Include Custom Columns" covers:
  1. Duplication anti-pattern
  2. Transformed data anti-pattern
  3. Data integrity violation anti-pattern

### Decision: NO CHANGES - User Decision Was Intentional

**Rationale:**
1. The user explicitly removed these after identifying the conflict with migration preservation
2. Supporting content provides non-normative guidance
3. The MAY for migration preservation is essential for addressing AWS column stability concerns
4. Making both MUST NOT (no duplication) and MAY (preserve old columns) would be contradictory

**No changes to attribute needed.**

---

## Summary of Decisions

| Gap | Decision | Rationale |
|-----|----------|-----------|
| Column Selection | Exclude | Separate issue #1091, explicitly excluded in plan.md |
| Conformance Documentation | Defer to #1098 | Separate issue with broader scope |
| Anti-Duplication Requirements | Keep removed | User decision to resolve conflict with migration MAY |
| x_ Prefix Requirement | No change | Already covered by Column Handling attribute |
| Conflict Avoidance | No change | Implicit in x_ prefix convention |

**Conclusion:** The Scenario Completeness attribute as implemented aligns with the feature request's core requirements. The gaps identified are either:
1. Intentionally excluded per user direction
2. Covered by separate issues (#1091, #1098)
3. Already addressed by other mechanisms (Column Handling, Conformance Certification)

No changes to the attribute are recommended.

---

## Pending Research

### Provider Objections
- [ ] Identify addressable vs fundamental blockers

### Supporting Content Location
- [ ] Determine where audit/analysis should live in `supporting_content/`
- [ ] Identify if new folder structure is needed

### Additional GDrive Content
- [ ] Provider column mapping spreadsheet: https://docs.google.com/spreadsheets/d/1HgtynMXWElhjektKT2I0U3c83TsemqTknYbSsaAQNdE/edit?gid=0#gid=0
- [ ] Account/Resource Hierarchy spreadsheet

---

## GitHub Issues Context

Key related issues and their status:

| Issue | Purpose | Status |
|-------|---------|--------|
| #1094 | Primary FR - completeness requirement | Open |
| #1030 | JSON column for provider-native attributes | Closed | Folded into #1094 |
| #1041 | Add commitment dimension columns | Open | Example of columns not yet in FOCUS |
| #1091 | Column selection NFR (potential blocker) | Open |
| #1098 | Provider column mappings NFR | Open |
| #1634 | Spec audit task | Open (mostly complete) |
| #1635 | Review supported features section | Open |
| #617 | Glossary update for FOCUS dataset | Closed (1.2) |
| #602 | Original discussion | Closed |

See [audit-1634-spec-analysis.md](audit-1634-spec-analysis.md) for detailed issue history.

