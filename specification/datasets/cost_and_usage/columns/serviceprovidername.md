# Service Provider Name

Service Provider Name is the name of the entity that provides the [*resources*](#glossary:resource) or [*services*](#glossary:service) available for usage or purchase. These services can be built on top of infrastructure provided by a [Host Provider](#hostprovider), offered as fully integrated solutions, or include complementary offerings such as support, licensing, or consulting. It is commonly used for cost analysis and reporting scenarios. In marketplace scenarios, the Service Provider is the seller, not the entity operating the marketplace, as marketplace is providing a mechanism for purchase, not independently providing the resources or services independently for purchase or usage.

The Service Provider Name column adheres to the following requirements:

* ServiceProviderName MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceProviderName MUST be of type String.
* ServiceProviderName MUST conform to [StringHandling](#stringhandling) requirements.
* ServiceProviderName MUST NOT be null.

See [Appendix: Entity Identification Examples](#entityidentification) section for examples of Service Provider Name values for various use case scenarios.

## Column ID

ServiceProviderName

## Display Name

Service Provider Name

## Description

The name of the entity that made the *resources* or *services* available for purchase or consumption.

## Content Constraints

| Constraint      | Value           |
|:----------------|:----------------|
| Column type     | Dimension       |
| Feature level   | Mandatory       |
| Allows nulls    | False           |
| Data type       | String          |
| Value format    | \<not specified> |

## Introduced (version)

1.3 Introduced as a replacement for [ProviderName](#providername)