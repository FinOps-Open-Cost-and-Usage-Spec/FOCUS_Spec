# List Unit Price

[List Unit Price](#term) represents the service-provider-suggested unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col). It is the unit price before the application of any [negotiated pricing terms](#term) or discount-bearing [commitment programs](#term) (e.g., [commitment discount](#term)).

[List Unit Price](#col) is denominated in the [Billing Currency](#col). [List Unit Price](#col) is commonly used for negotiation and rate optimization activities.

## Requirements

[ListUnitPrice](#col) MUST adhere to the following requirements:

* [ListUnitPrice](#col) MUST be of type Decimal.
* [ListUnitPrice](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ListUnitPrice](#col) MUST adhere to the following nullability requirements:
  * [ListUnitPrice](#col) MUST be null when [SkuPriceId](#col) is null.
  * [ListUnitPrice](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [ListUnitPrice](#col) MUST NOT be null when [SkuPriceId](#col) is not null.
  * [ListUnitPrice](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [ListUnitPrice](#col) MAY be null in all other cases.
* When [ListUnitPrice](#col) is not null, [ListUnitPrice](#col) MUST adhere to the following requirements:
  * [ListUnitPrice](#col) MUST be a non-negative decimal value.
  * [ListUnitPrice](#col) MUST be denominated in the [BillingCurrency](#col).
  * [ListUnitPrice](#col) MUST represent the service-provider-suggested unit price per [PricingUnit](#col) for the [SKU Price](#term) identified by the given [SkuPriceId](#col).
  * [ListUnitPrice](#col) MUST NOT reflect [negotiated pricing terms](#term) for the associated [SKU Price](#term).
  * [ListUnitPrice](#col) MUST NOT reflect any unit price impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).

## Implementation Guidance

[List Unit Price](#col) is the service-provider-suggested unit price that commonly serves as the starting point for negotiation. It is not necessarily publicly available. For example, it can be provided only in a [price list](#term) specific to a customer.

[List Unit Price](#col) does not reflect any [negotiated pricing terms](#term). This includes the following cases, which may be less obvious:

* Tier configuration: a negotiated tier configuration results in [SKU Price IDs](#col:SkuPriceId) that differ from those of the service-provider-suggested one. For these [SKU Price IDs](#col:SkuPriceId), [List Unit Price](#col) is the service-provider-suggested unit price for the same quantity under the service-provider-suggested tier configuration.
* Currency exchange rates: when the [Pricing Currency](#col) differs from the [Billing Currency](#col), [List Unit Price](#col) does not reflect [negotiated FX pricing terms](#term), such as a negotiated currency exchange rate, even though it is denominated in the [Billing Currency](#col).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The service-provider-suggested unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col).

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions | [Includes Unit Pricing](#omc)                                          |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid non-negative decimal value        |

## Version Introduced

1.0-preview
