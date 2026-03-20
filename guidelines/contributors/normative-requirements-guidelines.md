# Normative Requirements Guidelines

This section defines guidelines for authoring normative requirements in the FOCUS specification. These guidelines define **how** to write normative requirements to ensure clarity, consistency, and testability. It does not define the requirements themselves (the "what") but concentrates on their **structure, subjects, and verifiability**.

The guidelines cover authoring of normative requirements for the following entities:

* **FOCUS datasets** — the primary containers of structured data as defined in FOCUS.
* **FOCUS columns** — individual columns within FOCUS datasets, defined by FOCUS (may contain nested objects and object properties, which can have additional normative rules).
* **Custom columns** — individual columns within FOCUS datasets, not defined by FOCUS.
* **FOCUS attributes** — reusable sets of normative constraints that datasets, columns, or column sub-elements (such as objects and object properties) conform to; guidelines cover how to author requirements within Attribute sections.

The diagram below illustrates the relationships among these entities and shows where normative requirements apply:

```mermaid
erDiagram
Dataset ||--|{ Column : has
Column ||--o{ Object : contains
Object ||--|{ ObjectProperty : has
Dataset }|..|| Attribute : conforms-to
Column }|..|| Attribute : conforms-to
ObjectProperty }|..|| Attribute : conforms-to

%% Attribute
style Attribute fill:#f8d7da,stroke:#666,stroke-width:1px

%% Schema-level entities
style Dataset fill:#d4edda,stroke:#666,stroke-width:1px
style Column fill:#d4edda,stroke:#666,stroke-width:1px
style Object fill:#d4edda,stroke:#666,stroke-width:1px
style ObjectProperty fill:#d4edda,stroke:#666,stroke-width:1px
```

**Nodes:**

* 🟩 FOCUS schema-level entity (normative subject)
* 🟥 FOCUS normative rule set (not a normative subject)

**Relationships:**

* `|| -- has -- |{` : one parent to one-or-more enumerated structural members
* `|| -- contains -- o{` : one parent to zero-or-more child entities (array of objects)
* `}| .. conforms-to .. ||` : many children to one parent conformance relationship

> **Important clarification**

By glossary definition, the following concepts are used:

* **FOCUS Dataset** — the primary dataset concept defined by the FOCUS specification.
* **Dataset Instance** — represents a concrete instantiation of a **FOCUS Dataset Instance**.
* **Dataset Artifact** — represents a physical or delivered form of a **FOCUS Dataset Instance Artifact**.

However, by design decision, the specification adopts the following normative conventions:

* **FOCUS Dataset is used as the canonical normative subject** for dataset-level requirements.
* Normative requirements are intentionally written against **FOCUS Dataset**, even when the constraint applies to:
  * a dataset specification,
  * a dataset instance, or
  * a dataset instance artifact.
* The intended level of application (specification vs. instance vs. artifact) is inferred from context rather than encoded in the normative subject.

This choice is intentional and overrides interpretations based solely on abstraction level.

## 1. Core Normative Authoring Rules

### 1.1. Normative Requirement Structure

The recommended pattern for a normative requirement is:

``` markdown
<Subject (+qualifier)> + <BCP 14 Keyword> + <Verifiable State Descriptor> + <Object (+qualifier)> [+ Conditions]
```

* Each normative requirement MUST:
  * identify exactly one **normative subject** to which the requirement applies
  * contain exactly one **BCP 14 keyword** (MUST, SHOULD, MAY, MUST NOT, etc.), indicating the obligation level
  * express exactly one **verifiable constraint**
* Each normative requirement SHOULD describe a **verifiable state** of the object rather than behavior

### 1.2. Structural Anchor Requirement

Each Requirements section for a schema-level construct MUST begin with a single **structural anchor requirement**.

The structural anchor requirement:

* introduces the scope of the subsequent normative requirements,
* MUST appear as the first normative statement in the section,
* exists to support automated parsing and validation, and
* is non-verifiable and does not introduce an enforceable constraint.

The canonical form of a structural anchor requirement is:

``` markdown
<Entity> MUST adhere to the following requirements:
```

For **Attribute Requirements** sections, a different canonical form applies:

``` markdown
[Dataset|Column] conforming to <AttributeId> attribute MUST adhere to the following requirements:
```

See [Section 4.2. Structural Anchor Requirement for Attributes](#42-structural-anchor-requirement-for-attributes) for details.

### 1.3. Normative Subject

#### 1.3.1. Allowed Subjects

The normative subject MUST be a schema-level entity, such as:

* **FOCUS Dataset**, whereby use of:  
  * `FOCUS dataset` keyword represents any FOCUS dataset  
  * `FOCUS dataset` keyword with a qualifier represents a qualified subset of FOCUS datasets  
  * A single FOCUS dataset explicitly identified by `<FOCUS Dataset ID>` (e.g., `CostAndUsage`)

* **FOCUS Column**, whereby use of:  
  * `FOCUS column` keyword represents any FOCUS column  
  * `FOCUS column` keyword with a qualifier represents a qualified subset of FOCUS columns (e.g., `FOCUS column containing numeric values`)  
  * A single FOCUS column explicitly identified by `<FOCUS Column ID>` (e.g., `BilledCost`)

* **Custom Column**, whereby use of:  
  * `Custom column` keyword represents any custom column  
  * `Custom column` keyword with a qualifier represents a qualified subset of custom columns (e.g., `Custom column containing numeric values`)

* **Structural sub-elements within Columns** (objects, keys, key values):  
  *Note: MUST NOT use `object`, `key`, or `value` keywords alone. Always reference them in context, e.g.:*  
  * `Object in Columns containing JsonObjectFormat values`  
  * `Key in Object in FOCUS/Custom column containing JsonObjectFormat values`  
  * `Key value in Object in FOCUS/Custom column containing key-value pairs`

The subject SHOULD be explicit and unambiguous.

#### 1.3.2. Disallowed Subjects

The following MUST NOT be used as normative subjects:

* Actors (e.g. data generator, service provider, consumer)
* Processes or mechanisms (e.g. Delivery Handling, Correction Handling, etc.)

### 1.4. State, Not Behavior

Normative requirements MUST describe a **verifiable state**, not an operational process or behavior.

Specifically:

* Process-oriented verbs such as *ensure*, *handle*, *support*, or *provide* MUST NOT be used.
* If a requirement refers to actor behavior, it MUST be expressed as:
  * a constraint on the resulting dataset state, or
  * a constraint on a schema-defined artifact.

### 1.5. Use of BCP 14 Keywords

* Each normative bullet MUST contain exactly one BCP 14 keyword (MUST, SHOULD, MAY, MUST NOT, SHOULD NOT). See [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)].
* A bullet containing more than one normative keyword MUST be split.

