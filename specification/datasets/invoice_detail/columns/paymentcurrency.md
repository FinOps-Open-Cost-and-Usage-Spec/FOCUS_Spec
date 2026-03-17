# Payment Currency

Payment Currency represents the currency in which the invoice issuer requires settlement.  This is the currency of the financial obligation created by the invoice, which may differ from the [Billing Currency](#datasets.costandusage.billingcurrency) and/or the source currency of the payer's funds or bank account.  Payment Currency allows FinOps practitioners to track settlement obligations and foreign exchange impacts.

## Requirements

PaymentCurrency MUST adhere to the following requirements:

* PaymentCurrency MUST be of type String.
* PaymentCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PaymentCurrency MUST NOT be null.
* PaymentCurrency MUST represent the currency in which the invoice payment was made or expected to be made.
* PaymentCurrency MUST be expressed in [*national currency*](#glossary:national-currency) (e.g., USD, EUR).

## Column ID

PaymentCurrency

## Display Name

Payment Currency

## Description

The currency in which the invoice is paid.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Conditional                     |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | [Currency Format](#attributes.currencyformat) |

## Introduced (version)

1.4
