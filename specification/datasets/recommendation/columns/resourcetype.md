# Resource Type

Resource Type describes the kind of [*resource*](#glossary:resource) a recommendation applies to (ie: Virtual Machine, Data Warehouse, Load Balancer).

## Requirements

ResourceType MUST adhere to the following requirements:

* ResourceType MUST be of type String.
* ResourceType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ResourceType MUST adhere to the following nullability requirements:
  * ResourceType MUST be null when [ResourceId](#datasets.recommendation.resourceid) is null.
  * ResourceType MUST NOT be null when ResourceId is not null.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

The kind of *resource* a recommendation applies to.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
