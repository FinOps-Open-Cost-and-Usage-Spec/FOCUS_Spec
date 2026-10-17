# Addendum to Proposed Solution: How Definitions are Identified

> **Note:** Posted as a comment on #2779 (https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2779#issuecomment-6229607991). The posted version opens with this title in bold.

The proposal tags *references*. *Definitions* stay as they are. The registry recognizes each definition by the structure the specification already follows, and that structure becomes a checked contract:

* **Columns:** a file under `datasets/<dataset>/columns/` with `## Column ID` and `## Display Name` sections
* **Allowed values:** rows of the column's `## Allowed Values` table
* **Glossary terms:** the existing `<a name="glossary:key"><b>Term</b></a>` anchors
* **Attributes, operating model conditions, and datasets:** the level-1 heading of each file

The prototype checks this structure on every build. For example, it reports a missing Column ID, an H1 that differs from the Display Name, an Allowed Values table without a value column, or a Content Constraints Dataset row that names the wrong dataset.

Against `working_draft`, all 127 column files pass these checks, so the existing structure is reliable enough to build on. The checks also found:

* **Names shared across entity types.** Six names belong to two types of entity. For example, "billing currency" is both the BillingCurrency column and a glossary term, and "list unit price" is both the ListUnitPrice column and a glossary term. Untagged prose cannot say which one is meant, which is the ambiguity this request addresses.
* **Glossary keys that do not follow the pattern.** Four keys differ from the slug pattern the other glossary keys use: `chargeperiod`, `exclusiveendbound`, `inclusivestartbound`, and `pascalcase`. They are reported but not changed, because changing them would break existing links.

Facts the structure cannot hold, such as aliases (e.g., *covered* for *covered charge*), would go in optional front matter on the defining file. Column ID and Display Name would stay in their sections, so each entity is still defined in exactly one place. Using front matter in the real build would need markdown-pp to strip it when it assembles the specification.
