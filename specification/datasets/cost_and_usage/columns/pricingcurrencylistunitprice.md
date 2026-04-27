# Pricing Currency List Unit Price

The Pricing Currency List Unit Price represents the suggested service-provider-published unit price for a single [Pricing Unit](#datasets.costandusage.pricingunit) of the associated [*SKU*](#glossary:sku), exclusive of any discounts. This price is denominated in the [Pricing Currency](#datasets.costandusage.pricingcurrency). The Pricing Currency List Unit Price is commonly used for calculating savings based on various rate optimization activities.

## Requirements

PricingCurrencyListUnitPrice MUST adhere to the following requirements:

* PricingCurrencyListUnitPrice MUST be of type Decimal.
* PricingCurrencyListUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingCurrencyListUnitPrice MUST adhere to the following nullability requirements:
  * PricingCurrencyListUnitPrice MUST be null when [SkuPriceId](#datasets.costandusage.skupriceid) is null.
  * PricingCurrencyListUnitPrice MUST be null when [ChargeCategory](#datasets.costandusage.chargecategory) is "Tax".
  * PricingCurrencyListUnitPrice MUST NOT be null when SkuPriceId is not null.
  * PricingCurrencyListUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datasets.costandusage.chargeclass) is not "Correction".
  * PricingCurrencyListUnitPrice MAY be null in all other cases.
* When PricingCurrencyListUnitPrice is not null, PricingCurrencyListUnitPrice MUST adhere to the following requirements:
  * PricingCurrencyListUnitPrice MUST be a non-negative decimal value.
  * PricingCurrencyListUnitPrice MUST be denominated in the PricingCurrency.

## Column ID

PricingCurrencyListUnitPrice

## Display Name

Pricing Currency List Unit Price

## Description

The suggested service-provider-published unit price for a single Pricing Unit of the associated *SKU*, exclusive of any discounts and expressed in Pricing Currency.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

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

## Introduced (version)

1.2
