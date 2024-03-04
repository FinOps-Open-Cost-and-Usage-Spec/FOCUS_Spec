# Charge Period Start

Charge Period Start represents the starting date and time of the [*charge period*](#glossary:chargeperiod).

The ChargePeriodStart column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values. ChargePeriodStart column MUST conform to [Date/Time Format](#date/timeformat).

## Column ID

ChargePeriodStart

## Display name

Charge Period Start

## Description

The beginning date and time of a *charge period*.

## Content constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Dimension                            |
| FOCUS Essential | True                                 |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
