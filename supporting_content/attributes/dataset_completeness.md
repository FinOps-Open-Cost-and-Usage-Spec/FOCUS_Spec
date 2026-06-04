# Dataset Completeness

## Purpose

Dataset Completeness addresses *what* custom columns to include in a FOCUS dataset. Column Handling addresses *how* they are named and documented. Without Dataset Completeness, practitioners must maintain parallel native dataset workflows, making FOCUS an added overhead rather than a viable replacement. For some organizations, this has been noted as a blocker to adopting FOCUS.

## Key Decisions

### Relationship with Column Handling

* **Question:** Why not add these requirements to Column Handling?
* **Decision:** Different scopes — Column Handling is column-level (naming, documentation); Dataset Completeness is dataset-level (which columns to include).
* **Decided:** Dec 2025

### Inclusion framing

* **For exclusion-based ("include all except documented exclusions"):** Concrete, enforceable, verifiable against native dataset documentation. Shifts burden of proof to data generators — they must justify what they exclude, not what they include. Simpler than enumerating inclusion categories.
* **For scenario-based ("materially support analysis or reporting"):** More flexible, but subjective and hard to validate.
* **Decision:** Exclusion-based model. Evolved from scenario-based framing through TF2 consensus.
* **Decided:** Mar 2026

### MUST vs SHOULD for primary inclusion requirement

* **For MUST:** Practitioners need confidence that FOCUS datasets are complete. SHOULD allows providers to omit columns without accountability, undermining the attribute's purpose.
* **For SHOULD:** Column stability concerns — if custom columns later become FOCUS columns, names change, breaking workflows. Data volume concerns. Implementation burden.
* **Decision:** MUST with safeguards: (1) exclusion-based framing allows documented exceptions, (2) Dataset Configuration lets practitioners control what they receive, (3) "publicly-available documentation" ensures transparency, (4) correlation columns use SHOULD.
* **Decided:** Feb 2026

### Column stability and migration (duplicate columns)

* **For removing duplicates immediately:** Avoids confusion, keeps datasets clean.
* **For preserving duplicates temporarily:** Practitioners build workflows around `x_` column names. If FOCUS later standardizes an equivalent column, removing the custom version breaks those workflows.
* **Decision:** SHOULD exclude duplicates, except during a documented transitional period. "Transitional period" must be defined in publicly-available documentation so practitioners know when migration is expected.
* **Decided:** Mar 2026

### Data volume

* **Concern:** Requiring all native columns inflates dataset size and storage costs. Could accumulate low-quality data.
* **Decision:** Dataset Configuration (introduced alongside Dataset Completeness) lets practitioners select only columns they need. The requirement is about schema *availability*, not forced inclusion in every export. Data generators may offer default column sets.
* **Decided:** Feb 2026

### Data fidelity

* **For "accurately represent":** Simple, intuitive.
* **For "retain fidelity":** More precise — "accurately represent" is ambiguous about whether reformatting a date or normalizing casing on an identifier counts as a violation.
* **Decision:** "Retain fidelity without lossy transformations (e.g., rounding or truncation)." Formatting improvements that preserve information are fine. Lossy changes (rounding numbers, truncating strings, altering identifier casing) are prohibited. DateTimeFormat and StringHandling already have SHOULD-level guidance for custom columns.
* **Decided:** Mar 2026

### Correlation columns

* **For SHOULD NOT exclude:** Consistent with exclusion-based framing of the primary MUST.
* **For SHOULD include:** Reads more naturally; avoids confusing "exclude" and "exclusion" in the same sentence.
* **Decision:** SHOULD include, with "even if they meet the criteria for exclusion" to make clear these should survive the exclusion process.
* **Decided:** Mar 2026

### Requirement structure

* **For nesting sub-bullets:** Groups related sub-requirements under the MUST they modify.
* **For flat top-level bullets:** Requirements Model guidelines discourage nesting. Each requirement should be independently testable.
* **Decision:** Flattened to top-level bullets. Each requirement stands alone.
* **Decided:** Mar 2026

### Custom column documentation location

* **For Dataset Completeness:** It's about what to include, so documentation of what's included belongs here.
* **For Column Handling:** Documentation is a column-level rule that applies to all custom columns regardless of origin.
* **Decision:** Kept in Column Handling. Added "publicly-available" to the documentation MUST.
* **Decided:** Feb 2026

### Column ordering

* **For MAY:** Ordering is a nice-to-have, not critical.
* **For SHOULD:** Consistent ordering improves practitioner experience.
* **Decision:** Upgraded to SHOULD. Merged into single requirement: "SHOULD sort all FOCUS columns alphabetically first, then all custom columns alphabetically second." Removed opposite-polarity SHOULD NOT (antipattern per Requirements Model guidelines).
* **Decided:** Mar 2026

### Default column set

* **For Dataset Completeness:** Relates to what columns are available by default.
* **For Dataset Configuration:** Column selection belongs with the attribute that governs configuration.
* **Decision:** Moved to Dataset Configuration. MAY offer a default set, but if offered, MUST include all applicable FOCUS columns.
* **Decided:** Feb 2026

### Column Handling intro scope

* **Concern:** Intro said "All columns defined in the FOCUS specification MUST follow..." but custom columns aren't defined by FOCUS — this logically exempts them from the rules below.
* **Decision:** Changed to lowercase "must" (informative, not normative) and broadened scope to "All columns included in a FOCUS dataset."
* **Decided:** Mar 2026

## Future Considerations

1. **Clarify "data generator" scope:** The glossary should explicitly note that data generators include both providers (cloud, SaaS) and FinOps tool vendors who aggregate or transform billing data.
2. **GA dataset qualifier:** Consider limiting requirements to generally available native datasets only, excluding preview/beta datasets.
3. **Metadata importance:** With custom columns, Metadata (especially ColumnDefinition) gains importance. The current SHOULD for metadata may become a MUST in future releases.
