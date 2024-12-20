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
            - Provider <br><br>
            <strong>Attribute Names</strong>:<br>
            - Currency Code Format<br>
            - Date/Time Format
        </td>
        <td>
            <strong>Column Names:</strong><br>
            &nbsp;&nbsp; Pricing Quantity<br>
            &nbsp;&nbsp; Pricing Unit<br>
            &nbsp;&nbsp; Provider<br><br>
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
            - ProviderName<br><br>
          <strong>Attributes IDs</strong>:<br>
            - CurrencyCodeFormat <br> 
            - DateTimeFormat <br>
        </td>
        <td>
          <strong>Columns IDs:</strong><br>
          &nbsp;&nbsp; PricingQuantity <br>
          &nbsp;&nbsp; PricingUnit<br>
          &nbsp;&nbsp; ProviderName <br><br>
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
            - "Usage"<br>
            - "Tax"<br>
            - "TB"<br>
        </td>
        <td>
            This column:<br>
            &nbsp;&nbsp; * MUST be null when ChargeCategory is "Tax" ...
        </td>
        <td>
            - Enclosed in double quotation marks<br>
            - Normal text without bold or italics
        </td>
    </tr>
    <tr>
        <td><strong>Normative Keywords &amp; Statements</strong></td>
        <td>
            MUST, MAY, MUST NOT and normative statements
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
      <td> - Tables: Simple tables can be created using markdown, but for more complex tables, it is RECOMMENDED to use HTML elements. See the example below. </td>
    </tr>
</table>

**Editorial Notes**
* **Linking Only the First Time**: To prevent excessive linking within sections, Column Name, Column ID, Attributes Names, Attributes IDs, and Glossary will only be linked to their corresponding section or glossary the first time they appear in a section.

* **Normative Requirements as a Bullet List**: Normative statements (those using Normative Keywords) should be written as bullet points instead of lengthy sentences. 

* **Column IDs:** They SHOULD be used in normative text sections, such as when specifying mandatory rules, schema definitions, or other implementation-related content. These Column IDs should be formatted without spaces and should match the exact naming conventions used in the schema (e.g., CommitmentDiscountID). 

* **Display Names:** They SHOULD be used in introductory or explanatory sections where natural language context is more appropriate. In these sections, display names should follow normal text conventions, including spaces between words (e.g., Commitment Discount ID).


### Example

> **2.28. Pricing Quantity**
>
> The Pricing Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#pricingunit). Distinct from [Consumed Quantity](#consumedquantity) (complementary to [Consumed Unit](#consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.
>
>  * The PricingQuantity column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset). 
>  * This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements 
>  * The value MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction".
> 
> This column:
>  * MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", 
>  * MUST be null when ChargeCategory is "Tax", and 
>  * MAY be null for all other combinations of ChargeClass and ChargeCategory. 
>  * When unit prices are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric, except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.
>
> **2.28.1. Column ID**
>
> PricingQuantity 
>
> **2.28.2. Display Name**
>
> Pricing Quantity
>
> **2.28.3. Description**
>
> The volume of a given SKU associated with a *resource* or *service* used or purchased, based on the Pricing Unit. 
>
> **2.28.4. Content Constraints Constraint**
> 
> <img width="492" alt="image" src="https://github.com/user-attachments/assets/5185cbf9-306d-4663-a1c7-c8b7ab5c5bb8">
>
> **2.28.5. Introduced (version)** 
>
> 1.0-preview

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
