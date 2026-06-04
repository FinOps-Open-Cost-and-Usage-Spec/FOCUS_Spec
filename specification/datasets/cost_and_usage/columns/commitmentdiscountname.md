# Commitment Discount Name

A Commitment Discount Name is the display name assigned to a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountName column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

## Requirements

CommitmentDiscountName MUST adhere to the following requirements:

* CommitmentDiscountName MUST be of type String.
* CommitmentDiscountName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentDiscountName MUST adhere to the following nullability requirements:
  * CommitmentDiscountName MUST be null when [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is null.
  * When CommitmentDiscountId is not null, CommitmentDiscountName MUST adhere to the following requirements:
    * CommitmentDiscountName MUST NOT be null when a display name can be assigned to a *commitment discount*.
    * CommitmentDiscountName MAY be null when a display name cannot be assigned to a *commitment discount*.

## Column ID

CommitmentDiscountName

## Display Name

Commitment Discount Name

## Description

The display name assigned to a *commitment discount*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.0-preview
