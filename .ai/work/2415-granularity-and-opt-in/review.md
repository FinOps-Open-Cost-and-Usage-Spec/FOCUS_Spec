# PR #2473 Review: Glossary and Content Alignment

Reviewed 2026-09-13 against branch HEAD `a978845c` and `origin/working_draft`. Normative content under `specification/` is prioritized over `supporting_content/`.

## 0. Sync With `working_draft` First

The branch is 17 commits behind `working_draft`. Changes on the base that affect this work:

* `specification/glossary.md` gained Principal and Requester entries, and dataset links moved from `#datasets.*` to `#datamodel.*`. New glossary entries need the new anchors.
* The Normative Requirements Guidelines were rewritten: Constrainable Entity model, condition grouping bullets, documentation qualifier forms, and "Normative bullets MUST NOT begin with an article".
* PR #2360 merged. PrincipalId is now a Conditional Cost and Usage column tied to `IncludesRequesterAttribution` (`specification/operating_model_conditions/`). See 2.3 F.
* `dataset_configuration.md`, `attributes_overview.md`, and the supporting content file are unchanged on the base, so merging should not conflict.

## 1. Glossary Entries

### 1.1 Decisions Behind the Entries

* **Adopt `detail variant` in place of `detail level`.** @ijurica's reason is that "level" implies an ordinal scale. It also collides with "Feature level", which appears 164 times in Content Constraints tables. And "level of detail" invites the time-granularity reading that TF-2 dropped on 2026-07-22.
* **Adopt `detail representation` in place of `delivery method`.** "Delivery method" sits next to DeliveryHandling's "delivery mechanism" (Overwrite/Append). The concept describes how detail is shaped relative to other records, and only one of its three cases involves a separate delivery.
* **Rename the `Replacement` value to `Expanded`.** "Replacement" is already a CorrectionHandling correction style that uses the Overwrite mechanism.
* **Fold `data coverage` into Detail Scope.** The TF-2 action item (2026-08-26) listed it as a fourth term, but it only restates which records a scope covers. The requirement bullets can say that directly, which leaves one less term to define. A fallback entry is below in case TF-2 prefers to keep it.
* **Count the default output as a detail variant.** The current bullet only requires configurability "when the same data coverage can be delivered at more than one detail level". If the default isn't a level, a scope with one optional level never triggers that MUST, so the opt-in isn't guaranteed. This is the question @Matt-Cowsert raised on 2026-06-30. Defining the default as a variant settles it. **TF-2 decision needed.**
* **Keep Companion Artifact actor-neutral.** "Provider-defined" is ambiguous here, since the glossary uses both "service-provider-defined" and "data generator-defined". The entry says instead that FOCUS doesn't define the artifact's structure. That covers @ijurica's intent (either party can define it), and it stays true if FOCUS later adds a standard detail dataset.
* **Leave Dimension and Metric unchanged in this PR.** Both glossary entries exclude custom columns ("specification-defined", "FOCUS-defined"), which conflicts with other spec usage (e.g., `x_BillingModel` as a Dimension). The requirement wording in section 2 avoids depending on them. Raise a separate maintenance issue to align those entries.

### 1.2 Proposed Entries

Insert Companion Artifact between Commitment Program and Contract. Insert the three Detail entries between Delivery Scope and Dimension.

```markdown
<a name="glossary:companion-artifact"><b>Companion Artifact</b></a>

An artifact delivered alongside a [*dataset artifact*](#glossary:dataset-artifact) that contains records at a selected [*detail variant*](#glossary:detail-variant) for a [*detail scope*](#glossary:detail-scope) (e.g., a separate file or table). A companion artifact is not a dataset artifact of a [*FOCUS dataset*](#glossary:FOCUS-dataset), and its structure is not defined by FOCUS.

<a name="glossary:detail-representation"><b>Detail Representation</b></a>

The form in which records at a selected [*detail variant*](#glossary:detail-variant) are delivered in relation to the records for the same [*detail scope*](#glossary:detail-scope) when that detail variant is not selected. Examples include additional populated columns on the same records, more detailed records that replace the corresponding records in the same [*dataset artifact*](#glossary:dataset-artifact), and records delivered in a [*companion artifact*](#glossary:companion-artifact).

<a name="glossary:detail-scope"><b>Detail Scope</b></a>

A subset of records in a [*FOCUS dataset*](#glossary:FOCUS-dataset), identified by values of [*FOCUS columns*](#glossary:FOCUS-column) representing [*dimensions*](#glossary:dimension) (e.g., [Service Name](#datamodel.costandusage.servicename), [Resource Type](#datamodel.costandusage.resourcetype)), for which more than one [*detail variant*](#glossary:detail-variant) is offered. A detail scope can correspond to one [*service*](#glossary:service), multiple services, or records identified without reference to a service.

<a name="glossary:detail-variant"><b>Detail Variant</b></a>

An offered set of populated columns, together with the resulting records, for a [*detail scope*](#glossary:detail-scope). The records delivered for a detail scope when no additional detail is selected also constitute a detail variant. Detail variants within the same detail scope can differ in the columns they populate without one being more detailed than another.
```

