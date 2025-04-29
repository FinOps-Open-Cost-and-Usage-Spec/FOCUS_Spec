# Charge Period Start

Charge Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*charge period*](#glossary:chargeperiod). For example, a time period where Charge Period Start is '2024-01-01T00:00:00Z' and [Charge Period End](#chargeperiodend) is '2024-01-02T00:00:00Z' includes [*charges*](#glossary:charge) for January 1 since Charge Period Start represents the *inclusive start bound*, but does not include *charges* for January 2 since Charge Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound).

The ChargePeriodStart column adheres to the following requirements:

* ChargePeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargePeriodStart MUST be of type Date/Time.
* ChargePeriodStart MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* ChargePeriodStart MUST NOT be null.
* ChargePeriodStart MUST be the *inclusive start bound* of the effective period of the *charge*.

## Column ID

ChargePeriodStart

## Display Name

Charge Period Start

## Description

The *inclusive start bound* of a *charge period*.

## Content constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Dimension                            |
| Feature level   | Mandatory                            |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
