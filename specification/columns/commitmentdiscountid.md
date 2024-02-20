# Commitment Discount ID

A Commitment Discount ID is the identifier assigned to a [*commitment-based discount*](#glossary:commitment-based-discount) by the provider. Commitment Discount ID is commonly used for scenarios like chargeback for *commitments* and savings per *commitment-based discount*.

The CommitmentDiscountId column MUST be present in the billing data when the provider supports *commitment-based discounts*. This column MUST be of type String and MUST NOT contain null values when a charge is related to a *commitment-based discount*. When a charge is not associated with a *commitment-based discount*, the column MUST be null. CommitmentDiscountId MUST be unique within the provider.

## Column ID

CommitmentDiscountId

## Display name

Commitment Discount ID

## Description

The identifier assigned to a *commitment-based discount* by the provider.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| FOCUS Essential | False            |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
