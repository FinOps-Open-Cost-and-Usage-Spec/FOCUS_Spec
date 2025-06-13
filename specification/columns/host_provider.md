# Host Provider

A Host Provider is an entity whose [*resources*](#glossary:resource) are used by the Service Provider to make their [*resources*](#glossary:resource) or [*services*](#glossary:service) available.

The HostProvider column adheres to the following requirements:

* The HostProvider column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) and represents the service provider where [*resources*](#glossary:resource) or [*services*](#glossary:service) are deployed on.
* For Service Providers that allow their customer to select or know the host provider where resources or services are deployed, this SHOULD be the name of that selected or visible host provider
* For Service Providers that DO NOT allow their customer to select or know the host provider where resources or services are deployed, this SHOULD be the name of the [Service Provider](#serviceprovider)
* This column MUST be of type String and MAY contain null values when a line item does not pertain to a resource or services with a specific host provider, such as purchases, refunds, or taxes.

See [Appendix: Entity Identification Examples](#entityidentification) section for examples of Host Provider values for various use case scenarios.

## Column ID

HostProvider

## Display Name

Host Provider

## Description

The name of the entity whose *resources* are used by the Service Provider to make their [*resources*](#glossary:resource) or [*services*](#glossary:service) available.

## Content Constraints

| Constraint      | Value            |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Recommended      |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
