# Pricing Currency

[Pricing Currency](#col) is the [national](#term:national-currency) or [consumption currency](#term) denomination that a [resource](#term) or [service](#term) was priced in. [Pricing Currency](#col) is commonly used in scenarios where different currencies are used for pricing and billing.

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

The *national* or [consumption currency](#term) denomination that a [resource](#term) or [service](#term) was priced in.

## Content Constraints

| Constraint                 | Value                                         |
| :------------------------- | :-------------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                         |
| Operating model conditions | [Includes Pricing-Billing Currency Differences](#omc)                                                                 |
| Column type                | Dimension                                     |
| Feature level              | Conditional                                   |
| Allows nulls               | False                                         |
| Data type                  | String                                        |
| Value format               | [Currency Format](#attr)                      |

## Version Introduced

1.2
