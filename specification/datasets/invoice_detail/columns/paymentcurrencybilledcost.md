# Payment Currency Billed Cost

A Payment Currency Billed Cost represents the billed cost as expressed in payment currency. This metric is essential for organizations that need to reconcile their financial records in the currency used for actual settlement, especially when it differs from the currency used for initial billing.

## Requirements

PaymentCurrencyBilledCost adheres to the following requirements:

* PaymentCurrencyBilledCost MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PaymentCurrencyBilledCost MUST be of type Numeric.
* PaymentCurrencyBilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PaymentCurrencyBilledCost MUST represent the [BilledCost](#datasets.invoicedetail.billedcost) amount as denominated in the [PaymentCurrency](#datasets.invoicedetail.paymentcurrency).

## Column ID

PaymentCurrencyBilledCost

## Display Name

Payment Currency Billed Cost

## Description

The billed cost as expressed in payment currency.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Metric                          |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Numeric                         |
| Value format    | Decimal (any)                   |

## Introduced (version)

1.4