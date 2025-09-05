# Allocated Resource Details

Allocated Resource Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

The allocated_resource_details column adheres to the following requirements:

* allocated_resource_details SHOULD be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports [provider-calculated split cost allocation](#provider-calculated-split-cost-allocation).
* allocated_resource_details MUST be of type String.
* allocated_resource_details MUST conform to [StringHandling](#stringhandling) requirements.
* allocated_resource_details MUST conform to [ObjectFormat](#objectformat) requirements.
  * allocated_resource_details MUST conform to ObjectFormat schema requirements below.
* allocated_resource_details nullability is defined as follows:
  * allocated_resource_details MUST be null when a charge is not related to a provider-calculated split cost allocation.
  * allocated_resource_details SHOULD NOT be null when a charge is related to a provider-calculated split cost allocation.

## Object Schema

Allocated Resource Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

If allocated_resource_details is not null, the ObjectFormat for allocated_resource_details adheres to the following requirements:
* allocated_resource_details MUST have a top-level key "Elements" which contains an array.
* Each item in "Elements" MUST be an object.
  * Objects inside "Elements" MUST conform to [KeyValueFormat](#key-valueformat) requirements.
  * Objects inside "Elements" MUST contain key-value pairs (allocation properties).
    * FOCUS-defined allocation properties adhere to the following additional requirements:
      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.
      * Allocation property value MUST be of the type specified for that property.
      * Allocation property MUST adhere to additional normative requirements specific to that property.
    * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.
* allocated_resource_details root object MAY contain additional items, in addition to "Elements".

### FOCUS-Defined Allocation Properties

The following keys are used for allocation properties to facilitate querying data across allocations and across providers. Focus-defined keys will appear in the list below and Provider-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

FOCUS-defined allocation properties adhere to the following requirements:

* "AllocatedRatio" MUST be included inside each "Elements" object.
  * Values for "AllocatedRatio" MUST be a decimal value compatible with [NumericFormat](#numericformat) representing the allocated charge's percentage of the origin charge.
  * Values for "AllocatedRatio" across all allocated records related to a single origin record MUST sum up to 1 (100%).
* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.
  * Values for "UsageUnit" MUST capture the unit or component of provider's documented [AllocationMethod](#allocationmethod) that was used to determine the "AllocatedRatio" value.
  * Values for "UsageUnit" SHOULD conform to [UnitFormat](#unitformat) requirements.
* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.
  * Values for "UsageQuantity" MUST be compatible with NumericFormat.
  * Values for "UsageQuantity" SHOULD capture the quantity or volume of the "UsageUnit" measured by the provider that was used to determine the "AllocatedRatio" value.

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| Elements | Array | TRUE | The parent array containing one or more objects which communicate information about how an allocated record was calculated. |
| AllocatedRatio | Numeric | TRUE | Percentage of overall cost derived from corresponding method and meter. |
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

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column but cannot accurately describe the normative requirements for allocated_resource_details. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JDT requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Column ID

allocated_resource_details

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
