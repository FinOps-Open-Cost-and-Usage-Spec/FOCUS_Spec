# Commitment Name

A commitment-based discount is a contractual commitment to use a certain amount of a specific type of usage for a fixed term in exchange for a discounted unit price. Commitment-based discounts can cover either usage or cost of various resources such as virtual machines or databases. A provider can offer various pricing models, payment options, and term durations for commitment-based discounts.

A Commitment Name is the display name assigned to a commitment-based discount.

The CommitmentName column MUST be present in the billing data. This column must be of type String. The CommitmentName value MAY be null if a display name cannot be assigned to a commitment-based discount. CommitmentName MUST NOT be null if a display name can be assigned to a commitment-based discount.

## Column ID

CommitmentName

## Display name

Commitment Name

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