Fallback, only if TF-2 keeps `data coverage` as a term:

```markdown
<a name="glossary:data-coverage"><b>Data Coverage</b></a>

The records in a [*FOCUS dataset*](#glossary:FOCUS-dataset) to which a [*detail scope*](#glossary:detail-scope) applies, identified by values of [*FOCUS columns*](#glossary:FOCUS-column) representing [*dimensions*](#glossary:dimension).
```

When TF-2 keeps `detail level` and `delivery method`, the entry text still works with the term swapped. The collisions in 1.1 would then remain.

## 2. Normative Content: `specification/attributes/dataset_configuration.md`

### 2.1 Proposed Requirements Section

```markdown
Dataset conforming to DatasetConfiguration attribute MUST adhere to the following requirements:

* *FOCUS dataset* MUST be configurable to include only a user-defined selection of columns.
* *FOCUS dataset* MUST adhere to all column-level specifications defined in the FOCUS schema, regardless of the selected configuration (e.g., column selection or detail variant selection).
* *FOCUS dataset* SHOULD represent records with identical values in all delivered [*FOCUS dataset columns*](#glossary:FOCUS-dataset-column), other than *FOCUS dataset columns* representing summable [*metrics*](#glossary:metric), as a single record.
* *FOCUS dataset* MUST preserve the sum of each *FOCUS dataset column* representing a summable *metric* when records are represented as a single record.
* *FOCUS dataset* MAY offer a default column set.
* *FOCUS dataset* default column set MUST include all applicable [*FOCUS columns*](#glossary:FOCUS-column) when a default column set is offered.
* When a [*detail scope*](#glossary:detail-scope) is offered, *FOCUS dataset* MUST adhere to the following requirements:
  * *FOCUS dataset* MUST be configurable to select each [*detail variant*](#glossary:detail-variant) offered for a *detail scope*.
  * *FOCUS dataset* MUST include only one *detail variant* for each *detail scope*.
  * *FOCUS dataset* MUST include the columns documented for a selected *detail variant*, regardless of the user-defined selection of columns.
  * *FOCUS dataset* MUST be configurable to select one [*detail representation*](#glossary:detail-representation) when more than one *detail representation* is offered for a selected *detail variant*.
  * *FOCUS dataset* *detail scope* documentation MUST adhere to the following requirements:
    * *FOCUS dataset* *detail scope* documentation MUST include the values of *FOCUS columns* representing [*dimensions*](#glossary:dimension) that identify the records in each *detail scope*.
    * *FOCUS dataset* *detail scope* documentation MUST include each *detail variant* offered for each *detail scope*.
    * *FOCUS dataset* *detail scope* documentation MUST include the columns populated for each offered *detail variant*.
    * *FOCUS dataset* *detail scope* documentation MUST include whether each offered *detail variant* contains [*allocated charges*](#glossary:allocated-charge).
    * *FOCUS dataset* *detail scope* documentation MUST include each *detail representation* offered for each *detail variant*.
    * *FOCUS dataset* *detail scope* documentation MUST include the relationship between records delivered at each *detail representation* and other records representing the same underlying data in [*dataset artifacts*](#glossary:dataset-artifact) or [*companion artifacts*](#glossary:companion-artifact) (e.g., replacement, supplement).
    * *FOCUS dataset* *detail scope* documentation MUST include the columns that relate records in a *companion artifact* to the related records in the *dataset artifact* when a *companion artifact* is offered.
    * *FOCUS dataset* *detail scope* documentation MUST be accessible to practitioners.
```

### 2.2 Open Review Threads This Resolves

