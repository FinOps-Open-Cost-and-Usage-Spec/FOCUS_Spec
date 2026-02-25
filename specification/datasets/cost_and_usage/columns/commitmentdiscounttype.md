# Commitment Discount Type

Commitment Discount Type is a service-provider-assigned name to identify the type of [*commitment discount*](#glossary:commitment-discount) applied to the [*row*](#glossary:row). The CommitmentDiscountType column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

## Requirements

CommitmentDiscountType adheres to the following requirements:

* CommitmentDiscountType MUST be of type String.
* CommitmentDiscountType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentDiscountType nullability is defined as follows:
  * CommitmentDiscountType MUST be null when [CommitmentDiscountId](#datasets.costandusage.commitmentdiscountid) is null.
  * CommitmentDiscountType MUST NOT be null when CommitmentDiscountId is not null.

## Column ID

CommitmentDiscountType

## Display Name

Commitment Discount Type

## Description

A service-provider-assigned identifier for the type of *commitment discount* applied to the *row*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Introduced (version)

1.0-preview
