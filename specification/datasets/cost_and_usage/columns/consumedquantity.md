# Consumed Quantity

The Consumed Quantity represents the volume of a metered SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used, based on the [Consumed Unit](#datasets.costandusage.consumedunit). Consumed Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#datasets.costandusage.pricingquantity) (complementary to [Pricing Unit](#datasets.costandusage.pricingunit)) and focuses on *resource* and *service* consumption, not pricing and cost.

## Requirements

ConsumedQuantity MUST adhere to the following requirements:

* ConsumedQuantity MUST be of type Decimal.
* ConsumedQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ConsumedQuantity MUST adhere to the following nullability requirements:
  * ConsumedQuantity MUST be null when [SkuPriceId](#datasets.costandusage.skupriceid) is null.
  * ConsumedQuantity MUST be null when [ChargeCategory](#datasets.costandusage.chargecategory) is not "Usage", or when ChargeCategory is "Usage" and [CommitmentDiscountStatus](#datasets.costandusage.commitmentdiscountstatus) is "Unused".
  * When ChargeCategory is "Usage" and CommitmentDiscountStatus is not "Unused", ConsumedQuantity MUST adhere to the following additional requirements:
    * ConsumedQuantity MUST NOT be null when [ChargeClass](#datasets.costandusage.chargeclass) is not "Correction".
    * ConsumedQuantity MAY be null when ChargeClass is "Correction".
* ConsumedQuantity MUST be a valid decimal value when not null.

## Column ID

ConsumedQuantity

## Display Name

Consumed Quantity

## Description

The volume of a metered SKU associated with a *resource* or *service* used, based on the Consumed Unit.

## Content constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

1.0
