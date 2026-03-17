# Payment Due Date

<<<<<<< HEAD
A Payment Due Date is the date by which the payment for an invoice is expected to be received by the invoice issuer. This date is used by FinOps practitioners and finance teams to manage cash flow, prioritize payments, and avoid late fees or service interruptions.
=======
Payment Due Date is the date by which the payment for an invoice is expected to be received by the invoice issuer. This date is used by FinOps practitioners and finance teams to manage cash flow, prioritize payments, and avoid late fees or service interruptions.
>>>>>>> 1467-fr-add-14-specification-revisions-to-requirements-model-recreate

## Requirements

PaymentDueDate MUST adhere to the following requirements:

* PaymentDueDate MUST be of type Date/Time.
<<<<<<< HEAD
* PaymentDueDate MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements.
=======
* PaymentDueDate MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* PaymentDueDate MAY be null.
>>>>>>> 1467-fr-add-14-specification-revisions-to-requirements-model-recreate
* PaymentDueDate MUST be the date specified by the [*invoice issuer*](#glossary:invoice-issuer) as the deadline for payment for the corresponding [InvoiceId](#datasets.invoicedetail.invoiceid).

## Column ID

PaymentDueDate

## Display Name

Payment Due Date

## Description

The date by which the payment for an invoice is expected to be received by the invoice issuer.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | True                            |
| Data type       | Date/Time                       |
| Value format    | [Date/Time Format](#attributes.date/timeformat) |

## Introduced (version)

1.4
