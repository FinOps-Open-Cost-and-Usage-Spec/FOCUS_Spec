# Payment Terms

Payment Terms represents the [*terms*](#glossary:term) (typically focused on timeframe) by which the invoice issuer expects to receive payment for an invoice. These terms define the agreed-upon period for settling the invoice, helping both the provider and the customer manage financial expectations and payment schedules.

## Requirements

PaymentTerms MUST adhere to the following requirements:

* PaymentTerms MUST be of type String.
* PaymentTerms MUST NOT be null.
* PaymentTerms MUST represent the payment terms (e.g., "Net 30") as defined on the corresponding invoice.

## Column ID

PaymentTerms

## Display Name

Payment Terms

## Description

The terms (typically focused on timeframe) by which the invoice issuer expects to receive payment for an invoice.

## Content constraints

|    Constraint   |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | \<not specified>                |

## Introduced (version)

1.4
