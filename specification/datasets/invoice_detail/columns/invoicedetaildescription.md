# Invoice Detail Description

[Invoice Detail Description](#col) is the invoice-issuer-provided description of an invoice line item. This description provides context for the charge as it appears on the invoice, often summarizing the service, resource, or period covered by that specific line item to assist in human-readable reconciliation.

## Requirements

[InvoiceDetailDescription](#col) MUST adhere to the following requirements:

* [InvoiceDetailDescription](#col) MUST be of type String.
* [InvoiceDetailDescription](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceDetailDescription](#col) SHOULD NOT be null.
* [InvoiceDetailDescription](#col) maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.
* [InvoiceDetailDescription](#col) MUST describe the [charges](#term) represented by the [InvoiceDetailId](#col).

## Column ID

InvoiceDetailDescription

## Display Name

Invoice Detail Description

## Description

The invoice-issuer-provided description of an invoice line item.

## Content Constraints

| Constraint                 | Value                                      |
| :------------------------- | :----------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                      |
| Operating model conditions | Not applicable                             |
| Column type                | Dimension                                  |
| Feature level              | Mandatory                                  |
| Allows nulls               | True                                       |
| Data type                  | String                                     |
| Value format               | \<not specified>                           |

## Version Introduced

1.4