| Thread | Issue | Resolution in 2.1 |
|--------|-------|-------------------|
| #3866728644, #3867990817 (TF-2 action item, 2026-08-26) | Four normative terms are undefined in shipped content | Glossary entries in 1.2; `data coverage` removed from bullets |
| #3917948166 (@ijurica) | Renames and glossary entries | Adopted, with the additional collisions noted in 1.1 |
| #3866728667 | Documentation block has no applicability gate | Condition grouping bullet `When a detail scope is offered` |
| #3866728652 | `for all detail scopes or for each detail scope` reads both ways | Single configurability bullet; move the whole-dataset vs. per-scope choice to supporting content as a data generator choice (**confirm author intent**) |
| #3866728656 | Detail columns conflict with column selection | `regardless of the user-defined selection of columns` |
| #3866728674 | No accessibility bullet | Added, matching DeliveryHandling |
| #3866728680 | `dimension columns` may exclude custom columns | Merge criterion is "all delivered FOCUS dataset columns other than summable metrics" |
| #3866728683 | Overview row wording | See section 3 |
| #3800388224, #3818143965 (TF-2 action item, 2026-08-19) | Version Introduced | See 2.4 |

### 2.3 Additional Issues

* **A. Custom metrics have the same gap as custom dimensions (lines 29-30).** The glossary defines Metric as "A FOCUS-defined column". Under the current wording, two records that differ only in a custom non-summable column (e.g., `x_UnitRate`) qualify for merging, and summable custom columns get no sum protection. The 2.1 wording covers both.
* **B. Preserving the sum should be MUST, not SHOULD (line 30).** A merge that changes a sum is simply wrong data. The deferred row-aggregation text in supporting content already uses MUST for this ("MUST sum metric column values when rows are aggregated").
* **C. Line 25 treats an attribute as something a detail level "uses".** Datasets and columns conform to attributes; detail levels don't use them. "Contains allocated charges" states the same disclosure as a verifiable fact.
* **D. Record minimization may conflict with the Ledger correction style.** In CorrectionHandling's Ledger style, a reversal record matches the original on every non-additive column. When a correction changes only summable metrics, the reversal and the corrected record have identical non-summable values. If both land in the same dataset artifact, the SHOULD collapses them into a net record, which is effectively Delta style and loses the audit trail. **Ask TF-2** whether an exception clause is needed (e.g., `except when records represent a reversal and its corrected record`) or whether a supporting-content note is enough.
* **E. `less-detailed dataset artifact` (line 28).** A dataset artifact as a whole isn't "less detailed". The 2.1 wording relates records to records.
* **F. Merged PrincipalId undercuts the opt-in.** PrincipalId is required when the operating model includes requester attribution. Line 32 requires a default column set to "include all applicable FOCUS columns". Together, whenever a default column set is offered, high-cardinality actor detail is in it by default. Preventing that was the reason #2415 was a prerequisite for #2360. **TF-2 decision needed.** Options:
  * exempt columns populated only by a non-default detail variant from the default column set requirement
  * tie PrincipalId presence to a selected detail variant
  * accept that PrincipalId is on by default
* **G. Structure and ordering.**
  * The Attribute grouping convention puts documentation requirements last. The 2.1 order is global requirements, then the qualified detail-scope block, then documentation nested inside it.
  * The qualifier `detail scope documentation` (no hyphen) follows the `<Entity reference> <SubQualifier> documentation` form, as in `FOCUS dataset delivery mechanism documentation`.
  * The MUST in the second record-minimization bullet follows its SHOULD because it depends on it. Ordering by keyword can be overridden when order carries meaning.
* **H. Dataset-neutral phrasing.** ContractCommitment and InvoiceDetail also conform to DatasetConfiguration. Replace "usage or charges" with "data" and "cost areas" with "areas of a dataset".

### 2.4 Other Sections in the Attribute File

* **Intro bullet (line 9):**

  ```markdown
  * **Managing Detail**: Include optional detail for areas of a dataset where detailed attribution is needed (e.g., per-user or per-feature costs for a shared service)
  ```

* **Example (lines 46-48).** Replace with text that uses the new terms, shows the default variant, and follows the value convention (double quotes, no backticks):

  ```markdown
  A data generator offers a detail scope for records where Service Name is "Example AI Service". The detail scope documentation identifies two detail variants for that scope: the default variant, which does not populate per-user detail, and a "user" detail variant, which populates the custom column `x_UserId`.

  A practitioner selects the "user" detail variant and the expanded detail representation. In the delivered dataset artifact, each record in the detail scope is replaced by one record per user, and the summable metrics of those records sum to the values of the record they replace. The mechanism used to make these selections is not defined by FOCUS.
  ```

