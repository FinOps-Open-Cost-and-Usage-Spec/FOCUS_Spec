# Whole-Specification Conversion

> **Note:** This guide covers the conversion of the whole specification to semantic tags on this branch. Like the rest of the branch, it is a demonstration for FOCUS 1.6 and is not intended to be merged as is. [DEMO.md](DEMO.md) describes the branch. The questions at the end are open for the Working Group.

Every Markdown file that the specification build includes was converted where the tags cover its content. What the tags do not cover was left as written and is listed as a question. The branch is based on `working_draft` at `e0fd5f77` (2026-10-29), so the counts below describe the specification at that point.

## Result

| Measure | Count |
| :--- | ---: |
| Files the build includes | 377 |
| Files that now contain tags | 333 |
| Semantic tags | 7,851 |
| ... glossary terms | 2,720 |
| ... columns | 3,708 |
| ... attributes | 334 |
| ... datasets | 343 |
| ... metadata fields and collections | 270 |
| ... operating model conditions | 220 |
| ... allowed values | 199 |
| ... JSON objects and schemas | 57 |
| Build errors | 0 |
| Build warnings | 11 |
| Tests passing | 191 |
| Changed lines in the published `spec.md` | 816 |
| ... lines whose visible words changed | 0 |
| Items the converter left for a decision | 450 |
| Hand-written entity links left in place | 272 |

The build resolves every tag, markdown-pp anchors and the link tests are unchanged, and the Markdown linter passes on all converted files. The conversion is idempotent: running `convert_all.sh` on converted files changes nothing.

## What the Converter Does

`convert_all.sh` finds the included files and runs `tag_sources.py` on them. The converter handles what the specification's structure already makes unambiguous:

* A hand-written link to an entity's anchor becomes the shortest tag that means the same entity.
* A dataset-qualified column keeps its qualifier only when the file's dataset does not already supply it.
* An italic phrase that names a glossary term becomes a term tag.
* An attribute, operating model condition, JSON object, schema, or multi-word metadata ID written as plain text becomes a tag.
* A ColumnId written as plain text becomes a tag. When it exists in another dataset only, the tag names that dataset.
* A multi-word Display Name written as plain text becomes a tag when it names one entity, is not also a glossary term, and is outside quotes, headings, and code. The file's own Display Name is tagged even when it is one word.
* A quoted value becomes a value tag when it follows a column reference and is one of that column's allowed values, or when it is an allowed value of the file's own column.
* A file with no dataset of its own gets `dataset:` front matter when every column it references points into one dataset.

The converter leaves headings, code, raw HTML lines, the sections that define an entity, and tables outside Content Constraints alone.

## Differences in the Published Specification

`compare_rendered.sh` compares the published `spec.md` with `working_draft` and sorts every difference by kind. No visible words changed.

| Kind | Differences | What it is |
| :--- | ---: | :--- |
| Whitespace only | 297 | Table padding, because a tag is shorter than the link it replaced. The rendered tables are identical |
| Link added | 445 | A first mention that was plain text is now a link (419 columns and datasets, 18 glossary terms, 8 metadata) |
| Link removed | 213 | A repeat link is now plain text (149 columns and datasets, 60 glossary terms, 2 metadata, 2 operating model conditions) |
| Link retargeted | 2 | "invoice issuer" in the two BilledCost introductions links the glossary term instead of the InvoiceIssuerName column (a judgment call from the first sample) |
| Italics | 18 | Italics removed from 12 links to columns, attributes, and Display Names, and added to 6 glossary terms that lacked them |
| Visible words changed | 0 | None |

The added and removed links are the Editorial Guidelines applied uniformly: link an entity at its first mention in each source file and not again. Content Constraints tables keep linking every row, and the glossary counts first mentions per entry. A link in a table outside Content Constraints does not count as a first mention, which follows the entity catalog table rule proposed in #2514 and #2765. For example, the Columns table in `dataset.md` no longer turns the links in the requirement list below it into repeats.

