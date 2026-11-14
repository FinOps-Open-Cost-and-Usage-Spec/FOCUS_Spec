# Includes Context Window Pricing

The Includes Context Window Pricing operating model condition represents a verifiable state indicating whether the [*operating model*](#glossary:operating-model) includes context-window pricing tiers based on the number of input [*tokens*](#glossary:token), including cached input *tokens*, consumed from a single request.

> **Preview:** Includes Context Window Pricing exists for the SKU Price dataset, which is a preview in this version of FOCUS. While that dataset is a preview, Includes Context Window Pricing may change in the next version without a deprecation notice.

## Requirements

IncludesContextWindowPricing MUST adhere to the following requirements:

* IncludesContextWindowPricing MUST evaluate to true when the *operating model* includes context-window pricing tiers.
* IncludesContextWindowPricing MUST evaluate to false when the *operating model* does not include context-window pricing tiers.

## Operating Model Condition ID

IncludesContextWindowPricing

## Display Name

Includes Context Window Pricing

## Description

A verifiable state indicating whether the *operating model* includes context-window pricing tiers.

## Version Introduced

Preview: 1.6
