# Contract Commitment Discount Percentage

[Contract Commitment Discount Percentage](#col) represents the effective percentage reduction applied to the list price for resources or services covered by a [contract commitment](#term).

## Requirements

[ContractCommitmentDiscountPercentage](#col) MUST adhere to the following requirements:

* [ContractCommitmentDiscountPercentage](#col) MUST be of type Decimal.
* [ContractCommitmentDiscountPercentage](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ContractCommitmentDiscountPercentage](#col) MUST adhere to the following nullability requirements:
  * [ContractCommitmentDiscountPercentage](#col) MUST NOT be null when [ContractCommitmentBenefitCategory](#col) is ["Discount"](#val:ContractCommitment.ContractCommitmentBenefitCategory).
  * [ContractCommitmentDiscountPercentage](#col) MUST be null when [ContractCommitmentBenefitCategory](#col) is ["Availability"](#val:ContractCommitment.ContractCommitmentBenefitCategory).
* [ContractCommitmentDiscountPercentage](#col) MUST be a value between 0.0 and 1.0, inclusive.
* For contracts with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), [ContractCommitmentDiscountPercentage](#col) MUST adhere to the following additional requirements:
  * [ContractCommitmentDiscountPercentage](#col) MUST reflect the discount percentage defined for the specific pricing tier represented by the [ContractCommitment](#ds) row.
  * [ContractCommitmentDiscountPercentage](#col) MUST correspond to only one pricing tier per ContractCommitment row.
* [ContractCommitmentDiscountPercentage](#col) SHOULD represent the net effective discount when multiple contractual layers are applicable (e.g., a negotiated discount on top of a standard commitment).

## Implementation Guidance

### Calculating the Effective Percentage

In scenarios where a commitment has "stacked" or "nested" discounts, this field should reflect the total reduction from the list price.

Discount Percentage = 1 - (Contracted Unit Price / List Unit Price)

For example, consider usage that yields a cost for which the following discounts are applicable:

* Commitment discount: 20% applied to the on-demand cost
* Negotiated discount: 10% applied to the post-commitment discount cost

The effective discount is not 30%.
It is:
1 - (0.8 × 0.9) = 28%

In this scenario, [ContractCommitmentDiscountPercentage](#col) should be reported as 28%.

### Relationship to Benefit Category

This field provides the magnitude for the **Discount** category. While `ContractCommitmentCost` tracks the financial obligation (what you pay), `ContractCommitmentDiscountPercentage` tracks the benefit rate (what you save).

### Tiered Incentives

For commitments with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), this column should represent the **active** or **base** discount percentage applicable to the current contract row.

## Column ID

ContractCommitmentDiscountPercentage

## Display Name

Contract Commitment Discount Percentage

## Description

The effective percentage reduction applied to the list price of resources or services covered by a [contract commitment](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Metric                                               |
| Feature level              | Mandatory                                            |
| Allows nulls               | True                                                 |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attr)                              |
| Number range               | 0.0 to 1.0 (inclusive)                               |

## Version Introduced

1.4
