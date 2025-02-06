# Column Normative Requirements Guidelines

## Grouping and Ordering of Requirements

* Grouping and ordering of requirements ensure clarity, logical flow, and consistency across all columns, making related requirements easy to identify and follow. The order established in the cookbook should be used for consistency across specifications. See the cookbook for the exact sequence, but generally:

  1. **Technical (Actionable) Requirements**
     1. **Presence of the Column**: Defines whether this column must exist in the dataset.
     2. **Data Type**: Establishes a foundational expectation, ensuring all subsequent rules align with this type.
     3. **Value Format**: Ensures the value (if present) adheres to specific structural or syntactic rules.
     4. **Nullability**: Clarifies when the value can or cannot exist, ensuring all subsequent rules align with column nullability.
     5. **Values and Value Ranges**: Further constrains valid values, assuming the format is already correct.
     6. **Column-to-Column Relationships**: Defines dependencies and consistency rules between related columns.
        * Example:
          * *ColumnId SHOULD/MUST remain consistent over time for a given ReferencedColumnId.*

  2. **Business & Contextual Requirements ("Non-Actionable")**
     1. **Unit/Denomination**: Ensures consistency in measurement or currency.
        * Example:
          * *ColumnId MUST be denominated in the BillingCurrency.*
     2. **Uniqueness**: Defines uniqueness constraints for data integrity.
        * Examples:
          * *BillingAccountId MUST be a globally unique identifier within a provider.*
          * *BillingAccountName MUST be unique within a customer.*
     3. **Fallback/Substitute Values**: Specifies what alternative values may be used if the expected value is missing.
     4. **Relationships Outside the Spec**: Defines dependencies on external systems or datasets.
     5. **Cost Validation Rules:**
        * Note: Consider relocating this to the Technical Requirements section!!!
        1. **Formula-based Cost Validation (e.g., P × Q = C)**: Ensures calculated fields adhere to mathematical rules.
        2. **Cost Correction Discrepancies**: Disclaimer on discrepancies in unit pricing, pricing quantities, and costs, which can be addressed independently when ChargeClass is 'Correction'.
     6. **Cost Calculation and Relationships**: Defines how costs are calculated in specific use cases, including dependencies on related charges and alignment with other cost values.
     7. **Other**

  * **Note**: This section provides a current preview of the requirements grouping and ordering as established in the cookbook. Members should review how this applies to specific columns and provide feedback. The order may be adjusted based on that feedback.

* Within each group of requirements, order individual requirements as follows:
  * **MUST** – an absolute requirement
  * **MUST NOT** – a prohibition
  * **SHOULD** – recommended but not mandatory
  * **SHOULD NOT** – discouraged but not strictly prohibited
  * **MAY** – optional

* When requirements follow conditional logic (e.g., "If... Else If... Else"), the order should be adjusted so that the most specific conditions appear first, while the most general requirement (e.g., a MUST or SHOULD) is placed last as the fallback rule ("In all other cases" clause).

  **Example 1:**

  ```markdown
  * <ColumnId> nullability is defined as follows:
    * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
    * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
    * In all other cases, <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null.
  ```

  **Example 2:**

  ```markdown
  * <ColumnId> nullability is defined as follows:
    * <ColumnId> MUST be null when <Condition>.
    * When <Condition>, <ColumnId> adheres to the following additional requirements:
      * <ColumnId> MUST NOT be null when <Condition>.
      * <ColumnId> MAY be null when <Condition>.
  ```

### Examples

#### List Unit Price

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * In all other cases, ListUnitPrice MAY be null.
* **(DISCARD?)** When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) if PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

---

* **(Presence)** ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* **(Data Type)** ListUnitPrice MUST be of type Decimal.
* **(Value Format)** ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* **(Nullability - Definition)** ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * In all other cases, ListUnitPrice MAY be null.
* **(DISCARD?: Nullability - Conditional)** When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * **(Values and Value Ranges)** ListUnitPrice MUST be a non-negative decimal value.
  * **(Unit/Denomination)** ListUnitPrice MUST be denominated in the BillingCurrency.
  * **(Formula-based Cost Validation)** The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) if PricingQuantity is not null and ChargeClass is not "Correction".
  * **(Cost Correction Discrepancies)** Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

---

* **(Presence)** ListUnitPrice MUST be present in a FOCUS dataset when the provider publishes unit prices exclusive of discounts.
* **(Data Type)** ListUnitPrice MUST be of type Decimal.
* **(Nullability - Definition)** ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when ChargeCategory is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and ChargeClass is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* **(Nullability - Conditional)** When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST conform to Numeric Format requirements.
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ListUnitPrice and PricingQuantity MUST match the ListCost if PricingQuantity is not null and ChargeClass is not "Correction".
* **(Other Logical Requirements)** Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

## Guidelines for Structuring Individual Requirements

* **Start with the ColumnId**: Whenever possible, begin each requirement with the ColumnId to make the requirement clear and focused.

  **Example 3:**

  ```markdown
  * <ColumnId> MUST/MUST NOT/SHOULD/MUST be null when <Condition>.
  ```

* **Group related requirements by condition**: When a subset of requirements applies to a specific condition, you may group them under that condition. The requirement's bullet should then start with the condition, and nested requirements should begin with the ColumnId.

  **Example 4:**
  
  ```markdown
  * When <Condition>, <ColumnId> adheres to the following additional requirements:
    * <ColumnId> MUST NOT be null when <Condition>.
    * <ColumnId> MAY be null when <Condition>.
  ```

### Brief Description of Examples

* **Example 1**: This example illustrates how to define **nullability** for a column. It starts by clearly stating the nullability conditions and outlines the requirements for each condition. It includes a fallback "In all other cases" clause.
  
* **Example 2**: This example demonstrates the use of **nested requirements** under a specific condition. It shows how a main condition can group specific requirements, which are then elaborated with nested bullets beginning with the <ColumnId.

## Consistent Wording and Patterns in Requirements

To ensure clarity and consistency across columns and requirements, it is important to:

* **Use standardized phrasing and terminology**  
* **Follow common requirement patterns where applicable**  

**Note:** Refer to the cookbook for a set of recognized requirement patterns and commonly used phrasing.
