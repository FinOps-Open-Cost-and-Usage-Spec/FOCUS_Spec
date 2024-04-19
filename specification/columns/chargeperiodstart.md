# Charge Period Start

Charge Period Start represents the starting date and time of the [*charge period*](#glossary:chargeperiod).

The ChargePeriodStart column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values.

ChargePeriodStart column MUST conform to an [Inclusive](#glossary:inclusivebound) [Date/Time Format](#date/timeformat) requirements and MUST be an [*inclusive*](#glossary:inclusivedatetime) value.

For example, a time period where ChargePeriodStart is '2024-01-01T00:00:00Z' and ChargePeriodEnd is '2024-01-02T00:00:00Z' only includes charges for January 1, given ChargePeriodStart is *included* within the period.

## Column ID

ChargePeriodStart

## Display Name

Charge Period Start

## Description

The inclusive, beginning date and time of a *charge period*.

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
