# Feature-Level Rubric: Design Notes

This document records the thought process behind the [feature-level rubric principles guideline](../../guidelines/contributors/feature-level-rubric-guidelines.md) (PR 2507, FR 2335): the problem it answers, the design choices considered, the applicability-matrix method the companion mechanics guideline will carry, and the questions still open. It is development background, not specification content, and parts of it describe analysis that is ongoing or still to be stress tested. Where a column level appears here, it is the output of reasoned analysis under the draft rubric, not a proposal to change any column. Companion document: [blind-rater evidence](feature-level-rubric-blind-rater-evidence.md), which records how the guideline text itself was tested.

## The Problem the Rubric Answers

A FOCUS column's feature level has historically been an output, not a choice. The level falls out of how the presence requirement happens to be written: an unconditional MUST reads as Mandatory, a conditional MUST as Conditional, a SHOULD as Recommended, a MAY as Optional. Nothing decided what the requirement should be in the first place, so each column was leveled case by case, and leveling debates recurred because there was no rule to appeal to.

Two recurring failures motivated the rubric:

* **Presence and nullability argued as one question.** "Make it Mandatory, generators without it can carry it null or fill it from another column" answers a presence question with a nullability answer. The concrete in-spec trace is a Mandatory cost column whose definition resolves non-applicable operating models through a default to another column, so the presence question never gets asked.
* **Related columns drifting apart.** Columns bound to the same concept, or linked by derivation, landed at different levels with no rule to settle the split (a cost Mandatory while its unit price is Conditional).

Underneath both, Mandatory had become the default rather than a high bar, so columns that only some operating models can produce were mandated anyway, and the generators that could not produce them faced a choice between padding values and carrying dead columns. That is an adoption barrier for SaaS, AI, and internal-IT data generators, and removing it is the rubric's primary goal.

## Why the Operating Model is the Leveling Basis

The rubric levels by operating model, never by technology category, for three reasons:

* **Categories classify generators, not schemas.** A category (cloud, SaaS, PaaS, data center, AI) describes who the data generator is. It carries no normative force about what their billing data contains. The characteristics that actually decide whether a column applies (does the model include regions, commitment discounts, virtual currency) cut across categories.
* **Category names churn.** What are called technology categories today were called scopes earlier, and may be renamed again. A rubric keyed to category names would inherit that churn; one keyed to operating model characteristics does not.
* **Category rules leak into levels.** Any rule of the form "SaaS does not populate X" hides a category inside a normative statement and caps generators by their label. The rubric's phrasing guardrail exists to keep that construction out of the specification: levels and defaults are never written as category restrictions, and a generator may meet any operating model Condition regardless of how it is classified.

