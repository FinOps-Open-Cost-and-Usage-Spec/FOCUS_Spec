# Service Provider Name

[Service Provider Name](#col) is the name of the entity that provides the [resources](#term) or [services](#term) available for usage or purchase. These services can be built on top of infrastructure provided by a [Host Provider](#col:HostProviderName); offered as fully integrated solutions; or include complementary offerings such as support, licensing, or consulting. It is commonly used for cost analysis and reporting scenarios.

> **Notes:**
>
> * In marketplace scenarios, the Service Provider represents the seller rather than the marketplace operator, as the marketplace operator merely provides a purchasing mechanism and does not itself provide the [resources](#term) or [services](#term) available for usage or purchase.
> * In reseller scenarios, if the reseller is selling resource or services that are white-labeled from another provider, the Service Provider is the reseller.
> * In all other scenarios, the Service Provider is the entity that produced the resources or services.

## Requirements

[ServiceProviderName](#col) MUST adhere to the following requirements:

* [ServiceProviderName](#col) MUST be of type String.
* [ServiceProviderName](#col) MUST conform to [StringHandling](#attr) requirements.
* [ServiceProviderName](#col) MUST NOT be null.

See [Appendix: Participating Entity Identification Examples](#appendix.examples:participatingentityidentification) section for examples of [Service Provider Name](#col) values across various use case scenarios.

## Column ID

ServiceProviderName

## Display Name

Service Provider Name

## Description

The name of the entity that made the [resources](#term) or [services](#term) available for purchase or consumption.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | False                                     |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.3 Introduced as a replacement for the removed ProviderName column
