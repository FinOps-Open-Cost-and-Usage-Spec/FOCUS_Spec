# Editorial Style Guidelines

## Table of Contents

* [Overview](#overview)
* [Core Editorial Rules](#core-editorial-rules)
  * [References and Terminology](#references-and-terminology)
  * [Document Structure](#document-structure)
  * [Text and Formatting](#text-and-formatting)
* [Column Editorial Rules](#column-editorial-rules)
  * [Column Examples](#column-examples)
* [Supported Features Editorial Rules](#supported-features-editorial-rules)

## Overview

The "Editorial Style Guidelines" section ensures consistency and clarity across all documentation. Adhering to these guidelines is crucial for maintaining a unified style, which enhances readability and reduces misinterpretation. By following the specified standards—whether in formatting, linking, or structuring information—we ensure that all documents are professional, clear, and aligned with our editorial principles. Consistent application of these guidelines contributes to high-quality, user-friendly documentation.

These guidelines can be modified through a Pull Request (PR), which the members must review and agree upon. This process ensures that any changes are thoughtfully considered and maintains the overall integrity of our editorial standards.

## Core Editorial Rules

### References and Terminology

#### Entity References

* **Entity ID References:** Formatting and usage conventions for normative requirements are defined in the Normative Requirements Guidelines.
* **Entity ID Formatting:** Entity IDs MUST be formatted without spaces.
* **Entity ID Naming:** Entity IDs MUST match the exact naming conventions used in the schema (e.g., CommitmentDiscountId).
* **Column and Attribute ID Emphasis:** Column and attribute IDs are written in normal text, without bold or italics.
* **Entity Display Name References:** References to FOCUS entities in non-normative content (i.e., outside Requirements sections) MUST use Display Names when available.
* **Entity Scope:** These rules apply to all entities defined in the FOCUS specification (e.g., Columns, Attributes, Datasets, Objects).

#### Display Names

* **Display Names Usage:** Display Names SHOULD be used in introductory or explanatory sections where natural language context is more appropriate.
* **Display Names Formatting:** Display Names SHOULD follow normal text conventions, including spaces between words (e.g., Commitment Discount ID).
* **Consistent Formatting:** This formatting MUST be used consistently across all normative requirements, descriptions, and tables when referencing a specific string value.

#### Column Values

* **Column Value Formatting:** Column values are enclosed in double quotation marks and written in normal text, without bold or italics (e.g., "Usage", "Tax", "TB").

#### Linking

* **Link Targets:** Column and attribute names and IDs are linked to the section that defines them.
* **Glossary Terms:** Glossary terms are written in italics and are linked to the glossary (e.g., `[*SKU*](#glossary:sku)`).
* **Linking on First Occurrence:** To avoid excessive linking, entity references (including FOCUS entity IDs, display names, and glossary terms) MUST be linked only on their first occurrence within a given source markdown file.

> **Note:** Unless otherwise specified, first-occurrence linking is evaluated relative to the containing source markdown file.

**Exceptions:**

* In **Content Constraints** sections, all entity references MUST be linked, regardless of prior occurrence in the source markdown file.
* In the **Glossary** file, entity references MUST be linked only on their first occurrence within each glossary entry, rather than once per source markdown file.

#### Comparison Terminology

To ensure consistent language when describing relationships and evaluations between values, normative requirements and standard prose MUST use the following terminology:

* **Numeric Values:** Use "equal" or "be equal to" when comparing numeric values, costs, quantities, or mathematical sums (e.g., "ContractedCost MUST be equal to BilledCost"). Do not use "match".
* **Identifiers and Strings:** Use "match" when comparing strings, IDs, or names (e.g., "HostProviderName MUST match ServiceProviderName"). Do not use "equal".
* **State and Conditions:** Use forms of the verb "to be" (e.g., "is", "are", "be") when evaluating if a column contains a specific value or state (e.g., "when ChargeCategory is `Purchase`" or "ChargeCategory MAY be `Usage`"). Do not use "equals" or "equal", **except** when evaluating inequalities (e.g., "greater than or equal to").
* **Inequalities:** When expressing range or directional limits, the standard phrases "greater than or equal to" and "less than or equal to" MUST be used, even for non-numeric data types like timestamps or dates (e.g., "BillingPeriodLastUpdated MUST be greater than or equal to BillingPeriodCreated").
* **Semantic Comparisons:** When comparing concepts, formats, or values that share the same meaning but may not be strictly identical strings, use "equivalent" or "semantically equivalent" (e.g., "PricingUnit MUST be semantically equivalent to the corresponding pricing measurement unit..."). Do not use "equal".

> **Note:** Validation of comparison terminology may require contextual understanding of value types, identifiers, semantic equivalence, or domain-specific meaning and may not always be suitable for deterministic editorial validation.

### Document Structure

#### Section Structure

* **Consistent Subsection Order:** Sections for the same entity type SHOULD follow a consistent subsection order (e.g., Title, Requirements, Entity ID, Display Name, Description, Content Constraints, Version Introduced).

> **Note:** The subsection order examples in this section are illustrative unless a canonical order is explicitly defined for a specific entity type.

* **Consistent Subsection Titles:** Subsection titles SHOULD match exactly across sections of the same entity type.

#### Requirements Sections

Normative requirements are defined and authored exclusively according to the Normative Requirements Guidelines.

Authors MUST refer to the [Normative Requirements Guidelines](normative-requirements-guidelines.md) when writing or modifying normative requirements.

* **Structural Anchors:** Normative bullet lists MUST be preceded by a structural anchor. See [Normative Requirements Guidelines](normative-requirements-guidelines.md#structural-anchor) for details.

> **Note:** Validation of structural anchors may require contextual editorial judgment and is not always suitable for deterministic editorial validation.

* **Example** (Markdown, illustrative):

  ```md
  ... MUST adhere to the following requirements:
  ```
* **Consistent Introductory Phrases:** Introductory phrases for normative lists SHOULD be consistent within a section.

> **Note:** Authors SHOULD prefer stable introductory patterns such as "... MUST adhere to the following requirements:" within the same section unless contextual variation improves readability.

* **Normative Scope:** Normative requirements (those using BCP-14 keywords) MUST appear only in the "Requirements" section.
* **No Normative Leakage:** Normative keywords (MUST, SHOULD, MAY, etc.) MUST NOT be used in any section other than "Requirements".

> **Note:** This restriction applies to normative content within FOCUS specification entities and does not prohibit guideline documents, examples, or editorial instructions from discussing normative terminology or authoring rules.

* **Example** (Markdown, illustrative):

```md
 Correct:
  ## Requirements
  ...
  * PricingQuantity MUST be greater than 0.
  
 Incorrect:
  ## Description
  ...
  * PricingQuantity MUST be greater than 0.
```

#### Bullet Structure

* **Unordered List Style:** All unordered lists in Markdown MUST use asterisks (`*`) rather than dashes (`-`) or plus signs (`+`). This maintains visual consistency across the specification and aligns with our automated linting standards.
* **Indentation Levels:** Nested bullet points MUST be indented using two spaces per level.
* **Indentation Usage:** A nested indentation level MUST only be introduced when a parent bullet defines a composite (grouping) requirement, typically ending with a colon (:).
* **Example** (illustrative):

    ```md
    ... MUST adhere to the following requirements:

    * ... MUST be of type JSON ...
    * ... MUST adhere to the following nullability requirements:
      * ... SHOULD NOT be null when ...
      * ... MUST be null when ...
      * ... MUST adhere to the following ...
        * ... MUST be of type ...
    ```
* **No Skipped Levels:** Nested bullets points MUST NOT skip indentation levels.
* **Consistent Indentation:** All bullet points within the same list MUST use consistent indentation.
* **Example** (Markdown, illustrative):

  ```md
  * ... MUST be null when ChargeCategory is "Tax".
  * ... MUST be null when ChargeCategory is "Adjustment".
  ```

#### Notes and Exceptions

##### Notes

* **Permitted in Non-Normative Content Only:** Notes MUST NOT appear in Requirements sections. Notes MAY appear in non-normative sections of the specification and in guidelines documents.
* **Blockquote Format:** Notes MUST be expressed using Markdown blockquote syntax (`>`). This creates a consistent, parseable container and allows downstream tooling to control visual presentation in HTML and PDF outputs.
* **Note Label:** Notes MUST begin with the label `**Note:**`, `**Notes:**`, or `**Preview:**` (the term `Note`, `Notes`, or `Preview`, followed by a colon, in bold). The `**Preview:**` label is used only for notes that mark preview content (see [Preview Process](spec-change-guidelines.md#preview-process)).
* **Consistent Terminology:** Only the terms `Note`, `Notes`, or `Preview` MUST be used. Variants such as `Important Note`, `Warning`, or similar terms MUST NOT be used.
* **Non-Normative Content:** Notes MUST be informative and non-normative. They MUST NOT contain normative keywords (e.g., MUST, SHOULD, MAY).

> **Note:** This restriction applies to informative notes within specification content and does not prohibit guideline documents or explanatory examples from discussing normative keywords.

* **Single-Line Notes:** A note containing a single statement MUST be written as a single blockquote line.
* **Multi-Line Notes:** A note spanning multiple lines MUST repeat the blockquote prefix (`>`) on each line. A blank blockquote line (`>`) MUST separate the label from the bullet list.
* **Multiple Notes:** When multiple notes are present in the same context, they SHOULD be grouped within a single blockquote and expressed as bullet points.
* **Bullet Usage in Notes:** When using bullets inside a note, the bullets MUST follow standard bullet formatting rules defined in this document.
* **Example** (Markdown, illustrative):

  ```md
  > **Note:** This is a single-line note.
  ```
* **Example** (Markdown, illustrative):

  ```md
  > **Notes:**
  >
  > * This is the first note.
  > * This is the second note, which provides additional information.
  ```

##### Exceptions

* **Not Permitted in Requirements Sections:** Exceptions MUST NOT appear in Requirements sections of the specification. If a condition represents a normative constraint, authors MUST express it explicitly using structured requirement patterns (e.g., “when”, “unless”) instead.
* **No Blockquote Usage:** Exceptions MUST NOT be expressed using blockquote syntax (which is strictly reserved for Notes).
* **No Header Usage:** Exceptions MUST NOT use Markdown headers (e.g., `#### Exceptions`).
* **Exception Label:** Exceptions MUST begin with the inline label `**Exception[ for <Topic>]:**` or `**Exceptions[ for <Topic>]:**` (the term `Exception` or `Exceptions`, with or without a semantic qualifier `for <Topic>`, followed by a colon, formatted in bold).
  * A semantic qualifier SHOULD be included in Normative Requirements Guidelines to support cross-referencing and automated processing.
  * A semantic qualifier MAY be included in other guidelines.
  * When used, semantic qualifiers SHOULD be applied consistently throughout the document.
* **Consistent Terminology:** Only the term `Exception` or `Exceptions` MUST be used. Variants such as `Special Case`, `Caveat`, or similar terms MUST NOT be used.
* **Structural Relationship:** Exceptions MUST be directly associated with the content they modify and SHOULD appear immediately after the relevant content.
* **Single-Line Exceptions:** An exception containing a single statement MUST be written as a single line of plain text immediately following the label.
* **Multi-Line Exceptions:** An exception spanning multiple statements MUST be expressed as a bullet list. A blank line MUST separate the label from the bullet list.
* **Bullet Usage in Exceptions:** When using bullets inside an exception, the bullets MUST follow standard bullet formatting rules defined in this document.
* **Example** (Markdown, illustrative):

  ```md
  **Exception:** This is a single-line exception.
  ```
* **Example** (Markdown, illustrative):

  ```md
  **Exceptions:**

  * This rule does not apply when ChargeCategory is `Adjustment`.
  * This rule does not apply when ChargeCategory is `Tax`.
  ```

#### Examples

> **Note:** Authors should consult the actual FOCUS attribute specification files as the source of truth, as these guidelines do not necessarily reflect the latest version.

* **Brand-Free Identifiers:** Resource, host, and pod-level identifiers in appendix examples MUST use neutral, brand-free labels (e.g., `host-prod-07`, `pod-orders-01`) rather than labels derived from fictitious customer or data generator names, so that an identifier does not read as an additional, unintended entity in the example.
* **Valid Examples:** Examples MUST reflect valid combinations of values defined in the specification.

  > **Note:** Validation of example correctness may require schema, glossary, or domain-specific review beyond editorial validation.
* **No New Terminology:** Examples MUST NOT introduce terminology that is not defined in the specification.

  > **Note:** Validation of terminology consistency may require comparison against the approved glossary and specification entity definitions.
* **Informative Examples:** Examples MUST be considered informative and non-normative, and MUST NOT define requirements.
* **Informative Status Note:** Each of the following files MUST include an informative, non-normative status note directly below its first heading:
  * `specification/overview.md`
  * `specification/supported_features/supported_features_overview.md`
  * `specification/appendix/appendix_overview.md`
* **Informative Status Note Scope:**
  * Each note MUST refer only to the section identified by that heading (e.g., "The Appendix").
  * The note MUST NOT be placed under the subheadings of that heading, including a heading originating from a nested file.
  * The Conventions section in `specification/overview.md` MUST identify the same headings and exceptions as the corresponding notes.
* **Example** (Markdown, illustrative):

  ```md
  > **Note:** The Appendix, except the Rounding Variance Tolerance appendix entry, is informative and non-normative. It does not define requirements.
  ```

### Text and Formatting

#### Formatting

* **Sentence Spacing:** Sentences within paragraphs MUST be delineated with a single space.
* **Semicolons in Nested Lists:** When a comma-separated list contains one or more items with internal commas, semicolons MUST be used to separate the top-level list items to prevent ambiguity about item boundaries. See [Merriam-Webster's guide to semicolons](https://www.merriam-webster.com/grammar/a-guide-to-using-semicolons) for further reference.
  * **Example** (prose, illustrative):
    * Incorrect: `The columns foster data integrity, interoperability, and consistency, improve data analysis and reporting, and support reliable decision-making.`
    * Correct: `The columns foster data integrity, interoperability, and consistency; improve data analysis and reporting; and support reliable decision-making.`
* **Spelling Out Numbers**: In standard prose, numbers zero through nine MUST be spelled out as words (e.g., "one", "two", "nine"), while numbers 10 and above MUST be written as numerals (e.g., "10", "42").
  * **Exception:** This rule DOES NOT apply to technical values, mathematical formulas, JSON examples, or explicit column constraints (e.g., write `BilledCost MUST be 0`, not `BilledCost MUST be zero`).
* **Dash Formatting:**
  * An unspaced hyphen (`-`) MUST be used for compound words (e.g., `cost-only`) and ranges (e.g., `2024-2025`).
  * A spaced hyphen (` - `) MUST be used to set off parenthetical phrases (e.g., `The metric - BilledCost - is required.`).
  * HTML entities and special unicode dash characters SHOULD NOT be used.

#### Currency and Dollar Signs

* **Currency and Dollar Signs:** The `$` symbol SHOULD be used for currency values in prose and tables. For build-pipeline behavior and troubleshooting related to dollar-sign parsing, see [MarkdownPP Guidelines](markdownpp-guidelines.md#currency-and-dollar-sign-handling).

#### JSON Formatting

* **Valid JSON:** JSON examples MUST be valid and complete.
* **JSON Quotation Marks:** JSON keys MUST use double quotation marks.
* **Consistent Structure:** JSON examples SHOULD follow consistent formatting and indentation.
* **Monospace Font:** JSON examples are written in monospace font (in Markdown, a fenced code block).

#### Tables

* **Complex Tables:** Simple tables can be created using markdown, but for more complex tables, it is recommended to use HTML elements. See the example below.

> **Note:** Complex tables typically include merged rows or columns, embedded images, multi-line content, or advanced layout requirements that are difficult to express reliably using standard markdown tables.

* **Markdown Table Spacing:**
  * When a markdown table has a maximum row width of less than 120 characters, the table SHOULD be padded with spaces to align the vertical pipes visually.
  * When a markdown table has a maximum row width of 120 characters or more, the table SHOULD use exactly one space after values without additional padding.

##### Example HTML Table

This is an example of a complex table with merged rows and columns, along with an additional header row.

<table  border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th colspan="2"><b>Heading 1</b></th>
    <th><b>Heading 2</b></th>
    <th><b>Heading 3</b></th>
  </tr>
  <tr>
    <td colspan="2">Cell 1,1 and Cell 1,2 Merged</td>
    <td>Cell 1,3</td>
    <td>Cell 1,4</td>
  </tr>
  <tr>
    <td><b>Heading 4</b></td>
    <td><b>Heading 5</b></td>
    <td><b>Heading 6</b></td>
    <td><b>Heading 7</b></td>
  </tr>
  <tr>
    <td colspan="2">Cell 2,1 & Cell 2,2</td>
    <td rowspan="2">Cell 3,3 <br/>& <br/> Cell 4,3</td>
    <td>Cell 3,4</td>
  </tr>
  <tr>
    <td>Cell 4,1</td>
    <td>Cell 4,2</td>
    <td>Cell 4,4</td>
  </tr>
</table>

This is how it is written in HTML:

```html
<table  border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th colspan="2"><b>Heading 1</b></th>
    <th><b>Heading 2</b></th>
    <th><b>Heading 3</b></th>
  </tr>
  <tr>
    <td colspan="2">Cell 1,1 and Cell 1,2 Merged</td>
    <td>Cell 1,3</td>
    <td>Cell 1,4</td>
  </tr>
  <tr>
    <td><b>Heading 4</b></td>
    <td><b>Heading 5</b></td>
    <td><b>Heading 6</b></td>
    <td><b>Heading 7</b></td>
  </tr>
  <tr>
    <td colspan="2">Cell 2,1 & Cell 2,2</td>
    <td rowspan="2">Cell 3,3 <br/>& <br/> Cell 4,3</td>
    <td>Cell 3,4</td>
  </tr>
  <tr>
    <td>Cell 4,1</td>
    <td>Cell 4,2</td>
    <td>Cell 4,4</td>
  </tr>
</table>

```

## Column Editorial Rules

### Column Examples

> **Note:** Examples are illustrative, informative, and non-normative. They do not define requirements and do not override the rules in this section.

#### Pricing Quantity

```markdown
# Pricing Quantity

The Pricing Quantity represents the volume of a given [*SKU*](#glossary:sku) associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#datamodel.costandusage.pricingunit). Distinct from [Consumed Quantity](#datamodel.costandusage.consumedquantity) (complementary to [Consumed Unit](#datamodel.costandusage.consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

## Requirements

PricingQuantity MUST adhere to the following requirements:

* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingQuantity MUST adhere to the following nullability requirements:
  * PricingQuantity MUST be null when [SkuPriceId](#datamodel.costandusage.skupriceid) is null.
  * PricingQuantity MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.

## Usability Constraints

**Aggregation:** When aggregating Pricing Quantity per [SKU ID](#datamodel.costandusage.skuid) for a SKU that includes both [*covering charges*](#glossary:covering-charge) and their [*covered charges*](#glossary:covered-charge), exclude one or the other, based on the specific use case, to avoid double counting. The appropriate set to exclude depends on the relevant cost basis for the use case. Exclude *covered charges* when aggregating on a billed basis, or *covering charges* when aggregating on an accrual basis.

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given *SKU* associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#datamodel.costandusage)   |
| Operating model conditions | Not applicable                              |
| Column type                | Metric                                      |
| Feature level              | Mandatory                                   |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attributes.numericformat) |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.0-preview
```

## Supported Features Editorial Rules

Rules specific to supported features pages are being defined in [#2572](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues/2572) ([PR #2778](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/pull/2778)).
