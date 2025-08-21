# Contract Commitment Description

Contract Commitment Description provides a high-level context of a [*contract commitment*](#glossary:contractcommitment) without requiring additional discovery. Contract Commitment Description is a self-contained summary of the contract commitment's terms, which may not be sufficiently described by the other columns of the Contract Commitment dataset.

The ContractCommitmentDescription column adheres to the following requirements:

* ContractCommitmentDescription MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentDescription MUST be of type String.
* ContractCommitmentDescription MUST conform to [StringHandling](#stringhandling) requirements.
* ContractCommitmentDescription SHOULD NOT be null.
* ContractCommitmentDescription maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

ContractCommitmentDescription

## Display Name

Contract Commitment Description

## Description

The self-contained summary of the *contract commitment's* terms.

## Content Constraints

|    Constraint   |      Value       |
|:----------------|:-----------------|
| Column type     | Dimension        |
| Feature level   | Mandatory        |
| Allows nulls    | True             |
| Data type       | String           |
| Value format    | \<not specified> |

## Introduced (version)

1.3
