# Commitment Total Quantity

Commitment Total Quantity is the numeric value of [CommitmentConsumedUnits](#commitmentconsumedunit) that is eligible for amortization for any full or partial upfront purchase of a [*commitment-based discount*](#glossary:commitment-based-discount).

CommitmentTotalQuantity MUST be present in the billing data when the provider supports *commitment-based discounts*. CommitmentTotalQuantity value MUST be the total amount of units, denoted by CommitmentConsumedUnit, available for a *commitment-based discount* for its [*term*](#glossary:term) at the time of an applicable purchase.

When a purchase record exists for a *commitment-based discount*, CommitmentTotalQuantity MUST be a positive value when [ChargeCategory](#chargecategory) is *Purchase*, [PricingCategory](#pricingcategory) is *Committed*, and [CommitmentDiscountId](#commitmentdiscountid) is not null.

CommitmentTotalQuantity MUST be null in all other cases,

## Column ID

CommitmentTotalQuantity

## Display Name

Commitment Total Quantity

## Description

The numeric value of *CommitmentConsumedUnits* that is eligible for amortization for any full or partial upfront purchase of a *commitment-based discount*.

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
