# Contract Commitment Category

Contract Commitment Category represents the highest-level classification of a [*contract commitment*](#glossary:contract-commitment) based on the nature of how it is applied to a charge. Contract Commitment Category is commonly used to identify and distinguish between categories of contract commitments that may require different handling.

## Requirements

ContractCommitmentCategory adheres to the following requirements:

* ContractCommitmentCategory MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentCategory MUST be of type String.
* ContractCommitmentCategory MUST NOT be null.
* ContractCommitmentCategory MUST be one of the allowed values.

## Column ID

ContractCommitmentCategory

## Display Name

Contract Commitment Category

## Description

Represents the highest-level classification of a *contract commitment* based on the nature of how it is applied to a charge.

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value   | Description                                                              |
|:--------|:-------------------------------------------------------------------------|
| Spend   | Contract commitments that require a predetermined amount of spend.       |
| Usage   | Contract commitments that require a predetermined amount of usage.       |

## Introduced (version)

1.3
