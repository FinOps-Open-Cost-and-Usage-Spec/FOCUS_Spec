# Host Provider Name

Host Provider Name is the name of the entity that provides the underlying infrastructure on which the [*resources*](#glossary:resource) or [*services*](#glossary:service) of one or more Service Providers are deployed.

The HostProviderName column adheres to the following requirements:

* HostProviderName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* HostProviderName MUST be of type String.
* HostProviderName MUST conform to [StringHandling](#stringhandling) requirements.
* HostProviderName MUST NOT be null when a *charge* pertains to *resources* or *services*.
* HostProviderName values are defined as follows:
  * HostProviderName SHOULD reflect the name of the [*host provider*](#glossary:host-provider) of deployed *resources* or *services* when this information is available to customers.
  * HostProviderName MAY be "Not Applicable" for *charges* that are not relevant to a hosting scenario (e.g., professional services, licenses, taxes, refunds).
  * HostProviderName MUST equal [ServiceProviderName](#serviceprovidername) in all other cases.

See [Appendix: Entity Identification Examples](#entityidentification) section for examples of Host Provider values for various use case scenarios.

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
