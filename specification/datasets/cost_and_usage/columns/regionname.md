# Region Name

Region Name is a host-provider-assigned display name for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned or a [*service*](#glossary:service) is provided. Region Name is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

## Requirements

RegionName MUST adhere to the following requirements:

* RegionName MUST be of type String.
* RegionName MUST adhere to the following nullability requirements:
  * RegionName MUST be null when [RegionId](#datasets.costandusage.regionid) is null.
  * RegionName MUST NOT be null when RegionId is not null.

## Column ID

RegionName

## Display Name

Region Name

## Description

The name of an isolated geographic area where a *resource* is provisioned or a *service* is provided.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

1.0
