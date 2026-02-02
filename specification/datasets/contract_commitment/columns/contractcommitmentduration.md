# Contract Commitment Duration

Contract Commitment Duration represents the total calendar length of a [*contract commitment*](#glossary:contract-commitment), from [start date](#datasets.contractcommitment.datestart) to [end date](#datasets.contractcommitment.contractcommitmentdateend). 

The value follows a structured format of [Numeric Value] [Unit], representing the full lifespan of the agreement; see below for more information.

## Expected Format

"[Numeric Value] [Unit]"
* [Numeric Value]: A positive integer.
* [Unit]: A standardized unit of time, singular or plural (e.g., Hour, Year, Years).

## Standard Units

The following units should be used for the representation of time:

* Minute(s)
* Hour(s)
* Day(s)
* Week(s)
* Month(s)
* Quarter(s)
* Year(s)

## Requirements

ContractCommitmentDuration adheres to the following requirements:

* ContractCommitmentDuration MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentDuration MUST be of type String.
* ContractCommitmentDuration MUST NOT be null.
* ContractCommitmentDuration MUST adhere to the expected format of "[Numeric Value] [Unit]", where [Numeric Value] is a positive integer, and [Unit] is a standardized unit of time, either singular or plural (e.g., Hour, Year, Years).
* ContractCommitmentDuration MUST be calculated as the time elapsed between ContractCommitmentPeriodStart and ContractCommitmentPeriodEnd.

## Column ID

ContractCommitmentDuration

## Display Name

Contract Commitment Duration

## Description

Represents the total calendar length of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Expected format |

## Introduced (version)

1.4
