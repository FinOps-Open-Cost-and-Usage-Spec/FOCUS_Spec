# Commitment Utilization Unit

Commitment Utilization Unit is a String value representing the amortization unit of a [*commitment-based discount*](#glossary:commitment-based-discount) during a billing period.

CommitmentUtilizationUnit column MUST be present in the billing data when the provider supports *commitment-based discounts*.

A CommitmentUtilizationUnit value MUST be applied to a [*row*](#glossary:row) when:

* ChargeCategory is *Usage*.
* ChargeSubCategory is *UsedCommitment* or *UnusedCommitment*.
* ResourceId is not null.
* CommitmentDiscountId is not null.
* CommitmentUtilizationTotal is not null.
* CommitmentUtilizationUsed is not null.

CommitmentUtilizationUsed MUST be null for all other rows.

## Column ID

CommitmentUtilizationUnit

## Display Name

Commitment Utilization Unit

## Description

A String value representing the amortization unit of a purchased [*commitment-based discount*](#glossary:commitment-based-discount) for a billing period.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | Allowed values   |

Allowed values:

| Value      | Description                          |
| :--------- | :------------------------------------|
| Spend      | Positive amount of spend pre-allocated and amoritized over a billing period. |
| Hour       | Positive number of hours pre-allocated and amortized over a billing period.  |

## Introduced (version)

1.1
