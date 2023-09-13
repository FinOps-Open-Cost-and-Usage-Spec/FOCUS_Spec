# Resource Type

A Resource Type is a classifiable representation of a specific kind of cloud service or corresponding resource that can be provisioned, configured, and managed by users. A Resource Type is commonly used for scenarios like identifying changes in cost over time or building a resource inventory.  While Resource ID and Resource Name identifies a unique instance of a resource, the Resource Type describes the identity of the resource.

The ResourceType column MUST be present within billing data.  ResourceType MUST be of type String and MUST NOT be NULL when a corresponding ResourceId is not NULL.  When a corresponding ResourceId value is NULL, the ResourceType column value MUST be NULL.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

A classifiable representation of a specific kind of cloud service or corresponding resource that can be provisioned, configured, and managed by users.

## Normalized?

No

## Data type

String

## Content Constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
