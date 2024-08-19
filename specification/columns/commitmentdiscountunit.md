# Commitment Discount Unit

Commitment Discount Unit is the string value representing the provider-specified measurement unit that corresponds to [CommitmentDiscountConsumedQuantity](#commitmentdiscountconsumedquantity) and [CommitmentDiscountPurchaseQuantity](#commitmentdiscountpurchasequantity).

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in the billing data when the provider supports [*commitment-based discounts*](#glossary:commitment-based-discount).
* CommitmentDiscountUnit MUST be of type String, and the units of measure used in CommitmentDiscountUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.
* CommitmentDiscountUnit MUST NOT be null if [ChargeCategory](#chargecategory) is "Usage" or "Purchase", [*CommitmentDiscountId*](#commitmentdiscountid) is not null, and [ChargeClass](#chargeclass) is not "Correction".
* CommitmentDiscountUnit MAY be null if *ChargeCategory* is "Usage" or "Purchase" and *ChargeClass* is "Correction".
* CommitmentDiscountUnit MUST be null in all other cases.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The string value representing the provider-specified measurement unit that corresponds to *CommitmentDiscountConsumedQuantity* and *CommitmentDiscountPurchaseQuantity*.

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
