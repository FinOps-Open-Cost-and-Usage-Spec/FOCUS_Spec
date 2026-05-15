# FOCUS Development Process

## FOCUS 1.5 — Operating Model Augmentation Discussion

**Related Issue:** AI #2183
**Context:** TF3 discussion on 2026-04-10 (Udam Dewaraja, Sanjna Srivatsa, Irena Jurica)

---

### 1. Dual Input Model

#### Problem Being Addressed

A non-draft Pull Request that adds or modifies content under `/specification` or `/guidelines` is currently the only formal mechanism for introducing work into Task Force consideration. High-quality input often arrives too late in the lifecycle. Meaningful pre-specification work does not receive sufficient emphasis in the current process, and in cases where Supporting Content is hosted on Google Drive rather than in the GitHub repository, it may not be captured at all. This directly contributes to the 300+ comment volume observed over recent releases — when the specification PR is the first place a topic is formally discussed, all alignment work lands there.

#### Proposed Change

FOCUS 1.5 operates two equally important input channels. Both channels use the Pull Request mechanism within the same GitHub repository, but they differ in what content they govern and the level of rigor applied.

#### A. Specification Channel

* Governs content under `/specification` and `/guidelines` in the FOCUS repository
* Content merged through this channel constitutes the normative specification
* Final decision and merge authority applies to specification and guidelines content included in the PR
* Enforces full alignment with editorial guidelines, normative requirements guidelines, and the requirements model
* Remains the official specification boundary

#### B. Supporting Content Channel

* Governs content under `/supporting_content` in the FOCUS repository, plus materials hosted on Google Drive
* Serves as a structured input for pre-specification shaping
* Provides context and rationale for specification development
* Remains active during and after specification PR creation
* Supports asynchronous discussion alongside synchronous meetings

The Supporting Content Channel is a continuous working layer across the entire lifecycle of a change:

**Pre-Specification Phase:**

* Idea development and structuring
* Early design exploration and analysis
* Drafting and refining concepts before specification PR creation

**During Specification Phase:**

* Asynchronous discussion alongside active specification PR review
* Extension of synchronous meeting discussions
* Clarification of intent, rationale, and design decisions

**Post-Specification Phase:**

* Ongoing context preservation
* Follow-up discussion and refinement of understanding
* Reference layer for future changes

#### Key Principle

* The Specification Channel remains the decision layer
* The Supporting Content Channel is the shaping layer

#### Engagement Tracking Note

* Supporting Content that lives under `/supporting_content` in the GitHub repository is submitted via PRs, and engagement on those PRs (comments, reviews, authorship) is captured by the existing engagement report alongside specification PRs. Supporting Content that lives on Google Drive, and async contribution via Slack, is not captured by the current engagement automation.

* Additionally, the Champion Scope model is expected to generate ad-hoc coordination meetings beyond the scheduled TF-1, TF-2, TF-RM, and Open Forum sessions. Attendance and contribution at these meetings is not currently tracked. These asymmetries should be noted when interpreting engagement metrics.

#### Disclaimer Requirement

Every file under `/supporting_content` and every Supporting Content artifact on Google Drive must include a visible disclaimer making it clear to readers that:

* The content is working-level material, not normative specification
* The content may be out of date relative to the current published specification
* The content exists as a space where contributors develop ideas and discuss approaches
* Readers should treat the content accordingly and verify against the specification for authoritative statements

The exact wording and placement of this disclaimer is to be agreed by Maintainers, but its presence on every Supporting Content file is a requirement of this proposal.

#### Relationship to Scope Proposal

The Scope Proposal does not define a Supporting Content Channel or a dual input model. The Champion Scope process described in Section 5 of the Scope Proposal requires a PR as the entry point for TF consideration. This proposal introduces a parallel input path that operates alongside — not in place of — that process.

---

### 2. Champion Scope Intake — Extension of Scope Proposal Section 5

#### Problem Being Addressed

TF scope inclusion currently depends too heavily on specification PR maturity. Early ideas lack structured entry pathways. The Scope Proposal Section 5 ("Accepting Champion Scope") defines three criteria for introducing an out-of-scope Feature Request for TF discussion:

1. A Pull Request (PR) must be issued for the feature.
2. At least one Maintainer (who is not the original author) must approve the PR.
3. The PR can then be formally discussed in TF-1, TF-2, or TF-RM, to be assigned at the discretion of the WG Chair.

This is appropriate for mature, well-formed contributions. However, it does not provide a path for emerging ideas that are well-structured but not yet ready for specification PR formalization.

#### Proposed Change

TF consideration can be initiated from two sources:

**Specification-Based Entry (Existing — as defined in Scope Proposal Section 5):**

* Fully formed specification PR
* Subject to formal review and approval process
* At least one Maintainer approval required

**Supporting Content-Based Entry (Proposed Extension):**

* Based on well-formed Supporting Content artifact
* Can originate from `/supporting_content` in the repository or from Google Drive
* Eligible for TF consideration prior to specification PR creation

#### Impact

* Earlier signal of emerging ideas
* Reduced specification PR overhead for discovery and alignment
* Improved filtering before formal specification work begins

#### Key Principle

This is a material change to the intake process defined in the Scope Proposal. Specification-Based Entry remains the path to formal specification. Supporting Content-Based Entry provides a structured alternative for early-stage work that is not yet ready for specification PR formalization but has sufficient substance for TF evaluation.

---

### 3. SME Contribution Path

#### Problem Being Addressed

Guideline complexity increases friction. AI capability is uneven across contributors. GitHub-based workflows can be a barrier for SMEs. The widening gap between domain practitioners and normative/requirements model authoring work — raised by Sanjna and Irena in TF3 — makes it hard for FinOps contributors to engage without feeling buried in process.

#### Proposed Change

Contributors can engage at two levels, both of which require basic interaction with GitHub:

**Low-friction contribution paths** — do not require familiarity with specification structure, editorial guidelines, requirements authoring guidelines, or requirements-model expectations:

* Task Force discussion and evaluation
* Supporting Content creation (GitHub `/supporting_content` or Google Drive)
* GitHub comments on PRs

**Specification-level contribution paths** — require familiarity with the above:

* Specification PR authoring (content under `/specification` or `/guidelines`)

Low-friction paths are not preliminary steps toward specification authoring. They are valued contribution modes in their own right. Contributors who engage exclusively through low-friction paths are making meaningful contributions to the development of the specification.

#### Impact

* Lowers entry barriers for contributors with domain expertise
* Preserves SME participation without requiring specification-level compliance as a starting point

#### Key Principle

Basic GitHub interaction is required across all paths. The distinction is not between GitHub and non-GitHub contribution, but between contribution that requires specification-level editorial and structural knowledge and contribution that does not.

Low-friction contribution paths include the ability to initiate TF consideration via the **Supporting Content-Based Entry** (see *2. Champion Scope Intake*), without requiring a specification-level Pull Request.

#### Relationship to Scope Proposal

The Scope Proposal Section 3 describes the Open Forum as a space where "Working group members can bring and discuss whatever they wish." The SME Contribution Path formalizes structured ways to contribute between the Open Forum and the specification-based Champion Scope intake, without requiring specification-level participation as a starting point.

