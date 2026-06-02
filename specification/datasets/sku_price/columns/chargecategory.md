# Charge Category

Charge Category represents the highest-level classification of a [*SKU Price*](#glossary:sku-price) based on the nature of what is being priced. In the SKU Price dataset, Charge Category is used to quickly distinguish between published rates for consumption-based usage and published fees for upfront or recurring purchases.

## Requirements

ChargeCategory MUST adhere to the following requirements:

* ChargeCategory MUST be of type String.
* ChargeCategory MUST NOT be null.
* ChargeCategory MUST be one of the allowed values.
* ChargeCategory MUST be "Usage" when the *SKU Price* represents the rate for consumption of a service or resource.
* ChargeCategory MUST be "Purchase" when the *SKU Price* represents a fee for the acquisition of a service, resource, or *commitment*.

## Allowed Values

| Value      | Description                                                                                                                                    |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------|
| Usage      | The published unit price for the quantity of a service or resource that is consumed over a given period of time. |
| Purchase   | The published fee for the acquisition of a service, resource, or *commitment* bought upfront or on a recurring basis.          |

## Implementation Guidance

While the Charge Category column is shared between the [Cost and Usage](#datasets.costandusage) dataset and the [SKU Price](#datasets.skuprice) dataset, practitioners should note that the allowed values differ significantly by design.

The Cost and Usage dataset acts as a financial ledger that tracks post-facto financial events. Therefore, it requires values like `Tax`, `Credit`, and `Adjustment` to accurately balance a final invoice.

Conversely, the SKU Price dataset acts as a pre-facto catalog of available unit rates. Because taxes are calculated dynamically based on jurisdiction and entity, and credits or adjustments are account-level ledger corrections, service providers do not publish catalog unit prices for these events. Therefore, the allowed values for Charge Category in the SKU Price dataset are strictly limited to catalog pricing constructs: `Usage` (the published rate to consume a resource) and `Purchase` (the published fee to acquire a commitment or service).

## Column ID

ChargeCategory

## Display Name

Charge Category

## Description

Represents the highest-level classification of a *SKU Price* based on whether it is a usage rate or a purchase fee.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | Allowed values                                       |

## Version Introduced

1.5
