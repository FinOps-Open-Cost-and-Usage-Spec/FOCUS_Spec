# Resource Name

The [Resource Name](#col) is a display name assigned to a [resource](#term). It is commonly used for cost analysis, reporting, and allocation scenarios.

## Requirements

[ResourceName](#col) MUST adhere to the following requirements:

* [ResourceName](#col) MUST be of type String.
* [ResourceName](#col) MUST conform to [StringHandling](#attr) requirements.
* [ResourceName](#col) MUST adhere to the following nullability requirements:
  * [ResourceName](#col) MUST be null when [ResourceId](#col) is null or when the [resource](#term) does not have an assigned display name.
  * [ResourceName](#col) MUST NOT be null when [ResourceId](#col) is not null and the [resource](#term) has an assigned display name.
* [ResourceName](#col) MUST NOT duplicate [ResourceId](#col) when the [resource](#term) is not provisioned interactively or only has a system-generated [ResourceId](#col).

## Column ID

ResourceName

## Display Name

Resource Name

## Description

Display name assigned to a [resource](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Provisioned Resources](#omc)                                                   |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

0.5
