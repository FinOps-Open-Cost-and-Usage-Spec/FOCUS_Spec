# Pricing Service Name
Pricing Service Name is a display name for the [*service*](#glossary:service) under which the specified [*SKU Price*](#glossary:sku-price) is published in the [*service provider's*](#glossary:service-provider) [*price list*](#glossary:price-list). The Pricing Service Name is commonly used for scenarios like analyzing unit price variations across *services* or filtering *price lists* to find specific offerings.

## Requirements

PricingServiceName MUST adhere to the following requirements:

* PricingServiceName MUST be of type String.
* PricingServiceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingServiceName MUST represent the service offering explicitly defined by the *service provider* for the *SKU Price*, even when this represents a grouping or abstraction of multiple distinct underlying *services*.
* PricingServiceName MUST NOT be null.

## Implementation Guidance

[*Practitioners*](#glossary:practitioner) are encouraged to carefully distinguish between **Pricing Service Name** and [Service Name](#datamodel.costandusage.servicename).

* **Pricing Service Name** defines the name of the *service* as explicitly published in the provider's rate card or pricing catalog.
* **Service Name** defines the name of the *service* associated with the actual usage or provisioned [*resource*](#glossary:resource) in the [Cost and Usage](#datamodel.costandusage) data.

In many cases, these will be identical. However, if a *service provider* abstracts or groups rate card offerings differently than their provisioned *resources* (e.g., pricing multiple distinct database engines under a single generic rate card service name), `Pricing Service Name` reflects the exact service name designated by the rate card. The set of `Service Name` values can instead be represented as inclusion criteria within [SKU Price Eligibility](#datamodel.skuprice.skupriceeligibility) to capture the service names without conflating the rate card logic.

## Column ID

PricingServiceName

## Display Name

Pricing Service Name

## Description

A display name for the *service* under which the specified *SKU Price* is published in the *service provider's* *price list*.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                     |
| Operating Model Conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.5
