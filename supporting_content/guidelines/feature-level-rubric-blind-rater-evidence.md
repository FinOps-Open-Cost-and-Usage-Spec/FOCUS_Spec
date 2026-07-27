# Feature-Level Rubric: Blind-Rater Evidence

This document records the blind-rater testing behind the [feature-level rubric principles guideline](../../guidelines/contributors/feature-level-rubric-guidelines.md) (FR 2335). It is development evidence, not specification content. Companion document: [design notes](feature-level-rubric-design-notes.md), which record the thought process and method behind the guideline itself.

**What the levels in this document are.** Every level shown here is a rater's output produced under the draft guideline with published levels removed. They measure whether the guideline text determines an answer; they are not proposed levels for any column. Level changes to existing columns are adjudicated separately, through the working group's review of the guideline and of the open level-change pull requests.

## What This Evidence Covers

Rounds 1 through 8 tested a fuller draft than the current guideline. That draft covered all four feature levels and the prior question of whether a proposed column belongs in the schema; the current guideline is scoped to the Mandatory and Conditional criteria and defers the rest. The rounds are retained in full, because the passages they exercised most heavily are the ones the narrowed guideline keeps, but the mapping needs stating precisely:

* **The rounds do carry over as evidence for the surviving text.** The applicability and producibility tests, the presence-versus-nullability discriminator, the earned-Mandatory bar, the interim boundary rule, and the directional derivation principle are all unchanged from the text rounds 7 and 8 exercised, and the sentinels that converged unanimously in round 8, the last round against that text, converged on those passages: BilledCost, EffectiveCost, ChargeClass, ContractCommitmentId, RegionId, AvailabilityZone, InvoiceId, ListUnitPrice, and ContractedUnitPrice.
* **The sentinels that never converged turned mainly on deferred material.** BillingAccountName's split ran through the necessity refinement carve-out in every round it appeared, and the round-8 outcomes for ListCost and ContractedCost were a held-out-of-schema reading against a level the fuller draft forbade. All three of those routes are admission decisions the current guideline no longer makes, so those columns are now leveled by applicability alone.
* **One unresolved observation is in scope and stands.** Raters repeatedly acknowledged a boundary case and then chose Mandatory over the interim rule's Conditional default, first in round 6 and again in round 7. That default sits in the current guideline unchanged, and whether it needs reinforcing is a live question.
* **The narrowed text was tested separately, in round 9.** Rounds 1 through 8 should be read as evidence about the surviving passages rather than as validation of this revision. Round 9 tested the narrowed text directly, under a reduced packet, and is the round to read for this revision's own determinacy. One round-8 observation is now moot: the ambiguity flagged in AvailabilityZone's Condition name came from an inheritance sentence that no longer exists, so that column is decided directly by applicability.

Principle numbers below are the ones in force at the time of each round. Later passes merged the two fabrication principles and added a Supported Features write-back, so the current guideline still carries seven, but not the same seven: what these rounds call principle 6 is now part of principle 5, derivation moved from 7 to 6, and principle 7 is new and has not been tested.

## Why Blind Raters

The guideline states its own bar: two people applying the principles to the same column should reach the same level, without the author in the room. Blind rating tests that bar directly and cheaply before human inter-rater testing. Raters receive the guideline and the evidence a leveling decision needs, with every column's published feature level, nullability, and normative requirements removed, and are instructed not to recall published levels. Where the text under-determines an answer, isolated raters diverge; where it determines one, they converge. Divergence and ungroundable answers are the signal, not agreement, because published levels appear in model training data and agreement alone could reflect memory.

## Method

Each rater receives a single packet file and may read nothing else:

* **Part A.** The guideline, verbatim, at the revision under test.
* **Part B.** The FOCUS Supported Features content, as evidence for the necessity input.
* **Part C.** A roster of other Cost and Usage columns and their current levels, for the derivability input, with all columns under test removed.
* **Part D.** The columns to classify, each as a redacted evidence pack: overview, description, and content constraints kept; feature level, nullability, and normative requirements removed.

