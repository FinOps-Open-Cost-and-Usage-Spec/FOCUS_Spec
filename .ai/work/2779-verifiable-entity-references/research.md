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

`scan_spec.sh` on `working_draft` (2026-10-17) reports:

| Measure | Count |
| :--- | ---: |
| Markdown source files scanned | 308 |
| Files with at least one finding | 278 |
| Hard-coded entity links | 2,313 |
| ... to columns and datasets | 1,040 |
| ... to glossary terms | 885 |
| Formatting-only references | 3,494 |
| ... untagged ColumnIds | 1,684 |
| ... italic glossary terms | 1,387 |
| ... untagged display names | 423 |

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

## Open Questions

* **Dataset scope.** Eleven ColumnIds exist in more than one dataset. Appendix and attribute files need a default dataset or explicit qualifiers.
* **Plain prose.** May an ordinary phrase that matches an entity name stay untagged?
* **Self-references.** Should a file tag references to the entity it defines? Recommendation (David Moreau): tag them. Tagging lets the checks identify every mention unambiguously (casing, ColumnId in Requirements) and keeps one rule for all references. The 10 to 20 extra tags per column file are cheap when tools or AI agents apply them. Definitions (H1, Column ID, Display Name) stay untagged. The prototype has not been changed yet: it still exempts self-references from FOCUS004 and FOCUS006, and it does not check tag casing.
* **Context rules.** Some editorial rules choose which name is written, not how it is decorated. For example, #2794 changes headings to Display Names under the rules proposed in #2778. Other rules: Requirements use Entity IDs, but an operating model condition used as a condition is its lowercase phrase (#2765); prose uses Display Names for conceptual references and may use Entity IDs for schema-facing ones (#2514, #2765); Content Constraints tables link every reference; entity catalog table rows do not count toward first mention; Allowed Values tables are unquoted (#2514); the glossary counts first mention per entry; a column whose Display Name is a glossary term links the glossary. The options are (A) the author writes the name and the linter checks it against the context, or (B) the resolver writes the name from an empty tag (e.g., `[](#col:BilledCost)`). Recommendation: A, because B cannot handle plurals, possessives, operating model condition phrases, or the conceptual versus schema-facing judgment. The linter can check headings, Requirements, `Dataset.Column` paths, Allowed Values quoting, and Content Constraints links deterministically. Tags in headings are safe for markdown-pp's anchors and table of contents, but the resolver would need to render them without links and not count them as first mentions. Prototype gaps: links in every table, first mention per glossary file, and links in tagged headings. The full table is in `DEMO.md` on the `2779-semantic-markup-demo` branch.
* **Value links.** Should allowed values link to the column's Allowed Values table?
* **Line numbers.** Lint messages should carry line numbers before strict mode.
* **Front matter.** markdown-pp would need to strip front matter, which is needed for aliases.
* **Requirements Model.** How should the entity registry relate to `requirements_model/` (#2406)?
