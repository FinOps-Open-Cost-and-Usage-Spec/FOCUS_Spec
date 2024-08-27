# Commitment Discount Consumed Quantity

Commitment Discount Consumed Quantity is the quantity of [Commitment Discount Units](#commitmentdiscountunit) that represents either a [*resource's*](#glossary:resource) consumption or complete unuse of a [*commitment discount*](#glossary:commitment-discount) over a [*row's*](#glossary:row) [*charge period*](#glossary:chargeperiod). The CommitmentDiscountConsumedQuantity column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountConsumedQuantity column adheres to the following requirements:

* CommitmentDiscountConsumedQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
* CommitmentDiscountConsumedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountConsumedQuantity MUST be the positive, metered quantity of the *commitment discount* that is allocated to a *resource* over the [*row's*](#glossary:row) [*charge period*](#glossary:chargeperiod) when [*ChargeCategory*](#chargecategory) is "Usage", [*CommitmentDiscountStatus*](#commitmentdiscountstatus) is "Used", and [*ChargeClass*](#chargeclass) is not "Correction".
* CommitmentDiscountConsumedQuantity MUST be the remaining, positive, unused quantity for the corresponding *commitment discount* over the *row's* *charge period* when *ChargeCategory* is "Usage", *CommitmentDiscountStatus* is "Unused", and *ChargeClass* is not "Correction".
* CommitmentDiscountConsumedQuantity MAY be negative, 0, or null if *ChargeClass* is "Correction".
* CommitmentDiscountConsumedQuantity MUST be null in all other cases.

## Column ID

CommitmentDiscountConsumedQuantity

## Display Name

Commitment Discount Consumed Quantity

## Description

The quantity of Commitment Discount Units that represents either a *resource's* consumption or complete unuse of a *commitment discount* over a *row's* *charge period*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Numeric          |
| Value format    | Any valid decimal value |

## Introduced (version)

1.1
