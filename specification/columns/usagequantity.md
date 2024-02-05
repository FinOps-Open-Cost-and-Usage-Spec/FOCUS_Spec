# Usage Quantity

The Usage Quantity represents the volume of a given SKU associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used, based on the [Usage Unit](#usageunit). Usage Quantity is often derived at a finer granularity or over a different time interval when compared to the [Pricing Quantity](#pricingquantity) (complementary to [Pricing Unit](#pricingunit)), and focuses on *resource* and *service* consumption, not pricing and cost.

UsageQuantity MUST be present in the billing data. This column MUST be of type Decimal and MUST conform to [Numeric Format](#numericformat). The value MAY be negative in cases where [ChargeSubcategory](#chargesubcategory) is "Refund".

This column MUST NOT be null under the following conditions:

* When [ChargeCategory](#chargecategory) is "Usage" and ChargeSubcategory is "On-Demand" or "Used Commitment".
* When ChargeCategory is "Adjustment" and ChargeSubcategory is "Refund", related to charges with a specific SkuPriceId.

This column MUST be null in case of any other ChargeCategory – ChargeSubcategory combinations.

## Column ID

UsageQuantity

## Display name

Usage Quantity

## Description

Volume of a given SKU associated with a *resource* or *service* used, based on the Usage Unit.

## Content constraints

| Constraint      | Value         |
|:----------------|:--------------|
| Column type     | Metric        |
| Column required | True          |
| Allows nulls    | True          |
| Data type       | Decimal       |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
