# Service Provider Name

Service Provider Name is the name of the entity that provides the [*contract commitment*](#glossary:contract-commitment). This entity is responsible for fulfilling the terms of the commitment, such as applying discounts, managing credit pools, or guaranteeing resource availability.

**Notes:**

* In marketplace scenarios, the Service Provider represents the seller of the commitment (e.g., Datadog, MongoDB) rather than the marketplace operator (e.g., AWS, Azure), unless the marketplace operator is the entity providing the specific commitment benefit.
* In reseller scenarios, if the commitment is made directly with a reseller for white-labeled services, the Service Provider is the reseller. Otherwise, it is the entity that produced the underlying services tied to the commitment.

## Requirements

* ServiceProviderName MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
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
| Column type     | Dimension       |
| Feature level   | Mandatory       |
| Allows nulls    | False           |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.4