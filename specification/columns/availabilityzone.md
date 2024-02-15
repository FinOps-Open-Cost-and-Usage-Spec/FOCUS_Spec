# Availability Zone

[Availability Zone](#glossary:availability-zone) is a provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance. Availability Zone is commonly used for scenarios like analyzing cross-zone data transfer usage and the corresponding cost based on where [*resources*](#glossary:resource) are deployed.

The AvailabilityZone column SHOULD be present in the billing data. This column MUST be of type String and MAY contain null values.

## Column ID

AvailabilityZone

## Display name

Availability Zone

## Description

A provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance.

## Content constraints

| Constraint          | Value            |
|:--------------------|:-----------------|
| Column type         | Dimension        |
| Dataset requirement | Extended         |
| Allows nulls        | True             |
| Data type           | String           |
| Value format        | \<not specified> |

## Introduced (version)

0.5
