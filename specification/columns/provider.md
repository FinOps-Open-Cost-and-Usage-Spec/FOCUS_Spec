# Provider

A Provider is an entity that makes the [*resources*](#glossary:resource) or [*services*](#glossary:service) available for purchase. It is commonly used for cost analysis and reporting scenarios.

The ProviderName column adheres to the following requirements:

* ProviderName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ProviderName MUST be of type String.
* ProviderName MUST conform to [StringHandling](#stringhandling) requirements.
* ProviderName MUST NOT be null.

See [Appendix: Origination of cost data](#originationofcostdata) section for examples of Provider, Publisher and
Invoice Issuer values that can be used for various purchasing scenarios.

## Column ID

ProviderName

## Display Name

Provider

## Description

The name of the entity that made the *resources* or *services* available for purchase.

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
