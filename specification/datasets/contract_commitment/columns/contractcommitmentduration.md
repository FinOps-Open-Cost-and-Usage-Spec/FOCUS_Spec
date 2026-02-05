# Contract Commitment Duration

Contract Commitment Duration represents the total calendar length of a [*contract commitment*](#glossary:contract-commitment), from [start date](#datasets.contractcommitment.datestart) to [end date](#datasets.contractcommitment.contractcommitmentdateend).

The value follows a structured format of [Numeric Value] [Unit], representing the full lifespan of the agreement; see below for more information.

## Expected Format

"[Numeric Value] [Unit]"
* [Numeric Value]: A positive integer.
* [Unit]: A standardized unit of time, singular or plural (e.g., Hour, Year, Years).

## Requirements

ContractCommitmentDuration adheres to the following requirements:

* ContractCommitmentDuration MUST be of type String.
* ContractCommitmentDuration MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentDuration MUST NOT be null.
* ContractCommitmentDuration MUST adhere to the expected format of "[Numeric Value] [Unit]", where [Numeric Value] is a positive integer, and [Unit] is a standardized unit of time, either singular or plural (e.g., Hour, Year, Years).
* ContractCommitmentDuration SHOULD present the unit of time as one of the allowed values.
* ContractCommitmentDuration MUST be calculated as the time elapsed between ContractCommitmentPeriodStart and ContractCommitmentPeriodEnd.
* ContractCommitmentDuration SHOULD present the largest relevant unit of time (e.g., "1 Year" instead of "12 Months").

## Column ID

ContractCommitmentDuration

## Display Name

Contract Commitment Duration

## Description

Represents the total calendar length of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Expected format |

Allowed values:

The following units (either singular or plural) should be used for the representation of time:

| Duration Unit |
| :--- |
| Minute(s) |
| Hour(s) |
| Day(s) |
| Week(s) |
| Month(s) |
| Quarter(s) |
| Year(s) |

## Introduced (version)

1.4
