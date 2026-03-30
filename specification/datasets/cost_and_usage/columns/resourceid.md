# Resource ID

A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by the service provider. The Resource ID is commonly used for cost reporting, analysis, and allocation scenarios.

## Requirements

ResourceId MUST adhere to the following requirements:

* ResourceId MUST be of type String.
* ResourceId MUST adhere to the following nullability requirements:
  * ResourceId MUST be null when a [*charge*](#glossary:charge) is not related to a *resource*.
  * ResourceId MUST NOT be null when a *charge* is related to a *resource*.
* When ResourceId is not null, ResourceId MUST adhere to the following requirements:
  * ResourceId MUST be a unique identifier within the service provider.
  * ResourceId SHOULD be a fully-qualified identifier.

## Column ID

ResourceId

## Display Name

Resource ID

## Description

Identifier assigned to a *resource* by the service provider.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

0.5
