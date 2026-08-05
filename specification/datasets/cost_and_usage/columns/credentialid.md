# Credential ID

A Credential ID is an identifier representing the [*credential*](#glossary:credential) presented to a [*service provider*](#glossary:service-provider) on the request that produced a [*charge*](#glossary:charge). A *credential* is the means by which a [*principal*](#glossary:principal) authenticates to a *service provider* (e.g., API key, access token, session), and is distinct from the *principal* itself. Where a *service provider* exposes only one level, the *principal* is the *credential* presented, and Credential ID carries the same value as [Principal ID](#datamodel.costandusage.principalid). The Credential ID is commonly used to distinguish *charges* that share a *principal* but originate from different *credentials*.

For scenarios demonstrating how Credential ID is populated across different technology categories, see [Examples: Actor Attribution](#appendix.examples:actorattribution).

## Requirements

CredentialId MUST adhere to the following requirements:

* CredentialId MUST be of type String.
* CredentialId MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* CredentialId MUST adhere to the following nullability requirements:
  * CredentialId MUST be null when the *service provider* cannot determine the *credential* presented on the request that produced the *charge*.
  * CredentialId MUST NOT be null when the *service provider* can determine the *credential* presented on the request that produced the *charge*.
* When CredentialId is not null, CredentialId MUST adhere to the following requirements:
  * CredentialId MUST be a unique identifier within the *service provider*.
  * CredentialId MUST equal PrincipalId when the *service provider* does not distinguish the *credential* presented from the *principal* that presented it.

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
