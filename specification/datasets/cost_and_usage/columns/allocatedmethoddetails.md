# Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Resource Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

## Requirements

### Column Requirements

The AllocatedMethodDetails column adheres to the following requirements:

* AllocatedMethodDetails SHOULD be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports [provider-calculated split cost allocation](#provider-calculated-split-cost-allocation).
* AllocatedMethodDetails MUST be of type String.
* AllocatedMethodDetails MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedMethodDetails MUST conform to [ObjectFormat](#objectformat) requirements.
  * AllocatedMethodDetails MUST conform to ObjectFormat schema requirements below.
* AllocatedMethodDetails nullability is defined as follows:
  * AllocatedMethodDetails MUST be null when a charge is not related to a provider-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a provider-calculated split cost allocation.

### Object Schema Requirements

Allocated Method Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

If AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:
* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.
* Each item in "Elements" MUST be an object.
  * Objects inside "Elements" MUST conform to [KeyValueFormat](#key-valueformat) requirements.
  * Objects inside "Elements" MUST contain key-value pairs (allocation properties).
    * FOCUS-defined allocation properties adhere to the following additional requirements:
      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.
      * Allocation property value MUST be of the type specified for that property.
      * Allocation property MUST adhere to additional normative requirements specific to that property.
    * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.
* AllocatedMethodDetails root object MAY contain additional items, in addition to "Elements".

### Content Requirements

The following keys are used for allocation properties to facilitate querying data across allocations and across providers. Focus-defined keys will appear in the list below and Provider-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

**Allocated Ratio**

Percentage of overall cost derived from corresponding method and metric.

The AllocatedRatio property adheres to the following requirements:

* "AllocatedRatio" MUST be included inside each "Elements" object.
* Values for "AllocatedRatio" MUST be a decimal value compatible with [NumericFormat](#numericformat) representing the allocated charge's percentage of the origin charge.
* Values for "AllocatedRatio" across all allocated records related to a single origin record MUST sum up to 1 (100%).

**Usage Unit**

Unit being measured used to calculate allocation.

* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.
* Values for "UsageUnit" MUST capture the unit or component of provider's documented [AllocationMethod](#allocationmethod) that was used to determine the "AllocatedRatio" value.
* Values for "UsageUnit" SHOULD conform to [UnitFormat](#unitformat) requirements.

**Usage Quantity**

Volume of UsageUnit consumed or used.

* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.
* Values for "UsageQuantity" MUST be compatible with NumericFormat.
* Values for "UsageQuantity" SHOULD capture the quantity or volume of the "UsageUnit" measured by the provider that was used to determine the "AllocatedRatio" value.

## Overview

### Array of Objects

The parent array is called `Elements` and contains one or more objects which communicate information about how an allocated record was calculated.

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| Elements | Array | True | The parent array containing one or more objects which communicate information about how an allocated record was calculated. |

### Object Entries

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| AllocatedRatio | Numeric | True | Percentage of overall cost derived from corresponding method and metric. |
| UsageUnit | [String](#stringhandling) | Conditional | Unit being measured used to calculate allocation. |
| UsageQuantity | Numeric | False | Volume of UsageUnit consumed or used. |

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

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column but cannot accurately describe the normative requirements for AllocatedMethodDetails. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JDT requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Column ID

AllocatedMethodDetails

## Display Name

Allocated Method Details

## Description

Allocated Method Details provides information about how resources are allocated when using split cost allocation.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | JSON            |
| Value format    | [JSON Object Format](#jsonobjectformat) |

## Introduced (version)

1.3
