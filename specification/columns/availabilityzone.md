# Availability Zone

An [*availability zone*](#glossary:availability-zone) is a provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance. Availability Zone is commonly used for scenarios like analyzing cross-zone data transfer usage and the corresponding cost based on where [*resources*](#glossary:resource) are deployed.

The AvailabilityZone column adheres to the following requirements:

* AvailabilityZone is RECOMMENDED to be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports deploying resources or services within an *availability zone*.
* AvailabilityZone MUST be of type String.
* AvailabilityZone MUST conform to [String Handling](#stringhandling) requirements.
* AvailabilityZone MAY be null when a charge is not specific to an *availability zone*.

## Column ID

AvailabilityZone

## Display Name

Availability Zone

## Description

A provider-assigned identifier for a physically separated and isolated area within a Region that provides high availability and fault tolerance.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Recommended      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

0.5
