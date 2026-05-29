# Pricing Category

Pricing Category describes the pricing model applied to this specific price point. It is useful for distinguishing between standard baseline rates, rates tied to a commitment discount, and variable spot pricing within the catalog.

## Requirements

PricingCategory MUST adhere to the following requirements:

* PricingCategory MUST be of type String.
* PricingCategory MUST NOT be null.
* PricingCategory MUST be one of the allowed values.
* PricingCategory MUST be "Standard" when pricing is predetermined at the agreed upon rate.
* PricingCategory MUST be "Committed" when the rate is subject to an existing [*commitment discount*](#glossary:commitment-discount) and is not the purchase of the *commitment discount*.
* PricingCategory MUST be "Dynamic" when pricing is determined by the service provider and may change over time, regardless of predetermined agreement pricing.
* PricingCategory MUST be "Other" when there is a pricing model but none of the allowed values apply.

## Allowed Values

| Value     | Description                                                                                                                                                                                                                          |
| :-------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard  | Rates priced at the agreed upon rate, including [*negotiated discounts*](#glossary:negotiated-discount). This pricing includes any flat rate and volume/tiered pricing but does not include dynamic pricing or reduced pricing due to the application of a *commitment discount*. This does include the purchase of a commitment discount at agreed upon rates. |
| Dynamic   | Rates priced at a variable rate determined by the service provider. This includes any product or service with a unit price the service provider can change without notice, like interruptible or low priority [*resources*](#glossary:resource). |
| Committed | Rates with reduced pricing due to the application of a *commitment discount*. |
| Other     | Rates priced in a way not covered by another pricing category. |

## Column ID

PricingCategory

## Display Name

Pricing Category

## Description

The pricing model applied to this price point.

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