* **Description (line 60).** No change needed.
* **Version Introduced (line 64).** Revert to `1.4`, per the 2026-08-19 TF-2 action item. Record the 1.5 additions in the changelog.

### 2.5 Requirements Model

`specification/requirements_model/releases/1.5/model_rules/attributes/datasetconfiguration.json` still has only rules A-000 through A-004. A-002's `MustSatisfy` text ("regardless of the user's chosen configuration (e.g., column selection)") no longer matches the spec text. `tasks.md` defers the RM update. Confirm with maintainers whether it must land in this PR or can follow before the 1.5 release.

## 3. `specification/attributes/attributes_overview.md`

Accept @Matt-Cowsert's suggestion (#3866728683):

```markdown
| [Dataset Configuration](#attributes.datasetconfiguration) | Defines the rules for customizing a dataset's schema and scoped detail. |
```

## 4. Supporting Content: `supporting_content/attributes/dataset_configuration.md`

Lower priority, since this file isn't part of the standard. Align it after section 2 settles.

* **Terminology.** Rename detail level → detail variant and delivery method → detail representation throughout. Rename the `### Delivery Methods` heading to `### Detail Representations`. Use the values **Inline**, **Expanded** (was Replacement), and **Companion artifact**.
* **Detail Scopes and Data Coverage section.** Retitle it `### Detail Scopes and Detail Variants`. State that the default output is itself a variant.
* **Selection granularity.** Move the "complete dataset or separately for each detail scope" text here as a data generator choice (thread #3866728652).
* **Actor Attribution section.** Reference the merged PrincipalId column, the Principal and Requester glossary terms, and the IncludesRequesterAttribution condition. Record the outcome of 2.3 F.
* **Record Minimization section.** Add the Ledger correction interaction (2.3 D) and custom metric columns (2.3 A).
* **Configuration Metadata example.** Rename `DataCoverage` and `DetailLevel` (e.g., `DetailScope`, `DetailVariant`, `DetailRepresentation`). Update the "What Needs to Be Tracked" row to match.
* **"usage or charges".** Replace with dataset-neutral phrasing.
* **Migrate from `research.md` before the working folder is deleted.**
  * Placement alternatives: standalone attribute vs. DatasetConfiguration. Issue #2415's Definition of Done asked for these to be explored, and @Matt-Cowsert asked on 2026-06-17 for the rationale to be visible.
  * The embedded JSON breakdown option and its tradeoffs.
  * The AWS split cost allocation precedent.
  * Privacy considerations for actor-level identifiers. These no longer appear anywhere in the PR.

## 5. Decisions Needed from TF-2

* Term names: detail variant and detail representation, vs. keeping detail level and delivery method.
* Whether the default output counts as a detail variant (this determines whether the opt-in is guaranteed).
* Whether both selection granularities are required, or either one is acceptable.
* PrincipalId and the default column set (2.3 F).
* Record minimization vs. the Ledger correction style (2.3 D).

## 6. AI Working Files

* **Convention.** `.ai/work/<issue>-<name>/` holds `research.md`, `plan.md`, and `tasks.md`. These are committed during active work. After approval and before merge: migrate valuable content to `supporting_content/`, capture execution notes in the PR or issue, and delete the folder in a final commit. Don't delete before approval.
* **Superseded research.** `research.md` still describes the abandoned granularity-configuration and applicability-filter design, and its "Suggested Normative Direction" contradicts the current text. Reviewers see all 428 lines in the PR diff. Consider adding a one-line superseded note at the top until the folder is deleted.
* **Extra file.** `pr_body.md` isn't one of the three conventional files. Keep it in sync with the PR body or drop it.
* **Guideline inconsistency.** `guidelines/contributors/ai-usage-guidelines.md` lists `.ai/<branch-name>/` in its configuration list but `.ai/work/<issue-number>-<kebab-case-name>/` in its lifecycle section. AGENTS.md uses the latter. This is outside this PR's scope and is a candidate `[Maintenance]` issue.
* **Co-authorship.** When applying reviewer suggestions through an AI assistant, add `Co-authored-by:` trailers for the commenters (AI Usage Guidelines, Review Process item 5). That applies to @Matt-Cowsert and @ijurica here.
* **Thread replies.** When replying through the `pr-update` workflow, use the `🤖 [AI][{ai-platform}]` prefix.
* **This file.** It is working-file content and is deleted with the folder.
