# Includes Virtual Currency

The Includes Virtual Currency condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes prices in a [*consumption currency*](#glossary:consumption-currency).

> **Note:** A *consumption currency* is the service-provider-issued subtype of [*virtual currency*](#glossary:virtual-currency). This condition is deliberately scoped to consumption currencies, which is the case the columns it gates address. A price denominated in another form of *virtual currency*, such as a cryptocurrency, does not by itself satisfy this condition.

## Requirements

IncludesVirtualCurrency MUST adhere to the following requirements:

* IncludesVirtualCurrency MUST evaluate to true when the *operating model* includes prices in a *consumption currency*.
* IncludesVirtualCurrency MUST evaluate to false when the *operating model* does not include prices in a *consumption currency*.

## Condition ID

IncludesVirtualCurrency

## Display Name

Includes Virtual Currency

## Description

A verifiable state indicating whether the *operating model* includes prices in a *consumption currency*.

## Version Introduced

1.5
