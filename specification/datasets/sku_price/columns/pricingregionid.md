# Pricing Region ID

Pricing Region ID is a service-provider-assigned identifier for an isolated geographic area where the specified price for a [*resource*](#glossary:resource) or [*service*](#glossary:service) applies. This column is commonly used to join pricing rates against actual usage or to analyze unit price variations across different geographical deployments.

## Requirements

PricingRegionId MUST adhere to the following requirements:

* PricingRegionId MUST be of type String.
* PricingRegionId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingRegionId MUST represent the geographic boundary or regional construct explicitly defined by the *service provider* for the unit price, even when this represents a global or macro-region scope.
* PricingRegionId MUST adhere to the following nullability requirements:
  * PricingRegionId MUST NOT be null when the unit price is specific to a distinct region.
  * PricingRegionId MAY be null when the unit price applies globally or is not regionally scoped.

## Implementation Guidance

### Difference Between Pricing Region ID and Region ID

Practitioners are encouraged to carefully distinguish between **Pricing Region ID** and [Region ID](#datamodel.costandusage.regionid).

* **Pricing Region ID** defines the geographic boundary for which the *rate itself* is valid.
* **Region ID** defines the physical location where a specific *resource* is provisioned.

In many cases these will be identical. However, if a pricing rate is global but still applies to specific regional deployments, or if the provider rate card dictates a resource deployment region that differs from the pricing boundary, `Pricing Region ID` reflects the pricing boundary. The set of `Region ID` values can instead be represented as inclusion criteria within [SKU Price Eligibility](#datamodel.skuprice.skupriceeligibility) to capture the resource location without conflating the rate card logic.

### Null Vs Global Values For Non-Regionalized Prices

Non-regionalized services (i.e., services with no physical geography) are inconsistently represented across *service providers*. This variance exists not only across different *service providers*, but frequently across different services within the exact same *service provider*. For instance, one service team might use a null Pricing Region ID, while another service from the same *service provider* explicitly publishes the string identifier "global" to mean the exact same thing.

Because of this native inconsistency, consumers of this dataset should be aware that a Pricing Region ID of null or "global" cannot reliably be used on its own to distinguish between a truly worldwide geographic scope and a non-regionalized service scope.

## Column ID

PricingRegionId

## Display Name

Pricing Region ID

## Description

Service-provider-assigned identifier for an isolated geographic area where the specified unit price applies.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [SKU Price](#datamodel.skuprice)                     |
| Operating Model Conditions | [Includes Regions](#operatingmodelconditions.includesregions) |
| Column type                | Dimension                                            |
| Feature level              | Conditional                                          |
| Allows nulls               | True                                                 |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.5
