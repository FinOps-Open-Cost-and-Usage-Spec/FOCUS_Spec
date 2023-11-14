# Charge Period End

Charge period represents the time window in which a charge was incurred. The time window is inclusive of the charge period start date and exclusive of the charge period end date. A charge can start and/or end at any time within a charge period window. The charge period for continuous usage should match the time granularity of the dataset (e.g., 1 hour for hourly, 1 day for daily).

Charge Period End represents the end date and time of the charge period.

The ChargePeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values. ChargePeriodEnd column MUST conform to [FOCUS Date/Time Format](#date/timeformat).

## Column ID

ChargePeriodEnd

## Display name

Charge Period End

## Description

The end date and time of a charge period.

## Content constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column Required | True                                 |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
