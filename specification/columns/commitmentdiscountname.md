# Commitment Discount Name

A Commitment Discount Name is the display name assigned to a [*commitment-based discount*](#glossary:commitment-based-discount).

The CommitmentDiscountName column MUST be present in the billing data when the provider supports *commitment-based discounts*. This column MUST be of type String. The CommitmentDiscountName value MUST be null if the charge is not related to a *commitment-based discount* and MAY be null if a display name cannot be assigned to a *commitment-based discount*. CommitmentDiscountName MUST NOT be null if a display name can be assigned to a *commitment-based discount*.

## Column ID

CommitmentDiscountName

## Display name

Commitment Discount Name

## Description

The display name assigned to a *commitment-based discount*.

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
