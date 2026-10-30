# Invoice Issuer Name

[Invoice Issuer Name](#col) is the name of the entity responsible for issuing payable invoices for the [resources](#term) or [services](#term) consumed. It is commonly used for cost analysis and reporting scenarios.

## Requirements

[InvoiceIssuerName](#col) MUST adhere to the following requirements:

* [InvoiceIssuerName](#col) MUST be of type String.
* [InvoiceIssuerName](#col) MUST conform to [StringHandling](#attr) requirements.
* [InvoiceIssuerName](#col) MUST NOT be null.
* [InvoiceIssuerName](#col) MUST represent the entity that issues invoices.

See [Appendix: Participating Entity Identification Examples](#appendix.examples:participatingentityidentification) section for examples of [Invoice Issuer Name](#col) values across various use case scenarios.

## Column ID

InvoiceIssuerName

## Display Name

Invoice Issuer Name

## Description

The name of the entity responsible for invoicing for the [resources](#term) or [services](#term) consumed.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
