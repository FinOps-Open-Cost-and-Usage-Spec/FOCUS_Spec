# SKU Price Created

[SKU Price Created](#col) is the timestamp when the [SKU Price](#ds) record was first created. This timestamp facilitates auditability of the rate card publication lifecycle, allowing the FinOps [practitioner](#term) to distinguish between the time a [SKU Price](#ds) record becomes effective (i.e., [SKU Price Effective Start](#col)) and the time the provider actually generated the pricing record.

## Requirements

[SkuPriceCreated](#col) MUST adhere to the following requirements:

* [SkuPriceCreated](#col) MUST be of type Date/Time.
* [SkuPriceCreated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [SkuPriceCreated](#col) MUST NOT be null.
* [SkuPriceCreated](#col) MUST represent the moment in time the [SKU Price](#ds) record was instantiated.

## Column ID

SkuPriceCreated

## Display Name

SKU Price Created

## Description

The timestamp when the [SKU Price](#ds) record was first created.

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
