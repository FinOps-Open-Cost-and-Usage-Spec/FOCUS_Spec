# Invoice Issue Status

Invoice Issue Status indicates the publication state of the invoice. It distinguishes between provisional data that is subject to change, invoices that have been formally issued as valid financial obligations, and invoices that have been explicitly retracted.

## Requirements

InvoiceIssueStatus MUST adhere to the following requirements:

* InvoiceIssueStatus MUST be of type String.
* InvoiceIssueStatus MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceIssueStatus MUST NOT be null.
* InvoiceIssueStatus MUST be one of the allowed values defined in the [Allowed Values](#datasets.invoicedetail.invoiceissuestatus.allowed-values) section.
* InvoiceIssueStatus MUST represent the current publication state of the invoice.

## Column ID

InvoiceIssueStatus

## Display Name

Invoice Issue Status

## Description

The publication state of the invoice, indicating if it is provisional (`Open`), issued (`Issued`), or voided (`Voided`).

## Content constraints

|    Constraint   |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | String                          |
| Value format    | <unspecified>                   |

## Allowed Values

| Value    | Description                              |
| :---     | :---                                     |
| `Open`   | The invoice is provisional and subject to change. It is not a valid financial obligation. |
| `Issued` | The invoice has been formally issued by the provider. It represents a static financial obligation. |
| `Voided` | The invoice was previously issued but has been retracted or nullified. It is not a valid financial obligation. |

## Introduced (version)

1.4
