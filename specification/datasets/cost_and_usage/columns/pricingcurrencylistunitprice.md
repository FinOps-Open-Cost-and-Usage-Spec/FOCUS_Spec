# Pricing Currency List Unit Price

[Pricing Currency List Unit Price](#col) represents the service-provider-suggested unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col). It is the unit price before the application of any [negotiated pricing terms](#term) or discount-bearing [commitment programs](#term) (e.g., [commitment discount](#term)).

[Pricing Currency List Unit Price](#col) is denominated in the [Pricing Currency](#col). [Pricing Currency List Unit Price](#col) is commonly used for negotiation and rate optimization activities.

## Requirements

[PricingCurrencyListUnitPrice](#col) MUST adhere to the following requirements:

* [PricingCurrencyListUnitPrice](#col) MUST be of type Decimal.
* [PricingCurrencyListUnitPrice](#col) MUST conform to [NumericFormat](#attr) requirements.
* [PricingCurrencyListUnitPrice](#col) MUST adhere to the following nullability requirements:
  * [PricingCurrencyListUnitPrice](#col) MUST be null when [SkuPriceId](#col) is null.
  * [PricingCurrencyListUnitPrice](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [PricingCurrencyListUnitPrice](#col) MUST NOT be null when [SkuPriceId](#col) is not null.
  * [PricingCurrencyListUnitPrice](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [PricingCurrencyListUnitPrice](#col) MAY be null in all other cases.
* When [PricingCurrencyListUnitPrice](#col) is not null, [PricingCurrencyListUnitPrice](#col) MUST adhere to the following requirements:
  * [PricingCurrencyListUnitPrice](#col) MUST be a non-negative decimal value.
  * [PricingCurrencyListUnitPrice](#col) MUST be denominated in the [PricingCurrency](#col).
  * [PricingCurrencyListUnitPrice](#col) MUST represent the service-provider-suggested unit price per [PricingUnit](#col) for the [SKU Price](#term) identified by the given [SkuPriceId](#col).
  * [PricingCurrencyListUnitPrice](#col) MUST NOT reflect [negotiated pricing terms](#term) for the associated [SKU Price](#term).
  * [PricingCurrencyListUnitPrice](#col) MUST NOT reflect any unit price impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

PricingCurrencyListUnitPrice

## Display Name

Pricing Currency List Unit Price

## Description

The service-provider-suggested unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col), expressed in [Pricing Currency](#col).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions |                                             |
| ├─ Must                    | [Includes Consumption Currency](#omc) and [Includes Unit Pricing](#omc)                                                                                           |
| └─ Should                  | [Includes Pricing-Billing Currency Differences](#omc) and [Includes Unit Pricing](#omc)                                                                                                          |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid non-negative decimal value        |

## Version Introduced

1.2
