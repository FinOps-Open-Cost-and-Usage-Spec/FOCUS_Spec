# Resource ID

A Resource ID is an identifier assigned to a [*resource*](#glossary:resource) by the [*service provider*](#glossary:service-provider). The Resource ID associates a recommendation with the *resource* it seeks to optimize, enabling recommendations to be joined to cost and usage data.

## Requirements

ResourceId MUST adhere to the following requirements:

* ResourceId MUST be of type String.
* ResourceId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ResourceId MUST adhere to the following nullability requirements:
  * ResourceId MUST be null when a recommendation is not associated with a single *resource*.
  * ResourceId MUST NOT be null when a recommendation is associated with a single *resource*.
* When ResourceId is not null, ResourceId MUST adhere to the following requirements:
  * ResourceId MUST be a unique identifier within the *service provider*.
  * ResourceId SHOULD be a fully-qualified identifier.

## Column ID

ResourceId

## Display Name

Resource ID

## Description

Identifier assigned to a *resource* by the service provider.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
