# Commitment Discount Type

Commitment Discount Type is a provider-assigned name to identify the type of [*commitment-based discount*](#glossary:commitment-based-discount) applied to the [*row*](#glossary:row).

The CommitmentDiscountType column MUST be present in the billing data when the provider supports *commitment-based discounts*. This column MUST be of type String, MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null, and MUST NOT be null when CommitmentDiscountId is not null. Providers MUST use a consistent value-format and a set of values for CommitmentDiscountType values within their billing datasets.

## Column ID

CommitmentDiscountType

## Display name

Commitment Discount Type

## Description

A provider-assigned identifier for the type of *commitment-based discount* applied to the *row*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| FOCUS Essential | False            |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0
