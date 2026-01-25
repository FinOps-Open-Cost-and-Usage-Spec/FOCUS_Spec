# Reference Invoice ID

A Reference Invoice ID is an invoice-issuer-assigned identifier for an invoice that affects charges as stated on a previous invoice. This occurs typically in the context of credits, refunds, or corrections where an adjustment is applied to a specific previously-issued billing document. This ID allows for direct lineage between adjustments and the original billing records.

## Requirements

ReferenceInvoiceId adheres to the following requirements:

* ReferenceInvoiceId MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) if the provider supports linking adjustments to original invoices.
* ReferenceInvoiceId MUST be of type String.
* ReferenceInvoiceId MUST be the same as the [InvoiceId](#datasets.costandusage.invoiceid) of the original [*invoice*](#glossary:invoice) to which the current adjustment applies.
* ReferenceInvoiceId MUST NOT be null for *charges* where [ChargeCategory](#datasets.costandusage.chargecategory) is 'Credit' or 'Refund' and a specific original invoice is identified.
* ReferenceInvoiceId MUST be null for *charges* that do not reference a specific previous [*invoice*](#glossary:invoice).

## Column ID

ReferenceInvoiceId

## Display Name

Reference Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice that affects charges as stated on a previous invoice.

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