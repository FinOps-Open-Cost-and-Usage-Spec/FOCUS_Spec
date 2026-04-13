## Editorial Style Guidelines
The "Editorial Style Guidelines" section ensures consistency and clarity across all documentation. Adhering to these guidelines is crucial for maintaining a unified style, which enhances readability and reduces misinterpretation. By following the specified standards—whether in formatting, linking, or structuring information—we ensure that all documents are professional, clear, and aligned with our editorial principles. Consistent application of these guidelines contributes to high-quality, user-friendly documentation.

These guidelines can be modified through a Pull Request (PR), which the members must review and agree upon. This process ensures that any changes are thoughtfully considered and maintains the overall integrity of our editorial standards.

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
            - Pricing Quantity<br>
            - Pricing Unit<br>
            - Service Provider Name<br><br>
            <strong>Attribute Names</strong>:<br>
            - Currency Code Format<br>
            - Date/Time Format
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
            - Use the display name in the non-normative section.<br>
            - The first occurrence in a section is linked to the section.
        </td>
    </tr>
    <tr>
        <td><strong>Column &amp; Attribute IDs:</strong></td>
        <td>
           <strong>Columns IDs</strong>:<br>
            - PricingQuantity<br> 
            - PricingUnit<br> 
            - ServiceProviderName<br><br>
          <strong>Attributes IDs</strong>:<br>
            - CurrencyCodeFormat <br> 
            - DateTimeFormat <br>
        </td>
        <td>
          <strong>Columns IDs:</strong><br>
          &nbsp;&nbsp; PricingQuantity <br>
          &nbsp;&nbsp; PricingUnit<br>
          &nbsp;&nbsp; ServiceProviderName <br><br>
          <strong>Attributes IDs:</strong> </br>
          &nbsp;&nbsp; CurrencyCodeFormat </br>
          &nbsp;&nbsp; DateTimeFormat <br>
        </td>
        <td>
           - Use PascalCamel case (the first letter of every word, is capitalized)<br>
           - Normal text without bold or italics.<br>
           - The first occurrence in a section is linked to the section.
        </td>
    </tr>
    <tr>
        <td><strong>Column Values:</strong></td>
        <td>
            - `Usage`<br>
            - `Tax`<br>
            - `TB`<br>
        </td>
        <td>
            This column:<br>
            &nbsp;&nbsp; * MUST be null when ChargeCategory is "Tax" ...
        </td>
        <td>
            - Enclosed in backticks (e.g., `Usage`)<br>
            - Normal text without bold or italics
        </td>
    </tr>
    <tr>
        <td><strong>Normative Keywords &amp; Requirements Statements</strong></td>
        <td>
            MUST, MAY, MUST NOT and normative requirements statements
        </td>
        <td>
            This column:</br>
            &nbsp;&nbsp; * MUST NOT be null when ChargeClass is ... </br>
            &nbsp;&nbsp; * MUST be null when ChargeCategory is ... </br>
            &nbsp;&nbsp; * MAY be null for all other combinations of ... </br>
        </td>
        <td>
           - All uppercase, without bold.<br>
           - Bullet list format. <br>
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
            - Blue font + italic<br>
            - The first occurrence in a section is linked to the glossary.
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

* **Linking Only the First Time**: To prevent excessive linking within sections, Entity Names and Entity IDs (e.g., Column Names, Attribute IDs, and Glossary) will only be linked to their corresponding section or glossary the first time they appear in a section.

### Normative Requirements

* **Normative Requirements as a Bullet List**: Normative requirements (those using Normative Keywords) MUST be written as bullet points instead of lengthy sentences.

* **Normative Keyword Standardization:** To ensure consistency in the specification, normative language MUST use only the BCP-14 keywords MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY. The term "RECOMMENDED" as a normative keyword is deprecated starting December 2025. Where legacy text uses RECOMMENDED, it MUST be replaced with SHOULD.

