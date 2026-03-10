# Contract Applied

Contract Applied is a set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment), denoted as key-value pairs in a JSON object.  Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with a service provider.

## Requirements

The ContractApplied column MUST adhere to the following requirements:

* ContractApplied MUST be of type String.
* ContractApplied MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractApplied MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractApplied nullability is defined as follows:
  * ContractApplied MUST NOT be null when one or more *contract commitments* are applied to the *charge*.
* ContractApplied MUST conform to [ContractAppliedObject](#datasets.costandusage.contractapplied.contractappliedobject) requirements when ContractApplied is not null.

## Contract Applied Object

Contract Applied Object consists of a valid JSON object which contains an array of key-value objects describing the one or more contract commitments applied to the charge. Each object consists of FOCUS-defined property keys but can be extended to provide additional details about the contract application.

The FOCUS-defined properties are:

* `Contract ID`: The unique identifier representing a single contract.
* `Contract Commitment ID`: The unique identifier representing a single contract term.
* `Contract Commitment Applied Cost`: The value of the charge applied to a single contract term.
* `Contract Commitment Applied Quantity`: The usage of the charge applied to a single contract term.
* `Contract Commitment Applied Unit`: The unit of measure for the usage of the charge applied to a single contract term.

In addition to these, a data generator may include one or more custom properties, also denoted as key-value pairs.

### Object Requirements

The ContractAppliedObject MUST adhere to the following requirements:

* ContractAppliedObject MUST conform to the [ContractAppliedObjectSchema](#schemas.datasets.costandusage.contractappliedobjectschema) JSON Schema.
* ContractAppliedObject.Elements[\*] MUST NOT have nested property key-value pairs.
* ContractAppliedObject.Elements[\*].ContractId MUST be a unique identifier within the service provider.
* ContractAppliedObject.Elements[\*].ContractId SHOULD be a fully-qualified identifier.
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST be a unique identifier within the service provider.
* ContractAppliedObject.Elements[\*].ContractCommitmentId SHOULD be a fully-qualified identifier.
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST have one and only one parent ContractAppliedObject.Elements[\*].ContractId.
* ContractAppliedObject.Elements[\*].ContractCommitmentId MUST be equal to ResourceID when ChargeCategory is "Purchase".
* ContractAppliedObject.Elements[\*].ContractCommitmentId MAY be equal to ContractAppliedObject.Elements[\*].ContractId.
* ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST be denominated in the BillingCurrency.
* ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST be denominated in the ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit.
* ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.

### Array of Objects

The parent array is called `Elements` and contains one or more objects which communicate information about how an allocated record was calculated.

| Key | Value Type | Required | Description |
| ----- | ---- | ---------- | ----------- |
| Elements | Array | True | The parent array containing one or more objects which communicate information about how contract commitments were applied to the charge. |

### Object Entries

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key | Value Type | Feature Level | Description |
| ----- | ---- | ---------- | ----------- |
| ContractId | String | Required | Unique identifier for the contract. |
| ContractCommitmentId | String | Required | Unique identifier for the contract commitment term. |
| ContractCommitmentAppliedCost | Metric | Conditional | Cost value of the charge applied to the contract commitment. |
| ContractCommitmentAppliedQuantity | Metric | Conditional | Quantity of usage applied to the contract commitment. |
| ContractCommitmentAppliedUnit | String | Conditional | Unit of measure for the applied quantity. Required if Quantity is present. |

The following keys are used for contract application properties to facilitate querying data across allocations and across service providers. FOCUS-defined keys will appear in the list below, and custom keys will be prefixed with "x_" to make them easy to identify as well as prevent collisions.

<b>Contract ID</b>

Contract ID is a service-provider-assigned identifier for a contract describing the agreed terms between a service provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

<b>Contract Commitment ID</b>

A Contract Commitment ID is a service-provider-assigned identifier describing an agreement agreed between a service provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

<b>Contract Commitment Applied Cost</b>

Contract Commitment Applied Cost represents the cost of the charge applied to the contract line item.  Contract Commitment Applied Cost is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

<b>Contract Commitment Applied Quantity</b>

Contract Commitment Applied Quantity represents the quantity of the charge applied to the contract line item.  Contract Commitment Applied Quantity is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

<b>Contract Commitment Applied Unit</b>

The Contract Commitment Applied Unit represents a service-provider-specified measurement unit for the usage declared in Contract Commitment Applied Quantity. Contract Commitment Applied Unit complements the Contract Commitment Applied Quantity metric.

### Object Example

Here is a basic example of the object format.

* For more detailed examples, please see this column's entry in the JSON Object Examples appendix entry [here](#appendix.examples:jsonobject.examples:contractapplied).
* For the JSON schema, please see [Contract Applied Object Schema](#schemas.datasets.contractcommitment.contractappliedobjectschema).

```json
{
  "Elements" : [ {
    "ContractId" : "12345",
    "ContractCommitmentId" : "23456",
    "ContractCommitmentAppliedCost" : 500000.00
  }, {
    "ContractId" : "12345",
    "ContractCommitmentId" : "34567",
    "ContractCommitmentAppliedQuantity" : 10000.00,
    "ContractCommitmentAppliedUnit" : "compute_hours"
  } ]
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

A set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :----------------------------------------------------|
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension and Metric                                 |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat)   |
| Object          | [ContractAppliedObject](#datasets.costandusage.contractapplied.contractappliedobject)

## Introduced (version)

1.3
