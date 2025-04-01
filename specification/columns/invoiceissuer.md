# Invoice Issuer

An Invoice Issuer is the entity responsible for invoicing and receiving payment from the customer for the consumed [*resources*](#glossary:resource) or [*services*](#glossary:service), including resellers, marketplaces, or billing intermediaries. Commonly used in cost analysis and reporting.

The InvoiceIssuerName column adheres to the following requirements:

* InvoiceIssuerName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* InvoiceIssuerName MUST be of type String.
* InvoiceIssuerName MUST conform to [StringHandling](#stringhandling) requirements.
* InvoiceIssuerName MUST NOT be null.

See [Appendix: Origination of cost data](#originationofcostdata) section for examples of Invoice Issuer values that can be used for various purchasing scenarios.

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
