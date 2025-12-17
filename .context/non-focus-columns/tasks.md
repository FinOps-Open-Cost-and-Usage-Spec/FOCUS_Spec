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
- [ ] Search Google Drive for related docs/sheets (identify, don't deep-dive)
- [ ] List any GDrive docs found that need review (note: may be out of scope)

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

