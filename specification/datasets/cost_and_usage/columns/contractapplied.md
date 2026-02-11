# Contract Applied

Contract Applied is a set of properties that associate a charge with one or more [*contract commitments*](#glossary:contract-commitment), denoted as key-value pairs in a JSON object.  Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with a service provider.

## Requirements

### Column Requirements

The ContractApplied column adheres to the following requirements:

* ContractApplied MUST be of type String.
* ContractApplied MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractApplied MUST conform to [JsonObjectFormat](#attributes.jsonobjectformat) requirements.
* ContractApplied nullability is defined as follows:
  * ContractApplied MUST NOT be null when one or more *contract commitments* are applied to the *charge*.
* ContractApplied MUST conform to [AllocatedMethodDetailsObject](#datasets.costandusage.contractappliedobject) requirements when ContractApplied is not null.

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
| Column type     | Dimension and Metric                                 |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | JSON                                                 |
| Value format    | [JSON Object Format](#attributes.jsonobjectformat)   |

## Introduced (version)

1.3

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

The ContractAppliedObject adheres to the following requirements:

* ContractAppliedObject MUST have a top-level property key "Elements".
* ContractAppliedObject MAY contain additional data generator-defined root object property keys, in addition to ContractAppliedObject.Elements.
* ContractAppliedObject MUST have property keys that begin with the string "x_" unless it is the top-level property key "Elements".
* ContractAppliedObject.Elements MUST adhere to the following requirements:
  * ContractAppliedObject.Elements MUST be of type Array.
  * ContractAppliedObject.Elements[\*] MUST be of type JSON object.
  * ContractAppliedObject.Elements[\*] MUST conform to [KeyValueFormat](#attributes.key-valueformat) requirements.
  * ContractAppliedObject.Elements[\*] MUST NOT have nested property key-value pairs.
  * ContractAppliedObject.Elements[\*] MAY contain data generator-defined allocation properties.
  * ContractAppliedObject.Elements[\*] MUST have property keys that begin with the string "x_" unless it is a FOCUS-defined allocation property.
  * ContractAppliedObject.Elements[\*] MUST have custom key-value pairs documented by the data generator.

  * The ContractAppliedObject.Elements[\*].ContractId property key adheres to the following requirements:
    * ContractAppliedObject.Elements[\*].ContractId MUST be present inside each ContractAppliedObject.Elements object.
    * ContractAppliedObject.Elements[\*].ContractId MUST be of type String.
    * ContractAppliedObject.Elements[\*].ContractId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
    * ContractAppliedObject.Elements[\*].ContractId nullability is defined as follows:
      * ContractAppliedObject.Elements[\*].ContractId MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
      * ContractAppliedObject.Elements[\*].ContractId MUST NOT be null when a *charge* is related to a *contract commitment*.
    * When ContractAppliedObject.Elements[\*].ContractId is not null, ContractAppliedObject.Elements[\*].ContractId adheres to the following additional requirements:
      * ContractAppliedObject.Elements[\*].ContractId MUST be a unique identifier within the service provider.
      * ContractAppliedObject.Elements[\*].ContractId SHOULD be a fully-qualified identifier.

  * The ContractAppliedObject.Elements[\*].ContractCommitmentID property key adheres to the following requirements:
    * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST be present inside each ContractAppliedObject.Elements object.
    * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST be of type String.
    * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST conform to [StringHandling](#attributes.stringhandling) requirements.
    * ContractAppliedObject.Elements[\*].ContractCommitmentID nullability is defined as follows:
      * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
      * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST NOT be null when a *charge* is related to a *contract commitment*.
    * When ContractAppliedObject.Elements[\*].ContractCommitmentID is not null, ContractAppliedObject.Elements[\*].ContractCommitmentID adheres to the following additional requirements:
      * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST be a unique identifier within the service provider.
      * ContractAppliedObject.Elements[\*].ContractCommitmentID SHOULD be a fully-qualified identifier.
      * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST have one and only one parent ContractAppliedObject.Elements[\*].ContractID.
      * ContractAppliedObject.Elements[\*].ContractCommitmentID MUST be equal to ResourceID when ChargeCategory is "Purchase".
      * ContractAppliedObject.Elements[\*].ContractCommitmentID MAY be equal to ContractAppliedObject.Elements[\*].ContractID.

  * The ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost property key adheres to the following requirements:
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST be present inside each ContractAppliedObject.Elements object.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST be of type Decimal.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST be a valid decimal value.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST be denominated in the BillingCurrency.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost nullability is defined as follows:
      * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MUST NOT be null when ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity is null.
      * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost MAY be null in all other cases.

  * The ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity property key adheres to the following requirements:
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST be present inside each ContractAppliedObject.Elements object.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST be of type Decimal.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST be a valid decimal value.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST be denominated in the ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity nullability is defined as follows:
      * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MUST NOT be null when ContractAppliedObject.Elements[\*].ContractCommitmentAppliedCost is null.
      * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity MAY be null in all other cases.

  * The ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit property key adheres to the following requirements:
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit MUST be present inside each ContractAppliedObject.Elements object.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit MUST be of type String.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit MUST conform to [StringHandling](#attributes.stringhandling) requirements.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
    * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit nullability is defined as follows:
      * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit MUST be null when ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity is null.
      * ContractAppliedObject.Elements[\*].ContractCommitmentAppliedUnit MUST NOT be null when ContractAppliedObject.Elements[\*].ContractCommitmentAppliedQuantity is not null.

## Object ID

ContractAppliedObject

## Object Display Name

Contract Applied Object

### Overview

#### Array of Objects

The parent array is called `Elements` and contains one or more objects which communicate information about how an allocated record was calculated.

| Key | ValueType | Required | Description |
| ----- | ---- | ---------- | ----------- |
| Elements | Array | True | The parent array containing one or more objects which communicate information about how contract commitments were applied to the charge. |

#### Object Entries

The `Elements` array contains one or more objects, each of which contains the following entries:

| Key                               | Key Type    | Feature Level | Allows Nulls | Data Type |
| --------------------------------- | ----------- | ------------- | ------------ | --------- |
| ContractID                        | Dimension   | Conditional   | False        | String    |
| ContractCommitmentID              | Dimension   | Conditional   | False        | String    |
| ContractCommitmentAppliedCost     | Dimension   | Conditional   | True         | Numeric   |
| ContractCommitmentAppliedQuantity | Dimension   | Conditional   | True         | Numeric   |
| ContractCommitmentAppliedUnit     | Dimension   | Conditional   | True         | String    |

### Descriptions

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

### Example

```json
{
  "Elements" : [ {
    "ContractID" : "12345",
    ContractAppliedObject.Elements[\*].ContractCommitmentID : "23456",
    "ContractCommitmentAppliedCost" : 500000.00
  }, {
    "ContractID" : "12345",
    ContractAppliedObject.Elements[\*].ContractCommitmentID : "34567",
    "ContractCommitmentAppliedQuantity" : 10000.00,
    "ContractCommitmentAppliedUnit" : "compute_hours"
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
          "ContractID": { "type": "string" },
          ContractAppliedObject.Elements[\*].ContractCommitmentID: { "type": "string" }
        },
        "optionalProperties": {
          "ContractCommitmentAppliedCost": { "type": "float64" },
          "ContractCommitmentAppliedQuantity": { "type": "float64" },
          "ContractCommitmentAppliedUnit": { "type": "float64" }
        },
        "additionalProperties": true
      }
    }
  },
  "additionalProperties": true
}
```

NOTE: The above JSON Type Definition (JTD) is an approximation of the expected contents of this column, but it should not be considered normative because it cannot accurately describe the normative requirements (above) for ContractApplied. Where there are discrepancies, deference will be given to the normative requirements. For example, [NumericFormat](#attributes.numericformat) allows for multiple numeric data types and precisions, but JTD requires both to be specified; other numeric data types and precisions allowable under NumericFormat are considered valid.

## Example Scenarios

### Scenario 1: Initial contract commitment

A single Cost and Usage charge represents the values stated on a contract and its three contract commitments agreed between a service provider and a customer:

1) 12345: Spend $500k overall.  (This is the value of the contract, and thus ContractID = ContractCommitmentID.)
2) 23456: Spend $25k on a particular service.
3) 34567: Consume 100k compute hours on a particular resource type.

The Charge Category is denoted as Purchase, and the Contract ID, Resource ID, and Contract Commitment ID are all denoted as 12345.

```json
{
  "ResourceID": "12345",
  "ChargeCategory": "Purchase",
  "BilledCost": 500000.00,
  "EffectiveCost": 0.00,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "12345",
        "ContractCommitmentAppliedCost": 500000.00
      }, {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "23456",
        "ContractCommitmentAppliedCost": 25000.00
      }, {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "34567",
        "ContractCommitmentAppliedQuantity": 100000.00,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
```

### Scenario 2: Contract commitment usage with no custom columns

Assume the contract commitment as described in Scenario 1.  Assume that only 50% of cost and usage gets applied to the contract commitments, per the contract terms.

A single Cost and Usage charge for `myResource1` carries Effective Cost of 30 (denominated in USD) and Consumed Quantity of 1 (denominated in compute hours).  The Charge Category is denoted as Usage.

This applies to the contract commitments in the following manner:

```json
{
  "ResourceID": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "12345",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "23456",
        "ContractCommitmentAppliedCost": 15.00
      }, {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
```

### Scenario 3: Contract commitment usage with custom columns

The same as Scenario 2, except a custom key-value pair `x_ContractCommitmentCostBalance` is provided by the data generator.   This datapoint represents the value remaining on a given contract commitment.

```json
{
  "ResourceID": "myResource1",
  "ChargeCategory": "Usage",
  "BilledCost": 0.00,
  "EffectiveCost": 30.00,
  "ConsumedQuantity": 1,
  "ContractApplied":
    {
      "Elements": [ {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "12345",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 499985.00
      }, {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "23456",
        "ContractCommitmentAppliedCost": 15.00,
        "x_ContractCommitmentCostBalance": 24985.00
      }, {
        "ContractID": "12345",
        ContractAppliedObject.Elements[\*].ContractCommitmentID: "34567",
        "ContractCommitmentAppliedQuantity": 0.50,
        "ContractCommitmentAppliedUnit": "compute_hours"
      } ]
    }
```
