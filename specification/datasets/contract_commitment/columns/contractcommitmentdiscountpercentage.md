# Contract Commitment Discount Percentage

Contract Commitment Discount Percentage represents the effective percentage reduction applied to the list price for resources or services covered by a [*contract commitment*](#glossary:contract-commitment).

## Implementation Context

### Calculating the Effective Percentage

In scenarios where a commitment has "stacked" or "nested" discounts, this field should reflect the total reduction from the list price.

Discount Percentage = 1 - (Contracted Unit Price / List Unit Price)

For example, consider usage that yields a cost for which the following discounts are applicable:

* Commitment discount: 20% applied to the on-demand cost
* Negotiated discount: 10% applied to the post-commitment discount cost

The effective discount is not 30%.
It is:
1 - (0.8 × 0.9) = 28%

In this scenario, ContractCommitmentDiscountPercentage should be reported as 28%.

### Relationship to Benefit Category

This field provides the magnitude for the **Discount** category. While `ContractCommitmentCost` tracks the financial obligation (what you pay), `ContractCommitmentDiscountPercentage` tracks the benefit rate (what you save).

### Tiered Incentives

For commitments with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), this column should represent the **active** or **base** discount percentage applicable to the current contract row.

## Requirements

ContractCommitmentDiscountPercentage adheres to the following requirements:

* ContractCommitmentDiscountPercentage MUST be of type Decimal.
* ContractCommitmentDiscountPercentage MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractCommitmentDiscountPercentage MUST NOT be null if [ContractCommitmentBenefitCategory](#datasets.contractcommitment.contractcommitmentbenefitcategory) is "Discount".
* ContractCommitmentDiscountPercentage MUST be null if ContractCommitmentBenefitCategory is "Credit" or "Availability".
* ContractCommitmentDiscountPercentage MUST be a value between 0.0 and 1.0.
* For contracts with multiple tiers (e.g., 5% discount up to 1M, 10% above 1M), ContractCommitmentDiscountPercentage MUST adhere to the following additional requirements:
  * ContractCommitmentDiscountPercentage MUST reflect the discount percentage defined for the specific pricing tier represented by the Contract Commitment row.
  * ContractCommitmentDiscountPercentage MUST correspond to only one pricing tier per Contract Commitment row.
* ContractCommitmentDiscountPercentage SHOULD represent the net effective discount if multiple contractual layers are applicable (e.g., a negotiated discount on top of a standard commitment).

## Column ID

ContractCommitmentDiscountPercentage

## Display Name

Contract Commitment Discount Percentage

## Description

The effective percentage reduction applied to the list price of resources or services covered by a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | True           |
| Data type       | Decimal        |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | 0.0 to 1.0                                           |

## Introduced (version)

1.4