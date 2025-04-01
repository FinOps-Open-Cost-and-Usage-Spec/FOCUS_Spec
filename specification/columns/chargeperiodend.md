# Charge Period End

Charge Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*charge period*](#glossary:chargeperiod). For example, a time period where [Charge Period Start](#chargeperiodstart) is '2024-01-01T00:00:00Z' and Charge Period End is '2024-01-02T00:00:00Z' includes charges for January 1 since Charge Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include charges for January 2 since Charge Period End represents the *exclusive end bound*.

The ChargePeriodEnd column adheres to the following requirements:

* ChargePeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ChargePeriodEnd MUST be of type Date/Time.
* ChargePeriodEnd MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* ChargePeriodEnd MUST NOT be null.
* ChargePeriodEnd MUST be the *exclusive end bound* of the effective period of the charge.

## Column ID

ChargePeriodEnd

## Display Name

Charge Period End

## Description

The *exclusive end bound* of a *charge period*.

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
