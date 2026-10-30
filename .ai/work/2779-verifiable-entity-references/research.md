# Research: Verifiable Entity References (#2779)

Issue: [#2779](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2779), "[FR] Enable verifiable entity references in specification source". The prototype is in [`supporting_content/semantic_markup_prototype/`](../../../supporting_content/semantic_markup_prototype/README.md).

## Requirements from the Issue

* Reviewers can tell from the source alone which entity a phrase refers to, if any.
* References to entities that do not exist, and values not among a column's allowed values, are reported before merge.
* First-occurrence linking, glossary styling, and link targets are applied identically in every file, without contributors applying them by hand.
* Changing a linking or formatting convention requires no edits to specification source files.

## Current Build Pipeline

* markdown-pp assembles `spec.md` from `!INCLUDE` directives. Its TableOfContents module (`vendored/MarkdownPP/Modules/TableOfContents.py`) builds anchors such as `#datamodel.costandusage.resourceid` from the heading path, so anchors change when headings change.
* Pandoc (`-f gfm`) renders HTML with one panflute filter (`pandoc-project-relative-links.py`). wkhtmltopdf renders the PDF.
* File boundaries are lost after markdown-pp, so a per-file rule such as first-occurrence linking needs a boundary marker from the Include module.

## Spec-Wide Scan

`scan_spec.sh` on a clean checkout of `working_draft` reports:

| Measure | 2026-10-17 | 2026-10-29 (e0fd5f77) |
| :--- | ---: | ---: |
| Markdown source files scanned | 308 | 342 |
| Files with at least one finding | 278 | 333 |
| Hard-coded entity links | 2,313 | 2,850 |
| ... to columns and datasets | 1,040 | 1,280 |
| ... to glossary terms | 885 | 1,031 |
| Formatting-only references | 3,494 | 4,477 |
| ... untagged ColumnIds | 1,684 | 1,813 |
| ... italic glossary terms | 1,387 | 1,755 |
| ... untagged display names | 423 | 909 |

Two things changed between the scans: `working_draft` grew (the SKU Price dataset and its supported features added 34 files), and the scanner now also counts JSON objects, schemas, and metadata fields. Running the original scanner on both dates separates them. On 2026-10-17 it finds 308 files, 2,319 links, and 3,495 formatting-only references. On 2026-10-29 it finds 342 files, 2,756 links, and 4,396 formatting-only references, so growth in the specification accounts for most of the increase and the wider scanner for about 94 links and 81 display names. The 2026-10-29 column uses the current scanner, because the proposal covers all entity types.

Most of these follow today's conventions. They are counted because none of them can be verified automatically.

## Definition Checks

`build_registry.py` on `working_draft`:

* All 127 column files pass the structural checks (Column ID, Display Name, H1, file name, Allowed Values table, Content Constraints Dataset row).
* Four glossary keys do not follow the slug pattern: `chargeperiod`, `exclusiveendbound`, `inclusivestartbound`, and `pascalcase`.
* Six names belong to two types of entity, for example "billing currency" (column and glossary term), "list unit price" (column and glossary term), and "billing period" (dataset and glossary term).

## Syntax Options Considered

| Option | Raw on GitHub | Pandoc `gfm` build | pymarkdownlnt | New tooling |
| :--- | :--- | :--- | :--- | :--- |
| Link form, `[ResourceType](#col)` | Readable, shown as a link | Normal link node | Passes | None |
| Custom tags, `<column>...</column>` | Readable, tags hidden | Unpaired raw HTML pieces | Inline-HTML rule fires | None |
| Pandoc spans, `[ResourceType]{.col}` | `{.col}` shown literally | Needs a different reader | Unknown syntax | None |
| Remark plugins | Depends on syntax | Second parser beside Pandoc | Depends on syntax | Node.js |

The link form was chosen. It extends the existing `#glossary:` pattern.

## Prior Art

* **OpenTelemetry semantic conventions** (CNCF, Linux Foundation). A YAML registry in `model/` is the source of truth. Weaver generates tables between `<!-- semconv ... -->` markers, and `make table-check` fails CI when they drift. Prose references are not tagged: in a shallow clone (2026-10-15), about 644 code spans in 195 hand-written docs match attribute IDs, alongside hand-typed links such as ``[`http.route`](/docs/registry/attributes/http.md)``. The link check catches only broken URLs. These counts come from a rough regex scan.
* **Bikeshed** (W3C, WHATWG, C++ committee). Authors write semantic shorthands (e.g., `{{foo}}` for IDL terms, `[[FOO]]` for references) and the preprocessor links terms to their definitions, including across specifications.
* **Fit for FOCUS.** OpenTelemetry's approach covers generated metadata tables, which suits a later phase for Content Constraints and Allowed Values. It does not address references in prose, which is the core of #2779. A YAML registry would also add a third source of truth beside the Markdown and `requirements_model/`.

## Whole-Specification Conversion

On 2026-10-30 the demo branch converted every file the build includes (`convert_all.sh`), on `working_draft` at e0fd5f77: 7,851 tags in 333 of 377 files, 0 build errors, 191 tests passing, and no visible words changed. 816 lines of the published `spec.md` differ (445 links added, 213 removed, 2 retargeted, 18 italics, 297 table padding). Getting there took several fixes found only at full scale: a definition section with a `<!--SkipTOC-->` suffix was tagged, a stray `*` was dropped from link text, an Allowed Values header containing a link broke the registry, dataset inference changed on a second run, and "tables always link" added 953 links outside Content Constraints. `CONVERSION.md` on the demo branch has the results and 15 numbered questions; the issue lists the six main ones.

## Semantic Review

On 2026-10-30 a semantic review followed the mechanical conversion on the demo branch, as its own commit so it can be compared and rolled back separately. A commit before it (mechanical) also tagged plain dataset IDs, which the converter had missed (276 tags). The review grouped the 8,127 tags into 685 patterns of kind, text, and entity, set aside the 2,491 tags that cannot be wrong (an ID only one dataset defines), checked the other 550 patterns against their contexts, and decided the converter's 435 open items. Result: 7 tags corrected, 377 added, 60 left plain with a reason, 8,504 tags in all, and no visible words changed. `SEMANTIC_REVIEW.md`, `semantic-review-changes.tsv`, and `semantic_review.py` on the demo branch hold the details. Findings a tag cannot fix: the data generator role has no glossary entry (linked to the metadata section 16 times), Host Provider likewise, "AllocationMethod" in a requirement is not an entity ID, and the registry derives a schema ID with the wrong casing.

## Rules Review

After the full conversion, the tagging rules were reviewed (`CONVERSION.md`, Review of the Rules, on the demo branch). Eleven findings, four high priority: one rule for tables outside Content Constraints, anchor-based self-links, plain rendering of tags in headings, and a warning instead of silently dropping emphasis inside a tag. Medium: the Requirements check keyed to requirement statements, a stated plain-prose rule, dataset scope per section, shortest value tags, and the functional-link exemption. Low: the glossary anchor dependency and plurals of Display Names.

## Open Questions

* **Entity coverage.** The first prototype missed three entity types: JSON objects (5, defined by Object ID and Object Display Name sections in column files), JSON schemas (5, headings in `schemas/schemas.mdpp`), and metadata fields and collections (32, Metadata ID and Metadata Name sections). `working_draft` has 10, 10, and 75 hand-written links to them. #2703 (the repeated schema link in each JSON column) prompted the check. The demo branch adds `#obj`, `#schema`, and `#meta`. Metadata IDs repeat across collections (DatasetInstanceId in three; DataGenerator is both a collection and a field), so references resolve in the file's own collection. REG014 (H1 differs from Metadata Name) reports the two mismatches #2794 fixes by hand. Appendix and supported features links point to sections, not entities, and stay ordinary links.
* **Dataset scope.** Sixteen ColumnIds exist in more than one dataset. Appendix and attribute files need a default dataset or explicit qualifiers. Options: qualify only ambiguous columns (as #2765 proposes), a project-wide Cost and Usage default, a per-file default in front matter, or always qualify. Recommendation: a per-file default (`dataset: CostAndUsage`), with unqualified columns resolving in that dataset only, so a column added to another dataset later cannot change or break references. The demo branch implements it (`resolve_semantic.py`, `tag_sources.py`, REG012, FOCUS010) and applies it to `consumption_currency_pricing_model.md`.
* **Plain prose.** May an ordinary phrase that matches an entity name stay untagged?
* **Self-references.** Should a file tag references to the entity it defines? Recommendation (David Moreau): tag them. Tagging lets the checks identify every mention unambiguously (casing, ColumnId in Requirements) and keeps one rule for all references. The 10 to 20 extra tags per column file are cheap when tools or AI agents apply them. Definitions (H1, Column ID, Display Name) stay untagged. The prototype has not been changed yet: it still exempts self-references from FOCUS004 and FOCUS006, and it does not check tag casing.
* **Context rules.** Some editorial rules choose which name is written, not how it is decorated. For example, #2794 changes headings to Display Names under the rules proposed in #2778. Other rules: Requirements use Entity IDs, but an operating model condition used as a condition is its lowercase phrase (#2765); prose uses Display Names for conceptual references and may use Entity IDs for schema-facing ones (#2514, #2765); Content Constraints tables link every reference; entity catalog table rows do not count toward first mention; Allowed Values tables are unquoted (#2514); the glossary counts first mention per entry; a column whose Display Name is a glossary term links the glossary. The options are (A) the author writes the name and the linter checks it against the context, or (B) the resolver writes the name from an empty tag (e.g., `[](#col:BilledCost)`). Recommendation: A, because B cannot handle plurals, possessives, operating model condition phrases, or the conceptual versus schema-facing judgment. The linter can check headings, Requirements, `Dataset.Column` paths, Allowed Values quoting, and Content Constraints links deterministically. Tags in headings are safe for markdown-pp's anchors and table of contents, but the resolver would need to render them without links and not count them as first mentions. Prototype gaps: links in every table, first mention per glossary file, and links in tagged headings. The full table is in `DEMO.md` on the `2779-semantic-markup-demo` branch.
* **Value links.** Should allowed values link to the column's Allowed Values table?
* **Line numbers.** Lint messages should carry line numbers before strict mode.
* **Front matter.** markdown-pp would need to strip front matter, which is needed for aliases.
* **Requirements Model.** How should the entity registry relate to `requirements_model/` (#2406)?
