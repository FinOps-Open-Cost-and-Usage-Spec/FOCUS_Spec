# Commitment Discount Quantity

Commitment Discount Quantity is the amount of a [*commitment discount*](#commitment-discount) purchased or accounted for in *commitment discount* related [*rows*](#glossary:row) that is denominated in [*Commitment Discount Units*](#glossary:commitmentdiscountunit). The aggregated Commitment Discount Quantity across purchase records, pertaining to a particular [Commitment Discount ID](#commitmentdiscountid) during its [*term*](#glossary:term), represents the total *Commitment Discount Units* acquired with that commitment discount. For committed usage, the Commitment Discount Quantity is either the number of *Commitment Discount Units* consumed by a [*row*](glossary:#row) that is covered by a *commitment discount* or is the unused portion of a *commitment discount* over a *charge period*. Commitment Discount Quantity is commonly used in *commitment discount* analysis and optimization use cases and only applies to *commitment discounts*, not [*negotiated discounts*](#glossary:negotiated-discount).

When *CommitmentDiscountCategory* is "Usage" (usage-based *commitment discounts*), the Commitment Discount Quantity reflects the predefined amount of usage purchased or consumed. If *commitment flexibility* is applicable, this value may be further transformed based on additional, provider-specific requirements. When *CommitmentDiscountCategory* is "Spend" (spend-based *commitment discounts*), the Commitment Discount Quantity reflects the predefined amount of spend purchased or consumed.

**Important:** When aggregating Commitment Discount Quantity for utilization calculations, it's important to exclude *commitment discount* purchases (i.e. when *ChargeCategory* is "Purchase") that are paid to cover future eligible charges (e.g., *Commitment Discount*). This exclusion helps prevent double counting of these quantities in the aggregation.

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in a FOCUS dataset when the provider supports *commitment discounts*.
* CommitmentDiscountQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountQuantity MAY be negative if [*ChargeClass*](#chargeclass) is "Correction".

In cases where the *ChargeCategory* is "Purchase" and [*CommitmentDiscountId*](#commitmentdiscountid) is not null, the following applies:

* When [*ChargeFrequency*](#chargefrequency) is "One-Time", and *CommitmentDiscountId* is not null, CommitmentDiscountQuantity MUST be the positive quantity of *CommitmentDiscountUnits*, paid fully or partially upfront, that is eligible for consumption over the *commitment discount's* *term*.
* When *ChargeFrequency* is "Recurring", and *CommitmentDiscountId* is not null, CommitmentDiscountQuantity MUST be the positive quantity of *CommitmentDiscountUnits* that is eligible for consumption for each *charge period* that corresponds with the purchase.

In cases where the *ChargeCategory* is "Usage" and *CommitmentDiscountId* is not null, the following applies:

* When *CommitmentDiscountStatus* is "Used", and *ChargeClass* is not "Correction", CommitmentDiscountQuantity MUST be the positive, metered quantity of *CommitmentDiscountUnits* that is consumed over the *row's* *charge period*.
* When *CommitmentDiscountStatus* is "Unused", and *ChargeClass* is not "Correction", CommitmentDiscountQuantity MUST be the remaining, positive, unused quantity of *CommitmentDiscountUnits* for the *row's* *charge period*.

CommitmentDiscountQuantity MUST be null for all other *ChargeCategory* values.

## Column ID

CommitmentDiscountQuantity

## Display Name

Commitment Discount Quantity

## Description

The amount of a *commitment discount* purchased or accounted for in *commitment discount* related *rows* that is denominated in *Commitment Discount Units*.

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