# Payment Currency

[Payment Currency](#col) represents the currency in which the [invoice issuer](#term) requires settlement. This is the currency of the financial obligation created by the invoice, which may differ from the [Billing Currency](#col:CostAndUsage.BillingCurrency) and/or the source currency of the payer's funds or bank account. [Payment Currency](#col) allows FinOps practitioners to track settlement obligations and foreign exchange impacts.

## Requirements

[PaymentCurrency](#col) MUST adhere to the following requirements:

* [PaymentCurrency](#col) MUST be of type String.
* [PaymentCurrency](#col) MUST conform to [StringHandling](#attr) requirements.
* [PaymentCurrency](#col) MUST NOT be null.
* [PaymentCurrency](#col) MUST represent the currency in which the invoice payment was made or expected to be made.
* [PaymentCurrency](#col) MUST be expressed in [national currency](#term) (e.g., USD, EUR).

## Column ID

PaymentCurrency

## Display Name

Payment Currency

## Description

The currency in which the invoice is paid.

## Content Constraints

| Constraint                 | Value                                         |
| :------------------------- | :-------------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                         |
| Operating model conditions | [Includes Billing and Payment Currency Differences](#omc)                                                                   |
| Column type                | Dimension                                     |
| Feature level              | Conditional                                   |
| Allows nulls               | False                                         |
| Data type                  | String                                        |
| Value format               | [Currency Format](#attr)                      |

## Version Introduced

1.4
