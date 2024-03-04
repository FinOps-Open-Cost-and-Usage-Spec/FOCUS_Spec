# Region

A Region ID is a provider assigned identifier for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned in or a [*service*](#glossary:service) is provided from. Region is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed.

Region ID MUST be present in the billing data and MUST be of type String. Region ID MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region. Region ID values MUST be consistent within the provider and MUST be the same values used to indicate the region when provisioning or purchasing the *resource* or *service*.

## Column ID

Region ID

## Display name

Region ID

## Description

ID of an isolated geographic area where a *resource* is provisioned in or a *service* is provided from.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column type     | Dimension       |
| Column required | True            |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

0.5
