# Host Provider Name

[Host Provider Name](#col) is the name of the entity that provides the underlying infrastructure on which the [resources](#term) or [services](#term) of the [Service Provider](#col:ServiceProviderName) are deployed.

In some instances, the host provider and the service provider are the same entity: the provider hosts their own services. In other instances, the host provider and the service provider are separate entities, though the service provider may or may not expose the host provider and/or allow the customer to select the host provider.

## Requirements

[HostProviderName](#col) MUST adhere to the following requirements:

* [HostProviderName](#col) MUST be of type String.
* [HostProviderName](#col) MUST conform to [StringHandling](#attr) requirements.
* [HostProviderName](#col) MUST adhere to the following nullability requirements:
  * [HostProviderName](#col) MAY be NULL when the associated [ServiceName](#col) does not involve deployment on any underlying infrastructure (e.g., professional services, software licenses).
  * [HostProviderName](#col) MAY be NULL when the information about the entity providing the underlying infrastructure cannot be uniquely determined (e.g., when the [ChargeCategory](#col) is ["Tax"](#val:CostAndUsage.ChargeCategory) or "Adjustment").
  * [HostProviderName](#col) MUST NOT be null in all other cases.
* When [HostProviderName](#col) is not null, [HostProviderName](#col) values MUST adhere to the following requirements:
  * [HostProviderName](#col) MUST reflect the name of the host provider when explicitly selected by the customer.
  * [HostProviderName](#col) MUST reflect the name of the host provider when the service provider exposes the underlying hosting provider.
  * [HostProviderName](#col) MUST match [ServiceProviderName](#col) in all other cases.

See [Appendix: Participating Entity Identification Examples](#appendix.examples:participatingentityidentification) section for examples of Host Provider values across various use case scenarios.

## Column ID

HostProviderName

## Display Name

Host Provider Name

## Description

The name of the entity whose [resources](#term) are used by the Service Provider to make their [resources](#term) or [services](#term) available.

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | Not applicable                            |
| Column type                | Dimension                                 |
| Feature level              | Mandatory                                 |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.3