Parts B and C served the necessity and derivability inputs, which the narrowed guideline no longer has. Round 9 ran on a reduced packet without them.

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

**Round 7 (2026-07-12, simplification re-check, three model slots run twice each, plus an informed arm).** After a simplification pass (heavy de-duplication, the summary section removed, a worked illustration on each principle, derivation symmetry replaced by the directional derivation principle, the manufactured-value reframe, and the in-flux cost and price examples removed from the applicability input), the check ran on an extended sentinel set: the seven prior sentinels, the guideline's two worked-example columns (RegionId, ContractCommitmentId), and three cost and price family probes (ContractedCost, ListUnitPrice, ContractedUnitPrice). Three raters on distinct models each ran twice on identical packets, giving six blind runs, and two informed raters on distinct models received the family's full definitions with only the published levels and nullability removed.

| Column | Six blind runs | Expected outcome |
|---|---|---|
| BilledCost (canary) | Mandatory, 6 of 6 | Mandatory, unanimous |
| EffectiveCost | Mandatory, 6 of 6 | Mandatory |
| ChargeClass | Mandatory, nulls allowed, 6 of 6 | Mandatory, nulls allowed |
| ContractCommitmentId | Mandatory, 6 of 6 | Mandatory |
| RegionId | Conditional, 6 of 6 | Conditional |
| AvailabilityZone | Conditional, 6 of 6 | Conditional |
| InvoiceId | Conditional, 4 of 6 | Conditional |
| BillingAccountName | Recommended, 5 of 6 | open question, no derivability demotion |
| ListCost | split: 2 Mandatory, 3 Conditional, 1 Recommended | see family note |

The three cost and price family probes (ContractedCost, ListUnitPrice, ContractedUnitPrice) are covered in the family note below rather than in the table, because they did not resolve to a per-column tally this round.

Six of the nine sentinels held unanimously across all six runs, and every load-bearing quote verified verbatim against the simplified text; no rater cited the removed summary section or the removed symmetry sentences. InvoiceId repeated round 6's known behavior: Conditional in four of six runs, with one rater choosing Mandatory over the interim rule's Conditional default while acknowledging the boundary, and one stray Recommended. BillingAccountName reached Recommended in five of six runs, all through the necessity refinement carve-out; this is the first round in which one reading has dominated, the derivability demotion stayed closed for every rater, and round 5's open question stands, sharpened.

The cost and price family moved, as the directional-derivation change was expected to make it. The directional principle itself behaved as designed: no rater pulled a cost down because of its unit price, and none applied a shared-level rule, since none exists to apply. But the family did not land in one place. Blind, it is bistable between two internally coherent readings that identical raters alternated between across runs: costs Mandatory with unit prices Recommended by derivability, or the whole family Conditional gated on unit pricing. Informed, with the full definitions visible, both raters converged at high confidence on costs Mandatory with Allows nulls = False (reading the tax-row and unrelated-charge substitution branches as row-scoped definitional equalities that hold in every operating model) and unit prices Recommended (fully derivable from a Mandatory cost and PricingQuantity). The blind split traces to redaction: the requirements that decide the definitional-equality versus gap-filling-substitution test are what redaction removes. The open decision this round surfaces for the working group: the earlier text carried a worked cost example that fixed which scope that test reads (a substitution for a whole class of models, versus a substitution firing on some rows in every model); the simplification removed it as in-flux, and without it the blind text no longer determines the family. These are rater outputs under the draft text, not proposed levels.

**Round 8 (2026-07-19, readability-edit check, three raters on distinct models, one run each).** Three readability edits went in for validation: the Overview's four-outcome list trimmed to its core claims, principle 6's "manufacture" wording unified to "fabricate" to match principle 5, and the input 2 definitional-equality example rewritten so EffectiveCost reads accurately (equal to BilledCost for ordinary charges, computed from it where commitments amortize, rather than an unconditional equality). The check reused round 7's extended sentinel set: the seven prior sentinels, the two worked-example columns (RegionId, ContractCommitmentId), and the three cost and price family probes (ContractedCost, ListUnitPrice, ContractedUnitPrice). Three raters on distinct models each ran once.

