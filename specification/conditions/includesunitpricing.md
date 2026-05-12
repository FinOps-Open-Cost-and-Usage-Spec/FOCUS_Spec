# Includes Unit Pricing

The Includes Unit Pricing presence condition represents a verifiable state where the source operating model calculates charges based on a measured quantity multiplied by a predefined rate.

## Requirements

IncludesUnitPricing MUST adhere to the following requirements:

* IncludesUnitPricing MUST evaluate to true when the source operating model utilizes a per-unit billing mechanic.
* IncludesUnitPricing MUST evaluate to false when the source operating model strictly utilizes dynamic, flat-rate, or purely tier-based billing without a distinct per-unit rate.

## Presence Condition ID

IncludesUnitPricing

## Display Name

Includes Unit Pricing

## Description

A verifiable state indicating whether the source operating model includes unit pricing concepts.

## Version Introduced

1.5
