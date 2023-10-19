# Resource Region ID

A Resource Region ID is a provider-assigned identifier for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned. The region is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

The ResourceRegionId column MUST be present in the billing data when the provider supports deploying resources or services within a *region* and MUST be of type String. ResourceRegionId MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider and MAY contain null values when a *resource* or *service* is not restricted to an isolated geographic area.

## Column ID

ResourceRegionId

## Display Name

Resource Region ID

## Description

Provider-assigned identifier for an isolated geographic area where a *resource* is provisioned.

## Content constraints

| Constraint    | Value            |
| ------------- | ---------------- |
| Column type   | Dimension        |
| Feature level | Conditional      |
| Allows nulls  | True             |
| Data type     | String           |
| Value format  | \<not specified> |

## Introduced (version)

1.0
