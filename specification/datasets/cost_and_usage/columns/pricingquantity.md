# Pricing Quantity

The Pricing Quantity represents the volume of a given [*SKU*](#glossary:sku) associated with a [*resource*](#glossary:resource) or [*service*](#glossary:service) used or purchased, based on the [Pricing Unit](#datamodel.costandusage.pricingunit). Distinct from [Consumed Quantity](#datamodel.costandusage.consumedquantity) (complementary to [Consumed Unit](#datamodel.costandusage.consumedunit)), it focuses on pricing and cost, not *resource* and *service* consumption.

## Requirements

PricingQuantity MUST adhere to the following requirements:

* PricingQuantity MUST be of type Decimal.
* PricingQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* PricingQuantity MUST adhere to the following nullability requirements:
  * PricingQuantity MUST be null when [SkuPriceId](#datamodel.costandusage.skupriceid) is null.
  * PricingQuantity MUST be null when [ChargeCategory](#datamodel.costandusage.chargecategory) is "Tax".
  * PricingQuantity MUST NOT be null when ChargeCategory is "Usage" or "Purchase" and [ChargeClass](#datamodel.costandusage.chargeclass) is not "Correction".
  * PricingQuantity MAY be null in all other cases.

## Usability Constraints

**Aggregation:** When aggregating Pricing Quantity per [SKU ID](#datamodel.costandusage.skuid) for a SKU that includes both [*covering charges*](#glossary:covering-charge) and their [*covered charges*](#glossary:covered-charge), exclude either the *covering charges* or the *covered charges* to avoid double counting. The appropriate set to exclude depends on the purpose: exclude *covering charges* when calculating utilization, or exclude *covered charges* when accounting for billed purchases.

## Column ID

PricingQuantity

## Display Name

Pricing Quantity

## Description

The volume of a given *SKU* associated with a *resource* or *service* used or purchased, based on the Pricing Unit.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datamodel.costandusage)             |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Version Introduced

1.0-preview
