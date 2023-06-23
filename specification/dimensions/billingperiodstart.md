# Billing Period Start

Billing period represents the time window for which an organization has or will receive an invoice for. The time window is inclusive of the start date and exclusive of the end date.

Billing Period Start represents the start date and time of the billing period.

The BillingPeriodStart column MUST be present in the billing data. This column MUST be of type String and MUST NOT contain null values. BillingPeriodStart column MUST conform to [FOCUS Date/Time Format](#datetimeformat). The sum of the Billed Cost metric for line items in a given billing period MUST match the total cost of the invoices received for that billing period.

## Column ID

BillingPeriodStart

## Display Name

Billing Period Start

## Description

The beginning of a billing period.

## Content Constraints

| Constraint      | Value                                                        |
|:----------------|:-------------------------------------------------------------|
| Column Required | True                                                         |
| Data type       | Datetime                                                     |
| Allows nulls    | False                                                        |
| Value format    | Meets [FOCUS Date/Time Format](#datetimeformat) requirements |

## Introduced (version)

0.5
