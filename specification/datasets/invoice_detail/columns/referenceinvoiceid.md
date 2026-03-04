# Reference Invoice ID

A Reference Invoice ID is an invoice-issuer-assigned identifier for an invoice that affects charges as stated on a previous invoice. This occurs typically in the context of credits, refunds, or corrections where an adjustment is applied to a specific previously-issued billing document. This ID allows for direct lineage between adjustments and the original billing records.

## Requirements

ReferenceInvoiceId MUST adhere to the following requirements:

* ReferenceInvoiceId MUST be of type String.
* ReferenceInvoiceId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ReferenceInvoiceId MUST NOT be null.
* ReferenceInvoiceId MUST equal the [InvoiceId](#datasets.costandusage.invoiceid) of the original [*invoice*](#glossary:invoice) if it adjusts another invoice.
* ReferenceInvoiceId MUST equal the InvoiceId of the current invoice if it does not adjust another invoice.

## Column ID

ReferenceInvoiceId

## Display Name

Reference Invoice ID

## Description

The invoice-issuer-assigned identifier for an invoice that affects charges as stated on a previous invoice.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | \<unspecified>                   |

## Introduced (version)

1.4
