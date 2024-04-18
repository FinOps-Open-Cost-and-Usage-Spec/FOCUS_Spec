# Commitment Discount Category

Commitment Discount Category indicates the category of a [*commitment-based discount*](#glossary:commitment-based-discount) purchase or the eligibility category of an on-demand or usage-based charges.

The CommitmentDiscountCategory column MUST be of type String and be present in the billing data when the provider supports commitment-based discounts.

CommitmentDiscountCategory MUST NOT be *Multiple* when a CommitmentDiscountId exists.

A CommitmentDiscountCategory value MUST be applied to a [*row*](#glossary:row) when [ChargeCategory](#chargecategory) is *Purchase*, or ChargeCategory is *Usage* and [ChargeSubCategory](#chargesubcategory) is *Used* or *Unused*.

A CommitmentDiscountCategory value MUST be applied to a row where the ChargeCategory is *Usage*, ChargeSubCategory is *On-Demand*, and the [SkuId](#skuid) is eligible for one or more commitments offered by the provider.

In all other cases, CommitmentDiscountCategory MUST be null.

## Column ID

CommitmentDiscountCategory

## Display Name

Commitment Discount Category

## Description

Indicates the category of a Commitment-Based Discount purchase or the eligibility category of an on-demand or usage-based charges

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | Allowed Values   |

Allowed values:

| Value    | Description                                                                                   |
|:---------|:----------------------------------------------------------------------------------------------|
| Spend    | Commitment-based discounts that require a predetermined amount of spend.                      |
| Usage    | Commitment-based discounts that require a predetermined amount of usage.                      |
| Multiple | On-demand usage charges that are eligible for both Spend and Usage commitment-based discounts |

## Introduced (version)

1.1
