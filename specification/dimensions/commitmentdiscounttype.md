# Commitment Discount Type

A commitment-based discount is a contractual commitment for an amount of usage or spend throughout a specified term, in exchange for discounted unit pricing on that amount. The commitment may be based on quantities of resource units or monetary value, with various payment options and time frames.

Commitment Discount Type indicates whether the commitment-based discount identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

The CommitmentDiscountType column MUST be present in the billing data. This column MUST be of type String, MUST be null when CommitmentDiscountId is null, and MUST NOT be null when CommitmentDiscountId is not null. The CommitmentDiscountType MUST be one of the allowed values.

## Column ID

CommitmentDiscountType

## Display name

Commitment Discount Type

## Description

Indicates whether the commitment-based discount identified in the CommitmentDiscountId column is based on usage quantity or cost (aka "spend").

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | List of values   |

Allowed values:

| Value      | Description                                                                                                                                                                   |
|:---------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Spend-Based   | Commitment-based discounts that require a predetermined amount of spend.    |
	| Usage-Based   | Commitment-based discounts that require a predetermined amount of usage.     |

## Introduced (version)

1.0
