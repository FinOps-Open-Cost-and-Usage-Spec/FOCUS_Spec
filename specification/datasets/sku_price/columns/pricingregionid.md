# Pricing Region ID

Pricing Region ID is a service-provider-assigned identifier for an isolated geographic area where the specified price for a [*resource*](#glossary:resource) or [*service*](#glossary:service) applies. This column is commonly used to join unit prices against actual usage or to analyze unit price variations across different geographical deployments.

## Requirements

PricingRegionId MUST adhere to the following requirements:

* PricingRegionId MUST be of type String.
* PricingRegionId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingRegionId MUST represent the geographic boundary or regional construct explicitly defined by the *service provider* for the unit price, even when this represents a global or macro-region scope.
* PricingRegionId MUST adhere to the following nullability requirements:
  * PricingRegionId MUST NOT be null when the unit price is specific to a distinct region.
  * PricingRegionId MAY be null when the unit price applies globally or is not regionally scoped.

## Implementation Guidance

Practitioners are encouraged to carefully distinguish between **Pricing Region ID** and [Region ID](#datamodel.costandusage.regionid).

* **Pricing Region ID** defines the geographic boundary for which the *unit price itself* is valid.
* **Region ID** defines the physical location where a specific *resource* is provisioned.

In many cases these will be identical. However, if a unit price is global but still applies to specific regional deployments, or if the provider price list dictates a resource deployment region that differs from the pricing boundary, `Pricing Region ID` reflects the pricing boundary. The set of `Region ID` values can instead be represented as inclusion criteria within [SKU Price Eligibility](#datamodel.skuprice.skupriceeligibility) to capture the resource location without conflating the price list logic.

## Column ID

PricingRegionId

## Display Name

Pricing Region ID

## Description

Service-provider-assigned identifier for an isolated geographic area where the specified unit price applies.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datamodel.skuprice)                      |
| Conditions      | [Includes Regions](#conditions.includesregions)      |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
