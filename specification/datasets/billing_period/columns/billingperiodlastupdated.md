# Billing Period Last Updated

A Billing Period Created is the timestamp when the [Billing Period](#datasets.billingperiod) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a record, particularly if corrections or status changes have been applied to the record after its initial creation.

## Requirements

BillingPeriodLastUpdated adheres to the following requirements:

* BillingPeriodLastUpdated MUST be of type Date/Time.
* BillingPeriodLastUpdated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* BillingPeriodLastUpdated MUST NOT be null.
* BillingPeriodLastUpdated MUST represent the most recent moment in time when any column value of the Billing Period record was created or modified.
* BillingPeriodLastUpdated MUST be greater than or equal to [BillingPeriodCreated](#datasets.billingperiod.billingperiodcreated).

## Column ID

BillingPeriodLastUpdated

## Display Name

Billing Period Last Updated

## Description

The timestamp when the Billing Period record was last updated.

## Content constraints

|    Constraint    |              Value             |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Date/Time                        |
| Value format    | [DateTime Format](#attributes.date/timeformat) |

## Introduced (version)

1.4
