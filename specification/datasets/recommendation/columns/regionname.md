# Region Name

Region Name is a host-provider-assigned display name for an isolated geographic area where the [*resource*](#glossary:resource) or [*service*](#glossary:service) targeted by a recommendation is provisioned or provided. In the Recommendation dataset, the Region Name is commonly used to analyze recommendations by where the related *resources* are deployed.

## Requirements

RegionName MUST adhere to the following requirements:

* RegionName MUST be of type String.
* RegionName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RegionName MUST adhere to the following nullability requirements:
  * RegionName MUST be null when [RegionId](#datasets.recommendation.regionid) is null.
  * RegionName MUST NOT be null when RegionId is not null.

## Column ID

RegionName

## Display Name

Region Name

## Description

The name of an isolated geographic area where a *resource* is provisioned or a *service* is provided.

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
