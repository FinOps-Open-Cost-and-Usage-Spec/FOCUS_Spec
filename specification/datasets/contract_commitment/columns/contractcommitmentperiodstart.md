# Contract Commitment Period Start

Contract Commitment Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*contract commitment period*](#glossary:contractcommitmentperiod). For example, a time period where Contract Commitment Period Start is '2024-01-01T00:00:00Z' and [Contract Commitment End](#contractcommitmentperiodend) is '2025-01-01T00:00:00Z' includes January 1 2024 since Contract Commitment Period Start represents the *inclusive start bound*, but does not include *charges* for January 2 2025 since Contract Commitment Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound).

The ContractCommitmentPeriodStart column adheres to the following requirements:

* ContractCommitmentPeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentPeriodStart MUST be of type Date/Time.
* ContractCommitmentPeriodStart MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* ContractCommitmentPeriodStart MUST NOT be null.
* ContractCommitmentPeriodStart MUST be the *inclusive start bound* of the effective period of the *contract commitment*.

## Column ID

ContractCommitmentPeriodStart

## Display Name

Contract Commitment Period Start

## Description

The *inclusive start bound* of a *contract commitment period*.

## Content constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Dimension                            |
| Feature level   | Mandatory                            |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

1.3
