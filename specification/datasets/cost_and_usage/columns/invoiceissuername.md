# Invoice Issuer Name

Invoice Issuer Name is the name of the entity responsible for issuing payable invoices for the [*resources*](#glossary:resource) or [*services*](#glossary:service) consumed. It is commonly used for cost analysis and reporting scenarios.

## Requirements

InvoiceIssuerName adheres to the following requirements:

* InvoiceIssuerName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [StringHandling](#stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.

See [Appendix: Participating Entity Identification Examples](#participatingentityidentificationexamples) section for examples of Invoice Issuer Name values across various use case scenarios.

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

## Introduced (version)

0.5
