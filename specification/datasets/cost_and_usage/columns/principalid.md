# Principal ID

A Principal ID is an identifier representing the [*principal*](#glossary:principal): an entity defined in a service provider identity and access management model (e.g., user, role, service account) to which access to [*resources*](#glossary:resource) or [*services*](#glossary:service) is granted. A *principal* is distinct from the credential (e.g., API key, access token) presented with an individual request, and from the organizational container (e.g., project, workspace) within which the request runs. The same *principal* may be associated with multiple credentials. The Principal ID is commonly used in auditing to determine which *principal* is associated with a [*charge*](#glossary:charge).

For scenarios demonstrating how Principal ID is populated across different technology categories, see [Examples: Actor Attribution](#appendix.examples:actorattribution).

> **Note:** Principal ID contains personally identifiable information (PII) when the *principal* is an individual (e.g., a system-generated ID, a username, or an email). Such identifiers are personal data under privacy frameworks such as GDPR or CCPA when they can be resolved to an individual. Organizations need to separately ensure that the ingestion, storage, and processing of datasets containing this column comply with their internal data privacy, security, and retention policies.

## Requirements

PrincipalId MUST adhere to the following requirements:

* PrincipalId MUST be of type String.
* PrincipalId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PrincipalId MUST adhere to the following nullability requirements:
  * PrincipalId MUST be null when the service provider cannot determine the *principal* associated with the *charge*.
  * PrincipalId MUST NOT be null when the service provider can determine the *principal* associated with the *charge*.
* When PrincipalId is not null, PrincipalId MUST adhere to the following requirements:
  * PrincipalId MUST be a unique identifier within the service provider.
* PrincipalId documentation MUST include the use cases for which PrincipalId is provided.

## Column ID

PrincipalId

## Display Name

Principal ID

## Description

Identifier representing the *principal* to which access to a *resource* or *service* is granted.

## Content Constraints

| Constraint      | Value                                                |
| :-------------- | :--------------------------------------------------- |
| Dataset         | [Cost and Usage](#datamodel.costandusage)             |
| Column type     | Dimension                                            |
| Feature level   | Conditional                                          |
| Allows nulls    | True                                                 |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.5
