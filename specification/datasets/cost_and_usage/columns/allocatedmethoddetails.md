# Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

## Requirements

### Column Requirements

The AllocatedMethodDetails column adheres to the following requirements:

* AllocatedMethodDetails MUST be of type String.
* AllocatedMethodDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedMethodDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* AllocatedMethodDetails nullability is defined as follows:
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.
* AllocatedMethodDetails MUST conform to [AllocatedMethodDetailsObject](#datasets.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject) requirements when AllocatedMethodDetails is not null.

## Allocated Method Details Object

Allocated Method Details consists of a valid JSON object with a top level key of Elements containing an Array of entry objects. Each entry object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

The FOCUS-defined properties are:

* `Allocated Ratio`: The ratio of a [*charge*](#glossary:charge) that this allocation represents.
* `Usage Unit`: Unit being measured used to calculate this allocation.
* `Usage Quantity`: The quantity of units used denominated by the defined usage unit.

In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.

### Object Requirements

The AllocatedMethodDetailsObject adheres to the following requirements:

* AllocatedMethodDetailsObject MUST have a top-level property key "Elements".
* AllocatedMethodDetailsObject MAY contain additional data generator-defined top-level property keys, in addition to AllocatedMethodDetailsObject.Elements.
* AllocatedMethodDetailsObject MUST have property keys that begin with the string "x_" unless it is the top-level property key "Elements".

* AllocatedMethodDetailsObject.Elements MUST adhere to the following requirements:
  * AllocatedMethodDetailsObject.Elements MUST be of type Array.
  * AllocatedMethodDetailsObject.Elements[\*] MUST be of type JSON object.
  * AllocatedMethodDetailsObject.Elements[\*] MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
  * AllocatedMethodDetailsObject.Elements[\*] MAY contain data generator-defined allocation properties.
  * AllocatedMethodDetailsObject.Elements[\*] MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined allocation property.
  
  * The AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio property key adheres to the following requirements:
    * AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST be present inside each AllocatedMethodDetailsObject.Elements object.
    * AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST be of type Decimal.
    * AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST conform to [NumericFormat](#attributes.numericformat) requirements.
    * AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST represent the allocated charge's percentage of the origin charge.
    * Values for all AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).
  
  * The AllocatedMethodDetailsObject.Elements[\*].UsageUnit property key adheres to the following requirements:
    * AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST be present inside an AllocatedMethodDetailsObject.Elements object if AllocatedMethodDetailsObject.Elements[*].UsageQuantity allocation property is present in that AllocatedMethodDetailsObject.Elements object
    * AllocatedMethodDetailsObject.Elements[\*].UsageUnit MAY be present inside an AllocatedMethodDetailsObject.Elements object if AllocatedMethodDetailsObject.Elements[*].UsageQuantity allocation property is not present in that AllocatedMethodDetailsObject.Elements object
    * AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST be of type String.
    * AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST conform to StringHandling requirements.
    * AllocatedMethodDetailsObject.Elements[\*].UsageUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
    * AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST represent the unit or component of data generator's documented [AllocationMethod](#datasets.costandusage.allocatedmethodid) which was used to determine the AllocatedMethodDetailsObject.Elements[*].AllocatedRatio value.
  
  * The AllocatedMethodDetailsObject.Elements[\*].UsageQuantity property key adheres to the following requirements:
    * AllocatedMethodDetailsObject.Elements[\*].UsageQuantity MUST be present inside an AllocatedMethodDetailsObject.Elements object if AllocatedMethodDetailsObject.Elements[*].UsageUnit allocation property is present in that AllocatedMethodDetailsObject.Elements object
    * AllocatedMethodDetailsObject.Elements[\*].UsageQuantity MUST be of type Decimal.
    * AllocatedMethodDetailsObject.Elements[\*].UsageQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
    * AllocatedMethodDetailsObject.Elements[\*].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements[\*].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.

### Object ID

AllocatedMethodDetailsObject

### Object Display Name

Allocated Method Details Object

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
| UsageUnit | [String](#attributes.stringhandling) | Conditional | Unit being measured used to calculate allocation. |
| UsageQuantity | Numeric | False | Volume of UsageUnit consumed or used. |

### Descriptions

The following property keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined property keys will appear in the list below and data generator-defined property keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

<b>Allocated Ratio</b>

Allocated Ratio communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#datasets.costandusage.allocatedmethodid) and Usage Unit property.

<b>Usage Unit</b>

Usage Unit communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property.

<b>Usage Quantity</b>

Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.

### Object Example

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

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for AllocatedMethodDetails. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#attributes.numericformat) allows for multiple numeric data types and precisions, but JTD requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Column ID

AllocatedMethodDetails

## Display Name

Allocated Method Details

## Description

A set of properties describing how resources are allocated in data generator-defined split cost allocation.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Recommended                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat)   |
| Object          | [AllocatedMethodDetailsObject](#datasets.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject)

## Introduced (version)

1.3
