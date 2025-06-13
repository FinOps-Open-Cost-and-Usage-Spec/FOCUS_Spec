# Service Provider

A Service Provider is the entity that makes the [*resources*](#glossary:resource) or [*services*](#glossary:service) available for purchase or consumption.  It is commonly used for cost analysis and reporting scenarios.

The Service Provider column adheres to the following requirements:

* The Service Provider column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* This column MUST be of type String and MUST NOT contain null values.

See [Appendix: Entity Identification Examples](#entityidentification) section for examples of Service Provider values for various use case scenarios.

## Column ID

ServiceProvider

## Display Name

Service Provider

## Description

The name of the entity that made the *resources* or *services* available for purchase or consumption.

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
