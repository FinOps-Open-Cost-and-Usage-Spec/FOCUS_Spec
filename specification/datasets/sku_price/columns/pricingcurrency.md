# Pricing Currency

[Pricing Currency](#col) is the [national currency](#term) or [consumption currency](#term) denomination that a [resource](#term) or [service](#term) is priced in. This represents the foundational currency denomination for the provided rate, regardless of what currency it may ultimately be billed in.

## Requirements

[PricingCurrency](#col) MUST adhere to the following requirements:

* [PricingCurrency](#col) MUST be of type String.
* [PricingCurrency](#col) MUST conform to [StringHandling](#attr) requirements.
* [PricingCurrency](#col) MUST conform to [CurrencyFormat](#attr) requirements.
* [PricingCurrency](#col) MUST NOT be null.
* [PricingCurrency](#col) MUST represent a [national currency](#term) or a [consumption currency](#term).
* [PricingCurrency](#col) documentation MUST adhere to the following requirements:
  * [PricingCurrency](#col) documentation MUST specify how to determine whether a value represents a [national currency](#term).
  * [PricingCurrency](#col) documentation MUST be accessible to practitioners.

## Column ID

PricingCurrency

## Display Name

Pricing Currency

## Description

The [national currency](#term) or [consumption currency](#term) denomination that a [resource](#term) or [service](#term) is priced in.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | [Currency Format](#attr)                             |

## Version Introduced

Preview: 1.5
