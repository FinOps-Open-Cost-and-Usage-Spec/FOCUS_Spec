# Region ID

A [Region ID](#col) is a host-provider-assigned identifier for an isolated geographic area where a [resource](#term) is provisioned or a [service](#term) is provided. The region is commonly used for scenarios like analyzing cost and unit prices based on where [resources](#term) are deployed.

## Requirements

[RegionId](#col) MUST adhere to the following requirements:

* [RegionId](#col) MUST be of type String.
* [RegionId](#col) MUST conform to [StringHandling](#attr) requirements.
* [RegionId](#col) MUST adhere to the following nullability requirements:
  * [RegionId](#col) MUST NOT be null when a [resource](#term) or [service](#term) is operated in or managed from a distinct region.
  * [RegionId](#col) MAY be null when a [resource](#term) or [service](#term) is not operated in or managed from a distinct region.

## Column ID

RegionId

## Display Name

Region ID

## Description

Host-provider-assigned identifier for an isolated geographic area where a [resource](#term) is provisioned or a [service](#term) is provided.

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
