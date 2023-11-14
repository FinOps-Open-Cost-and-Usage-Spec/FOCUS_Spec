# Commitment Discount ID

A commitment-based discount is a commitment for an amount of usage or spend throughout a specified term, in exchange for discounted unit pricing on that amount. The commitment may be based on quantities of resource units or monetary value, with various payment options and time frames.

A Commitment Discount ID is the identifier assigned to a commitment-based discount by the provider. Commitment Discount ID is commonly used for scenarios like chargeback for commitments and savings per commitment-based discount.

The CommitmentDiscountId column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values when a charge is related to a commitment-based discount. When a charge is not associated with a commitment-based discount, the column MUST be null. CommitmentDiscountId MUST be unique within the provider.

## Column ID

CommitmentDiscountId

## Display name

Commitment Discount ID

## Description

The identifier assigned to a commitment-based discount by the provider.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Column required | True             |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
