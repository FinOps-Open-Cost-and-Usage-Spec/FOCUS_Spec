# Commitment Consumed Quantity

Commitment Consumed Quantity is the numeric value of [CommitmentConsumedUnits](#commitmentconsumedunit) that is either applied to a metered [*resource*](#glossary:resource) or [*service*](#glossary:service) or is unused over a [*charge period*](#glossary:chargeperiod).

CommitmentConsumedQuantity MUST be present in the billing data when the provider supports *commitment-based discounts*. When CommitmentDiscountStatus is "Used", CommitmentConsumedQuantity MUST be the amortized quantity of a corresponding *commitment-based discount* by a metered *resource* or *service* over the charge period. When CommitmentDiscountStatus is "Unused", CommitmentConsumedQuantity MUST be the remaining, unused quantity for the corresponding *commitment-based-discount* over the charge period. CommitmentConsumedQuantity values MUST be less than or equal to the corresponding ConsumedQuantity value over a charge period when both values are not null and ConsumedUnit and CommitmentConsumedUnit values are equal.

CommitmentConsumedQuantity MUST be null when [ChargeCategory](#chargecategory) is *Purchase*, [PricingCategory](#pricingcategory) is *Committed*, and [*CommitmentDiscountId*](#commitmentdiscountid) is not null.

CommitmentConsumedQuantity MUST be a positive value when [ChargeCategory](#chargecategory) is *Usage*, [PricingCategory](#pricingcategory) is *Committed*, [ResourceId](#resourceid) is not null, and [CommitmentDiscountId](#commitmentdiscountid) is not null.

CommitmentConsumedQuantity MUST be null in all other cases.

## Column ID

CommitmentConsumedQuantity

## Display Name

Commitment Consumed Quantity

## Description

The numeric value of *CommitmentConsumedUnits* that is either applied to a metered *resource* or *service* or is unused over a *charge period*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Numeric          |
| Value format    | Any valid, non-negative, decimal value |

## Introduced (version)

1.1