### 1.6. Splitting Requirements

A requirement MUST be split into multiple bullets if it:

* combines multiple obligations,
* combines a rule and an exception,
* mixes a definition with a constraint,
* applies different constraints to different subjects.

### 1.7. Composite Requirements

Composite (parent + nested) requirements MAY be used when strictly controlled.

Composite requirements MUST adhere to the following requirements:

* Nested bullets MUST share the same condition if defined by the parent bullet.
* Nested bullets SHOULD NOT introduce a different subject.
* When nested bullets introduce different subjects, all subjects SHOULD be of the same subject type (e.g., FOCUS columns).

Composite requirements SHOULD be used when grouping improves readability and:

* multiple requirements share the same subject, or
* multiple requirements share the same business context (e.g., all requirements related to a specific business scenario or feature)

Flat parallel bullets SHOULD be preferred when ordering keyword is sufficient for clarity and readability.

### 1.8. Definitions vs. Normative Requirements

* Definitions, explanations, rationale, and examples MUST NOT be expressed as normative requirements.
* Definitions SHOULD be written as plain declarative statements without BCP 14 keywords.
* Normative bullets SHOULD be reduced to the enforceable constraint only.

### 1.9. DRY (Don't Repeat Yourself) Principle

Each normative requirement MUST be defined in exactly one place across the specification. The following rules determine where a requirement belongs:

* If a requirement applies broadly to multiple datasets, columns, or column sub-elements (e.g., objects within columns), it SHOULD be defined as an Attribute requirement, with conformance declared by those entities.

* If a requirement involves multiple columns within a single dataset, it MUST be defined on the primary column it describes. Other columns involved MUST NOT restate it as a normative requirement but MAY reference it in their introductory description.

  *Example: `ListCost MUST equal the product of ListUnitPrice and PricingQuantity when ListUnitPrice is not null and PricingQuantity is not null.` — this requirement is defined on ListCost. ListUnitPrice and PricingQuantity MAY reference it in their introductory description but MUST NOT restate it as a normative requirement.*

* If a requirement spans multiple datasets, it MUST be defined on the column in the dataset that is the primary owner of the validation. Other datasets involved MUST NOT restate it as a normative requirement but MAY reference it in their introductory description.

  *Example: A cross-dataset sum validation comparing BilledCost aggregated by InvoiceId and InvoiceIssuerName between InvoiceDetail and CostAndUsage is defined on InvoiceDetail.BilledCost, as InvoiceDetail is the primary owner of invoice-level validation. CostAndUsage MAY reference it in its introductory description but MUST NOT restate it as a normative requirement.*

## 2. Dataset Requirements

### 2.1. Logical Grouping of Dataset Requirements

Grouping and ordering of dataset-level normative requirements ensures clarity, consistency, and maintainability across all FOCUS datasets, making related or similar requirements easy to identify and follow.

  1. **Technical Requirements**
     1. **Dataset Presence:** Defines whether, and under what conditions, a dataset must be present in the FOCUS delivery.
     2. **Column Presence in Dataset:** Intended to define which columns must or are recommended to be present within a dataset, and under which conditions.
     3. **Technical Attributes Conformance:** Captures technical requirements that apply to all (or most) columns within the dataset (e.g., column handling, null handling). These requirements reflect general technical rules rather than rules for individual columns.
  2. **Business & Contextual Requirements**
     1. **Business/Contextual Attributes Conformance:** Captures business logic and contextual requirements that span multiple columns within the dataset (e.g., discount handling, invoice handling). These rules are not tied to a single column but define broader dataset behavior.
     2. **Other Business/Contextual Requirements (*FOR FUTURE USE*):** Captures additional dataset-level rules that do not fall into the above categories but are relevant for interpretation, validation, or integration.

#### Tabular Overview of Dataset Normative Requirement Grouping and Specifications

| Requirement Type | Requirement Group                                      | When Required?                               | Example                                                    |
|------------------|--------------------------------------------------------|----------------------------------------------|------------------------------------------------------------|
| Technical        | Dataset Presence                                       | Always                                       | {DatasetId} MUST be present when {Condition}.              |
| Technical        | Column Presence in Dataset                             | {DatasetId} MUST include {ColumnId} | N/A                                                        |
| Technical        | Technical Attributes Conformance                       | Always or when applicable                    | {DatasetId} MUST conform to ColumnHandling requirements.   |
| Business         | Business/Contextual Attributes Conformance             | When applicable                              | {DatasetId} MUST conform to DiscountHandling requirements. |
| Business         | Other Business/Contextual Requirements (FOR FUTURE USE)| For future use                               | N/A                                                        |

