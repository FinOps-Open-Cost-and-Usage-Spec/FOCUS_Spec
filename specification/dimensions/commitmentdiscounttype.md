# Commitment Discount Type

A commitment-based discount is a contractual commitment in exchange for a discounted unit price. Commitment discounts are available as spend-based or resource-based discounts, depending on the Provider's offering.

This column determines whether the commitment is based on a minimum spend or minimum usage.

The CommitmentDiscountType column MUST be present in the billing data. This column must be of type String and MUST NOT contain null values when a charge IS related to a commitment-based discount. When a charge IS NOT associated with a commitment-based discount, the column MUST be null. The CommitmentDiscountType MUST be one of the allowed values.

## Column ID

CommitmentDiscountType

## Display name

Commitment Discount Type

## Description

The type of commitment agreed to in exchange for the discounted unit price.

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
| Spend-based    | Commitments are purchased and measured in terms of the dollars per hour of equivalent on-demand spend.                                                                    |
| Resource-based | Commitments are purchased and measured in terms of the underlying resources.                                                                                              |

## Introduced (version)

1.0
