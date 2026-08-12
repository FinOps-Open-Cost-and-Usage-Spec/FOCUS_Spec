# Allocated Method Details

Allocated Method Details provides information about how resources are allocated when usage records are split to support cost allocation requirements.

Allocated Method Details consists of a valid JSON object which contains an array consisting of key-value objects describing the one or more factors that determined the split cost allocation. Each object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

## Requirements

### Column Requirements

AllocatedMethodDetails MUST adhere to the following requirements:

* AllocatedMethodDetails MUST be of type JSON Object (serialized as a String where necessary).
* AllocatedMethodDetails MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AllocatedMethodDetails MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* AllocatedMethodDetails MUST adhere to the following nullability requirements:
  * AllocatedMethodDetails MUST be null when a charge is not related to a data generator-calculated split cost allocation.
  * AllocatedMethodDetails SHOULD NOT be null when a charge is related to a data generator-calculated split cost allocation.
* AllocatedMethodDetails MUST conform to [AllocatedMethodDetailsObject](#datamodel.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject) requirements when AllocatedMethodDetails is not null.

## Allocated Method Details Object

Allocated Method Details consists of a valid JSON object with a top level key of Elements containing an Array of entry objects. Each entry object consists of FOCUS-defined property keys but can be extended to provide additional details about the allocation.

The following section details the normative requirements for the AllocatedMethodDetailsObject and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject.objectschemastructure) and [Object Example](#datamodel.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject.objectexample) sections.

### Object Requirements

The AllocatedMethodDetailsObject MUST adhere to the following requirements:

* AllocatedMethodDetailsObject MUST conform to the [AllocatedMethodDetailsObjectSchema](#schemas.costandusage.allocatedmethoddetailsobjectschema) JSON Schema.
* AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio MUST represent the allocated charge's percentage of the origin charge.
* The sum of AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio across all allocated charges related to a single origin charge MUST be equal to 1 (100%).
* AllocatedMethodDetailsObject.Elements[\*].UsageUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* AllocatedMethodDetailsObject.Elements[\*].UsageUnit MUST represent the unit or component of data generator's documented [AllocationMethod](#datamodel.costandusage.allocatedmethodid) which was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.
* AllocatedMethodDetailsObject.Elements[\*].UsageQuantity SHOULD capture the quantity or volume of the AllocatedMethodDetailsObject.Elements[\*].UsageUnit measured by the data generator that was used to determine the AllocatedMethodDetailsObject.Elements[\*].AllocatedRatio value.

### Object Schema Structure

AllocatedMethodDetails contains a structured JSON object defining the allocation properties used to calculate a split cost allocation.

<div class="h7-nonindex">Top-Level Properties</div>

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Elements` | Array | True | The parent array containing one or more objects which communicate information about how an allocated record was calculated. |

<div class="h7-nonindex">Elements Object</div>

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `AllocatedRatio` | Numeric | True | Communicates the percentage of the [*Origin Charge*](#glossary:origin-charge) that this [*Allocated Charge*](#glossary:allocated-charge) derived from the corresponding [Allocated Method Id](#datamodel.costandusage.allocatedmethodid) and Usage Unit property. |
| `UsageUnit` | String | Conditional | Communicates the aspect of the documented Allocation Method Id being used to calculate the Allocated Ratio property and what is being measured by Usage Quantity property. <br><br>**Condition:** must be present if Usage Quantity is provided. |
| `UsageQuantity` | Numeric | False | Communicates the volume that was consumed or used, denominated in the Usage Unit property value. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Properties</div>

To facilitate querying data across allocations and across data generators, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `Elements`) or nested within the individual `Elements` objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:allocatedmethoddetails).
* For the JSON schema, please see [Allocated Method Details Object Schema](#schemas.costandusage.allocatedmethoddetailsobjectschema).

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

| Constraint                 | Value                                                                                                       |
| :------------------------- | :---------------------------------------------------------------------------------------------------------- |
| Dataset                    | [Cost and Usage](#datamodel.costandusage)                                                                   |
| Operating Model Conditions | Recommended when: [Includes Split Cost Allocation](#operatingmodelconditions.includessplitcostallocation)   |
| Column type                | Dimension / Metric                                                                                          |
| Feature level              | Recommended                                                                                                 |
| Allows nulls               | True                                                                                                        |
| Data type                  | JSON                                                                                                        |
| Value format               | [JSON Object Format](#attributes.jsonobjectformat)                                                          |
| Object                     | [AllocatedMethodDetailsObject](#datamodel.costandusage.allocatedmethoddetails.allocatedmethoddetailsobject) |

## Version Introduced

1.3
