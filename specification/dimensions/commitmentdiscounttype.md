# Commitment Discount Type

A commitment-based discount is a commitment for an amount of usage or spend throughout a specified term, in exchange for discounted unit pricing on that amount. The commitment may be based on quantities of resource units or monetary value, with various payment options and time frames.

Commitment Discount Type is a provider-assigned name to identify the type of commitment-based discount applied to this record. For example, GCP might refer to a "Committed Use Discount" (CUD) while Azure might call their offering a "Reservation" or "Reserved Instance".

The CommitmentDiscountType column MUST be present in the billing data. This column MUST be of type String, MUST be null when CommitmentDiscountId is null, and MUST NOT be null when CommitmentDiscountId is not null. Providers MUST use a consistent value-format and a set of values for CommitmentDiscountType values within their cost and usage datasets.

## Column ID

CommitmentDiscountType

## Display name

Commitment Discount Type

## Description

A provider-assigned identifier for the type of commitment-based discount applied to this record.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column required | False            |
| Data type       | String           |
| Allows nulls    | True             |
| Value format    | \<not specified> |

## Introduced (version)

1.0
