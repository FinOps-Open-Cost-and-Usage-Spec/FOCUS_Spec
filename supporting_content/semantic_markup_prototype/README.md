# Semantic Markup Prototype

> **Note:** This is a research prototype. On branch `2779-semantic-markup-demo` it is wired into the specification build with a sample of converted files; see [DEMO.md](DEMO.md).

This prototype tests whether FOCUS source files can mark *what* a reference is (a column, a glossary term, an allowed value) instead of *how* it looks (a hand-written link, italics). The build then decides the links and formatting.

## Syntax

A semantic reference is an ordinary Markdown link whose target names an entity type, optionally followed by an ID:

| Source | Meaning |
| :--- | :--- |
| `[ResourceType](#col)` | Column; the ID comes from the link text |
| `[resource type](#col:ResourceType)` | Column with an explicit ID and any display text |
| `[BilledCost](#col:InvoiceDetail.BilledCost)` | Column in a specific dataset |
| `["Usage"](#val:ChargeCategory)` | Allowed value of a column |
| `[Cost and Usage](#ds)` | Dataset |
| `[NumericFormat](#attr)` | Attribute |
| `[Includes Tags](#omc)` | Operating model condition |
| `[ContractAppliedObject](#obj)` | JSON object (or value) defined in a column file |
| `[ContractAppliedObjectSchema](#schema)` | JSON schema |
| `[FocusVersion](#meta)` | Metadata field or collection |
| `[DatasetInstanceId](#meta:Recency.DatasetInstanceId)` | Metadata field in a specific collection |
| `[charges](#term)` | Glossary term; plurals resolve to the singular entry |
| `[covered](#term:covered-charge)` | Glossary term with an explicit key |

Any other link, such as `#appendix.roundingvariancetolerance`, passes through unchanged.

The link form was picked because every tool already in the toolchain parses it as a normal link: Pandoc's `gfm` reader, pymarkdownlnt, GitHub, and editors. Custom HTML tags trigger the inline-HTML lint rule and show up as unpaired raw HTML in Pandoc. Pandoc's `[x]{.col}` spans render literally on GitHub.

## Pieces

* [`build_registry.py`](build_registry.py) generates `build/registry.json` from `specification/`. It reads each column's Column ID, Display Name, dataset and Allowed Values, each JSON column's object, each attribute and operating model condition by its heading, the schemas in `schemas/schemas.mdpp`, each metadata field and collection, and the `<a name="glossary:…">` anchors. Anchors are computed with the same algorithm as markdown-pp's TableOfContents module, so links match the assembled spec.
* [`focus_semantic.py`](focus_semantic.py) is a panflute filter that resolves references and lints them. Its docstring lists the options.
* [`samples/`](samples/) holds `billedcost.md` and `chargeclass.md` rewritten in semantic form.
* [`build.sh`](build.sh) runs everything and writes its outputs to `build/`.
* [`scan_spec.sh`](scan_spec.sh) runs the lint over all 308 Markdown source files and prints the spec-wide counts cited in issue #2779.
* [`resolve_semantic.py`](resolve_semantic.py) resolves tags Markdown-to-Markdown during `make` (see [DEMO.md](DEMO.md)).
* [`tag_sources.py`](tag_sources.py) rewrites source files to use semantic tags and lists what needs a human decision.
* [`compare_rendered.sh`](compare_rendered.sh) compares the published `spec.md` with a base ref, word by word.

```bash
PYTHON=/path/to/venv/bin/python ./build.sh
```

```bash
PYTHON=/path/to/venv/bin/python ./scan_spec.sh
```

## Definitions

Definitions are not tagged. The registry recognizes them by the structure the specification already follows, and that structure is treated as the contract:

| Entity | Defined by |
| :--- | :--- |
| Column | A file under `datasets/<dataset>/columns/` with `## Column ID` and `## Display Name` sections |
| Allowed value | A row of the column's `## Allowed Values` table, in the column headed "Value" or headed with the Display Name |
| Glossary term | `<a name="glossary:key"><b>Term</b></a>` in `glossary.md` |
| Attribute, operating model condition, dataset | Its file's ID and name sections (`## Attribute ID` and `## Attribute Name`, `## Operating Model Condition ID` and `## Display Name`, `## Dataset ID` and `## Display Name`); the anchor comes from the level-1 heading |
| JSON object | `### Object ID` and `### Object Display Name` (or `### Value ID` and `### Value Display Name`) in a column file, under a level-2 heading named by the object |
| JSON schema | A level-3 heading in `schemas/schemas.mdpp`, under its dataset's level-2 heading |
| Metadata field | A file under `metadata/` with `## Metadata ID` and `## Metadata Name` sections; its collection is the folder's `*_overview.md` |

