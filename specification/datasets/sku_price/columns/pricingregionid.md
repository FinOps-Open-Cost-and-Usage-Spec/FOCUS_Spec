# Pricing Region ID

[Pricing Region ID](#col) is a service-provider-assigned identifier for an isolated geographic area where the specified [SKU Price](#term) applies. This column is commonly used to join pricing rates against actual usage or to analyze unit price variations across different geographical deployments.

## Requirements

[PricingRegionId](#col) MUST adhere to the following requirements:

* [PricingRegionId](#col) MUST be of type String.
* [PricingRegionId](#col) MUST conform to [StringHandling](#attr) requirements.
* [PricingRegionId](#col) MUST represent the geographic boundary or regional construct explicitly defined by the [service provider](#term) for the [SKU Price](#term), even when this represents a global or macro-region scope.
* [PricingRegionId](#col) MUST adhere to the following nullability requirements:
  * [PricingRegionId](#col) MUST NOT be null when the [SKU Price](#term) is specific to a distinct region.
  * [PricingRegionId](#col) MAY be null when the [SKU Price](#term) applies globally or is not regionally scoped.

## Implementation Guidance

### Difference Between Pricing Region ID and Region ID

[Practitioners](#term) are encouraged to carefully distinguish between **[Pricing Region ID](#col)** and [Region ID](#col:CostAndUsage.RegionId).

* **[Pricing Region ID](#col)** defines the geographic boundary for which the *rate itself* is valid.
* **[Region ID](#col:CostAndUsage.RegionId)** defines the physical location where a specific [resource](#term) is provisioned.

In many cases these will be identical. However, if a [SKU Price](#term) is global but still applies to specific regional deployments, or if the *service provider's* [price list](#term) dictates a resource deployment region that differs from the pricing boundary, `Pricing Region ID` reflects the pricing boundary. The set of `Region ID` values can instead be represented as inclusion criteria within [SKU Price Eligibility](#col) to capture the resource location without conflating the [price list](#term) logic.

### Null vs Global Values for Non-Regionalized Prices

Non-regionalized [services](#term) (i.e., [services](#term) with no physical geography) are inconsistently represented across [service providers](#term). This variance exists not only across different [service providers](#term), but frequently across different [services](#term) within the exact same [service provider](#term). For instance, one service team might use a null [Pricing Region ID](#col), while another [service](#term) from the same [service provider](#term) explicitly publishes the string identifier "global" to mean the exact same thing.

Because of this native inconsistency, consumers of this dataset should be aware that a [Pricing Region ID](#col) of null or "global" cannot reliably be used on its own to distinguish between a truly worldwide geographic scope and a non-regionalized service scope.

## Column ID

PricingRegionId

## Display Name

Pricing Region ID

## Description

Service-provider-assigned identifier for an isolated geographic area where the specified [SKU Price](#term) applies.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#ds)                                     |
| Operating Model Conditions | [Includes Regions](#omc)                                      |
| Column type                | Dimension                                            |
| Feature level              | Conditional                                          |
| Allows nulls               | True                                                 |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

Preview: 1.5
