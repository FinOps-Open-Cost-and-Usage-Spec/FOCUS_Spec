# Contract Commitment Period End

[Contract Commitment Period End](#col) represents the [exclusive end bound](#term) of a contract commitment period. For example, a time period where [Contract Commitment Period Start](#col:ContractPeriodStart) is '2024-01-01T00:00:00Z' and [Contract Commitment Period End](#col) is '2024-01-02T00:00:00Z' includes January 1 2024 since [Contract Commitment Period Start](#col) represents the [inclusive start bound](#term), but does not include January 1 2025 since [Contract Commitment Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[ContractCommitmentPeriodEnd](#col) MUST adhere to the following requirements:

* [ContractCommitmentPeriodEnd](#col) MUST be of type Date/Time.
* [ContractCommitmentPeriodEnd](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ContractCommitmentPeriodEnd](#col) MUST NOT be null.
* [ContractCommitmentPeriodEnd](#col) MUST be the [exclusive end bound](#term) of the effective period of the [contract commitment](#term).

## Column ID

ContractCommitmentPeriodEnd

## Display Name

Contract Commitment Period End

## Description

The [exclusive end bound](#term) of a contract commitment period.

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

1.3
