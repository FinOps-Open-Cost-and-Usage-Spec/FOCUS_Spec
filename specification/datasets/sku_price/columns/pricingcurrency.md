# Pricing Currency

Pricing Currency is the [*national currency*](#glossary:national-currency) or [*consumption currency*](#glossary:consumption-currency) denomination that a [*resource*](#glossary:resource) or [*service*](#glossary:service) is priced in. This represents the foundational currency denomination for the provided rate, regardless of what currency it may ultimately be billed in.

## Requirements

PricingCurrency MUST adhere to the following requirements:

* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* PricingCurrency MUST NOT be null.
* PricingCurrency MUST represent a *national currency* or a *consumption currency*.
* PricingCurrency documentation MUST adhere to the following requirements:
  * PricingCurrency documentation MUST specify how to determine whether a value represents a *national currency*.
  * PricingCurrency documentation MUST be accessible to practitioners.

## Column ID

PricingCurrency

## Display Name

Pricing Currency

## Description

The *national currency* or *consumption currency* denomination that a *resource* or *service* is priced in.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | [Currency Format](#attributes.currencyformat)        |

## Version Introduced

1.5
