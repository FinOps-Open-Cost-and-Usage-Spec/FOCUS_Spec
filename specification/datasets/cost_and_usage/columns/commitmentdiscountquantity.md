# Commitment Discount Quantity

[Commitment Discount Quantity](#col) is the amount of a [commitment discount](#term) purchased or accounted for in [commitment discount](#term) related [rows](#term) that is denominated in [Commitment Discount Units](#col:CommitmentDiscountUnit). The aggregated [Commitment Discount Quantity](#col) across purchase records, pertaining to a particular [Commitment Discount ID](#col) during its commitment [period](#term), represents the total Commitment Discount Units acquired with that commitment discount. For committed usage, the [Commitment Discount Quantity](#col) is either the number of Commitment Discount Units consumed by a [row](#term) that is covered by a [commitment discount](#term) or is the unused portion of a [commitment discount](#term) over a [charge period](#term). [Commitment Discount Quantity](#col) is commonly used in [commitment discount](#term) analysis and optimization use cases and only applies to [commitment discounts](#term), not [negotiated discounts](#term).

When [Commitment Discount Category](#col) is ["Usage"](#val:CostAndUsage.CommitmentDiscountCategory) (usage-based [commitment discounts](#term)), the [Commitment Discount Quantity](#col) reflects the predefined amount of usage purchased or consumed. If [commitment discount flexibility](#term) is applicable, this value may be further transformed based on additional, service-provider-specific requirements. When [Commitment Discount Category](#col) is ["Spend"](#val:CostAndUsage.CommitmentDiscountCategory) (spend-based [commitment discounts](#term)), the [Commitment Discount Quantity](#col) reflects the predefined amount of spend purchased or consumed. See [Appendix: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility) for more details around [commitment discount flexibility](#term).

## Requirements

[CommitmentDiscountQuantity](#col) MUST adhere to the following requirements:

* [CommitmentDiscountQuantity](#col) MUST be of type Decimal.
* [CommitmentDiscountQuantity](#col) MUST conform to [NumericFormat](#attr) requirements.
* [CommitmentDiscountQuantity](#col) MUST adhere to the following nullability requirements:
  * [CommitmentDiscountQuantity](#col) MUST be null when [SkuPriceId](#col) is null.
  * When [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory) or "Purchase" and [CommitmentDiscountId](#col) is not null, [CommitmentDiscountQuantity](#col) MUST adhere to the following requirements:
    * [CommitmentDiscountQuantity](#col) MUST NOT be null when [ChargeClass](#col) is not ["Correction"](#val:CostAndUsage.ChargeClass).
    * [CommitmentDiscountQuantity](#col) MAY be null when [ChargeClass](#col) is ["Correction"](#val:CostAndUsage.ChargeClass).
  * [CommitmentDiscountQuantity](#col) MUST be null in all other cases.
* When [CommitmentDiscountQuantity](#col) is not null and [ChargeCategory](#col) is ["Purchase"](#val:CostAndUsage.ChargeCategory), [CommitmentDiscountQuantity](#col) MUST adhere to the following requirements:
  * [CommitmentDiscountQuantity](#col) MUST be the quantity of [CommitmentDiscountUnit](#col), paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* term when [ChargeFrequency](#col) is ["One-Time"](#val:CostAndUsage.ChargeFrequency).
  * [CommitmentDiscountQuantity](#col) MUST be the quantity of [CommitmentDiscountUnit](#col) that is eligible for consumption for each [charge period](#term) that corresponds with the purchase when [ChargeFrequency](#col) is ["Recurring"](#val:CostAndUsage.ChargeFrequency).
* When [CommitmentDiscountQuantity](#col) is not null and [ChargeCategory](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory), [CommitmentDiscountQuantity](#col) MUST adhere to the following requirements:
  * [CommitmentDiscountQuantity](#col) MUST be the metered quantity of [CommitmentDiscountUnit](#col) that is consumed in a given [charge period](#term) when [CommitmentDiscountStatus](#col) is ["Used"](#val:CostAndUsage.CommitmentDiscountStatus).
  * [CommitmentDiscountQuantity](#col) MUST be the remaining, unused quantity of [CommitmentDiscountUnit](#col) in a given [charge period](#term) when [CommitmentDiscountStatus](#col) is ["Unused"](#val:CostAndUsage.CommitmentDiscountStatus).

## Usability Constraints

**Aggregation:** When aggregating [Commitment Discount Quantity](#col) for commitment utilization calculations, it's important to exclude [commitment discount](#term) purchases (i.e., when [Charge Category](#col) is ["Purchase"](#val:CostAndUsage.ChargeCategory)) that are paid to cover future eligible [charges](#term) (e.g., [commitment discount](#term)). Otherwise, when accounting for all upfront or accrued purchases, it's important to exclude [commitment discount](#term) usage (i.e., when [Charge Category](#col) is ["Usage"](#val:CostAndUsage.ChargeCategory)). This exclusion helps prevent double counting of these quantities in the aggregation.

## Column ID

CommitmentDiscountQuantity

## Display Name

Commitment Discount Quantity

## Description

The amount of a [commitment discount](#term) purchased or accounted for in [commitment discount](#term) related [rows](#term) that is denominated in Commitment Discount Units.

## Content Constraints

| Constraint                 | Value                                       |
| :------------------------- | :------------------------------------------ |
| Dataset                    | [Cost and Usage](#ds)                       |
| Operating model conditions | [Includes Commitment Discounts](#omc)                                                  |
| Column type                | Metric                                      |
| Feature level              | Conditional                                 |
| Allows nulls               | True                                        |
| Data type                  | Decimal                                     |
| Value format               | [Numeric Format](#attr)                     |
| Number range               | Any valid decimal value                     |

## Version Introduced

1.1
