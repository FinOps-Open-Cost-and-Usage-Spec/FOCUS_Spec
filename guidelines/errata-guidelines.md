# FOCUS Errata Guidelines

## Overview
Once a version of the FOCUS Specification is formally published, the normative text and schema are locked to ensure stability for data generators and practitioners. However, minor drafting discrepancies—such as typos, formatting issues, or copy-paste errors—can occasionally occur.

This document outlines the guidelines and process for identifying, submitting, and publishing non-material corrections to the FOCUS specification via the repository's `ERRATA.md` file.

---

## 1. What Qualifies as an Erratum?
An erratum is strictly a correction to the intended language of the specification and **must not represent a material or normative change**.

**Acceptable Errata:**
* **Typographical Errors:** Spelling, grammar, and punctuation fixes.
* **Formatting Fixes:** Correcting broken hyperlinks, misaligned markdown tables, or missing code block ticks.
* **Terminology & Reference Corrections:** Fixing inconsistent casing (e.g., `ContractID` vs `ContractId`) or broken cross-references between sections.
* **Schema & Validation Typos:** Correcting obvious discrepancies where the text contradicts the clear intent of the working group (e.g., correcting a JSON property presence requirement that was accidentally copied from a dataset-level requirement).

**Unacceptable Errata (Requires a Feature Request):**
* Adding new columns, datasets, or JSON properties.
* Changing normative BCP-14 keywords (e.g., changing a `MAY` to a `MUST`).
* Deprecating or removing existing columns or features.
* Changing data types or validation logic in a way that forces data generators to write new code to remain compliant.

*If your suggestion involves adding, changing, or removing a data field, label, or structure, please submit a Feature Request instead*.

---

## 2. Submission Process
All errata must be tracked via a GitHub Issue to ensure visibility.

1. **Open an Issue:** Navigate to the FOCUS repository and create a new Issue.
2. **Select the Template:** Choose the **General Feedback** issue template. This template is specifically designed for reporting minor corrections, clarity improvements, or inconsistencies.
3. **Provide Details:**
  * Set the Type of Feedback to "Typo or grammar," "Minor correction (non-breaking)," or "Field naming or label inconsistency".
  * Clearly state the affected section or field.
  * Provide the "Original Text" and the proposed "Corrected Text".

---

## 3. Maintainer Assessment and Triage
Once a General Feedback issue is submitted, it must be evaluated to ensure it meets the strict definition of an erratum.

* **Review:** The Maintainers shall meet to review the submitted issue.
* **Assessment:** They shall determine if the report constitutes a valid, non-material erratum or if it represents a material/normative change that should be deferred to a future specification release.
* **Outcome:** 
  * *Approved:* If the issue qualifies as an erratum that the working group wishes to issue, the Maintainers shall approve it for inclusion and signal that a Pull Request can be drafted.  The issue shall receive the `errata` label.
  * *Rejected/Re-routed:* If the issue introduces material changes, the submitter shall be provided an explanation and directed to open a formal Feature Request.

---

## 4. Pull Request & Updating ERRATA.md
Once an issue is assessed and confirmed as a valid erratum by the Maintainers, it can be added to the `ERRATA.md` file via a Pull Request (PR).

1. **Branching:** Create a feature branch following the naming convention `[issue-number]-short-description` (e.g., `1042-fix-contractapplied-typo`).
2. **Update ERRATA.md:** Locate the section for the currently published version (e.g., `## Version 1.3`) in the root `ERRATA.md` file.
3. **Categorize the Fix:** Add the correction to the appropriate impact-based table:
   * *A. Schema & Validation Logic Corrections*
   * *B. Terminology & Reference Corrections*
   * *C. Typographical Errors*
   * *D. Requirements Model Corrections*
4. **Format the Entry:** Use the standard side-by-side format:
   `| **#[Issue Number]: Brief Title** | Section X.Y (or File) | Original | Corrected | Issue:[#IssueLink](url) <br> PR:[#PRLink](url) |`
5. **Commit & Push:** Commit your changes with a clear, atomic commit message referencing the issue (e.g., `Fixes #1042: Correct presence scope in ContractApplied`).

---

## 5. Review and Approval
Even non-material corrections must go through the formal FOCUS review process to ensure they do not accidentally alter normative logic.

* **Drafting:** Open a PR against the `working_draft` branch. Reference the issue in the PR title and affix the label `errata`.
* **Review:** The PR must be reviewed by the Members to confirm the change aligns with the approved erratum scope.
* **Approval:** To be eligible for merging, the PR must have resolved all comments and receive approval from at least one Maintainer and the assigned reviewers.
* **Publication:** Once merged into `working_draft`, the corrections will be formally published to the `main` branch during the next release.
