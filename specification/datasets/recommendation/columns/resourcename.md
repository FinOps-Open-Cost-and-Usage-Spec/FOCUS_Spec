# Resource Name

The Resource Name is a display name assigned to a [*resource*](#glossary:resource). In the Recommendation dataset, the Resource Name is commonly used to make resource-scoped recommendations readable without resolving the [Resource ID](#datasets.recommendation.resourceid).

## Requirements

ResourceName MUST adhere to the following requirements:

* ResourceName MUST be of type String.
* ResourceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ResourceName MUST adhere to the following nullability requirements:
  * ResourceName MUST be null when ResourceId is null or when the *resource* does not have an assigned display name.
  * ResourceName MUST NOT be null when ResourceId is not null and the *resource* has an assigned display name.

## Column ID

ResourceName

## Display Name

Resource Name

## Description

Display name assigned to a *resource*.

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
