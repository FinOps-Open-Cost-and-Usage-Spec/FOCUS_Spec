# Region Name

Region Name is a provider assigned name for an isolated geographic area where a [*resource*](#glossary:resource) is provisioned in or a [*service*](#glossary:service) is provided from. Region Name is commonly used for scenarios like analyzing cost and unit prices based on where *resources* are deployed. 

Region Name MUST be present in the billing data and MUST be of type String. Region Name MUST NOT be null when a *resource* or *service* is operated in or managed from a distinct region by the Provider. Region Name values MUST be consistent within the provider and MUST be the same values used to indicate the region when provisioning or purchasing the *resource* or *service*. The value of the dimension Region Name SHOULD be a proper noun.

## Column ID

RegionName

## Display name

Region Name

## Description

The name of Isolated geographic area where a *resource* is provisioned in or a *service* is provided from.

## Content constraints

| Constraint      | Value           |
|-----------------|-----------------|
| Column type     | Dimension       |
| Column required | True            |
| Allows nulls    | True            |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.5
