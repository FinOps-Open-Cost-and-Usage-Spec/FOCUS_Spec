# Commitment Name

A commitment is a contractual commitment to use a minimum amount of spending on resources for a fixed term in exchange for discounts on those resources. Commitments can cover various resources such as virtual machines, or databases. A provider can offer various pricing models, payment options, and term durations for its commitment offerings.

A Commitment Name is the display name assigned to a commitment by the provider.

The CommitmentName column MUST be present in the billing data. This column must be of type String. The ResourceName value MAY be null if a display name cannot be assigned to a commitment. CommitmentName MUST NOT be null if a display name can be assigned to a commitment and MUST NOT duplicate the value of the CommitmentId.

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
