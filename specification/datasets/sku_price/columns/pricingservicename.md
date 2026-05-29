# Pricing Service Name

Pricing Service Name represents an offering that can be purchased from a [*service provider*](#glossary:service-provider) (e.g., virtual machine, database, professional service). A *service* offering can include various types of usage or other [*charges*](#glossary:charge). 

Pricing Service Name is a display name for the offering to which the specified unit price applies. The Pricing Service Name is commonly used for scenarios like analyzing unit price variations across services or filtering rate cards to find specific offerings.

## Requirements

PricingServiceName MUST adhere to the following requirements:

* PricingServiceName MUST be of type String.
* PricingServiceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingServiceName MUST represent the service offering explicitly defined by the *service provider* for the unit price, even if this represents a grouping or abstraction of multiple distinct underlying services.
* PricingServiceName MUST NOT be null.

## Implementation Guidance

Practitioners are encouraged to carefully distinguish between **Pricing Service Name** and **Service Name**. 

* **Pricing Service Name** defines the name of the service as explicitly published in the provider's rate card or pricing catalog.
* **Service Name** defines the name of the service associated with the actual usage or provisioned resource in the cost and usage data.

In many cases, these will be identical. However, if a *service provider* abstracts or groups rate card offerings differently than their provisioned resources (e.g., pricing multiple distinct database engines under a single generic rate card service name), `Pricing Service Name` reflects the exact service name designated by the rate card. The set of `Service Name` values can instead be represented as key-value pairs within [SKU Price Details](#datasets.skuprice.skupricedetails) to capture the service names without conflating the rate card logic.

## Column ID

PricingServiceName

## Display Name

Pricing Service Name

## Description

A display name for the offering to which the specified unit price applies (e.g., cloud virtual machine, SaaS database).

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
