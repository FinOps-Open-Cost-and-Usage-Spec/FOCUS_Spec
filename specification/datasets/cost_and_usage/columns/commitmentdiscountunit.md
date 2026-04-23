# Commitment Discount Unit

Commitment Discount Unit represents the service-provider-specified measurement unit indicating how a service provider measures the [Commitment Discount Quantity](#datasets.costandusage.commitmentdiscountquantity) of a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

## Requirements

CommitmentDiscountUnit MUST adhere to the following requirements:

* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CommitmentDiscountUnit SHOULD conform to [UnitFormat](#attributes.unitformat) requirements.
* CommitmentDiscountUnit MUST adhere to the following nullability requirements:
  * CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  * CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit MUST adhere to the following requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

See [Examples: Commitment Discount Flexibility](#appendix.examples:commitmentdiscountflexibility) for more details around *commitment discount flexibility*.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The service-provider-specified measurement unit indicating how a service provider measures the Commitment Discount Quantity of a *commitment discount*.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | [Unit Format](#attributes.unitformat)                |

## Version Introduced

1.1
