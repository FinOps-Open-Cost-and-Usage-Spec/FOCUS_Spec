# Charge Period End

Charge Period End represents the end date and time of the [*charge period*](#glossary:chargeperiod).

The ChargePeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values. ChargePeriodEnd column MUST conform to [Date/Time Format](#date/timeformat) requirements.

## Column ID

ChargePeriodEnd

## Display Name

Charge Period End

## Description

The end date and time of a *charge period*.

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
