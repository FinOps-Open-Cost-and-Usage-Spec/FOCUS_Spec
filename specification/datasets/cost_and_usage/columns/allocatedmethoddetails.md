# Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

## Requirements

### Column Requirements

AllocatedMethodDetails MUST adhere to the following requirements:

* AllocatedMethodDetails MUST be of type String.
* AllocatedMethodDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedMethodDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* AllocatedMethodDetails MUST adhere to the following nullability requirements:
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

The AllocatedMethodDetailsObject MUST adhere to the following requirements:

* AllocatedMethodDetailsObject MUST conform to the [AllocatedMethodDetailsObjectSchema](#schemas.datasets.costandusage.allocatedmethoddetailsobjectschema) JSON Schema.
* AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST represent the allocated charge's percentage of the origin charge.
* Values for all AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio properties across all allocated charges related to a single origin charge MUST sum up to 1 (100%).
* AllocatedMethodDetailsObject.Elements[\*].UsageUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST represent the unit or component of data generator's documented [AllocationMethod](#datasets.costandusage.allocatedmethodid) which was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.
* AllocatedMethodDetailsObject.Elements[\*].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements[\*].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.

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

The following property keys are used for allocation properties to facilitate querying data across allocations and across data generators. Focus-defined property keys will appear in the list below and data generator-defined property keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

<b>Allocated Ratio</b>

Allocated Ratio communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#datasets.costandusage.allocatedmethodid) and Usage Unit property.

<b>Usage Unit</b>

Usage Unit communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property.

<b>Usage Quantity</b>

Usage Quantity communicates the volume that was consumed or used, denominated in the Usage Unit property value.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:allocatedmethoddetails).
* For the JSON schema, please see [Allocated Method Details Object Schema](#schemas.datasets.contractcommitment.allocatedmethoddetailsobjectschema).

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

### Object ID

AllocatedMethodDetailsObject

### Object Display Name

Allocated Method Details Object

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
