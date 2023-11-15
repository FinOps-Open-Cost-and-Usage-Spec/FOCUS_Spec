# Billing Period End


Billing Period End represents the end date and time of the *billing period*.

The BillingPeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values. BillingPeriodEnd column MUST conform to [FOCUS Date/Time Format](#date/timeformat). The sum of the [Billed Cost](#billedcost) column for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a billing account.

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The end date and time of the *billing period*.

## Content Constraints

| Constraint      | Value                                                         |
|:----------------|:--------------------------------------------------------------|
| Column Required | True                                                          |
| Data type       | Date/Time                                                     |
| Allows nulls    | False                                                         |
| Value format    | Meets [FOCUS Date/Time Format](#date/timeformat) requirements |

## Introduced (version)

0.5
