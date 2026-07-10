# Contracted Unit Price

Contracted Unit Price represents the agreed-upon unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contracts applicable to the charge, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program.

For SKUs with [threshold-based tiered pricing](#appendix.thresholdbasedtieredpricing), it reflects the applicable unit price per pricing tier, which may be based on quantity, duration, or spend within a defined aggregation scope and aggregation interval. Contracted Unit Price also reflects any customer-specific pricing tier configuration defined by the governing contracts applicable to the charge, where such configuration exists.

If no customer-specific pricing adjustments or pricing configurations unconditionally guaranteed by the governing contracts applicable to the charge exist, the Contracted Unit Price defaults to the [List Unit Price](#datasets.costandusage.listunitprice).

Contracted Unit Price is denominated in the [Billing Currency](#datasets.costandusage.billingcurrency). Contracted Unit Price is commonly used for calculating savings based on negotiation activities.

## Requirements

ContractedUnitPrice MUST adhere to the following requirements:

* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedUnitPrice MUST adhere to the following nullability requirements:
  * ContractedUnitPrice MUST be null when [SkuPriceId](#datasets.costandusage.skupriceid) is null.
  * ContractedUnitPrice MUST be null when [ChargeCategory](#datasets.costandusage.chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datasets.costandusage.chargeclass) is not "Correction".
  * ContractedUnitPrice MAY be null in all other cases.
* When ContractedUnitPrice is not null, ContractedUnitPrice MUST adhere to the following requirements:
  * ContractedUnitPrice MUST be a non-negative decimal value.
  * ContractedUnitPrice MUST be denominated in the BillingCurrency.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Column ID

ContractedUnitPrice

## Display Name

Contracted Unit Price

## Description

The agreed-upon unit price for a single Pricing Unit of the associated SKU, inclusive of all pricing adjustments unconditionally guaranteed by the governing contracts applicable to the charge, while excluding pricing adjustments contingent on the active status, activation, or remaining balance of a discount-bearing commitment program, reflecting the applicable unit price per pricing tier for SKUs with threshold-based tiered pricing.

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

1.0
