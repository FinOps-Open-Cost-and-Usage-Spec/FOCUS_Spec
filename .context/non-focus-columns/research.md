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

#### Provider Concerns Raised (1.2)

1. **Backwards Compatibility**
   - What happens when a custom column gets standardized into FOCUS?
   - If retained: data duplication
   - If removed: breaks existing workflows
   - **AWS position:** Does not remove columns to avoid breaking changes

2. **Split Cost Allocation (AWS-specific)**
   - SCA adds **rows**, not just columns
   - Causes aggregation issues with effective cost calculations
   - Unresolved whether SCA data belongs in FOCUS dataset

3. **Dataset Size**
   - All columns = dataset too large
   - Practitioners split: some want all, others want minimal
   - Led to **column selection** proposal (Issue #1091)

4. **Scope Creep**
   - FOCUS defines schema/data, not application-level features
   - Column selection = functional requirement = precedent concern

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

## Pending Research

### Provider Objections
- [ ] Document AWS concerns and objections (partially captured from 1.2 discussions)
- [ ] Document GCP concerns and objections
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

