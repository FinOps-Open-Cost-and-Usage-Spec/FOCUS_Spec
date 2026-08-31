# Pricing Currency

Pricing Currency is the [*national currency*](#glossary:national-currency) or [*consumption currency*](#glossary:consumption-currency) denomination that a [*resource*](#glossary:resource) or [*service*](#glossary:service) is priced in. This represents the foundational currency denomination for the provided unit price, regardless of what currency it may ultimately be billed in.

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

The *national currency* or *consumption currency* denomination that a *resource* or *service* is priced in.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | Not applicable                                        |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | [Currency Format](#attributes.currencyformat)        |

## Version Introduced

1.5
