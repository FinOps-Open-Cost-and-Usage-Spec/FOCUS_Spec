# Resource Type

[Resource Type](#col) describes the kind of [resource](#term) the [charge](#term) applies to. A [Resource Type](#col) is commonly used for scenarios like identifying cost changes in groups of similar [resources](#term) and may include values like Virtual Machine, Data Warehouse, and Load Balancer.

## Requirements

[ResourceType](#col) MUST adhere to the following requirements:

* [ResourceType](#col) MUST be of type String.
* [ResourceType](#col) MUST conform to [StringHandling](#attr) requirements.
* [ResourceType](#col) MUST adhere to the following nullability requirements:
  * [ResourceType](#col) MUST be null when [ResourceId](#col) is null.
  * [ResourceType](#col) MUST NOT be null when [ResourceId](#col) is not null.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

The kind of [resource](#term) the [charge](#term) applies to.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Provisioned Resources](#omc) and [Includes Resource Type Assignment](#omc)                                                                                                       |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.0-preview
