# Commitment Utilization Unit

Commitment Utilization Unit is the string value representing the [Commitment Unit](#glossary:commitment-unit) unit type.

CommitmentUtilizationUnit MUST be present in the billing data when the provider supports *commitment-based discounts*.

A CommitmentUtilizationUnit value MUST be applied to a [*row*](#glossary:row) when:

* ChargeCategory is either *Purchase* or *Recurring*.
* PricingCategory is *Committed*.
* CommitmentDiscountStatus is not null.
* CommitmentDiscountId is not null.
* CommitmentUtilizationTotal is not null.
* CommitmentUtilizationUsed is not null.

In all other cases, CommitmentUtilizationUnit MUST be null.

## Column ID

CommitmentUtilizationUnit

## Display Name

Commitment Utilization Unit

## Description

The String value representing the [Commitment Unit](#glossary:commitment-unit) unit type.

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
| Spend      | Positive amount of spend pre-allocated and amortized over a billing period. |
| Hour       | Positive number of hours pre-allocated and amortized over a billing period. |

## Introduced (version)

1.1
