# Pricing Currency

Pricing Currency is the [*national*](#glossary:national-currency) or [*virtual currency*](#glossary:virtual-currency) denomination that a [*resource*](#glossary:resource) or [*service*](#glossary:service) is priced in. This represents the foundational currency denomination for the provided rate, regardless of what currency it may ultimately be billed in.

## Requirements

PricingCurrency MUST adhere to the following requirements:

* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* PricingCurrency MUST NOT be null.

## Column ID

PricingCurrency

## Display Name

Pricing Currency

## Description

The *national* or *virtual currency* denomination that a *resource* or *service* is priced in.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | [Currency Format](#attributes.currencyformat)        |

## Version Introduced

1.5