`build_registry.py` checks that contract every time it runs:

| Code | Level | Check |
| :--- | :--- | :--- |
| REG001 | Error | Column file has no Column ID or no Display Name section |
| REG002 | Warning | Column file H1 differs from its Display Name |
| REG003 | Warning | Column ID is not PascalCase |
| REG004 | Error | Allowed Values table has no "Value" column or column headed with the Display Name |
| REG005 | Warning | The same allowed value is listed twice for one column |
| REG006 | Warning | Glossary key does not match its term (a trailing acronym such as "(CSP)" is ignored) |
| REG007 | Warning | Content Constraints "Dataset" row does not name the column's own dataset |
| REG008 | Error | A name or alias is shared by two entities of the same type |
| REG009 | Info | A name or alias is shared by entities of different types, so references must state the type |
| REG010 | Error | Malformed glossary anchor (the term would be silently dropped) |
| REG011 | Warning | Unknown front matter key, or aliases for an unknown glossary key |
| REG012 | Warning | A file under `datasets/` declares a dataset in front matter; it takes its dataset from its location |
| REG013 | Error | An ID section without its name section, or the reverse; or an attribute, operating model condition, or dataset file with neither (its ID falls back to its H1) |
| REG014 | Warning | A dataset, attribute, operating model condition, or metadata file's H1, or an object's level-2 heading, differs from its name |
| REG016 | Warning | A file or folder that defines an entity is not named after its ID in lowercase, per the [Repository Naming Conventions](../../guidelines/contributors/repository-naming-conventions.md) |
| REG017 | Warning | The specification and the Requirements Model (`requirements_model/releases/latest`) disagree: an entity with no rule file, an active rule file with no entity, or a different EntityId or EntityName. `--rm-release none` skips it |

`--strict` makes errors exit non-zero.

### Aliases in Front Matter

Facts the structure cannot hold go in optional YAML front matter on the defining file. The prototype supports one key, `aliases`:

```yaml
---
aliases: [invoice issuer]
---
```

In `glossary.md`, aliases are keyed by glossary key:

```yaml
---
aliases:
  covered-charge: [covered]
  cash-based-accounting: [cash-based]
---
```

An alias resolves like the Display Name, so `[covered](#term)` reaches the covered-charge entry without spelling out the key. Aliases also feed the lint checks: italic *covered* in legacy text is now reported as an untagged glossary term.

Column ID and Display Name deliberately stay in their sections, not in front matter, so there is still one place that defines each.

The prototype does not edit `specification/`. `samples/front_matter/` holds front matter snippets, and `build.sh` prepends each one to a fresh copy of the matching spec file (`--overlay`), so the demo never goes stale.

## Rendering Rules

* The first reference to an entity in each source file is a link. Later references are not.
* References inside tables always link, except glossary terms.
* A file never links to the entity it defines. For example, `BilledCost` inside `billedcost.md` is never linked.
* Glossary terms render in italics. Other entities render as plain text. With `focus-annotate=true`, each reference is also wrapped in `<span class="focus-col" data-focus-id="…">`, so styling becomes a CSS decision.
* `focus-link-mode=anchor` (the default) links to assembled-spec anchors. `focus-link-mode=source` links to the defining `.md` file instead, for GitHub-style per-file previews. Both come from the same source.

File boundaries come from `<!-- focus:file <path> -->` markers. The prototype's `build.sh` inserts them. In the real build, markdown-pp's `Include.py` would emit one per `!INCLUDE`.

## Lint Checks

