# Commitment Discount Unit

Commitment Discount Unit represents the provider-specified measurement unit indicating how a provider measures the [Commitment Discount Quantity](#commitmentdiscountquantity) of a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in a FOCUS dataset when the provider supports [*commitment discounts*](#glossary:commitment-discount).
* CommitmentDiscountUnit MUST be of type String.
* Units of measure used in CommitmentDiscountUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.
* If *CommitmentDiscountId* is not null and [ChargeCategory](#chargecategory) is "Usage" or "Purchase", the following applies:
  * CommitmentDiscountUnit MUST NOT be null when [*ChargeClass*](#chargeclass) is not "Correction".
  * CommitmentDiscountUnit MAY be null when *ChargeClass* is "Correction".
* CommitmentDiscountUnit MUST be null in all other cases.
* In cases where the CommitmentDiscountUnit is not null, the following applies:
  * CommitmentDiscountUnit MUST be the same across all *rows* having the same [*CommitmentDiscountId*](#commitmentdiscountid).
  * CommitmentDiscountUnit MUST represent the unit used to measure the *commitment discount*.
  * When accounting for *commitment flexibility*, the CommitmentDiscountUnit value SHOULD reflect this consideration.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The provider-specified measurement unit indicating how a provider measures the *Commitment Discount Quantity* of a *commitment discount*.

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
