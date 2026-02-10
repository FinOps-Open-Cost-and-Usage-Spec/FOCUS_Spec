# Billing Period Status

A Billing Period Status represents the state of the billing period (i.e., open or closed). This status helps FinOps practitioners determine if the [Cost and Usage](#datasets.costandusage) data for a given period is preliminary and subject to change, or if it is finalized and ready for formal financial reporting and showback/chargeback processes.

## Requirements

BillingPeriodStatus adheres to the following requirements:

* BillingPeriodStatus MUST be of type String.
* BillingPeriodStatus MUST NOT be null.
* BillingPeriodStatus MUST be one of the [allowed values](#datasets.billingperiod.billingperiodstatus.allowed-values).
* BillingPeriodStatus MUST represent the state of the billing period identified by [BillingPeriodStart](#datasets.billingperiod.billingperiodstart) and [BillingPeriodEnd](#datasets.billingperiod.billingperiodend).

## Column ID

BillingPeriodStatus

## Display Name

Billing Period Status

## Description

The state of the billing period (i.e., open or closed).

## Content Constraints

| Constraint    | Value                               |
| :------------ | :---------------------------------- |
| Column type   | Dimension                           |
| Feature level | Mandatory                           |
| Allows nulls  | False                               |
| Data type     | String                              |
| Value format  | Allowed values                      |

## Allowed Values

| Value    | Description                                                                                                                                      |
| :------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| Open   | The billing period is currently active or still being processed. Charges may continue to be added or revised.        |
| Closed | The billing period has ended, and all charges have been finalized and issued via invoice. |

## Introduced (version)

1.4