Since this branch was cut, `working_draft` has already fixed some of these by hand (for example #2773 and #2789). The remaining differences are the same kind of fix in the files nobody has reached yet.

Review of these differences is migration step 4. Each one is listed with its line in `build/compare/classification.tsv`. The kinds that need a person are link retargeted and any visible-word change, and both are rare or absent here. The added and removed links are editorial under the Specification Change Guidelines.

## What the Checks Found in the Source

The checks report disagreements. They do not say which side is wrong.

* **A link points at a different column than its text names.** In `contractcommitmentperiodend.md`, the text "Contract Commitment Period Start" links to ContractPeriodStart (FOCUS011).
* **Names that do not match their files.** 41 entity files and folders are not named after their entity ID (REG016). #2787 renames these along with the other files in the repository.
* **Names that do not match the Requirements Model.** 45 differences (REG017): 25 are the new SKU Price entities, which have no rule files yet.
* **A table header that is not "Value".** The SKU Price column PurchaseDurationType has an Allowed Values table headed "Time Unit" (REG004), so its values cannot be referenced.
* **Glossary keys that do not match their terms.** Four keys (REG006), for example `pascalcase` for "Pascal Case".
* **A role with no glossary entry.** "data generator" is written as an italic link nine times, but only the Data Generator metadata section exists to link to.
* **Display Names in Requirements sections.** Ten (FOCUS003): nine are in notes or "See" lines placed under a Requirements heading, and one is a requirement in `delivery_handling.md` whose link text is a phrase, not the entity ID.

## Questions

Each question lists what the conversion did, so the answer can be applied by rerunning the converter.

1. **Tables outside Content Constraints.** 231 hand-written links and 340 rows with references in 37 files were left as written. Catalog tables (the Columns table in `dataset.md`, the overview tables in supported features and operating model conditions) link every row, while example data tables do not. Is there a way for an author to say that a reference always links, or should catalog tables be recognized by structure? Should links in these tables count as first mentions? The demo says they do not.
2. **Display Names that are also glossary terms.** 208 occurrences were left untagged: SKU Price (101), Billing Period (21), List Unit Price (19), Billing Currency (18), Contracted Unit Price (16), Tags (14), Contract Commitment (12), and Dataset Instance (6). #2765 proposes that the capitalization of the Display Name means the entity and any other capitalization means the term. Should the converter apply that rule?
3. **Files that mix datasets.** 190 mentions of shared columns, in 11 files, could not be resolved to one dataset, and 111 of them are in `rate_optimization_and_contract_evaluation.md`. Qualifying each one (`[SkuPriceId](#col:SkuPrice.SkuPriceId)`) is explicit but verbose. Would a dataset per section be better?
4. **Inferred dataset defaults.** 57 files got `dataset:` front matter from the columns they already reference (53 Cost and Usage, 3 SKU Price, 1 Invoice Detail). A plain shared ColumnId in those files now means that dataset, and the rendered comparison cannot verify it. Should an author confirm each one? `grep -rl "^dataset:" specification` lists them.
5. **The data generator role and the metadata collection.** Nine italic links use "data generator" as a term linked to the Data Generator metadata section, and 28 Title Case metadata names appear outside the metadata section (Data Generator, FOCUS Version, Data Generator Version, and others). The conversion left them as written. Should the glossary get a Data Generator entry, and should metadata names be tagged outside the metadata section?
6. **Links to sub-sections.** 32 prose links point at sub-sections of an entity (the correction styles in `correction_handling.md`, "Schema Structure" in each JSON column), not at an entity. They stay hand-written. Should sub-sections become taggable?
7. **Display Names in Requirements sections.** Nine of the ten FOCUS003 findings are notes and "See" lines under a Requirements heading. Should the check skip them, or should they move out of Requirements sections? The tenth is a requirement with a descriptive link text ("FOCUS Metadata Schema object"), which is the functional-link question again.
8. **First-mention differences.** 445 links added and 213 removed. Is it acceptable to review them as editorial changes in bulk, and in what size of pull request?
9. **Functional links.** Seven removed links have anchor text unlike the entity's name (for example "column requirements" and "accrual basis"). AGENTS.md exempts "functional links using different anchor text", but the Editorial Guidelines do not. Should the resolver keep them?
10. **Emphasis on entity links.** Italics were removed from 12 links to columns, attributes, and Display Names, and added to 6 glossary terms. Nine lowercase italic links to the Data Generator section were left as written. Is italic on a non-term a mistake or deliberate emphasis?
11. **Quoted values.** 199 value tags were made. 125 quoted allowed values remain untagged (84 belong to one column and 41 to several, such as "Purchase" and "Usage") because no column reference precedes them. How should an author name the column for these?
12. **Link text and target disagree.** One case was found (see above). Does it need a separate fix in the specification?
13. **Table padding.** 297 table rows differ only in padding. Should the converter pad whole table columns, or is the linter's table rule enough?
14. **Merge mechanics.** The conversion changes 326 files, so every open pull request that edits specification content would conflict. Convert once on a quiet day, or convert area by area? The Requirements Model extraction workflow (`rm_extraction.yml`) also reads the Markdown source and is not tag-aware.
15. **Outside the specification.** The guidelines, `AGENTS.md`, and the Requirements Model rule files describe or depend on the link conventions, and were not converted. They would need to change together with the specification.

## Reproduce

```bash
PYTHON=/path/to/venv/bin/python supporting_content/semantic_markup_prototype/convert_all.sh
```

```bash
cd specification
make spec.html
```

```bash
PYTHON=/path/to/venv/bin/python supporting_content/semantic_markup_prototype/compare_rendered.sh
```

The first command converts the files and writes every item that needs a decision to `build/convert-run.txt`. The second builds the specification. The third writes the comparison with `working_draft` to `build/compare/`.
