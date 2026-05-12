# Includes Capacity Reservations

The Includes Capacity Reservations presence condition represents a verifiable state where the source operating model encompasses the procurement, allocation, or billing of infrastructure or service [*capacity reservations*](#glossary:capacity-reservation).

## Requirements

IncludesCapacityReservations MUST adhere to the following requirements:

* IncludesCapacityReservations MUST evaluate to true when the source operating model contains a mechanism to reserve capacity.
* IncludesCapacityReservations MUST evaluate to false when the source operating model lacks any commercial or technical construct for reserving capacity.

## Presence Condition ID

IncludesCapacityReservations

## Display Name

Includes Capacity Reservations

## Description

A verifiable state indicating whether the source operating model supports or includes the use of capacity reservations.

## Version Introduced

1.5
