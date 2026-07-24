# Service Provider Name

Service Provider Name is the name of the entity that provides the [*resources*](#glossary:resource) or [*services*](#glossary:service) to which a recommendation applies. Service Provider Name is commonly used to analyze recommendations across the providers a [*practitioner*](#glossary:practitioner) is responsible for.

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

The name of the entity that provides the resources or services to which a recommendation applies.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | False                                          |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
