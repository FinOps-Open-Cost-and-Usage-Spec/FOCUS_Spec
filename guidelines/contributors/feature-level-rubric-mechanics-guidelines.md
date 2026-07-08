# Column Feature-Level Rubric: Mechanics

## Overview

This guideline is the companion to [Column Feature-Level Rubric: Principles](feature-level-rubric-guidelines.md). The principles decide what a level means and when a column earns it. This part gives the machinery for applying them the same way every time: the step-by-step procedure, the data artifacts that make a leveling decision reproducible and checkable, and the machine-readable check that flags a column whose level does not match its recorded inputs.

Two commitments run through the whole companion, because the rubric's bar is that two people reach the same answer without the author in the room:

* **The level and its expression are both reproducible.** Two people leveling the same column reach not only the same level but the same expression of it: the same gating operating model Condition, the same primary a refining column points at, the same kind of gate. Every mechanism below is built so the author cannot pick the expression that yields the level they prefer.
* **Author-independence is enforced by review.** Wherever a mechanism reads an author-authored input (a matrix row, a refines-pointer, a leveling justification), the leveling decision for a column is confirmed by a reviewer who is not the column's author, and the author is never the sole enumerator of their own column's inputs. This rule is stated once here and relied on by the sections that need it; those sections point back to it rather than restating it.

