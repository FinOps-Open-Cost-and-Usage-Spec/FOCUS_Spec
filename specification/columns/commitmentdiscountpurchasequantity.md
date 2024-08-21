# Commitment Discount Purchase Quantity

Commitment Discount Purchase Quantity is the numeric value of [CommitmentDiscountUnits](#commitmentdiscountunit) that is eligible for amortization for any full or partial upfront purchase of a [*commitment-based discount*](#glossary:commitment-based-discount).

The CommitmentDiscountPurchaseQuantity column adheres to the following requirements:

* CommitmentDiscountPurchaseQuantity MUST be present in the billing data when the provider supports *commitment-based discounts*.
* CommitmentDiscountPurchaseQuantity MUST be a positive value when [ChargeCategory](#chargecategory) is *Purchase* and [CommitmentDiscountId](#commitmentdiscountid) is not null.
* CommitmentDiscountPurchaseQuantity value MUST be the total, positive quantity of units, denoted by [CommitmentDiscountUnit](#commitmentdiscountunit), available for a *commitment-based discount* across the [charge period](#glossary:chargeperiod).
* CommitmentDiscountPurchaseQuantity MAY be negative in cases where [ChargeClass](#chargeclass) is "Correction".
* CommitmentDiscountPurchaseQuantity MUST be null in all other cases.

In cases where *ChargeCategory* is "Purchase" and *CommitmentDiscountId* is not null, the following applies:

* When *ChargeFrequency* is "One-Time", CommitmentDiscountPurchaseQuantity contains the eligible quantity of *CommitmentDiscountUnits* that is paid fully or partially before the *commitment-based discount's* [term](#glossary:term) begins.
* When *ChargeFrequency* is "Recurring", CommitmentDiscountPurchaseQuantity contains the eligible quantity of *CommitmentDiscountUnits* for each
*charge period* of the *commitment-based discount's* *term*.

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
