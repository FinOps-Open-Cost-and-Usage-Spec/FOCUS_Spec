# Service Provider Name

[Service Provider Name](#col) is the name of the entity that provides the resources or services available for usage or purchase. This entity is responsible for fulfilling the terms of the [contract commitment](#term), such as applying discounts, managing credit pools, or guaranteeing resource availability.

> **Notes:**
>
> * In marketplace scenarios, the Service Provider represents the seller of the commitment (e.g., Datadog, MongoDB) rather than the marketplace operator (e.g., AWS, Azure), unless the marketplace operator is the entity providing the specific commitment benefit.
> * In reseller scenarios, if the commitment is made directly with a reseller for white-labeled services, the Service Provider is the reseller. Otherwise, it is the entity that produced the underlying services tied to the commitment.

## Requirements

[ServiceProviderName](#col) MUST adhere to the following requirements:

* [ServiceProviderName](#col) MUST be of type String.
* [ServiceProviderName](#col) MUST conform to [StringHandling](#attr) requirements.
* [ServiceProviderName](#col) MUST NOT be null.

## Column ID

ServiceProviderName

## Display Name

Service Provider Name

## Description

The name of the entity that provides the [contract commitment](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.4
