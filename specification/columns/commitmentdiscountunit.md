# Commitment Discount Unit

Commitment Discount Unit is the string value representing the provider-specified measurement unit that corresponds to [Commitment Discount Quantity](#commitmentdiscountquantity) of a [*commitment discount*](#glossary:commitment-discount). The CommitmentDiscountUnit column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountUnit column adheres to the following requirements:

* CommitmentDiscountUnit MUST be present in the billing data when the provider supports [*commitment discounts*](#glossary:commitment-discount).
* CommitmentDiscountUnit MUST be of type String, and the units of measure used in CommitmentDiscountUnit SHOULD adhere to the values and format requirements specified in the [UnitFormat](#unitformat) attribute.
* The CommitmentDiscountUnit MUST be the same across all *rows* where *CommitmentDiscountQuantity* has the same [*CommitmentDiscountId*](#commitmentdiscountid).
* CommitmentDiscountUnit MUST NOT be null when *CommitmentDiscountId* is not null.
* CommitmentDiscountUnit MUST be null in all other cases.

In cases where the *CommitmentDiscountQuantity* are present, the following applies:

* When the *commitment discount* commits to a usage amount over a term, the CommitmentDiscountUnit SHOULD be "Hours".
* When the *commitment discount* commits to a usage amount over a term where size-flexibility is applied, the CommitmentDiscountUnit SHOULD be "Normalized Hours".
* When the *commitment discount* commits to a spend amount over a term, the CommitmentDiscountUnit SHOULD match the [*BillingCurrency*](#billingcurrency).

## Column ID

CommitmentDiscountUnit

## Display Name

Commitment Discount Unit

## Description

The string value representing the provider-specified measurement unit that corresponds to *CommitmentDiscountQuantity* and *CommitmentDiscountPurchasedQuantity* of a *commitment discount*.

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
