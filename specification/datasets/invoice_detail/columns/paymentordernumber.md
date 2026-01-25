# Payment Order Number

A Payment Order Number is the unique customer-issued identifier for tracking the lifecycle of a purchase. This identifier is typically provided by the customer to the invoice issuer to ensure that charges are mapped to specific internal procurement records or purchase orders.

## Requirements

PaymentOrderNumber adheres to the following requirements:

* PaymentOrderNumber MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) if the provider supports customer input of purchase order numbers.
* PaymentOrderNumber MUST be of type String.
* PaymentOrderNumber MUST be the identifier used by the [InvoiceIssuerName](#datasets.costandusage.invoiceissuername) to identify the purchase order responsible for the charge.

## Column ID

PaymentOrderNumber

## Display Name

Payment Order Number

## Description

The unique customer-issued identifier for tracking the lifecycle of a purchase.

## Content constraints

|    Constraint    |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Conditional                     |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | <unspecified>                   |

## Introduced (version)

1.4