| Code | Level | Check |
| :--- | :--- | :--- |
| FOCUS001 | Error | Unknown entity; a column ID that exists in several datasets, in a file with no dataset, without a qualifier; or an unqualified column that is not in the file's dataset |
| FOCUS003 | Warning | Column reference in a Requirements section whose text is not the ColumnId |
| FOCUS004 | Warning | Untagged ColumnId in prose |
| FOCUS005 | Warning | Italic text that matches a glossary term but is not tagged |
| FOCUS006 | Warning | Untagged multi-word Display Name (e.g., "Resource Type") in prose |
| FOCUS007 | Warning | Hard-coded link to a registry anchor; the message gives the semantic replacement |
| FOCUS008 | Error | Value that is not in the column's Allowed Values |
| FOCUS009 | Info | Plain text matching a glossary term (opt-in with `focus-lint-terms=true`) |
| FOCUS010 | Error | Front matter `dataset` names an unknown dataset (`resolve_semantic.py` only) |

`focus-strict=true` makes errors fail the Pandoc run.

## Results

* **Definition checks on the current specification.** All 127 column files pass REG001 to REG007, so the structural convention is reliable enough to build on. Four glossary keys don't follow the slug pattern (`chargeperiod`, `exclusiveendbound`, `inclusivestartbound`, `pascalcase`); changing them would break existing links, so they are reported, not fixed. Six names are shared by two entity types (e.g., "billing currency" is both the BillingCurrency column and a glossary term), which is the ambiguity that typed references resolve.
* **Lint of the original files.** The current `billedcost.md` and `chargeclass.md` produce 38 and 14 warnings (38 includes one found through the *covered* alias): hard-coded links (each with its suggested replacement), untagged ColumnIds in requirements (`BillingCurrency`, `InvoiceIssuerName`), and italic glossary terms with no tag. These are the warnings a migration script would act on.
* **Lint of the semantic samples.** 0 errors, 0 warnings.
* **Resolved output compared with the hand-written originals** (`build/*.diff`). Every difference is a consistency fix:
  * Glossary terms that were linked twice in one file (*covered charge*, *covering charge*, *covered*, *invoice issuer*) are now linked only once.
  * *commitments* was italic but never linked. Its first occurrence now links.
  * In `chargeclass.md`, "corrections", "charges" and "correction" were plain text in some places and italic glossary terms in others. They are now consistent.
* **Ambiguity found.** `billedcost.md` links the words "invoice issuer" to the **InvoiceIssuerName column** in the first paragraph, and to the **invoice issuer glossary term** in the Description. Linting can't settle that. With semantic markup the author has to choose, and the choice is recorded. The sample uses the glossary term in prose and the column in requirements.
* **Error handling.** Misspelled IDs, unknown terms, values outside a column's Allowed Values, and unqualified column IDs that exist in several datasets are all reported with a fix hint.

`build/preview.html` is an annotated rendering with a toggle that highlights each entity type and marks later, unlinked mentions.

## Open Questions

* **Front matter in the real build.** markdown-pp pastes included files in raw, so front matter would land mid-document. The Include module would need to strip it, next to the one-line file marker change.
* **More front matter keys.** A likely next candidate is `deprecated-ids` (resolve an old ColumnId with a warning).
* **Dataset scope in shared files.** Eleven ColumnIds (e.g., `BilledCost`, `BillingCurrency`, `InvoiceId`) exist in more than one dataset. Column files resolve to their own dataset automatically. Other files can declare a default in front matter (`dataset: CostAndUsage`), which the demo branch build (`resolve_semantic.py` and `tag_sources.py`) applies; see `DEMO.md`. The Pandoc filter in `focus_semantic.py` does not read it yet. The alternatives are qualifying every shared column or a project-wide default of Cost and Usage.
* **Line numbers.** `resolve_semantic.py` reports source line numbers. The Pandoc filter reports file and section, not line. Pandoc's `gfm+sourcepos` extension could add line numbers. A separate pymarkdownlnt plugin could also run the same checks against source positions.
* **Lowercase prose.** "resource type" as ordinary words is still allowed. FOCUS009 shows how noisy term detection on plain text is. It probably works best as an on-demand report, not a build gate.
* **Links for values.** Values currently render as plain `"Correction"` text. They could link to the column's Allowed Values table.
* **Migration.** FOCUS007, FOCUS004 and FOCUS005 already give the exact rewrite for most existing markup. A script could apply those mechanically and leave the ambiguous cases (like "invoice issuer") for people to decide.
