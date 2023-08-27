# Commitment Name

A commitment is a contractual commitment to use a minimum amount of spending on resources for a fixed term in exchange for discounts on those resources. Commitments can cover various resources such as virtual machines, or databases. A provider can offer various pricing models, payment options, and term durations for its commitment offerings.

A Commitment ID is the identifier assigned to a commitment by the provider.

The CommitmentId column MUST be present in the billing data. This column must be of type String and MUST NOT contain null values. CommitmentId MUST be a globally unique identifier within a provider.

## Column ID

CommitmentName

## Display name

Commitment Name

## Description

The identifier assigned to a commitment by the provider.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
