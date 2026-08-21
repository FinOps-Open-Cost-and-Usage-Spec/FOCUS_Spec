# Commitment Discount Category

Commitment Discount Category indicates whether the [*commitment discount*](#glossary:commitment-discount) a recommendation proposes to purchase is based on usage quantity or cost (aka "spend"). Commitment Discount Category provides a programmatically referenceable classification of a proposed [*contract commitment*](#glossary:contract-commitment), whereas [Contract Commitment Type](#datasets.recommendation.contractcommitmenttype) values differ across [*service providers*](#glossary:service-provider). Commitment Discount Category uses the same allowed values as [Commitment Discount Category](#datasets.costandusage.commitmentdiscountcategory) in the [Cost and Usage](#datasets.costandusage) dataset, which supports comparison of proposed commitment discounts against existing ones.

## Requirements

CommitmentDiscountCategory MUST adhere to the following requirements:

* CommitmentDiscountCategory MUST be of type String.
* CommitmentDiscountCategory MUST adhere to the following nullability requirements:
  * CommitmentDiscountCategory MUST NOT be null when a recommendation proposes the purchase of a *contract commitment*.
  * CommitmentDiscountCategory MUST be null when a recommendation does not propose the purchase of a *contract commitment*.
* CommitmentDiscountCategory MUST be one of the allowed values.

## Allowed Values

| Value   | Description                                                        |
|:--------|:-------------------------------------------------------------------|
| Spend   | Commitment discounts that require a predetermined amount of spend. |
| Usage   | Commitment discounts that require a predetermined amount of usage. |

## Column ID

CommitmentDiscountCategory

## Display Name

Commitment Discount Category

## Description

Indicates whether the *commitment discount* a recommendation proposes to purchase is based on usage quantity or cost (aka "spend").

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
