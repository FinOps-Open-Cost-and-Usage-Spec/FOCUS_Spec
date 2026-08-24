# Credential ID

A Credential ID is an identifier representing the [*credential*](#glossary:credential) presented on the request that produced a [*charge*](#glossary:charge). A *credential* is the means by which a [*principal*](#glossary:principal) is authenticated (e.g., API key, access token, session), and is distinct from the *principal* itself. Credential ID is an identifier that references a *credential* rather than the *credential* itself, so a *credential* with no published identifier has no value to include in the column. Credential ID is commonly used to distinguish *charges* that share a *principal* but originate from different *credentials*.

For scenarios demonstrating how Credential ID is populated across different technology environments, see [Examples: Actor Attribution](#appendix.examples:actorattribution).

## Requirements

CredentialId MUST adhere to the following requirements:

* CredentialId MUST be of type String.
* CredentialId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CredentialId MUST adhere to the following nullability requirements:
  * CredentialId MUST be null when a *charge* is not associated with a *credential*.
  * CredentialId MUST be null when the *credential* associated with a *charge* has no published identifier.
  * CredentialId MUST NOT be null when the *credential* associated with a *charge* has a published identifier.
* When CredentialId is not null, CredentialId MUST adhere to the following requirements:
  * CredentialId MUST be a unique identifier within the service provider.
  * CredentialId MUST be an identifier that references a *credential*.
  * CredentialId MUST NOT contain a *credential* value that authenticates a request (e.g., an API key string, an access token, a password).
* CredentialId documentation MUST include the use cases for which CredentialId is provided.

## Column ID

CredentialId

## Display Name

Credential ID

## Description

Identifier representing the *credential* presented on the request that produced a *charge*.

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
