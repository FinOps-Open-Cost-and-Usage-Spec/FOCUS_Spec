# Contract Applied

[Contract Applied](#col) is a set of properties that associate a [charge](#term) with one or more [contract commitments](#term), denoted as key-value pairs in a JSON object. [Contract Applied](#col) allows the practitioner to track the progress of the commitments to which they have agreed with a service provider.

## Requirements

### Column Requirements

[ContractApplied](#col) MUST adhere to the following requirements:

* [ContractApplied](#col) MUST be of type JSON Object (serialized as a String where necessary).
* [ContractApplied](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractApplied](#col) MUST conform to [JsonObjectFormat](#attr) requirements.
* [ContractApplied](#col) MUST NOT be null when one or more [contract commitments](#term) are applied to the [charge](#term).
* [ContractApplied](#col) MUST conform to [ContractAppliedObject](#obj) requirements when [ContractApplied](#col) is not null.

## Contract Applied Object

[Contract Applied Object](#obj) consists of a valid JSON object which contains an array of key-value objects describing the one or more contract commitments applied to the [charge](#term). Each object consists of FOCUS-defined property keys but can be extended to provide additional details about the contract application.

The following section details the normative requirements for the [ContractAppliedObject](#obj) and its nested properties. For a logical overview of the expected content, see the [Schema Structure](#datamodel.costandusage.contractapplied.contractappliedobject.objectschemastructure) and [Object Example](#datamodel.costandusage.contractapplied.contractappliedobject.objectexample) sections.

### Object Requirements

[ContractAppliedObject](#obj) MUST adhere to the following requirements:

* [ContractAppliedObject](#obj) MUST conform to the [ContractAppliedObjectSchema](#schema) JSON Schema.
* ContractAppliedObject.Elements[\*].ContractId MUST be a unique identifier within the service provider.
* ContractAppliedObject.Elements[\*].ContractId SHOULD be a fully-qualified identifier.
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST be a unique identifier within the service provider.
* ContractAppliedObject.Elements[\*].ContractCommitmentId SHOULD be a fully-qualified identifier.
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST have one and only one parent ContractAppliedObject.Elements[\*].ContractId.
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST match [ResourceId](#col) when [ChargeCategory](#col) is "Purchase" and the [charge](#term) represents a purchase of that [contract commitment](#term).
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST match [ResourceId](#col) when [ChargeCategory](#col) is "Usage" and the [charge](#term) represents an unused portion of that [contract commitment](#term).
* ContractAppliedObject.Elements[\*].ContractCommitmentId MAY match ContractAppliedObject.Elements[\*].ContractId.
* ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST be denominated in the [BillingCurrency](#col).
* ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST be denominated in the ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit.
* ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit SHOULD conform to [UnitFormat](#attr) requirements.

### Object Schema Structure

[ContractApplied](#col) contains a structured JSON object defining the allocation and application of a [charge](#term) against specific contract commitments.

<div class="h7-nonindex">Top-Level Properties</div>

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `Elements` | Array | True | The parent array containing one or more objects which communicate information about how contract commitments were applied to the [charge](#term). |

<div class="h7-nonindex">Elements Object</div>

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `ContractId` | String | Yes | A service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer. Contracts can include commitment to a certain amount of spend or usage over an agreed period of time. |
| `ContractCommitmentId` | String | Yes | A service-provider-assigned identifier describing an agreement agreed between a service provider and a customer. |
| `ContractCommitmentAppliedCost` | Decimal | Conditional | The cost of the [charge](#term) applied to the contract line item. It is associated with the contract line item via Contract Commitment ID, and is commonly used for monitoring progress towards fulfilling contractual commitments that may facilitate discounts for [resources](#term) or [services](#term) as agreed between a service provider and a customer. <br><br>**Condition:** Must be present if Quantity and Unit are not provided.                       |
| `ContractCommitmentAppliedQuantity` | Decimal | Conditional | The quantity of the [charge](#term) applied to the contract line item. It is associated with the contract line item via Contract Commitment ID, and is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [resources](#term) or [services](#term) as agreed between a service provider and a customer. <br><br>**Condition:** Must be present if Cost is not provided.                       |
| `ContractCommitmentAppliedUnit` | String | Conditional | A service-provider-specified measurement unit for the usage declared in Contract Commitment Applied Quantity. It complements the Contract Commitment Applied Quantity metric. <br><br>**Condition:** Must be present if Contract Commitment Applied Quantity is provided. |

### Object Implementation Guidance

<div class="h7-nonindex">Custom Properties</div>

To facilitate querying data across allocations and across service providers, a data generator may include one or more custom properties. These may be placed at the top level of the object (alongside `Elements`) or nested within the individual `Elements` objects. Custom keys must be prefixed with "x_" followed by PascalCase format (e.g., `x_MyCustomKey`) to make them easy to identify as well as prevent collisions with FOCUS-defined keys.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:contractapplied).
* For the JSON schema, please see [Contract Applied Object Schema](#schema).

```json
{
  "Elements": [
    {
      "ContractId": "12345",
      "ContractCommitmentId": "23456",
      "ContractCommitmentAppliedCost": 500000.00
    },
    {
      "ContractId": "12345",
      "ContractCommitmentId": "34567",
      "ContractCommitmentAppliedQuantity": 10000.00,
      "ContractCommitmentAppliedUnit": "compute_hours"
    }
  ]
}
```

### Object ID

ContractAppliedObject

### Object Display Name

Contract Applied Object

## Column ID

ContractApplied

## Display Name

Contract Applied

## Description

A set of properties that associate a [charge](#term) with one or more [contract commitments](#term).

## Content Constraints

| Constraint                 | Value                                              |
| :------------------------- | :------------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                              |
| Operating model conditions | [Includes Contract Commitments](#omc)                                                  |
| Column type                | Dimension / Metric                                 |
| Feature level              | Conditional                                        |
| Allows nulls               | True                                               |
| Data type                  | JSON                                               |
| Value format               | [JSON Object Format](#attr)                        |
| Object                     | [ContractAppliedObject](#obj)                                                          |

## Version Introduced

1.3
