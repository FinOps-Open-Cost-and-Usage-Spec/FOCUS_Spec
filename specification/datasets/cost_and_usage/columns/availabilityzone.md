# Availability Zone

An [*Availability Zone*](#glossary:availability-zone) is a host-provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance. Availability Zone is commonly used for scenarios like analyzing cross-zone data transfer usage and the corresponding cost based on where [*resources*](#glossary:resource) are deployed.

## Requirements

AvailabilityZone MUST adhere to the following requirements:

* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* AvailabilityZone MUST be null when a [*charge*](#glossary:charge) is not specific to an *availability zone*.

## Column ID

AvailabilityZone

## Display Name

Availability Zone

## Description

A host-provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#datamodel.costandusage) |
| Operating model conditions | [Includes Availability Zones](#operatingmodelconditions.includesavailabilityzones) |
| Column type                | Dimension                                 |
| Feature level              | Recommended                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

Preview: 0.5 · GA: 1.0
