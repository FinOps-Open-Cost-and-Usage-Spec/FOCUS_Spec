# Charge Period End

[Charge Period End](#col) represents the [exclusive end bound](#term) of a [charge period](#term). For example, a time period where [Charge Period Start](#col) is '2024-01-01T00:00:00Z' and [Charge Period End](#col) is '2024-01-02T00:00:00Z' includes [charges](#term) for January 1 since [Charge Period Start](#col) represents the [inclusive start bound](#term), but does not include [charges](#term) for January 2 since [Charge Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[ChargePeriodEnd](#col) MUST adhere to the following requirements:

* [ChargePeriodEnd](#col) MUST be of type Date/Time.
* [ChargePeriodEnd](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ChargePeriodEnd](#col) MUST NOT be null.
* [ChargePeriodEnd](#col) MUST be the [exclusive end bound](#term) of the effective period of the [charge](#term).

## Column ID

ChargePeriodEnd

## Display Name

Charge Period End

## Description

The [exclusive end bound](#term) of a [charge period](#term).

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | False                                           |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attr)                       |

## Version Introduced

0.5