The operating model Conditions vocabulary (the specification's Conditions section, each entry reading "the operating model includes X") is what makes this workable: applicability variance is expressed as a named, self-asserted, verifiable state instead of a category assumption.

## Why Mandatory is Earned

The rubric's central reframe makes Mandatory a high bar a column earns: the concept exists for every operating model and a value is naturally producible, so no reasonable generator would have it null on every row. Anything a reasonable operating model would leave entirely null is Conditional, gated on the operating model Condition that marks where the concept lives.

The reframe was not the starting position. Earlier drafts treated Mandatory-with-honest-nulls as the safer default because it preserves a stable column set for consumers. Blind-rater testing moved the design: raters applying the earlier text kept re-deriving Conditional for columns whose concept is not universal, and the fallback rules that propped up Mandatory for those columns turned out to be the same gap-filling defaults the rubric was written to catch. The consumer-stability concern did not disappear; it moved into two guardrails (the definitional-equality versus gap-filling-default distinction, and the interim boundary rule's recorded-exception path) and into an open consumer-side question noted below.

## The Applicability Matrix and the Flip Criterion

The companion mechanics guideline carries the data-driven test the principles defer to. Its method is designed and has been dry-run; its calibration has not happened, because the data to calibrate it does not exist yet. The method:

* **The matrix.** Rows are columns under test; columns are representative operating-model profiles, current and prospective (cloud hyperscaler, flat-rate SaaS, usage-based SaaS, PaaS, data center, AI provider, internal IT). Each cell records how that profile would treat that column: **P** (populated), **N** (null), **F** (a value would have to be fabricated), or **?** (unknown).
* **The flip criterion.** A column that is F, or all-N across every row, for more than roughly a third of representative non-cloud profiles is Conditional, gated on the operating model Condition that distinguishes the profiles where it is live. A column that is mostly P with occasional row-level N is Mandatory with Allows nulls = True. Any F cell is treated as disqualifying for the current level, because a fabrication-forcing level is never correct.
* **The threshold is a parameter, not a principle.** The one-third trigger is directional. The designed calibration restates the pattern test as a prevalence share over a census of real generator exports, with the cutoff set from that data. The directional expectation is that one unusual operating model is an exception and two or more distinct operating models are a pattern, but the number is an evidence question.

### What the Dry Run Showed

A full dry run of the matrix and a back-test across the audit columns were performed during design (2026-06-29). The honest status of that run:

* **Only the cloud anchors are measured.** The populated cells for cloud profiles come from real data. Every non-cloud cell that actually drives the flip criterion is operating-model inference (reasoning about what a flat-rate SaaS would populate), because no non-cloud generator's FOCUS export was available cell by cell. The threshold can presently be reasoned but not empirically calibrated.
* **The structural columns are stable.** Region, resource, commitment-discount, and sub-account families sit far from the flip line under any plausible threshold; their levels do not move as the parameter moves.
* **A pricing and usage cluster is threshold-sensitive.** Unit-price columns, the SKU family, and consumed-quantity columns sit near the one-third line, and their levels genuinely depend on where calibration lands. This is why the rubric refuses to settle them by argument and why the interim boundary rule exists.
* **The back-test surfaced real gaps, not just confirmations.** Derivation symmetry flagged the cost-versus-price level splits. Two operating model Conditions the analysis leans on did not exist in the Conditions section at the time: a principals or actor-identification Condition, and any marketplace, reseller, or billing-relationship Condition. The second is the known boundary of the operating-model abstraction: applicability that turns on which entity issues the invoice, or whether a host provider is exposed to the customer, does not phrase cleanly as "the operating model includes X," and the guideline routes such variance to a recorded boundary case rather than forcing an ill-fitting Condition.

## Design Questions Still Open

These are known and deliberately unresolved; several need stress testing or data before they can be settled:

* **Exception versus pattern at n = 1.** The interim rule lets the working group record one unusual operating model as an exception that keeps a column Mandatory. The opposing position: when the variance is a genuine, admissible operating model Condition, even a single generator exhibiting it argues for Conditional, because a Condition either exists or it does not. The tension is between honesty about applicability and a gaming concern (one poor implementation becoming the hook that demotes a column everyone else populates). The Condition-admissibility rule (a Condition must name an independent operating-model characteristic, not the presence of the column it gates) is the current guard; whether it is sufficient is untested.
* **All-null versus fabrication, same treatment or split.** The flip criterion treats a high-N column and an any-F column similarly (both push to Conditional), but they are different harms: a dead column versus a corrupting value. Whether the rule should split is open.
* **The refinement carve-out and display-name columns.** The necessity carve-out demotes a column that only refines a result another Mandatory column already delivers. Applied to display names that sit under Mandatory identifiers, that reading demotes them to Recommended; it has now been observed twice in blind-rater testing. Whether the carve-out is meant to reach identifier-name pairs, or only classification hierarchies, needs an explicit decision.
* **Recommended's routing.** The rubric routes useful-but-not-needed columns to Recommended. Whether Recommended remains a level the specification wants columns routed to at all is a live discussion; if it changes, the rubric's necessity output re-routes accordingly.
* **The consumer-side counterpart.** The rubric constrains generators (no padding, no fabrication) but does not yet say how cross-generator Supported Features behave when a Conditional column is absent, which by default leaves consumers to silently exclude data. The likely shape is a write-back: feature definitions state their behavior across Conditional columns. This is under discussion and unwritten.
* **Calibration data.** The prevalence threshold waits on cell-level column-population evidence from real non-cloud generator exports: conformance submissions are the natural source, targeted requests to non-cloud generators the alternative. Until then the interim boundary rule governs, and it is expected to govern the whole current release cycle.

## Relationship to the Guideline and the Companion

The principles guideline carries what is stable: the operating-model basis, the earned-Mandatory bar, the two axes, the four decision inputs, the gate taxonomy, the two-layer output, and the interim boundary rule. The companion mechanics guideline carries the machinery described here: the matrix, the calibrated threshold, the records, the back-test, and a machine-readable check. The split is deliberate: the principles can be adopted and applied with the interim rule now, and nothing in them changes when calibration replaces the interim rule with a measured threshold.
