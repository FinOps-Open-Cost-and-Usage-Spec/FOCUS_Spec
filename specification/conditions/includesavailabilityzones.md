# Includes Availability Zones

The Includes Availability Zones condition represents a verifiable state where the [operating model](#glossary:operating-model) includes deploying resources or services within an availability zone.

## Requirements

IncludesAvailabilityZones MUST adhere to the following requirements:

* IncludesAvailabilityZones MUST evaluate to true when the operating model includes the ability to deploy resources or services within an availability zone.
* IncludesAvailabilityZones MUST evaluate to false when the operating model does not support availability zone placement.

## Condition ID

IncludesAvailabilityZones

## Display Name

Includes Availability Zones

## Description

A verifiable state indicating whether the operating model includes deploying resources or services within an availability zone.

## Version Introduced

1.5
