# Commitment Discount Consumed Quantity

Commitment Discount Consumed Quantity is the metered quantity of [Commitment Discount Units](#commitmentdiscountunit) consumed by a row covered by a [*commitment discount*](#glossary:commitmentdiscount) or the unused portion of a *commitment discount* over a [*charge period*](#glossary:chargeperiod). The CommitmentDiscountConsumedQuantity column only applies to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

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

The quantity of Commitment Discount Units that represents the amount that was committed to by a *commitment discount* over the specified *charge period*.

## Content constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Conditional      |
| Allows nulls    | True             |
| Data type       | Decimal          |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.1
