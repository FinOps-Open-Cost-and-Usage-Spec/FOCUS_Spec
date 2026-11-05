# Service Provider Name

[Service Provider Name](#col) is the name of the entity that provides the [resources](#term) or [services](#term) to which the specified [SKU Price](#term) applies. These offerings can range from foundational infrastructure to fully integrated software solutions, or include complementary offerings such as support, licensing, or consulting. This column is commonly used to filter rate cards by the publishing vendor or to compare prices across different providers.

**Notes:**

* In marketplace scenarios, the Service Provider represents the seller rather than the marketplace operator, as the marketplace operator merely provides a purchasing mechanism and does not itself provide the [resources](#term) or [services](#term) available for purchase.
* In reseller scenarios, if the reseller is selling [resources](#term) or [services](#term) that are white-labeled from another provider, the Service Provider is the reseller.
* In all other scenarios, the Service Provider is the entity that produced the [resources](#term) or [services](#term).

## Requirements

[ServiceProviderName](#col) MUST adhere to the following requirements:

* [ServiceProviderName](#col) MUST be of type String.
* [ServiceProviderName](#col) MUST conform to [StringHandling](#attr) requirements.
* [ServiceProviderName](#col) MUST NOT be null.

See the [Appendix: Participating Entity Identification Examples](#appendix.examples:participatingentityidentification) section for examples of [Service Provider Name](#col) values across various use case scenarios.

## Column ID

ServiceProviderName

## Display Name

Service Provider Name

## Description

The name of the entity that provides the [resources](#term) or [services](#term) to which the specified [SKU Price](#term) applies.

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
