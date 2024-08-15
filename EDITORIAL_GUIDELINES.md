## Editorial Style Suggestions



<table>
    <tr>
        <th>Editorial Type</th>
        <th>Display (PDF, HTML)</th>
        <th>Markdown (examples)</th>
        <th>Editorial Guidelines</th>
    </tr>
    <tr>
        <td><strong>Column &amp; Attributes Names</strong>:</td>
        <td>
            <strong>Column Names</strong>:<br>
            - <strong>Pricing Quantity</strong><br>
            - <strong>Pricing Unit</strong><br>
            - <strong>Provider</strong> <br><br>
            <strong>Attribute Names</strong>:<br>
            - <strong>Currency Code Format</strong><br>
            - <strong>Date/Time Format</strong>
        </td>
        <td>
            <strong>Column Names</strong>:<br>
            &nbsp;&nbsp; **Pricing Quantity**<br>
            &nbsp;&nbsp; **Pricing Unit**<br>
            &nbsp;&nbsp; **Provider**<br><br>
            <strong>Attribute Names</strong>:<br>
            &nbsp;&nbsp; **Currency Code Format**<br>
            &nbsp;&nbsp; **Date/Time Format**<br>
        </td>
        <td>
            - Bold <br>
            - Use the display name in the non-normative section.<br>
            - The first occurrence in a new section is linked
        </td>
    </tr>
    <tr>
        <td><strong>Columns &amp; Attributes IDs:</strong></td>
        <td>
           <strong>Columns IDs</strong>:<br>
            - PricingQuantity</strong><br> 
            - PricingUnit</strong><br> 
            - ProviderName</strong> <br><br>
          <strong>Attributes IDs</strong>:<br>
            - CurrencyCodeFormat <br> 
            - DateTimeFormat <br>
        </td>
        <td>
          <strong>Columns IDs:</strong>:<br>
          &nbsp;&nbsp; PricingQuantity <br>
          &nbsp;&nbsp; PricingUnit</strong><br>
          &nbsp;&nbsp; ProviderName</strong> <br><br>
          <strong>Attributes IDs:</strong> </br>
          &nbsp;&nbsp; CurrencyCodeFormat </br>
          &nbsp;&nbsp; DateTimeFormat <br>
        </td>
        <td>
           - Display normal text without italics.<br>
           - The first occurrence in a new section is linked.
        </td>
    </tr>
    <tr>
        <td><strong>Normative Keywords &amp; Statements</strong></td>
        <td>
            MUST, MAY, MUST NOT and normative statements
        </td>
        <td>
            ConsumedQuantity and ConsumedUnit:<br>
            <ul>
                <li>MUST NOT be null if ChargeCategory is "Usage", unless ChargeClass is "Correction" or CommitmentStatus is 'Unused'</li>
                <li>MAY be null if ChargeCategory is "Usage" and ChargeClass is "Correction"</li>
            </ul>
        </td>
        <td>
           - Uppercase, without bold.<br>
           - Bullet list format<br>
           - Presenting normative statements in a bullet list format ensures clarity and facilitates quick scanning and comprehension.
        </td>
    </tr>
    <tr>
        <td><strong>Glossary</strong></td>
        <td>
            [SKU](), [resource](), [service]()
        </td>
        <td>
            [*SKU*](#glossary:sku) <br>
            [*resource*](#glossary:resource) <br>
            [*service*](#glossary:service) <br>
        </td>
        <td>
            - Blue + italic<br>
            - link to the glossary of the first iteration in the section.
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
      <td> - Tables</td>
    </tr>
</table>

### Editorial Notes
* > **Linking Only the First Time**: To prevent excessive linking within sections, Column Name, Column ID, Attributes Names, Attributes IDs, and Glossary will only be linked to their corresponding description section or description the first time they appear in a new section.
* > **Normative Requirements as a Bullet List**: Normative statements (those using Normative Keywords) should be written as bullet points instead of lengthy sentences. 

### Example

>**2.28. Pricing Quantity**
>
>The Pricing Quantity represents the volume of a given SKU associated with a resource or service used or purchased, based on the Pricing Unit. Distinct from Consumed Quantity (complementary to Consumed Unit), it focuses on pricing and cost, not resource and service consumption. 
>
  * >The PricingQuantity column MUST be present in the billing data. 
  * > This column MUST be of type Decimal and MUST conform to Numeric Format requirements. 
  * > The value MAY be negative in cases where ChargeClass is "Correction". 
* > This column:
  * > MUST NOT be null when ChargeClass is not "Correction" and ChargeCategory is "Usage" or "Purchase", 
  * > MUST be null when ChargeCategory is "Tax", and 
  * > MAY be null for all other combinations of ChargeClass and ChargeCategory. 
* > When unit prices are not null, multiplying PricingQuantity by a unit price MUST produce a result equal to the corresponding cost metric, except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.
>
> **2.28.1. Column ID**
> PricingQuantity 
>
> **2.28.2. Display Name**
> Pricing Quantity
>
> **2.28.3. Description**
> The volume of a given SKU associated with a resource or service used or purchased, based on the Pricing Unit. 
>
> **2.28.4. Content Constraints Constraint**
> 
> <img width="492" alt="image" src="https://github.com/user-attachments/assets/5185cbf9-306d-4663-a1c7-c8b7ab5c5bb8">
>
> **2.28.5. Introduced (version)** 
> 1.0-preview
