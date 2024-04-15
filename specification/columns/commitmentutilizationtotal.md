# Commitment Utilization Total

Commitment Utilization Total is a numeric value representing the aggregate unit amount of a purchased [*commitment-based discount*](#glossary:commitment-based-discount) for a billing period.  A CommitmentUtilizationTotal value MUST remain a constant value for a specific [*commitment-based discount*](#glossary:commitment-based-discount) within a billing period. The ratio of [*CommitmentUtilizationUsed*](#commitment-utilization-used) over CommitmentUtilizedTotal produces the utilization rate for a given commitment-based discount or aggregate of.

CommitmentUtilizationTotal column MUST be present in the billing data when the provider supports *commitment-based discounts*.

A positive CommitmentUtilizationTotal value MUST be applied to a [*row*](#glossary:row) when:

* ChargeCategory is *Usage*.
* ChargeSubCategory is *UsedCommitment* or *UnusedCommitment*.
* ResourceId is not null.
* CommitmentDiscountId is not null.
* CommitmentUtilizationUsed is not null.
* CommitmentUtilizationUnit is not null.

When the corresponding CommitmentUtilizationUnit is *Spend*, the CommitmentUtilizationTotal value describes a monetary amount matching the associated BillingCurrency.

Otherwise, CommitmentUtilizationUsed MUST be null.

## Column ID

CommitmentUtilizationTotal

## Display Name

Commitment Utilization Total

## Description

A numeric value representing the aggregate unit amount of a purchased [*commitment-based discount*](#glossary:commitment-based-discount) for a billing period.

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
