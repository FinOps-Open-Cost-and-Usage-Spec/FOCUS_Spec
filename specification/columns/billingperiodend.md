# Billing Period End

Billing Period End represents the end date and time of the [*billing period*](#glossary:billing-period).

The BillingPeriodEnd column MUST be present in the billing data. This column MUST be of type Date/Time and MUST NOT contain null values. BillingPeriodEnd column MUST conform to the [Date/Time Format](#date/timeformat). The sum of the [BilledCost](#billedcost) column for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The end date and time of the *billing period*.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Dimension                            |
| FOCUS Essential | True                                 |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
