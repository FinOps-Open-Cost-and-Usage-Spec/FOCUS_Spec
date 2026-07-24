# Region ID

A Region ID is a host-provider-assigned identifier for an isolated geographic area where the [*resource*](#glossary:resource) or [*service*](#glossary:service) targeted by a recommendation is provisioned or provided. In the Recommendation dataset, the Region ID is commonly used to analyze recommendations by where the related *resources* are deployed.

## Requirements

RegionId MUST adhere to the following requirements:

* RegionId MUST be of type String.
* RegionId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RegionId MUST adhere to the following nullability requirements:
  * RegionId MUST NOT be null when a recommendation targets a *resource* or *service* operated in or managed from a distinct region.
  * RegionId MAY be null when a recommendation does not target a *resource* or *service* operated in or managed from a distinct region.

## Column ID

RegionId

## Display Name

Region ID

## Description

Host-provider-assigned identifier for an isolated geographic area where a *resource* is provisioned or a *service* is provided.

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
