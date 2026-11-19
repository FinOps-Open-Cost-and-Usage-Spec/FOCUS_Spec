# Contract Commitment Period Start

[Contract Commitment Period Start](#col) represents the [inclusive start bound](#term) of a contract commitment period. For example, a time period where [Contract Commitment Period Start](#col) is '2024-01-01T00:00:00Z' and [Contract Commitment Period End](#col) is '2025-01-01T00:00:00Z' includes January 1 2024 since [Contract Commitment Period Start](#col) represents the [inclusive start bound](#term), but does not include [charges](#term) for January 2 2025 since [Contract Commitment Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[ContractCommitmentPeriodStart](#col) MUST adhere to the following requirements:

* [ContractCommitmentPeriodStart](#col) MUST be of type Date/Time.
* [ContractCommitmentPeriodStart](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ContractCommitmentPeriodStart](#col) MUST NOT be null.
* [ContractCommitmentPeriodStart](#col) MUST be the [inclusive start bound](#term) of the effective period of the [contract commitment](#term).

## Column ID

ContractCommitmentPeriodStart

## Display Name

Contract Commitment Period Start

## Description

The [inclusive start bound](#term) of a contract commitment period.

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
