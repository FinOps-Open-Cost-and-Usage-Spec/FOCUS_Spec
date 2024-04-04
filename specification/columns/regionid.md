# Region ID

A Region ID is a provider-assigned identifier for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned or a [*service*](#glossary:service) is provided. The region is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

The RegionId column SHOULD be present in the billing data when the provider supports deploying resources or services within a *region* and MUST be of type String. RegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider and MAY contain null values when a *resource* or *service* is not restricted to an isolated geographic area. RegionId values MUST be consistent within the provider and MUST be the same values used to indicate the region when provisioning or purchasing the *resource* or *service*.

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

0.5
