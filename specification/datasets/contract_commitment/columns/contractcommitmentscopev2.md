# Contract Commitment Scope

Contract Commitment Scope is a structured definition of the specific entities to which a contract commitment applies, with both inclusionary and exclusionary logic, as well as the portion of cost or usage that is applicable.

## Requirements

ContractCommitmentScope adheres to the following requirements:

* ContractCommitmentScope MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentScope MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractCommitmentScope MUST NOT be null.

## Logical Schema Structure

ContractCommitmentScope contains a structured JSON object defining the logical boundaries and the applicability percentage of a commitment.

### Top-Level Attributes

| Attribute | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `IsGlobalScope` | Boolean | No | If `true`, the commitment applies to all resources. Defaults to `false`. Exclusions are still processed if present. |
| `IsComplexScope` | Boolean | No | If `true`, indicates logic exceeds schema capabilities. Defaults to `false`. |
| `Applicability` | Decimal OR Object | No | The fraction of the identified cost or usage to which terms apply. A **Decimal** applies to both Cost and Usage. An **Object** (see below) allows for divergence. Defaults to `1.0`. |
| `InclusionOperator` | String | Conditional | **Required** only if `IsGlobalScope` and `IsComplexScope` are both `false` or null. Valid values: `AND`, `OR`. Defaults to `OR`. |
| `Inclusions` | Array | Conditional | **Required** only if `IsGlobalScope` and `IsComplexScope` are both `false` or null. List of `Rule` objects defining the boundary. |
| `ExclusionOperator` | String | No | Defines the relationship for `Exclusions`. Valid values: `AND`, `OR`. Defaults to `OR`. |
| `Exclusions` | Array | No | List of `Rule` objects defining entities to be removed from the boundary. |

### Rule Object

Rules are evaluated against the column values of the resource being analyzed.

| Key | Type | Description |
| :--- | :--- | :--- |
| `Dimension` | String | A valid FOCUS Column Name (e.g., `ProviderAccountId`, `RegionId`). |
| `Operator` | String | The comparison logic to apply. Must be one of the Supported Operators. |
| `Values` | Array | A list of strings to compare. A value of `["*"]` acts as a global wildcard. |
| `Applicability` | Decimal OR Object | **Optional.** The specific fraction of applicability for resources matching this rule. Overrides the top-level `Applicability`. |

### Applicability Object

When specified as an object, `Applicability` allows for independent percentages for different metrics.

| Key | Type | Description |
| :--- | :--- | :--- |
| `Cost` | Decimal | Percentage applicable to `BilledCost` and `AmortizedCost`. |
| `Usage` | Decimal | Percentage applicable to `UsageQuantity`. |

---

## Examples

The following examples demonstrate how to model common contract commitment scenarios using ContractCommitmentScope.

### Global Scope and Applicability
An Enterprise Discount Program (EDP) or a global Savings Plan that applies to all resources across the entire provider footprint.  100% of activity is applicable, regardless of cost or usage.

```json
{
  "IsGlobalScope": true,
  "Applicability": 1.0
}
```

The inclusion of Applicability is optional, given that the default is 1.0.  It could thus be delivered even simpler, as:

```json
{
  "IsGlobalScope": true
}
```

### Global Scope with Specific Exceptions
Organization-wide coverage EXCEPT for Database services running in BillingAccountId 123456789012.

```json
{
  "IsGlobalScope": true,
  "ExclusionOperator": "AND",
  "Exclusions": [
    {
      "Dimension": "BillingAccountId",
      "Operator": "In",
      "Values": ["123456789012"]
    },
    {
      "Dimension": "ServiceCategory",
      "Operator": "In",
      "Values": ["Database"]
    }
  ]
}
```

### Regional Scope
A commitment purchased for a specific region (e.g., `us-east-1`). Since `IsGlobalScope` and `IsComplexScope` are omitted, they default to `false`, requiring the inclusion block.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"]
    }
  ]
}
```

### Regional Compute Commitment with Exceptions
Applies to Compute in `us-east-1` and `us-west-2`, excluding any resources or services tagged with an `Environment` of `Sandbox`.

```json
{
  "InclusionOperator": "AND",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1", "us-west-2"]
    },
    {
      "Dimension": "ServiceCategory",
      "Operator": "In",
      "Values": ["Compute"]
    }
  ],
  "ExclusionOperator": "OR",
  "Exclusions": [
    {
      "Dimension": "Tags",
      "Operator": "Contains",
      "Values": ["\"Environment\": \"Sandbox\""]
    }
  ]
}
```

### Shorthand Applicability (Decimal)
A commitment that applies fully to `us-east-1` but only 50% of cost and usage in `us-west-2` is eligible.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-east-1"],
      "Applicability": 1.0
    },
    {
      "Dimension": "RegionId",
      "Operator": "In",
      "Values": ["us-west-2"],
      "Applicability": 0.5
    }
  ]
}
```

### Granular Applicability (Object)
A scenario where 100% of Marketplace **Usage** counts toward a volume commitment, but only 50% of the **Cost** is applicable for financial credit.

```json
{
  "InclusionOperator": "OR",
  "Inclusions": [
    {
      "Dimension": "InvoiceIssuerName",
      "Operator": "In",
      "Values": ["Cloud Marketplace"],
      "Applicability": {
        "Cost": 0.5,
        "Usage": 1.0
      }
    }
  ]
}
```

### Complex Fallback
A commitment with dynamic or conditional logic that requires calculation against the total aggregate of cost or usage (e.g., 'Applies to the top 10% of compute spend by volume'). While the intent can be described in ContractCommitmentDescription, the IsComplexScope flag signals that the scope and applicability cannot be described in isolation for a subset of included or excluded values.

```json
{
  "IsComplexScope": true
}
```

---

## Implementation Guidance

### Processing Workflow

The evaluation of a resource against a commitment scope MUST follow a strict linear progression:

1.  **Normalization:** Convert the resource attribute and the Scope `Values` to a consistent case (default: lowercase) for comparison.
2.  **Inclusion Evaluation:** Iterate through `Inclusions`. If a match is found, record the rule-level `Applicability` if present. Apply `InclusionOperator`. If result is `False`, terminate.
3.  **Exclusion Evaluation:** Iterate through `Exclusions`. If `True`, terminate evaluation.
4.  **Applicability Resolution:**
    * **Resolution Logic:** If `Applicability` is a Decimal, the value is applied to both Cost and Usage. If it is an Object, the engine MUST use the specific metric key.
    * **Rule-level Priority:** Use the `Applicability` from the matching inclusion rule. If multiple rules match under `OR`, the engine MUST use the highest percentage for each respective metric.
    * **Fallback:** Use the top-level `Applicability` if no rule-level value is provided.

### Dependency Logic

1. **Polymorphic Handling:** Engines MUST check the type of the `Applicability` field. If a metric key (e.g., `Cost`) is missing from an `Applicability` object, the engine SHOULD assume `0.0` for that specific metric.
2. **Conflict Resolution:** If `IsGlobalScope` is `true`, rule-level applicability in the `Inclusions` array is ignored in favor of the top-level `Applicability` attribute.

## Column ID
ContractCommitmentScope

## Display Name
Contract Commitment Scope

## Description
A structured definition of the specific entities to which a contract commitment applies, including inclusion/exclusion logic and applicability percentages.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Column type | Dimension |
| Feature level | Mandatory |
| Allows nulls | False |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |

## Introduced (version)

1.4