## Editorial Style Suggestions




 **Tables and Lists**
   - **Style**: Use standard table formatting with clear column headings in bold.
   - **Reasoning**: Standard table formatting with bold headings improves readability and ensures that data is well-organized and easy to interpret.
   - **Example**:

     | **Constraint**      | **Value**            |
     |---------------------|----------------------|
     | Column type         | Dimension            |
     | Feature level       | Conditional          |
     | Allows nulls        | True                 |
     | Data type           | String               |
     | Value format        | Not specified        |


<table>
    <tr>
        <th>Editorial Type</th>
        <th>Display (PDF, HTML)</th>
        <th>Markdown (examples)</th>
        <th>Editorial Guidelines</th>
    </tr>
    <tr>
        <td>Column &amp; Attributes Names:</td>
        <td>
            <strong>Column Names:<br>
            Pricing Quantity<br>
            Pricing Unit<br><br>
            Attribute Names:<br>
            Currency Code Format<br>
            Date/Time Format</strong>
        </td>
        <td>
            **Pricing Quantity**<br>
            **Pricing Unit**<br><br>
            **Currency Code Format**<br>
            **Date/Time Format**<br>
        </td>
        <td>
            Bold <br>
            Use the display name in the non-normative section.<br>
            *The first occurrence in a new section is linked*
        </td>
    </tr>
    <tr>
        <td>Columns &amp; Attributes IDs:</td>
        <td>
           <strong>Columns IDs:<br>
            ChargeClass, ChargeCategory, PricingQuantity<br><br>
            Attributes IDs:<br>
            CurrencyCodeFormat, ChargeClass, ChargeCategory, PricingQuantity</strong>
        </td>
        <td>
            <strong>CurrencyCodeFormat</strong>
        </td>
        <td>
            Display normal text without italics.<br>
            The first occurrence in a new section is linked.
        </td>
    </tr>
    <tr>
        <td>Normative Keywords &amp; Statements</td>
        <td>
            MUST, MAY, MUST NOT and normative statements
        </td>
        <td>
            **ConsumedQuantity** and **ConsumedUnit**:<br>
            <ul>
                <li>* MUST NOT be null if ChargeCategory is "Usage", unless ChargeClass is "Correction" or CommitmentStatus is 'Unused'</li>
                <li>* MAY be null if ChargeCategory is "Usage" and ChargeClass is "Correction"</li>
            </ul>
        </td>
        <td>
            Uppercase, without bold.<br>
            Bullet list format<br>
            Presenting normative statements in a bullet list format ensures clarity and facilitates quick scanning and comprehension.
        </td>
    </tr>
    <tr>
        <td>Glossary</td>
        <td>
            SKU, resource, service
        </td>
        <td>
            [*service*](#glossary:service)
        </td>
        <td>
            Blue + italic<br>
            *link to the glossary of the first iteration in the section.
        </td>
    </tr>
    <tr>
        <td>Important Text</td>
        <td> <img width="492" alt="image" src="https://github.com/user-attachments/assets/c6f60ff9-1503-43a3-8229-004595b334d2"></td>
        <td>> Important Consideration</td>
        <td>It is added as a note.</td>
    </tr>
    <tr>
        <td>Key-Value Format</td>
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
        <td>Monospace font</td>
    </tr>
    <tr>
      <td>Tables</td>
      <td><img width="492" alt="image" src="https://github.com/user-attachments/assets/5185cbf9-306d-4663-a1c7-c8b7ab5c5bb8"></td>
      <td><img width="492" alt="image" src="https://github.com/user-attachments/assets/83d0977f-a731-4def-93e3-b3e5f5dedb72">
      <td>Tables</td>
</td>
    </tr>
</table>