* **Non-Normative Use of “recommended”:** The lowercase word “recommended” may still be used in non-normative, descriptive text (e.g., “Feature level: Recommended”) provided it does not express a normative requirement on implementers.

* **Single Requirement per Statement:** Each normative statement MUST express a single requirement.

* **Example** (Markdown, illustrative):

  ```md
  * ... MUST be of type String.
  * ... MUST conform to CurrencyFormat requirements.
  ```

* **Explicit Conditions:** Normative requirements MUST include an explicit condition unless the rule applies in all cases.

* **Condition Format:** Conditional clauses MUST use standardized patterns: “when / if / unless / only when / only if / except when / except if <condition>”.

* **Example** (Markdown, illustrative):

  ```md
  * ... MUST be null when ChargeCategory is "Tax".
  * ... MUST be null if ChargeCategory is "Tax".
  * ... MUST be null unless ChargeCategory is "Usage".
  ```

* **Subject Consistency:** Each normative statement MUST clearly identify the subject being constrained.

* **Example** (Markdown, illustrative):

  ```md
  * PricingQuantity MUST be greater than 0.
  ```
* **No Compound Conditions:** Normative requirements MUST NOT combine multiple conditions using “and” or “or” within a single statement.

### Entity References

* **Entity IDs:** Entity IDs (e.g., Column IDs, Attribute IDs, Dataset IDs) SHOULD be used in normative text sections, such as when specifying mandatory rules, schema definitions, or other implementation-related content. 

* **Entity IDs:** MUST be formatted without spaces.

* **Entity IDs:** MUST match the exact naming conventions used in the schema (e.g., CommitmentDiscountId).

* **Display Names:** Display Names SHOULD be used in introductory or explanatory sections where natural language context is more appropriate. These names should follow normal text conventions, including spaces between words (e.g., Commitment Discount ID).

* **Consistent Reference Type:** Normative requirements MUST use Entity IDs consistently.

* **Consistent Reference Type:** MUST NOT mix Entity IDs and Display Names within the same statement.

* **Multiple Entity References:** MUST use Entity IDs when referencing multiple entities in a normative statement.

* **Entity Scope:** These rules apply to all entities defined in the FOCUS specification (e.g., Columns, Attributes, Datasets, Objects).

### Column Values

* **Inline Code for Values:** When referencing specific string values that a column can contain, the value MUST be enclosed in backticks to render as inline code (e.g., `Usage`). 

* **Consistent Formatting:** This formatting MUST be used consistently across all normative requirements, descriptions, and tables when referencing a specific string value.

### Bullet Structure

* **Unordered List Style:** All unordered lists in Markdown MUST use asterisks (`*`) rather than dashes (`-`) or plus signs (`+`). This maintains visual consistency across the specification and aligns with our automated linting standards.

* **Indentation Levels:** Nested bullet points MUST be indented using two spaces per level.

* **Example** (illustrative):

    ```md
    ... MUST adhere to the following rules:

    * ... MUST be of type JSON ...
    * ... MUST adhere to the following nullability requirements:
      * ... SHOULD NOT be null when ...
      * ... MUST be null when ...
      * ... MUST adhere to the following ...
          * ... MUST be of type ...
    ```

* **No Skipped Levels:** Nested bullets MUST NOT skip indentation levels.

* **Consistent Indentation:** All bullets within the same list MUST use consistent indentation.

* **Separate Conditions:** Alternative conditions MUST be expressed as separate bullet points.

* **Example** (Markdown, illustrative):

  ```md
  * ... MUST be null when ChargeCategory is "Tax".
  * ... MUST be null when ChargeCategory is "Adjustment".
  ```

### Formatting

* **Introductory Phrase for Rules:** Normative bullet lists SHOULD be preceded by a short introductory phrase ending with a colon (:). 

* **Example** (Markdown, illustrative):

  ```md
  ... MUST adhere to the following rules:
  ```

* **Consistent Introductory Phrases:** Introductory phrases for normative lists SHOULD be consistent within a section.

