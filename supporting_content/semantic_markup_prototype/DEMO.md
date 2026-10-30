# Semantic Markup Demo Branch

> **Note:** This branch demonstrates feature request [#2779](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2779), which is proposed for FOCUS 1.6. It is for understanding the concept and for local testing. It is not intended to be merged as is.
>
> This branch is also not up to date with `working_draft`. It was cut at commit `038257ac`, and later commits are not included. Two open pull requests are expected to merge soon and are not reflected either:
>
> * [#2710](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2710), the 1.5 Requirements Model update. The REG017 findings below compare against the Requirements Model as it was before this PR, so some of them may disappear when it merges.
> * [#2787](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2787), the file and folder renames. It is expected to wait for 1.6. The REG016 findings below match the names it renames, and the registry builder hard-codes the current paths (e.g., `datasets/data_model.md` and `*_overview.md`).
>
> The branch needs an update once both merge: bring it up to date with `working_draft`, rerun the converter on the converted files, and refresh the counts in this guide.

The branch is cut from `working_draft`. A representative set of specification files is rewritten with semantic tags, and the real build (`make`) resolves those tags into today's links and formatting. Every file that is not converted keeps its hand-written markup, and both kinds coexist in one build.

## Try It

```bash
cd specification
make spec.html
```

```bash
cd supporting_content/semantic_markup_prototype
PYTHON=/path/to/venv/bin/python ./compare_rendered.sh
```

The first command builds the specification with the tags resolved. The second lists every line of the published `spec.md` that differs from the commit where this branch left `working_draft`, word by word, so later changes to `working_draft` do not show up. You can also open any converted file on GitHub to see how the tagged source reads.

## What Changed in the Build

| File | Change |
| :--- | :--- |
| `vendored/MarkdownPP/Modules/Include.py` | Marks each included file's start and end, and drops YAML front matter from included files |
| `specification/Makefile` | Builds and checks the entity registry, assembles `spec.semantic.md`, and resolves it into `spec.md` |
| `specification/markdownlnt.cfg` | Enables the linter's front matter extension |
| `.gitignore` | Ignores the two new build intermediates |

`resolve_semantic.py` converts Markdown to Markdown, so everything after it is unchanged: the linter, Pandoc, wkhtmltopdf, the link tests, and the published `spec.md` artifact all see ordinary Markdown. With no tags in the source, the resolved `spec.md` is byte-identical to the current build.

Build-time checks:

* Definition checks (REG codes) run on every build. Errors fail the build.
* Unknown entities, invalid values, ambiguous ColumnIds, and unknown front matter datasets fail the build with the source file and line number.
* `tests/test_spec_links.py` confirms that every resolved anchor exists in `spec.html`.

`make force=1` downgrades both to warnings.

The source files are expected to contain mistakes, and finding them is one of the reasons for semantic tagging. A finding means two places that should agree do not: an ID and a file name, a heading and a name section, or the specification and the Requirements Model. The checks do not decide which side is wrong. The messages name both sides, and a person resolves each finding on whichever side is in error.

## Converted Files

| File | What it shows |
| :--- | :--- |
| `datasets/cost_and_usage/columns/billedcost.md` | Glossary-heavy prose, self-references, aliases (*covered*, *cash-based*), and the "invoice issuer" decision |
| `datasets/cost_and_usage/columns/chargeclass.md` | An allowed value tag (`["Correction"](#val:ChargeClass)`) and plain words that become glossary terms |
| `datasets/cost_and_usage/columns/resourcetype.md` | Operating model condition and attribute references, and a Content Constraints table |
| `datasets/invoice_detail/columns/billedcost.md` | A ColumnId shared by two datasets, which resolves to the file's own dataset, plus dataset-qualified IDs (`CostAndUsage.BilledCost`) |
| `attributes/numeric_format.md` | Attribute self-references and glossary terms in normative text |
| `operating_model_conditions/includesresourcetypeassignment.md` | An operating model condition referring to itself |
| `appendix/saas_examples/consumption_currency_pricing_model.md` | Non-normative prose with a front matter dataset (`dataset: CostAndUsage`), so shared ColumnIds such as BilledCost need no qualifier |
| `datasets/cost_and_usage/columns/contractapplied.md` | A JSON column: its object (`#obj`), its schema (`#schema`), and the repeated schema link from #2703 |
| `metadata/schema/focus_version.md` | Metadata self-references and a collection reference (`[Schema](#meta)`) |
| `metadata/recency/dataset_instance_id.md` | A Metadata ID defined in three collections, which resolves to the file's own collection |
| `glossary.md` | Front matter declaring two aliases |

Conversion followed the migration steps:

1. `tag_sources.py` made 298 mechanical changes and listed what it could not decide.
2. Judgment calls were made by hand:
   * Self-references by Display Name in prose (e.g., "Billed Cost represents...") are tagged, per the recommendation on #2779.
   * In `chargeclass.md`, "correction" and "charges" are tagged as glossary terms where the same file already treated them as terms.
   * "invoice issuer" in both BilledCost files points to the glossary term, not the InvoiceIssuerName column.
   * The appendix file declares `dataset: CostAndUsage` in front matter, because the example rows are Cost and Usage rows. See Dataset Scope.
   * Ordinary phrases such as "Billing Period" in the appendix are left untagged, because whether plain prose may stay untagged is an open question.
   * In `contractapplied.md`, "Contract Commitment ID" in the property table names a JSON property, not the ContractCommitmentId column, so it stays untagged. Property paths such as `ContractAppliedObject.Elements[\*].ContractCommitmentId` are also left as written.
   * In `metadata/recency/dataset_instance_id.md`, "Dataset Instance" could mean the Dataset Instance metadata collection or the *dataset instance* glossary term, so it stays untagged.

## Dataset Scope

Eleven ColumnIds (e.g., BilledCost, BillingCurrency, InvoiceId) are defined in more than one dataset. This branch decides which dataset an unqualified column reference means as follows:

1. A file under `datasets/<dataset>/` belongs to that dataset.
2. Any other file may declare a dataset in front matter:

   ```yaml
   ---
   dataset: CostAndUsage
   ---
   ```

3. In a file with a dataset, an unqualified column resolves in that dataset only. A column from another dataset needs a qualifier (e.g., `[BilledCost](#col:InvoiceDetail.BilledCost)`), and an unqualified column that is not in the file's dataset fails the build.
4. In a file without a dataset, a column may stay unqualified only when a single dataset defines it.

With the front matter, the appendix reads `[ListCost](#col), [BilledCost](#col), and [ContractedCost](#col)`, and all three resolve to Cost and Usage. Before, only BilledCost carried a qualifier, because it is the only one of the three defined in two datasets. Writing the dataset once per file states the intent directly, and adding a column to another dataset later cannot change or break existing references.

`tag_sources.py` applies the rule as well. After adding the front matter, rerunning it removed the six qualifiers that had become unnecessary. It keeps a qualifier when the visible text is qualified too (e.g., `InvoiceDetail.BilledCost` next to `CostAndUsage.BilledCost`). The rendered output did not change.

This is one answer to the Dataset scope question in #2779, which is still open.

## Schemas, JSON Objects, and Metadata

The first prototype covered columns, allowed values, datasets, attributes, operating model conditions, and glossary terms. This branch adds three more entity types, each recognized from structure the specification already follows:

| Type | Entities | Hand-written links on `working_draft` | Defined by |
| :--- | ---: | ---: | :--- |
| `obj` | 5 | 10 | `### Object ID` and `### Object Display Name` (or `Value`) in a JSON column's file |
| `schema` | 5 | 10 | A level-3 heading in `schemas/schemas.mdpp` |
| `meta` | 32 | 75 | A file under `metadata/` with `## Metadata ID` and `## Metadata Name`; each folder's `*_overview.md` defines its collection |

All 42 resolve to anchors that exist in the assembled specification.

Metadata IDs repeat across collections the way ColumnIds repeat across datasets. DatasetInstanceId is defined in the Dataset Instance, Recency, and Schema collections, and DataGenerator is both a collection and a field inside it. An unqualified metadata reference resolves in the collection that holds the file's own definition, or at the top level in any other file. A qualifier names another collection (e.g., `[DatasetInstanceId](#meta:Schema.DatasetInstanceId)`), and an ambiguous reference fails the build.

**#2703.** Each JSON column links its schema twice: by ID in the conformance bullet and by name in the example pointer (`For the JSON schema, please see [Contract Applied Object Schema](...)`). With both tagged as `#schema`, the first-mention rule renders the pointer without a link, which is the "remove the second link" outcome. Keeping the link instead would be one resolver exception for schema pointers, not an edit in each of the five files. Either way, every JSON column renders the same.

**Definition checks.** REG014 reports a metadata file whose H1 differs from its Metadata Name. On this branch it reports `previouscolumnname.md` and `stringencoding.md`, the two mismatches that #2794 fixes by hand.

**IDs come from ID sections.** Attribute, operating model condition, and dataset files each have an ID section (e.g., `## Attribute ID`). The first prototype derived these IDs from the H1 instead, which gave three wrong IDs: FOCUSColumnHandling (for FocusColumnHandling), JSONObjectFormat (for JsonObjectFormat), and IncludesBillingAndPaymentCurrencyDifferences (for IncludesBillingPaymentCurrencyDifferences). References still resolved, because IDs match without regard to case, but the registry recorded the wrong IDs. The registry now reads the ID sections, like Column ID and Metadata ID.

**File and folder names.** The [Repository Naming Conventions](../../guidelines/contributors/repository-naming-conventions.md) require a file or folder that defines a FOCUS entity to be named after its ID in lowercase, with no separator (e.g., `numericformat.md`). The registry knows which files and folders define entities, so REG016 checks this for every entity type: column, attribute, operating model condition, and metadata files; dataset and metadata collection folders; and schema JSON files. On this branch it reports 40 names, all snake_case dataset folders, attribute files, and metadata files and folders. It reports a warning, not an error, because the renames are planned for 1.6.

## Requirements Model Cross-Check

> **Note:** This section is one possible answer to the open Requirements Model question in #2779 (how the entity registry relates to `requirements_model/`, #2406). The demo is deliberately opinionated: it expects the registry and the Requirements Model to describe the same entities, with the same IDs and names. It does not assume either one is correct.

The Requirements Model rule files are named after the entity they cover, like the specification files: `model_rules/attributes/<id>.json`, `conditions/<id>.json`, and `datasets/<dataset>/<id>.json`, `columns/<id>.json`, and `objects/<id>.json`. Each rule also records the EntityId and EntityName it applies to. REG017 compares the registry with `requirements_model/releases/latest` (1.5) in both directions:

* Every column, dataset, attribute, operating model condition, and JSON object has a rule file.
* Every rule file matches an entity, unless all of its rules have Status "Removed" (history for a removed entity, e.g., ProviderName).
* The EntityId and EntityName in the rules match the specification exactly.

Metadata fields and schemas have no rule files, so they are not checked. On this branch REG017 reports 18 findings:

| Finding | Count | Entities |
| :--- | ---: | :--- |
| Entity with no rule file | 7 | AllocatedServiceName, CredentialId, PrincipalId, RequesterDetails, RequesterDetailsValue, IncludesConsumptionCurrency, IncludesRequesterAttribution |
| Active rule file with no entity | 3 | IncludesListUnitPrices, IncludesNegotiatedPricing, IncludesVirtualCurrency |
| EntityName differs | 8 | Rules "Sku ID", "Sku Meter", "Sku Price Details", and "Sku Price ID" against specification "SKU ..."; rules "Json Object Format", "Date Time Format", "Key Value Format", and "Data Generator Calculated Split Cost Allocation Handling" against specification "JSON Object Format", "Date/Time Format", "Key-Value Format", and "Data Generator-Calculated Split Cost Allocation Handling" |

Each finding is an inconsistency to resolve, not a verdict. For example, the SKU names could be fixed in the rule files or in the specification's Display Names, and a rule file with no entity could mean a missing specification file or a stale rule. Every name difference is in capitalization or punctuation. The findings are reported, not fixed, because the Requirements Model is outside this demo. `build_registry.py --rm-release none` skips the check.

A JSON object is defined in its column's file but is a separate entity. References to it link normally, unlike the column's references to itself.

## Review of Rendered Differences

`compare_rendered.sh` reports 33 changed lines in the published `spec.md`. The build resolves 329 semantic references in total. Each one was reviewed and classified using the change types in the Specification Change Guidelines.

| Classification | Lines | Change | Why |
| :--- | ---: | :--- | :--- |
| No visible change | 12 | Table padding in Content Constraints and Object Schema Structure rows | Cell widths differ; the rendered tables are identical |
| Editorial | 13 | Repeat links removed: *covered*, *covered charge*, *covering charge*, *invoice issuer* (Description), repeated InvoiceDetail column links in Requirements, and *resources* and *services* in the Contract Applied property table | The Editorial Guidelines link an entity only on its first occurrence in a source file |
| Editorial | 2 | *commitments* now linked at its first mention (one of these lines also has a repeat link removed) | It was styled as a glossary term but never linked |
| Editorial | 4 | "correction", "corrections", and "charges" in ChargeClass now italicized as glossary terms | The same file already treated these words as glossary terms elsewhere |
| Editorial (pending #2703) | 1 | The Contract Applied schema pointer renders without a link | The schema is already linked in the conformance bullet; #2703 decides whether the pointer keeps its link |
| Bug fix (needs Working Group confirmation) | 2 | "invoice issuer" in the BilledCost introductions now links the glossary term instead of the InvoiceIssuerName column | The sentence describes the party that issues the invoice, and both files' Descriptions already used the glossary term |
| Regression | 0 | None | |

No normative wording changed. The words of every requirement are the same, and only link styling differs.

One mistake was caught before it reached the output. A hand edit tagged the `# Billed Cost` heading, which is the column's definition, and the REG002 definition check reported it on the next build.

## Known Limitations

* **Requirements Model extraction.** `.github/workflows/rm_extraction.yml` extracts normative statements from the Markdown source. It has not been made tag-aware, so a PR from this branch would show extraction differences.
* **PDF.** The PDF step (wkhtmltopdf) was not run locally. It uses the same resolved `spec.md` and `spec.html`, so it should behave like the HTML build.
* **`build.sh`.** The prototype's `build.sh` compares the samples against the unconverted spec files. On this branch those spec files are already converted, so use `make` and `compare_rendered.sh` instead.
* **Open questions.** The questions in #2779 are still open: dataset scope, plain prose, value links, self-references, context rules, and the Requirements Model.

## Open Question: Context Rules

The resolver decides how a reference is decorated (link, italics, quotes), but it renders the name exactly as the author wrote it. Some editorial rules instead decide which name is written, depending on where the reference appears. For example, #2794 changes headings such as `### Cost Columns: BilledCost vs. EffectiveCost vs. ListCost` to use Display Names, following the heading rules proposed in #2778. On this branch, those edits would still be made by hand.

| Context | Rule | Source | Prototype |
| :--- | :--- | :--- | :--- |
| Headings | Display Name (or Metadata Name), never a link; a JSON property keeps its schema name | #2778 (open) | The converter skips headings. A tagged heading would be linked and counted as a first mention |
| Requirements | Entity ID; an operating model condition used as a condition is written as its lowercase phrase | #2765 (open) | FOCUS003 checks columns only |
| Requirements, other dataset | `Dataset.Column` | #2765 (open) | Accepted |
| Prose outside Requirements | Display Name for conceptual references; an Entity ID is allowed for schema-facing references (SHOULD in the appendix) | Editorial Guidelines, #2514 and #2765 (open) | Not checked |
| Content Constraints tables | Every reference links | Editorial Guidelines | Every table links, which is broader than the rule |
| Entity catalog tables | Row links do not count toward first mention | #2514 and #2765 (open) | Not modeled |
| Allowed Values tables | Values are unquoted | #2514 (open) | Values render as written |
| Glossary | First mention is counted per entry, not per file | Editorial Guidelines | Counted per file |
| Column file whose Display Name is a glossary term | The first mention links to the glossary, never to the column | #2765 (open) | Not modeled |
| Code, SQL, JSON | Entity IDs, no links | Editorial Guidelines | Skipped |

There are two ways to handle the name:

* **A. The author writes the name, and the linter checks it against the context.** The tag identifies the entity, so a rule such as "headings use the Display Name" is a deterministic check against the registry, and the fix can be automated. All of #2794's heading changes would be reported.
* **B. The resolver writes the name.** A tag with no text (e.g., `[](#col:BilledCost)`) renders as the Display Name in headings and the Entity ID in requirements, so a renamed Display Name updates everywhere. It cannot handle plurals, possessives, operating model condition phrases, or the conceptual versus schema-facing judgment.

Recommendation: A. The resolver keeps decoration, and the linter checks the name. The source stays readable, and the cases that B cannot handle are the ones the open guideline PRs spend the most words on. The linter can check headings, Requirements, `Dataset.Column` paths, Allowed Values quoting, and Content Constraints links deterministically. For conceptual versus schema-facing prose, it can only check that the text is one of the entity's names.

Tags inside headings are safe for the build: markdown-pp builds a clean anchor and table of contents entry from the link text. The resolver would need to render heading tags without links and not count them as first mentions. The prototype has not been changed for any of this yet.
