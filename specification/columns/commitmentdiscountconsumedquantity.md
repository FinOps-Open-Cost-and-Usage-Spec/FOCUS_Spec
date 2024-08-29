# Commitment Discount Consumed Quantity

Commitment Discount Consumed Quantity is the metered quantity of [Commitment Discount Units](#commitmentdiscountunit) that is either consumed by a [*row*](glossary:#row) covered by a [*commitment discount*](#glossary:commitmentdiscount) or is the unused portion of a *commitment discount* over a [*charge period*](#glossary:chargeperiod). The CommitmentDiscountConsumedQuantity column only applies to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The Commitment Discount Consumed Quantity helps customers track how efficiently their *commitment discounts* apply to their workloads. The *commitment discount's* utilization rate is typically used to measure this, and it can be derived by dividing the used portion of CommitmentDiscountConsumedQuantity (i.e. where [*CommitmentDiscountStatus*](#commitmentdiscountstatus) is "Used") by the sum of CommitmentDiscountConsumedQuantity for the *charge period*. Across many *charge periods*, and even other *commitment discounts*, this helps customers determine how well their commitment strategy is being applied.

The CommitmentDiscountConsumedQuantity column adheres to the following requirements:

* CommitmentDiscountConsumedQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
* CommitmentDiscountConsumedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* When [*ChargeCategory*](#chargecategory) is "Usage", *CommitmentDiscountStatus* is "Used", and [*ChargeClass*](#chargeclass) is not "Correction", CommitmentDiscountConsumedQuantity MUST be the positive, metered quantity of *CommitmentDiscountUnits* that is consumed over the *row's* *charge period*.
* When *ChargeCategory* is "Usage", *CommitmentDiscountStatus* is "Unused", and *ChargeClass* is not "Correction", CommitmentDiscountConsumedQuantity MUST be the remaining, positive, unused quantity of *CommitmentDiscountUnits* over the *row's* *charge period*
* CommitmentDiscountConsumedQuantity MAY be negative if *ChargeClass* is "Correction".
* CommitmentDiscountConsumedQuantity MUST be null in all other cases.

## Column ID

CommitmentDiscountConsumedQuantity

## Display Name

Commitment Discount Consumed Quantity

## Description

The metered quantity of *Commitment Discount Units* that is either consumed by a *row* covered by a *commitment discount* or is the unused portion of a *commitment discount* over a *charge period*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Decimal          |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.1
