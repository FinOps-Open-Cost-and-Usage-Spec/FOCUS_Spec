# Commitment Discount Consumed Quantity

Commitment Discount Consumed Quantity is the total quantity of [Commitment Discount Units](#commitmentdiscountunit) amortized to either one or more metered [*resources*](#glossary:resource) or [*services*](#glossary:service) or that is unused over a [*charge period*](#glossary:chargeperiod) from one or more *commitment discount* purchases. The CommitmentDiscountConsumedQuantity column is only applicable to *commitment discounts* and not [*negotiated discounts*](#glossary:negotiated-discount).

The CommitmentDiscountConsumedQuantity column adheres to the following requirements:

* CommitmentDiscountConsumedQuantity MUST be present in the billing data when the provider supports *commitment discounts*.
* CommitmentDiscountConsumedQuantity MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat) requirements.
* CommitmentDiscountConsumedQuantity MUST be the positive, used quantity of a corresponding *commitment discount* by a metered *resource* or *service* over the charge period when [ChargeCategory](#chargecategory) is "Usage", [CommitmentDiscountStatus](#commitmentdiscountstatus) is "Used", and [ChargeClass](#chargeclass) is not "Correction".
* CommitmentDiscountConsumedQuantity MUST be the remaining, positive, unused quantity for the corresponding *commitment discount* over the charge period when *ChargeCategory* is "Usage", *CommitmentDiscountStatus* is "Unused", and *ChargeClass* is not "Correction".
* CommitmentDiscountConsumedQuantity MAY be negative, 0, or null if *ChargeClass* is "Correction".
* CommitmentDiscountConsumedQuantity MUST be null in all other cases.

## Column ID

CommitmentDiscountConsumedQuantity

## Display Name

Commitment Discount Consumed Quantity

## Description

The numeric, total quantity of Commitment Discount Units that is amortized to either a metered *resource* or *service* or that is unused over a *charge period* from one or more *commitment discount* purchases.

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
