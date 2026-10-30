# Pricing Service Name

[Pricing Service Name](#col) is a display name for the [service](#term) under which the specified [SKU Price](#term) is published in the [service provider's](#term:service-provider) [price list](#term). The [Pricing Service Name](#col) is commonly used for scenarios like analyzing unit price variations across [services](#term) or filtering [price lists](#term) to find specific offerings.

## Requirements

[PricingServiceName](#col) MUST adhere to the following requirements:

* [PricingServiceName](#col) MUST be of type String.
* [PricingServiceName](#col) MUST conform to [StringHandling](#attr) requirements.
* [PricingServiceName](#col) MUST represent the service offering explicitly defined by the [service provider](#term) for the [SKU Price](#term), even when this represents a grouping or abstraction of multiple distinct underlying [services](#term).
* [PricingServiceName](#col) MUST NOT be null.

## Implementation Guidance

[Practitioners](#term) are encouraged to carefully distinguish between **[Pricing Service Name](#col)** and [Service Name](#col:CostAndUsage.ServiceName).

* **[Pricing Service Name](#col)** defines the name of the [service](#term) as explicitly published in the provider's rate card or pricing catalog.
* **[Service Name](#col:CostAndUsage.ServiceName)** defines the name of the [service](#term) associated with the actual usage or provisioned [resource](#term) in the [Cost and Usage](#ds) data.

In many cases, these will be identical. However, if a [service provider](#term) abstracts or groups rate card offerings differently than their provisioned [resources](#term) (e.g., pricing multiple distinct database engines under a single generic rate card service name), `Pricing Service Name` reflects the exact service name designated by the rate card. The set of `Service Name` values can instead be represented as inclusion criteria within [SKU Price Eligibility](#col) to capture the service names without conflating the rate card logic.

## Column ID

PricingServiceName

## Display Name

Pricing Service Name

## Description

A display name for the [service](#term) under which the specified [SKU Price](#term) is published in the *service provider's* [price list](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

Preview: 1.5
