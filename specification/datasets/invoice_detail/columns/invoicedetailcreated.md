# Invoice Detail Created

Invoice Detail Created is the timestamp when the [Invoice Detail](#datamodel.invoicedetail) record was first created. This timestamp facilitates auditability of the charge and invoice lifecycle, allowing the FinOps practitioner to distinguish between the time of service consumption and the time of financial record generation.

## Requirements

InvoiceDetailCreated MUST adhere to the following requirements:

* InvoiceDetailCreated MUST be of type Date/Time.
* InvoiceDetailCreated MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* InvoiceDetailCreated MUST NOT be null.
* InvoiceDetailCreated MUST represent the moment in time the Invoice Detail record was instantiated.
* InvoiceDetailCreated for a given [BillingPeriodStart](#datamodel.invoicedetail.billingperiodstart) and [InvoiceIssuerName](#datamodel.invoicedetail.invoiceissuername) MUST be earlier than or equal to [BillingPeriod.BillingPeriodLastUpdated](#datamodel.billingperiod.billingperiodlastupdated) for the same [BillingPeriod.BillingPeriodStart](#datamodel.billingperiod.billingperiodstart) and [BillingPeriod.InvoiceIssuerName](#datamodel.billingperiod.invoiceissuername) when [BillingPeriod.BillingPeriodStatus](#datamodel.billingperiod.billingperiodstatus) is "Closed".

## Column ID

InvoiceDetailCreated

## Display Name

Invoice Detail Created

## Description

The timestamp when the Invoice Detail record was first created.

## Content Constraints

| Constraint                 | Value                                           |
| :------------------------- | :---------------------------------------------- |
| Dataset                    | [Invoice Detail](#datamodel.invoicedetail)      |
| Operating Model Conditions | Not applicable                                  |
| Column type                | Dimension                                       |
| Feature level              | Mandatory                                       |
| Allows nulls               | False                                           |
| Data type                  | Date/Time                                       |
| Value format               | [Date/Time Format](#attributes.date/timeformat) |

## Version Introduced

1.4
