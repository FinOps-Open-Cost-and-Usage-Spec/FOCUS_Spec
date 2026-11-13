# [AI] Convert existing references to semantic tags with the translation rules

## Action Item Details

**Parent Issue:** #2779

**Depends on:** AI #<rules>

**Detailed Description**

This AI runs the translation rules approved in AI #<rules> (entity links, italic glossary terms, and plain entity IDs) over the specification, in the scope the Working Group chooses. Each converted file records each converted kind as `mechanical` in its `semantic:` front matter, so CI keeps it converted.

The conversion carries over what the markup says today and corrects nothing. For example, `skupricecreated.md:12` reads "the *SKU Price* record" in a requirement. The italics mark a glossary term, so the phrase becomes `[SKU Price](#term)`. As the first mention in the file, it now links to the glossary entry, although #2735 says the record is meant. Fixing that is a separate change, which the tags make easy to find.

**Scope.** The Working Group chooses which kinds and which files to convert. The counts are for `working_draft_interim` at `12770c1a`.

| Area | Files changed | `col` | `term` | `ds` | `attr` | `meta` | `omc` | `obj`, `schema` | Tags |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `appendix/` | 73 of 79 | 682 | 465 | 34 | 11 | 23 | 0 | 0 | 1,215 |
| `attributes/` | 15 of 16 | 4 | 318 | 5 | 27 | 1 | 0 | 0 | 355 |
| `datasets/billing_period/` | 7 of 7 | 43 | 27 | 29 | 17 | 0 | 0 | 0 | 116 |
| `datasets/contract_commitment/` | 31 of 31 | 262 | 87 | 80 | 50 | 0 | 5 | 6 | 490 |
| `datasets/cost_and_usage/` | 70 of 70 | 1,054 | 837 | 177 | 114 | 0 | 74 | 31 | 2,287 |
| `datasets/invoice_detail/` | 23 of 23 | 265 | 105 | 78 | 42 | 0 | 7 | 0 | 497 |
| `datasets/sku_price/` | 24 of 24 | 288 | 177 | 96 | 39 | 0 | 14 | 7 | 621 |
| `metadata/` | 33 of 33 | 4 | 25 | 1 | 18 | 191 | 0 | 0 | 239 |
| `operating_model_conditions/` | 27 of 27 | 3 | 205 | 0 | 0 | 0 | 78 | 0 | 286 |
| `supported_features/` | 25 of 27 | 200 | 308 | 20 | 4 | 2 | 9 | 0 | 543 |
| `glossary.md`, `overview.md`, `datasets/data_model.md`, `schemas/schemas.mdpp` | 4 of 4 | 31 | 143 | 8 | 4 | 3 | 3 | 0 | 192 |
| **All** | **332 of 341** | **2,836** | **2,697** | **528** | **326** | **220** | **190** | **44** | **6,841** |
| Files with the kind | | 239 | 258 | 182 | 169 | 51 | 93 | 7 | |

* Allowed values (`val`) have no translation rule. Only the inferences tag them.
* `term` has no dataset question, so converting it alone leaves no items open for lack of a dataset.
* Proposed: every kind and every file in one PR, merged at a time agreed with the maintainers. Area by area is the alternative, with one PR per row of the table.

**What the PR shows.** For the whole specification with every kind:

* **Rendered differences** in the published `spec.md`: 689 lines, and no visible word changed. 294 links are added where a first mention was plain text (270 columns and datasets, 18 glossary terms, 6 metadata). 197 repeat links are removed (136 columns and datasets, 58 glossary terms, 2 operating model conditions, 1 metadata). There are 14 italics changes and 295 table padding changes. `compare_rendered.sh` lists each one.
* **Items left open**, 234 in all. 223 are ColumnIds defined in several datasets, in files with no dataset of their own, nearly all in the appendix and supported features. 9 are italic links from "data generator" to the Data Generator metadata section. 1 is a column outside its file's dataset. 1 is a link whose text names another column, which is converted to its target as written and reported by FOCUS011. With `col` listed as `mechanical`, the 221 untagged ColumnIds that FOCUS004 reports are information, not errors. The inference AI or the semantic review resolves them.
* **Checks on the new tags**: 0 errors and 20 warnings. FOCUS012 (case) has 12, FOCUS003 (a Display Name in a requirement) has 5, FOCUS013 (glossary case) has 2, and FOCUS011 has 1. These report disagreements already in the source, and the PR leaves them as they are.

**Merge timing.** A whole-specification conversion conflicts with every open PR that edits specification content. The maintainers should choose the merge window, and decide whether it comes before or after PR #2787, which renames files and folders. 1.6 work targets `working_draft_interim` until the 1.5 IPR Review ends on 2026-12-03, and `working_draft` after that.

**Definition of Done**

* [ ] The Working Group's choice of kinds and files is recorded on this issue.
* [ ] The converter, with only the approved translation rules switched on, has been run on every file in scope, and nothing else in those files changed.
* [ ] Each converted file lists each converted kind as `mechanical`, and rerunning the converter changes nothing, which CI checks.
* [ ] The build passes with 0 errors.
* [ ] The PR includes the rendered comparison against its base. No visible word changed, and every added or removed link and every italics change is listed.
* [ ] The PR lists the items left open, for the inference AI and the semantic review.
* [ ] The PR is merged in the agreed window.
