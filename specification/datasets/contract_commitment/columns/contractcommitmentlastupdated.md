# Contract Commitment Last Updated

[Contract Commitment Last Updated](#col) is the timestamp when the [Contract Commitment](#ds) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a Contract Commitment record, particularly if corrections or status changes have been applied to the record after its initial creation.

## Requirements

[ContractCommitmentLastUpdated](#col) MUST adhere to the following requirements:

* [ContractCommitmentLastUpdated](#col) MUST be of type Date/Time.
* [ContractCommitmentLastUpdated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ContractCommitmentLastUpdated](#col) MUST NOT be null.
* [ContractCommitmentLastUpdated](#col) MUST represent the most recent moment in time when any column value of the [ContractCommitment](#ds) record was created or modified.
* [ContractCommitmentLastUpdated](#col) MUST be greater than or equal to [ContractCommitmentCreated](#col).

## Column ID

ContractCommitmentLastUpdated

## Display Name

Contract Commitment Last Updated

## Description

The timestamp when the contract commitment record was last updated.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | Date/Time                                            |
| Value format               | [Date/Time Format](#attr)                            |

## Version Introduced

1.4
