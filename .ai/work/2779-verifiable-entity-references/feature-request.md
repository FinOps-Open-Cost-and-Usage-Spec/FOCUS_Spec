# Feature Request Draft

Title: `[FR] Enable verifiable entity references in specification source`

<!-- Filed as #2779 on 2026-10-17. Synced with the issue body on 2026-10-17.
     Draft for the Feature Request issue template (.github/ISSUE_TEMPLATE/feature-request.yml).
     Only the Requester Information sections are filled in; Maintainer Assessment is left for triage.
     Title: 61 characters. -->

## Requester Information

### Problem Statement

The specification source cannot state which FOCUS entity a piece of text refers to. Contributors mark references to columns, glossary terms, attributes, operating model conditions, datasets, allowed values, JSON objects and schemas, and metadata fields with formatting alone: a hand-typed anchor link on the first mention in a file, italics for glossary terms, and plain text for ColumnIds. Formatting cannot carry that meaning unambiguously. A phrase such as "resource type" might be the ResourceType column or two ordinary words. Italics mark both glossary terms and emphasis. A ColumnId in plain text might be misspelled or stale, and nothing detects it.

As a result, reference consistency can only be checked by manual review, and drift reaches the specification. Two column files on `working_draft` show the typical patterns:

* `billedcost.md` links the words "invoice issuer" to the InvoiceIssuerName column in its first paragraph and to the *invoice issuer* glossary term in its Description. Only the author can say which was meant.
* `billedcost.md` links *covered charge* and *covering charge* two or three times each, despite the first-occurrence rule. *commitments* is italicized as a glossary term but its first mention is never linked.
* `chargeclass.md` links "correction" as a glossary term once and leaves it as plain text in three other places.

The scale makes manual review impractical. Across the 342 Markdown source files under `specification/` (`working_draft` on 2026-10-29), there are about 2,850 hand-typed anchor links to entities (1,280 to columns and datasets, 1,031 to glossary terms, and the rest to attributes, operating model conditions, JSON objects, schemas, and metadata fields), plus about 4,477 more references marked only by formatting or plain text: untagged ColumnIds, italic glossary terms, and Title Case display names. These appear in 333 of the files. These counts come from an automated scan and are approximate. Most of these references follow today's conventions, but none of them can be verified automatically.

