# Implementation Plan: Non-FOCUS Columns

## Goal

Increase FOCUS adoption by enabling customers to achieve the same analysis and reporting scenarios with FOCUS datasets that are currently only possible with native datasets.

---

## Phased Approach

### Phase 1: Research & Analysis
Gather evidence and confirm alignment before drafting.
- **Spec audit:** Identify all existing mentions of custom column requirements across the specification
- **Alignment review:** Confirm the proposed supported features content aligns with the new attribute vision
- Decide attribute location (new vs extend column_handling)
- Define precise normative requirements to propose

**Purpose:** Build the foundation and evidence needed for drafting.

### Phase 2: Draft & TF Approval
- Consolidate research notes into single location
- Draft spec changes (new attribute or extended column_handling)
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
AWS and GCP are the key providers to convince. Expected pushback areas:
- Additional implementation effort
- Scope concerns (what counts as "all" native data?)
- Potential performance/size implications

### The Approach
1. **Be evidence-based** - Use audit findings and practitioner use cases to justify the requirement
2. **Understand concerns individually** - Don't assume; document actual objections
3. **Address concerns directly** - Propose solutions or scope adjustments where reasonable
4. **Pre-socialize** - Engage provider representatives before formal proposals

### Evidence to Collect
- Specific AWS objections and concerns
- Specific GCP objections and concerns
- Examples of native columns that should/shouldn't become `x_` columns
- Practitioner pain points from incomplete FOCUS datasets

---

## Open Questions

### Q1: New attribute or extend column_handling?

| Option | Pros | Cons |
|--------|------|------|
| New attribute | Clean separation, clear ownership | More spec surface area |
| Extend column_handling | Builds on existing work, lower effort | May get cluttered |

**Current lean:** Separate attribute feels right, but open to input.

**Resolution approach:** Document pros/cons, get TF-2 input.

### Q2: MUST vs SHOULD for completeness?

**Decision:** Use SHOULD for the initial requirement. MUST will be harder to get approval for.

**Rationale:** Start with SHOULD to ease adoption, with potential to strengthen to MUST in a future release based on adoption experience.

### Q3: What constitutes "all native data"?

**Need to define:**
- Scope: Cost and usage datasets only (not all provider data)
- Exclusions: Deprecated columns? Columns with no analytical value?
- Examples: What specific native columns should/shouldn't become `x_` columns?

### Q4: Is column selection a true blocker?

**Context:** The team has discussed whether data generators should allow practitioners to select which columns to include in their FOCUS exports.

**Team position:** Listed as blocking dependency for completeness requirement.  
**Hypothesis:** May be nice-to-have rather than true blocker.

**Resolution approach:** Validate with TF-2.

---

## Success Criteria

- Customers who were blocked on FOCUS adoption due to missing native data are unblocked
- Practitioners can retire native dataset queries and use FOCUS exclusively for cost and usage analysis
- Provider FOCUS exports include custom columns that cover all native dataset information
