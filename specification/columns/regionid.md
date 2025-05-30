# Region ID

A Region ID is a provider-assigned identifier for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned or a [*service*](#glossary:service) is provided. The region is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

The RegionId column adheres to the following requirements:

* RegionId MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* RegionId MUST be of type String.
* RegionId MUST conform to [StringHandling](#stringhandling) requirements.
* RegionId nullability is defined as follows:
  * RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region.
  * RegionId MAY be null when a *resource* or *service* is not operated in or managed from a distinct region.

## Column ID

RegionId

## Display Name

Region ID

## Description

Provider-assigned identifier for an isolated geographic area where a *resource* is provisioned or a *service* is provided.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column type     | Dimension       |
| Feature level   | Conditional     |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.0
