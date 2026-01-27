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
- [x] Identify what evidence/examples are needed to support proposal (see plan.md § Evidence Needed)

---

## Phase 2: Attribute Design & Supporting Content ✅ COMPLETE

### Design Attribute Requirements

- [x] Document known AWS concerns and objections (see research.md § Concerns)
- [x] Document known GCP concerns and objections (see research.md § Concerns)
- [x] Incorporate solutions into attribute requirements where appropriate:
  - [x] Add column preservation approach as MAY requirement (addresses AWS column stability)
  - [x] Ensure requirements address data quality concerns (addresses GCP "junk drawer" concern)
- [x] Review 8 requirements from plan.md and refine based on concerns/solutions
- [x] Validate requirements align with attribute purpose (formatting, naming, data types, granularity, etc.)

### Create Supporting Content

- [x] Draft `supporting_content/attributes/scenario_completeness.md` with:
  - [x] Design rationale (why attribute exists, relationship to Column Handling)
  - [x] How concerns are addressed (AWS column stability, GCP data quality)
  - [x] When to include custom columns (4 scenarios from plan.md)
  - [x] When NOT to include custom columns (3 anti-patterns from plan.md)
  - [x] Correlation guidance (FOCUS-to-native dataset joins)
  - [x] Aggregation/splitting examples
  - [x] Provider-specific examples (AWS, Azure, GCP, OCI)

---

## Phase 3: Provider Engagement & Refinement

### Pre-Socialize with Providers

- [x] Identify specific people to engage at AWS (Letian Feng) and GCP (Sarah McMullin)
- [ ] Share draft attribute and supporting content with AWS (Letian Feng) for feedback
- [ ] Share draft attribute and supporting content with GCP (Sarah McMullin) for feedback
- [ ] Document feedback and adjust attribute/supporting content as needed
- [ ] Identify which objections are addressable vs fundamental blockers

### TF-2 Proposal

- [ ] Present refined proposal to TF-2 with attribute requirements and supporting content
- [ ] Incorporate TF-2 feedback
- [ ] Get TF-2 approval to proceed

### Broader Approval

- [ ] Present to maintainers/members for approval
- [ ] Handle any remaining objections
- [ ] Get formal approval to proceed

---

## Phase 4: Implementation ✅ COMPLETE

> **References:** `plan.md` § Deliverables for requirements, `guidelines/` for conventions

### Deliverable 1: Attribute File (CREATE) ✅ COMPLETE

- [x] Create `specification/attributes/scenario_completeness.md`
- [x] Follow `guidelines/normative-requirements-guidelines.md` for structure
- [x] Use `invoice_handling.md` as reference
- [x] Include requirements (refined to 7 from original 8, with scenario-focused framing)

### Deliverable 2: Attributes Index (UPDATE) ✅ COMPLETE

- [x] Add `!INCLUDE "scenario_completeness.md",1` to `specification/attributes/attributes.mdpp`

### Deliverable 3: Dataset Reference (UPDATE) ✅ COMPLETE

- [x] Add conformance line to `specification/datasets/cost_and_usage/dataset.md`

### Deliverable 4: Requirements Model - Attribute Rules (CREATE) ✅ COMPLETE

- [x] Create `specification/requirements_model/model_rules/attributes/scenariocompleteness.json`
- [x] Follow `guidelines/writing-requirements-model-guidelines.md`
- [x] Use `columnhandling.json` as reference

### Deliverable 5: Requirements Model - Dataset Rules (UPDATE) ✅ COMPLETE

- [x] Add `ScenarioCompleteness-A-000-M` to Dependencies in `costandusage.json`

### Deliverable 6: Supporting Content (CREATE) ✅ COMPLETE

- [x] Create `supporting_content/attributes/scenario_completeness.md`
- [x] Include 6 sections from plan.md
- [x] Follow `guidelines/editorial-guidelines.md`

### Deliverable 7: Supported Features (UPDATE - if needed) ✅ COMPLETE

- [x] Review `specification/supported_features/custom_columns.md`
- [x] Add reference to Scenario Completeness if appropriate

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

- [x] Create PR, link to #1094 ✅ [PR #1800](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/1800)
- [ ] Review cycle
- [ ] Rename attribute to "Dataset Completeness" (use `git mv` to preserve history; do last before merge)
- [ ] Merge to working draft

### Before PR Merge Checklist

- [ ] Review Future Considerations in `supporting_content/attributes/scenario_completeness.md`:
  - [ ] Glossary entry for "native dataset" - decide if needed for 1.4
  - [ ] Clarify "data generator" scope - decide if needed for 1.4
  - [ ] GA dataset qualifier - hold for negotiation if needed
- [ ] Resolve or close all PR review threads
- [ ] Contract Commitment dataset: Decide if this PR should add conformance or defer to separate PR (see PR discussion #2692032328)
- [ ] Column Handling cleanup: Decide if descriptive paragraph (lines 12-14) should be simplified now that Scenario Completeness formalizes those requirements (see PR discussion #2691961973)
- [ ] Move any valuable content from `.context/non-focus-columns/` to `supporting_content/` or related issues
- [ ] Delete `.context/non-focus-columns/` working folder

---

## Notes

- **Phase 0** complete - #1634 and #1635 closed
- Provider engagement (Phase 2) is critical path - don't skip pre-socialization
- `.context/` is working space; final content goes to `supporting_content/`
- **plan.md § Deliverables** contains complete specs for each file - use as primary reference for implementation
