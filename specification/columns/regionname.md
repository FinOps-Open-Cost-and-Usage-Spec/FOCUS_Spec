# Region Name

Region Name is a provider-assigned display name for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned or a [*service*](#glossary:service) is provided. Region Name is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

The RegionName column adheres to the following requirements:

* RegionName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within a region.
* RegionName MUST be of type String.
* RegionName MUST conform to [String Handling](#stringhandling) requirements.
* RegionName nullability is defined as follows:
  * RegionName MUST be null when [RegionId](#regionid) is null.
  * RegionName MUST NOT be null when RegionId is not null.

## Column ID

RegionName

## Display Name

Region Name

## Description

The name of an isolated geographic area where a *resource* is provisioned or a *service* is provided.

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
