# Resource Type

Resource Type describes the kind of resource for which you are being charged.  A Resource Type is commonly used for scenarios like identifying cost changes in groups of similar resources.

Resource Type MUST be present within billing data.  Resource Type MUST be of type String and MUST NOT be NULL when a corresponding ResourceId is not NULL.  When a corresponding ResourceId value is NULL, the ResourceType column value MUST also be NULL.  Resource Type MUST contain consistent values and a consistent value-format that accounts for additional values added.

Some potential values MAY include Virtual Machine, Data Warehouse, and Load Balancer.

## Column ID

ResourceType

## Display Name

Resource Type

## Description

The kind of resource for which you are being charged.

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
