# Commitment Discount Purchased Quantity

Commitment Discount Purchased Quantity is the total quantity of [Commitment Discount Units](#commitmentdiscountunit) that is eligible for amortization from a [*commitment discount's*](#glossary:commitment-discount) purchase over a corresponding [charge period](#glossary:chargeperiod). The CommitmentDiscountPurchaseQuantity column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountPurchasedQuantity column adheres to the following requirements:

* CommitmentDiscountPurchasedQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
* CommitmentDiscountPurchasedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* When [ChargeCategory](#chargecategory) is "Purchase" and [CommitmentDiscountId](#commitmentdiscountid) is not null, CommitmentDiscountPurchasedQuantity value MUST be the total, positive quantity of units available for a *commitment discount* for the corresponding *charge period*.
* CommitmentDiscountPurchasedQuantity MAY be negative, 0, or null in cases where [ChargeClass](#chargeclass) is "Correction".
* CommitmentDiscountPurchasedQuantity MUST be null in all other cases.

In cases where *ChargeCategory* is "Purchase" and *CommitmentDiscountId* is not null, the following applies:

* When *ChargeFrequency* is "One-Time", CommitmentDiscountPurchaseQuantity MUST match the total number of *CommitmentDiscountUnits*, paid fully or partially upfront, that is eligible for amortization across the *commitment discount's* *term*.
* When *ChargeFrequency* is "Recurring", CommitmentDiscountPurchasedQuantity MUST match the total number of *CommitmentDiscountUnits* that is eligible for amortization for each *charge period* corresponding with the purchase.

## Column ID

CommitmentDiscountPurchasedQuantity

## Display Name

Commitment Discount Purchased Quantity

## Description

The numeric value of CommitmentDiscountUnits that is eligible for amortization from a *commitment discount's* purchase over a corresponding *charge period*.

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
