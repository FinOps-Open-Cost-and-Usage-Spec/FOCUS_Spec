# Includes SKU Prices

The Includes SKU Prices condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes [*SKU Prices*](#glossary:sku-price).

## Requirements

IncludesSkuPrices MUST adhere to the following requirements:

* IncludesSkuPrices MUST evaluate to true when the *operating model* includes *SKU Prices*.
* IncludesSkuPrices MUST evaluate to false when the *operating model* does not include *SKU Prices*.

> **Note:** An *operating model* does not include *SKU Prices* when no billing party maintains a standing catalog of them (e.g., auction-based marketplaces, pure pass-through aggregation of third-party prices, or exclusively bespoke-quoted capacity).

## Condition ID

IncludesSkuPrices

## Display Name

Includes SKU Prices

## Description

A verifiable state indicating whether the *operating model* includes *SKU Prices*.

## Version Introduced

1.5
