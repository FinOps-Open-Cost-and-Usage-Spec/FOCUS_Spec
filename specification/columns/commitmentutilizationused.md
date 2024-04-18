# Commitment Utilization Used

Commitment Utilization Used is the numeric value representing the number of [Commitment Units](#glossary:commitment-unit) applied to a resource or service.

CommitmentUtilizationUsed MUST be present in the billing data when the provider supports *commitment-based discounts*.

CommitmentUtilizationUsed MUST be less than or equal to its corresponding [*CommitmentUtilizationTotal*](#commitment-utilization-total) value.

A positive CommitmentUtilizationUsed value MUST be applied to a [*row*](#glossary:row) when:

* ChargeCategory is *Usage*
* ChargeSubCategory is *UsedCommitment*.
* CommitmentDiscountId is not null.
* CommitmentUtilizationTotal is not null.
* CommitmentUtilizationUnit is not null.

The unit for the CommitmentUtilizationUsed is described by the CommitmentUtilizationUnit column. For example, when the commitment utilization unit is *Spend*, the CommitmentUtilizationUsed amount is the cost denoted by the [BillingCurrency](#glossary:billing-currency) column.

When the ChargeSubCategory is *UsedCommitment*, a CommitmentUtilizationUsed value MUST contain the remaining unit value for a specific Commitment-Based Discount](#glossary:commitment-based-discount) *after* factoring in the commitment discount for a given row.

When the ChargeSubCategory is *UnusedCommitment*, a CommitmentUtilizationUsed value MUST contain an unchanged unit value for a specific commitment-based discount.

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
