# Payment Due Date

[Payment Due Date](#col) is the date by which the payment for an invoice is expected to be received by the [invoice issuer](#term). This date is used by FinOps practitioners and finance teams to manage cash flow, prioritize payments, and avoid late fees or service interruptions.

## Requirements

[PaymentDueDate](#col) MUST adhere to the following requirements:

* [PaymentDueDate](#col) MUST be of type Date/Time.
* [PaymentDueDate](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [PaymentDueDate](#col) MAY be null.
* [PaymentDueDate](#col) MUST be the date specified by the invoice issuer as the deadline for payment for the corresponding [InvoiceId](#col).

## Column ID

PaymentDueDate

## Display Name

Payment Due Date

## Description

The date by which the payment for an invoice is expected to be received by the invoice issuer.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | True                                            |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attr)                       |

## Version Introduced

1.4
