# Contract Commitment Discount Percentage

Contract Commitment Discount Percentage represents the effective percentage reduction applied to the list price for resources or services covered by a [*contract commitment*](#glossary:contract-commitment).

## Implementation Context

### Calculating the Effective Percentage
In scenarios where a commitment has "stacked" or "nested" discounts, this field should reflect the total reduction from the list price.

Discount Percentage = 1 - (Contracted Unit Price / List Unit Price)

### Relationship to Benefit Category
This field provides the magnitude for the **Discount** category. While `ContractCommitmentCost` tracks the financial obligation (what you pay), `ContractCommitmentDiscountPercentage` tracks the benefit rate (what you save).

### Tiered Incentives
For commitments with multiple tiers (e.g., 5% discount up to $1M, 10% above $1M), this column should represent the **active** or **base** discount percentage applicable to the current contract row.

## Requirements

ContractCommitmentDiscountPercentage adheres to the following requirements:

* ContractCommitmentDiscountPercentage MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentDiscountPercentage MUST be of type Decimal.
* ContractCommitmentDiscountPercentage MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractCommitmentDiscountPercentage MUST NOT be null if [ContractCommitmentBenefitCategory](#datasets.contractcommitment.contractcommitmentbenefitcategory) is "Discount".
* ContractCommitmentDiscountPercentage MUST be null if ContractCommitmentBenefitCategory is "Credit" or "Availability Guarantee" and no secondary discount is applied.
* ContractCommitmentDiscountPercentage MUST be a value between 0.0 and 1.0.
* For contracts with multiple tiers (e.g., 5% discount up to $1M, 10% above $1M), ContractCommitmentDiscountPercentage MUST represent the discount percentage applicable to the current contract commitment.
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
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | True           |
| Data type       | Decimal        |
| Value format    | 0.0 to 1.0     |

## Introduced (version)

1.4