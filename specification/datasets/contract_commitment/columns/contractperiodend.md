# Contract Period End

[Contract Period End](#col) represents the [exclusive end bound](#term) of a contract period. For example, a time period where [Contract Period Start](#col) is '2024-01-01T00:00:00Z' and [Contract Period End](#col) is '2024-01-02T00:00:00Z' includes January 1 2024 since [Contract Period Start](#col) represents the [inclusive start bound](#term), but does not include January 1 2025 since [Contract Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[ContractPeriodEnd](#col) MUST adhere to the following requirements:

* [ContractPeriodEnd](#col) MUST be of type Date/Time.
* [ContractPeriodEnd](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ContractPeriodEnd](#col) MUST NOT be null.
* [ContractPeriodEnd](#col) MUST be the [exclusive end bound](#term) of the effective period of the [contract](#term).

## Column ID

ContractPeriodEnd

## Display Name

Contract Period End

## Description

The [exclusive end bound](#term) of a contract period.

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
