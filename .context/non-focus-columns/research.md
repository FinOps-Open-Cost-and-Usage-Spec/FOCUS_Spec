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

| Document | Type | Relevance |
|----------|------|-----------|
| [FOCUS Task Force 1 - Agenda & Minutes (v1.2)](https://docs.google.com/document/d/1I0cTiEuJuaLPohZgG73-fOSDQTD_h_xyHbgstoPdy6A/edit) | Meeting minutes | Issue #617 / PR #838 discussions |

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

## Pending Research

### Additional Google Drive Content
- [ ] Search for other related docs/sheets in GDrive (spreadsheets, provider mappings)
- [ ] Check TF-2 meeting minutes for 1.3 discussions

### Provider Objections
- [ ] Document AWS concerns and objections
- [ ] Document GCP concerns and objections
- [ ] Identify addressable vs fundamental blockers

### Supporting Content Location
- [ ] Determine where audit/analysis should live in `supporting_content/`
- [ ] Identify if new folder structure is needed

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

