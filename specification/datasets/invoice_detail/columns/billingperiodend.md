# Billing Period End

[Billing Period End](#col) represents the [exclusive end bound](#term) of a [billing period](#term). For example, a time period where [Billing Period Start](#col) is '2024-01-01T00:00:00Z' and [Billing Period End](#col) is '2024-02-01T00:00:00Z' includes [charges](#term) for January since [Billing Period Start](#col) represents the [inclusive start bound](#term), but does not include [charges](#term) for February since [Billing Period End](#col) represents the [exclusive end bound](#term).

## Requirements

[BillingPeriodEnd](#col) MUST adhere to the following requirements:

* [BillingPeriodEnd](#col) MUST be of type Date/Time.
* [BillingPeriodEnd](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [BillingPeriodEnd](#col) MUST NOT be null.
* [BillingPeriodEnd](#col) MUST be the [exclusive end bound](#term) of the [billing period](#term).
* [BillingPeriodEnd](#col) for a given [InvoiceId](#col) and [InvoiceIssuerName](#col) MUST match [CostAndUsage.BillingPeriodEnd](#col:CostAndUsage.BillingPeriodEnd) for the same [CostAndUsage.InvoiceId](#col:CostAndUsage.InvoiceId) and [CostAndUsage.InvoiceIssuerName](#col:CostAndUsage.InvoiceIssuerName).

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The [exclusive end bound](#term) of a [billing period](#term).

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | False                                           |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attr)                       |

## Version Introduced

1.4
