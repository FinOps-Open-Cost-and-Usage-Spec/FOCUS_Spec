# Commitment Discount Name

A commitment-based discount is a contractual commitment for an amount of usage or spend throughout a specified term, in exchange for discounted unit pricing on that amount. The commitment may be based on quantities of resource units or monetary value, with various payment options and time frames.

A Commitment Discount Name is the display name assigned to a commitment-based discount.

The CommitmentDiscountName column MUST be present in the billing data. This column must be of type String. The CommitmentDiscountName value MUST be null if the charge is not related to a commitment-based discount and MAY be null if a display name cannot be assigned to a commitment-based discount. CommitmentDiscountName MUST NOT be null if a display name can be assigned to a commitment-based discount.

## Column ID

CommitmentDiscountName

## Display name

Commitment Discount Name

## Description

The display name assigned to a commitment-based discount.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
