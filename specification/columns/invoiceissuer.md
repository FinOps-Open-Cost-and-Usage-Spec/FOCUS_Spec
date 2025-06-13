# Invoice Issuer

An Invoice Issuer is an entity responsible for issuing payable invoices for the [*resources*](#glossary:resource) or [*services*](#glossary:service) consumed. It is commonly used for cost analysis and reporting scenarios.

The InvoiceIssuerName column adheres to the following requirements:

* InvoiceIssuerName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [StringHandling](#stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.

See [Appendix: Entity Identification Examples](#entityidentification) section for examples of Invoice Issuer values for various use case scenarios.

## Column ID

InvoiceIssuerName

## Display Name

Invoice Issuer

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

## Introduced (version)

0.5
