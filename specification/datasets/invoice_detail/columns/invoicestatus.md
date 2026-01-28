# Invoice Status

An Invoice Status represents the status of an invoice at the time the dataset was generated. This status allows FinOps practitioners to distinguish between invoices that are still pending, finalized, or potentially disputed, ensuring that cost reporting and reconciliation are based on the correct stage of the billing lifecycle.

## Requirements

InvoiceStatus adheres to the following requirements:

* InvoiceStatus MUST be of type String.
* InvoiceStatus MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceStatus MUST NOT be null.
* InvoiceStatus MUST be one of the allowed values defined in the [Allowed Values](#datasets.invoicedetail.invoicestatus.allowed-values) section.
* InvoiceStatus MUST represent the current state of the invoice.

## Column ID

InvoiceStatus

## Display Name

Invoice Status

## Description

The status of an invoice at the time the dataset was generated.

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
| `Open`   | The invoice is not considered finalized. |
| `Closed` | The invoice is considered finalized.     |

## Introduced (version)

1.4