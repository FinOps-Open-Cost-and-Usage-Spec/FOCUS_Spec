# Pricing Currency

[*Pricing Currency*](#glossary:pricing-currency) is a value that represents the denomination in which a charge for [*resources*](#glossary:resource) or [*services*](#glossary:service) was priced. Pricing Currency is commonly used in scenarios where costs need to be grouped or aggregated by some combination of the following currency types:

* National currency (e.g. USD, EUR).
* Virtual currency (e.g. tokens, credits).

The PricingCurrency column adheres to the following requirements:

* PricingCurrency MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports pricing and billing in different currencies.
  * PricingCurrency MUST be present in a FOCUS dataset when the provider presents prices and usage in different national currencies (e.g. prices in USD and usage in EUR).
  * PricingCurrency MAY be present in a FOCUS dataset in all other cases.
* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#currencyformat) requirements.
* PricingCurrency MUST NOT be null.

## Column ID

PricingCurrency

## Display Name

Pricing Currency

## Description

Represents the unit of measure in which a charge was priced.

## Content Constraints

| Constraint      | Value                               |
|:----------------|:------------------------------------|
| Column type     | Dimension                           |
| Feature level   | Conditional                         |
| Allows nulls    | True                                |
| Data type       | String                              |
| Value format    | [Currency Format](#currencyformat) |

## Introduced (version)

1.2
