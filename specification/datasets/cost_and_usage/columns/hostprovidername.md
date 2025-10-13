# Host Provider Name

Host Provider Name is the name of the entity that provides the underlying infrastructure on which the [*resources*](#glossary:resource) or [*services*](#glossary:service) of the Service Provider's are deployed.

The HostProviderName column adheres to the following requirements:

* HostProviderName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* HostProviderName MUST be of type String.
* HostProviderName MUST conform to [StringHandling](#stringhandling) requirements.
* HostProviderName MAY be null.
* HostProviderName values are defined as follows:
  * HostProviderName MUST reflect the name of the host provider when explicitly selected by the customer.
  * HostProviderName MUST reflect the name of the host provider when the service provider gives visibility into the underlying hosting provider.
  * HostProviderName MUST equal [ServiceProviderName](#serviceprovidername) when the service provider does not provide visibility into the underlying hosting provider.
  * HostProviderName MAY be NULL when the associated [ServiceName](#servicename) does not involve deployment on any underlying infrastructure (e.g., professional services, software licenses).
  * HostProviderName MAY be NULL when the information about the entity providing the underlying infrastructure cannot be uniquely determined (e.g., when the [ChargeCategory](#chargecategory) is "Tax" or "Adjustment").

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
