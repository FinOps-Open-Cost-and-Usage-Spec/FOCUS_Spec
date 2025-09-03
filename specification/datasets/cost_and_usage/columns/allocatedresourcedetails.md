# Allocated Resource Details

Allocated Resource Details provides information about how resources are allocated when using split cost allocation.

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

Allocated Resource Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

If AllocatedResourceDetails is not null, the ObjectFormat for AllocatedResourceDetails adheres to the following requirements:
* ObjectFormat for AllocatedResourceDetails MUST be a valid JSON object.
* AllocatedResourceDetails MUST have a top-level key "Elements" which contains an array.
* Each item in "Elements" MUST be an object.
  * Objects inside "Elements" MUST conform to [KeyValueFormat](#key-valueformat) requirements.
  * Objects inside "Elements" MUST contain key-value pairs (allocation properties).
    * FOCUS-defined allocation properties adhere to the following additional requirements:
      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.
      * Allocation property value MUST be of the type specified for that property.
      * Allocation property MUST adhere to additional normative requirements specific to that property.
    * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.
* AllocatedResourceDetails root object MAY contain additional items, in addition to "Elements".

### FOCUS-Defined Allocation Properties

The following keys are used for allocation properties to facilitate querying data across allocations and across providers. Focus-defined keys will appear in the list below and Provider-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

FOCUS-defined allocation properties adhere to the following requirements:

* "AllocatedRatio" MUST be included inside each "Elements" object.
  * Values for "AllocatedRatio" MUST be a decimal value compatible with [NumericFormat](#numericformat) representing the allocated charge's percentage of the origin charge.
  * Values for "AllocatedRatio" across all allocated records related to a single origin record MUST sum up to 1 (100%).
* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.
  * Values for "UsageUnit" SHOULD capture the unit or component of provider's documented [AllocationMethod](#allocationmethod) that was used to determine the "AllocatedRatio" value.
  * Values for "UsageUnit" are RECOMMENDED to use [UnitFormat](#unitformat).
* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.
  * Values for "UsageQuantity" MUST be compatible with NumericFormat.
  * Values for "UsageQuantity" SHOULD capture the quantity or volume of the "UsageUnit" measured by the provider that was used to determine the "AllocatedRatio" value.

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| Elements | Array | TRUE | The parent array containing one or more objects which communicate information about how an allocated record was calculated. |
| AllocatedRatio | Numeric | TRUE | Percentage of overall cost derived from corresponding method and metric. |
| UsageUnit | [String](#stringhandling) | Conditional | Unit being measured used to calculate allocation. |
| UsageQuantity | Numeric | FALSE | Volume of UsageUnit consumed or used. |

### Example

```json
{
  "Elements" : [ {
    "AllocatedRatio" : 0.05,
    "UsageUnit" : "CPU",
    "UsageQuantity" : 0.5
  }, {
    "AllocatedRatio" : 0.1,
    "UsageUnit" : "Memory",
    "UsageQuantity" : 4
  } ]
}
```

### JSON Type Definition

```json
{
  "properties": {
    "Elements": {
      "elements": {
        "properties": {
          "AllocatedRatio": { "type": "float64" }
        },
        "optionalProperties": {
          "UsageUnit": { "type": "string" },
          "UsageQuantity": { "type": "float64" }
        },
        "additionalProperties": true
      }
    }
  },
  "additionalProperties": true
}
```

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column but cannot accurately describe the normative requirements for AllocatedResourceDetails. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JDT requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Column ID

AllocatedResourceDetails

## Display Name

Allocated Resource Details

## Description

Allocated Resource Details provides information about how resources are allocated when using split cost allocation.

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
