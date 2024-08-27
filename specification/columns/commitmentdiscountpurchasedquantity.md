# Commitment Discount Purchased Quantity

Commitment Discount Purchased Quantity is the total, positive quantity of [Commitment Discount Units](#commitmentdiscountunit) that is eligible for consumption from a [*commitment discount's*](#glossary:commitment-discount) purchase over a [*row's*](glossary:row) [*charge period*](#glossary:chargeperiod). The CommitmentDiscountPurchaseQuantity column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountPurchasedQuantity column adheres to the following requirements:

* CommitmentDiscountPurchasedQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
* CommitmentDiscountPurchasedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* When [*ChargeCategory*](#chargecategory) is "Purchase", [*ChargeFrequency*](#chargefrequency) is "One-Time", and [*CommitmentDiscountId*](#commitmentdiscountid) is not null, CommitmentDiscountPurchaseQuantity MUST be the total, positive quantity of *CommitmentDiscountUnits*, paid fully or partially upfront, that is eligible for amortization across the *commitment discount's* *term*.
* When *ChargeCategory* is "Purchase", *ChargeFrequency* is "Recurring", and *CommitmentDiscountId* is not null, CommitmentDiscountPurchasedQuantity MUST be the total, positive quantity of *CommitmentDiscountUnits* that is eligible for amortization for each *charge period* that corresponds with the purchase.
* CommitmentDiscountPurchasedQuantity MAY be negative, 0, or null in cases where [*ChargeClass*](#chargeclass) is "Correction".
* CommitmentDiscountPurchasedQuantity MUST be null in all other cases.

## Column ID

CommitmentDiscountPurchasedQuantity

## Display Name

Commitment Discount Purchased Quantity

## Description

The total, positive quantity of Commitment Discount Units that is eligible for consumption from a *commitment discount's* purchase over the *row's* *charge period*.

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
