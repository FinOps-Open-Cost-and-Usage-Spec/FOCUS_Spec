# Billing Period Start

[Billing Period Start](#col) represents the [inclusive start bound](#term) of a [billing period](#term). For example, a time period where [Billing Period Start](#col) is '2024-01-01T00:00:00Z' and [Billing Period End](#col) is '2024-02-01T00:00:00Z' includes [charges](#term) for January since [Billing Period Start](#col) represents the [inclusive start bound](#term), but does not include [charges](#term) for February since [Billing Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[BillingPeriodStart](#col) MUST adhere to the following requirements:

* [BillingPeriodStart](#col) MUST be of type Date/Time.
* [BillingPeriodStart](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [BillingPeriodStart](#col) MUST NOT be null.
* [BillingPeriodStart](#col) MUST be the [inclusive start bound](#term) of the [billing period](#term).

## Column ID

BillingPeriodStart

## Display Name

Billing Period Start

## Description

The [inclusive start bound](#term) of a [billing period](#term).

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
