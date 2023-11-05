# List Cost

The List Cost represents a charge inclusive of the impacts of free-tier, volume/tier-based, BYOL-based and dynamically priced SKU rates, while excluding any other discounts or the amortization of upfront charges (one-time or recurring). It equals the [Billed Cost](#billedcost) if there are no negotiated nor commitment-based discounts against the resource and/or service. This cost is denominated in the [Billing Currency](#billingcurrency). It is used for calculating savings based on rate optimization activities, by comparing it with [Effective Cost](#effectivecost). In this context, activities such as increased consumption leading to lower volume/tier-based rates, the use of pre-owned software licenses (BYOL - Bring Your Own License), leveraging interruptible resources and/or services, or optimizing usage to take advantage of dynamic pricing models are not considered rate optimization activities.

The ListCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal and MUST NOT contain null values. When a [ListUnitPrice](#listunitprice) is not null, multiplying the ListUnitPrice by [QuantityInPricingUnit](#quantityinpricingunit ) MUST produce the ListCost. In cases where the ListUnitPrice is null, the following applies:

* If the line item is based on other charges (e.g. [ChargeType](#chargetype) is 'Tax'), the ListCost MUST be calculated based on ListCost of the related charges
* If the line item is unrelated to other charges (e.g. [AdjustmentType](#adjustmenttype) is 'Credit'), the ListCost MUST match the BilledCost.

## Column ID

ListCost

## Display name

List Cost

## Description

A charge inclusive of the impacts of free-tier, volume/tier-based, BYOL-based and dynamically priced SKU rates, while excluding any other discounts or the amortization of upfront charges (one-time or recurring).

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