### 2.2. Ordering of Dataset Requirements Within Groups

To further enhance readability, individual requirements within each group SHOULD be ordered as follows:

* **MUST** – an absolute requirement
* **MUST NOT** – a prohibition
* **SHOULD** – recommended but not mandatory
* **SHOULD NOT** – discouraged but not strictly prohibited
* **MAY** – optional
* **MAY NOT** – optional prohibition / permitted not to

> ***Important Note:*** *The term **RECOMMENDED** (recommended but not mandatory; previously used only for presence-related normative requirements) is no longer permitted for use in normative requirements as of December 2025. The keyword **SHOULD** must be used instead. Please refer to the [**Editorial Style Guidelines**](editorial-guidelines.md).*

* For detailed interpretation of keywords such as "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", and others, see [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)].

### 2.3. Structuring Individual Dataset Requirements

* **Start with the DatasetId**: Whenever possible, begin each requirement with the DatasetId to make the requirement clear and focused.

  **Example Pattern 1**

  *Note: Text in square brackets [ ] indicates optional elements that apply only under certain conditions.*

  ```markdown
  * <DatasetId> MUST be present[ when <Condition>].
  ```

### 2.4. Consistent Wording and Patterns in Dataset Requirements

Use standardized phrasing and terminology, and apply common requirement patterns where applicable to ensure clarity and consistency across datasets and corresponding requirements.

#### 2.4.1. Dataset Requirement Patterns

##### 2.4.1.1. Technical Requirements: Dataset Presence

```markdown
* <DatasetId> MUST be present[ when <Condition>].
```

##### 2.4.1.2. Technical Requirements: Column Presence

```markdown
* <DatasetId> MUST include <ColumnId>.
* <DatasetId> MUST include <ColumnId> when <Condition>.
* <DatasetId> SHOULD include <ColumnId>.
* <DatasetId> SHOULD include <ColumnId> when <Condition>.
```

##### 2.4.1.3. Technical Requirements: Technical Attributes Conformance

```markdown
* <DatasetId> MUST conform to <TechnicalAttributeId> requirements.
```

##### 2.4.1.4. Business Requirements: Business/Contextual Attributes Conformance

```markdown
* <DatasetId> MUST conform to <BusinessAttributeId> requirements.
```

### 2.5. Dataset Normative Requirements Examples

#### 2.5.1. **Contract Commitment**

ContractCommitment MUST adhere to the following requirements:

