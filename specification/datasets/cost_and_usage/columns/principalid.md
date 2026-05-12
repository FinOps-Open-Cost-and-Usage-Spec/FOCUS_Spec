# Principal ID

A Principal ID is an identifier representing the [*principal*](#glossary:principal): an authenticated actor (e.g., user, service account, application credential) that initiated the request to the [host provider](#datasets.costandusage.hostprovidername) or [service provider](#datasets.costandusage.serviceprovidername). The Principal ID is commonly used to audit which infrastructure actor authorized a [*charge*](#glossary:charge).

Principal ID works in conjunction with [Consumer ID](#datasets.costandusage.consumerid) to resolve asymmetric actor granularity. While Principal ID captures the authenticated actor that authorized the transaction with the provider, Consumer ID captures the logical downstream actor (e.g., end user, tenant) that ultimately utilized a [*resource*](#glossary:resource) or [*service*](#glossary:service) at the application layer.

## Requirements

PrincipalId MUST adhere to the following requirements:

* PrincipalId MUST be of type String.
* PrincipalId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PrincipalId MUST adhere to the following nullability requirements:
  * PrincipalId MUST be null when a *charge* is not attributed to a *principal* by the service provider.
  * PrincipalId MUST NOT be null when a *charge* is attributed to a *principal* by the service provider.
* When PrincipalId is not null, PrincipalId MUST adhere to the following requirements:
  * PrincipalId MUST be a unique identifier within the context of the service provider.

## Column ID

PrincipalId

## Display Name

Principal ID

## Description

Identifier of the authenticated actor that initiated the request to the service provider.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datasets.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
