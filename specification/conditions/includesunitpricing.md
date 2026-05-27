# Includes Unit Pricing

The Includes Unit Pricing condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes unit pricing concepts.

## Requirements

IncludesUnitPricing MUST adhere to the following requirements:

* IncludesUnitPricing MUST evaluate to true when the *operating model* utilizes a per-unit billing mechanic.
* IncludesUnitPricing MUST evaluate to false when the *operating model* strictly utilizes dynamic, flat-rate, or purely tier-based billing without a distinct per-unit rate.

## Condition ID

IncludesUnitPricing

## Display Name

Includes Unit Pricing

## Description

A verifiable state indicating whether the *operating model* includes unit pricing concepts.

## Version Introduced

1.5
