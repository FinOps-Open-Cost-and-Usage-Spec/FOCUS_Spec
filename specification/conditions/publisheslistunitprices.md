# Publishes List Unit Prices

The Publishes List Unit Prices condition represents a verifiable state where the operating model publishes standard, non-discounted baseline unit prices that are universally accessible to the public.

## Requirements

PublishesListUnitPrices MUST adhere to the following requirements:

* PublishesListUnitPrices MUST evaluate to false when [IncludesUnitPricing](#conditions.includesunitpricing) evaluates to false.
* PublishesListUnitPrices MUST evaluate to true when the operating model provides predefined "retail" or standard unit rates that anyone can reference (e.g., via a public website or open pricing API) without requiring a negotiated contract.
* PublishesListUnitPrices MUST evaluate to false when the operating model restricts its baseline unit pricing entirely to private agreements or lacks baseline unit prices altogether.

## Condition ID

PublishesListUnitPrices

## Display Name

Publishes List Unit Prices

## Description

A verifiable state indicating whether the operating model publishes baseline unit prices that are publicly accessible.

## Version Introduced

1.5
