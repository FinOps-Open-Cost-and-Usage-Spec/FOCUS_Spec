# SKU Price Created

SKU Price Created is the timestamp when the [SKU Price](#datasets.skuprice) record was first created. This timestamp facilitates auditability of the rate card publication lifecycle, allowing the FinOps practitioner to distinguish between the time a unit price becomes effective (i.e., [SKU Price Effective Start](#datasets.skuprice.skupriceeffectivestart)) and the time the provider actually generated the pricing record.

## Requirements

SkuPriceCreated MUST adhere to the following requirements:

* SkuPriceCreated MUST be of type Date/Time.
* SkuPriceCreated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* SkuPriceCreated MUST NOT be null.
* SkuPriceCreated MUST represent the moment in time the SKU Price record was instantiated.

## Column ID

SkuPriceCreated

## Display Name

SKU Price Created

## Description

The timestamp when the SKU Price record was first created.

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
