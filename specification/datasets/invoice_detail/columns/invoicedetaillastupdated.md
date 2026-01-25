# Invoice Detail Last Updated

An Invoice Detail Created is the timestamp when the [Invoice Detail](#datasets.invoicedetail) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a record, particularly if corrections or status changes have been applied to the record after its initial creation.

## Requirements

InvoiceDetailLastUpdated adheres to the following requirements:

* InvoiceDetailLastUpdated MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceDetailLastUpdated MUST be of type Datetime.
* InvoiceDetailLastUpdated MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements.
* InvoiceDetailLastUpdated MUST represent the most recent moment in time when any column value of the record identified by [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid) was created or modified.
* InvoiceDetailLastUpdated MUST be greater than or equal to [InvoiceDetailCreated](#datasets.invoicedetail.invoicedetailcreated).

## Column ID

InvoiceDetailLastUpdated

## Display Name

Invoice Detail Last Updated

## Description

The timestamp when the Invoice Detail record was last updated.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Datetime                        |
| Value format    | [DateTime Format](#attributes.datetimeformat) |

## Introduced (version)

1.4