# Invoice Issuer Name

Invoice Issuer Name is the name of the entity responsible for issuing payable invoices for the [*resources*](#glossary:resource) or [*services*](#glossary:service) consumed. It is commonly used for cost analysis and reporting scenarios.

## Requirements

InvoiceIssuerName MUST adhere to the following requirements:

* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.
* InvoiceIssuerName MUST represent the entity that issued the invoice.

See [Appendix: Participating Entity Identification Examples](#appendix.examples:participatingentityidentification) section for examples of Invoice Issuer Name values across various use case scenarios.

## Column ID

InvoiceIssuerName

## Display Name

Invoice Issuer Name

## Description

The name of the entity responsible for invoicing for the *resources* or *services* consumed.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Mandatory       |
| Allows nulls    | False           |
| Data type       | String          |
| Value format    | \<not specified> |

## Version Introduced

1.4
