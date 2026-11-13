# [AI] Decide the conversion and rendering rules for semantic tags

## Action Item Details

**Parent Issue:** #2779

**Depends on:** AI #<tooling>

**Detailed Description**

Converting the specification to semantic tags touches more than 300 files, which is too many to review line by line. Instead, the Working Group approves each rule once, with an example, a count, and its known failure modes. A conversion PR is then reviewed by checking that it applies only approved rules, with the converter's report and the rendered comparison as evidence. This AI writes those rules down, implements each one as a separate switch in the converter, and records which are approved.

There are two sets of rules. **Conversion rules** decide which existing text becomes which tag. **Rendering rules** decide how a tag appears in the published specification. Rendering applies to every tag, so a conversion that changes no wording still changes where links appear.

Counts below are for `working_draft_interim` at `12770c1a`. They were measured with the demo converter (`tag_sources.py` on `2779-semantic-markup-demo`), turning one rule on at a time. With every rule on, the converter reproduces the demo's mechanical commit, apart from the sample files reviewed by hand.

**Conversion rules: translations.** These carry over what today's markup already says, without reading the prose. A reference converts to the entity its current markup names, even when the markup looks wrong. The checks report those cases, and they are corrected separately.

| Rule | What it does | Example | Tags | Files | Known failure modes |
| :--- | :--- | :--- | ---: | ---: | :--- |
| Entity links | A hand-written link to an entity's anchor becomes the shortest tag for that entity. The tag carries an explicit ID when the link text doesn't name the entity. Emphasis that wraps the whole link text is dropped. | `[Billed Cost](#datamodel.costandusage.billedcost)` → `[Billed Cost](#col)`, `[*charge*](#glossary:charge)` → `[charge](#term)` | 2,616 | 310 | A link to the wrong entity becomes a tag for the same wrong entity. One case: in `contractcommitmentperiodend.md`, the text "Contract Commitment Period Start" links to ContractPeriodStart, which FOCUS011 reports. |
| Italic glossary terms | An italic phrase outside a link becomes a term tag when it is a glossary term or its plural. | `*charges*` → `[charges](#term)` | 1,682 | 209 | Italics used for emphasis on a phrase that is also a glossary term become a term tag. In `skupricecreated.md:12`, "the *SKU Price* record" becomes a term tag, although #2735 says the record is meant. |
| Plain entity IDs | A ColumnId, dataset ID, attribute ID, operating model condition ID, JSON object or schema ID, or multi-word metadata ID in plain text becomes a tag. A column resolves in the file's dataset, which comes from its location under `datasets/<dataset>/`. Elsewhere it resolves in the only dataset that defines it. | `ChargeClass MUST` → `[ChargeClass](#col) MUST` | 2,543 | 291 | When several datasets define a ColumnId and the file has no dataset, it is left as written: 223 items, nearly all in the appendix and supported features. One-word metadata IDs (e.g., Schema) are left as ordinary words. |

Together the translations make 6,841 tags in 332 of the 341 files they apply to.

**Conversion rules: inferences.** These decide from context what today's markup leaves unstated, so a wrong result looks like a deliberate choice. Counts are on top of the translations.

