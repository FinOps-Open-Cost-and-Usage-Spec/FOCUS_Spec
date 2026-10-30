# Payment Terms

[Payment Terms](#col) represents the [terms](#term) (typically focused on timeframe) by which the [invoice issuer](#term) expects to receive payment for an invoice. These terms define the agreed-upon period for settling the invoice, helping both the provider and the customer manage financial expectations and payment schedules.

## Requirements

[PaymentTerms](#col) MUST adhere to the following requirements:

* [PaymentTerms](#col) MUST be of type String.
* [PaymentTerms](#col) MUST conform to [StringHandling](#attr) requirements.
* [PaymentTerms](#col) MUST NOT be null.
* [PaymentTerms](#col) MUST represent the payment terms (e.g., "Net 30") as defined on the corresponding invoice.

## Column ID

PaymentTerms

## Display Name

Payment Terms

## Description

The terms (typically focused on timeframe) by which the invoice issuer expects to receive payment for an invoice.

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | Not applicable                             |
| Column type                | Dimension                                  |
| Feature level              | Mandatory                                  |
| Allows nulls               | False                                      |
| Data type                  | String                                     |
| Value format               | \<not specified>                           |

## Version Introduced

1.4
