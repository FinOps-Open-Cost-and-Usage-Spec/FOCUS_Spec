# Pricing Currency Effective Cost

The Pricing Currency Effective Cost represents the cost of the [*charge*](#glossary:charge) after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this *charge*, as denominated in [Pricing Currency](#datasets.costandusage.pricingcurrency). This allows the practitioner to perform a conversion from either 1) a [*national currency*](#glossary:nationalcurrency) to a [*virtual currency*](#glossary:virtualcurrency) (e.g., tokens to USD), or 2) one national currency to another (e.g., EUR to USD).

## Requirements

PricingCurrencyEffectiveCost MUST adhere to the following requirements:

* PricingCurrencyEffectiveCost presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) MUST adhere to the following presence requirements:
  * PricingCurrencyEffectiveCost SHOULD be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage.
* PricingCurrencyEffectiveCost MUST be denominated in the [PricingCurrency](#datasets.costandusage.pricingcurrency).

## Column ID

PricingCurrencyEffectiveCost

## Display Name

Pricing Currency Effective Cost

## Description

The cost of the *charge* after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this *charge*, as denominated in Pricing Currency.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | False                                                |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

1.2
