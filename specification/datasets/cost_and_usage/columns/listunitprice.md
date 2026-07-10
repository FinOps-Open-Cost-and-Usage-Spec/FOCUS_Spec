# List Unit Price

List Unit Price represents the suggested service-provider-defined unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated [*SKU*](#glossary:sku), exclusive of any discounts.

For *SKUs* with [threshold-based tiered pricing](#appendix.thresholdbasedtieredpricing), it reflects the applicable unit price per pricing tier, which may be based on quantity, duration, or spend within a defined aggregation scope and aggregation interval.

List Unit Price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## Requirements

ListUnitPrice MUST adhere to the following requirements:

* ListUnitPrice MUST be of type Decimal.
* ListUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ListUnitPrice MUST adhere to the following nullability requirements:
  * ListUnitPrice MUST be null when [SkuPriceId](#datasets.costandusage.skupriceid) is null.
  * ListUnitPrice MUST be null when [ChargeCategory](#datasets.costandusage.chargecategory) is "Tax".
  * ListUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datasets.costandusage.chargeclass) is not "Correction".
  * ListUnitPrice MAY be null in all other cases.
* When ListUnitPrice is not null, ListUnitPrice MUST adhere to the following requirements:
  * ListUnitPrice MUST be a non-negative decimal value.
  * ListUnitPrice MUST be denominated in the BillingCurrency.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ListUnitPrice

## Display Name

List Unit Price

## Description

The suggested service-provider-defined unit price for a single Pricing Unit of the associated *SKU*, exclusive of any discounts, reflecting the applicable unit price per pricing tier for *SKUs* with threshold-based tiered pricing.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid non-negative decimal value                 |

## Version Introduced

1.0-preview
