# SKU Price Last Updated

SKU Price Last Updated is the timestamp when the [SKU Price](#datasets.skuprice) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a rate card record, particularly if corrections, status changes, or metadata updates have been applied to the record after its initial creation.

## Requirements

SkuPriceLastUpdated MUST adhere to the following requirements:

* SkuPriceLastUpdated MUST be of type Date/Time.
* SkuPriceLastUpdated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* SkuPriceLastUpdated MUST NOT be null.
* SkuPriceLastUpdated MUST represent the most recent moment in time when any column value of the SKU Price record was created or modified.
* SkuPriceLastUpdated MUST be greater than or equal to [SkuPriceCreated](#datasets.skuprice.skupricecreated).

## Column ID

SkuPriceLastUpdated

## Display Name

SKU Price Last Updated

## Description

The timestamp when the SKU Price record was last updated.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time Format](#attributes.date/timeformat)      |

## Version Introduced

1.5
