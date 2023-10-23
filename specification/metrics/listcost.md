# List Cost

The List Cost represents a charge inclusive of the impacts of volume/tier-based rates while excluding any negotiated or commitment-based discounts. This cost is denominated in the [Billing Currency](#billingcurrency). The List Cost equals the [BilledCost](#billedcost) if there are no negotiated or commitment-based discounts against the resource and/or service. By comparing it with [EffectiveCost](#effectivecost) you can calculate savings based on rate optimization activities.

The ListCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal and MUST NOT contain null values. When a [ListUnitPrice](#listunitprice) is not null, multiplying the [ListUnitPrice](#listunitprice) by [QuantityInPricingUnit](#quantityinpricingunit ) MUST produce the ListCost. In cases where the [ListUnitPrice](#listunitprice) is null, the following applies:

- If the line item is based on other charges (e.g. [ChargeType](#chargetype) is ‘Tax’), the ListCost MUST be calculated based on ListCost of the related charges
- If the line item is unrelated to other charges (e.g. [AdjustmentType](#adjustmenttype) is ‘Credit’), the ListCost MUST match the [BilledCost](#billedcost).

## Column ID

ListCost

## Display name

List Cost

## Description

A charge inclusive of the impacts of volume/tier-based rates while excluding any negotiated or commitment-based discounts.

## Content Constraints

| Constraint      | Value                   |
|:----------------|:------------------------|
| Column required | True                    |
| Data type       | Decimal                 |
| Allows nulls    | False                   |
| Value format    | Numeric value           |
| Number range    | Any valid decimal value |

## Introduced (version)

1.0
