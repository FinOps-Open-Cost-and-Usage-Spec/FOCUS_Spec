# Contract Commitment Description

[Contract Commitment Description](#col) provides a high-level context of a [contract commitment](#term) without requiring additional discovery. [Contract Commitment Description](#col) is a self-contained summary of the contract commitment's terms, which may not be sufficiently described by the other columns of the [Contract Commitment](#ds) dataset.

## Requirements

[ContractCommitmentDescription](#col) MUST adhere to the following requirements:

* [ContractCommitmentDescription](#col) MUST be of type String.
* [ContractCommitmentDescription](#col) MUST conform to [StringHandling](#attr) requirements.
* [ContractCommitmentDescription](#col) SHOULD NOT be null.
* [ContractCommitmentDescription](#col) maximum length SHOULD be provided in the corresponding FOCUS Metadata Schema.

## Column ID

ContractCommitmentDescription

## Display Name

Contract Commitment Description

## Description

The self-contained summary of the *contract commitment's* terms.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | True                                                 |
| Data type                  | String                                               |
| Value format               | \<not specified>                                     |

## Version Introduced

1.3
