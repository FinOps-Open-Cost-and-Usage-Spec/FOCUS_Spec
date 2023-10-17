# Resource Type

Resource Type describes the kind of resource for which you are being charged.  A Resource Type is commonly used for scenarios like identifying cost changes in groups of similar resources and may include values like Virtual Machine, Data Warehouse, and Load Balancer.

The ResourceType column MUST be present within billing data.  This column MUST be of type String and MUST NOT be null when a corresponding ResourceId is not null.  When a corresponding ResourceId value is null, the ResourceType column value MUST also be null.  Providers MUST use a consistent value-format and a set of values for ResourceType values within their cost and usage datasets.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

The kind of resource for which you are being charged.
## Content Constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | True            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
