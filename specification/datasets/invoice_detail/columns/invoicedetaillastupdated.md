# Invoice Detail Last Updated

[Invoice Detail Last Updated](#col) is the timestamp when the [Invoice Detail](#ds) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a record, particularly if corrections or status changes have been applied to the record after its initial creation.

## Requirements

[InvoiceDetailLastUpdated](#col) MUST adhere to the following requirements:

* [InvoiceDetailLastUpdated](#col) MUST be of type Date/Time.
* [InvoiceDetailLastUpdated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [InvoiceDetailLastUpdated](#col) MUST NOT be null.
* [InvoiceDetailLastUpdated](#col) MUST represent the most recent moment in time when any column value of the record identified by [InvoiceDetailId](#col) was created or modified.
* [InvoiceDetailLastUpdated](#col) MUST be greater than or equal to [InvoiceDetailCreated](#col).

## Column ID

InvoiceDetailLastUpdated

## Display Name

Invoice Detail Last Updated

## Description

The timestamp when the [Invoice Detail](#ds) record was last updated.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | False                                           |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attr)                       |

## Version Introduced

1.4
