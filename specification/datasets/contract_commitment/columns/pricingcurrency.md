# Pricing Currency

[Pricing Currency](#col) is the [national](#term:national-currency) or [consumption currency](#term) denomination that a [contract commitment](#term) was priced in. This is commonly used in scenarios where a commitment is negotiated in one currency but billed in another.

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

The *national* or [consumption currency](#term) denomination that the [Contract Commitment Cost](#col) was priced in.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | [Includes Pricing-Billing Currency Differences](#omc)                                                                 |
| Column type                | Dimension                                            |
| Feature level              | Conditional                                          |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | [Currency Format](#attr)                             |

## Version Introduced

1.4
