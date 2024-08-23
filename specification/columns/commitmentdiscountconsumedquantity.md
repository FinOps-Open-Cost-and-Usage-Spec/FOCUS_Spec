# Commitment Discount Consumed Quantity

Commitment Discount Consumed Quantity relates to [*commitment discounts*](#glossary:commitment-discount), not to be confused with [*negotiated discounts*](#glossary:negotiated-discount), and is the numeric value of [CommitmentDiscountUnits](#commitmentdiscountunit) that is either applied to a metered [*resource*](#glossary:resource) or [*service*](#glossary:service) or is unused over a [*charge period*](#glossary:chargeperiod).

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

The numeric value of CommitmentDiscountUnits that is either applied to a metered *resource* or *service* or is unused over a *charge period*.

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
