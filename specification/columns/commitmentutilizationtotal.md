# Commitment Utilization Total

Commitment Utilization Total is the numeric value representing the number of [Commitment Units](#glossary:commitment-unit) eligible for a resource or service.

CommitmentUtilizationTotal MUST be present in the billing data when the provider supports *commitment-based discounts*.

When a commitment-based discount is allocated to a [Charge Period](#glossary:chargeperiod) granuarlity, a CommitmentUtilizationTotal value MUST be the total amount of commitment units eligible for a charge period. Cloud-based commitment-based discounts like Reservations and Savings Plans are allocated to each charge period of a corresponding billing period.

When a commitment-based is *not* allocated to specific charge periods but over an entire billing period, a CommitmentUtilizationTotal value MUST be the constant amount of commitment units for the entire billing period.  For example, SaaS-based commitments typically apply to an entire billing period and not a corresponding charge periods.

CommitmentUtilizationTotal MUST be greater than or equal to its corresponding [*CommitmentUtilizationUsed*](#commitment-utilization-used) value.

A positive CommitmentUtilizationTotal value MUST be applied to a [*row*](#glossary:row) when:

* ChargeCategory is *Usage*.
* ChargeSubCategory is *UsedCommitment* or *UnusedCommitment*.
* ResourceId is not null.
* CommitmentDiscountId is not null.
* CommitmentUtilizationUsed is not null.
* CommitmentUtilizationUnit is not null.

In all other cases, CommitmentUtilizationTotal MUST be null.

The unit for the CommitmentUtilizationTotal is described by the CommitmentUtilizationUnit column. For example, when the commitment utilization unit is *Spend*, CommitmentUtilizationTotal must be provided in the currency denoted by the [BillingCurrency](#glossary:billing-currency) column.

The ratio of CommitmentUtilizationUsed over CommitmentUtilizedTotal produces the utilization rate for a given commitment-based discount or aggregate of.

## Column ID

CommitmentUtilizationTotal

## Display Name

Commitment Utilization Total

## Description

The numeric value representing the aggregate commitment units eligible for an eligible resource or service.

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
