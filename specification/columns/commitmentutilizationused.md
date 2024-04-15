# Commitment Utilization Used

Commitment Utilization Used is a numeric value representing the unit amount of a purchased [*commitment-based discount*](#glossary:commitment-based-discount) applied or not applied to a resource during a billing period.  The ratio of CommitmentUtilizationUsed over [*CommitmentUtilizationTotal*](#commitment-utilization-total) produces the utilization rate for a given commitment-based discount or aggregate of.

CommitmentUtilizationTotal column MUST be present in the billing data when the provider supports *commitment-based discounts*.

A positive CommitmentUtilizationUsed value MUST be applied to a [*row*](#glossary:row) when:

* ChargeCategory is *Usage*
* ChargeSubCategory is *UsedCommitment* or *UnusedCommitment*.
* ResourceId is not null.
* CommitmentDiscountId is not null.
* CommitmentUtilizationTotal is not null.
* CommitmentUtilizationUnit is not null.

When the corresponding CommitmentUtilizationUnit is *Spend*, the CommitmentUtilizationTotal value describes a monetary amount matching the associated [BillingCurrency](#billing-currency).

When the ChargeSubCategory is *UsedCommitment*, a CommitmentUtilizationUsed value MUST be contain the remaining unit value for a specific [*commitment-based discount*](#glossary:commitment-based-discount) *after* factoring in the commitment discount for a given row.

When the ChargeSubCategory is *UnusedCommitment*, a CommitmentUtilizationUsed value MUST be contain an unchanged unit value for a specific [*commitment-based discount*](#glossary:commitment-based-discount).

Otherwise, CommitmentUtilizationUsed MUST be null.

## Column ID

CommitmentUtilizationUsed

## Display Name

Commitment Utilization Used

## Description

A numeric value representing the consumed unit amount of a purchased [*commitment-based discount*](#glossary:commitment-based-discount) for a billing period.

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
