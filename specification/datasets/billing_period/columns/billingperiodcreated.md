# Billing Period Created

[Billing Period Created](#col) is the timestamp when the [Billing Period](#ds) record was first created. This timestamp facilitates auditability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish between the time of service consumption and the time of financial record generation.

## Requirements

[BillingPeriodCreated](#col) MUST adhere to the following requirements:

* [BillingPeriodCreated](#col) MUST be of type Date/Time.
* [BillingPeriodCreated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [BillingPeriodCreated](#col) MUST NOT be null.
* [BillingPeriodCreated](#col) MUST represent the moment in time the [BillingPeriod](#ds) record was instantiated.

## Column ID

BillingPeriodCreated

## Display Name

Billing Period Created

## Description

The timestamp when the [Billing Period](#ds) record was first created.

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
