# Research

## Issue

Issue 2240, "Use backticks instead of double-quotes for all string column values," defines completion as replacing all uses of double quotes with backticks for string column values.

## Scope

* Inventory every Markdown path tracked by the pre-change base commit, including specification, supporting content, changelog, contributor guidance, and AI workflow documentation.
* Update string data values presented in prose and Markdown table cells.
* Update repository authoring guidance and examples that prescribe or demonstrate this convention.
* Preserve double quotes required by JSON and other code syntax, including fenced, inline, and raw HTML code.
* Preserve double quotes used for property names, ordinary quotations, HTML attributes, MarkdownPP include syntax, non-string literals, and format notation.

## Interpretation

The formatting applies to string data values referenced in prose, not column or property names. For example, `ChargeCategory` is a column name and `Usage` is a string column value. The implementation uses the broader editorial interpretation established during review: metadata values, nested object values, dataset-instance names, historical changelog values, and illustrative invoice values are included when they represent data. Code and JSON syntax, identifiers, non-string literals, format notation, and ordinary quotations remain excluded.

## Validation Method

The changes were generated from a non-mutating candidate inventory rather than a global replacement. All scans use the fixed pre-change commit `02e7dfbcc347edaade318eb06e111d18da3c4620` and the Markdown paths tracked at that commit.

* Actual entity IDs are discovered from Column ID, Metadata ID, Dataset ID, and Property ID sections.
* Fenced code, inline code, raw HTML code, JSON syntax, property keys, booleans, and ordinary quotations are identified separately.
* High-confidence classifications require an entity/value relationship, an explicit allowed-value context, an entity designation, or a string-example table.
* Classifications are review aids only. Each of the 960 baseline occurrences has a per-occurrence apply or skip decision and rationale in `repository_review_manifest.tsv`.
* The applied manifest contains 520 replacements across 81 tracked Markdown files, all corresponding to reviewed scanner candidates.
* The residual manifest contains explicit skip decisions for all 416 double-quoted prose occurrences retained after the rewrite.
* A base-to-worktree validator confirms that every non-guidance Markdown change is exactly represented by the applied manifest, including changes already staged or committed.

The retained records include JSON object keys and values, property names, the `x_` custom-key prefix, Boolean literals, code-like requirements-model property assignments such as `Function="Nullability"`, format and unit notation, quoted requirement sentences, comparison terminology, and ordinary narrative quotations. The classifier deliberately has no global value blacklist: exclusions are recorded per occurrence so a token can be treated differently in a genuine data-value context.

The illustrative invoice line-item labels `Enterprise Support` and `Storage` were explicitly treated as values and converted to backticks for semantic and reading clarity. The structured duration example `[Numeric Value] [Unit]` was also converted because it represents the format of a string column value, although it is format notation rather than a literal allowed value.

## Human Scope Decisions

* Metadata string examples such as `FOCUS Cost and Usage` and `FOCUS Contract` use backticks because they are example values of a string property.
* Historical design values use backticks because this makes proposed and previously considered column values clear in Markdown.
* The nested wildcard is retained as the quoted code literal `"*"`, including in the reserved-value table, because the surrounding object and array examples require quoted string syntax.
* The `"x_"` custom-column prefix remains quoted because it is prefix notation rather than a string data value.
* Code-like property assignments such as `Function="Nullability"` retain their double quotes as required string syntax.

## Audit Corrections

Three independent reviews materially improved the workflow:

* A Markdown-link/JSON defect was corrected. A closed Markdown link followed by a colon is no longer misclassified as a JSON array; the defect had hidden clear values from the first completeness scan.
* Scope and reproduction were expanded from current, unstaged specification files to all tracked Markdown from a fixed base commit. This includes changelog and supporting-content values and keeps validation valid after staging or committing.
* Inline-code spans are now masked without changing character positions before quotation parsing. This prevents closing and opening quotation marks on opposite sides of inline code from being paired into artificial occurrences.
* Requirements-model values missed during guidance review were converted, patch generation now reads from the fixed base revision, and repository-wide lint evidence compares current diagnostics with the base rather than treating legacy diagnostics as new failures.

Regression tests cover Markdown links followed by colons, JSON objects and arrays, multiple values on one line, quotations containing inline code, inline and fenced code, single-line and multiline raw HTML code, CRLF input, deterministic entity ordering, and worktree symlinks.

## Editorial Decision

The illustrative requirements around line 320 of `guidelines/contributors/normative-requirements-guidelines.md` retain quoted values such as `"X"`, `"Tax"`, and `"Adjustment"`. Human review confirmed that these should remain whole-requirement code examples. Each complete requirement is enclosed in an inline code span, so its internal double quotes are intentional code syntax and fall outside the prose-formatting rule.
