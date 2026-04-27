# Service Provider Name

Service Provider Name is the name of the entity that provides the resources or services available for usage or purchase. This entity is responsible for fulfilling the terms of the [*contract commitment*](#glossary:contract-commitment), such as applying discounts, managing credit pools, or guaranteeing resource availability.

**Notes:**

* In marketplace scenarios, the Service Provider represents the seller of the commitment (e.g., Datadog, MongoDB) rather than the marketplace operator (e.g., AWS, Azure), unless the marketplace operator is the entity providing the specific commitment benefit.
* In reseller scenarios, if the commitment is made directly with a reseller for white-labeled services, the Service Provider is the reseller. Otherwise, it is the entity that produced the underlying services tied to the commitment.

## Requirements

ServiceProviderName MUST adhere to the following requirements:

* ServiceProviderName MUST be of type String.
* ServiceProviderName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ServiceProviderName MUST NOT be null.

## Column ID

ServiceProviderName

## Display Name

Service Provider Name

## Description

The name of the entity that provides the [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension       |
| Feature level   | Mandatory       |
| Allows nulls    | False           |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (Version)

1.4
