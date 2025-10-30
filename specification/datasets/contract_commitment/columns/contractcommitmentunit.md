# Contract Commitment Unit

The Contract Commitment Unit represents a service-provider-specified measurement unit for the amount declared in Contract Commitment Quantity. Contract Commitment Unit complements the Contract Commitment Quantity metric.

## Requirements

ContractCommitmentUnit adheres to the following requirements:

* ContractCommitmentUnit MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentUnit MUST be of type String.
* ContractCommitmentUnit MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* ContractCommitmentUnit nullability is defined as follows:
  * ContractCommitmentUnit MUST be null when ContractCommitmentQuantity is null.
  * ContractCommitmentUnit MUST NOT be null when ContractCommitmentQuantity is not null.

## Column ID

ContractCommitmentUnit

## Display Name

Contract Commitment Unit

## Description

A service-provider-specified measurement unit for the amount declared in Contract Commitment Quantity.

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
