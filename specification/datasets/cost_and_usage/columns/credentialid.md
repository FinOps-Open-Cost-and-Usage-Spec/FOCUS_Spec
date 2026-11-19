# Credential ID

A [Credential ID](#col) is an identifier representing the [credential](#term) presented on the request that produced a [charge](#term). [Credential ID](#col) commonly distinguishes [charges](#term) that share a [principal](#term) but were authenticated with different [credentials](#term). Descriptive attributes of the [credential](#term) (e.g., display name, type) are carried in [Requester Details](#col).

For scenarios demonstrating how [Credential ID](#col) is populated across different technology environments, see [Examples: Requester Attribution](#appendix.examples:requesterattribution).

## Requirements

[CredentialId](#col) MUST adhere to the following requirements:

* [CredentialId](#col) MUST be of type String.
* [CredentialId](#col) MUST conform to [StringHandling](#attr) requirements.
* [CredentialId](#col) MUST adhere to the following nullability requirements:
  * [CredentialId](#col) MUST be null when a [charge](#term) is not associated with a [credential](#term).
  * [CredentialId](#col) MUST be null when the [credential](#term) associated with a [charge](#term) has no published identifier.
  * [CredentialId](#col) MUST NOT be null when the [credential](#term) associated with a [charge](#term) has a published identifier.
* When [CredentialId](#col) is not null, [CredentialId](#col) MUST adhere to the following requirements:
  * [CredentialId](#col) MUST be an identifier that references a [credential](#term).
  * [CredentialId](#col) MUST be a unique identifier within the [service provider](#term).
  * [CredentialId](#col) MUST NOT contain a [credential](#term) value that authenticates a request (e.g., an API key string, an access token, a password).

## Column ID

CredentialId

## Display Name

Credential ID

## Description

Identifier representing the [credential](#term) presented on the request that produced a [charge](#term).

## Content Constraints

| Constraint                 | Value                                     |
| :------------------------- | :---------------------------------------- |
| Dataset                    | [Cost and Usage](#ds)                     |
| Operating model conditions | [Includes Requester Attribution](#omc)                                                   |
| Column type                | Dimension                                 |
| Feature level              | Conditional                               |
| Allows nulls               | True                                      |
| Data type                  | String                                    |
| Value format               | \<not specified>                          |

## Version Introduced

1.5
