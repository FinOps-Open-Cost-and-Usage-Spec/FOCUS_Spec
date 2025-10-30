# Publisher - DEPRECATED

Publisher is the name of the entity that produces the [*resources*](#glossary:resource) or [*services*](#glossary:service) that were purchased. It is commonly used for cost analysis and reporting scenarios.

## Requirements

PublisherName adheres to the following requirements:

* PublisherName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PublisherName MUST be of type String.
* PublisherName MUST conform to [StringHandling](#stringhandling) requirements.
* PublisherName MUST NOT be null.

See [Appendix: Participating Entity Identification Examples](#participatingentityidentificationexamples) section for examples of [Service Provider Name](#serviceprovidername), [Host Provider Name](#hostprovidername) and [Invoice Issuer Name](#invoiceissuername) values across various use case scenarios.  For entity identification examples that include the deprecated Publisher column, please see [here](https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/7296e3146fb931ee32b6496fa6e4200e7f4384f7/specification/appendix/origination_of_cost_data.md) (external GitHub link to FOCUS v1.2).

## Column ID

PublisherName

## Display Name

Publisher Name

## Description

The name of the entity that produced the *resources* or *services* that were purchased.

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

## Deprecated (version)

1.3
