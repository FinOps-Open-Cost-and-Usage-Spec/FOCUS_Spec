# Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

The FOCUS-defined properties are:

* `Allocated Ratio`: The ratio of a [*charge*](#glossary:charge) that this allocation represents.
* `Usage Unit`: Unit being measured used to calculate this allocation.
* `Usage Quantity`: The value of the charge applied to a single contract term.

In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.

## Requirements

### Column Requirements

The AllocatedMethodDetails column adheres to the following requirements:

* AllocatedMethodDetails SHOULD be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the data generator supports [Data Generator-Calculated Split Cost Allocation](#datagenerator-calculatedsplitcostallocationhandling).
* AllocatedMethodDetails MUST be of type String.
* AllocatedMethodDetails MUST conform to [StringHandling](#stringhandling) requirements.
* AllocatedMethodDetails MUST conform to [JsonObjectFormat](#jsonobjectformat) requirements.
* AllocatedMethodDetails nullability is defined as follows:
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.

### Object Schema Requirements

Allocated Method Details consists of a valid JSON object which contains an array of key-value objects describing the one or more factors (allocation properties) that determined the split cost allocation. Each object consists of FOCUS-defined keys but can be extended to provide additional details about the allocation.

When AllocatedMethodDetails is not null, the JsonObjectFormat for AllocatedMethodDetails adheres to the following requirements:
* AllocatedMethodDetails MUST have a top-level key "Elements" which contains an array.
* Each item in "Elements" MUST be an object.
  * Objects inside "Elements" MUST conform to [KeyValueFormat](#key-valueformat) requirements.
    * FOCUS-defined allocation properties adhere to the following additional requirements:
      * Allocation property key MUST match the spelling and casing specified for the FOCUS-defined property.
      * Allocation property value MUST be of the type specified for that property.
      * Allocation properties MUST adhere to additional normative requirements specific to that property.
    * Data generator-defined allocation properties MAY be included in "Elements".
      * Allocation property keys MUST begin with the string "x_" unless it is a FOCUS-defined allocation property.
* AllocatedMethodDetails root object MAY contain additional data generator-defined items, in addition to "Elements".

### Content Requirements

The following keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined keys will appear in the list below and data generator-defined keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

<b>Allocated Ratio</b>

Allocated Ratio communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#allocatedmethodid) and Usage Unit property.

The "AllocatedRatio" property adheres to the following requirements:

* "AllocatedRatio" MUST be included inside each "Elements" object.
* Values for "AllocatedRatio" MUST be a decimal value compatible with [NumericFormat](#numericformat) representing the allocated charge's percentage of the origin charge.
* Values for all "AllocatedRatio" properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).

<b>Usage Unit</b>

Usage Unit communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property.

The "UsageUnit" property adheres to the following requirements:

* "UsageUnit" MUST be included inside an "Elements" object if "UsageQuantity" allocation property is included in that "Elements" object, otherwise "UsageUnit" MAY be included in each "Elements" object.
* Values for "UsageUnit" MUST capture the unit or component of data generator's documented [AllocationMethod](#allocationmethodid) that was used to determine the "AllocatedRatio" value.
* Values for "UsageUnit" SHOULD conform to [UnitFormat](#unitformat) requirements.

<b>Usage Quantity</b>

Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.

The "UsageQuantity" property adheres to the following requirements:

* "UsageQuantity" MAY be included inside an "Elements" object when that "Elements" object contains a "UsageUnit" allocation property.
* Values for "UsageQuantity" MUST be compatible with NumericFormat.
* Values for "UsageQuantity" SHOULD capture the quantity or volume of the "UsageUnit" measured by the data generator that was used to determine the "AllocatedRatio" value.

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

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for AllocatedMethodDetails. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#numericformat) allows for multiple numeric data types and precisions, but JDT requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

### Scenario 1: Single "UsageUnit" value used for allocation

When only a single "UsageUnit" is used to calculate the allaction.

```json
{
  "Elements" : [ {
    "AllocatedRatio" : 0.1,
    "UsageUnit" : "Hours",
    "UsageQuantity" : 300
    }
  ]
}
```
### Scenario 2: Multiple "UsageUnit" values used for allocation

When multiple "UsageUnit" values are used to calculate the allaction, another object is added to the "Elements" collection.

```json
{
  "Elements": [
    {
      "AllocatedRatio": 0.05,
      "UsageUnit": "CPU",
      "UsageQuantity": 0.5
    },
    {
      "AllocatedRatio": 0.1,
      "UsageUnit": "Memory",
      "UsageQuantity": 4
    }
  ]
}
```
### Scenario 3: Data generator omits keys that are not required

This data generator does not wish to supply the "UsageUnit" or "UsageQuantity" keys but still provides cost allocation with some additional allocation method details. In this case, "UsageUnit" and "UsageQuantity" are omitted, and only the "AllocatedRatio" is supplied.

```json
{
  "Elements" : [ {
    "AllocatedRatio" : 0.45
    }
  ]
}
```
### Scenario 4: Additional non-FOCUS specified properties

A data generator can add additional properties if they feel more context is helpful or necessary to the practitioner. In this scenario, the data generator is supplying additional context that shows only 0.5 of a unit was used. However, since 1 unit was requested by the service this allocation represents, the allocation is being charged at 1 regardless.

```json
{
  "Elements": [
    {
      "AllocatedRatio": 0.6,
      "UsageUnit": "vCPU",
      "UsageQuantity": 1,
      "x_ReservedVCPU": 1,
      "x_UsedVCPU": 0.5,
      "x_AllocatedVCPU": 1
    }
  ]
}
```
## Column ID

AllocatedMethodDetails

## Display Name

Allocated Method Details

## Description

A set of properties describing how resources are allocated in data generator-defined split cost allocation.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Recommended     |
| Allows nulls    | True            |
| Data type       | JSON            |
| Value format    | [JSON Object Format](#jsonobjectformat) |

## Introduced (version)

1.3
