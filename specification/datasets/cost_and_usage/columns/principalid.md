# Principal ID

A Principal ID is an identifier representing the [*principal*](#glossary:principal): an entity defined in an identity and access management model (e.g., user, role, service account) to which access to [*resources*](#glossary:resource) or [*services*](#glossary:service) is granted. A *principal* is distinct from the credential (e.g., API key, access token) presented with an individual request, and from the organizational container (e.g., project, workspace) within which the request runs. The same *principal* may be associated with multiple credentials. Principal ID is commonly used to report and audit cost by the *principal* that incurred a [*charge*](#glossary:charge).

For scenarios demonstrating how Principal ID is populated across different technology environments, see [Examples: Actor Attribution](#appendix.examples:actorattribution).

## Requirements

PrincipalId MUST adhere to the following requirements:

* PrincipalId MUST be of type String.
* PrincipalId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PrincipalId MUST adhere to the following nullability requirements:
  * PrincipalId MUST be null when a *charge* is not associated with a *principal*.
  * PrincipalId MUST NOT be null when a *charge* is associated with a *principal*.
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
