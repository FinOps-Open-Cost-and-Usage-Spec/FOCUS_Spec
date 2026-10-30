# SKU Price Last Updated

[SKU Price Last Updated](#col) is the timestamp when the [SKU Price](#ds) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a rate card record, particularly if corrections or metadata updates have been applied to the record after its initial creation.

## Requirements

[SkuPriceLastUpdated](#col) MUST adhere to the following requirements:

* [SkuPriceLastUpdated](#col) MUST be of type Date/Time.
* [SkuPriceLastUpdated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [SkuPriceLastUpdated](#col) MUST NOT be null.
* [SkuPriceLastUpdated](#col) MUST represent the most recent moment in time when any column value of the [SKU Price](#ds) record was created or modified.
* [SkuPriceLastUpdated](#col) MUST be greater than or equal to [SkuPriceCreated](#col).

> **Note:** [SKU Price Last Updated](#col) reflects when the [SKU Price](#ds) record was last modified and may be later than [SKU Price Effective End](#col), because corrections to a record's descriptive or pricing properties can be applied to a retired rate after its effective window has closed. Practitioners reconstructing price history should key on [SKU Price Effective Start](#col) and [SKU Price Effective End](#col) rather than on the record audit timestamps.

## Column ID

SkuPriceLastUpdated

## Display Name

SKU Price Last Updated

## Description

The timestamp when the [SKU Price](#ds) record was last updated.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | Date/Time                                            |
| Value format               | [Date/Time Format](#attr)                            |

## Version Introduced

Preview: 1.5