| Column | Three raters | Expected outcome |
|---|---|---|
| BilledCost (canary) | Mandatory, 3 of 3 | Mandatory, unanimous |
| EffectiveCost | Mandatory, 3 of 3 | Mandatory |
| ChargeClass | Mandatory, nulls allowed, 3 of 3 | Mandatory, nulls allowed |
| ContractCommitmentId | Mandatory, 3 of 3 | Mandatory |
| RegionId | Conditional, 3 of 3 | Conditional |
| AvailabilityZone | Conditional, 3 of 3 | Conditional |
| InvoiceId | Conditional, 3 of 3 | Conditional |
| ListUnitPrice | Conditional, 3 of 3 | converged this round |
| ContractedUnitPrice | Conditional, 3 of 3 | converged this round |
| BillingAccountName | 2 held out, 1 Mandatory | open question, no derivability demotion |
| ListCost | 2 held out, 1 Optional (disallowed) | non-convergent under redaction |
| ContractedCost | 2 held out, 1 Optional (disallowed) | non-convergent under redaction |

Every determinate sentinel held its round-7 outcome, and every load-bearing quote verified against the edited text. The EffectiveCost rewrite strengthened its own grounding: all three raters quoted the rewritten definitional-equality sentence as the dispositive applicability text and landed Mandatory unanimously, so the accuracy fix (the prior text overstated the BilledCost equality as unconditional, where the specification scopes it by charge category) did not cost determinacy. No rater cited the trimmed Overview bullets for any decision, direct evidence that the removed text was scaffolding rather than deciding material. Principle 6's fabricate wording drew no rater comment, and its quotes verified against the new phrasing. The unit-price probes converged this round, ListUnitPrice and ContractedUnitPrice both landing Conditional on unit pricing across all three raters, where round 7 had left the cost and price family bistable. InvoiceId landed Conditional for all three, tighter than round 7's four of six, though its known boundary wobble is unchanged.

Three observations about unchanged text were recorded. Raters flagged that input 1's inheritance phrasing points AvailabilityZone at the includes-regions Condition while a more specific includes-availability-zones Condition exists in the specification; the level holds Conditional, but the Condition name is ambiguous and one clarifying word would settle it. The weakest of the three raters output Optional for ListCost and ContractedCost, an outcome the rubric explicitly forbids, while the two stronger raters held both out of the schema; this echoes round 6's note that the held-out default may need reinforcement for weaker readers. BillingAccountName's open question stands, now under the held-out framing: two raters routed it out of the schema through the necessity refinement carve-out, the reading that dominated round 7, and one read it Mandatory through a constant-value sentence, leaving unchanged the working group question of whether the carve-out reaches display-name columns that sit under Mandatory identifiers. These are rater outputs under redaction, not proposed levels.

**Round 9 (2026-07-21, narrowing and readability check, three raters on distinct models, three arms).** The first round run against the narrowed guideline. Two changes were under test at once, so the round was run as three arms of twelve columns each, with the same three models in every arm: a control arm on the narrowed text before a plain-language editing pass, a treatment arm on the same text after that pass, and a verification arm after two sentences the treatment arm was found to have weakened were restored. The column evidence was byte-identical across all three arms, so only the guideline text varied.

The packet itself was reduced this round. The Supported Features content and the roster of other columns with their levels were both removed, because the necessity and derivability inputs that consumed them are no longer part of the guideline. That makes round 9 not directly comparable to round 8: an outcome may differ because the text changed, because the packet changed, or both. The three arms are internally comparable to each other, and every conclusion below rests on comparisons within round 9 rather than against earlier rounds.

Verification arm, the text as it now stands:

