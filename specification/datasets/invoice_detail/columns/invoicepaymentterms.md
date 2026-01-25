# Invoice Payment Terms

An Invoice Payment Terms represents the terms (typically focused on timeframe) by which the invoice issuer expects to receive invoice payment. These terms define the agreed-upon period for settling the invoice, helping both the provider and the customer manage financial expectations and payment schedules.

## Requirements

InvoicePaymentTerms adheres to the following requirements:

* InvoicePaymentTerms MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoicePaymentTerms MUST be of type String.
* InvoicePaymentTerms MUST represent the contractual payment window (e.g., "Net 30") as defined by the [InvoiceIssuerName](#datasets.costandusage.invoiceissuername).

## Column ID

InvoicePaymentTerms

## Display Name

Invoice Payment Terms

## Description

The terms (typically focused on timeframe) by which the invoice issuer expects to receive invoice payment.

## Content constraints

|    Constraint    |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | <unspecified>                   |

## Introduced (version)

1.4