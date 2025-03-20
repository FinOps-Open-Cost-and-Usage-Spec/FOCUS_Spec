# Column Normative Requirements Guidelines

## Grouping and Ordering of Requirements Groups

* Grouping and ordering of requirements ensure clarity, logical flow, and consistency across all columns, making related requirements easy to identify and follow. This structure should be maintained for consistency across the specification.

* **Note**: This section provides a current preview of the requirements grouping and ordering. Members should review how this applies to specific columns and provide feedback. The order may be adjusted based on that feedback.

  1. **Technical Requirements**
     1. **Presence**: Defines whether this column must exist in the dataset.
     2. **Data Type**: Establishes a foundational expectation, ensuring all subsequent rules align with this type.
     3. **Value Format**: Ensures the value (if present) adheres to specific structural or syntactic rules.
     4. **Nullability**: Clarifies when the value can or cannot exist, ensuring all subsequent rules align with column nullability.
     5. **Values and Value Ranges**: Further constrains valid values, assuming the format is already correct.
     6. **Column-to-Column Relationships**: Defines dependencies and consistency rules between related columns.
  2. **Business & Contextual Requirements**
     1. **Unit/Denomination**: Ensures consistency in measurement or currency.
     2. **Uniqueness**: Defines uniqueness constraints for data integrity.
     3. **Fallback/Substitute Values**: Specifies what alternative values may be used if the expected value is missing.
     4. **Relationships Outside the Spec**: Defines dependencies on external systems or datasets.
     5. **Cost Validation Rules:**
        1. **Formula-based Cost Validation (e.g., P × Q = C)**: Ensures calculated fields adhere to mathematical rules.
        2. **Cost Correction Discrepancies**: Disclaimer on discrepancies in unit pricing, pricing quantities, and costs, which can be addressed independently when ChargeClass is 'Correction'.
     6. **Cost Calculation and Relationships**: Defines how costs are calculated in specific use cases, including dependencies on related charges and alignment with other cost values.
     7. **Other**: Requirements that do not fall into one of the previous categories.

### Tabular Overview of Requirement Grouping and Specifications

