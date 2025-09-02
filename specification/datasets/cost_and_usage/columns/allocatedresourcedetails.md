# Allocated Resource Details

Allocated Resource Details provides information critical in understanding how resources are allocated when using split cost allocation. This information includes: allocation method name, metric used to calculate cost, the usage value/quantity, and the ratio of the cost derived from the method.

The AllocatedResourceDetails column adheres to the following requirements:

* AllocatedResourceDetails SHOULD be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports [provider-calculated split cost allocation](#provider-calculated-split-cost-allocation).
* AllocatedResourceDetails MUST be of type String.
* AllocatedResourceDetails MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedResourceDetails MUST conform to [ObjectFormat](#objectformat) requirements.
  * AllocatedResourceDetails MUST conform to ObjectFormat schema requirements below.
* AllocatedResourceDetails nullability is defined as follows:
  * AllocatedResourceDetails MUST be null when a charge is not related to a provider-calculated split cost allocation.
  * AllocatedResourceDetails SHOULD NOT be null when a charge is related to a provider-calculated split cost allocation.

## Object Schema

If AllocatedResourceDetails is not null, the ObjectFormat for AllocatedResourceDetails adheres to the following requirements:
* ObjectFormat for AllocatedResourceDetails MUST be a single array.
* The array in AllocatedResourceDetails MUST consist of one or more objects.
  * Objects inside the array MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* Property keys MUST begin with the string "x_" unless it is a FOCUS-defined property.
* FOCUS-defined Allocation properties adhere to the following additional requirements:
  * Property key MUST match the spelling and casing specified for the FOCUS-defined property.
  * Property value MUST be of the type specified for that property.

### FOCUS-Defined Properties

The following keys should be used when applicable to facilitate querying data across allocations and across providers. Focus-defined keys will appear in the list below and Provider-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| AllocatedRatio | [Numeric](#numericformat) | TRUE | Percentage of overall cost derived from corresponding method and metric. |
| UsageUnit | [String](#stringhandling) | FALSE | Unit being measured used to calculate allocation. |
| UsageQuantity | Numeric | FALSE | Volume of UsageUnit consumed or used. |

### Example

```json
[
  {
    "AllocatedRatio": 0.05,
    "UsageUnit": "CPU",
    "UsageValue": 0.5
  },
  {
    "AllocatedRatio": 0.1,
    "UsageUnit": "Memory",
    "UsageValue": 4
  }
]
```

### JSON Type Definition

```json
{
  "elements": {
    "properties": {
      "AllocatedRatio": { "type": "float64" }
    },
    "optionalProperties": {
      "UsageUnit": { "type": "string" },
      "UsageValue": { "type": "float64" }
    },
    "additionalProperties": true
  }
}
```

NOTE: [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JDT requires both to be specified. Other numeric data types and precisions allowable under NumericFormat are considered valid.

## Column ID

AllocatedResourceDetails

## Display Name

Allocated Resource Details

## Description

Self-contained summary of the allocated cost's purpose and price.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | JSON            |
| Value format    | [Object](#objectformat) |

## Introduced (version)

1.3
