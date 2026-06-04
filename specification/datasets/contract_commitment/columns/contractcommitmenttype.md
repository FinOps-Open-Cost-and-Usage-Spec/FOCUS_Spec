# Contract Commitment Type

Contract Commitment Type is a service-provider-assigned name to identify the type of [*contract commitment*](#glossary:contract-commitment). Contract Commitment Type is a readable display name and not a code. Contract Commitment Type is commonly used for displaying and aggregating the types of commitments the practitioner has made, stated in service-provider-specific terms.

## Requirements

ContractCommitmentType MUST adhere to the following requirements:

* ContractCommitmentType MUST be of type String.
* ContractCommitmentType MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentType MUST NOT be null.
* ContractCommitmentType MUST be a consistent, readable display value.

## Column ID

ContractCommitmentType

## Display Name

Contract Commitment Type

## Description

A service-provider-assigned name to identify the type of *contract commitment*.

## Content Constraints

| Constraint      | Value                                                |
|:----------------|:-----------------------------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | String                                               |
| Value format    | \<not specified>                                     |

## Version Introduced

1.3
