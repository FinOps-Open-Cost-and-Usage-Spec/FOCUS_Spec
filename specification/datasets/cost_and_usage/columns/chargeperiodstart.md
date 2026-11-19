# Charge Period Start

[Charge Period Start](#col) represents the [inclusive start bound](#term) of a [charge period](#term). For example, a time period where [Charge Period Start](#col) is '2024-01-01T00:00:00Z' and [Charge Period End](#col) is '2024-01-02T00:00:00Z' includes [charges](#term) for January 1 since [Charge Period Start](#col) represents the [inclusive start bound](#term), but does not include [charges](#term) for January 2 since [Charge Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[ChargePeriodStart](#col) MUST adhere to the following requirements:

* [ChargePeriodStart](#col) MUST be of type Date/Time.
* [ChargePeriodStart](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [ChargePeriodStart](#col) MUST NOT be null.
* [ChargePeriodStart](#col) MUST be the [inclusive start bound](#term) of the effective period of the [charge](#term).

## Column ID

ChargePeriodStart

## Display Name

Charge Period Start

## Description

The [inclusive start bound](#term) of a [charge period](#term).

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
