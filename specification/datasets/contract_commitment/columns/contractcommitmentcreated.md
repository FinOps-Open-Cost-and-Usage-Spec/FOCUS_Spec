# Contract Commitment Created

Contract Commitment Created is the timestamp when the [Contract Commitment](#datasets.contractcommitment) record was first created. This timestamp facilitates auditability of the contract commitment lifecycle.

## Requirements

ContractCommitmentCreated MUST adhere to the following requirements:

* ContractCommitmentCreated MUST be of type Date/Time.
* ContractCommitmentCreated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* ContractCommitmentCreated MUST NOT be null.
* ContractCommitmentCreated MUST represent the moment in time the [Contract Commitment](#datasets.contractcommitment) record was instantiated.

## Column ID

ContractCommitmentCreated

## Display Name

Contract Commitment Created

## Description

The timestamp when the contract commitment record was first created.

## Content Constraints

|    Constraint   |              Value              |
|:----------------|:--------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Date/Time                        |
| Value format    | [Date/Time Format](#attributes.date/timeformat) |

## Introduced (Version)

1.4
