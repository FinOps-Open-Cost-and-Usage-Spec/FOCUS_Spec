# Tasks: Non-FOCUS Columns Initiative

> **Target Release:** 1.4  
> **Immediate Priority:** Complete #1634 and #1635 by 2025-12-17

---

## Phase 0: Immediate Deliverables (Due Tomorrow)

### #1634 - Audit spec for existing mentions of non-focus column requirements

#### Research Tasks
- [x] Search specification folder for custom column mentions
- [x] Search specification folder for x_ prefix mentions  
- [x] Search specification folder for provider column mentions
- [x] Search supporting_content folder for relevant content
- [x] Document findings in audit-1634-spec-analysis.md
- [x] Consolidate list of all provider columns referenced (see provider-columns-referenced.md)
- [x] Search Google Drive for related docs/sheets (identify, don't deep-dive)
  - [x] "custom column" OR "x_" FOCUS
  - [x] "native column" OR "provider column"
  - [x] "AWS CUR" FOCUS
  - [x] "GCP billing" OR "BigQuery billing" FOCUS
  - [x] "data completeness" FOCUS
  - [x] "non-FOCUS" OR "non FOCUS"
  - [x] "column mapping" provider
  - [x] "Azure cost" FOCUS column
  - [x] "OCI" FOCUS column
  - [x] 1094 OR "dataset completeness"
  - [x] Squad minutes
- [x] Review Google Drive files for potential native columns:
  - [x] Squad 1 Meeting Minutes - No new columns found
  - [x] Squad 2 Meeting Minutes - No new columns found
  - [x] VS2 - Meeting Notes - No new columns found
  - [x] VS4 - Meeting Notes - Azure hierarchy columns (BillingProfile, InvoiceSection, ResourceGroup)
  - [x] HS_Practitioners - Meeting Notes - No new columns found
  - [x] FOCUS Maintainers - Agenda & Minutes (v1.0 & v1.1) - No new columns found
  - [x] FOCUS Members WG - Agenda & Minutes (v1.0 & v1.1) - Not downloaded
  - [x] FOCUS Task Force 1 - Agenda & Minutes (v1.0, v1.1) - Custom columns appendix discussion
  - [x] FOCUS Task Force 2 - Agenda & Minutes (v1.0, v1.1) - No new columns found
  - [x] FOCUS Task Force 3 - Agenda & Minutes (v1.0 & v1.1) - PR #474 native column discussions
  - [x] FOCUS Maintainers - Agenda & Minutes (v1.2) - No new columns found
  - [x] FOCUS Task Force 1 - Agenda & Minutes (v1.2) - #617/#838 native column requirement removed
  - [x] FOCUS Task Force 2 - Agenda & Minutes (v1.2) - No new columns found
  - [x] FOCUS Task Force 3 - Agenda & Minutes (v1.2) - Not downloaded
  - [x] FOCUS Members WG - Agenda & Minutes - (v1.2) - Not downloaded
  - [x] FOCUS Maintainers - Agenda & Minutes (v1.3) - No new columns found
  - [x] FOCUS Task Force 1 - Agenda & Minutes (v1.3) - Not downloaded
  - [x] FOCUS Task Force 2 - Agenda & Minutes (v1.3) - #1094/#1030 discussions
  - [x] FOCUS Task Force 3 - Agenda & Minutes (v1.3) - #1094 strong support (Irena, Larry/Twilio, MS)
  - [x] GMT20250513-145716_RecordingnewChat (TF-1-13-May-25) - #963 SKU categorization, service subcategory
  - [x] FOCUS Potato Summary, Decisions, and Proposals 🥔 - Native column discussions (PR #474)
  - [x] 24.05.14 FOCUS Spec Items for v1.1 - Open Issues - 24.05.14 - Historical context, SKU/pricing issues
  - [x] SKU properties survey - Practitioner column parsing (AHBinfo, PEC, MPC data)
- [ ] Review: https://docs.google.com/spreadsheets/d/1HgtynMXWElhjektKT2I0U3c83TsemqTknYbSsaAQNdE/edit?gid=0#gid=0 (provider column mapping)
- [x] List any GDrive docs found that need review (captured in GDrive Docs to Review)

#### Synthesis Tasks
- [x] Summarize all locations where custom column requirements exist
- [x] Identify inconsistencies or gaps in current requirements
- [x] Document deferred proposals from 1.2
- [ ] Write recommendation for where consolidated requirements should live

#### Deliverable Tasks
- [ ] Review audit-1634-spec-analysis.md for completeness
- [ ] Draft comment for issue #1634 summarizing findings
- [ ] Post comment to #1634

---

### #1635 - Review supported features section for #1094

#### Prep Tasks
- [ ] Read "Enhancement to Existing Supported Feature" section in feature-request.md
- [ ] Compare proposed changes against current supported_features/custom_columns.md

#### Analysis Tasks
- [ ] Assess: Does the proposed description align with the new attribute vision?
- [ ] Assess: Are the "when to include / when not to include" guidelines clear?
- [ ] Assess: Is the completeness principle (MUST for all native data) the right scope?
- [ ] Identify any gaps or concerns

#### Deliverable Tasks
- [ ] Document feedback/alignment in this repo (for AI context)
- [ ] Draft comment for issue #1635 with alignment confirmation or suggested edits
- [ ] Post comment to #1635

---

## Phase 1: Foundation & Planning

### Attribute Location Decision
- [ ] Document pros/cons: extend column_handling.md vs new attribute
- [ ] Draft strawman for each option (outline only)
- [ ] Get TF-2 input on preferred approach
- [ ] Finalize decision

### Plan Refinement  
- [ ] Update plan.md with finalized approach
- [ ] Define specific normative requirements to propose
- [ ] Identify what evidence/examples are needed to support proposal

---

## Phase 2: Provider Engagement Prep

### Understand Objections
- [ ] Document known AWS concerns and objections
- [ ] Document known GCP concerns and objections
- [ ] Identify which objections are addressable vs fundamental blockers

### Build Evidence
- [ ] Gather examples of native columns that should become x_ columns (per provider)
- [ ] Document practitioner pain points from not having completeness
- [ ] Identify any providers already doing this well (positive examples)

### Pre-Socialize
- [ ] Identify specific people to engage at AWS and GCP
- [ ] Schedule or async outreach to discuss concerns before TF-2 proposal
- [ ] Document feedback and adjust proposal as needed

---

## Phase 3: Proposal & Approval

### TF-2 Proposal
- [ ] Draft formal proposal with normative requirements
- [ ] Present to TF-2 for refinement
- [ ] Incorporate feedback

### Broader Approval
- [ ] Present to maintainers/members for approval
- [ ] Handle objections (with pre-socialized provider buy-in)
- [ ] Get formal approval to proceed

---

## Phase 4: Implementation

### Spec Changes
- [ ] Draft attribute content (new or extended column_handling)
- [ ] Update cross-references in other files
- [ ] Update supported features content
- [ ] Update glossary if needed

### Review & Merge
- [ ] PR for spec changes
- [ ] Review cycle
- [ ] Merge to working draft

---

## Ongoing: Documentation & Housekeeping

- [ ] Determine where analysis should live in `supporting_content/` (or if new structure needed)
- [ ] Move/copy finalized content to appropriate `supporting_content/` location
- [ ] Update research.md with new findings as work progresses

---

## Notes

- **Phase 0** is the immediate focus - everything else can wait
- **Phases 1-4** are rough sequencing, will refine after Phase 0 complete
- Provider engagement (Phase 2) is critical path - don't skip pre-socialization
- `.context/` is working space; final content goes to `supporting_content/`

