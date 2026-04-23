## Editorial Style Guidelines
The "Editorial Style Guidelines" section ensures consistency and clarity across all documentation. Adhering to these guidelines is crucial for maintaining a unified style, which enhances readability and reduces misinterpretation. By following the specified standards—whether in formatting, linking, or structuring information—we ensure that all documents are professional, clear, and aligned with our editorial principles. Consistent application of these guidelines contributes to high-quality, user-friendly documentation.

These guidelines can be modified through a Pull Request (PR), which the members must review and agree upon. This process ensures that any changes are thoughtfully considered and maintains the overall integrity of our editorial standards.

### Normative Requirements
Normative requirements are defined and authored exclusively according to the Normative Requirements Guidelines.

Authors MUST refer to the [Normative Requirements Guidelines](normative-requirements-guidelines.md) when writing or modifying normative requirements.

<table>
    <tr>
        <th>Component</th>
        <th>Display (PDF, HTML)</th>
        <th>Markdown (examples)</th>
        <th>Editorial Guidelines</th>
    </tr>
    <tr>
        <td><strong>Column &amp; Attribute Names:</strong></td>
        <td>
            <strong>Column Names</strong>:<br>
            * Pricing Quantity<br>
            * Pricing Unit<br>
            * Service Provider Name<br><br>
            <strong>Attribute Names</strong>:<br>
            * Currency Code Format<br>
            * Date/Time Format
        </td>
        <td>
            <strong>Column Names:</strong><br>
            &nbsp;&nbsp; Pricing Quantity<br>
            &nbsp;&nbsp; Pricing Unit<br>
            &nbsp;&nbsp; Service Provider Name<br><br>
            <strong>Attribute Names</strong>:<br>
            &nbsp;&nbsp; Currency Code Format<br>
            &nbsp;&nbsp; Date/Time Format<br>
        </td>
        <td>
            * Use the display name in the non-normative section.<br>
            * The first occurrence in a section is linked to the section.
        </td>
    </tr>
    <tr>
        <td><strong>Column &amp; Attribute IDs:</strong></td>
        <td>
           <strong>Columns IDs</strong>:<br>
            * PricingQuantity<br> 
            * PricingUnit<br> 
            * ServiceProviderName<br><br>
          <strong>Attributes IDs</strong>:<br>
            * CurrencyCodeFormat <br> 
            * DateTimeFormat <br>
        </td>
        <td>
          <strong>Columns IDs:</strong><br>
          &nbsp;&nbsp; PricingQuantity <br>
          &nbsp;&nbsp; PricingUnit<br>
          &nbsp;&nbsp; ServiceProviderName <br><br>
          <strong>Attributes IDs:</strong> <br/>
          &nbsp;&nbsp; CurrencyCodeFormat <br/>
          &nbsp;&nbsp; DateTimeFormat <br>
        </td>
        <td>
           * Use PascalCamel case (the first letter of every word, is capitalized)<br>
           * Normal text without bold or italics.<br>
           * The first occurrence in a section is linked to the section.
        </td>
    </tr>
    <tr>
        <td><strong>Column Values:</strong></td>
        <td>
            * "Usage"<br>
            * "Tax"<br>
            * "TB"<br>
        </td>
        <td>
            This column:<br>
            &nbsp;&nbsp; * MUST be null when ChargeCategory is "Tax" ...
        </td>
        <td>
            * Enclosed in double quotation marks<br>
            * Normal text without bold or italics
        </td>
    </tr>
    <tr>
        <td><strong>Normative Keywords</strong> (Formatting Only)</td>
        <td>
            Normative keywords and statements (see Normative Requirements Guidelines)
        </td>
        <td>
            This column:<br/>
            &nbsp;&nbsp; * MUST NOT be null when ChargeClass is ... <br/>
            &nbsp;&nbsp; * MUST be null when ChargeCategory is ... <br/>
            &nbsp;&nbsp; * MAY be null for all other combinations of ... <br/>
        </td>
        <td>
           * Formatting follows Editorial Guidelines.<br>
           * Structure and usage are defined in the Normative Requirements Guidelines.<br>
        </td>
    </tr>
    <tr>
        <td><strong>Glossary</strong></td>
        <td>
            <a>SKU</a>, <a>resource</a>, <a>service</a>
        </td>
        <td>
            [*SKU*](#glossary:sku) <br>
            [*resource*](#glossary:resource) <br>
            [*service*](#glossary:service) <br>
        </td>
        <td>
            * Blue font + italic<br>
            * The first occurrence in a section is linked to the glossary.
        </td>
    </tr>
    <tr>
        <td><strong>Important Text</strong></td>
        <td> <img width="492" alt="image" src="https://github.com/user-attachments/assets/c6f60ff9-1503-43a3-8229-004595b334d2"></td>
        <td>> Important Consideration</td>
        <td>- It is added as a note.</td>
    </tr>
    <tr>
        <td><strong>Key-Value Format</strong></td>
        <td>JSON Script</td>
        <td>
            <pre>
**Example**:
```json
{
    "key1": "value1",
    "key2": true,
    "key3": 123
}
```
            </pre>
        </td>
        <td>- Monospace font</td>
    </tr>
    <tr>
      <td><strong>Tables</strong></td>
      <td><img width="492" alt="image" src="https://github.com/user-attachments/assets/5185cbf9-306d-4663-a1c7-c8b7ab5c5bb8"></td>
      <td><img width="492" alt="image" src="https://github.com/user-attachments/assets/83d0977f-a731-4def-93e3-b3e5f5dedb72"></td>
      <td> - Tables: Simple tables can be created using markdown, but for more complex tables, it is recommended to use HTML elements. See the example below. </td>
    </tr>
</table>

## Editorial Notes

> Note: Examples are illustrative, informative, and non-normative. They do not define requirements and do not override the rules in this section.

### Linking

* **Linking Only the First Time:** To prevent excessive linking within sections, Entity Names and Entity IDs (e.g., Column Names, Attribute IDs, and Glossary) will only be linked to their corresponding section or glossary the first time they appear in a section.

### Entity References

* **Entity ID References:** Formatting and usage conventions for normative requirements are defined in the Normative Requirements Guidelines.

* **Entity ID Formatting:** Entity IDs MUST be formatted without spaces.

* **Entity ID Naming:** Entity IDs MUST match the exact naming conventions used in the schema (e.g., CommitmentDiscountId).

* **Entity Display Name References:** References to FOCUS entities in non-normative content (i.e., outside Requirements sections) MUST use Display Names when available.

* **Entity Scope:** These rules apply to all entities defined in the FOCUS specification (e.g., Columns, Attributes, Datasets, Objects).

### Display Names


* **Display Names Usage:** Display Names SHOULD be used in introductory or explanatory sections where natural language context is more appropriate. 

* **Display Names Formatting:** Display Names SHOULD follow normal text conventions, including spaces between words (e.g., Commitment Discount ID).

* **Consistent Formatting:** This formatting MUST be used consistently across all normative requirements, descriptions, and tables when referencing a specific string value.

### Comparison Terminology

To ensure consistent language when describing relationships and evaluations between values, normative requirements and standard prose MUST use the following terminology:

* **Numeric Values:** Use "equal" or "be equal to" when comparing numeric values, costs, quantities, or mathematical sums (e.g., "ContractedCost MUST be equal to BilledCost"). Do not use "match".
* **Identifiers and Strings:** Use "match" when comparing strings, IDs, or names (e.g., "HostProviderName MUST match ServiceProviderName"). Do not use "equal".
* **State and Conditions:** Use forms of the verb "to be" (e.g., "is", "are", "be") when evaluating if a column contains a specific value or state (e.g., "when ChargeCategory is `Purchase`" or "ChargeCategory MAY be `Usage`"). Do not use "equals" or "equal", **except** when evaluating inequalities (e.g., "greater than or equal to").
* **Inequalities:** When expressing range or directional limits, the standard phrases "greater than or equal to" and "less than or equal to" MUST be used, even for non-numeric data types like timestamps or dates (e.g., "BillingPeriodLastUpdated MUST be greater than or equal to BillingPeriodCreated"). 
* **Semantic Comparisons:** When comparing concepts, formats, or values that share the same meaning but may not be strictly identical strings, use "equivalent" or "semantically equivalent" (e.g., "PricingUnit MUST be semantically equivalent to the corresponding pricing measurement unit..."). Do not use "equal".

### Bullet Structure

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

### Formatting

* * **Structural Anchor Requirements:** Normative bullet lists MUST be preceded by a structural anchor requirement. See [Normative Requirements Guidelines](normative-requirements-guidelines.md#structural-anchor-requirement) for details..

* **Example** (Markdown, illustrative):

  ```md
  ... MUST adhere to the following requirements:
  ```

* **Consistent Introductory Phrases:** Introductory phrases for normative lists SHOULD be consistent within a section.

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

### JSON Formatting

* **Valid JSON:** JSON examples MUST be valid and complete.

* **JSON Quotation Marks:** JSON keys MUST use double quotation marks.

* **Consistent Structure:** JSON examples SHOULD follow consistent formatting and indentation.

### Section Structure

* **Consistent Subsection Order:** Sections for the same entity type SHOULD follow a consistent subsection order (e.g., Title, Requirements, Entity ID, Display Name, Description, Content Constraints, Introduced (version)).

* **Consistent Subsection Titles:** Subsection titles SHOULD match exactly across sections of the same entity type.

* **Normative Scope:** Normative requirements (those using BCP-14 keywords) MUST appear only in the "Requirements" section.

* **No Normative Leakage:** Normative keywords (MUST, SHOULD, MAY, etc.) MUST NOT be used in any section other than "Requirements".

* **Example** (Markdown, illustrative):

```md
 ✔ Correct:
  ## Requirements
  ...
  * PricingQuantity MUST be greater than 0.
  
 ✘ Incorrect:
  ## Description
  ...
  * PricingQuantity MUST be greater than 0.
```

### Examples

> Note: Authors should consult the actual FOCUS attribute specification files as the source of truth, as these guidelines do not necessarily reflect the latest version.

* **Valid Examples:** Examples MUST reflect valid combinations of values defined in the specification.

* **No New Terminology:** Examples MUST NOT introduce terminology that is not defined in the specification.

* **Informative Examples:** Examples MUST be considered informative and non-normative, and MUST NOT define requirements. 

* **Example Note Requirement:** Example sections MUST include a note indicating that the content is informative and non-normative.

* **Example** (Markdown, illustrative):

  ```md
  > Note: The following examples are informative and non-normative. They do not define requirements.
  ```

### Notes and Exceptions

#### Notes

* **Permitted in Non-Normative Content Only:** Notes MUST NOT appear in Requirements sections. Notes MAY appear in non-normative sections of the specification and in guidelines documents.

* **Blockquote Format:** Notes MUST be expressed using Markdown blockquote syntax (`>`). This creates a consistent, parseable container and allows downstream tooling to control visual presentation in HTML and PDF outputs.

* **Note Label:** Notes MUST begin with the label `**Note:**` or `**Notes:**` (the term `Note` or `Notes`, followed by a colon, in bold).

* **Consistent Terminology:** Only the terms `Note` or `Notes` MUST be used. Variants such as `Important Note`, `Warning`, or similar terms MUST NOT be used.

* **Non-Normative Content:** Notes MUST be informative and non-normative. They MUST NOT contain normative keywords (e.g., MUST, SHOULD, MAY).

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

#### Exceptions

* **Not Permitted in Requirements Sections:** Exceptions MUST NOT appear in Requirements sections of the specification. If a condition represents a normative constraint, authors MUST express it explicitly using structured requirement patterns (e.g., “when”, “unless”) instead.

* **No Blockquote Usage:** Exceptions MUST NOT be expressed using blockquote syntax (which is strictly reserved for Notes).

* **No Header Usage:** Exceptions MUST NOT use Markdown headers (e.g., `#### Exceptions`). 

* **Exception Label:** Exceptions MUST begin with the inline label `**Exception:**` or `**Exceptions:**` (the term `Exception` or `Exceptions`, optionally followed by a qualifier, followed by a colon, in bold).

* **Consistent Terminology:** Only the term `Exception` or `Exceptions` MUST be used. Variants such as `Special Case`, `Caveat`, or similar terms MUST NOT be used.

* **Structural Relationship:** Exceptions MUST be directly associated with the content they modify and SHOULD appear immediately after the relevant content.

* **Single-Line Exceptions:** An exception containing a single statement MUST be written as a single line of plain text immediately following the label.

* **Multi-Line Exceptions:** An exception spanning multiple statements MUST be expressed as a bullet list. A blank line MUST separate the label from the bullet list.

* **Bullet Usage in Exceptions:** When using bullets inside an exception, the bullets MUST follow standard bullet formatting rules defined in this document.

* **Example** (Markdown, illustrative):

  ```md
  **Exceptions:** This is a single-line exception.
  ```

* **Example** (Markdown, illustrative):

  ```md
  **Exceptions:**

  * This rule does not apply when ChargeCategory is `Adjustment`.
  * This rule does not apply when ChargeCategory is `Tax`.
  ```

### Important Text

* **Informative Notes:** Important notes MUST NOT contain normative keywords.

* **Currency and Dollar Signs:** The `$` symbol SHOULD be used for currency values in prose and tables. For build-pipeline behavior and troubleshooting related to dollar-sign parsing, see [MarkdownPP Guidelines](markdownpp-guidelines.md#currency-and-dollar-sign-handling).

### Example

> **3.1.47 Pricing Quantity**
>
> The Pricing Quantity represents the volume of a given [*SKU*](#glossary:sku) associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#datasets.costandusage.pricingunit). Distinct from [Consumed Quantity](#datasets.costandusage.consumedquantity) (complementary to [Consumed Unit](#datasets.costandusage.consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.
>
> **3.1.47.1. Requirements**
>
> PricingQuantity MUST adhere to the following requirements:
>
> * PricingQuantity MUST be of type Decimal.
> * PricingQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
> * PricingQuantity MUST adhere to the following nullability requirements:
>   * PricingQuantity MUST be null when [SkuPriceId](#datasets.costandusage.skupriceid) is null.
>   * PricingQuantity MUST be null when [ChargeCategory](#datasets.costandusage.chargecategory) is "Tax".
>   * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datasets.costandusage.chargeclass) is not "Correction".
>   * PricingQuantity MAY be null in all other cases.
> * Cost metric (e.g., [ContractedCost](#datasets.costandusage.contractedcost)) MUST equal the product of the corresponding unit price (e.g., [ContractedUnitPrice](#datasets.costandusage.contractedunitprice)) and PricingQuantity when the unit price is not null and PricingQuantity is not null.
>
> **3.1.47.2. Column ID**
>
> PricingQuantity
>
> **3.1.47.3. Display Name**
>
> Pricing Quantity
>
> **3.1.47.4. Description**
>
> The volume of a given *SKU* associated with a *resource* or *service* used or purchased, based on the Pricing Unit.
>
> **3.1.47.5. Usability Constraints**
>
> **Aggregation:** When aggregating Pricing Quantity for commitment utilization calculations, it's important to exclude [*commitment discount*](#glossary:commitment-discount) purchases (i.e. when Charge Category is "Purchase") that are paid to cover future eligible [*charges*](#glossary:charge) (e.g., *commitment discount*). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude *commitment discount* usage (i.e. when Charge Category is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.
>
> **3.1.47.6. Content Constraints**
>
> <img width="492" alt="image" src="https://github.com/user-attachments/assets/5185cbf9-306d-4663-a1c7-c8b7ab5c5bb8">
> 
> **3.1.47.7. Introduced (version)**
>
> 1.0-preview

### Tables

* **Markdown Table Spacing:**
  * When a markdown table has a maximum row width of less than 120 characters, the table SHOULD be padded with spaces to align the vertical pipes visually.
  * When a markdown table has a maximum row width of 120 characters or more, the table SHOULD use exactly one space after values without additional padding.

### Example HTML Table
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
