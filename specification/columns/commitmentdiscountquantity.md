# Commitment Discount Quantity

Commitment Discount Quantity is the amount of purchased, used, or unused [*Commitment Discount Units*](#glossary:commitmentdiscountunit) applied to a [*commitment discount's*](#commitment-discount) [*row*](#glossary:row). For a purchase, the Commitment Discount Quantity is either the total or apportioned number of *Commitment Discount Units* over a *commitment discount's* [*term*](#glossary:term). For committed usage, the Commitment Discount Quantity is either the number of *Commitment Discount Units* consumed by a [*row*](glossary:#row) that is covered by a *commitment discount* or is the unused portion of a *commitment discount* over a [*charge period*](#glossary:chargeperiod). The CommitmentDiscountQuantity column only applies to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

For purchases, the Commitment Discount Quantity helps customers track how many total *Commitment Discount Units* are available across *commitment discounts* at various points in time, and for committed usage, it helps customers track how efficiently their *commitment discounts* apply to their workloads. The *commitment discount's* utilization rate is used to measure this efficiency and can be derived by dividing the used portion of CommitmentDiscountQuantity by the sum of CommitmentDiscountQuantity for the *charge period*. As an example, a SQL statement calculating a commitment discount's utilization rate might be:

```sql
SELECT (
    SELECT SUM(CommitmentDiscountQuantity) FROM <dataset> WHERE ChargeCategory = 'Usage'
    AND CommitmentDiscountStatus = 'Used' AND CommitmentDiscountId = '<commitment-discount-id>'
    /
    SELECT SUM(CommitmentDiscountQuantity) FROM <dataset> WHERE ChargeCategory = 'Usage'
    AND CommitmentDiscountId = '<commitment-discount-id>'
)
```

With this information, customers can analyze their existing *commitment discount* strategy to make more informed decisions on additional purchases.

**Important:** When aggregating Commitment Discount Quantity for utilization calculations, it's important to exclude either one-time or recurring *commitment discount* purchases (i.e. when *ChargeCategory* is *Purchase*) that are paid to cover future eligible charges (e.g., *Commitment Discount*). This exclusion helps prevent double counting of these charges in the aggregation.

The CommitmentDiscountQuantity column adheres to the following requirements:

* CommitmentDiscountQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
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

The amount of purchased, used, or unused *Commitment Discount Units* applied to a *commitment discount's* *row*.

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
