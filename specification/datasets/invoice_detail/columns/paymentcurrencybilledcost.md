# Payment Currency Billed Cost

A Payment Currency Billed Cost represents the [Billed Cost](#datasets.invoicedetail.billedcost) as expressed in [Payment Currency](#datasets.invoicedetail.paymentcurrency). This metric is essential for organizations that need to reconcile their financial records in the currency used for actual settlement, especially when it differs from the currency used for initial billing.

## Requirements

PaymentCurrencyBilledCost adheres to the following requirements:

* PaymentCurrencyBilledCost MUST be of type Decimal.
* PaymentCurrencyBilledCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PaymentCurrencyBilledCost MUST NOT be null.
* PaymentCurrencyBilledCost MUST be a valid decimal value.
* PaymentCurrencyBilledCost MUST be 0 for *charges* where payments are received by a third party (e.g., marketplace transactions).
* PaymentCurrencyBilledCost MUST represent the [BilledCost](#datasets.invoicedetail.billedcost) amount as denominated in the [PaymentCurrency](#datasets.invoicedetail.paymentcurrency).

## Column ID

PaymentCurrencyBilledCost

## Display Name

Payment Currency Billed Cost

## Description

The [Billed Cost](#datasets.invoicedetail.billedcost) as expressed in [Payment Currency](#datasets.invoicedetail.paymentcurrency).

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Conditional             |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#attributes.numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.4