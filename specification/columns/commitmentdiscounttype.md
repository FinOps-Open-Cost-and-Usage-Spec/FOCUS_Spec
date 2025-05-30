# Commitment Discount Type

Commitment Discount Type is a provider-assigned name to identify the type of [*commitment discount*](#glossary:commitment-discount) applied to the [*row*](#glossary:row). The CommitmentDiscountType column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountType column adheres to the following requirements:

* CommitmentDiscountType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountType nullability is defined as follows:
  * CommitmentDiscountType MUST be null when [CommitmentDiscountId](#commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

## Column ID

CommitmentDiscountType

## Display Name

Commitment Discount Type

## Description

A provider-assigned identifier for the type of *commitment discount* applied to the *row*.

## Content Constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.0-preview
