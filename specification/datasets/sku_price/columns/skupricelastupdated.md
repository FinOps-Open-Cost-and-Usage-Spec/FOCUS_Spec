# SKU Price Last Updated

SKU Price Last Updated is the timestamp when the [SKU Price](#datamodel.skuprice) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a [*price list*](#glossary:price-list) record, particularly if corrections or metadata updates have been applied to the record after its initial creation.

## Requirements

SkuPriceLastUpdated MUST adhere to the following requirements:

* SkuPriceLastUpdated MUST be of type Date/Time.
* SkuPriceLastUpdated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* SkuPriceLastUpdated MUST NOT be null.
* SkuPriceLastUpdated MUST represent the most recent moment in time when any column value of the SkuPrice record was created or modified.
* SkuPriceLastUpdated MUST be greater than or equal to [SkuPriceCreated](#datamodel.skuprice.skupricecreated).

> **Note:** SKU Price Last Updated reflects when the SKU Price record was last modified and may be later than [SKU Price Effective End](#datamodel.skuprice.skupriceeffectiveend), because corrections to a record's descriptive or pricing properties can be applied to a retired [*SKU Price*](#glossary:sku-price) after its effective window has closed. Practitioners reconstructing price history should key on SKU Price Effective Start and SKU Price Effective End rather than on the record audit timestamps.

## Column ID

SkuPriceLastUpdated

## Display Name

SKU Price Last Updated

## Description

The timestamp when the SKU Price record was last updated.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | Not applicable                                        |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time Format](#attributes.date/timeformat)      |

## Version Introduced

1.5
