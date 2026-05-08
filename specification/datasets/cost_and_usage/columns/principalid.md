# Principal ID

A Principal ID is an identifier representing the [*principal*](#glossary:principal): an authenticated system identity, service account, access role, or user that initiated the request to the infrastructure provider or service provider. The Principal ID is commonly used to audit which infrastructure credential authorized a [*charge*](#glossary:charge). 

Principal ID works in conjunction with [Consumer ID](#datasets.costandusage.consumerid) to resolve asymmetric identity granularity.  While Principal ID captures the system identity that authorized the transaction with the provider, Consumer ID captures the logical downstream actor (such as an end-user or tenant) that ultimately utilized the service at the application layer.

## Requirements

PrincipalId MUST adhere to the following requirements:

* PrincipalId MUST be of type String.
* PrincipalId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PrincipalId MUST adhere to the following nullability requirements:
  * PrincipalId MUST be null when a [*charge*](#glossary:charge) is not attributed to a *principal* by the service provider.
  * PrincipalId MUST NOT be null when a *charge* is attributed to a *principal* by the service provider.
* When PrincipalId is not null, PrincipalId MUST adhere to the following requirements:
  * PrincipalId MUST be a unique identifier within the context of the service provider.

## Column ID

PrincipalId

## Display Name

Principal ID

## Description

Identifier of the authenticated system identity or role that initiated the request to the service provider.

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
