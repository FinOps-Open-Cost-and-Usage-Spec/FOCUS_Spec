# Contract Commitment Created

[Contract Commitment Created](#col) is the timestamp when the [Contract Commitment](#ds) record was first created. This timestamp facilitates auditability of the contract commitment lifecycle.

## Requirements

[ContractCommitmentCreated](#col) MUST adhere to the following requirements:

* [ContractCommitmentCreated](#col) MUST be of type Date/Time.
* [ContractCommitmentCreated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ContractCommitmentCreated](#col) MUST NOT be null.
* [ContractCommitmentCreated](#col) MUST represent the moment in time the [ContractCommitment](#ds) record was instantiated.

## Column ID

ContractCommitmentCreated

## Display Name

Contract Commitment Created

## Description

The timestamp when the contract commitment record was first created.

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
