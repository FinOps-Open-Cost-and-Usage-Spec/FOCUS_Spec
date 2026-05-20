# Includes Capacity Reservations

The Includes Capacity Reservations condition represents a verifiable state where the [*operating model*](#glossary:operating-model) encompasses the procurement, allocation, or billing of infrastructure or service [*capacity reservations*](#glossary:capacity-reservation).

## Requirements

IncludesCapacityReservations MUST adhere to the following requirements:

* IncludesCapacityReservations MUST evaluate to true when the operating model contains a mechanism to reserve capacity.
* IncludesCapacityReservations MUST evaluate to false when the operating model lacks any commercial or technical construct for reserving capacity.

## Condition ID

IncludesCapacityReservations

## Display Name

Includes Capacity Reservations

## Description

A verifiable state indicating whether the operating model supports or includes the use of capacity reservations.

## Version Introduced

1.5
