# Contract Applied

Contract Applied is a set of four datapoints that associate a charge to one or more [*contract commitments*](#glossary:contract-commitment).  

The datapoints are:

* `Contract Commitment ID`: The unique identifier representing the contract line item.
* `Contract Commitment Applied Cost`: The value of the charge applied to the contract line item.
* `Contract Commitment Applied Quantity`: The usage of the charge applied to the contract line item.
* `Contract Commitment Applied Unit`: The unit of measure for the usage of the charge applied to the contract line item.

These datapoints are represented as key-value pairs in JSON format.  

Contract Applied allows the practitioner to track the progress of the commitments to which they have agreed with their provider.

The ContractApplied column adheres to the following requirements:

The next sections describe the four datapoints contained with Contract Applied, each of which have their own requirements.

### Contract Commitment ID

The ContractCommitmentID column adheres to the following requirements:

<<tbd>>

### Contract Commitment Applied Cost

The ContractCommitmentAppliedCost column adheres to the following requirements:

<<tbd>>

### Contract Commitment Applied Quantity

The ContractCommitmentAppliedQuantity column adheres to the following requirements:

<<tbd>>

### Contract Commitment Applied Unit

The ContractCommitmentAppliedUnit column adheres to the following requirements:

<<tbd>>

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
