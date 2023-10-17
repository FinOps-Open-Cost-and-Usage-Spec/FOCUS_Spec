# Pricing Model

Pricing Model indicates the type of unit price applied to a charge at the time it was used or purchased. Pricing Model is commonly used to differentiate between charges at on-demand vs. reduced prices when investigating optimization opportunities, like for commitment-based discount coverage.

The PricingModel column MUST be present and MUST NOT be null or empty. This column is of type String and MUST be one of the allowed values. PricingModel MUST be "Commitment-Based Discount" when CommitmentDiscountId is not null. PricingModel MUST be "Dynamic" when pricing is determined by the provider and may change over time, regardless of predetermined agreement pricing.

## Column ID

PricingModel

## Display name

Pricing Model

## Description

Type of unit price applied to a charge at the time it was used or purchased.

## Content constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column required | True             |
| Data type       | String           |
| Allows nulls    | False             |
| Value format    | list-of-values   |

Allowed values:

| Value                     | Description                                                                                                                                                                                                  |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed                     | Charges priced at a constant rate, regardless of quantity used or purchased.                                                                                                                                 |
| On-Demand                 | Charges priced at the standard rate for the billing account. This includes any applicable negotiated discounts and volume/tiered pricing, but does not include dynamic or commitment-based discount pricing. |
| Dynamic                   | Charges priced at a variable rate determined by the provider. This includes any product or service with a unit price the provider can change without notice, like interruptible or low priority resources.   |
| Commitment-Based Discount | Charges with reduced prices due to a commitment-based discount specified by the Commitment Discount ID.                                                                                                      |

## Introduced (version)

1.0
