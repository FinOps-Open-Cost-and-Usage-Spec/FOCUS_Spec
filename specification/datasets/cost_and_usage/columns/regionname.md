# Region Name

[Region Name](#col) is a host-provider-assigned display name for an isolated geographic area where a [resource](#term) is provisioned or a [service](#term) is provided. [Region Name](#col) is commonly used for scenarios like analyzing cost and unit prices based on where [resources](#term) are deployed.

## Requirements

[RegionName](#col) MUST adhere to the following requirements:

* [RegionName](#col) MUST be of type String.
* [RegionName](#col) MUST conform to [StringHandling](#attr) requirements.
* [RegionName](#col) MUST adhere to the following nullability requirements:
  * [RegionName](#col) MUST be null when [RegionId](#col) is null.
  * [RegionName](#col) MUST NOT be null when [RegionId](#col) is not null.

## Column ID

RegionName

## Display Name

Region Name

## Description

The name of an isolated geographic area where a [resource](#term) is provisioned or a [service](#term) is provided.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Regions](#omc)                                      |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.0
