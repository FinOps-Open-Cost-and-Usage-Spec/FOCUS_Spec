# Commitment Discount Purchase Quantity

Commitment Discount Purchase Quantity is the numeric value of [CommitmentDiscountUnits](#commitmentdiscountunit) that is eligible for amortization for any full or partial upfront purchase of a [*commitment-based discount*](#glossary:commitment-based-discount).

The CommitmentDiscountPurchaseQuantity column adheres to the following requirements:

* CommitmentDiscountPurchaseQuantity MUST be present in the billing data when the provider supports *commitment-based discounts*.
* CommitmentDiscountPurchaseQuantity MUST be a positive value when [ChargeCategory](#chargecategory) is *Purchase*, [PricingCategory](#pricingcategory) is *Committed*, and [CommitmentDiscountId](#commitmentdiscountid) is not null.
* CommitmentDiscountPurchaseQuantity value MUST be the total, positive amount of units, denoted by CommitmentDiscountUnit, available for a *commitment-based discount* across its [*term*](#glossary:term) at the time of an applicable purchase.
* CommitmentDiscountPurchaseQuantity MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction".
* CommitmentDiscountPurchaseQuantity MUST be null in all other cases.

## Column ID

CommitmentDiscountPurchaseQuantity

## Display Name

Commitment Discount Purchase Quantity

## Description

The numeric value of *CommitmentDiscountUnits* that is eligible for amortization for any full or partial upfront purchase of a *commitment-based discount*.

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