* **Sentence Spacing:** Sentences within paragraphs MUST be delineated with a single space.

### JSON Formatting

* **Valid JSON:** JSON examples MUST be valid and complete.

* **JSON Quotation Marks:** JSON keys MUST use double quotation marks.

* **Consistent Structure:** JSON examples SHOULD follow consistent formatting and indentation.

### Section Structure

* **Consistent Subsection Order:** Sections for the same entity type SHOULD follow the same subsection order (e.g., Title, Requirements, Entity ID, Display Name, Description, Content Constraints, Introduced (version)).

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

* **Valid Examples:** Examples MUST reflect valid combinations of values defined in the specification.

* **No New Terminology:** Examples MUST NOT introduce terminology that is not defined in the specification.

* **Informative Examples:** Examples MUST be considered informative and non-normative, and MUST NOT define requirements. 

* **Example Note Requirement:** Example sections MUST include a note indicating that the content is informative and non-normative.

* **Example** (Markdown, illustrative):

  ```md
  > Note: The following examples are informative and non-normative. They do not define requirements.
  ```

### Important Text

* **Informative Notes:** Important notes MUST NOT contain normative keywords.

* **Currency and Dollar Signs:** Use literal `$` for currency values in prose and tables. For build-pipeline behavior and troubleshooting related to dollar-sign parsing, see [MarkdownPP Guidelines](markdownpp-guidelines.md#currency-and-dollar-sign-handling).

### Example

> **3.1.45. Pricing Quantity**
>
> The Pricing Quantity represents the volume of a given SKU associated with a resource or service used or purchased, based on the Pricing Unit. Distinct from Consumed Quantity (complementary to Consumed Unit), it focuses on pricing and cost, not resource and service consumption.
>
> **3.1.45.1. Requirements**
>
> PricingQuantity adheres to the following requirements:
> * PricingQuantity MUST be present in a Cost and Usage FOCUS dataset.
> * PricingQuantity MUST be of type Decimal.
> * PricingQuantity MUST conform to NumericFormat requirements.
> * PricingQuantity nullability is defined as follows:
>   * PricingQuantity MUST be null when SkuPriceId is null.
>   * PricingQuantity MUST be null when ChargeCategory is "Tax"
>   * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction"
>   * PricingQuantity MAY be null in all other cases.
> * PricingQuantity MUST be a valid decimal value when not null.
> * Cost metric (e.g., ContractedCost) MUST equal the product of the corresponding unit price (e.g., ContractedUnitPrice) and PricingQuantity when the unit price is not null and
> * PricingQuantity is not null.
>
> **3.1.45.2. Column ID**
>
> PricingQuantity
>
> **3.1.45.3. Display Name**
>
> Pricing Quantity
>
> **3.1.45.4. Description**
> The volume of a given SKU associated with a resource or service used or purchased, based on the Pricing Unit.
>
> **3.1.45.5. Usability Constraints**
>
> **Aggregation:** When aggregating Pricing Quantity for commitment utilization calculations, it's important to exclude commitment discount purchases (i.e. when Charge Category is "Purchase") that are paid to cover future eligible charges (e.g., commitment discount ). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude commitment discount usage (i.e. when Charge Category is "Usage"). This exclusion helps prevent double counting of these quantities in the aggregation.
>
> **3.1.45.6. Content Constraints**
>
> <img width="492" alt="image" src="https://github.com/user-attachments/assets/5185cbf9-306d-4663-a1c7-c8b7ab5c5bb8">
> 
> **3.1.45.7. Introduced (version)** 
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
    <td rowspan="2">Cell 3,3 </br>& </br> Cell 4,3</td>
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
    <td rowspan="2">Cell 3,3 </br>& </br> Cell 4,3</td>
    <td>Cell 3,4</td>
  </tr>
  <tr>
    <td>Cell 4,1</td>
    <td>Cell 4,2</td>
    <td>Cell 4,4</td>
  </tr>
</table>

```