| **Requirement Type** | **Requirement Group**              | **When required?**                    | **Example**                                                                                |
|----------------------|------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------|
| Technical            | Presence                           | Always                                | {ColumnId} MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when Condition. |
| Technical            | Data Type                          | Always                                | {ColumnId} MUST be of type String.                                                         |
| Technical            | Value Format                       | Always (except normalized dimensions) | {ColumnId} MUST conform to [StringHandling](#stringhandling) requirements.                 |
| Technical            | Nullability                        | Always                                | {ColumnId} MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when Condition.                     |
| Technical            | Values and Value Ranges            | Metrics and normalized dimensions     | {ColumnId} MUST be a valid decimal value.<br/>{ColumnId} MUST be one of the allowed values. |
| Technical            | Column to column Relationships     | When applicable                       | {ColumnId} SHOULD/MUST remain consistent over time for a given ReferencedColumnId.         |
| Business             | Unit/Denomination                  | When applicable                       | {ColumnId} MUST be denominated in the BillingCurrency.                                     |
| Business             | Uniqueness                         | When applicable                       | BillingAccountId MUST be a unique identifier within a provider.                            |
| Business             | Fallback/Substitute Values         | When applicable                       | {ColumnId} MUST NOT duplicate {OtherColumnId} when Condition.                              |
| Business             | Relationships Outside the Spec     | When applicable                       | The sum of {ColumnId} in a given billing period MUST match the sum of the invoices received for that billing period for a billing account. |
| Business             | Formula-based Cost Validation      | When applicable                       | The product of Column1 and Column2 MUST match the column3 when Condition.                  |
| Business             | Cost Correction Discrepancies      | When applicable                       | Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction". |
| Business             | Cost Calculation and Relationships | When applicable                       | When Condition, {ColumnId} adheres to the following additional requirements:<br>  * {ColumnId} of a charge calculated based on other charges (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the ContractedCost of those related charges.<br>  * {ColumnId} of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the BilledCost. |
| Business             | Other                              | When applicable                       |                                                                                           |

## Ordering of Requirements Within Groups

* Within each group of requirements, order individual requirements as follows:
  * **MUST** – an absolute requirement
  * **MUST NOT** – a prohibition
  * **SHOULD** – recommended but not mandatory
  * **RECOMMENDED** - recommended but not mandatory (currently used only for presence-related normative requirements, as specified in the [FOCUS Feature Level](#focusfeaturelevel) section)
  * **SHOULD NOT** – discouraged but not strictly prohibited
  * **MAY** – optional

* For detailed interpretation of keywords such as "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", and others, see [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)].

## Guidelines for Structuring Individual Requirements

* **Start with the ColumnId**: Whenever possible, begin each requirement with the ColumnId to make the requirement clear and focused.

  **Example Pattern 1**

  ```markdown
  * <ColumnId> MUST/MUST NOT/SHOULD/MUST be null when <Condition>.
  ```

* **Use {ColumnId} for Column and Value References**: Whenever possible, use {ColumnId} when referring to a column or its values.

* **Default to Singular Form**: Column references should be singular, with the understanding that the requirement applies to all values in the column.

### Additional Guidelines for Columns in Simplified JSON Format

#### Key-Value Pairs

* **References to Key-Value Pairs depend on the context**: The terminology for key-value pairs varies depending on the column and context. For instance, when referring to key-value pairs, **tags**, **user-defined tags**, and **provider-defined tags** are used in **Tags**, whereas **SkuPriceDetails property** is used in **SkuPriceDetails**.

* **Default to Plural for Key-Value Pairs**: When referring to key-value pairs, **tags** and **properties** should be used in the plural form to reflect the fact that the column may contain multiple key-value pairs.

#### Keys and Values

* **Refer to Key and Values Explicitly**: When specifying normative requirements for key and value, use precise terminology based on the column type. For instance:
  * In **Tags**, refer to **tag key** when addressing only the key, and **tag value** when addressing only the value.
  * In **SkuPriceDetails**, refer to **property key** when addressing only the key, and **property value** when addressing only the value.
  * When linking a key to its value, use **corresponding value**.

* **Start Key-Specific Requirements with the Key Term**: When a requirement applies to a key, it SHOULD begin with **tag key**, **property key**, or the applicable term for that column.

* **Start Value-Specific Requirements with the Value Term**: When a requirement applies to a value, it SHOULD begin with **tag value**, **property value**, or the applicable term for that column.

* **Default to Singular Form for Keys and Values**: Keys and values references should be singular, with the understanding that the requirement applies to all occurrences (e.g., "property key", "tag value", etc.).

## Grouping of Nullability-Related and Subsequent Normative Requirements

* When there is only one nullability-related requirement, state it directly. If there are multiple, list them as nested bullets under the introductory bullet 'ColumnId nullability is defined as follows:'

  **Example Pattern 1**

  ```markdown
  * <ColumnId> nullability is defined as follows:
    * <ColumnId> MUST be null when <Condition>.
    * <ColumnId> MUST NOT be null when <Condition>.
  ```

* When requirements follow conditional logic (e.g., "If... Else If... Else"), the order should be adjusted so that the most specific conditions appear first, while the most general requirement (e.g., a MUST or SHOULD) is placed last as the fallback rule ("In all other cases" clause).

  **Example Pattern 2**

  ```markdown
  * <ColumnId> nullability is defined as follows:
    * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
    * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
    * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null in all other cases.
  ```

  **Example Pattern 3**

  ```markdown
  * <ColumnId> nullability is defined as follows:
    * <ColumnId> MUST be null when <Condition>.
    * When <Condition>, <ColumnId> adheres to the following additional requirements:
      * <ColumnId> MUST NOT be null when <Condition>.
      * <ColumnId> MAY be null when <Condition>.
  ```

## Grouping of Requirements Based on Specific Conditions

* **Parent Condition**
  * When a specific condition (or set of conditions) applies to a subset of requirements, you may group them under that condition.
  * The requirement's bullet should start with the {Condition}, and the following requirements should begin with the {ColumnId}.
  * For conditions that apply to multiple nested requirements, use the following pattern:

  ```markdown
    When <Condition(s)>, <ColumnId> adheres to the following additional requirements:
  ```

  **Example Pattern 1**
  
  ```markdown
  * When <Condition>, <ColumnId> adheres to the following additional requirements:
    * <ColumnId> MUST NOT be null when <Condition>.
    * <ColumnId> MAY be null when <Condition>.
  ```

* **Nested Condition**
  * For nested conditions, if the parent condition already defines the adherence (e.g., {ColumnId} adheres to the following additional requirements), do not repeat this phrase. Simply state the nested condition, and then list the specific requirements for that condition under the nested bullet.

  **Example Pattern 2**

  ```markdown
  * When <Condition>, <ColumnId> adheres to the following additional requirements:
    * <ColumnId> MUST be a valid decimal value.
    * When <NestedCondition>:
      * <ColumnId> MUST be <SpecificRequirement>.
      * <ColumnId> MUST be <SpecificRequirement>.
  ```

## Consistent Wording and Patterns in Requirements

To ensure clarity and consistency across columns and requirements, it is important to:

* **Follow common requirement patterns where applicable**
* **Use standardized phrasing and terminology**

### Requirement Patterns

#### Technical Requirements: Presence

```markdown
* <ColumnId> MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* <CoumnId> MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when <Condition>.
* <ColumnId> is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when <Condition>.
```

#### Technical Requirements: Data Type

```markdown
* <ColumnId> MUST be of type String.
* <ColumnId> MUST be of type Decimal.
* <ColumnId> MUST be of type Date/Time.
```

#### Technical Requirements: Value Format

```markdown
* <ColumnId> MUST conform to [StringHandling](#stringhandling) requirements.
* <ColumnId> MUST conform to [Numeric Format](#numericformat) requirements.
* <ColumnId> MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* <ColumnId> SHOULD conform to [UnitFormat](#unitformat) requirements.
* <ColumnId> MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* <ColumnId> MUST conform to [CurrencyCodeFormat](#currencycodeformat) requirements.
```

#### Technical Requirements: Nullability

```markdown
* <ColumnId> MUST NOT be null.
```

```markdown
* <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
```

```markdown
* <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition1>.
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition2>.
```

```markdown
* <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST be null when <Condition>.
  * When <Condition>, the column adheres to the following additional requirements:
    * <ColumnId> MUST NOT be null when <Condition>.
    * <ColumnId> MAY be null when <Condition>.
```

```markdown
* <ColumnId> nullability is defined as follows:
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
  * <ColumnId> MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when <Condition>.
  * <ColumnId> MAY be null in all other cases.
```

```markdown
* <ColumnId> nullability is defined as follows:
  * When <Condition>, <ColumnId> adheres to the following additional requirements:
    * <ColumnId> MUST NOT be null when <Condition>.
    * <ColumnId> MAY be null when <Condition>.
  * <ColumnId> MUST be null in all other cases.
```

#### Technical Requirements: Values and Value Ranges

```markdown
* <ColumnId> MUST be a valid decimal value.
* <ColumnId> MUST be a non-negative decimal value.
```

#### Technical Requirements: Column-to-Column Relationships

```markdown
* <ColumnId> SHOULD/MUST remain consistent over time for a given <OtherColumnId>.
```

#### Business & Contextual Requirements: Unit/Denomination

```markdown
* <ColumnId> MUST be denominated in the BillingCurrency.
* <ColumnId> MUST be expressed in the <OtherColumnId>.
```

#### Business & Contextual Requirements: Uniqueness

```markdown
* <ColumnId> MUST be a unique identifier within <Scope>.
```

#### Business & Contextual Requirements: Fallback/Substitute Values

```markdown
* <ColumnId> MUST NOT duplicate <OtherColumnId> when <Condition>
```

#### Business & Contextual Requirements: Relationships Outside the Spec

```markdown
* The sum of <ColumnId> in a given billing period MUST/MAY NOT match the sum of the invoices received for that billing period for a billing account.
```

#### Business & Contextual Requirements: Cost Validation Rules

##### Formula-based Cost Validation

```markdown
* The product of <PricingQuantity|UnitPriceColumnId> and <UnitPriceColumnId|PricingQuantity> MUST match the <CostColumnId> when <Condition> and ChargeClass is not "Correction".
* The product of <PricingQuantity|UnitPriceColumnId> and <UnitPriceColumnId|PricingQuantity> MUST match the <CostColumnId> when <Condition1>, <Condition2>, and ChargeClass is not "Correction".
```

##### Cost Correction Discrepancies

```markdown
* Discrepancies in <MetricId1>, <MetricId2>, or <MetricId3> MAY be addressed independently when ChargeClass is "Correction".
```

#### Business & Contextual Requirements: Cost Calculation and Relationships

```markdown
* When <Condition>, <CostColumnId> adheres to the following additional requirements:
  * <CostColumnId> of a charge calculated based on other charges (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the <CostColumnId> of those related charges.
  * <CostColumnId> of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the BilledCost.
```

### Standardized Terminology

#### Identifiers and Uniqueness within Scope

* Patterns:
  * {ColumnId} MUST be a unique identifier within {Scope}.
  * {ColumnId} SHOULD be a fully-qualified identifier.
* Examples:
  * BillingAccountId MUST be a unique identifier within a provider.
  * ResourceId SHOULD be a fully-qualified identifier.

#### Column Aggregation

* Pattern: The sum of {ColumnId} in a given billing period...
* Example: The sum of BilledCost in a given billing period...

#### Column value Consistency

* Patterns:
  * {ColumnId} MUST/SHOULD remain consistent over time for a given {OtherColumnId}.
* Examples:
  * SkuMeter SHOULD remain consistent over time for a given SkuId.
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.

#### References to charge and billing periods

* Patterns:
  * in a given billing period
  * in a given charge period

#### Preferred Terminology for Numerical References

* Patterns: When specifying quantities in normative requirements, follow these conventions:
  * Use "one" instead of "1".
  * Use "more than one" instead of "2 or more".
* Examples:
  * When the provider has only one user-defined tag scheme. (instead of: When the provider has only 1 user-defined tag scheme.)
  * When the provider has more than one user-defined tag scheme. (instead of: When the provider has 2 or more user-defined tag schemes.)

## Examples

### **List Unit Price**

#### **List Unit Price v.1.2 (Simplified Refinement)**

The ListUnitPrice column adheres to the following requirements:

* **(Presence)** ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* **(Data Type)** ListUnitPrice MUST be of type Decimal.
* **(Value Format)** ListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
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

* ListUnitPrice MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider publishes unit prices exclusive of discounts.
* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#numericformat) requirements.
* ListUnitPrice nullability is defined as follows:
  * ListUnitPrice MUST be null when [ChargeCategory](#chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice adheres to the following additional requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.
  * The product of ListUnitPrice and [PricingQuantity](#pricingquantity) MUST match the [ListCost](#listcost) when PricingQuantity is not null and ChargeClass is not "Correction".
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY be addressed independently when ChargeClass is "Correction".

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
* BilledCost MUST conform to [NumericFormat](#numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of BilledCost in a given [*billing period*](#glossary:billing-period) MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

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
* CommitmentDiscountQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* CommitmentDiscountQuantity nullability is defined as follows:
  * When ChargeCategory is "Usage" or "Purchase" and CommitmentDiscountId is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
    * CommitmentDiscountQuantity MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountQuantity MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountQuantity MUST be null in all other cases.
* When CommitmentDiscountQuantity is not null, CommitmentDiscountQuantity adheres to the following additional requirements:
  * CommitmentDiscountQuantity MUST be a valid decimal value.
  * When ChargeCategory is "Purchase":
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term* when [ChargeFrequency](#chargefrequency) is "One-Time".
    * CommitmentDiscountQuantity MUST be the quantity of CommitmentDiscountUnit that is eligible for consumption for each *charge period* that corresponds with the purchase when ChargeFrequency is "Recurring".
  * When ChargeCategory is "Usage":
    * CommitmentDiscountQuantity MUST be the metered quantity of CommitmentDiscountUnit that is consumed in a given *charge period* when [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used".
    * CommitmentDiscountQuantity MUST be the remaining, unused quantity of CommitmentDiscountUnit in a given *charge period* when CommitmentDiscountStatus is "Unused".

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
