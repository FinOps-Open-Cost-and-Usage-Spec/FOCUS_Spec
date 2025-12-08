# Commitment Discount Unit

Commitment Discount Unit represents the service-provider-specified measurement unit indicating how a service provider measures the [Commitment Discount Quantity](#commitmentdiscountquantity) of a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

## Requirements

CommitmentDiscountUnit adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports *commitment discounts*.
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* CommitmentDiscountUnit nullability is defined as follows:
  * CommitmentDiscountUnit MUST be null when CommitmentDiscountQuantity is null.
  * CommitmentDiscountUnit MUST NOT be null when CommitmentDiscountQuantity is not null.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

See [Examples: Commitment Discount Flexibility](#commitmentdiscountflexibility) for more details around *commitment discount flexibility*.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The service-provider-specified measurement unit indicating how a service provider measures the Commitment Discount Quantity of a *commitment discount*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | [Unit Format](#unitformat)|

## Introduced (version)

1.1
