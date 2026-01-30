# Contract Commitment Scope

Contract Commitment Scope is a structured definition of the specific entities to which a contract commitment applies, with both inclusionary and exclusionary logic.

## Requirements

ContractCommitmentScope adheres to the following requirements:

* ContractCommitmentScope MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentScope MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractCommitmentScope MUST NOT be null.

## Logical Schema Structure

ContractCommitmentScope contains a structured JSON object defining the logical boundaries of a commitment.

### Top-Level Attributes

| Attribute | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `IsGlobalScope` | Boolean | No | If `true`, the commitment applies to all resources. Defaults to `false`.  Exclusions are still processed if present. |
| `IsComplexScope` | Boolean | No | If `true`, indicates logic exceeds schema capabilities. Defaults to `false`. |
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
| `Exists` | Checks if the dimension is present and not null. | `Values` can be `["*"]` |
| `DoesNotExist` | Checks if the dimension is missing or null. | `Values` can be `["*"]` |

### Wildcard Handling

ContractCommitmentScope uses a reserved string to represent global or unrestricted boundaries within a specific Dimension.

| Reserved Value | Description | Supported Operators |
| :--- | :--- | :--- |
| `"*"` | Represents all possible values for the specified Dimension. | `In`, `Contains` |

#### Wildcard Behavior Rules

1. **Inclusion Logic:** When `["*"]` is used in an Inclusion rule, the rule evaluates to `True` for every resource, effectively making the commitment "Organization-wide" for that specific Dimension.
2. **Exclusion Logic:** When `["*"]` is used in an Exclusion rule, the rule evaluates to `True` for every resource, effectively excluding all resources (this is typically used only in combination with `ExclusionOperator: "AND"` for surgical filtering).
3. **Implicit Wildcards:** If a Dimension (e.g., `RegionId`) is omitted entirely from the `Inclusions` array, it is treated as an implicit wildcard (unrestricted) unless the `InclusionOperator` is set to `AND`.

## Examples

The following examples demonstrate how to model common contract commitment scenarios using ContractCommitmentScope.

### Global Applicability
An Enterprise Discount Program (EDP) or a global Savings Plan that applies to all resources across the entire provider footprint.

```json
{
  "IsGlobalScope": true
}
```

### Global Applicability with Specific Exceptions
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

### Complex Fallback
A commitment with non-linear or proprietary logic (e.g., "Applies to the top 10% of compute spend"). While this situation can be described in ContractCommitmentDescription, the data generator signals that this cannot be parsed by standard engines in ContractCommitmentScope.

```json
{
  "IsComplexScope": true
}
```

## Implementation Guidance

This section provides technical requirements for engineers developing processing engines that consume ContractCommitmentScope.

### Processing Workflow
The evaluation of a resource against a commitment scope MUST follow a strict linear progression to ensure predictable results.

1.  **Normalization:** Convert the resource attribute and the Scope `Values` to a consistent case (default: lowercase) for comparison.
2.  **Inclusion Evaluation:** * Iterate through the `Inclusions` array. 
    * Apply the `InclusionOperator` (AND/OR) to the results of each rule. 
    * If the final inclusion result is `False`, the resource is **NOT** eligible; terminate evaluation.
3.  **Exclusion Evaluation:** * Iterate through the `Exclusions` array.
    * Apply the `ExclusionOperator` (AND/OR) to the results of each rule.
    * If the final exclusion result is `True`, the resource is **NOT** eligible; terminate evaluation.
4.  **Final Validation:** If the resource passes step 2 and is not discarded by step 3, it is **Eligible**.

### Evaluation Priority 

1. **Complexity Check:** If `IsComplexScope` is `true`, flag for manual handling. Stop.
2. **Inclusion Stage:** If `IsGlobalScope` is `true`, result is **True**.
    - If `IsGlobalScope` is `false/null`, evaluate the `Inclusions` array. 
    - If the result of this stage is **False**, the resource is **Out of Scope**.
3. **Exclusion Stage:** If `Exclusions` is present, evaluate it.
    - If the result is **True**, the resource is **Out of Scope**.
4. **Final Result:** If stage 2 is True and stage 3 is False, the resource is **In Scope**.

### Dependency Logic

To ensure data quality and predictable engine behavior, the processing engine MUST enforce the following structural requirements within the `ContractCommitmentScope` object:

1. **Standard Mode:** When `IsGlobalScope` is `false`, `null`, or **absent** AND `IsComplexScope` is `false`, `null`, or **absent**, the object MUST contain both `InclusionOperator` and `Inclusions`.
2. **Override Mode:** If either `IsGlobalScope` or `IsComplexScope` is `true`, all other attributes are optional and SHOULD be omitted to minimize payload size.
3. **Conflicting Flags:** If both `IsGlobalScope` and `IsComplexScope` are set to `true`, the `IsGlobalScope` flag MUST take precedence, and the commitment MUST be treated as globally applicable.
4. **Exclusion Optionality:** The `Exclusions` array and `ExclusionOperator` are always optional. If `Exclusions` is absent, the engine MUST assume a result of `False` for the Exclusion Stage (nothing is removed).

### Handling Edge Cases

| Scenario | Expected Behavior |
| :--- | :--- |
| **Empty Inclusions** | Should return `False`. A commitment with no inclusion rules cannot match any resource. |
| **Empty Exclusions** | Should return `False` for the exclusion stage (meaning nothing is excluded). |
| **Missing Dimension** | If a resource does not possess the column specified in `Dimension`, the rule evaluates to `False` (except for the `DoesNotExist` operator). |
| **Malformed JSON** | If the `ContractCommitmentScope` contains invalid JSON, the engine MUST flag the row as an error and treat the scope as "Indeterminate." |

### Case Sensitivity and Special Characters
To maintain multi-cloud compatibility, the following standards are required:

* **Case Insensitivity:** By default, string comparisons (`In`, `StartsWith`, `Contains`) SHOULD be case-insensitive to account for variations between cloud provider APIs (e.g., `us-east-1` vs `US-EAST-1`).
* **Tag Parsing:** When the `Dimension` is `Tags`, the engine should look for a `Key:Value` pair. The `Contains` operator is the recommended method for matching specific tag-value combinations.
* **Wildcard Priority:** The wildcard `"*"` MUST be evaluated first. If found within an `In` operator, the individual rule result is immediately `True`.

### Performance Optimization
For large datasets (millions of usage rows), engines SHOULD:
1.  **Pre-compile** the `ContractCommitmentScope` logic into a reusable boolean function for each commitment.
2.  **Filter by Region first**, as `RegionId` is typically the highest-cardinality dimension and can quickly discard the majority of non-matching usage rows.

## Column ID

ContractCommitmentScope

## Display Name

Contract Commitment Scope

## Description

A structured definition of the specific entities to which a contract commitment applies.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | JSON           |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat) |

## Introduced (version)

1.4
