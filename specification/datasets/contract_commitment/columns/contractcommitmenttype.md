# Contract Commitment Type

Contract Commitment Type is a provider-assigned name to identify the type of [*contract commitment*](#glossary:contract-commitment). Contract Commitment Type is a readable display name and not a code. Contract Commitment Type is commonly used for displaying and aggregating the types of commitments the practitioner has made, stated in provider-specific terms.

The ContractCommitmentType column adheres to the following requirements:

* ContractCommitmentType MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentType MUST be of type String.
* ContractCommitmentType MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentType MUST NOT be null.
* ContractCommitmentType MUST be a consistent, readable display value.

## Column ID

ContractCommitmentType

## Display Name

Contract Commitment Type

## Description

A provider-assigned name to identify the type of *contract commitment*.

## Content Constraints

| Constraint      | Value            |
| :-------------- | :--------------- |
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | False            |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
