## Editorial Style Suggestions
This document provides editorial style suggestions for the FOCUS v1.0 specifications. It was created in response to a recent discussion about the need for a consistent and professional editorial style to enhance and harmonize FOCUS technical specifications. The guidelines outlined below aim to standardize the presentation of various elements such as **column names**, *column IDs*, [_glossary terms_](), **NORMATIVE KEYWORDS**, **`attribute names`**, *`attribute IDs`* and other key components of the FOCUS documentation.

1. **Column Names**
   - **Style**: **Bold**, (_with blank space for compound names_)
   - **Reasoning**: Column names should be easily distinguishable for quick reference and clarity.
   - **Example**: **Billing Account ID**, **Resource Name**

2. **Column IDs**
   - **Style**: *Italic*, (_without blank space for compound names, and compound words capitalized_)
   - **Reasoning**: Italicizing the column IDs helps differentiate them from the display names and other text, making it clear when referring to specific IDs.
   - **Example**: *BillingAccountId*, *ResourceName*

3. **Glossary Terms**
   - **Style**: [_Underlined_](), and capitalized
   - **Reasoning**: Underlining glossary terms makes them stand out, helping readers quickly locate definitions and understand terminology.
   - **Example**: [_Amortization_](), [_CommitmentDiscountId_]()

4. **Normative Statements (e.g., MUST, SHOULD, MAY)**
   - **Style**: **ALL CAPITALS** and **bold**
   - **Reasoning**: Using all capitals for normative terms emphasizes their importance and aligns with standard practice in technical specifications to indicate requirement levels. In alignment with [BCP14](https://www.rfc-editor.org/info/bcp14) [[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)][[RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)].
   - **Example**: **MUST**, **SHOULD**, **MAY**

5. **Descriptions and Content Constraints**
   - **Style**: Normal text, but ensure clear headings and subheadings
   - **Reasoning**: These sections should remain easily readable, with clear headings for each sub-section to facilitate navigation.
   - **Example**:
     - **Description**: A name assigned to a grouping of resources or services, often used to manage access and/or cost.
     - **Content Constraints**:
       - **Column type**: Dimension
       - **Feature level**: Conditional

6. **Attribute Names and IDs in Specifications**
   - **Style**: Attribute Names in **`Bold`**, Attribute IDs in *`Italic`*
   - **Reasoning**: This approach helps in visually distinguishing between attribute names and their respective IDs.
   - **Example**:
     - **Attribute Name**: **`Currency Code Format`**
     - **Attribute ID**: *`CurrencyCodeFormat`*

7. **Key-Value Format**
   - **Style**: <code>Monospaced font</code>
   - **Reasoning**: Using a monospaced font for key-value pairs ensures clarity and readability, especially for JSON or code snippets.
   - **Example**:
     ```json
     {
       "key1": "value1",
       "key2": true,
       "key3": 123
     }
     ```

8. **Tables and Lists**
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

9. **Highlighting Important Paragraphs**

    - **Style**: Markdown quote (>) symbol
    - **Reasoning**: Highlighting key paragraphs ensures they capture the reader's attention, emphasizing their importance within the document.
    - *Example*:

        > Important: Ensure all critical parameters are verified.

10. **Formatting Normative Statements as Bullet Lists**

    - **Style**: Bullet list format
    - **Reasoning**: Presenting normative statements in a bullet list format ensures clarity and facilitates quick scanning and comprehension.
    - **Example**:
    **ConsumedQuantity** and **ConsumedUnit**:
        * MUST NOT be null if ChargeCategory is "Usage", unless ChargeClass is "Correction" or CommitmentStatus is 'Unused'
        * MAY be null if ChargeCategory is "Usage" and ChargeClass is "Correction"
        * MUST be null if CommitmentStatus is 'Unused' or for other ChargeCategory values