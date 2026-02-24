# Contract Commitment Unit

The Contract Commitment Unit represents a service-provider-specified measurement unit for the amount declared in Contract Commitment Quantity. Contract Commitment Unit complements the Contract Commitment Quantity metric.

## Requirements

The ContractCommitmentUnit column MUST adhere to the following requirements:

* ContractCommitmentUnit MUST be of type String.
* ContractCommitmentUnit MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* The ContractCommitmentUnit column MUST adhere to the following nullability requirements:
  * ContractCommitmentUnit MUST be null when ContractCommitmentQuantity is null.
  * ContractCommitmentUnit MUST NOT be null when ContractCommitmentQuantity is not null.

## Column ID

ContractCommitmentUnit

## Display Name

Contract Commitment Unit

## Description

A service-provider-specified measurement unit for the amount declared in Contract Commitment Quantity.

## Content Constraints

| Constraint      | Value                                                |
|:----------------|:-----------------------------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit Format](#attributes.unitformat) recommended    |

## Introduced (version)

1.3
