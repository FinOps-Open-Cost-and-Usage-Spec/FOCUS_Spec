# Commitment Discount Unit

Commitment Discount Unit represents the provider-specified measurement unit indicating how a provider measures the [Commitment Discount Quantity](#commitmentdiscountquantity) of a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider supports *commitment discounts*.
* CommitmentDiscountUnit MUST be of type String.
* CommitmentDiscountUnit MUST conform to [StringHandling](#stringhandling) requirements.
* CommitmentDiscountUnit SHOULD conform to [UnitFormat](#unitformat) requirements.
* CommitmentDiscountUnit nullability is defined as follows:
  * When ChargeCategory is "Usage" or "Purchase" and [CommitmentDiscountId](#commitmentdiscountid) is not null, CommitmentDiscountUnit adheres to the following additional requirements:
    * CommitmentDiscountUnit MUST NOT be null when [ChargeClass](#chargeclass) is not "Correction".
    * CommitmentDiscountUnit MAY be null when ChargeClass is "Correction".
  * CommitmentDiscountUnit MUST be null in all other cases.
* When CommitmentDiscountUnit is not null, CommitmentDiscountUnit adheres to the following additional requirements:
  * CommitmentDiscountUnit MUST remain consistent over time for a given CommitmentDiscountId.
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for [*commitment discount flexibility*](#glossary:commitment-discount-flexibility), the CommitmentDiscountUnit value SHOULD reflect this consideration.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The provider-specified measurement unit indicating how a provider measures the Commitment Discount Quantity of a *commitment discount*.

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
