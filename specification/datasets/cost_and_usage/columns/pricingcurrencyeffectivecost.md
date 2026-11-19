# Pricing Currency Effective Cost

[Pricing Currency Effective Cost](#col) represents the [Pricing Currency](#col)-denominated equivalent of [Effective Cost](#col). It reflects the cost of a [charge](#term) based on the [resources](#term) used, [services](#term) used, or [contract commitments](#term) recognized in a given [charge period](#term).

[Pricing Currency Effective Cost](#col) applies the same pricing adjustments, amortizations, and exclusions as [Effective Cost](#col), before any currency exchange rate conversion between the [Pricing Currency](#col) and the [Billing Currency](#col). This column provides practitioners with a standardized baseline, allowing them to view costs in a uniform currency before converting from a [consumption currency](#term) to a [national currency](#term) (e.g., platform credits to USD) or from one national currency to another (e.g., EUR to USD).

[Pricing Currency Effective Cost](#col) is commonly used to support FinOps activities, including [accrual-based](#term:accrual-based-accounting) reporting, forecasting, and cost allocation when pricing and billing use different currencies.

## Requirements

[PricingCurrencyEffectiveCost](#col) MUST adhere to the following requirements:

* [PricingCurrencyEffectiveCost](#col) MUST be of type Decimal.
* [PricingCurrencyEffectiveCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [PricingCurrencyEffectiveCost](#col) MUST NOT be null.
* [PricingCurrencyEffectiveCost](#col) MUST be denominated in the [PricingCurrency](#col).
* [PricingCurrencyEffectiveCost](#col) MUST be the [PricingCurrency](#col)-denominated equivalent of [EffectiveCost](#col), before any currency exchange rate conversion.

## Column ID

PricingCurrencyEffectiveCost

## Display Name

Pricing Currency Effective Cost

## Description

The Pricing Currency-denominated equivalent of [Effective Cost](#col), representing the cost of a [charge](#term) based on the [resources](#term) used, [services](#term) used, or [contract commitments](#term) recognized in a given [charge period](#term).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions |                                             |
| ├─ Must                    | [Includes Consumption Currency](#omc)                                                  |
| └─ Should                  | [Includes Pricing-Billing Currency Differences](#omc)                                                                 |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | False                                       |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.2