| Column | Rater 1 | Rater 2 | Rater 3 | Outcome |
|---|---|---|---|---|
| BilledCost (canary) | Mandatory | Mandatory | Mandatory | unanimous |
| EffectiveCost | Mandatory | Mandatory | Mandatory | unanimous |
| ChargeClass | Mandatory, nulls allowed | Mandatory, nulls allowed | Mandatory, nulls allowed | unanimous |
| ContractCommitmentId | Mandatory | Mandatory | Mandatory | unanimous |
| RegionId | Conditional | Conditional | Conditional | unanimous |
| AvailabilityZone | Conditional | Conditional | Conditional | unanimous |
| ListUnitPrice | Conditional | Conditional | Conditional | unanimous |
| ContractedUnitPrice | Conditional | Conditional | Conditional | unanimous |
| ListCost | Conditional | Conditional | Conditional | unanimous |
| ContractedCost | Conditional | Conditional | Conditional | unanimous |
| InvoiceId | Conditional | Conditional | Mandatory | two to one |
| BillingAccountName | Conditional | Conditional | Mandatory | two to one |

Ten of twelve were unanimous, and the canary held in all three arms. The cost and price family converged for the first time: ListCost and ContractedCost landed Conditional for every rater in every arm, each quoting the directional derivation principle, where round 7 had left the family bistable and round 8 non-convergent. Both columns are now leveled by applicability and derivation direction alone, which is what removing the admission tests was expected to do.

**The regression the arms were built to find.** In the treatment arm one column moved against its control: InvoiceId fell from Conditional in two of three raters to one of three. The cause was traced to two sentences the plain-language pass had weakened. Principle 4's "The default between them is Conditional" had become "When it is genuinely unclear which of the two applies, the answer is Conditional," and the Interim Boundary Rule's list heading "The rule:" had become "How to choose between them:". Both were restored, and the verification arm reproduced the control arm exactly, with both recovering raters quoting the restored sentences as governing. The mechanism is worth recording because it is not simply that softer wording is weaker: the added qualifier hands the reader discretion over whether the default applies at all, so the default fires inversely with reader confidence. The rater that was uncertain applied it and reached Conditional; the rater that was confident in its own analysis judged the case not genuinely unclear, skipped the default, and reached Mandatory. A default that only binds readers who already doubt themselves does not bind the reader it most needs to.

**Two observations on unchanged text.** The weakest of the three raters returned Mandatory for InvoiceId in all three arms, and in the verification arm recorded an empty governing quote with an explicit note that no sentence establishes invoicing as universal. That reading is independent of both changes under test and stands as the open question of whether a non-invoicing operating model is an exception or a pattern. BillingAccountName remained unstable across all three arms, splitting two to one in each, with individual raters swapping sides between the control and treatment arms rather than moving together. Its instability is therefore a property of the column against this text, not an effect of either change, and it independently reproduces the display-name question the design notes record as deferred. These are rater outputs under redaction, not proposed levels.

**Edits after this round.** The guideline was edited twice after the verification arm ran, so the current text is not byte-identical to what round 9 tested. The first pass corrected wording that contradicted itself or the specification: the Overview's applicability claim, the Interim Boundary Rule's all-null case, input 1's presence-gate bullet, and input 2's producibility scope. It also named the consumer-side counterpart in Scope and reconnected the flowchart's nullability subgraph. The second pass removed restatement: the Overview's preview list, principle 3's duplication of the two-axes table, and the merge of principles 5 and 6 into one. Neither pass altered a default or a rule heading, which is the change class this round identified as outcome-moving, but that is reasoning rather than evidence. A round 10 against the current text is the confirmation.

## Caveats

* **Shared model ancestry.** Round 1 used raters sharing one base model, so unanimity there is weak evidence; later rounds mixed models. The strong signals throughout are divergence, intra-model flip-flops across identical runs, and answers a rater could not ground in a quoted sentence.
* **Training-data leakage.** Published levels exist in model training data. Mitigations: redaction, the verbatim-quote requirement, synthetic columns with no published answer, and reading divergence rather than agreement as the primary signal.
* **Redaction removes normative rules by design.** A column's fallback or default rules were stripped with its requirements, so raters could not see them. This is intentional, since the guideline should carry the logic those rules encode, but it means some early findings measured the guideline's coverage rather than rater error.
* **Machine raters are a pre-screen.** A human inter-rater check at the boundary columns is the planned confirmation step before the rubric's bar is treated as met.
