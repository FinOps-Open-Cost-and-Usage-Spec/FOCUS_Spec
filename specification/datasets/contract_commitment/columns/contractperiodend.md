# Contract Period End

Contract Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*contract period*](#glossary:contractperiod). For example, a time period where [Contract Period Start](#contractperiodstart) is '2024-01-01T00:00:00Z' and Contract Period End is '2024-01-02T00:00:00Z' includes January 1 2024 since Contract Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include January 1 2025 since Contract Period End represents the *exclusive end bound*.

The ContractPeriodEnd column adheres to the following requirements:

* ContractPeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractPeriodEnd MUST be of type Date/Time.
* ContractPeriodEnd MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* ContractPeriodEnd MUST NOT be null.
* ContractPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract*.

## Column ID

ContractPeriodEnd

## Display Name

Contract Period End

## Description

The *exclusive end bound* of a *contract period*.

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
