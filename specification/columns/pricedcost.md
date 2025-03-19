# Priced Cost

The Priced Cost represents the cost of the [*charge*](#glossary:charge) after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge, as denominated in [Pricing Currency](#pricingcurrency).  Priced Cost can be denominated in [Billing Currency](#billingcurrency) by multiplying by the [Pricing to Billing Exchange Rate](#pricingtobillingexchangerate).  This allows the practitioner to perform a conversion from either 1) a [*national currency*](#glossary:nationalcurrency) to a [*virtual currency*](#glossary:virtualcurrency) (e.g. tokens to USD), or 2) one national currency to another (e.g. EUR to USD).

The PricedCost column adheres to the following requirements:

* PricedCost presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricedCost MUST be present in a FOCUS dataset when the provider supports virtual currencies (e.g. credits, tokens).
  * PricedCost MUST be present in a FOCUS dataset when the provider presents prices and usage in different national currencies (e.g. prices in USD and usage in EUR).
  * PricedCost MAY be present in a FOCUS dataset in all other cases.
* PricedCost MUST be of type Decimal.
* PricedCost MUST conform to [NumericFormat](#numericformat) requirements.
* PricedCost MUST NOT be null.
* PricedCost MUST be a valid decimal value.
* PricedCost MUST be denominated in the [PricingCurrency](#pricingcurrency).

## Column ID

PricedCost

## Display Name

Priced Cost

## Description

The cost of the [*charge*](#glossary:charge) as denominated in [Pricing Currency](#pricingcurrency),

## Content Constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Conditional             |
| Allows nulls    | True                    |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.2
