# Payment Currency

A Payment Currency represents the currency used for the actual payment of an invoice, as determined by the invoice issuer. This currency may differ from the [Billing Currency](#datasets.costandusage.billingcurrency) if the customer and provider have agreed on a different settlement currency, making it essential for tracking actual cash outflow and foreign exchange impacts.

## Requirements

PaymentCurrency adheres to the following requirements:

* PaymentCurrency MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PaymentCurrency MUST be of type String.
* PaymentCurrency MUST represent the currency in which the invoice payment was made or is expected to be made to the [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername).

## Column ID

PaymentCurrency

## Display Name

Payment Currency

## Description

The currency in which the invoice is paid.

## Content constraints

|    Constraint    |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | [Currency Format](#attributes.currencyformat) |

## Introduced (version)

1.4