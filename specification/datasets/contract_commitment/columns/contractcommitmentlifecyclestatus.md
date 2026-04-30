# Contract Commitment Lifecycle Status

Contract Commitment Lifecycle Status represents the current lifecycle state of a [*contract commitment*](#glossary:contract-commitment). The Status determines the applicability of the commitment to a specific period of [Cost and Usage](#datasets.costandusage) data.

## Requirements

ContractCommitmentLifecycleStatus MUST adhere to the following requirements:

* ContractCommitmentLifecycleStatus MUST be of type String.
* ContractCommitmentLifecycleStatus MUST NOT be null.
* ContractCommitmentLifecycleStatus MUST be one of the allowed values.
* When a contract commitment record is modified in a way that requires a new [ContractCommitmentID](#datasets.contractcommitment.contractcommitmentid), ContractCommitmentLifecycleStatus for the previous record MUST be "Superseded".

## Allowed Values

| Value | Sort Order | Description |
| :--- | :--- | :--- |
| Proposed | 10 | The commitment is being negotiated or modeled; it has no legal or financial impact on current data. |
| Pending | 20 | The commitment is finalized or signed, but the effective start date is in the future. |
| Active | 30 | The commitment is currently in effect, and it has remaining value. |
| Exhausted | 40 | The commitment is currently in effect, but its value has been fully consumed. |
| Expired | 50 | The commitment is no longer active because it reached its scheduled end date. |
| Canceled | 60 | The commitment is no longer active because it was terminated by either party prior to its scheduled end date. |
| Superseded | 70 | The commitment is no longer active because it was replaced by a newer version prior to its scheduled end date. |

## Column ID

ContractCommitmentLifecycleStatus

## Display Name

Contract Commitment Lifecycle Status

## Description

The current lifecycle state of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

## Introduced (version)

1.4