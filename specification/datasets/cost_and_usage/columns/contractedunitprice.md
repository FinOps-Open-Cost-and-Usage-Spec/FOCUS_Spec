# Contracted Unit Price

[Contracted Unit Price](#term) represents the negotiated unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col). It is the unit price before the application of any discount-bearing [commitment programs](#term) (e.g., [commitment discount](#term)).

When no [negotiated pricing terms](#term) apply to the [charge](#term), [Contracted Unit Price](#col) defaults to [List Unit Price](#col).

[Contracted Unit Price](#col) is denominated in the [Billing Currency](#col). [Contracted Unit Price](#col) is commonly used for negotiation and rate optimization activities.

## Requirements

[ContractedUnitPrice](#col) MUST adhere to the following requirements:

* [ContractedUnitPrice](#col) MUST be of type Decimal.
* [ContractedUnitPrice](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ContractedUnitPrice](#col) MUST adhere to the following nullability requirements:
  * [ContractedUnitPrice](#col) MUST be null when [SkuPriceId](#col) is null.
  * [ContractedUnitPrice](#col) MUST be null when [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory).
  * [ContractedUnitPrice](#col) MUST NOT be null when [SkuPriceId](#col) is not null.
  * [ContractedUnitPrice](#col) MUST NOT be null when [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
  * [ContractedUnitPrice](#col) MAY be null in all other cases.
* When [ContractedUnitPrice](#col) is not null, [ContractedUnitPrice](#col) MUST adhere to the following requirements:
  * [ContractedUnitPrice](#col) MUST be a non-negative decimal value.
  * [ContractedUnitPrice](#col) MUST be denominated in the [BillingCurrency](#col).
  * [ContractedUnitPrice](#col) MUST reflect [negotiated pricing terms](#term) for the [SKU Price](#term) identified by the given [SkuPriceId](#col) that are independent of any discount-bearing [commitment programs](#term) being applied to the [charge](#term).
  * [ContractedUnitPrice](#col) MUST NOT reflect any unit price impact dependent on a discount-bearing [commitment program](#term) being applied to the [charge](#term).
  * [ContractedUnitPrice](#col) MUST equal [ListUnitPrice](#col) when no [negotiated pricing terms](#term) apply to the [charge](#term).

## Implementation Guidance

Every [charge](#term) with a [SKU Price ID](#col) has a [Contracted Unit Price](#col), whether or not [negotiated pricing terms](#term) apply. Agreeing to a contract does not by itself introduce [negotiated pricing terms](#term); only privately agreed terms that modify the service-provider-suggested pricing do.

Unlike [List Unit Price](#col), [Contracted Unit Price](#col) reflects [negotiated pricing terms](#term) when they apply to the [SKU Price](#term) identified by the given [SKU Price ID](#col). These may include a negotiated unit price, a negotiated tier configuration, and [negotiated FX pricing terms](#term), such as a negotiated currency exchange rate. When no [negotiated pricing terms](#term) apply, [Contracted Unit Price](#col) equals [List Unit Price](#col).

[Pricing Currency Contracted Unit Price](#col) does not reflect [negotiated FX pricing terms](#term), because it is before any currency exchange rate conversion.

The terms of a [commitment program](#term) can also be negotiated, such as the unit price for its purchase, its discount, or its eligibility. A [negotiated discount](#term) (e.g., a discount received in exchange for a spend commitment) is reflected in [Contracted Unit Price](#col). The impact of applying a [commitment discount](#term) to [covered charges](#term) is not; it is reflected in their [Effective Cost](#col).

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ContractedUnitPrice

## Display Name

Contracted Unit Price

## Description

The negotiated unit price per [Pricing Unit](#col) for the [SKU Price](#term) identified by the given [SKU Price ID](#col).

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

1.0
