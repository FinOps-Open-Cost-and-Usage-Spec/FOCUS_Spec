# Pricing Model

A commitment-based discount is a contractual commitment in exchange for a discounted unit price. These discounts may be available for spend-based commitments or resource-based commitments, depending on the Provider's offerings.

This column determines whether the commitment is based on a minimum spend or minimum usage.

The PricingModel column MUST be present in the billing data. This column must be of type String, MUST be null when CommitmentDiscountId is null, and MUST NOT be null when CommitmentDiscountId is not null.

The PricingModel MUST be one of the allowed values.

## Column ID

PricingModel

## Display name

Pricing Model

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
| Spend-Based    | Commitments are purchased and measured in terms of the dollars per hour of equivalent on-demand spend.                                                                    |
| Usage-Based | Commitments are purchased and measured in terms of the underlying resource usage.                                                                                              |

## Introduced (version)

1.0
