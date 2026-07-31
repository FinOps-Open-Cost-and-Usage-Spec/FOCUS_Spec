# Contracted Unit Price

Contracted Unit Price represents the negotiated unit price per [Pricing Unit](#datamodel.costandusage.pricingunit) for the [*SKU Price*](#glossary:sku-price) identified by the given [SKU Price ID](#datamodel.costandusage.skupriceid).

Contracted Unit Price is inclusive of negotiated pricing adjustments that modify the unit price of the associated *SKU Price* and exclusive of pricing adjustments resulting from [*commitment discounts*](#glossary:commitment-discount) or other [*post-pricing discount*](#glossary:post-pricing-discount) mechanisms applied to the [*charge*](#glossary:charge).

When no negotiated pricing adjustments are applied, Contracted Unit Price equals [List Unit Price](#datamodel.costandusage.listunitprice).

Contracted Unit Price is denominated in the [Billing Currency](#datamodel.costandusage.billingcurrency). Contracted Unit Price is commonly used for calculating savings based on negotiation activities.

## Requirements

ContractedUnitPrice MUST adhere to the following requirements:

* ContractedUnitPrice MUST be of type Decimal.
* ContractedUnitPrice MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractedUnitPrice MUST adhere to the following nullability requirements:
  * ContractedUnitPrice MUST be null when [SkuPriceId](#datamodel.costandusage.skupriceid) is null.
  * ContractedUnitPrice MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * ContractedUnitPrice MUST NOT be null when SkuPriceId is not null.
  * ContractedUnitPrice MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
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

The negotiated unit price per Pricing Unit for the *SKU Price* identified by the given SKU Price ID.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datamodel.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid non-negative decimal value                 |

## Version Introduced

1.0
