# Pricing Currency Effective Cost

Pricing Currency Effective Cost represents the [Pricing Currency](#datasets.costandusage.pricingcurrency)-denominated equivalent of [Effective Cost](#datasets.costandusage.effectivecost). It reflects the cost of a [*charge*](#glossary:charge) based on the [*resources*](#glossary:resource) used, [*services*](#glossary:service) used, or [*contract commitments*](#glossary:contract-commitment) recognized in a given [*charge period*](#glossary:charge-period). Pricing Currency Effective Cost differs from Effective Cost only in denomination, not in the cost it represents.

For all *charges*, Pricing Currency Effective Cost reflects all applicable pricing adjustments (e.g., reduced pricing from [*negotiated discounts*](#glossary:negotiated-discount) or [*commitment discounts*](#glossary:commitment-discount)). For usage *charges*, Pricing Currency Effective Cost includes the recognized portion of purchase *charges* applied to this *charge* (e.g., amortized portions of prepayments, drawdowns). For purchase *charges*, Pricing Currency Effective Cost excludes any amounts recognized in related usage *charges* (e.g., usage [*covered*](#glossary:covered-charge) by [*covering charges*](#glossary:covering-charge) such as *commitments*, pre-payments, or marketplace purchases which draw down based on usage), regardless of when those related *charges* are invoiced.

Pricing Currency Effective Cost is denominated in the [Pricing Currency](#datasets.costandusage.pricingcurrency). This allows the practitioner to perform a conversion from either 1) a [*national currency*](#glossary:national-currency) to a [*virtual currency*](#glossary:virtual-currency) (e.g., tokens to USD), or 2) one national currency to another (e.g., EUR to USD). Pricing Currency Effective Cost is commonly used to support FinOps activities, including [*accrual-based*](#glossary:accrual-based-accounting) reporting, forecasting, and cost allocation when pricing and billing use different currencies.

## Requirements

PricingCurrencyEffectiveCost MUST adhere to the following requirements:

* PricingCurrencyEffectiveCost presence in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) MUST adhere to the following presence requirements:
  * PricingCurrencyEffectiveCost SHOULD be present in a Cost and Usage *FOCUS dataset* when the service provider supports pricing and billing in different currencies and publishes unit prices exclusive of discounts.
  * PricingCurrencyEffectiveCost MAY be present in a Cost and Usage *FOCUS dataset* in all other cases.
* PricingCurrencyEffectiveCost MUST be of type Decimal.
* PricingCurrencyEffectiveCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingCurrencyEffectiveCost MUST NOT be null.
* PricingCurrencyEffectiveCost MUST be a valid decimal value.
* PricingCurrencyEffectiveCost MUST be denominated in the [PricingCurrency](#datasets.costandusage.pricingcurrency).
* PricingCurrencyEffectiveCost MUST be the PricingCurrency-denominated equivalent of [EffectiveCost](#datasets.costandusage.effectivecost). All normative requirements that apply to EffectiveCost apply equivalently to PricingCurrencyEffectiveCost when denominated in PricingCurrency.

## Column ID

PricingCurrencyEffectiveCost

## Display Name

Pricing Currency Effective Cost

## Description

The PricingCurrency-denominated equivalent of Effective Cost, representing the cost of a *charge* based on the *resources* used, *services* used, or *contract commitments* recognized in a given *charge period*.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

1.2
