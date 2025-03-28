# Pricing Currency Effective Cost

The Pricing Currency Effective Cost represents the cost of the [*charge*](#glossary:charge) after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge, as denominated in [Pricing Currency](#pricingcurrency).  Pricing Currency Effective Cost can be denominated in [Billing Currency](#billingcurrency) by multiplying by the [Pricing to Billing Effective Exchange Rate](#pricingtobillingeffectiveexchangerate).  This allows the practitioner to perform a conversion from either 1) a [*national currency*](#glossary:nationalcurrency) to a [*virtual currency*](#glossary:virtualcurrency) (e.g. tokens to USD), or 2) one national currency to another (e.g. EUR to USD).

The PricingCurrencyEffectiveCost column adheres to the following requirements:

* PricingCurrencyEffectiveCost presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyEffectiveCost MUST be present in a FOCUS dataset when the provider supports prices in virtual currency and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost is RECOMMENDED to be present in a FOCUS dataset when the provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a FOCUS dataset in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to [NumericFormat](#numericformat) requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be a valid decimal value.
* PricingCurrencyEffectiveCost MUST be denominated in the [PricingCurrency](#pricingcurrency).
* PricingCurrencyEffectiveCost MUST be 0 in the event of prepaid purchases or purchases that are applicable to previous usage. 

## Column ID

PricingCurrencyEffectiveCost

## Display Name

Pricing Currency Effective Cost

## Description

The cost of the [*charge*](#glossary:charge) after applying all reduced rates, discounts, and the applicable portion of relevant, prepaid purchases (one-time or recurring) that covered this charge, as denominated in [Pricing Currency](#pricingcurrency).

## Usability Constraints

**Aggregation:** Given that Pricing Currency Effective Cost can contain a combination of national and/or virtual currencies, it is necessary to group by the [Pricing Currency](#pricingcurrency) column before performing any Pricing Currency Effective Cost aggregations.  Other cost columns such as [Effective Cost](#effectivecost) state all values in a unified [Billing Currency](#billingcurrency) and therefore do not require such a grouping.

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
