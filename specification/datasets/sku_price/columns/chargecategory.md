# Charge Category

Charge Category represents the highest-level classification of a [*SKU Price*](#glossary:sku-price) based on the nature of what is being priced. In the SKU Price dataset, Charge Category is used to quickly distinguish between published unit prices for consumption-based usage, published unit prices for upfront or recurring purchases, and published unit values for granted credits.

## Requirements

ChargeCategory MUST adhere to the following requirements:

* ChargeCategory MUST be of type String.
* ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.
* ChargeCategory MUST be "Usage" when the *SKU Price* represents the unit price for consumption of a service or resource.
* ChargeCategory MUST be "Purchase" when the *SKU Price* represents a purchase for the acquisition of a service, resource, or [*commitment*](#glossary:commitment).
* ChargeCategory MUST be "Credit" when the *SKU Price* represents the unit value of a credit granted by the service provider.

## Allowed Values

| Value      | Description                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------|
| Usage      | The published unit price for the quantity of a service or resource that is consumed over a given period of time. |
| Purchase   | The published unit price for the acquisition of a service, resource, or *commitment* bought upfront or on a recurring basis.          |
| Credit     | The published unit value of a credit granted by the service provider (e.g., a promotional credit carrying a defined unit value). |

## Implementation Guidance

While the Charge Category column is shared between the [Cost and Usage](#datamodel.costandusage) dataset and the [SKU Price](#datamodel.skuprice) dataset, practitioners should note that the allowed values differ by design.

The Cost and Usage dataset acts as a financial ledger that tracks post-facto financial events. Therefore, it requires values like "Tax" and "Adjustment" to accurately balance a final invoice.

Conversely, the SKU Price dataset acts as a pre-facto catalog of available unit prices. Because taxes are calculated dynamically based on jurisdiction and entity, and adjustments are account-level ledger corrections, service providers do not publish catalog unit prices for these events. Therefore, the allowed values for Charge Category in the SKU Price dataset are limited to catalog pricing constructs: "Usage" (the published unit price to consume a resource), "Purchase" (the published unit price to acquire a commitment or service), and "Credit" (the published unit value of a granted credit).

Credits are catalog pricing constructs where a service provider issues a distinct *SKU* and *SKU Price* for the credit, most commonly a promotional credit carrying a defined unit value. Where a service provider publishes no such *SKU Price*, the credit appears only in Cost and Usage and has no SKU Price record.

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Represents the highest-level classification of a *SKU Price* based on whether it is a usage unit price, a purchase unit price, or a credit value.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | Not applicable                                        |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

1.5
