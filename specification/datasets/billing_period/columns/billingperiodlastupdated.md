# Billing Period Last Updated

[Billing Period Last Updated](#col) is the timestamp when the [Billing Period](#ds) record was last updated. This timestamp helps FinOps practitioners ensure that they are working with the most current version of a record, particularly if corrections or status changes have been applied to the record after its initial creation.

## Requirements

[BillingPeriodLastUpdated](#col) MUST adhere to the following requirements:

* [BillingPeriodLastUpdated](#col) MUST be of type Date/Time.
* [BillingPeriodLastUpdated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [BillingPeriodLastUpdated](#col) MUST NOT be null.
* [BillingPeriodLastUpdated](#col) MUST represent the most recent moment in time when any column value of the [BillingPeriod](#ds) record was created or modified.
* [BillingPeriodLastUpdated](#col) MUST be greater than or equal to [BillingPeriodCreated](#col).

## Column ID

BillingPeriodLastUpdated

## Display Name

Billing Period Last Updated

## Description

The timestamp when the Billing Period record was last updated.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Billing Period](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | False                                           |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attr)                       |

## Version Introduced

1.4
