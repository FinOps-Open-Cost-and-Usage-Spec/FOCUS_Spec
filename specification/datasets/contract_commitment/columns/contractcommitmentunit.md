# Contract Commitment Unit

The Contract Commitment Applied Unit represents a provider-specified measurement unit for the amount declared in Contract Commitment Applied Quantity. Contract Commitment Applied Unit complements the Contract Commitment Applied Quantity metric.

The ContractCommitmentAppliedUnit column adheres to the following requirements:

* ContractCommitmentAppliedUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentAppliedUnit MUST be of type String.
* ContractCommitmentAppliedUnit MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentAppliedUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* ContractCommitmentAppliedUnit nullability is defined as follows:
  * ContractCommitmentAppliedUnit MUST be null when ContractCommitmentAppliedQuantity is null.
  * ContractCommitmentAppliedUnit MUST NOT be null when ContractCommitmentAppliedQuantity is not null.

## Column ID

ContractCommitmentUnit

## Display Name

Contract Commitment Unit

## Description

A provider-specified measurement unit for the amount declared in Contract Commitment Applied Quantity.

## Content Constraints

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Column type   | Dimension                          |
| Feature level | Mandatory                          |
| Allows nulls  | True                               |
| Data type     | String                             |
| Value format  | \<not specified>                   |

## Introduced (version)

1.3
