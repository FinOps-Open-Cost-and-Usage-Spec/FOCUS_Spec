# SKU Price Eligibility

SKU Price Eligibility is a structured definition of the specific entities, accounts, or contexts eligible to receive the specified [*SKU Price*](#glossary:sku-price). This column details the inclusionary and exclusionary logic that dictates when a specific unit price can be applied to consumption.

## Requirements

### Column Requirements

SkuPriceEligibility MUST adhere to the following requirements:

* SkuPriceEligibility MUST be of type JSON Object (serialized as a String where necessary).
* SkuPriceEligibility MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* SkuPriceEligibility MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* SkuPriceEligibility MUST conform to [SkuPriceEligibilityObject](#datamodel.skuprice.skupriceeligibility.skupriceeligibilityobject) requirements.
* SkuPriceEligibility MUST NOT be null.

## SKU Price Eligibility Object

SKU Price Eligibility consists of a valid JSON object which contains a set of top-level property keys. These keys define entity-based inclusionary and exclusionary logic for the *SKU Price*.

The following section details the normative requirements for the SkuPriceEligibilityObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.skuprice.skupriceeligibility.skupriceeligibilityobject.objectschemastructure) and [Object Example](#datamodel.skuprice.skupriceeligibility.skupriceeligibilityobject.objectexample) sections.

### Object Requirements

SkuPriceEligibilityObject MUST adhere to the following requirements:

* SkuPriceEligibilityObject MUST conform to the [SkuPriceEligibilityObjectSchema](#schemas.skuprice.skupriceeligibilityobjectschema) JSON Schema.
* SkuPriceEligibilityObject.IsGlobalScope MUST be `true` when the *SKU Price's* eligibility is not restricted to an enumerated set of entities (e.g., a standard public list price).
* SkuPriceEligibilityObject.IsComplexScope MUST be `true` when the *SKU Price's* eligibility logic exceeds schema capabilities.
* SkuPriceEligibilityObject.Inclusions[\*].Dimension SHOULD represent a column in [Cost and Usage](#datamodel.costandusage).
* SkuPriceEligibilityObject.Exclusions[\*].Dimension SHOULD represent a column in Cost and Usage.
* SkuPriceEligibilityObject.Inclusions[\*].Values MUST contain only the single string "*" when the wildcard is present.
* SkuPriceEligibilityObject.Exclusions[\*].Values MUST contain only the single string "*" when the wildcard is present.

### Object Schema Structure

SkuPriceEligibility contains a structured JSON object defining the logical boundaries of price applicability.

<div class="h7-nonindex">Top-Level Properties</div>

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `IsGlobalScope` | Boolean | No | When `true`, the price applies to all entities except those matched by `Exclusions`. Defaults to `false`. |
| `IsComplexScope` | Boolean | No | When `true`, indicates logic exceeds schema capabilities. Defaults to `false`. |
| `InclusionOperator` | String | Conditional | Required only when `IsGlobalScope` and `IsComplexScope` are both `false`. Valid values: `And`, `Or`. Omitted when Global or Complex scope is `true`. |
| `Inclusions` | Array | Conditional | Required only when `IsGlobalScope` and `IsComplexScope` are both `false`. List of `Rule` objects defining the boundary. Omitted when Global or Complex scope is `true`. |
| `ExclusionOperator` | String | Conditional | Required only when `Exclusions` are present. Defines the relationship for `Exclusions`. Valid values: `And`, `Or`. |
| `Exclusions` | Array | No | List of `Rule` objects defining entities to be removed from the boundary. |

<div class="h7-nonindex">Rule Object</div>

| Key | Type | Description |
| :--- | :--- | :--- |
| `Dimension` | String | A valid FOCUS Column Name (e.g., `BillingAccountId`, `SubAccountId`). |
| `Operator` | String | The comparison logic to apply. Must be one of the Supported Operators. |
| `Values` | Array | A list of strings to compare. A value of `["*"]` acts as a global wildcard. |

<div class="h7-nonindex">Supported Operators</div>

| Operator | Logic | Usage Example |
| :--- | :--- | :--- |
| `In` | Exact match against any item in the list. | `["123456789", "987654321"]` |
| `NotIn` | Does not match any item in the list. | `["123456789"]` |
| `StartsWith` | String prefix match. | `["prod-"]` |
| `NotStartsWith` | Does not begin with the specified prefix. | `["test-"]` |
| `Contains` | Substring match anywhere in the value. | `["database"]` |
| `NotContains` | Substring is not present in the value. | `["sandbox"]` |
| `EndsWith` | String suffix match. | `["-temp"]` |
| `Exists` | Checks if the dimension is present and not null. | `Values` must be `["*"]` |
| `DoesNotExist` | Checks if the dimension is missing or null. | `Values` must be `["*"]` |

<div class="h7-nonindex">Wildcard Handling</div>

SkuPriceEligibility uses a reserved string to represent global or unrestricted boundaries within a specific Dimension.

| Reserved Value | Description | Supported Operators |
| :--- | :--- | :--- |
| `"*"` | Represents all possible values for the specified Dimension. | `In`, `Contains`, `Exists`, `DoesNotExist` |

<div class="h7-nonindex">Wildcard Behavior Rules</div>

1. **Inclusion Logic:** When `["*"]` is used in an Inclusion rule, the rule evaluates to `True` for every entity, effectively making the price globally eligible for that specific Dimension.
2. **Exclusion Logic:** When `["*"]` is used in an Exclusion rule, the rule evaluates to `True` for every entity, effectively excluding all entities (this is typically used only in combination with `ExclusionOperator: "And"` for surgical filtering).
3. **Implicit Wildcards:** If a Dimension is omitted entirely from the `Inclusions` array, it is treated as an implicit wildcard (unrestricted).

### Object Implementation Guidance

<div class="h7-nonindex">Processing Workflow</div>

The evaluation of an entity's usage against a rate card's eligibility rules proceeds in the following order:

1. **Normalization:** Convert the entity attribute and the Scope `Values` to a consistent case (default: lowercase) for comparison.
2. **Scope Check:** If `IsGlobalScope` is `true`, the entity passes inclusion; proceed to Exclusion Evaluation. If `IsComplexScope` is `true`, the object does not determine eligibility; terminate evaluation.
3. **Inclusion Evaluation:** Iterate through `Inclusions`. Apply `InclusionOperator`. If result is `False`, the entity is not eligible for this unit price; terminate evaluation.
4. **Exclusion Evaluation:** Iterate through `Exclusions`. If `True`, the entity is explicitly excluded from this unit price; terminate evaluation.
5. **Resolution:** If the entity passes the Scope Check or Inclusion Evaluation and is not caught by Exclusions, the `SKU Price` is valid for that entity.

<div class="h7-nonindex">Dependency Logic</div>

1. **Consistency:** Engines are expected to accept a JSON Object and to reject scalar values for this field, for compatibility with typed database schemas.
2. **Conflict Resolution:** When `IsGlobalScope` or `IsComplexScope` is `true`, the `Inclusions` array is empty or omitted, and `IsGlobalScope` and `IsComplexScope` are not both `true`. Engines are expected to validate these structural constraints before processing.

### Object Example

Here is a basic example of the object format, describing a custom contracted rate that is only eligible for two specific Billing Accounts.

```json
{
  "IsGlobalScope": false,
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": [
        "123456789012",
        "987654321098"
      ]
    }
  ]
}
```

### Object ID

SkuPriceEligibilityObject

### Object Display Name

SKU Price Eligibility Object

## Column ID

SkuPriceEligibility

## Display Name

SKU Price Eligibility

## Description

A structured definition of the specific entities, accounts, or contexts eligible to receive the specified unit price.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [SKU Price](#datamodel.skuprice) |
| Conditions | Not applicable |
| Column type | Dimension |
| Feature level | Mandatory |
| Allows nulls | False |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [SkuPriceEligibilityObject](#datamodel.skuprice.skupriceeligibility.skupriceeligibilityobject) |

## Version Introduced

1.5
