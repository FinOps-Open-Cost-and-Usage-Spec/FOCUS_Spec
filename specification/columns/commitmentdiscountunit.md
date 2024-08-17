# Commitment Discount Unit

Commitment Discount Unit is the string value representing the provider-specified measurement unit that corresponds to [CommitmentDiscountConsumedQuantity](#commitmentdiscountconsumedquantity) and [CommitmentDiscountPurchaseQuantity](#commitmentdiscountpurchasequantity).

CommitmentDiscountUnit MUST be present in the billing data when the provider supports [*commitment-based discounts*](#glossary:commitment-based-discount).

CommitmentDiscountUnit MUST not be null when [ChargeCategory](#chargecategory) is either *Purchase* or *Usage*, [PricingCategory](#pricingcategory) is *Committed*, and [CommitmentDiscountId](#commitmentdiscountid) is not null.

CommitmentDiscountUnit MUST be null in all other cases.

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The string value representing the provider-specified measurement unit that corresponds to CommitmentDiscountConsumedQuantity and CommitmentDiscountPurchaseQuantity.

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
