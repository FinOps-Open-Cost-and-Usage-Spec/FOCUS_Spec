# Region ID

A Region ID is a host-provider-assigned identifier for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned or a [*service*](#glossary:service) is provided. The region is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

## Requirements

RegionId adheres to the following requirements:

* RegionId MUST be of type String.
* RegionId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RegionId nullability is defined as follows:
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

## Column ID

RegionId

## Display Name

Region ID

## Description

Host-provider-assigned identifier for an isolated geographic area where a *resource* is provisioned or a *service* is provided.

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
