# Region

A Region ID is a provider-assigned identifier for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned or a [*service*](#glossary:service) is provided. The region is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

RegionId MUST be present in the billing data and MUST be of type String. RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region. RegionId values MUST be consistent within the provider and MUST be the same values used to indicate the region when provisioning or purchasing the *resource* or *service*.

## Column ID

RegionId

## Display name

Region ID

## Description

Provider-assigned identifier for an isolated geographic area where a *resource* is provisioned or a *service* is provided

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column type     | Dimension       |
| Column Required | True            |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
