# Pricing Currency Contracted Unit Price

[Pricing Currency Contracted Unit Price](#col) represents the negotiated unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col). It is the unit price before any currency exchange rate conversion or the application of any discount-bearing [commitment programs](#term) (e.g., [commitment discount](#term)).

When no [negotiated non-FX pricing terms](#term) apply to the [charge](#term), [Pricing Currency Contracted Unit Price](#col) defaults to [Pricing Currency List Unit Price](#col).

[Pricing Currency Contracted Unit Price](#col) is denominated in the [Pricing Currency](#col). [Pricing Currency Contracted Unit Price](#col) is commonly used for negotiation and rate optimization activities.

## Requirements

[PricingCurrencyContractedUnitPrice](#col) MUST adhere to the following requirements:

* [PricingCurrencyContractedUnitPrice](#col) MUST be of type Decimal.
* [PricingCurrencyContractedUnitPrice](#col) MUST conform to [NumericFormat](#attr) requirements.
* [PricingCurrencyContractedUnitPrice](#col) MUST adhere to the following nullability requirements:
  * [PricingCurrencyContractedUnitPrice](#col) MUST be null when [SkuPriceId](#col) is null.
  * [PricingCurrencyContractedUnitPrice](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [PricingCurrencyContractedUnitPrice](#col) MUST NOT be null when [SkuPriceId](#col) is not null.
  * [PricingCurrencyContractedUnitPrice](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [PricingCurrencyContractedUnitPrice](#col) MAY be null in all other cases.
* When [PricingCurrencyContractedUnitPrice](#col) is not null, [PricingCurrencyContractedUnitPrice](#col) MUST adhere to the following requirements:
  * [PricingCurrencyContractedUnitPrice](#col) MUST be a non-negative decimal value.
  * [PricingCurrencyContractedUnitPrice](#col) MUST be denominated in the [PricingCurrency](#col).
  * [PricingCurrencyContractedUnitPrice](#col) MUST reflect [negotiated non-FX pricing terms](#term) for the [SKU Price](#term) identified by the given [SkuPriceId](#col) that are independent of any discount-bearing [commitment programs](#term) being applied to the [charge](#term).
  * [PricingCurrencyContractedUnitPrice](#col) MUST NOT reflect any unit price impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).
  * [PricingCurrencyContractedUnitPrice](#col) MUST equal [PricingCurrencyListUnitPrice](#col) when no [negotiated non-FX pricing terms](#term) apply to the [charge](#term).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

PricingCurrencyContractedUnitPrice

## Display Name

Pricing Currency Contracted Unit Price

## Description

The negotiated unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col), expressed in [Pricing Currency](#col).

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
