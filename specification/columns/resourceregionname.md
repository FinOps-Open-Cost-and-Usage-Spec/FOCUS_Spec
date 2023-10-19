# Resource Region Name

Resource Region Name is a provider-assigned display name for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned. Resource Region Name is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

The ResourceRegionName column MUST be present in the billing data when the provider supports deploying resources or services within a *region* and MUST be of type String. ResourceRegionName MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider and MAY contain null values when a *resource* or *service* is not restricted to an isolated geographic area.

## Column ID

ResourceRegionName

## Display Name

Resource Region Name

## Description

The name of an isolated geographic area where a *resource* is provisioned.

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
