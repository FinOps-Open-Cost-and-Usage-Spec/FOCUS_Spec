# Service Provider Name

Service Provider Name is the name of the entity that provides the [*resources*](#glossary:resource) or [*services*](#glossary:service) available for usage or purchase. These services can be built on top of infrastructure provided by a [Host Provider](#hostprovidername), offered as fully integrated solutions, or include complementary offerings such as support, licensing, or consulting. It is commonly used for cost analysis and reporting scenarios.

**Notes:**
* In marketplace scenarios, the Service Provider represents the seller rather than the marketplace operator, as the marketplace operator merely provides a purchasing mechanism and does not itself provide the *resources* or *services* available for usage or purchase.
* In reseller scenarios, if the reseller is selling resource or services that are white-labeled from another provider, the Service Provider is the reseller. In all other cases the Service Provider is the entity that produced the resources or services.

## Requirements

ServiceProviderName adheres to the following requirements:

* ServiceProviderName MUST be present in a Cost and Usage [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ServiceProviderName MUST be of type String.
* ServiceProviderName MUST conform to [StringHandling](#stringhandling) requirements.
* ServiceProviderName MUST NOT be null.

See [Appendix: Participating Entity Identification Examples](#participatingentityidentificationexamples) section for examples of Service Provider Name values across various use case scenarios.

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
