# Contract Commitment Period End

Contract Commitment Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*contract commitment period*](#glossary:contractcommitmentperiod). For example, a time period where [Contract Commitment Period Start](#datasets.contractcommitment.contractperiodstart) is '2024-01-01T00:00:00Z' and Contract Commitment Period End is '2024-01-02T00:00:00Z' includes January 1 2024 since Contract Commitment Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include January 1 2025 since Contract Commitment Period End represents the *exclusive end bound*.

## Requirements

ContractCommitmentPeriodEnd MUST adhere to the following requirements:

* ContractCommitmentPeriodEnd MUST be of type Date/Time.
* ContractCommitmentPeriodEnd MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* ContractCommitmentPeriodEnd MUST NOT be null.
* ContractCommitmentPeriodEnd MUST be the *exclusive end bound* of the effective period of the *contract commitment*.

## Column ID

ContractCommitmentPeriodEnd

## Display Name

Contract Commitment Period End

## Description

The *exclusive end bound* of a *contract commitment period*.

## Content Constraints

| Constraint      | Value                                                |
|:----------------|:-----------------------------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension                                            |
| Feature level   | Mandatory                                            |
| Allows nulls    | False                                                |
| Data type       | Date/Time                                            |
| Value format    | [Date/Time Format](#attributes.date/timeformat)      |

## Introduced (version)

1.3
