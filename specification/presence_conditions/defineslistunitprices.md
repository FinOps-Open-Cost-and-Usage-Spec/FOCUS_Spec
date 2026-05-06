# Defines List Unit Prices

The Defines List Unit Prices presence condition represents a verifiable state where the source operating model defines standard unit prices exclusive of any negotiated or programmatic discounts.

## Requirements

DefinesListUnitPrices MUST adhere to the following requirements:

* DefinesListUnitPrices MUST evaluate to true when the source operating model relies on a published list price as the baseline for calculating costs.
* DefinesListUnitPrices MUST evaluate to false when the source operating model strictly utilizes dynamic or flat-rate billing without a predefined unit rate.

## Presence Condition ID

DefinesListUnitPrices

## Display Name

Defines List Unit Prices

## Description

A verifiable state indicating whether the source operating model defines unit prices exclusive of discounts.

## Version Introduced

1.5
