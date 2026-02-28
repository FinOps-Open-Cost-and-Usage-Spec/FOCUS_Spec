# Billing Period Status

A Billing Period Status represents the state of the billing period (i.e., open or closed). This status helps FinOps practitioners determine if the [Cost and Usage](#datasets.costandusage) data for a given period is preliminary and subject to change, or if it is finalized and ready for formal financial reporting and showback/chargeback processes.

## Requirements

BillingPeriodStatus MUST adhere to the following requirements:

* BillingPeriodStatus MUST be of type String.
* BillingPeriodStatus MUST NOT be null.
* BillingPeriodStatus MUST be one of the [allowed values](#datasets.billingperiod.billingperiodstatus.allowed-values).
* BillingPeriodStatus MUST represent the state of the billing period identified by [BillingPeriodStart](#datasets.billingperiod.billingperiodstart) and [BillingPeriodEnd](#datasets.billingperiod.billingperiodend).

## Implementation Context

While the transition from Open to Closed typically signifies the end of a billing cycle, the billing period may reopen in scenarios such as:

* Retroactive adjustments: an invoice issuer generates credits or corrections for a period previously marked as finalized.
* Audit corrections: discrepancies are discovered during financial reconciliation that require the data to be re-processed.
* Late-arriving usage: occasional delays in usage reporting necessitate a revision of the final invoice.

FinOps tools and reporting engines should be designed to detect these transitions and trigger updates to downstream showback or chargeback reports to ensure financial accuracy.

For more information, please see the [Correction Handling](#attributes.correctionhandling) attribute.

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
