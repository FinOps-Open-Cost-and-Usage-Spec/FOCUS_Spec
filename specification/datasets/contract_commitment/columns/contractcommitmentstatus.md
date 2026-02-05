# Contract Commitment Status

Contract Commitment Status represents the current lifecycle state of a [*contract commitment*](#glossary:contract-commitment). The Status determines the applicability of the commitment to a specific period of [Cost and Usage](#datasets.costandusage) data.

## Requirements

ContractCommitmentStatus adheres to the following requirements:

* ContractCommitmentStatus MUST be of type String.
* ContractCommitmentStatus MUST NOT be null.
* ContractCommitmentStatus MUST be one of the allowed values.
* When a contract commitment record is modified in a way that requires a new [ContractCommitmentID](#datasets.contractcommitment.contractcommitmentid), ContractCommitmentStatus for the previous record MUST be "Superseded".

## Column ID

ContractCommitmentStatus

## Display Name

Contract Commitment Status

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

## Allowed Values

| Value | Sort Order | Description |
| :--- | :--- | :--- |
| Proposed | 10 | The commitment is being negotiated or modeled; it has no legal or financial impact on current data. |
| Pending | 20 | The commitment is finalized or signed, but the effective start date is in the future. |
| Active | 30 | The commitment is currently in effect and its terms should be applied to applicable activity. |
| Expired | 40 | The commitment reached its scheduled end date and is no longer providing benefits. |
| Canceled | 50 | The commitment was terminated by either party prior to its scheduled end date. |
| Superseded | 60 | The commitment has been replaced by a newer version of the record or a successor agreement. |

## Introduced (version)

1.4