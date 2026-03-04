# Contract Commitment Last Updated

A Contract Commitment Last Updated is the timestamp when the [Contract Commitment](#datasets.contractcommitment) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a Contract Commitment record, particularly if corrections or status changes have been applied to the record after its initial creation.

## Requirements

ContractCommitmentLastUpdated MUST adhere to the following requirements:

* ContractCommitmentLastUpdated MUST be of type Date/Time.
* ContractCommitmentLastUpdated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* ContractCommitmentLastUpdated MUST NOT be null.
* ContractCommitmentLastUpdated MUST represent the most recent moment in time when any column value of the Contract Commitment record was created or modified.
* ContractCommitmentLastUpdated MUST be greater than or equal to [ContractCommitmentCreated](#datasets.contractcommitment.contractcommitmentcreated).

## Column ID

ContractCommitmentLastUpdated

## Display Name

Contract Commitment Last Updated

## Description

The timestamp when the contract commitment record was last updated.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Date/Time                        |
| Value format    | [Date/Time Format](#attributes.date/timeformat) |

## Introduced (version)

1.4