The companion is scoped to two releases of capability. In its first release the machine-readable check flags divergence; it does not pronounce a Mandatory-versus-Conditional verdict. The data-calibrated threshold and the automated verdict both wait for inputs that do not exist yet, a conformance census and completed Supported-Feature coverage, described in [Scope and Sequencing](#scope-and-sequencing). Until those land, the interim boundary rule from the principles governs: a column at the Mandatory-versus-Conditional boundary is Conditional unless the working group records why a specific operating model is exceptional.

## The Operating Model, Made Reproducible

The threshold and the applicability matrix both count operating models, so the term needs a canonical form. Without one the count is set by how finely the operating models are sliced, and slicing is something an author can steer.

* **Definition.** For leveling a given column, an operating model is identified by the normalized set of the presence-gating operating model Conditions that are relevant to that column, drawn from the specification's Conditions section. Two candidate profiles that differ only on operating model Conditions that do not gate the column under test are the same operating model for that column's purposes, and collapse to one.
* **Why it is normalized to the column.** The Conditions section defines many operating model Conditions, and each is asserted by the generator, so the raw combination space is enormous. An unnormalized count lets an author move a level by splitting near-duplicate profiles apart or merging them together. Restricting the count to the column's own presence-gating operating model Conditions removes that lever: an operating model Condition the column does not depend on cannot change the column's operating model count.
* **The enumeration is reviewer-confirmable.** The operating models that carry a boundary column null throughout are enumerated against the Conditions section and confirmed by a reviewer other than the author, per the Overview. The set is checkable against the registry, not taken on the author's word.

## Recording Asserted Operating Model Conditions

The principles establish that asserting an operating model Condition is not a separate registration step; this section states where an assertion is read from, so a consumer or a conformance check has a definite record rather than a convention.

* **The published dataset is the record.** A data generator asserts an operating model Condition by publishing a dataset whose schema carries the columns that Condition gates. The dataset's metadata names the columns present, and under the gate taxonomy a presence-gated column is present exactly when its gating operating model Condition holds, so the asserted set is read from the published schema rather than declared through a side channel.
* **Presence binds.** Reading assertion from presence keeps the direction of principle 2: including a gated column asserts its operating model Condition and takes on the matching obligations, including the presence and values the Condition implies; it never exempts the generator from them. A generator cannot include the column and disclaim the Condition.
* **The assertion is per dataset.** The unit of leveling is a column within a dataset, so the asserted set is read per dataset; two datasets from the same generator may assert different operating model Conditions.
* **An explicit declaration is deferred, not rejected.** A metadata field that lists asserted operating model Conditions outright would make the record self-describing rather than read from the schema, but it is a specification change with its own design questions (its scope, how it evolves, and what governs when the declaration and the observed schema disagree). It is listed under [Scope and Sequencing](#scope-and-sequencing); until it exists, the published schema is the single record.

## The Leveling Procedure

A leveling decision answers the four decision inputs in the order the principles' flowchart applies them: necessity first, then derivability, then applicability variance, with producibility deciding nullability on a separate axis. The inputs keep their numbering from the principles, which is for reference rather than order of application, so each step below carries its input number and names the section that supplies its test.

1. **Necessity (input 1).** Decide whether the column is needed, on either the use-case basis or the dataset-structural basis. A column that is not needed is Recommended, or Optional only when it is genuinely discretionary. When the column appears in a Supported Feature's Directly Dependent Columns list, apply the [necessity-boundary test](#the-necessity-boundary-test-refines-versus-breaks) to decide whether it breaks the use case or only refines a result a Mandatory primary already delivers.
2. **Derivability (input 4).** Decide whether the column is fully derivable from other Mandatory columns in the same dataset instance, using the [derivation source](#the-machine-readable-check). A fully derivable column defaults to Recommended rather than being made a Mandatory obligation. When the dataset includes the derived column together with its source columns, derivation symmetry (principle 7) governs instead: the related columns are leveled together, and when the inputs would place them on opposite sides of the Mandatory-versus-Conditional line, the group is a boundary case that takes the Conditional default from the interim rule. The Recommended default applies to a derivable column outside such a group.
3. **Applicability variance (input 2).** For a needed, non-derivable column, decide whether its concept exists for every operating model or is absent for a class of them, using the [applicability threshold](#the-applicability-threshold) against the [applicability matrix](#the-applicability-matrix). A concept absent for a class of operating models makes the column Conditional, gated on the operating model Condition that marks the models where the concept exists; a concept present for every operating model makes it Mandatory.
4. **Producibility (input 3).** On the separate nullability axis, decide whether a meaningful value is available on every row where the column is present. This sets Allows nulls and never changes the level.

Every leveling decision produces a record (see [Recording Leveling Decisions](#recording-leveling-decisions)) and is confirmed by a reviewer who is not the column's author.

## The Applicability Threshold

The threshold decides when a near-universal column stays or hardens to Mandatory rather than flipping Conditional. The companion fixes the method now and calibrates the number when the data to calibrate it exists.

* **Interim rule, in force now.** One unusual operating model that lacks the column may be an exception that keeps the column Mandatory, but only when the working group records which operating model is exceptional and why. A pattern of operating models leaving the column null throughout, meaning two or more distinct operating models in the normalized sense above, makes the column Conditional. This rule is normative for the current release so that columns are actually leveled rather than left to argue out after they ship. The Conditional default is binding, not advisory: a column recognized to sit at the boundary takes Conditional unless the exception path is actually exercised, and recognizing the boundary while leveling Mandatory with no recorded exception is outside the rubric, not a judgment call within it.
* **The calibrated form, deferred.** When a conformance census of generators exists, the pattern test is restated as a prevalence share over that census: a column is Conditional when the share of operating models carrying it null throughout exceeds a set cutoff. The method around it, counting normalized operating models and reading the matrix, does not change; only the pattern test is replaced. The prevalence share and its cutoff are left open until a census exists, because there is no conformance census in the repository today.
* **Anti-gaming.** The count is over operating models normalized to the column, so it cannot be inflated by asserting unrelated operating model Conditions. The author is not the sole enumerator of the count. A later change to the threshold parameter carries a written change rationale, so the parameter cannot be loosened quietly to re-level many columns at once.

## The Applicability Matrix

The applicability matrix records which columns are gated by which operating model Conditions. A standalone data file is its single source of truth; the matrix rendered in this guideline and the machine-readable check both read from that file.

* **The file is an independent expected-state.** The file is authored and reviewed as its own artifact, not generated from the dataset requirements. That independence is the point: because the file states what the gating should be, the check can diff it against the dataset requirements and the model rules and catch a place where they disagree. A view generated from the dataset requirements would only re-render whatever those requirements already say, so it could never surface an error in them.
* **The reconciliation check is not optional.** Without the check that reconciles the file against the dataset requirements and the model rules, the file is only a second hand-maintained copy of the gating, with the same exposure as no file at all. The reconciliation check reads every place a gate can appear: the dataset requirements, the `ApplicabilityCriteria` on the composite and dataset-level model rules, and the Requirements bullets of each column, not just the column-table anchor, because a column may be gated in more than one place, may carry more than one gate, or may be a gated `SHOULD` with no anchor in the column table.
* **Shape.** Each entry keys on a dataset and a column and records its presence-gating and nullability-gating operating model Conditions, and the level and nullability the column file authors. A sketch:

```json
{
  "CostAndUsage/RegionId": {
    "presenceGates": ["IncludesRegions"],
    "nullabilityGates": [],
    "authoredLevel": "Conditional",
    "authoredNullability": "AllowsNulls"
  }
}
```

The initial population of the file is compiled once the requirements-model changes below are in place, so that the file, the model rules, and the dataset requirements are reconciled from the start rather than diverging on day one.

## The Necessity-Boundary Test (Refines Versus Breaks)

Input 1's carve-out demotes a column that only refines a result a Mandatory primary already delivers, and keeps a column that breaks the use case without it. The companion makes that boundary a small, reviewable artifact rather than a judgment call.

* **The refines-pointer.** A refining column carries a one-line pointer that names the Supported Feature and the primary column it refines. The pointer is a reviewable artifact, not a sentence buried in prose, so a reader can see and a reviewer can confirm which primary is claimed. The carve-out demotes the refining column only when that primary is itself Mandatory, per the principles; a column that refines a Conditional primary is not demoted and is leveled by the remaining inputs, typically inheriting the primary's operating model Condition.
* **The primary is determined, not chosen.** So that the expression is reproducible and not just the level, which column counts as the primary for a feature's result comes from a per-feature mapping of the feature's primary result to the column that delivers it, not from the author's choice. That mapping depends on the Supported Features naming the columns each use case depends on, which is the Directly Dependent Columns coverage work. Until that coverage is complete the mapping is filled in feature by feature as coverage lands; in the interim the pointer is authored and confirmed by a reviewer other than the column's author.
* **The rerun is a falsification check only.** A drop-the-column rerun of a feature's example query may be used, and only where that query's selected columns and its grouping columns coincide, to flag a pointer that a clean rerun contradicts: structure says the column refines, behavior says it breaks. Such a contradiction goes to the working group; the rerun never demotes a column on its own, because it trusts an author-written query and many features have no runnable query at all.

## Recording Leveling Decisions

The principles defer two record obligations to the companion: the justification for keeping a column Mandatory by declaring a specific operating model exceptional, and the log of boundary cases whose variance fits no operating model Condition. Both get a durable home, and the per-column justification is also enforced by the build.

* **The records registry.** A dedicated versioned file in the repository holds both records: the exceptional-model justifications and the cross-column boundary-case log. The file participates in the build's include validation so an entry cannot rot silently after the case that created it is resolved. The registry is authoritative; a pull request body is only where a leveling decision is proposed, not where it lives.
* **Per-rule enforcement in the requirements model.** A column kept Mandatory by an operating model exception also carries a leveling-justification field on its model rule, and the build fails when a Mandatory-by-exception rule lacks it. The registry is the human-auditable record and the model field is the machine-enforced one; the two are written together and are expected to agree.
* **Expression is recorded, not only level.** The record for a Conditional column names its gating operating model Condition; the record for a refining column carries its refines-pointer; the record for either names the kind of gate. Recording the expression is what lets a later reviewer confirm that two people would express the level the same way, not merely arrive at the same level.

## Variance That Fits No Operating Model Condition

Some columns vary by a billing relationship or a marketplace topology, such as which entity issues the invoice or whether a host provider is exposed to the customer, which is not cleanly "the operating model includes X". The companion disposes of this variance intrinsic-first, with an objective test for the one lever that could otherwise move a level.

* **Default disposition.** Where the variance can be stated as a rule about the row itself, express it as an intrinsic gate rather than forcing it into an ill-fitting operating model Condition. The column's level is already pinned by the interim boundary rule, so this disposition settles how the variance is expressed, not what the level is.
* **The definitional-equality discriminator is objective.** The one lever that could move a level here is relabeling a gap-filling default as a definitional equality to keep a column Mandatory. The test that closes it: a rule that equates the column's value to another column is a definitional equality, and leaves the concept universal, only when the equated value is defined for the rule's specified rows in every operating model. A rule that substitutes another column's value only for the operating models that lack the concept is a gap-filling default, and marks the concept as not universal, so the column is Conditional. This is the same distinction the principles draw, stated here as a test a reviewer can apply the same way twice.
* **Escalation.** Variance that fits neither an operating model Condition nor a clean intrinsic rule goes to working-group adjudication, with the disposition written into the records registry. A third kind of gate, beyond the intrinsic and operating model gates the principles define, is held in reserve and not introduced now, because only a small number of columns would use it and its boundary is contested at the first real column.

## The Informative Layer (Category Defaults)

The rubric produces a non-normative informative layer: per category, the operating model Conditions typically met in that category today. It has to stay outside anything the conformance check reads, or a category default could leak back into a level-determining check.

* **Its home is this guideline.** The category-defaults table lives in this guideline: outside the specification, as the principles expect, and physically outside the files the check consumes. Educational materials may mirror the table, but this guideline's copy is the one the refresh keeps current. Putting the defaults into the Conditions section, or into a data file that a level-determining check reads, is not allowed, because it would place category strings inside the exact firewall the rubric exists to hold.
* **Referential integrity is checked outside the conformance scope.** A markdown-lint rule, not the requirements-model test layer, asserts that every operating model Condition named in the table exists in the Conditions section. The check keeps the table honest without giving a conformance check anything category-shaped to read.
* **It is refreshed, not authoritative.** The table records today's expectations without binding tomorrow's generators, and is refreshed each release from the back-test's snapshot. The initial table is filled once the category data is compiled; a generator may always go past its category default, per principle 2 (defaults are not ceilings).

## The Machine-Readable Check

The check runs as tests over the merged model, a derivation source, and a Conditions map. In this release it flags divergence; it does not decide a level.

* **It reads the authored level; it does not infer it.** The check reads the feature level a column file authors and the keyword on each gate. It never infers a level from the rule-ID suffix, because that suffix does not carry the level distinction the rubric needs. The check's job is to flag a column whose authored level diverges from what its recorded gates and derivation imply, for a human to resolve.
* **The derivation source.** A `derivations.json` file records, per column, what it derives from and by what relation, one of arithmetic, lookup, or conversion, with the direction of the derivation stated explicitly and an evidence rule identifier on every arithmetic edge. The direction is recorded independently of any result-column field, so a cost and its unit price are not read in the wrong direction.
* **The Conditions map.** A `conditions_map.json` file maps the requirements model's older `ApplicabilityCriteria` keys (for example, `REGION_SUPPORTED`) to the matching operating model Condition IDs (for example, `IncludesRegions`). It is allowed to be partial: a key with no Condition yet emits an explicit unmapped-key finding rather than failing the build or being silently dropped. The keys that have no counterpart today are minted as Conditions or dispositioned explicitly as part of the requirements-model changes below.
* **What it validates in this release.** Structural validity, that every column has a level and every Conditional column links to an operating model Condition that exists in the Conditions section; Condition linkage, that the `ApplicabilityCriteria` keys resolve through the map; and derivation consistency, that derivation edges reference real columns and that a fully derivable column outside a derivation symmetry group is not authored Mandatory. The automated Mandatory-versus-Conditional verdict is deferred to when the threshold is data-calibrated and Supported-Feature coverage is complete.

## Requirements-Model Changes

The companion introduces a small set of changes to the requirements model, implemented through the normal downstream per-release model sync.

* **A leveling-justification field** on the rule of a column kept Mandatory by an operating model exception, naming the exceptional operating model, the rationale, and the decision reference. The build fails when a Mandatory-by-exception rule omits it.
* **Per-column derivation fields**, a `DerivesFrom` and a `RelationKind`, so the derivation source can be assembled from the model rather than from prose equalities scattered across column files.
* **The Conditions map, and the Conditions it exposes as unmapped.** The keys with no Condition counterpart today are either minted as operating model Conditions in the Conditions section or dispositioned explicitly, so the map's unmapped-key findings resolve to a decision rather than a gap.

## The Back-Test

The back-test re-levels existing columns against the rubric. It is planned here and run once its prerequisite lands.

* **What it produces.** The back-test flags existing Mandatory columns that satisfy neither necessity basis, of which administrative and audit columns are the common case, and states the handling for each: re-level it, or record the dataset-structural basis that keeps it Mandatory. The re-leveling output is a reviewed list, not an automatic rewrite.
* **Its prerequisite.** The back-test does not run until the Supported Features name the columns each use case depends on, because a column needed on the use-case basis but absent from every Directly Dependent Columns list has nothing for the necessity input to point at. Completing that coverage, especially for the datasets beyond Cost and Usage, is a prerequisite this guideline calls out rather than assumes.

## Scope and Sequencing

* **In this release:** the leveling procedure, the normalized operating model definition, the assertion-recording rule (the published schema as the record), the interim threshold rule, the refines-pointer, the records registry and the per-rule leveling-justification field, the intrinsic-first disposition, the informative-layer table, and the flag-only check covering structure, Condition linkage, and derivation consistency.
* **Waiting on a conformance census:** the data-calibrated prevalence threshold and the automated Mandatory-versus-Conditional verdict.
* **Waiting on Directly Dependent Columns coverage:** the per-feature primary-result mapping and the back-test.
* **Deferred without a data prerequisite:** an explicit metadata declaration of asserted operating model Conditions, per [Recording Asserted Operating Model Conditions](#recording-asserted-operating-model-conditions).
* **Depends on the principles.** This companion assumes the principles as finalized in their guideline, and follows once those are approved.
