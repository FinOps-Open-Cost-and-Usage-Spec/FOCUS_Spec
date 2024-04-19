# Charge Period End

Charge Period End represents the end date and time of the [*charge period*](#glossary:chargeperiod).

The ChargePeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values.

ChargePeriodEnd column MUST conform to an [Exclusive](#glossary:exclusivebound) [Date/Time Format](#date/timeformat) requirements.

For example, a time period where ChargePeriodStart is '2024-01-01T00:00:00Z' and ChargePeriodEnd is '2024-01-02T00:00:00Z' only includes charges for January 1, given ChargePeriodEnd is *excluded* from the period.

## Column ID

ChargePeriodEnd

## Display Name

Charge Period End

## Description

The exclusive, end date and time of a *charge period*.

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
