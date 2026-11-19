# Contract Period Start

[Contract Period Start](#col) represents the [inclusive start bound](#term) of a contract period. For example, a time period where [Contract Period Start](#col) is '2024-01-01T00:00:00Z' and [Contract Period End](#col) is '2025-01-01T00:00:00Z' includes January 1 2024 since [Contract Period Start](#col) represents the [inclusive start bound](#term), but does not include January 2 2025 since [Contract Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[ContractPeriodStart](#col) MUST adhere to the following requirements:

* [ContractPeriodStart](#col) MUST be of type Date/Time.
* [ContractPeriodStart](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ContractPeriodStart](#col) MUST NOT be null.
* [ContractPeriodStart](#col) MUST be the [inclusive start bound](#term) of the effective period of the [contract](#term).

## Column ID

ContractPeriodStart

## Display Name

Contract Period Start

## Description

The [inclusive start bound](#term) of a contract period.

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
