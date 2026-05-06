# Includes Multiple Pricing Categories

The Includes Multiple Pricing Categories presence condition represents a verifiable state where the [source operating model](#glossary:source-operating-model) includes more than one pricing category across all SKUs.

## Requirements

IncludesMultiplePricingCategories MUST adhere to the following requirements:

* IncludesMultiplePricingCategories MUST evaluate to true when the source operating model supports more than one pricing category (e.g., On-Demand, Reservation, Spot).
* IncludesMultiplePricingCategories MUST evaluate to false when the source operating model supports only a single pricing category.

## Presence Condition ID

IncludesMultiplePricingCategories

## Display Name

Includes Multiple Pricing Categories

## Description

A verifiable state indicating whether the source operating model includes more than one pricing category across all SKUs.

## Version Introduced

1.5
