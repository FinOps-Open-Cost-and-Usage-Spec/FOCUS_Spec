# Includes List Unit Prices

The Includes List Unit Prices condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes standard, non-discounted unit prices.

## Requirements

IncludesListUnitPrices MUST adhere to the following requirements:

* IncludesListUnitPrices MUST evaluate to true when [IncludesUnitPricing](#conditions.includesunitpricing) is true and the *operating model* includes standard, non-discounted unit prices.
* IncludesListUnitPrices MUST evaluate to false when [IncludesUnitPricing](#conditions.includesunitpricing) is false or the *operating model* does not include standard, non-discounted unit prices.

## Condition ID

IncludesListUnitPrices

## Display Name

Includes List Unit Prices

## Description

A verifiable state indicating whether the *operating model* includes standard, non-discounted unit prices.

## Version Introduced

1.5
