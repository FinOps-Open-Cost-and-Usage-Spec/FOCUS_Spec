# Publisher Name - DEPRECATED

Publisher Name is the name of the entity that produces the [*resources*](#glossary:resource) or [*services*](#glossary:service) that were purchased. It is commonly used for cost analysis and reporting scenarios.

The PublisherName column adheres to the following requirements:

* PublisherName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* PublisherName MUST be of type String.
* PublisherName MUST conform to [StringHandling](#stringhandling) requirements.
* PublisherName MUST NOT be null.

See [Appendix: Participating Entity Identification Examples](#participatingentityidentificationexamples) section for examples of [Service Provider Name](#serviceprovidername), [Host Provider Name](#hostprovidername) and [Invoice Issuer Name](#invoiceissuername) values across various use case scenarios.

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
