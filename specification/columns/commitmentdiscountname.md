# Commitment Discount Name

A Commitment Discount Name is the display name assigned to a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountName column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountName column adheres to the following requirements:

* CommitmentDiscountName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountName MUST be of type String.
* CommitmentDiscountName MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountName nullability is defined as follows:
  * CommitmentDiscountName MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * When CommitmentDiscountId is not null, CommitmentDiscountName adheres to the following additional requirements:
    * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

## Column ID

CommitmentDiscountName

## Display Name

Commitment Discount Name

## Description

The display name assigned to a *commitment discount*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
