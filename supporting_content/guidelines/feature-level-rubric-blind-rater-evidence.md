# Feature-Level Rubric: Blind-Rater Evidence

This document records the blind-rater testing behind the [feature-level rubric principles guideline](../../guidelines/contributors/feature-level-rubric-guidelines.md) (PR 2507, FR 2335). It is development evidence, not specification content. Companion document: [design notes](feature-level-rubric-design-notes.md), which record the thought process and method behind the guideline itself.

**What the levels in this document are.** Every level shown here is a rater's output produced under the draft guideline with published levels removed. They measure whether the guideline text determines an answer; they are not proposed levels for any column. Level changes to existing columns are adjudicated separately, through the working group's review of the guideline and of the open level-change pull requests.

## Why Blind Raters

The guideline states its own bar: two people applying the principles to the same column should reach the same level, without the author in the room. Blind rating tests that bar directly and cheaply before human inter-rater testing. Raters receive the guideline and the evidence a leveling decision needs, with every column's published feature level, nullability, and normative requirements removed, and are instructed not to recall published levels. Where the text under-determines an answer, isolated raters diverge; where it determines one, they converge. Divergence and ungroundable answers are the signal, not agreement, because published levels appear in model training data and agreement alone could reflect memory.

## Method

Each rater receives a single packet file and may read nothing else:

* **Part A.** The guideline, verbatim, at the revision under test.
* **Part B.** The FOCUS Supported Features content, as evidence for the necessity input.
* **Part C.** A roster of other Cost and Usage columns and their current levels, for the derivability input, with all columns under test removed.
* **Part D.** The columns to classify, each as a redacted evidence pack: overview, description, and content constraints kept; feature level, nullability, and normative requirements removed.

Protocol rules: every classification carries verbatim quotes of the Part A sentences that governed each decision input, so memorized answers are separable from grounded ones; a rater who finds no governing sentence records an empty quote and describes the missing sentence; raters flag any column whose level could flip on the boundary threshold the guideline defers to the companion mechanics guideline. BilledCost is carried as a canary in every round: a rater or a revision that moves it off Mandatory fails the round.

## Rounds

**Round 1 (2026-07-01, four raters, 13 columns).** First pass against the original draft. The canary held and the clean anchors reproduced, but the boundary columns were unstable: InvoiceId, BillingAccountName, InvoiceIssuerName, and ChargeClass split across raters, and ListCost unanimously landed opposite the draft's own worked position. The failures traced to specific missing or contradictory sentences, and drove the reframe in which Mandatory is a high bar a column earns rather than the default.

**Round 2 (2026-07-01 to 07-02, adversarial review).** Five blind raters, three informed raters (full column definitions, levels removed), and targeted attack prompts, over 23 columns including two synthetic net-new columns with no published answer. This round measured test-retest stability by running identical raters repeatedly: the same model produced different levels for InvoiceId and BillingAccountName across identical runs, locating the instability in the text rather than in any rater. Its findings produced the revision set applied on 2026-07-02.

**Round 3 (2026-07-02, revision verification).** Three raters re-leveled the previously unstable columns against the revised text. Every previously split column converged to the expected outcome: InvoiceId to Conditional, ChargeClass to Mandatory with nulls allowed, EffectiveCost Mandatory alongside ListCost Conditional, and the two demotion paths that had pulled BillingAccountName and AvailabilityZone off their expected levels no longer fired.

**Round 4 (2026-07-03, clarity-pass re-check).** After a clarity and accuracy editing pass, the re-check on the affected columns held all outcomes.

**Round 5 (2026-07-06, restructure re-check, three raters on distinct models).** After the guideline was restructured for standalone readability (terms defined before use, seven self-contained principles, one home for the interim boundary rule), three raters on distinct models re-leveled the seven sentinel columns:

| Column | Rater 1 | Rater 2 | Rater 3 | Expected outcome |
|---|---|---|---|---|
| BilledCost (canary) | Mandatory | Mandatory | Mandatory | Mandatory, unanimous |
| InvoiceId | Conditional | Conditional | Conditional | Conditional |
| ChargeClass | Mandatory, nulls allowed | Mandatory, nulls allowed | Mandatory, nulls allowed | Mandatory, nulls allowed |
| EffectiveCost | Mandatory | Mandatory | Mandatory | Mandatory |
| ListCost | Conditional | Conditional | Conditional | Conditional |
| BillingAccountName | Mandatory | Recommended | Mandatory | no derivability demotion |
| AvailabilityZone | Conditional | Conditional | Conditional | no carve-out demotion |

Six of seven columns were unanimous and matched the expected outcomes. Raters quoted the restructured text's new sentences as deciding material, including the presence-versus-nullability discriminator (settling ChargeClass) and the Conditional-primary inheritance rule (settling AvailabilityZone). InvoiceId and ListCost converged on the interim boundary rule's Conditional default with the companion-threshold flag set, which is the designed behavior for boundary columns.

**Open question from round 5.** BillingAccountName split two to one. The minority rater demoted it to Recommended through the necessity refinement carve-out, reading the display name as only refining a result its Mandatory identifier already delivers. The derivability demotion path closed in round 3 stayed closed for all three raters, and the carve-out sentence was unchanged by the restructure, so this is a latent reading surfaced by re-sampling rather than a regression. It stands as an open design question for the working group: whether the refinement carve-out applies to display-name columns that sit under Mandatory identifiers.

**Round 6 (2026-07-08, summary-section check, three raters per run).** A plain-language summary section, The Rubric in Brief, was added after the guideline's Overview, built only from sentences reused verbatim from the guideline and pointer lines that defer to the governing sections. To confirm the summary changes no leveling outcome, the seven-column check ran twice with fresh raters: once on the guideline with the summary in place, and once without it. BilledCost held Mandatory for every rater in both runs; ChargeClass, EffectiveCost, and AvailabilityZone matched expected outcomes unanimously in both; InvoiceId split the same way in both runs, one rater choosing Mandatory while acknowledging the boundary. Every deviation observed with the summary also appeared without it, the run without the summary showed one additional deviation (on ListCost), and no rater cited the summary as the basis for any level, so the summary introduced no new divergence. Two observations about the unchanged text were recorded: BillingAccountName reached Mandatory for zero of six raters across the two runs, through three distinct readings (the necessity refinement carve-out, principle 4's Conditional default, and applicability variance), sharpening round 5's open question; and in three instances a rater acknowledged a boundary case yet chose Mandatory over the interim rule's Conditional default, suggesting that default may need reinforcement. These are rater outputs under redaction, not proposed levels.

## Caveats

* **Shared model ancestry.** Round 1 used raters sharing one base model, so unanimity there is weak evidence; later rounds mixed models. The strong signals throughout are divergence, intra-model flip-flops across identical runs, and answers a rater could not ground in a quoted sentence.
* **Training-data leakage.** Published levels exist in model training data. Mitigations: redaction, the verbatim-quote requirement, synthetic columns with no published answer, and reading divergence rather than agreement as the primary signal.
* **Redaction removes normative rules by design.** A column's fallback or default rules were stripped with its requirements, so raters could not see them. This is intentional, since the guideline should carry the logic those rules encode, but it means some early findings measured the guideline's coverage rather than rater error.
* **Machine raters are a pre-screen.** A human inter-rater check at the boundary columns is the planned confirmation step before the rubric's bar is treated as met.
