# Invoice Detail Created

An Invoice Detail Created is the timestamp when the [Invoice Detail](#datasets.invoicedetail) record was first created. This timestamp facilitates auditiability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish betwee the time between the time of service consumption and the time of financial record generation.

## Requirements

InvoiceDetailCreated adheres to the following requirements:

* InvoiceDetailCreated MUST be present in an Invoice Detail [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceDetailCreated MUST be of type Datetime.
* InvoiceDetailCreated MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements.
* InvoiceDetailCreated MUST represent the moment in time the Invoice Detail record was instantiated.

## Column ID

InvoiceDetailCreated

## Display Name

Invoice Detail Created

## Description

The timestamp when the Invoice Detail record was first created.

## Content constraints

|    Constraint    |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Datetime                        |
| Value format    | [DateTime Format](#attributes.date/timeformat) |

## Introduced (version)

1.4