| Rule | What it does | Example | Tags | Files | Known failure modes |
| :--- | :--- | :--- | ---: | ---: | :--- |
| Plain Display Names | A Display Name in plain text becomes a tag when it is written in its defined capitalization, has at least two words (or is the file's own entity), names one entity, and isn't also a glossary term. It must sit outside quotes, headings, and code. Metadata names count only under `metadata/`. | `Billed Cost represents` → `[Billed Cost](#col) represents` | 866 | 231 | Title Case words that mean the concept, not the column. Display Names that are also glossary terms are left as written (208 occurrences, e.g., SKU Price 101, Billing Period 21). |
| Values after a column reference | A quoted value right after a column reference and `is`, `is not`, `MUST be`, `MUST NOT be`, `equals`, `=`, or `!=` becomes a value tag when it is one of that column's allowed values. | `[ServiceCategory](#col) is "AI and Machine Learning"` → `is ["AI and Machine Learning"](#val:CostAndUsage.ServiceCategory)` | 157 | 53 | Few expected, since the sentence names the column. |
| Values of the file's own column | In a column file, a quoted string that is one of that column's allowed values becomes a value tag. | In `billingperiodstatus.md`, `"Open"` → `["Open"](#val:BillingPeriodStatus)` | 67 | 15 | A quoted value of another column that has the same string. |
| File dataset | A file with no dataset of its own gets `dataset:` front matter when every column it references that only one dataset defines is in the same dataset. Its shared ColumnIds then resolve in that dataset. | `dataset: CostAndUsage` added to `appendix/ai_model_billing_examples/ai_model_billing_examples.md` | 166 | 56 | A shared ColumnId meant for another dataset resolves to the inferred one. The rendered comparison can't show this, because the text was plain before. |

The two value rules overlap and together make 199 value tags. Because the rules interact, all four inferences together add 1,265 tags to the translations.

**Conversion rules: exclusions.** Both sets leave these as written:

* Headings, code spans and code blocks, raw HTML lines, and front matter.
* The sections that define an entity (Column ID, Display Name, Attribute ID, Attribute Name, Operating Model Condition ID, Dataset ID, Metadata ID, Metadata Name, Object ID, Object Display Name, Value ID, Value Display Name).
* Tables outside Content Constraints: 340 rows that hold references.
* An italic, lowercase link to an entity that isn't a glossary term: 9 links from "data generator" to the Data Generator metadata section.
* Links to anchors that aren't entities, such as sub-sections of an entity: 32 links.
* Files with no references (`version.md`, `license.md`, `contributors.md`, `spec_abstract.md`), and `.mdpp` files other than `schemas/schemas.mdpp`.

**Rendering rules.** These restate today's linking conventions so the build applies them the same way in every file:

| Rule | Basis today |
| :--- | :--- |
| The first reference to an entity in a source file links, and later ones don't. A hand-written link to the entity counts as its first mention. | Editorial Guidelines, Linking on First Occurrence |
| References in Content Constraints tables always link, except glossary terms. | Editorial Guidelines, without the exception for glossary terms |
| A hand-written link in any other table doesn't count as a first mention. | Proposed in #2514 and #2765 |
| In `glossary.md`, each entry counts first mentions on its own. | Editorial Guidelines |
| A reference to the entity a file defines never links. A JSON object defined in its column's file links normally. | Existing practice, not stated in the guidelines |
| Glossary terms render in italics. Other entities render as plain text. | Editorial Guidelines, Entity References |
| Allowed values render as written, without a link. | Existing practice |

With the translations alone, the published `spec.md` changes on 689 lines, and no visible word changes: 294 links added where a first mention was plain text, 197 repeat links removed, 14 italics changes, and 295 lines whose table padding changed. Adding the inferences raises this to 812 lines, with 450 links added and 213 removed.

Decisions that change what the conversion PRs do:

* **Tables outside Content Constraints.** Leave them as written, as the demo does, or apply one rule: a reference links at its first mention within the table, and tables don't affect first mentions in prose. The demo's rules review recommends the second.
* **Glossary terms in Content Constraints.** The Editorial Guidelines link every entity reference there, but the demo doesn't link glossary terms.
* **Functional links.** In the demo conversion, seven links whose text isn't a name of the entity (e.g., "column requirements") were removed as repeats. `AGENTS.md` exempts functional links, but the Editorial Guidelines don't. Keep the exemption, or remove it?
* **Self-links.** Decide them by file, as the demo does, or by anchor (no link to the section a reference sits in, or to any section that contains it), which the demo's rules review recommends.
* **Each conversion rule.** Approve or reject each row. A rejected rule stays off, and the text it would have tagged stays as written.

The questions the demo raised that don't change these rules, such as properties of JSON columns or a glossary entry for the data generator role, stay with FR #2779 ([`CONVERSION.md`](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/2779-semantic-markup-demo/supporting_content/semantic_markup_prototype/CONVERSION.md#questions) lists all 17).

**Definition of Done**

* [ ] Each row in the tables above has an example, a count measured on the current base, and its known failure modes. The rendering rules are in the Editorial Guidelines. The conversion rules are in the converter's documentation, and they are removed when the `semantic:` key is removed.
* [ ] The converter switches each conversion rule on separately. Only approved rules are on, and CI reads that list from a single place.
* [ ] Each rule has a test for its example and a test for at least one case it must leave as written.
* [ ] For each file, the converter's dry run reports how many tags each rule would make and lists the items it left open.
* [ ] The Working Group's decision on each row and on each question above is recorded on this issue.
* [ ] The PR is merged into `working_draft_interim` (or into `working_draft` after 2026-12-03).
