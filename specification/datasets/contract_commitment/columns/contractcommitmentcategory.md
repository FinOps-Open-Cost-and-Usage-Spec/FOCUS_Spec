# Contract Commitment Category

[Contract Commitment Category](#col) represents the highest-level classification of a [contract commitment](#term) based on the nature of how it is applied to a charge. [Contract Commitment Category](#col) is commonly used to identify and distinguish between categories of contract commitments that may require different handling.

## Requirements

[ContractCommitmentCategory](#col) MUST adhere to the following requirements:

* [ContractCommitmentCategory](#col) MUST be of type String.
* [ContractCommitmentCategory](#col) MUST NOT be null.
* [ContractCommitmentCategory](#col) MUST be one of the allowed values.

## Allowed Values

| Value   | Description                                                              |
|:--------|:-------------------------------------------------------------------------|
| Spend   | Contract commitments that require a predetermined amount of spend. |
| Usage   | Contract commitments that require a predetermined amount of usage. |

## Column ID

ContractCommitmentCategory

## Display Name

Contract Commitment Category

## Description

Represents the highest-level classification of a [contract commitment](#term) based on the nature of how it is applied to a charge.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | Allowed values                                       |

## Version Introduced

1.3
