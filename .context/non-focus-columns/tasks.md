# Tasks: Non-FOCUS Columns Initiative

> **Target Release:** 1.4  

---

## Phase 0: Immediate Deliverables ✅ COMPLETE

### #1634 - Audit spec for existing mentions of non-focus column requirements

#### Research Tasks

- [x] Search specification folder for custom column mentions
- [x] Search specification folder for x\_ prefix mentions
- [x] Search specification folder for provider column mentions
- [x] Search supporting_content folder for relevant content
- [x] Document findings in audit-1634-spec-analysis.md
- [x] Consolidate list of all provider columns referenced (see provider-columns-referenced.md)
- [x] Search Google Drive for related docs/sheets (identify, don't deep-dive)
  - [x] "custom column" OR "x\_" FOCUS
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
- [x] Write recommendation for where consolidated requirements should live

#### Deliverable Tasks

- [x] Review audit-1634-spec-analysis.md for completeness
- [x] Draft comment for issue #1634 summarizing findings
- [x] Post comment to #1634 ✅ https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/1634#issuecomment-3665386261

---

### #1635 - Review supported features section for #1094 ✅ CLOSED

- [x] Reviewed supported features content
- [x] Posted comment confirming alignment
- [x] Detailed feedback posted to #1094 directly
- [x] Closed issue

---

## Phase 1: Foundation & Planning

### Attribute Location Decision ✅ DECIDED

**Decision:** New attribute called **"Scenario Completeness"**

**Rationale:**
- 10-12 potential requirements - too many to add to Column Handling
- Column Handling is about format (naming, ordering); this is about content (what to include)
- "Scenario Completeness" aligns to goal: "achieve the same analysis and reporting scenarios"
- Avoids overloaded terms like "provider" and "native"

**Attribute details:**
- Attribute ID: `ScenarioCompleteness`
- Attribute Name: `Scenario Completeness`

### Plan Refinement

- [x] Decide attribute location (new attribute: Scenario Completeness)
- [x] Decide requirement strength (MUST, let TF-2 discuss)
- [x] Define scope criteria (use goal statement as objective test)
- [x] Confirm column selection is not a blocker
- [x] Update plan.md with finalized approach
- [x] Define specific normative requirements (see plan.md § Proposed Requirements)
- [ ] Identify what evidence/examples are needed to support proposal

---

## Phase 2: Provider Engagement Prep

### Understand Objections

- [ ] Document known AWS concerns and objections
- [ ] Document known GCP concerns and objections
- [ ] Identify which objections are addressable vs fundamental blockers

### Build Evidence

- [ ] Gather examples of native columns that should become x\_ columns (per provider)
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

> **References:** `plan.md` § Deliverables for requirements, `guidelines/` for conventions

### Deliverable 1: Attribute File (CREATE)

- [ ] Create `specification/attributes/scenario_completeness.md`
- [ ] Follow `guidelines/normative-requirements-guidelines.md` for structure
- [ ] Use `invoice_handling.md` as reference
- [ ] Include 8 requirements from plan.md (MUST/MUST NOT first, then SHOULD)

### Deliverable 2: Attributes Index (UPDATE)

- [ ] Add `!INCLUDE "scenario_completeness.md",1` to `specification/attributes/attributes.mdpp`

### Deliverable 3: Dataset Reference (UPDATE)

- [ ] Add conformance line to `specification/datasets/cost_and_usage/dataset.md`

### Deliverable 4: Requirements Model - Attribute Rules (CREATE)

- [ ] Create `specification/requirements_model/model_rules/attributes/scenariocompleteness.json`
- [ ] Follow `guidelines/writing-requirements-model-guidelines.md`
- [ ] Use `columnhandling.json` as reference

### Deliverable 5: Requirements Model - Dataset Rules (UPDATE)

- [ ] Add `ScenarioCompleteness-A-000-M` to Dependencies in `costandusage.json`

### Deliverable 6: Supporting Content (CREATE)

- [ ] Create `supporting_content/attributes/scenario_completeness.md`
- [ ] Include 6 sections from plan.md
- [ ] Follow `guidelines/editorial-guidelines.md`

### Deliverable 7: Supported Features (UPDATE - if needed)

- [ ] Review `specification/supported_features/custom_columns.md`
- [ ] Add reference to Scenario Completeness if appropriate

### Validation

```bash
cd specification
python validate_includes.py spec.mdpp        # Verify includes
make clean && make                            # Build + lint
cd requirements_model && python -m pytest tests/  # Test model
```

- [ ] Build succeeds, no linting errors
- [ ] Requirements model tests pass
- [ ] Manual review: matches existing attribute patterns

### Review & Merge

- [ ] Create PR, link to #1094
- [ ] Review cycle
- [ ] Merge to working draft

---

## Ongoing: Documentation & Housekeeping

- [ ] Determine where analysis should live in `supporting_content/` (or if new structure needed)
- [ ] Move/copy finalized content to appropriate `supporting_content/` location
- [ ] Update research.md with new findings as work progresses

---

## Notes

- **Phase 0** complete - #1634 and #1635 closed
- Provider engagement (Phase 2) is critical path - don't skip pre-socialization
- `.context/` is working space; final content goes to `supporting_content/`
- **plan.md § Deliverables** contains complete specs for each file - use as primary reference for implementation
