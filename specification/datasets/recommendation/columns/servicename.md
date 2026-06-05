# Service Name

A [*service*](#glossary:service) represents an offering that can be purchased from a [*service provider*](#glossary:service-provider) (e.g., cloud virtual machine, SaaS database). The Service Name is a display name for the offering. In the Recommendation dataset, the Service Name is commonly used to analyze recommendations by the offering they relate to.

## Requirements

ServiceName MUST adhere to the following requirements:

* ServiceName MUST be of type String.
* ServiceName MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ServiceName MUST adhere to the following nullability requirements:
  * ServiceName MUST be null when a recommendation is not associated with a single *service*.
  * ServiceName MUST NOT be null when a recommendation is associated with a single *service*.

## Column ID

ServiceName

## Display Name

Service Name

## Description

An offering that can be purchased from a service provider (e.g., cloud virtual machine, SaaS database).

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | \<not specified>                               |

## Version Introduced

1.5
