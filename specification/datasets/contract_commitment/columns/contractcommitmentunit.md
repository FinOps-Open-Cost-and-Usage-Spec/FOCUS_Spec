# Contract Commitment Unit

The [Contract Commitment Unit](#col) represents a service-provider-specified measurement unit for the amount declared in [Contract Commitment Quantity](#col). [Contract Commitment Unit](#col) complements the [Contract Commitment Quantity](#col) metric.

## Requirements

[ContractCommitmentUnit](#col) MUST adhere to the following requirements:

* [ContractCommitmentUnit](#col) MUST be of type String.
* [ContractCommitmentUnit](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractCommitmentUnit](#col) SHOULD conform to [UnitFormat](#attr) requirements.
* [ContractCommitmentUnit](#col) MUST adhere to the following nullability requirements:
  * [ContractCommitmentUnit](#col) MUST be null when [ContractCommitmentQuantity](#col) is null.
  * [ContractCommitmentUnit](#col) MUST NOT be null when [ContractCommitmentQuantity](#col) is not null.

## Column ID

ContractCommitmentUnit

## Display Name

Contract Commitment Unit

## Description

A service-provider-specified measurement unit for the amount declared in [Contract Commitment Quantity](#col).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | True                                                 |
| Data type                  | String                                               |
| Value format               | [Unit Format](#attr) recommended                     |

## Version Introduced

1.3
