# Contract Applied

Contract Applied is a set of four datapoints that associate a charge to one or more [*contract commitments*](#glossary:contract-commitment), denoted as key-value pairs in JSON format.  Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with a provider.

The datapoints are:

* `Contract Commitment ID`: The unique identifier representing the contract line item.
* `Contract Commitment Applied Cost`: The value of the charge applied to the contract line item.
* `Contract Commitment Applied Quantity`: The usage of the charge applied to the contract line item.
* `Contract Commitment Applied Unit`: The unit of measure for the usage of the charge applied to the contract line item.

The ContractApplied column adheres to the following requirements:

* ContractApplied MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *contract commitments*.
* ContractApplied MUST conform to [KeyValueFormat](#key-valueformat) requirements.
* ContractApplied property keys SHOULD conform to [PascalCase](#glossary:pascalcase) format.
* ContractApplied nullability is defined as follows:
  * ContractApplied MUST be null when [ContractID](#contractid) is null.
  * ContractApplied MUST NOT be null when ContractID is not null.
* When ContractApplied is not null, ContractApplied adheres to the following additional requirements:
  * ContractApplied MUST contain four key-value pairs, representing ContractCommitmentID, ContractCommitmentAppliedCost, ContractCommitmentAppliedQuantity, and ContractCommitmentAppliedUnit.
  * ContractApplied MAY contain further key-value pairs, representing custom datapoints provided by the data generator.
  * When ContractApplied custom key-value pairs are present:
    * ContractApplied custom key-value pairs MUST be documented by the data generator.
    * ContractApplied custom key-value pairs MUST NOT be nested.

## JSON Datapoints

The next sections describe the four datapoints contained within Contract Applied, each of which have their own requirements.

### Contract Commitment ID

A Contract Commitment ID is a provider-assigned identifier describing an agreement negotiated between a provider and a customer.  Contracts can include commitment to a certain amount of spend or usage over an agreed period of time.

The ContractCommitmentID column adheres to the following requirements:

* ContractCommitmentID MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *contract commitments*.
* ContractCommitmentID MUST be of type String.
* ContractCommitmentID MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentID nullability is defined as follows:
  * ContractCommitmentID MUST be null when a [*charge*](#glossary:charge) is not related to a *contract commitment*.
  * ContractCommitmentID MUST NOT be null when a *charge* is related to a *contract commitment*.
* When ContractCommitmentID is not null, ContractCommitmentID adheres to the following additional requirements:
  * ContractCommitmentID MUST be a unique identifier within the provider.
  * ContractCommitmentID SHOULD be a fully-qualified identifier.
* ContractCommitmentID MUST have one and only one parent [ContractID](#contractid).
* ContractCommitmentID MAY be equal to ContractID.

### Contract Commitment Applied Cost

Contract Commitment Applied Cost represents the cost of the charge applied to the contract line item.  Contract Commitment Applied Cost is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as negotiated between a provider and a customer.

The ContractCommitmentAppliedCost column adheres to the following requirements:

* ContractCommitmentAppliedCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *contract commitments*.
* ContractCommitmentAppliedCost MUST be of type Decimal.
* ContractCommitmentAppliedCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractCommitmentAppliedCost nullability is defined as follows:
  * ContractCommitmentAppliedCost MUST be null when ContractCommitmentID is null.
  * ContractCommitmentAppliedCost MUST NOT be null when ContractCommitmentID is not null.
  * ContractCommitmentAppliedCost MUST NOT be null when ContractCommitmentQuantity is null.
  * ContractCommitmentAppliedCost MAY be null when ContractCommitmentQuantity is not null.
* ContractCommitmentAppliedCost MUST be a valid decimal value.
* ContractCommitmentAppliedCost MUST be denominated in the BillingCurrency.

### Contract Commitment Applied Quantity

Contract Commitment Applied Quantity represents the quantity of the charge applied to the contract line item.  Contract Commitment Applied Quantity is associated with the contract line item via Contract Commitment ID.  Contract Commitment Applied Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as negotiated between a provider and a customer.

The ContractCommitmentAppliedQuantity column adheres to the following requirements:

* ContractCommitmentAppliedQuantity MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *contract commitments*.
* ContractCommitmentAppliedQuantity MUST be of type Decimal.
* ContractCommitmentAppliedQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* ContractCommitmentAppliedQuantity nullability is defined as follows:
  * ContractCommitmentAppliedQuantity MUST be null when ContractCommitmentID is null.
  * ContractCommitmentAppliedQuantity MUST NOT be null when ContractCommitmentID is not null.
  * ContractCommitmentAppliedQuantity MUST NOT be null when ContractCommitmentCost is null.
  * ContractCommitmentAppliedQuantity MAY be null when ContractCommitmentCost is not null.
* ContractCommitmentAppliedQuantity MUST be a valid decimal value.

### Contract Commitment Applied Unit

The Contract Commitment Applied Unit represents a provider-specified measurement unit for the usage declared in Contract Commitment Applied Quantity. Contract Commitment Applied Unit complements the Contract Commitment Applied Quantity metric.

The ContractCommitmentAppliedUnit column adheres to the following requirements:

* ContractCommitmentAppliedUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *contract commitments*.
* ContractCommitmentAppliedUnit MUST be of type String.
* ContractCommitmentAppliedUnit MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentAppliedUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* ContractCommitmentAppliedUnit nullability is defined as follows:
  * ContractCommitmentAppliedUnit MUST be null when ContractCommitmentAppliedQuantity is null.
  * ContractCommitmentAppliedUnit MUST NOT be null when ContractCommitmentAppliedQuantity is not null.

# Examples

## Example 1

A single charge has two contractual commitments applied:

1) Spend a certain amount of money on the relevant service.
2) Consume a certain number of compute hours on the relevant resource type.

```json
{
"ContractApplied": [
          {
               "ContractCommitmentID": "12346",
               "ContractCommitmentAppliedCost": 100.00,
               "ContractCommitmentAppliedQuantity": null,
               "ContractCommitmentAppliedUnit": null
           },
           {
               "ContractCommitmentID": "23456",
               "ContractCommitmentAppliedCost": null,
               "ContractCommitmentAppliedQuantity": 10,
               "ContractCommitmentAppliedUnit": "compute_hours"
           }
     ]
}
```

## Example 2

The same as Example 1, except a custom key-value pair `x_ContractCommitmentCostBalance` is provided by the data generator.   This datapoint represents the value remaining on a burndown contract commitment, which started at $500k.

```json
{
"ContractApplied": [
          {
               "ContractCommitmentID": "12346",
               "ContractCommitmentAppliedCost": 100.00,
               "ContractCommitmentAppliedQuantity": null,
               "ContractCommitmentAppliedUnit": null,
               "x_ContractCommitmentCostBalance": 499000.00
           },
           {
               "ContractCommitmentID": "23456",
               "ContractCommitmentAppliedCost": null,
               "ContractCommitmentAppliedQuantity": 10,
               "ContractCommitmentAppliedUnit": "compute_hours",
               "x_ContractCommitmentCostBalance": null
           }
     ]
}
```

## Column ID

ContractApplied

## Display Name

Contract Applied

## Description

A set of four datapoints that associate a charge to one or more [*contract commitments*](#glossary:contract-commitment).

## Content Constraints

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Column type   | Dimension and Metric               |
| Feature level | Conditional                        |
| Allows nulls  | True                               |
| Data type     | JSON                               |
| Value format  | [KeyValueFormat](#key-valueformat) |

## Introduced (version)

1.3
