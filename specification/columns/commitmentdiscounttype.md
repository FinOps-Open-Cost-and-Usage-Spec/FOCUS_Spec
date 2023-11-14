# Commitment Discount Type

A commitment-based discount is a commitment for an amount of usage or spend throughout a specified term, in exchange for discounted unit pricing on that amount. The commitment may be based on quantities of resource units or monetary value, with various payment options, time frames, or additional usage charges.

Commitment Discount Type is a provider-assigned name to identify the type of commitment-based discount applied to the row.

The CommitmentDiscountType column MUST be present in the billing data. This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null. Providers MUST use a consistent value-format and a set of values for CommitmentDiscountType values within their billing datasets.

## Column ID

CommitmentDiscountType

## Display name

Commitment Discount Type

## Description

A provider-assigned identifier for the type of commitment-based discount applied to the row.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column Type     | Dimension        |
| Column required | False            |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
