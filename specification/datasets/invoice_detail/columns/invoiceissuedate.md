# Invoice Issue Date

[Invoice Issue Date](#col) is the date the invoice was issued by the [invoice issuer](#term). This date serves as the official point of record for the billing document, determining the beginning of payment terms and providing a key reference point for financial audits and period closing processes.

## Requirements

[InvoiceIssueDate](#col) MUST adhere to the following requirements:

* [InvoiceIssueDate](#col) MUST be of type Date/Time.
* [InvoiceIssueDate](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [InvoiceIssueDate](#col) MAY be null.
* [InvoiceIssueDate](#col) MUST represent the official date of issuance for the corresponding [InvoiceId](#col).

## Column ID

InvoiceIssueDate

## Display Name

Invoice Issue Date

## Description

The date the invoice was issued by the invoice issuer.

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
