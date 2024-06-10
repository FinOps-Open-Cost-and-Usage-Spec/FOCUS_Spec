# Commitment Utilization Used

Commitment Utilization Used is the numeric value representing the number of unnormalized [Commitment Units](#glossary:commitment-unit) applied to a resource or service.

Cloud-based commitment-based discounts, like Reservations and Savings Plans, are commonly allocated to fixed, hourly [Charge Period](#glossary:chargeperiod) of a [Billing Period](#glossary:billingperiod). When a commitment-based discount is amortized to a fixed charge period, the CommitmentUtilizationUsed value MUST be the total amount of commitment units amortized for that charge period.

CommitmentUtilizationUsed MUST be present in the billing data when the provider supports *commitment-based discounts*.
CommitmentUtilizationUsed MUST be less than or equal to its corresponding [*CommitmentUtilizationTotal*](#commitment-utilization-total) value.

A zero-value CommitmentUtilizationUsed value MUST be applied to a [*row*](#glossary:row) when a Commitment *Purchase* row exists:

* ChargeCategory is *Purchase*.
* ChargeFrequency is *One-Time*.
* PricingCategory is *Committed*.
* CommitmentDiscountStatus is null.
* CommitmentDiscountId is not null.
* CommitmentUtilizationTotal is not null.
* CommitmentUtilizationUnit is not null.
* CommitmentDiscountType is not null.

A non-null CommitmentUtilizationUsed value MUST be applied to a [*row*](#glossary:row) when a *Recurring* Commitment row exists:

* ChargeCategory is *Recurring*.
* ChargeFrequency is *Recurring*.
* PricingCategory is *Committed*.
* CommitmentDiscountStatus is *Unused*.
* CommitmentDiscountId is not null.
* CommitmentUtilizationTotal is not null.
* CommitmentUtilizationUnit is not null.
* CommitmentDiscountType is not null.

The unit for the CommitmentUtilizationUsed is described by the CommitmentUtilizationUnit column. For example, when the commitment utilization unit is *Spend*, the CommitmentUtilizationUsed amount is the cost denoted by the [BillingCurrency](#glossary:billing-currency) column.

When the CommitmentDiscountStatus is *Unused* and a commitment is allotted over a granularity (i.e. hourly), a CommitmentUtilizationUsed value MUST contain the remaining, unused unit value for a specific Commitment-Based Discount](#glossary:commitment-based-discount).

In all other cases, CommitmentUtilizationUsed MUST be null.

The ratio of CommitmentUtilizationUsed over CommitmentUtilizedTotal produces the utilization rate for a given commitment-based discount or aggregate of.

## Column ID

CommitmentUtilizationUsed

## Display Name

Commitment Utilization Used

## Description

The numeric value representing the commitment units applied to an eligible resource or service.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Numeric          |
| Value format    | Any valid non-negative decimal value |

## Introduced (version)

1.1
