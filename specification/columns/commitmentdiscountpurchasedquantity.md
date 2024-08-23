# Commitment Discount Purchased Quantity

Commitment Discount Purchased Quantity is the numeric value of [CommitmentDiscountUnits](#commitmentdiscountunit) that is eligible for amortization for upfront or recurring purchase of a [*commitment discount*](#glossary:commitment-discount), not to be confused with a [*negotiated discount*](#glossary:negotiated-discount).

The CommitmentDiscountPurchasedQuantity column adheres to the following requirements:

* CommitmentDiscountPurchasedQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
* CommitmentDiscountPurchasedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements when [ChargeCategory](#chargecategory) is *Purchase* and [CommitmentDiscountId](#commitmentdiscountid) is not null.
* CommitmentDiscountPurchasedQuantity value MUST be the total, positive quantity of units, denoted by [CommitmentDiscountUnit](#commitmentdiscountunit), available for a *commitment discount* across the [charge period](#glossary:chargeperiod).
* CommitmentDiscountPurchasedQuantity MAY be negative, 0, or null in cases where [ChargeClass](#chargeclass) is "Correction".
* CommitmentDiscountPurchasedQuantity MUST be null in all other cases.

In cases where *ChargeCategory* is "Purchase" and *CommitmentDiscountId* is not null, the following applies:

* When *ChargeFrequency* is "One-Time", CommitmentDiscountPurchasedQuantity MUST be the quantity of *CommitmentDiscountUnits*, paid fully or partially upfront, that is eligible for amortization over all *charge periods* of that *commitment discount's* [term](#glossary:term),
* When *ChargeFrequency* is "Recurring", CommitmentDiscountPurchasedQuantity MUST be the quantity of *CommitmentDiscountUnits*, billed during the *charge period*, that is eligible for amortization over that *charge period*.

## Column ID

CommitmentDiscountPurchasedQuantity

## Display Name

Commitment Discount Purchased Quantity

## Description

The numeric value of *CommitmentDiscountUnits* that is eligible for amortization for any full or partial upfront purchase of a *commitment discount*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.1
