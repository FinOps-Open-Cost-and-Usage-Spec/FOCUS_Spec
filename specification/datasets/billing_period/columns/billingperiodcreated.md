# Billing Period Created

Billing Period Created is the timestamp when the [Billing Period](#datasets.billingperiod) record was first created. This timestamp facilitates auditability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish between the time of service consumption and the time of financial record generation.

## Requirements

BillingPeriodCreated MUST adhere to the following requirements:

* BillingPeriodCreated MUST be of type Date/Time.
* BillingPeriodCreated MUST NOT be null.
* BillingPeriodCreated MUST represent the moment in time the [Billing Period](#datasets.billingperiod) record was instantiated.

## Column ID

BillingPeriodCreated

## Display Name

Billing Period Created

## Description

The timestamp when the *Billing Period* record was first created.

## Content constraints

|    Constraint   |              Value              |
|:----------------|:--------------------------------|
| Column type     | Dimension                       |
| Feature level   | Mandatory                       |
| Allows nulls    | False                           |
| Data type       | Date/Time                        |
| Value format    | [Date/Time Format](#attributes.date/timeformat) |

## Introduced (version)

1.4
