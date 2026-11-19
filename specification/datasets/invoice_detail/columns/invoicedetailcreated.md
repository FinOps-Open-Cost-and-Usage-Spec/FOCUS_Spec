# Invoice Detail Created

[Invoice Detail Created](#col) is the timestamp when the [Invoice Detail](#ds) record was first created. This timestamp facilitates auditability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish between the time of service consumption and the time of financial record generation.

## Requirements

[InvoiceDetailCreated](#col) MUST adhere to the following requirements:

* [InvoiceDetailCreated](#col) MUST be of type Date/Time.
* [InvoiceDetailCreated](#col) MUST conform to [DateTimeFormat](#attr) requirements.
* [InvoiceDetailCreated](#col) MUST NOT be null.
* [InvoiceDetailCreated](#col) MUST represent the moment in time the [InvoiceDetail](#ds) record was instantiated.
* [InvoiceDetailCreated](#col) for a given [BillingPeriodStart](#col) and [InvoiceIssuerName](#col) MUST be earlier than or equal to [BillingPeriod.BillingPeriodLastUpdated](#col:BillingPeriod.BillingPeriodLastUpdated) for the same [BillingPeriod.BillingPeriodStart](#col:BillingPeriod.BillingPeriodStart) and [BillingPeriod.InvoiceIssuerName](#col:BillingPeriod.InvoiceIssuerName) when [BillingPeriod.BillingPeriodStatus](#col:BillingPeriod.BillingPeriodStatus) is ["Closed"](#val:BillingPeriod.BillingPeriodStatus).

## Column ID

InvoiceDetailCreated

## Display Name

Invoice Detail Created

## Description

The timestamp when the [Invoice Detail](#ds) record was first created.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Invoice Detail](#ds)                           |
| Operating model conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | False                                           |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attr)                       |

## Version Introduced

1.4
