# Billing Period End

Billing period represents the time window for which an organization has or will receive an invoice for. The time window is inclusive of the start date and exclusive of the end date.

Billing Period End represents the end date and time of the billing period.

The BillingPeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values. BillingPeriodEnd column MUST conform to [FOCUS Date/Time Format](#date/timeformat). The sum of the Billed Cost metric for rows in a given billing period MUST match the sum of the invoices received for that billing period for a billing account.

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The end date and time of the billing period.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column Required | True                                 |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
