# Payment Due Date

An Payment Due Date is the date by which the payment for an invoice is expected to be received by the invoice issuer to be considered on time. This date is used by FinOps practitioners and finance teams to manage cash flow, prioritize payments, and avoid late fees or service interruptions.

## Requirements

PaymentDueDate adheres to the following requirements:

* PaymentDueDate MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) if the provider supports specifying payment terms.
* PaymentDueDate MUST be of type Datetime.
* PaymentDueDate MUST conform to [DateTimeFormat](#attributes.datetimeformat) requirements.
* PaymentDueDate MUST be the date specified by the [InvoiceIssuerName](#datasets.costandusage.invoiceissuername) as the deadline for payment for the corresponding [InvoiceId](#datasets.costandusage.invoiceid).

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
| Feature level   | Conditional                     |
| Allows nulls    | True                            |
| Data type       | Date/time                        |
| Value format    | [DateTime Format](#attributes.date/timeformat) |

## Introduced (version)

1.4