# Host Provider

A Host Provider is an entity whose [*resources*](#glossary:resource) are used by the Publisher to make the Publisher's [*resources*](#glossary:resource) or [*services*](#glossary:service) available.

The HostProvider column adheres to the following requirements:

* The HostProvider column is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) whenever applicable.
* This column MUST be of type String and MUST NOT contain null values.

See [Appendix: Origination of cost data](#originationofcostdata) section for examples of Publisher.

## Column ID

HostProviderName

## Display Name

Host Provider

## Description

The name of the entity whose *resources* are used by the Publisher to make the Publisher's [*resources*](#glossary:resource) or [*services*](#glossary:service) available.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Recommended     |
| Allows nulls    | False           |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.2
