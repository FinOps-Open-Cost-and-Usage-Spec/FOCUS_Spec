# Pricing Region ID

Pricing Region ID is a service-provider-assigned identifier for an isolated geographic area where the specified price for a [*resource*](#glossary:resource) or [*service*](#glossary:service) applies. This column is commonly used to join pricing rates against actual usage or to analyze unit price variations across different geographical deployments.

## Requirements

PricingRegionId MUST adhere to the following requirements:

* PricingRegionId MUST be of type String.
* PricingRegionId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingRegionId MUST represent the geographic boundary or regional construct explicitly defined by the *service provider* for the unit price, even if this represents a global or macro-region scope.
* PricingRegionId MUST adhere to the following nullability requirements:
  * PricingRegionId MUST NOT be null when the unit price is specific to a distinct region.
  * PricingRegionId MAY be null when the unit price applies globally or is not regionally scoped.

## Implementation Guidance

Practitioners are encouraged to carefully distinguish between **Pricing Region ID** and **Region ID**. 

* **Pricing Region ID** defines the geographic boundary for which the *rate itself* is valid. 
* **Region ID** defines the physical location where a specific *resource* is provisioned. 

In many cases these will be identical. However, if a pricing rate is global but still applies to specific regional deployments, or if the provider rate card dictates a resource deployment region that differs from the pricing boundary, `Pricing Region ID` reflects the pricing boundary. The set of `Region ID` values can instead be represented as key-value pairs within [SKU Price Details](#datasets.skuprice.skupricedetails) to capture the resource location without conflating the rate card logic.

## Column ID

PricingRegionId

## Display Name

Pricing Region ID

## Description

Service-provider-assigned identifier for an isolated geographic area where the specified unit price applies.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                      |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Condition       | [Includes regions](#conditions.includesregions)      |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
