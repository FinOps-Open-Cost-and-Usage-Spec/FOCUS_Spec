# Invoice Issuer Name

Invoice Issuer Name is the name of the entity responsible for issuing payable invoices for the [*contract commitment*](#glossary:contract-commitment). It is commonly used for cost analysis, reconciliation, and reporting scenarios.

## Requirements

InvoiceIssuerName MUST adhere to the following requirements:

* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.

## Column ID

InvoiceIssuerName

## Display Name

Invoice Issuer Name

## Description

The name of the entity responsible for invoicing for the [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension       |
| Feature level   | Mandatory       |
| Allows nulls    | False           |
| Data type       | String          |
| Value format    | \<not specified> |

## Version Introduced

1.4
