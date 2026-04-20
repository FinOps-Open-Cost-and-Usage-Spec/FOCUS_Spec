# Pricing Currency

Pricing Currency is the [*national*](#glossary:national-currency) or [*virtual currency*](glossary:virtual-currency) denomination that a [*resource*](#glossary:resource) or [*service*](#glossary:service) was priced in. Pricing Currency is commonly used in scenarios where different currencies are used for pricing and billing.

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

The *national* or *virtual currency* denomination that a *resource* or *service* was priced in.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | [Currency Format](#attributes.currencyformat)        |

## Introduced (version)

1.2
