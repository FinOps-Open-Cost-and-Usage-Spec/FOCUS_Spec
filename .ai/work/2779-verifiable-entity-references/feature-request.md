# Feature Request Draft

Title: `[FR] Enable verifiable entity references in specification source`

<!-- Filed as #2779 on 2026-10-17. Later edits on GitHub are not reflected here.
     Draft for the Feature Request issue template (.github/ISSUE_TEMPLATE/feature-request.yml).
     Only the Requester Information sections are filled in; Maintainer Assessment is left for triage.
     Title: 61 characters. -->

## Requester Information

### Problem Statement

The specification source cannot state which FOCUS entity a piece of text refers to. Contributors mark references to columns, glossary terms, attributes, operating model conditions, datasets, and allowed values with formatting alone: a hand-typed anchor link on the first mention in a file, italics for glossary terms, and plain text for ColumnIds. Formatting cannot carry that meaning unambiguously. A phrase such as "resource type" might be the ResourceType column or two ordinary words. Italics mark both glossary terms and emphasis. A ColumnId in plain text might be misspelled or stale, and nothing detects it.

As a result, reference consistency can only be checked by manual review, and drift reaches the specification. Two column files on `working_draft` show the typical patterns:

* `billedcost.md` links the words "invoice issuer" to the InvoiceIssuerName column in its first paragraph and to the *invoice issuer* glossary term in its Description. Only the author can say which was meant.
* `billedcost.md` links *covered charge* and *covering charge* two or three times each, despite the first-occurrence rule. *commitments* is italicized as a glossary term but its first mention is never linked.
* `chargeclass.md` links "correction" as a glossary term once and leaves it as plain text in three other places.

The scale makes manual review impractical. Across the 308 Markdown source files under `specification/`, there are about 2,313 hand-typed anchor links to entities, plus about 3,494 more references marked only by formatting or plain text: untagged ColumnIds, italic glossary terms, and Title Case display names. These appear in 278 of the files. These counts come from an automated scan and are approximate. Most of these references follow today's conventions, but none of them can be verified automatically.

Anchors are derived from heading text, so renaming or moving a heading silently breaks links to it (see #2012). The linking conventions themselves are hard to apply consistently. Open work such as #2772 and #2703 exists to bring references back in line with the guidelines, and #2703 documents a case where the Editorial Guidelines and `AGENTS.md` state the linking rule differently.

### Use Case / User Story

**As a** FOCUS contributor or reviewer
**I need** every reference to a FOCUS entity in the specification source to state which entity it refers to
**So that** reference correctness and consistency are verified automatically before merge instead of by line-by-line manual review

### Success Criteria

* Reviewers can determine from the source alone, without interpretation, whether a phrase refers to a column, glossary term, attribute, operating model condition, dataset, or allowed value, and which one.
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
* A working prototype and a presentation are available. The presentation has been shared with Matt Cowsert as a PDF. [Decide with Matt whether to attach it here.]

### Proposed Solution / Approach (Optional)

A prototype tested the following approach against the current specification. Maintainers may explore alternatives during discovery.

* **Semantic references written as ordinary Markdown links.** The link target names an entity type instead of a location: `[ResourceType](#col)`, `[resource type](#col:ResourceType)`, `[charges](#term)`, `["Usage"](#val:ChargeCategory)`, `[NumericFormat](#attr)`, `[Includes Tags](#omc)`, `[Cost and Usage](#ds)`. This extends the pattern the glossary links already use (`#glossary:charge`). It renders legibly on GitHub, parses as a normal link in Pandoc's `gfm` reader, and passes the existing pymarkdownlnt configuration unchanged. Any other link passes through untouched, so legacy and semantic markup can coexist.
* **A generated entity registry.** Entities are read from the files that already define them: column files (Column ID, Display Name, dataset, Allowed Values), `glossary.md`, attribute files, operating model condition files, and dataset files. Anchors are computed with the same algorithm markdown-pp uses. Nothing is maintained by hand. The prototype registry holds 424 entities.
* **A resolver.** A panflute filter runs beside the existing relative-links filter. It applies today's conventions in one place: link the first mention per source file, never self-link, italicize glossary terms, always link in tables except glossary terms, and link either to spec anchors or to source `.md` files for per-file previews. markdown-pp would add one line that marks each `!INCLUDE` file boundary.
* **Checks enabled by the tags.** Errors cover unknown entities, values not in a column's allowed values, and ColumnIds that exist in more than one dataset without a qualifier. Warnings cover a Display Name used in a Requirements section, untagged ColumnIds and display names, and hard-coded entity links, each with the exact suggested rewrite.
* **Prototype results.** The original `billedcost.md` and `chargeclass.md` produced 51 findings. After conversion they produced none, and every difference between the built output and the hand-written originals was a consistency fix.
* **Phased migration that never breaks the build.**
  1. The resolver runs in warn-only mode.
  2. A script applies the suggested rewrites, one folder per PR, with each PR showing the difference in the built specification.
  3. Contributors triage only the ambiguous cases.
  4. Strict mode makes errors fail CI.

  The Billing Period dataset is a suggested pilot because of its small size.

Open questions for discovery:

* **Dataset scope.** Eleven ColumnIds (e.g., BilledCost, BillingCurrency, InvoiceId) exist in more than one dataset. Which dataset should references in appendix and attribute files resolve to by default?
* **Plain prose.** May an ordinary phrase that matches an entity name stay untagged?
* **Values.** Should allowed values link to their column's Allowed Values table?
* **Line numbers.** Should check messages carry line numbers before strict mode is enabled?

### Additional Context (Optional)

* **Current workaround.** Manual review during PRs and consistency review cycles, plus periodic alignment work items such as #2772.
* **Relationship to #2012.** Entity references resolved against a registry would be checked by construction, which covers much of what #2012 asks for. Links that are not entity references would still need a separate link check.
* **Relationship to #2406.** The entity registry and the Requirements Model both describe specification entities. Discovery should decide whether one is derived from the other, to avoid a third source of truth.
* **Urgency.** There is no external deadline. The value grows with every release, because each new column, value, and glossary term adds references that today can only be checked by hand.