Anchors are derived from heading text, so renaming or moving a heading silently breaks links to it (see #2012). The linking conventions themselves are hard to apply consistently. Work such as #2772 and #2703 brought references back in line with the guidelines by hand, one pull request at a time (#2773 and #2789 merged during 1.5), and #2703 documents a case where the Editorial Guidelines and `AGENTS.md` state the linking rule differently.

### Use Case / User Story

**As a** FOCUS contributor or reviewer
**I need** every reference to a FOCUS entity in the specification source to state which entity it refers to
**So that** reference correctness and consistency are verified automatically before merge instead of by line-by-line manual review

### Success Criteria

* Reviewers can determine from the source alone, without interpretation, whether a phrase refers to a column, glossary term, attribute, operating model condition, dataset, allowed value, JSON object, JSON schema, or metadata field, and which one.
* A reference to an entity that does not exist, or to a value that is not among a column's allowed values, is reported before merge, identifying the file and location.
* First-occurrence linking, glossary-term styling, and link targets are applied identically in every file of the published specification, without contributors applying them by hand.
* Changing a linking or formatting convention for a type of entity requires no edits to specification source files.

### Type of Request

* [ ] Standardization
* [ ] Enhancement
* [ ] Net New
* [ ] Enablement/Supporting Content
* [x] Tech Debt - Addressing technical debt or maintenance items

### Organizations Requesting This Feature

* [Backing organization to be confirmed with Matt Cowsert before filing] - Nice to Have - Reduces review burden and prevents reference drift in the specification that implementers rely on

## Optional Sections

### Data Generator Support (Optional)

Not applicable. This request affects how the specification source is authored and built, not FOCUS data.

### Supporting Documentation (Optional)

* Related issues: #2012 (internal link validation in CI), #2772 (align references and links with the contributor guidelines), #2703 (repeat links to JSON schemas), #2758 (Display Name casing lint rule), #2406 (automate Requirements Model extraction and validation)
* Prior art:
  * OpenTelemetry semantic conventions (CNCF, Linux Foundation) keep a machine-readable registry and generate the attribute tables in their Markdown docs with the Weaver tool. A CI check (`make table-check`) fails when the docs drift from the registry. Their prose references are still hand-written links and code spans, which is the part this request addresses: <https://opentelemetry.io/blog/2025/otel-weaver/>
  * Bikeshed, the preprocessor used for W3C, WHATWG, and other specifications, links terms through short semantic markers (e.g., `{{foo}}` for IDL terms, `[[FOO]]` for references): <https://pypi.org/project/bikeshed>
* Prototype: branch [`2779-verifiable-entity-references`](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/tree/2779-verifiable-entity-references/supporting_content/semantic_markup_prototype), in `supporting_content/semantic_markup_prototype/`. Its README covers the syntax, rules, checks, and results. `build.sh` reproduces the sample results.
* Demo: branch [`2779-semantic-markup-demo`](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/tree/2779-semantic-markup-demo), cut from `working_draft`, wires the resolver into the real build (`make`) and converts the whole specification to semantic tags where the tags cover the content (7,851 tags in 333 of 377 files). It is for understanding the concept and for local testing, not for merging. [`DEMO.md`](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/2779-semantic-markup-demo/supporting_content/semantic_markup_prototype/DEMO.md) explains how to build and compare it, and classifies every rendered difference from `working_draft`. [`CONVERSION.md`](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/2779-semantic-markup-demo/supporting_content/semantic_markup_prototype/CONVERSION.md) reports the whole-specification results and 15 numbered questions. It was rebased onto `working_draft` (e0fd5f77) on 2026-10-29. Its `scan_spec.sh` produced the spec-wide counts in the Problem Statement when run on a clean checkout of that commit; on the demo branch itself the counts are lower, because some files are converted.
* Slides: [FOCUS Semantic Markup](https://docs.google.com/presentation/d/1mkH4I4puVd2Bk2DbG2-yZ1ACfFLuf-8l0hT4rWH8l0o/edit), in the FOCUS shared Google Drive, presents the proposal and the results of the whole-specification conversion for the Working Group. It opens for FOCUS Members, Maintainers, and the Steering Committee.

### Proposed Solution / Approach (Optional)

A prototype tested the following approach against the current specification. Maintainers may explore alternatives during discovery.

* **Semantic references written as ordinary Markdown links.** The link target names an entity type instead of a location: `[ResourceType](#col)`, `[resource type](#col:ResourceType)`, `[charges](#term)`, `["Usage"](#val:ChargeCategory)`, `[NumericFormat](#attr)`, `[Includes Tags](#omc)`, `[Cost and Usage](#ds)`, `[ContractAppliedObject](#obj)`, `[ContractAppliedObjectSchema](#schema)`, `[FocusVersion](#meta)`. This extends the pattern the glossary links already use (`#glossary:charge`). It renders legibly on GitHub, parses as a normal link in Pandoc's `gfm` reader, and passes the existing pymarkdownlnt configuration unchanged. Any other link passes through untouched, so legacy and semantic markup can coexist.
* **A generated entity registry.** Entities are read from the files that already define them: column files (Column ID, Display Name, dataset, Allowed Values), `glossary.md`, attribute files, operating model condition files, dataset files, the Object ID and Object Display Name sections of JSON columns, `schemas/schemas.mdpp`, and metadata files (Metadata ID, Metadata Name). Anchors are computed with the same algorithm markdown-pp uses. Nothing is maintained by hand. On `working_draft` as of 2026-10-29, the registry holds 506 entities: 150 columns, 177 allowed values, 89 glossary terms, 26 operating model conditions, 15 attributes, 5 datasets, and 44 JSON objects, schemas, and metadata fields. Metadata IDs repeat across collections (e.g., DatasetInstanceId in three), so they resolve in the file's own collection, the way columns resolve in the file's dataset. #2703 removed the repeated schema link from five JSON columns by hand (#2789). With schemas in the registry, the first-mention rule gives the same result with no file edits, for every current and future JSON column.
* **A resolver.** A panflute filter runs beside the existing relative-links filter. It applies today's conventions in one place: link the first mention per source file, never self-link, italicize glossary terms, always link in Content Constraints tables except glossary terms, count each glossary entry as its own scope for first mentions, and link either to spec anchors or to source `.md` files for per-file previews. markdown-pp would add one line that marks each `!INCLUDE` file boundary.
* **Definitions stay as they are.** The registry recognizes each definition by the structure the specification already follows, and it checks that structure on every build (e.g., a missing Column ID, an H1 that differs from the Display Name, or an Allowed Values table without a value column). All 127 column files on `working_draft` pass. Facts the structure cannot hold, such as aliases, go in optional front matter on the defining file. Using front matter in the real build would need markdown-pp to strip it. A comment on this issue gives the details.
* **Checks enabled by the tags.** Errors cover unknown entities, values not in a column's allowed values, and ColumnIds that exist in more than one dataset without a qualifier. Warnings cover a Display Name used in a Requirements section, untagged ColumnIds and display names, and hard-coded entity links, each with the exact suggested rewrite.
* **Prototype results.** Against a registry built from the specification as it is, the original `billedcost.md` and `chargeclass.md` produced 51 findings. The prototype's alias demo adds one more (an italic *covered* recognized as the *covered charge* glossary term), for 52. After conversion the files produced none, and every difference between the built output and the hand-written originals was a consistency fix.
* **Whole-specification conversion.** A script converts every file the build includes, and running it again on converted files changes nothing. On `working_draft` at e0fd5f77 it made 7,851 tags in 333 of 377 files. The build resolves every tag with 0 errors and 11 warnings, all 191 tests pass, and no visible words change. 816 lines of the published `spec.md` differ: 445 links added at a first mention that was plain text, 213 repeat links removed, 2 links retargeted (the "invoice issuer" cases), 18 italics, and 297 table-padding changes. The checks also found inconsistencies in the source, for example a link whose text names ContractCommitmentPeriodStart but whose target is ContractPeriodStart, and 45 differences between the specification and the Requirements Model. The converter left 450 items, 272 hand-written links, and 340 table rows for a decision.
* **Rules review.** A review of the tagging rules after the full conversion found eleven places where they are inconsistent, implicit, or depend on the converter ([full table](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/2779-semantic-markup-demo/supporting_content/semantic_markup_prototype/CONVERSION.md#review-of-the-rules)). The four high-priority changes, not yet implemented:
  * Tables outside Content Constraints follow one rule: a reference links at its first mention within the table, and tables do not affect first mentions in prose.
  * Self-links are decided by anchor (no link to the section a reference sits in, or its parents), not by file, which removes the special cases for JSON objects and DataGenerator.
  * Tags in headings render as plain text and do not count as first mentions.
  * Emphasis inside a tag is reported as a warning rather than dropped silently.
* **Phased migration that never breaks the build.**
  1. The resolver runs in warn-only mode.
  2. A script applies the suggested rewrites, one folder per PR, with each PR showing the difference in the built specification.
  3. Contributors triage only the ambiguous cases.
  4. Strict mode makes errors fail CI.

  The Billing Period dataset is a suggested pilot because of its small size.

Open questions for discovery:

* **Dataset scope.** Sixteen ColumnIds (e.g., BilledCost, BillingCurrency, InvoiceId) exist in more than one dataset. Files under `datasets/<dataset>/` resolve unqualified columns to their own dataset. Which dataset should an unqualified column in an appendix, attribute, or other shared file resolve to? With qualifiers alone, a shared file qualifies only the shared ColumnIds, so one sentence can read `[ListCost](#col), [BilledCost](#col:CostAndUsage.BilledCost)`: both columns mean Cost and Usage, but only the one that happens to exist in two datasets says so. A column added to another dataset later would also break every unqualified reference to it in shared files. Options:
  * Qualify only ambiguous columns (the original prototype behavior, and the rule proposed in #2765).
  * Default to Cost and Usage project-wide. Simple and usually right, but a reference meant for another dataset would silently link to Cost and Usage.
  * Declare a default per file in front matter (`dataset: CostAndUsage`). Unqualified columns resolve in that dataset only, other datasets need a qualifier, and a column missing from the declared dataset fails the build.
  * Always qualify columns outside dataset files. Explicit, but verbose.

  Recommendation: a per-file default in front matter. It states the intent once per file, and adding a column to another dataset later cannot change or break existing references. The demo branch applies it to its appendix example.
* **Plain prose.** May an ordinary phrase that matches an entity name stay untagged? The conversion tags a multi-word Display Name that names one entity unambiguously and leaves every other plain match untagged (450 items).
* **Self-references.** Should a file tag references to the entity it defines (e.g., `[BilledCost](#col)` inside `billedcost.md`)? Self-references render without a link either way. Recommendation: tag them. Tagging lets the checks identify every mention of an entity unambiguously, so they can verify casing and confirm that Requirements use the ColumnId. It also keeps a single rule: every entity reference is tagged. A column file typically mentions its own column 10 to 20 times, but that cost is small when tags are applied by tools or AI agents. The definitions themselves (the H1 and the Column ID and Display Name sections) stay untagged. The prototype currently exempts self-references from the untagged-reference checks.
* **Context rules.** Some editorial rules decide which name is written, not how it is decorated. For example, #2794 (merged) changed headings from ColumnIds to Display Names, following the heading rules proposed in #2778 (still open). Other rules of this kind, in current guidelines or open PRs (#2514, #2765): Requirements use Entity IDs, but an operating model condition used as a condition is written as its lowercase phrase; prose uses Display Names for conceptual references and may use Entity IDs for schema-facing ones; Allowed Values tables list values without quotes. Related linking rules also depend on context: Content Constraints tables link every reference, entity catalog table rows do not count toward first mention, and the glossary counts first mention per entry. Should the author write the name and the checks verify it against the context, or should the build write the name from a tag with no text (e.g., `[](#col:BilledCost)`)? Recommendation: the author writes the name, and the checks verify it. The tag identifies the entity, so rules such as "headings use the Display Name" become deterministic checks, and the fix can be automated. A build-written name cannot handle plurals, possessives, operating model condition phrases, or the conceptual versus schema-facing judgment. Tags inside headings work with the current build, but they should render without a link and not count as a first mention. The prototype does not yet apply these rules.
* **Values.** Should allowed values link to their column's Allowed Values table?
* **Line numbers.** Should check messages carry line numbers before strict mode is enabled?

The whole-specification conversion on the demo branch raised more questions. These are the main ones; [`CONVERSION.md`]({BASE}/CONVERSION.md#questions) has all 15 with counts:

* **Tables outside Content Constraints.** 231 hand-written links and 340 rows with references in 37 files were left as written. Catalog tables (e.g., the Columns table in `dataset.md`) link every row, and example data tables do not. How does an author mark a reference that always links, and do links in these tables count as first mentions? The demo says they do not, following the entity catalog table rule proposed in #2514 and #2765.
* **Names that are also glossary terms.** 208 Display Name occurrences were left untagged because the same words are a glossary term (e.g., SKU Price 101, Billing Period 21, List Unit Price 19). Should the converter apply the capitalization rule proposed in #2765?
* **Files that mix datasets.** 190 mentions of shared columns in 11 files cannot be resolved to one dataset, 111 of them in one supported features page. Separately, 57 files received an inferred `dataset:` default that an author has not confirmed.
* **Links to sub-sections.** 32 links point at sub-sections of an entity (e.g., the correction styles in `correction_handling.md`, or "Schema Structure" in a JSON column), not at an entity. Should sub-sections become taggable?
* **The data generator role.** "data generator" is written as an italic link nine times, but the glossary has no entry and the only target is the Data Generator metadata section. Should the glossary define it?
* **Reviewing and merging the conversion.** It changes 326 files, adds 445 links, and removes 213. Can these be reviewed in bulk as editorial changes? Should the specification be converted at once or area by area, given that every open pull request that edits specification content would conflict?

### Additional Context (Optional)

* **Current workaround.** Manual review during PRs and consistency review cycles, plus periodic alignment work items such as #2772.
* **Relationship to #2012.** Entity references resolved against a registry would be checked by construction, which covers much of what #2012 asks for. Links that are not entity references would still need a separate link check.
* **Relationship to #2406.** The entity registry and the Requirements Model both describe specification entities. Discovery should decide whether one is derived from the other, to avoid a third source of truth.
* **Urgency.** There is no external deadline. The value grows with every release, because each new column, value, and glossary term adds references that today can only be checked by hand.
