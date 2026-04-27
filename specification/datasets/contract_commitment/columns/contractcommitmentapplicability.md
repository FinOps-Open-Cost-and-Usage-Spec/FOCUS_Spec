# Contract Commitment Applicability

Contract Commitment Applicability is a structured definition of the specific entities eligible for coverage under a [*contract commitment*](#glossary:contract-commitment). This column details inclusionary and exclusionary logic, as well as the specific portion of eligible cost or usage that is applicable.

## Requirements

ContractCommitmentApplicability MUST adhere to the following requirements:

* ContractCommitmentApplicability MUST be of type JSON Object (serialized as a String where necessary).
* ContractCommitmentApplicability MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentApplicability MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractCommitmentApplicability MUST conform to [ContractCommitmentApplicabilityObject](#datasets.contractcommitment.contractcommitmentapplicability.contractcommitmentapplicabilityobject) requirements.
* ContractCommitmentApplicability MUST NOT be null.

## Contract Commitment Applicability Object

Contract Commitment Applicability consists of a valid JSON object which contains a set of top-level property keys. These keys define entity-based inclusionary and exclusionary logic, as well as the portion of relevant cost and/or usage that is applicable to the *contract commitment*.

The following section details the normative requirements for the ContractCommitmentApplicabilityObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datasets.contractcommitment.contractcommitmentapplicability.schemastructure) and [Object Example](#datasets.contractcommitment.contractcommitmentapplicability.objectexample) sections.

## Object Requirements

ContractCommitmentApplicabilityObject MUST adhere to the following requirements:

* ContractCommitmentApplicabilityObject MUST conform to the [ContractCommitmentApplicabilityObjectSchema](#schemas.contractcommitment.contractcommitmentapplicabilityobjectschema) JSON Schema.
* ContractCommitmentApplicabilityObject.IsGlobalScope MUST be `true` if the *contract commitment* applies to all entities.
* ContractCommitmentApplicabilityObject.IsComplexScope MUST be `true` if the *contract commitment's* applicability logic exceeds schema capabilities.
* ContractCommitmentApplicabilityObject.Applicability.Cost MUST represent the fraction of an eligible charge's cost that is applicable to the commitment (0.0 to 1.0).
* ContractCommitmentApplicabilityObject.Applicability.Usage MUST represent the fraction of an eligible charge's usage that is applicable to the commitment (0.0 to 1.0).
* ContractCommitmentApplicabilityObject.Inclusions[\*].Applicability.Cost MUST represent the fraction of an eligible charge's cost that is applicable to the commitment (0.0 to 1.0).
* ContractCommitmentApplicabilityObject.Inclusions[\*].Applicability.Usage MUST represent the fraction of an eligible charge's usage that is applicable to the commitment (0.0 to 1.0).
* ContractCommitmentApplicabilityObject.Inclusions[\*].Dimension SHOULD represent a column in [Cost and Usage](#datasets.costandusage).
* ContractCommitmentApplicabilityObject.Exclusions[\*].Dimension SHOULD represent a column in [Cost and Usage](#datasets.costandusage).
* ContractCommitmentApplicabilityObject.Inclusions[\*].Values MUST contain only the single string "*" if the wildcard is present.
* ContractCommitmentApplicabilityObject.Exclusions[\*].Values MUST contain only the single string "*" if the wildcard is present.

## Object Schema Structure

ContractCommitmentApplicability contains a structured JSON object defining the logical boundaries and the applicability percentage of a commitment.

### Top-Level Properties

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `IsGlobalScope` | Boolean | No | If `true`, the commitment applies to all entities. Defaults to `false`. |
| `IsComplexScope` | Boolean | No | If `true`, indicates logic exceeds schema capabilities. Defaults to `false`. |
| `Applicability` | Object | No | The fractional mapping for metrics. If omitted, both `Cost` and `Usage` keys default to `1.0`. |
| `InclusionOperator` | String | Conditional | Required only if `IsGlobalScope` and `IsComplexScope` are both `false` or null. Valid values: `And`, `Or`. Must be omitted if Global or Complex scope is true. |
| `Inclusions` | Array | Conditional | Required only if `IsGlobalScope` and `IsComplexScope` are both `false` or null. List of `Rule` objects defining the boundary. Must be omitted if Global or Complex scope is true. |
| `ExclusionOperator` | String | Conditional | Required only if `Exclusions` are present. Defines the relationship for `Exclusions`. Valid values: `And`, `Or`. |
| `Exclusions` | Array | No | List of `Rule` objects defining entities to be removed from the boundary. |

### Rule Object

| Key | Type | Description |
| :--- | :--- | :--- |
| `Dimension` | String | A valid FOCUS Column Name (e.g., `SkuId`, `RegionId`). |
| `Operator` | String | The comparison logic to apply. Must be one of the Supported Operators. |
| `Values` | Array | A list of strings to compare. A value of `["*"]` acts as a global wildcard. |
| `Applicability` | Object | Optional. The specific fraction of applicability for entities matching this rule. Overrides the top-level `Applicability`. |

### Applicability Object

| Key | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `Cost` | Decimal | 1.0 | Fraction of an eligible charge's cost applicable to the *contract commitment*. |
| `Usage` | Decimal | 1.0 | Fraction of an eligible charge's usage applicable to the *contract commitment*. |

### Supported Operators

| Operator | Logic | Usage Example |
| :--- | :--- | :--- |
| `In` | Exact match against any item in the list. | `["us-east-1", "us-west-2"]` |
| `NotIn` | Does not match any item in the list. | `["123456789"]` |
| `StartsWith` | String prefix match. | `["prod-"]` |
| `NotStartsWith` | Does not begin with the specified prefix. | `["test-"]` |
| `Contains` | Substring match anywhere in the value. | `["database"]` |
| `NotContains` | Substring is not present in the value. | `["sandbox"]` |
| `EndsWith` | String suffix match. | `["-temp"]` |
| `Exists` | Checks if the dimension is present and not null. | `Values` must be `["*"]` |
| `DoesNotExist` | Checks if the dimension is missing or null. | `Values` must be `["*"]` |

### Wildcard Handling

ContractCommitmentApplicability uses a reserved string to represent global or unrestricted boundaries within a specific Dimension.

| Reserved Value | Description | Supported Operators |
| :--- | :--- | :--- |
| `"*"` | Represents all possible values for the specified Dimension. | `In`, `Contains`, `Exists`, `DoesNotExist` |

### Wildcard Behavior Rules

1. **Inclusion Logic:** When `["*"]` is used in an Inclusion rule, the rule evaluates to `True` for every entity, effectively making the commitment "Organization-wide" for that specific Dimension.
2. **Exclusion Logic:** When `["*"]` is used in an Exclusion rule, the rule evaluates to `True` for every entity, effectively excluding all entities (this is typically used only in combination with `ExclusionOperator: "And"` for surgical filtering).
3. **Implicit Wildcards:** If a Dimension (e.g., `RegionId`) is omitted entirely from the `Inclusions` array, it is treated as an implicit wildcard (unrestricted).

## Object Implementation Guidance

### Processing Workflow

The evaluation of an entity against a commitment applicability must follow a strict linear progression:

1. **Normalization:** Convert the entity attribute and the Scope `Values` to a consistent case (default: lowercase) for comparison.
2. **Inclusion Evaluation:** Iterate through `Inclusions`. If a match is found, record the rule-level `Applicability` if present. Apply `InclusionOperator`. If result is `False`, terminate.
3. **Exclusion Evaluation:** Iterate through `Exclusions`. If `True`, terminate evaluation.
4. **Applicability Resolution:**
   * **Inheritance:** A matching rule's `Applicability` object takes precedence over the top-level object.
   * **Defaulting:** If a metric key (`Cost` or `Usage`) is missing within a provided `Applicability` object, the engine must default that specific value to `1.0`.
   * **Rule-level Priority:** Use the `Applicability` from the matching inclusion rule. If multiple rules match under `Or`, the engine must use the highest percentage for each respective metric.
   * **Fallback:** Use the top-level `Applicability` if no rule-level value is provided.

### Integration with Commitment Logic

The evaluation of **Applicability** percentages must be contextually aligned with the [Contract Commitment Model](#datasets.contractcommitment.contractcommitmentmodel) and [Contract Commitment Fulfillment Interval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval):

* **Continuous Models:** Applicability percentages must be applied to each discrete unit of activity (e.g., every hour) within the **Fulfillment Interval**. If the commitment is not fully utilized by eligible entities within that hour, the remaining capacity expires.
* **Discontinuous Models:** Applicability percentages determine the portion of aggregate activity that counts toward fulfillment over the entire **Interval** (e.g., a full year).

### Dependency Logic

1. **Consistency:** Engines should expect a JSON Object and should not support scalar (Decimal/Float) values for this field to ensure compatibility with typed database schemas.
2. **Conflict Resolution:** If `IsGlobalScope` or `IsComplexScope` is `true`, the `Inclusions` array must be empty or omitted. Additionally, `IsGlobalScope` and `IsComplexScope` must both not be `true` at the same time. Engines should validate these structural constraints before processing.

## Object Example

Here is a basic example of the object format, describing organization-wide coverage **except** for Database services running in BillingAccountId 123456789012.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:contractcommitmentapplicability).
* For the JSON schema, please see [Contract Commitment Applicability Object Schema](#schemas.contractcommitment.contractcommitmentapplicabilityobjectschema).

```json
{
  "IsGlobalScope": true,
  "ExclusionOperator": "And",
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

## Object ID

ContractCommitmentApplicabilityObject

## Object Display Name

Contract Commitment Applicability Object

## Column ID

ContractCommitmentApplicability

## Display Name

Contract Commitment Applicability

## Description

A structured definition of the specific entities to which a contract commitment applies, including inclusion/exclusion logic and applicability percentages.

## Content Constraints

| Constraint | Value |
| :--- | :--- |
| Dataset | [Contract Commitment](#datasets.contractcommitment) |
| Column type | Dimension |
| Feature level | Mandatory |
| Allows nulls | False |
| Data type | JSON |
| Value format | [JSON Object Format](#attributes.jsonobjectformat) |
| Object | [ContractCommitmentApplicabilityObject](#datasets.contractcommitment.contractcommitmentapplicability.contractcommitmentapplicabilityobject) |

## Introduced (version)

1.4
