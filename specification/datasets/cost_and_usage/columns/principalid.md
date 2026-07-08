# Principal ID

A Principal ID is an identifier representing the [*principal*](#glossary:principal): an initiating or authorizing actor requesting [*resources*](#glossary:resource) or [*services*](#glossary:service). The Principal can differ from the downstream consumer or end-user on whose behalf the request is made (e.g., a gateway or proxy role acting for many end-users behind it). The Principal ID is commonly used in auditing to determine which actor initiated a [*charge*](#glossary:charge).

> **Note:** While Principal ID is designed to capture opaque identifiers rather than plain-text names or email addresses, these values may still be classified as Personal Data or Personally Identifiable Information (PII) under privacy frameworks such as GDPR or CCPA (e.g., as pseudonymized data). Organizations need to separately ensure that the ingestion, storage, and processing of datasets containing this column comply with their internal data privacy, security, and retention policies.

## Requirements

PrincipalId MUST adhere to the following requirements:

* PrincipalId MUST be of type String.
* PrincipalId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PrincipalId MUST adhere to the following nullability requirements:
  * PrincipalId MUST be null the service provider cannot determine the *principal* that initiated or authorized the *charge*.
  * PrincipalId MUST NOT be null when the service provider can determine the *principal* that initiated or authorized the *charge*.
* When PrincipalId is not null, PrincipalId MUST adhere to the following requirements:
  * PrincipalId MUST be a unique identifier within the context of the service provider.
  * PrincipalId MUST NOT contain plain-text personally identifiable information (PII) when the service provider supplies an alternative opaque identifier.
  * PrincipalId MAY contain plain-text personally identifiable information (PII) when the service provider does not supply an alternative opaque identifier.

## Column ID

PrincipalId

## Display Name

Principal ID

## Description

Identifier representing the authorized actor that initiated a request for a *resource* or *service*.

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
