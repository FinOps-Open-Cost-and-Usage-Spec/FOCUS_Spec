# Host Provider Name

Host Provider Name is the name of the entity that provides the underlying infrastructure on which the [*resources*](#glossary:resource) or [*services*](#glossary:service) of the [Service Provider](#serviceprovidername) are deployed.

In some instances, the host provider and the service provider are the same entity: the provider hosts their own services.  In other instances, the host provider and the service provider are separate entities, though the service provider may or may not expose the host provider and/or allow the customer to select the host provider.

## Requirements

HostProviderName adheres to the following requirements:

* HostProviderName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* HostProviderName MUST be of type String.
* HostProviderName MUST conform to [StringHandling](#stringhandling) requirements.
* HostProviderName nullability is defined as follows:
  * HostProviderName MAY be NULL when the associated [ServiceName](#servicename) does not involve deployment on any underlying infrastructure (e.g., professional services, software licenses).
  * HostProviderName MAY be NULL when the information about the entity providing the underlying infrastructure cannot be uniquely determined (e.g., when the [ChargeCategory](#chargecategory) is "Tax" or "Adjustment").
  * HostProviderName MUST NOT be null in all other cases.
* When HostProviderName is not null, HostProviderName values are defined as follows:
  * HostProviderName MUST reflect the name of the host provider when explicitly selected by the customer.
  * HostProviderName MUST reflect the name of the host provider when the service provider exposes the underlying hosting provider.
  * HostProviderName MUST equal [ServiceProviderName](#serviceprovidername) in all other cases.

See [Appendix: Participating Entity Identification Examples](#participatingentityidentificationexamples) section for examples of Host Provider values across various use case scenarios.

## Column ID

HostProviderName

## Display Name

Host Provider Name

## Description

The name of the entity whose *resources* are used by the Service Provider to make their [*resources*](#glossary:resource) or [*services*](#glossary:service) available.

## Content Constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
