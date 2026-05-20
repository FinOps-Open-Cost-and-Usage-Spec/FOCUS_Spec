# Includes List Unit Prices

The Includes List Unit Prices condition represents a verifiable state where the [*operating model*](#glossary:operating-model) includes standard, non-discounted baseline unit prices, regardless of whether that price list is public or private.

## Requirements

IncludesListUnitPrices MUST adhere to the following requirements:

* IncludesListUnitPrices MUST evaluate to false when [IncludesUnitPricing](#conditions.includesunitpricing) evaluates to false.
* IncludesListUnitPrices MUST evaluate to true when the *operating model* provides predefined "retail" or standard unit rates (e.g., a standard price catalog or baseline rate card), even when those prices are restricted to authenticated users or private customer portals.
* IncludesListUnitPrices MUST evaluate to false when the operating model lacks baseline unit prices altogether (e.g., all pricing is entirely custom-quoted without a standard starting rate).

## Condition ID

IncludesListUnitPrices

## Display Name

Includes List Unit Prices

## Description

A verifiable state indicating whether the operating model includes standard, non-discounted baseline unit prices.

## Version Introduced

1.5
