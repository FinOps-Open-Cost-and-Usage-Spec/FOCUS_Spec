# Commitment Applicability

Commitment Applicability is a structured definition of the usage that a [*commitment discount*](#glossary:commitment-discount) purchased under the specified [SKU Price](#datamodel.skuprice) record covers, and of how that usage is covered. For each covered scope, it states how much of the *commitment discount* one unit of covered usage consumes, the discount applied to the unit price of covered usage, or the unit price of covered usage. This allows practitioners to derive the unit price that applies to usage covered by the *commitment discount* without the SKU Price dataset carrying a separate record for each covered SKU and purchase option.

## Requirements

### Column Requirements

CommitmentApplicability MUST adhere to the following requirements:

* CommitmentApplicability MUST be of type JSON Object (serialized as a String where necessary).
* CommitmentApplicability MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentApplicability MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* CommitmentApplicability MUST conform to [CommitmentApplicabilityObject](#datamodel.skuprice.commitmentapplicability.commitmentapplicabilityobject) requirements when CommitmentApplicability is not null.
* CommitmentApplicability MUST adhere to the following nullability requirements:
  * CommitmentApplicability MUST be null when the SkuPrice record does not represent the purchase of a *commitment discount*.
  * CommitmentApplicability MUST NOT be null when the SkuPrice record represents the purchase of a *commitment discount*.

## Commitment Applicability Object

Commitment Applicability consists of a valid JSON object which contains a set of top-level property keys. These keys define the usage covered by the *commitment discount* through inclusionary and exclusionary logic, and the coverage that applies to it, either for all covered usage or for the usage matched by a specific rule.

The following section details the normative requirements for the CommitmentApplicabilityObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.skuprice.commitmentapplicability.commitmentapplicabilityobject.objectschemastructure) and [Object Example](#datamodel.skuprice.commitmentapplicability.commitmentapplicabilityobject.objectexample) sections.

### Object Requirements

CommitmentApplicabilityObject MUST adhere to the following requirements:

* CommitmentApplicabilityObject MUST conform to the [CommitmentApplicabilityObjectSchema](#schemas.skuprice.commitmentapplicabilityobjectschema) JSON Schema.
* CommitmentApplicabilityObject.IsGlobalScope MUST be `true` when the usage covered by the *commitment discount* is not restricted to an enumerated set of entities.
* CommitmentApplicabilityObject.IsComplexScope MUST be `true` when the coverage logic of the *commitment discount* exceeds schema capabilities.
* CommitmentApplicabilityObject.Coverage MUST conform to CoverageObject requirements when CommitmentApplicabilityObject.Coverage is present.
* CommitmentApplicabilityObject.Coverage MUST be present when CommitmentApplicabilityObject.IsGlobalScope is `true`.
* CommitmentApplicabilityObject.Inclusions[\*].Dimension SHOULD represent a column in [CostAndUsage](#datamodel.costandusage) or [SkuPrice](#datamodel.skuprice).
* CommitmentApplicabilityObject.Exclusions[\*].Dimension SHOULD represent a column in CostAndUsage or SkuPrice.
* CommitmentApplicabilityObject.Inclusions[\*].Values MUST contain only the single string "*" when the wildcard is present.
* CommitmentApplicabilityObject.Exclusions[\*].Values MUST contain only the single string "*" when the wildcard is present.
* CommitmentApplicabilityObject.Inclusions[\*].Coverage MUST conform to CoverageObject requirements when CommitmentApplicabilityObject.Inclusions[\*].Coverage is present.
* CommitmentApplicabilityObject.Inclusions[\*].Coverage MUST be present when CommitmentApplicabilityObject.Coverage is not present and CommitmentApplicabilityObject.IsComplexScope is not `true`.
* CommitmentApplicabilityObject.Inclusions[\*].Coverage MUST NOT be present when CommitmentApplicabilityObject.InclusionOperator is "And".

### Coverage Object Requirements

CoverageObject MUST adhere to the following requirements:

* CoverageObject MUST contain exactly one of the Factor, Discount, and UnitPrice properties.
* CoverageObject.Factor MUST represent the quantity of the *commitment discount*, expressed in the [PricingUnit](#datamodel.skuprice.pricingunit) of the SkuPrice record, consumed by one unit of covered usage, expressed in the PricingUnit of the covered usage.
* CoverageObject.Factor MUST NOT be present when [CommitmentDiscountCategory](#datamodel.skuprice.commitmentdiscountcategory) is "Spend".
* CoverageObject.Discount MUST represent the fraction by which the unit price of covered usage is reduced.
* CoverageObject.UnitPrice MUST represent the unit price per PricingUnit of the covered usage.
* CoverageObject.UnitPrice MUST be denominated in the [PricingCurrency](#datamodel.skuprice.pricingcurrency).

### Object Schema Structure

CommitmentApplicability contains a structured JSON object defining the usage covered by a *commitment discount* and how it is covered.

<div class="h7-nonindex">Top-Level Properties</div>

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `IsGlobalScope` | Boolean | No | When `true`, the *commitment discount* covers all usage except usage matched by `Exclusions`. Defaults to `false`. |
| `IsComplexScope` | Boolean | No | When `true`, indicates coverage logic exceeds schema capabilities. Defaults to `false`. |
| `Coverage` | Object | Conditional | Default `Coverage` object for all covered usage. Required when `IsGlobalScope` is `true`, or when any `Inclusions` rule has no `Coverage`. |
| `ApplicationOrder` | String | No | Order in which the *commitment discount* is applied to eligible usage. Valid values: `HighestDiscountFirst`, `RuleOrder`, `ServiceProviderDefined`. Defaults to `ServiceProviderDefined`. |
| `InclusionOperator` | String | Conditional | Required only when `IsGlobalScope` and `IsComplexScope` are both `false`. Valid values: `And`, `Or`. Empty or omitted when Global or Complex scope is `true`. |
| `Inclusions` | Array | Conditional | Required only when `IsGlobalScope` and `IsComplexScope` are both `false`. List of `Rule` objects defining the covered usage. Empty or omitted when Global or Complex scope is `true`. |
| `ExclusionOperator` | String | Conditional | Required only when `Exclusions` are present. Defines the relationship for `Exclusions`. Valid values: `And`, `Or`. |
| `Exclusions` | Array | No | List of `Rule` objects defining usage removed from coverage. |

<div class="h7-nonindex">Rule Object</div>

| Key | Type | Description |
| :--- | :--- | :--- |
| `Dimension` | String | A valid FOCUS Column ID from Cost and Usage or SKU Price (e.g., `SkuId`, `PricingServiceName`, `PricingRegionId`, `RegionId`). |
| `Operator` | String | The comparison logic to apply. Must be one of the Supported Operators. |
| `Values` | Array | A list of strings to compare. A value of `["*"]` acts as a global wildcard. |
| `Coverage` | Object | Optional, `Inclusions` only. The `Coverage` object for usage matched by this rule. Overrides the top-level `Coverage`. |

<div class="h7-nonindex">Coverage Object</div>

| Key | Type | Description |
| :--- | :--- | :--- |
| `Factor` | Decimal | Quantity of the *commitment discount*, in the Pricing Unit of the purchase record, consumed by one unit of covered usage. Greater than 0; can be greater than 1 (e.g., *commitment discount flexibility*). |
| `Discount` | Decimal | Fraction by which the unit price of covered usage is reduced, applied to both its list and its contracted unit price. From 0 to 1. |
| `UnitPrice` | Decimal | Unit price per Pricing Unit of the covered usage, denominated in the Pricing Currency of the purchase record. Non-negative. |

A `Coverage` object contains exactly one of `Factor`, `Discount`, or `UnitPrice`.

<div class="h7-nonindex">Supported Operators</div>

| Operator | Logic | Usage Example |
| :--- | :--- | :--- |
| `In` | Exact match against any item in the list. | `["AURAWEB-COMPUTE-VM-STD-8X32"]` |
| `NotIn` | Does not match any item in the list. | `["AURAWEB-COMPUTE-VM-GPU-8X64"]` |
| `StartsWith` | String prefix match. | `["AURAWEB-COMPUTE-VM-STD-"]` |
| `NotStartsWith` | Does not begin with the specified prefix. | `["AURAWEB-COMPUTE-VM-GPU-"]` |
| `Contains` | Substring match anywhere in the value. | `["-STD-"]` |
| `NotContains` | Substring is not present in the value. | `["-GPU-"]` |
| `EndsWith` | String suffix match. | `["-8X32"]` |
| `Exists` | Checks if the dimension is present and not null. | `Values` must be `["*"]` |
| `DoesNotExist` | Checks if the dimension is missing or null. | `Values` must be `["*"]` |

<div class="h7-nonindex">Wildcard Handling</div>

CommitmentApplicability uses a reserved string to represent unrestricted boundaries within a specific Dimension.

| Reserved Value | Description | Supported Operators |
| :--- | :--- | :--- |
| `"*"` | Represents all possible values for the specified Dimension. | `In`, `Contains`, `Exists`, `DoesNotExist` |

<div class="h7-nonindex">Wildcard Behavior Rules</div>

1. **Inclusion Logic:** When `["*"]` is used with the `In` or `Contains` operator in an Inclusion rule, the rule evaluates to `True` for every charge where the Dimension is not null.
2. **Exclusion Logic:** When `["*"]` is used with the `In` or `Contains` operator in an Exclusion rule, the rule evaluates to `True` for every charge where the Dimension is not null.
3. **Implicit Wildcards:** If a Dimension is omitted entirely from the `Inclusions` array, it is treated as an implicit wildcard (unrestricted).

### Object Implementation Guidance

<div class="h7-nonindex">Processing Workflow</div>

The coverage that applies to a usage *charge* is resolved in the following order:

1. **Scope Check:** If `IsGlobalScope` is `true`, the *charge* passes inclusion with the top-level `Coverage`; proceed to Exclusion Evaluation. If `IsComplexScope` is `true`, the object does not determine coverage; terminate evaluation.
2. **Inclusion Evaluation:** Iterate through `Inclusions` in array order and apply `InclusionOperator`. If the result is `False`, the *charge* is not covered by this *commitment discount*; terminate evaluation. With `Or`, the `Coverage` of the first matching rule applies, or the top-level `Coverage` when that rule has none. With `And`, the top-level `Coverage` applies.
3. **Exclusion Evaluation:** Iterate through `Exclusions`. If `True`, the *charge* is excluded from coverage; terminate evaluation.
4. **Resolution:** The *charge* is covered with the `Coverage` resolved in the previous steps.

Values are compared as exact strings.

<div class="h7-nonindex">Deriving the Unit Price of Covered Usage</div>

* **`UnitPrice`:** the unit price of covered usage, as published.
* **`Discount`:** the Unit Price of the SKU Price record for the covered usage multiplied by one minus `Discount`, for its "List" record and, under a *contract*, for its "Contracted" record.
* **`Factor`:** the price of the *commitment discount* (the Unit Price of the purchase record, spread over its Purchase Duration Type according to its Purchase Payment Model), multiplied by `Factor` and divided by the quantity of usage the *commitment discount* covers per unit of time.

<div class="h7-nonindex">Evaluating Rules Against Null Dimensions</div>

When the processing workflow evaluates a rule against a *charge* where the target `Dimension` is `null`:

* The `DoesNotExist` operator evaluates to `true`.
* The `Exists` operator evaluates to `false`.
* The `In` and `NotIn` operators do not match any string values.

<div class="h7-nonindex">Dependency Logic</div>

1. **Consistency:** Engines are expected to accept a JSON Object and to reject scalar values for this field, for compatibility with typed database schemas.
2. **Conflict Resolution:** When `IsGlobalScope` or `IsComplexScope` is `true`, the `Inclusions` array is empty or omitted, and `IsGlobalScope` and `IsComplexScope` are not both `true`. Engines are expected to validate these structural constraints before processing.

### Object Example

Here is a basic example of the object format, describing a reservation that covers three sizes of a virtual machine family, with *commitment discount flexibility* expressed as a `Factor` per size.

```json
{
  "Coverage": {
    "Factor": 1.0
  },
  "InclusionOperator": "Or",
  "Inclusions": [
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-4X16"],
      "Coverage": {
        "Factor": 0.5
      }
    },
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-8X32"]
    },
    {
      "Dimension": "SkuId",
      "Operator": "In",
      "Values": ["AURAWEB-COMPUTE-VM-STD-16X64"],
      "Coverage": {
        "Factor": 2.0
      }
    }
  ]
}
```

### Object ID

CommitmentApplicabilityObject

### Object Display Name

Commitment Applicability Object

## Column ID

CommitmentApplicability

## Display Name

Commitment Applicability

## Description

A structured definition of the usage that a *commitment discount* purchased under the specified SKU Price record covers, and of how that usage is covered.

## Content Constraints

| Constraint                 | Value |
| :------------------------- | :--- |
| Dataset                    | [SKU Price](#datamodel.skuprice) |
| Operating Model Conditions | [Includes Commitment Discounts](#operatingmodelconditions.includescommitmentdiscounts) |
| Column type                | Dimension |
| Feature level              | Conditional |
| Allows nulls               | True |
| Data type                  | JSON |
| Value format               | [JSON Object Format](#attributes.jsonobjectformat) |
| Object                     | [CommitmentApplicabilityObject](#datamodel.skuprice.commitmentapplicability.commitmentapplicabilityobject) |

## Version Introduced

1.5
