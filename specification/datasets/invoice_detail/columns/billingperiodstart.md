# Billing Period Start

Billing Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*billing period*](#glossary:billing-period). For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and [Billing Period End](#datamodel.invoicedetail.billingperiodend) is '2024-02-01T00:00:00Z' includes [*charges*](#glossary:charge) for January since Billing Period Start represents the *inclusive start bound*, but does not include *charges* for February since BillingPeriodEnd represents the [*exclusive end bound*](#glossary:exclusiveendbound).

## Requirements

BillingPeriodStart MUST adhere to the following requirements:

* BillingPeriodStart MUST be of type Date/Time.
* BillingPeriodStart MUST conform to [DateTimeFormat](#attributes.date/timeformat) requirements.
* BillingPeriodStart MUST NOT be null.
* BillingPeriodStart MUST be the *inclusive start bound* of the *billing period*.
* BillingPeriodStart for a given [InvoiceId](#datamodel.invoicedetail.invoiceid) and [InvoiceIssuerName](#datamodel.invoicedetail.invoiceissuername) MUST match [CostAndUsage.BillingPeriodStart](#datamodel.costandusage.billingperiodstart) for the same [CostAndUsage.InvoiceId](#datamodel.costandusage.invoiceid) and [CostAndUsage.InvoiceIssuerName](#datamodel.costandusage.invoiceissuername).

## Column ID

BillingPeriodStart

## Display Name

Billing Period Start

## Description

The *inclusive start bound* of a *billing period*.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Dataset         | [Invoice Detail](#datamodel.invoicedetail)             |
| Operating Model Conditions      | Not applicable                                         |
| Column type     | Dimension                            |
| Feature level   | Mandatory                            |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#attributes.date/timeformat) |

## Version Introduced

1.4
