# Principal ID

A [Principal ID](#col) is an identifier representing the [principal](#term) to which access to a [resource](#term) or [service](#term) is granted. [Principal ID](#col) is commonly used to report and audit cost by the [principal](#term) that incurred a [charge](#term). Descriptive attributes of the [principal](#term) (e.g., display name, type) are carried in [Requester Details](#col).

For scenarios demonstrating how [Principal ID](#col) is populated across different technology environments, see [Examples: Requester Attribution](#appendix.examples:requesterattribution).

## Requirements

[PrincipalId](#col) MUST adhere to the following requirements:

* [PrincipalId](#col) MUST be of type String.
* [PrincipalId](#col) MUST conform to [StringHandling](#attr) requirements.
* [PrincipalId](#col) MUST adhere to the following nullability requirements:
  * [PrincipalId](#col) MUST be null when a [charge](#term) is not associated with a [principal](#term).
  * [PrincipalId](#col) MUST be null when the [principal](#term) associated with a [charge](#term) has no published identifier.
  * [PrincipalId](#col) MUST NOT be null when the [principal](#term) associated with a [charge](#term) has a published identifier.
* When [PrincipalId](#col) is not null, [PrincipalId](#col) MUST adhere to the following requirements:
  * [PrincipalId](#col) MUST be an identifier that references a [principal](#term).
  * [PrincipalId](#col) MUST be a unique identifier within the [service provider](#term).
  * [PrincipalId](#col) MUST NOT contain a value that authenticates a request (e.g., an API key string, an access token, a password).

## Column ID

PrincipalId

## Display Name

Principal ID

## Description

Identifier representing the [principal](#term) to which access to a [resource](#term) or [service](#term) is granted.

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
