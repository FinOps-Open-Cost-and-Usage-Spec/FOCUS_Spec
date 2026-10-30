# Contract Commitment Type

[Contract Commitment Type](#col) is a service-provider-assigned name to identify the type of [contract commitment](#term). [Contract Commitment Type](#col) is a readable display name and not a code. [Contract Commitment Type](#col) is commonly used for displaying and aggregating the types of commitments the practitioner has made, stated in service-provider-specific terms.

## Requirements

[ContractCommitmentType](#col) MUST adhere to the following requirements:

* [ContractCommitmentType](#col) MUST be of type String.
* [ContractCommitmentType](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractCommitmentType](#col) MUST NOT be null.
* [ContractCommitmentType](#col) MUST be a consistent, readable display value.

## Column ID

ContractCommitmentType

## Display Name

Contract Commitment Type

## Description

A service-provider-assigned name to identify the type of [contract commitment](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.3
