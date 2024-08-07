# Commitment Consumed Unit

Commitment Consumed Unit is the string value representing the provider-specified measurement unit that corresponds to [CommitmentConsumedQuantity](#commitmentconsumedquantity) and [CommitmentTotalQuantity](#commitmenttotalquantity).

CommitmentConsumedUnit MUST be present in the billing data when the provider supports [*commitment-based discounts*](#glossary:commitment-based-discount).

CommitmentConsumedUnit MUST not be null when [ChargeCategory](#chargecategory) is either *Purchase* or *Usage*, [PricingCategory](#pricingcategory) is *Committed*, and [CommitmentDiscountId](#commitmentdiscountid) is not null.

CommitmentConsumedUnit MUST be null in all other cases.

## Column ID

CommitmentConsumedUnit

## Display Name

Commitment Consumed Unit

## Description

The string value representing the provider-specified measurement unit that corresponds to CommitmentConsumedQuantity and CommitmentTotalQuantity.

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
