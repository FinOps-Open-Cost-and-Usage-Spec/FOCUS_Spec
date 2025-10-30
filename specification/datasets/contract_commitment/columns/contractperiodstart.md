# Contract Period Start

Contract Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*contract period*](#glossary:contractperiod). For example, a time period where Contract Period Start is '2024-01-01T00:00:00Z' and [Contract Period End](#contractperiodend) is '2025-01-01T00:00:00Z' includes January 1 2024 since Contract Period Start represents the *inclusive start bound*, but does not include January 2 2025 since Contract Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound).

The ContractPeriodStart column adheres to the following requirements:

* ContractPeriodStart MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractPeriodStart MUST be of type Date/Time.
* ContractPeriodStart MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* ContractPeriodStart MUST NOT be null.
* ContractPeriodStart MUST be the *inclusive start bound* of the effective period of the *contract*.

## Column ID

ContractPeriodStart

## Display Name

Contract Period Start

## Description

The *inclusive start bound* of a *contract period*.

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
