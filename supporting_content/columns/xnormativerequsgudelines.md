# Column Normative Requirements Guidelines

## Grouping and Ordering of Requirements

* Grouping and ordering of requirements ensure clarity, logical flow, and consistency across all columns, making related requirements easy to identify and follow. The order established in the cookbook should be used for consistency across specifications. See the cookbook for the exact sequence, but generally:

* **Note**: This section provides a current preview of the requirements grouping and ordering as established in the cookbook. Members should review how this applies to specific columns and provide feedback. The order may be adjusted based on that feedback.

  1. **Technical Requirements**
     1. **Presence of the Column**: Defines whether this column must exist in the dataset.
     2. **Data Type**: Establishes a foundational expectation, ensuring all subsequent rules align with this type.
     3. **Value Format**: Ensures the value (if present) adheres to specific structural or syntactic rules.
     4. **Nullability**: Clarifies when the value can or cannot exist, ensuring all subsequent rules align with column nullability.
     5. **Values and Value Ranges**: Further constrains valid values, assuming the format is already correct.
     6. **Column-to-Column Relationships**: Defines dependencies and consistency rules between related columns.
        * Example:
          * *ColumnId SHOULD/MUST remain consistent over time for a given ReferencedColumnId.*

  2. **Business & Contextual Requirements**
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
        1. **Formula-based Cost Validation (e.g., P × Q = C)**: Ensures calculated fields adhere to mathematical rules.
        2. **Cost Correction Discrepancies**: Disclaimer on discrepancies in unit pricing, pricing quantities, and costs, which can be addressed independently when ChargeClass is 'Correction'.
     6. **Cost Calculation and Relationships**: Defines how costs are calculated in specific use cases, including dependencies on related charges and alignment with other cost values.
     7. **Other**

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
    * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null in all other cases.
  ```

  **Example 2:**

  ```markdown
  * <ColumnId> nullability is defined as follows:
    * <ColumnId> MUST be null when <Condition>.
    * When <Condition>, <ColumnId> adheres to the following additional requirements:
      * <ColumnId> MUST NOT be null when <Condition>.
      * <ColumnId> MAY be null when <Condition>.
  ```

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

## Consistent Wording and Patterns in Requirements

To ensure clarity and consistency across columns and requirements, it is important to:

* **Use standardized phrasing and terminology**  
* **Follow common requirement patterns where applicable**  

**Note:** Refer to the cookbook for a set of recognized requirement patterns and commonly used phrasing.

## Examples

### **List Unit Price**

#### **List Unit Price v.1.2 (Simplified Refinement)**

The ListUnitPrice column adheres to the following requirements:

* **(Presence)** ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* **(Data Type)** ListUnitPrice MUST be of type Decimal.
* **(Value Format)** ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* **(Nullability - Definition)** ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* **(Nullability - Conditional)** When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * **(Values and Value Ranges)** ListUnitPrice MUST be a non-negative decimal value.
  * **(Unit/Denomination)** ListUnitPrice MUST be denominated in the BillingCurrency.
  * **(Formula-based Cost Validation)** The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
  * **(Cost Correction Discrepancies)** Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

---
The ListUnitPrice column adheres to the following requirements:

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

#### **List Unit Price v.1.2 (Technical Refinement)**

The ListUnitPrice column adheres to the following requirements:

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* If present, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be of type Decimal.
  * ListUnitPrice MUST conform to [Numeric Format](#numericformat) requirements.
  * If [ChargeCategory](#chargecategory) is "Tax", ListUnitPrice adheres to the following additional requirement:
    * ListUnitPrice MUST be null.
  * Else if ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction", ListUnitPrice adheres to the following additional requirement:
    * ListUnitPrice MUST NOT be null.
  * Else ListUnitPrice adheres to the following additional requirement:
    * ListUnitPrice MAY be null.
  * If ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
    * ListUnitPrice MUST be a non-negative decimal value.
    * ListUnitPrice MUST be denominated in the BillingCurrency.
    * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) if PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently if ChargeClass is "Correction".

#### **List Unit Price v.1.1 (Original)**

The ListUnitPrice column adheres to the following requirements:

* The ListUnitPrice column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* This column MUST be a Decimal within the range of non-negative decimal values, MUST conform to [Numeric Format](#numericformat) requirements, and be denominated in the BillingCurrency.
* It MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction" and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", MUST be null when ChargeCategory is "Tax", and MAY be null for all other combinations of ChargeClass and ChargeCategory.
* When ListUnitPrice is present and is not null, multiplying ListUnitPrice by [PricingQuantity](#pricingquantity) MUST equal [ListCost](#listcost), except in cases of ChargeClass "Correction", which may address PricingQuantity or any cost discrepancies independently.

### **Billed Cost**

#### **Billed Cost v.1.2 (Simplified Refinement)**

The BilledCost column adheres to the following requirements:

* BilledCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [Numeric Format](#numericformat) requirements.
* BilledCost nullability is defined as follows:
  * BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of the BilledCost for [*rows*](#glossary:row) in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

#### **Billed Cost v.1.2 (Technical Refinement)**

The BilledCost column adheres to the following requirements:

* BilledCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [Numeric Format](#numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of the BilledCost for [*rows*](#glossary:row) in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

#### **Billed Cost v.1.1 (Original)**

The BilledCost column adheres to the following requirements:

* The BilledCost column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and MUST NOT be null.
* This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency.
* The sum of the BilledCost for [*rows*](#glossary:row) in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

### **CommitmentDiscountQuantity**

#### **CommitmentDiscountQuantity v.1.2 (Simplified Refinement)**

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountQuantity MUST be of type Decimal.
* CommitmentDiscountQuantity MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountQuantity nullability is defined as follows:
  * When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountQuantity MUST be null in all other cases.
* When CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountQuantity MUST be a valid decimal value.
  * When ChargeCategory is "Purchase", CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [ChargeFrequency](#chargefrequency) is "One-Time".
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
  * When ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnits that is consumed over the *row's* *charge period* when [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
    * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnits for the *row's* *charge period* when CommitmentDiscountStatus is "Unused".

#### **CommitmentDiscountQuantity v.1.2 (Technical Refinement)**

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* If present, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountQuantity MUST be of type Decimal.
  * CommitmentDiscountQuantity MUST conform to [Numeric Format](#numericformat) requirements.
  * If ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST NOT be null if [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountQuantity MAY be null if ChargeClass is "Correction".
  * Else CommitmentDiscountQuantity adheres to the following additional requirement:
    * CommitmentDiscountQuantity MUST be null.
  * If CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST be a valid decimal value.
    * If ChargeCategory is "Purchase", CommitmentDiscountQuantity adheres to the following additional requirements:
      * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* if [ChargeFrequency](#chargefrequency) is "One-Time".
      * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnits that is eligible for consumption for each *charge period* that corresponds with the purchase if ChargeFrequency is "Recurring".
    * If ChargeCategory is "Usage", CommitmentDiscountQuantity adheres to the following additional requirements:
      * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnits that is consumed over the *row's* *charge period* if [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
      * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnits for the *row's* *charge period* if CommitmentDiscountStatus is "Unused".

#### **CommitmentDiscountQuantity v.1.1 (Original)**

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountQuantity MAY be null or any valid decimal value if [*CommitmentDiscountId*](#commitmentdiscountid) is not null and [*ChargeClass*](#chargeclass) is "Correction".

In cases where the ChargeCategory is "Purchase", CommitmentDiscountId is not null, and ChargeClass is not "Correction", the following applies:

* When [ChargeFrequency](#chargefrequency) is "One-Time", and CommitmentDiscountId is not null, CommitmentDiscountQuantity MUST be the positive quantity of CommitmentDiscountUnits, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term*.
* When ChargeFrequency is "Recurring", and CommitmentDiscountId is not null, CommitmentDiscountQuantity MUST be the positive quantity of CommitmentDiscountUnits that is eligible for consumption for each *charge period* that corresponds with the purchase.

In cases where the ChargeCategory is "Usage", CommitmentDiscountId is not null, and ChargeClass is not "Correction", the following applies:

* When [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used", CommitmentDiscountQuantity MUST be the positive, metered quantity of CommitmentDiscountUnits that is consumed over the *row's* *charge period*.
* When CommitmentDiscountStatus is "Unused", CommitmentDiscountQuantity MUST be the remaining, positive, unused quantity of CommitmentDiscountUnits for the *row's* *charge period*.

CommitmentDiscountQuantity MUST be null in all other cases.
