# Commitment ID

A commitment-based discount is a contractual commitment to use a certain amount of a specific type of usage for a fixed term in exchange for a discounted unit price. Commitment-based discounts can cover either usage or cost of various resources such as virtual machines or databases. A provider can offer various pricing models, payment options, and term durations for commitment-based discounts.

A Commitment ID is the identifier assigned to a commitment-based discount by the provider.

The CommitmentId column MUST be present in the billing data. This column must be of type String and MUST NOT contain null values. CommitmentId MUST be a globally unique identifier within a provider.

## Column ID

CommitmentId

## Display name

Commitment ID

## Description

The identifier assigned to a commitment by the provider.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | String          |
| Allows nulls    | False            |
| Value format    | \<not specified> |

## Introduced (version)

1.0