* ContractCommitment MUST be present when the provider supports *contract commitments*.
* ContractCommitment MUST conform to [ColumnHandling](#columnhandling) requirements.
* ContractCommitment MUST conform to [NullHandling](#nullhandling) requirements.

#### 2.5.2. **Cost and Usage**

CostAndUsage MUST adhere to the following requirements:

* CostAndUsage MUST be present.
* CostAndUsage MUST conform to [ColumnHandling](#columnhandling) requirements.
* CostAndUsage MUST conform to [NullHandling](#nullhandling) requirements.
* CostAndUsage MUST conform to [DiscountHandling](#discounthandling) requirements.
* CostAndUsage MUST conform to [InvoiceHandling](#invoicehandling) requirements.
* CostAndUsage MUST conform to [DataGeneratorCalculatedSplitCostAllocationHandling](#datageneratorcalculatedsplitcostallocationhandling) requirements.

## 3. Column Requirements

### 3.1. Logical Grouping of Column Requirements

Grouping and ordering of requirements ensure clarity, logical flow, and consistency across all columns, making related requirements easy to identify and follow. This structure should be maintained for consistency across the specification.

**Note**: This section provides a current preview of the requirements grouping and ordering. Members should review how this applies to specific columns and provide feedback. The order may be adjusted based on that feedback.

  1. **Technical Requirements**
     1. **Data Type**: Establishes a foundational expectation, ensuring all subsequent rules align with this type.
     2. **Value Format**: Ensures the value (if present) adheres to specific structural or syntactic rules.
     3. **Nullability**: Clarifies when the value can or cannot exist, ensuring all subsequent rules align with column nullability.
     4. **Values and Value Ranges**: Further constrains valid values, assuming the format is already correct.
     5. **Column-to-Column Relationships**: Defines dependencies and consistency rules between related columns.
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

#### Tabular Overview of Column Normative Requirement Grouping and Specifications

| **Requirement Type** | **Requirement Group**              | **When required?**                    | **Example**                                                                                |
|----------------------|------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------|
| Technical            | Data Type                          | Always                                | {ColumnId} MUST be of type String.                                                         |
| Technical            | Value Format                       | Always (except normalized dimensions) | {ColumnId} MUST conform to [StringHandling](#stringhandling) requirements.                 |
| Technical            | Nullability                        | Always                                | {ColumnId} MUST/MUST NOT/SHOULD/SHOULD NOT/MAY be null when {Condition}.                     |
| Technical            | Values and Value Ranges            | Metrics and normalized dimensions     | {ColumnId} MUST be a valid decimal value.<br/>{ColumnId} MUST be one of the allowed values. |
| Technical            | Column to column Relationships     | When applicable                       | {ColumnId} SHOULD/MUST remain consistent over time for a given ReferencedColumnId.         |
| Business             | Unit/Denomination                  | When applicable                       | {ColumnId} MUST be denominated in the BillingCurrency.                                     |
| Business             | Uniqueness                         | When applicable                       | BillingAccountId MUST be a unique identifier within a provider.                            |
| Business             | Fallback/Substitute Values         | When applicable                       | {ColumnId} MUST NOT duplicate {OtherColumnId} when {Condition}.                              |
| Business             | Relationships Outside the Spec     | When applicable                       | The sum of {ColumnId} in a given billing period MUST match the sum of the invoices received for that billing period for a billing account. |
| Business             | Formula-based Cost Validation      | When applicable                       | {CostColumnId} MUST equal the product of {UnitPriceColumnId} and PricingQuantity when {UnitPriceColumnId} is not null and PricingQuantity is not null. |
| Business             | Cost Calculation and Relationships | When applicable                       | When {Condition}, {ColumnId} adheres to the following additional requirements:<br>  *{ColumnId} of a charge calculated based on other charges (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the ContractedCost of those related charges.<br>* {ColumnId} of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the BilledCost. |
| Business             | Other                              | When applicable                       |                                                                                           |

### 3.2. Ordering of Column Requirements Within Groups

To further enhance readability, individual requirements within each group SHOULD be ordered as follows:

* **MUST** – an absolute requirement
* **MUST NOT** – a prohibition
* **SHOULD** – recommended but not mandatory
* **SHOULD NOT** – discouraged but not strictly prohibited
* **MAY** – optional
* **MAY NOT** – optional prohibition / permitted not to

> ***Important Note:*** *The term **RECOMMENDED** (recommended but not mandatory; previously used only for presence-related normative requirements) is no longer permitted for use in normative requirements as of December 2025. The keyword **SHOULD** must be used instead. Please refer to the [**Editorial Style Guidelines**](editorial-guidelines.md).*

* For detailed interpretation of keywords such as "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", and others, see [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)].

### 3.3. Structuring Individual Column Requirements

* **Start with the ColumnId**: Whenever possible, begin each requirement with the ColumnId to make the requirement clear and focused.

  **Example Pattern 1**

  ```markdown
  * <ColumnId> MUST/MUST NOT/SHOULD/MUST be null when <Condition>.
  ```

* **Use {ColumnId} for Column and Value References**: Whenever possible, use {ColumnId} when referring to a column or its values.

* **Default to Singular Form**: Column references should be singular, with the understanding that the requirement applies to all values in the column.

### 3.4. Additional Guidelines for Columns in JSON Format

#### 3.4.1. Column Definition Structure

* **Separate normative requirements into sections for column, JSON schema, and contents**: Communicating the normative requirements for a column, JSON schema, and the contents can be convoluted. Separating these requirements provides better clarity.
  * Column normative requirements specify requirements of the column such as nullability.
  * JSON schema normative requirements specify the shape of the JSON.
  * Contents normative requirements usually specify the expected Keys, the format of the Values, and the expected contents of the Values.

#### 3.4.2. JSON Schema

* **Omit JSON schema normative requirements for Key-Value Format columns**: The Key-Value Format definition is sufficient to define the expected JSON schema.

* **Include JSON schema normative requirements for JSON Object Format columns**: The JSON Object Format specifies that the format is subject to the requirement of the column and that data generator-defined columns must have documented schema.
  * The pattern used in [AllocatedMethodDetails](#allocatedmethoddetails) and [ContractApplied](#contractapplied) consists of Object containing a collection whose key is "Elements" which contains one or more objects in the Key-Value format.

  **Example JSON**

  ```json
  {
    "Elements" : [ {
      "RequiredKey1" : 0.05,
      "RecommendedKey2" : "CPU",
      "RecommendedKey3" : 0.5
    }, {
      "RequiredKey1" : 0.1,
      "RecommendedKey3" : 4,
      "ProviderDefinedKey4": "SomeString"
    } ]
  }
  ```

* **Include a [JSON Type Definition](https://www.rfc-editor.org/rfc/rfc8927) (JTD) as an approximation of the expected schema, but clarify that JTD is non-normative and that normative requirements take precedence when there is a discrepancy**: JSON Type Definition is a convenient way to visualize the expected shape of JSON data, but it often cannot replicate the JSON schema normative requirements of FOCUS. E.g. [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JTD requires both to be specified.

  **Example JTD**
  
  ```json
  {
    "properties": {
      "Elements": {
        "elements": {
          "properties": {
            "RequiredKey1": { "type": "float64" }
          },
          "optionalProperties": {
            "RecommendedKey2": { "type": "string" },
            "RecommendedKey3": { "type": "float64" }
          },
          "additionalProperties": true
        }
      }
    },
    "additionalProperties": true
  }
  ```

#### 3.4.3. Key-Value Pairs

* **References to Key-Value Pairs depend on the context**: The terminology for key-value pairs varies depending on the column and context. For instance, when referring to key-value pairs, **tags**, **user-defined tags**, and **data generator-defined tags** are used in **Tags**, whereas **SkuPriceDetails property** is used in **SkuPriceDetails**.

* **Default to Plural for Key-Value Pairs**: When referring to key-value pairs, **tags** and **properties** should be used in the plural form to reflect the fact that the column may contain multiple key-value pairs.

#### 3.4.4. Keys and Values

* **Refer to Key and Values Explicitly**: When specifying normative requirements for key and value, use precise terminology based on the column type. For instance:
  * In **Tags**, refer to **tag key** when addressing only the key, and **tag value** when addressing only the value.
  * In **SkuPriceDetails**, refer to **property key** when addressing only the key, and **property value** when addressing only the value.
  * When linking a key to its value, use **corresponding value**.

* **First Mention and Context**: In the case of SkuPriceDetails property key, the first mention explicitly uses "SkuPriceDetails property key" to establish the context. Subsequent references to "property key" and "property value" omit "SkuPriceDetails" as the context is already understood. In contrast, for Tags, this is not necessary, as the context is inherently clear from the column name.

* **Put references to a specific key in double quotes**: In the case of AllocatedMethodDetails, normative requirements are applied to specific keys. To delineate for example that the object with the key "Elements" is being referred, the key should be used in its exact casing inside of double quotation marks `"`.

* **Start Key-Specific Requirements with the Key Term**: When a requirement applies to a key, it SHOULD begin with **tag key**, **property key**, or the applicable term for that column.

* **Start Value-Specific Requirements with the Value Term**: When a requirement applies to a value, it SHOULD begin with **tag value**, **property value**, or the applicable term for that column.

* **Plural vs. Singular Form for Keys and Values**:
  * Use plural when referring to keys or values to reflect the fact that the column may contain multiple keys/values (e.g., "property keys", "tag values").
  * Use singular when referring to the key or value of a single tag or property (e.g., "property key", "tag value"), with the understanding that the requirement applies to all occurrences.

### 3.5. Grouping of Nullability-Related and Subsequent Column Requirements

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

### 3.6. Grouping of Column Requirements Based on Specific Conditions

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

### 3.7. Consistent Wording and Patterns in Column Requirements

To ensure clarity and consistency across columns and corresponding requirements, it is important to:

* Follow common requirement patterns where applicable
* Use standardized phrasing and terminology

#### 3.7.1. Column Requirement Patterns

##### 3.7.1.1. Technical Requirements: Data Type

```markdown
* <ColumnId> MUST be of type String.
* <ColumnId> MUST be of type Decimal.
* <ColumnId> MUST be of type Date/Time.
```

##### 3.7.1.2. Technical Requirements: Value Format

```markdown
* <ColumnId> MUST conform to [StringHandling](#stringhandling) requirements.
* <ColumnId> MUST conform to [NumericFormat](#numericformat) requirements.
* <ColumnId> MUST conform to [DateTimeFormat](#datetimeformat) requirements.
* <ColumnId> SHOULD conform to [UnitFormat](#unitformat) requirements.
* <ColumnId> MUST conform to [KeyValueFormat](#keyvalueformat) requirements.
* <ColumnId> MUST conform to [CurrencyFormat](#currencyformat) requirements.
```

##### 3.7.1.3. Technical Requirements: Nullability

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
  * When <Condition>, <ColumnId> adheres to the following additional requirements:
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

##### 3.7.1.4. Technical Requirements: Values and Value Ranges

```markdown
* <ColumnId> MUST be a valid decimal value.
* <ColumnId> MUST be a non-negative decimal value.
```

##### 3.7.1.5. Technical Requirements: Column-to-Column Relationships

```markdown
* <ColumnId> SHOULD/MUST remain consistent over time for a given <OtherColumnId>.
```

##### 3.7.1.6. Business & Contextual Requirements: Unit/Denomination

```markdown
* <ColumnId> MUST be denominated in the BillingCurrency.
* <ColumnId> MUST be expressed in the <OtherColumnId>.
```

##### 3.7.1.7. Business & Contextual Requirements: Uniqueness

```markdown
* <ColumnId> MUST be a unique identifier within <Scope>.
```

##### 3.7.1.8. Business & Contextual Requirements: Fallback/Substitute Values

```markdown
* <ColumnId> MUST NOT duplicate <OtherColumnId> when <Condition>
```

##### 3.7.1.9. Business & Contextual Requirements: Relationships Outside the Spec

```markdown
* The sum of <ColumnId> in a given billing period MUST/MAY NOT match the sum of the invoices received for that billing period for a billing account.
```

##### 3.7.1.10. Business & Contextual Requirements: Cost Validation Rules

```markdown
* <CostColumnId> MUST equal the product of <UnitPriceColumnId> and PricingQuantity when <UnitPriceColumnId> is not null and PricingQuantity is not null.
```

##### 3.7.1.11. Business & Contextual Requirements: Cost Calculation and Relationships

```markdown
* When <Condition>, <CostColumnId> adheres to the following additional requirements:
  * <CostColumnId> of a charge calculated based on other charges (e.g., when the ChargeCategory is "Tax") MUST be calculated based on the <CostColumnId> of those related charges.
  * <CostColumnId> of a charge unrelated to other charges (e.g., when the ChargeCategory is "Credit") MUST match the BilledCost.
```

#### 3.7.2. Column Requirement Standardized Terminology

##### 3.7.2.1. Identifiers and Uniqueness within Scope

* Patterns:
  * {ColumnId} MUST be a unique identifier within {Scope}.
  * {ColumnId} SHOULD be a fully-qualified identifier.
* Examples:
  * BillingAccountId MUST be a unique identifier within a service provider.
  * ResourceId SHOULD be a fully-qualified identifier.

##### 3.7.2.2. Column Aggregation

* Pattern: The sum of {ColumnId} in a given billing period...
* Example: The sum of BilledCost in a given billing period...

##### 3.7.2.3. Column value Consistency

* Patterns:
  * {ColumnId} MUST/SHOULD remain consistent over time for a given {OtherColumnId}.
* Examples:
  * SkuMeter SHOULD remain consistent over time for a given SkuId.
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.

##### 3.7.2.4. References to charge and billing periods

* Patterns:
  * in a given billing period
  * in a given charge period

##### 3.7.2.5. Preferred Terminology for Numerical References

* Patterns: When specifying quantities in normative requirements, follow these conventions:
  * Use "one" instead of "1".
  * Use "more than one" instead of "2 or more".
* Examples:
  * When the service provider has only one user-defined tag scheme. (instead of: When the service provider has only 1 user-defined tag scheme.)
  * When the service provider has more than one user-defined tag scheme. (instead of: When the service provider has 2 or more user-defined tag schemes.)

### 3.8. Column Normative Requirements Examples

#### 3.8.1. **List Unit Price**

ListUnitPrice MUST adhere to the following requirements:

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
  * Discrepancies in ListUnitPrice, ListCost, or PricingQuantity MAY exist when ChargeClass is "Correction".

#### 3.8.2. **Billed Cost**

BilledCost MUST adhere to the following requirements:

* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [NumericFormat](#numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of BilledCost for a given [InvoiceId](#invoiceid) MUST match the sum of the payable amount provided in the corresponding invoice with the same id generated by the [InvoiceIssuerName](#invoiceissuername).

#### 3.8.3. **CommitmentDiscountQuantity**

CommitmentDiscountQuantity MUST adhere to the following requirements:

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

## 4. Attribute Requirements

### 4.1. Role of Attributes in the Specification

Attributes define reusable sets of normative constraints applicable to FOCUS datasets, columns (both FOCUS and custom), and column sub-elements (e.g., objects, keys, key values). Although Attributes are FOCUS entities, they serve only as containers for these constraints and are not treated as normative subjects of requirements.

An entity is considered conforming to an Attribute if it explicitly declares conformance or inherits it from a parent entity. For example, when a dataset declares conformance to NullHandling, all columns within that dataset are considered conforming to that Attribute.

Normative requirements defined in an Attribute section are evaluated within the scope of conforming entities but apply only to the subjects explicitly defined by each requirement. Conformance determines the set of entities in scope, while the requirement subject determines which of those entities are targeted.

### 4.2. Structural Anchor Requirement for Attributes

Each Attribute Requirements section MUST begin with a structural anchor requirement.

The structural anchor requirement:

* uses the primary schema-level entity as the subject,
* references the Attribute ID to establish the conformance context,
* introduces the scope of the subsequent requirements,
* is non-verifiable and non-enforceable,
* exists solely for structural consistency and automated parsing.

The canonical form of the structural anchor requirement is:

```markdown
[Dataset|Column] conforming to <Attribute ID> attribute MUST adhere to the following requirements:
```

Where `[Dataset|Column]` is the primary schema-level entity targeted by the Attribute — either Dataset or Column. Most Attributes target either datasets or columns, but not both. When an Attribute targets both datasets and columns, a separate structural anchor requirement MUST be used for each entity type.

When an Attribute is applicable only under specific conditions, the structural anchor requirement MAY be preceded by an applicability criteria condition:

```markdown
When <actor> <applicability-citeria-condition>, [Dataset|Column] conforming to <Attribute ID> attribute MUST adhere to the following requirements:
```

### 4.3. Normative Subjects in Attribute Requirements

Unlike column-level and dataset-level requirements, where the subject is a specific named dataset, column, or column sub-element, Attribute requirements are expressed against normative subjects that represent normative FOCUS entities, i.e., datasets, columns, or column sub-elements.

These subjects define the targets of individual requirements within the scope of conforming entities. While conformance determines which entities are in scope, the subject of each requirement determines which of those entities are affected.

When an Attribute's requirements do not apply to all entities within scope but only to a subset, a qualifier condition narrows the scope by describing that subset (e.g., `When FOCUS column contains numeric values, FOCUS column MUST adhere to the following requirements`). This ensures that the applicability of each requirement is explicit and does not rely solely on the conformance declaration.

The following table provides an overview of anchor subject types and requirement subjects used across all attributes, with each Attribute typically targeting only a subset of these subjects.

| Anchor Subject Type | Requirement Subject |
|---|---|
| Dataset | FOCUS dataset |
| Column | FOCUS column |
| Column | Custom column |
| Column | Object in FOCUS column |
| Column | Object in array in FOCUS column |
| Column | Key in Object in FOCUS column |
| Column | Key value in Object in FOCUS column |
| Column | Key in FOCUS column |
| Column | Key value in FOCUS column |

### 4.4. FOCUS vs Custom Column Requirements

Custom columns are expected to behave in the same or similar way as FOCUS columns. The difference is that requirements for Custom columns are expressed as recommendations rather than mandatory constraints.

As a general rule, when authoring requirements for a FOCUS column, the author SHOULD also consider whether the same requirements apply to Custom columns and, where applicable, restate them as recommendations using `SHOULD` instead of `MUST` and `SHOULD NOT` instead of `MUST NOT`. `MAY` and `MAY NOT` SHOULD be retained as-is.

The following exceptions apply:

* Some requirements might not be applicable to Custom columns and SHOULD be omitted.
* Some requirements might be mandatory for Custom columns and SHOULD retain `MUST` or `MUST NOT`.
* Some requirements might be optional for Custom columns and SHOULD use `MAY` or `MAY NOT` instead.

The appropriate keyword SHOULD always be chosen based on the intent and context of the requirement.

### 4.5. Grouping of Attribute Requirements

Structured grouping and ordering of Attribute requirements improves clarity, consistency, and maintainability across the specification by making related requirements easier to locate and understand, without introducing any additional normative meaning.

The groups defined here represent an ordering convention, not a structural requirement. Requirements within each group MAY be expressed as flat parallel bullets or as composite (parent + nested) bullets — whichever improves clarity and readability.

The only **exception** is the Structural Anchor Requirement (group 0), which by its nature always acts as a parent composite requirement.

Attributes may include requirements that apply to one or more intended normative subjects. To make the applicability of each Attribute, and each of its individual requirements, as transparent as possible, intended normative subjects serve as the basis for grouping. This ensures that readers can readily determine whether a requirement applies to a dataset, a subset of datasets, FOCUS columns, or custom columns.

0. **Structural Attribute Anchor Requirement:** Introduces the scope of the Attribute and provides a stable parsing entry point; it does not introduce a verifiable constraint.
1. **FOCUS Dataset-level Attribute Requirements:**
   1. **Global FOCUS Dataset Requirements:** Applicable to all FOCUS datasets that declare conformance to the Attribute, regardless of their structure, specific role or context.
   2. **Qualified FOCUS Dataset Requirements:** Applicable to a subset of FOCUS datasets that declare conformance to the Attribute and are identified through a qualifier.
   3. **Specific FOCUS Dataset Requirements:** Applicable to a specific FOCUS dataset, identified explicitly by Dataset ID.
2. **FOCUS Column-level Attribute Requirements:** Applicable to FOCUS columns that declare conformance to the Attribute.
   1. **Global FOCUS Column Requirements:** Applicable to all FOCUS columns that declare conformance to the Attribute, regardless of their structure, specific role or context.
   2. **Qualified FOCUS Column Requirements:** Applicable to a subset of FOCUS columns that declare conformance to the Attribute and are identified through a qualifier.
   3. **Specific FOCUS Column Requirements:** Applicable to a specific FOCUS column, identified explicitly by Column ID.
3. **FOCUS Column sub-element Attribute Requirements:** Applicable to structural sub-elements within columns that declare conformance to the Attribute.
   1. **Objects in Columns containing JsonObjectFormat values**
   2. **Keys in Objects in Columns containing JsonObjectFormat values**
   3. **Key values in Objects in Columns containing JsonObjectFormat values**
   4. **Keys in Columns containing Key-Value pair format values**
   5. **Key values in Columns containing Key-Value pair format values**
4. **Custom Column Attribute Requirements:**
   1. **Global Custom Column Requirements:** Applicable to all Custom columns, regardless of their structure or purpose.
   2. **Qualified Custom Column Requirements:** Applicable to a subset of Custom columns, identified through a qualifier.

### 4.6. Ordering of Attribute Requirements within Groups

To further enhance readability, individual requirements within each group SHOULD be ordered as follows:

* Requirements targeting the general subject (e.g., FOCUS column) first
* Requirements targeting qualified subjects (e.g., FOCUS column containing numeric values) after
* Within each subject, order by BCP 14 keyword:
  * **MUST** – an absolute requirement
  * **MUST NOT** – a prohibition
  * **SHOULD** – recommended but not mandatory
  * **SHOULD NOT** – discouraged but not strictly prohibited
  * **MAY** – optional
  * **MAY NOT** – optional prohibition / permitted not to

> ***Important Note:*** *The term **RECOMMENDED** (recommended but not mandatory; previously used only for presence-related normative requirements) is no longer permitted for use in normative requirements as of December 2025. The keyword **SHOULD** must be used instead. Please refer to the [**Editorial Style Guidelines**](editorial-guidelines.md).*

* For detailed interpretation of keywords such as "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", and others, see [BCP14](https://tools.ietf.org/html/bcp14) [[RFC2119](https://tools.ietf.org/html/rfc2119)][[RFC8174](https://tools.ietf.org/html/rfc8174)].

### 4.7. Attribute Normative Requirements Examples

#### 4.7.1. Null Handling

> *Note: This example illustrates the baseline pattern for an Attribute that applies to both FOCUS columns and Custom columns, with no qualifiers.*

Column conforming to NullHandling attribute MUST adhere to the following requirements:

* FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST use NULL for absent values when the FOCUS column is defined as nullable.
  * FOCUS column MUST NOT contain empty strings or placeholder strings (e.g., "Not Applicable") for absent values when the FOCUS column contains string values.
  * FOCUS column MUST NOT contain placeholder numeric values (e.g., 0) for absent values when the FOCUS column contains numeric values.
* Custom column MUST adhere to the following requirements:
  * Custom column SHOULD use NULL for absent values when the custom column is defined as nullable.
  * Custom column SHOULD NOT contain empty strings or placeholder strings (e.g., "Not Applicable") for absent values when the custom column contains string values.
  * Custom column SHOULD NOT contain placeholder numeric values (e.g., 0) for absent values when the custom column contains numeric values.

#### 4.7.2. Date/Time Format

> *Note: This example illustrates an Attribute with a qualifier and a nested composite requirement, expressed for both FOCUS columns and Custom columns.*

Column conforming to DateTimeFormat attribute MUST adhere to the following requirements:

* When FOCUS column contains date/time values, FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST be expressed in UTC (Coordinated Universal Time) to avoid ambiguity and ensure consistency across different time zones.
  * FOCUS column MUST conform to the ISO 8601 standard, which provides a globally recognized format for representing dates and times.
  * When FOCUS column represents a specific moment in time, FOCUS column MUST adhere to the following requirements:
    * FOCUS column MUST use the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ').
    * FOCUS column MUST include both the date and time components, separated with the letter 'T'.
    * FOCUS column MUST use two-digit hours (HH), minutes (mm), and seconds (ss).
    * FOCUS column MUST end with the ISO 8601 UTC designator 'Z'.
* When custom column contains date/time values, custom column MUST adhere to the following requirements:
  * Custom column SHOULD be expressed in UTC (Coordinated Universal Time).
  * Custom column SHOULD conform to the ISO 8601 standard.
  * When custom column represents a specific moment in time, custom column MUST adhere to the following requirements:
    * Custom column SHOULD use the extended ISO 8601 format with UTC offset ('YYYY-MM-DDTHH:mm:ssZ').
    * Custom column SHOULD include both the date and time components, separated with the letter 'T'.
    * Custom column SHOULD use two-digit hours (HH), minutes (mm), and seconds (ss).
    * Custom column SHOULD end with the ISO 8601 UTC designator 'Z'.

#### 4.7.3. JSON Object Format

> *Note: This example illustrates an Attribute with sub-element requirements (Object, Key, Key value) expressed as qualified bullets within the FOCUS Column group.*

Column conforming to JsonObjectFormat attribute MUST adhere to the following requirements:

* When FOCUS column contains JsonObjectFormat values, FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST contain a serialized JSON string, consistent with the [ECMA 404](https://www.ecma-international.org/wp-content/uploads/ECMA-404_2nd_edition_december_2017.pdf) definition of an object.
  * FOCUS column MUST conform to all requirements of the corresponding column definition, which may specify or restrict the shape or contents of the object.
  * Object in FOCUS column SHOULD NOT exceed 3 levels of nesting.
  * Key in Object in FOCUS column MUST be unique.
  * Key value in Object in FOCUS column MUST be of type number, string, boolean (`true` or `false`), array, object, or `null`.
  * Object in array in FOCUS column MUST adhere to the following requirements:
    * Object in array in FOCUS column MUST be of a consistent type.
    * Object in array in FOCUS column MUST NOT be repeated.
    * Object in array in FOCUS column MUST NOT be null.
* Custom column MUST have its object schema documented by the data generator and accessible to practitioners when the custom column contains a JSON object.

#### 4.7.4. Data Generator Calculated Split Cost Allocation Handling

> *Note: This example illustrates an Attribute with an applicability condition preceding the structural anchor requirement.*

When the data generator supports data generator-calculated split cost allocation, column conforming to DataGeneratorCalculatedSplitCostAllocationHandling attribute MUST adhere to the following requirements:

* The sum of FOCUS column values in *allocated charges* MUST match the corresponding value in the *origin charge* when the FOCUS column represents a summable [*metric*](#glossary:metric) (e.g., costs and quantities).
* FOCUS column values in *allocated charges* MUST match the corresponding value in the *origin charge* when the FOCUS column represents a non-summable *metric* (e.g., unit prices).
* FOCUS column values in *allocated charges* MUST match the corresponding value in the *origin charge* when the FOCUS column represents a dimension.
* FOCUS column values in *allocated charges* MUST include the same keys and values present in the [CostAndUsage.Tags](#datasets.costandusage.tags) in the *origin charge* when the FOCUS column contains tag values.

#### 4.7.5. Column Handling

> *Note: This example illustrates the special case of an Attribute that targets both datasets and columns, requiring two separate structural anchor requirements.*

Dataset conforming to ColumnHandling attribute MUST adhere to the following requirements:

* FOCUS dataset MUST adhere to the following column ordering requirements:
  * FOCUS dataset SHOULD list all FOCUS columns before all Custom columns.
  * FOCUS dataset SHOULD sort FOCUS columns alphabetically by their Column ID within the FOCUS columns group.
  * FOCUS dataset SHOULD sort Custom columns alphabetically by their Column ID within the Custom columns group.
  * FOCUS dataset SHOULD NOT intermix FOCUS columns and Custom columns when ordering columns.

Column conforming to ColumnHandling attribute MUST adhere to the following requirements:

* FOCUS column MUST adhere to the following requirements:
  * FOCUS column MUST use a Display Name consistent with the Column ID, with spaces inserted between words (e.g., Column ID "BillingAccountName" and Display Name "Billing Account Name").
  * FOCUS column MUST use Pascal case in the Column ID.
  * FOCUS column MUST use only alphanumeric characters in the Column ID.
  * FOCUS column MUST NOT include special characters in the Column ID.
  * FOCUS column MUST NOT use abbreviations other than `Id` in the Column ID.
  * FOCUS column SHOULD NOT use acronyms other than `Sku` in the Column ID.
  * FOCUS column SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * FOCUS column MUST include the `Id` suffix in the Column ID when the FOCUS column represents an identifier.
  * FOCUS column MUST include the `Name` suffix in the Column ID when the FOCUS column represents a name.
  * FOCUS column MUST include `Sku` in the Column ID when the FOCUS column represents a product offering that incurred a charge.
  * FOCUS column MUST contain one of the FOCUS-defined allowed values when the FOCUS column includes `Category` suffix in the Column ID and is not null.
* Custom column (e.g., service-provider-defined column included in FOCUS dataset) MUST adhere to the following requirements:
  * Custom column MUST include the `x_` prefix in the Column ID to identify it as an external custom column and to distinguish it from FOCUS columns to avoid conflicts in future releases.
  * Custom column SHOULD use Pascal case in the Column ID.
  * Custom column SHOULD use only alphanumeric characters in the Column ID.
  * Custom column SHOULD NOT include special characters in the Column ID.
  * Custom column SHOULD NOT use abbreviations other than `Id` in the Column ID.
  * Custom column SHOULD NOT use acronyms other than `Sku` in the Column ID.
  * Custom column SHOULD NOT exceed 50 characters in the Column ID to accommodate column length restrictions of various data repositories.
  * Custom column SHOULD include the `Id` suffix in the Column ID when the custom column represents an identifier.
  * Custom column SHOULD include the `Name` suffix in the Column ID when the custom column represents a name.
