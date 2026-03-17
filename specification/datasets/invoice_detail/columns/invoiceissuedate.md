# Invoice Issue Date

<<<<<<< HEAD
An Invoice Issue Date is the date the invoice was issued by the invoice issuer. This date serves as the official point of record for the billing document, determining the beginning of payment terms and providing a key reference point for financial audits and period closing processes.
=======
Invoice Issue Date is the date the invoice was issued by the invoice issuer. This date serves as the official point of record for the billing document, determining the beginning of payment terms and providing a key reference point for financial audits and period closing processes.
>>>>>>> 1467-fr-add-14-specification-revisions-to-requirements-model-recreate

## Requirements

InvoiceIssueDate MUST adhere to the following requirements:

* InvoiceIssueDate MUST be of type Date/Time.
* InvoiceIssueDate MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* InvoiceIssueDate MAY be null.
* InvoiceIssueDate MUST represent the official date of issuance for the corresponding [InvoiceId](#datasets.invoicedetail.invoiceid).

## Column ID

InvoiceIssueDate

## Display Name

Invoice Issue Date

## Description

The date the invoice was issued by the invoice issuer.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | True                            |
| Data type       | Date/Time                        |
<<<<<<< HEAD
| Value format    | [DateTime Format](#attributes.date/timeformat) |
=======
| Value format    | [Date/Time Format](#attributes.date/timeformat) |
>>>>>>> 1467-fr-add-14-specification-revisions-to-requirements-model-recreate

## Introduced (version)

1.4
