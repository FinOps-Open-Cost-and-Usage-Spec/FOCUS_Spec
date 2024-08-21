# Commitment Discount Unit

Commitment Discount Unit relates to [*commitment-based discounts*](#glossary:commitment-based-discount), not to be confused with [*negotiated discounts*](#glossary:negotiated-discount), and is the string value representing the provider-specified measurement unit that corresponds to [CommitmentDiscountQuantity](#commitmentdiscountconsumedquantity) and [CommitmentDiscountPurchaseQuantity](#commitmentdiscountpurchasequantity).

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in the billing data when the provider supports [*commitment-based discounts*](#glossary:commitment-based-discount).
* CommitmentDiscountUnit MUST be of type String, and the units of measure used in CommitmentDiscountUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.
* CommitmentDiscountUnit MUST NOT be null when [*CommitmentDiscountId*](#commitmentdiscountid) is NOT null and *ChargeClass* is not "Correction".
* CommitmentDiscountUnit MUST be null in all other cases.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The string value representing the provider-specified measurement unit that corresponds to *CommitmentDiscountQuantity* and *CommitmentDiscountPurchaseQuantity*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | [Unit Format](#unitformat) recommended |

## Introduced (version)

1.1
