# Resource Name

The Resource Name is a display name assigned to a resource. It is commonly used for cost analysis, reporting, and
allocation scenarios.

The ResourceName column MUST be present in the billing data. This column MUST be of type String. The ResourceName value
MAY be a nullable column as some cost data rows may not be associated with a resource or because a display name cannot
be assigned to a resource. ResourceName MUST NOT be null if a display name can be assigned to a resource. Resources not
provisioned interactively or only have a system generated ResourceId MUST NOT duplicate the same value as the
ResourceName.

## Column ID

ResourceName

## Display Name

Resource Name

## Description

Display name assigned to a resource.

## Content Constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

0.5
