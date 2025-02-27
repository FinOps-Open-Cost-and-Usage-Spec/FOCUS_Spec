# Billing Period End

Billing Period End represents the [*exclusive*](#glossary:exclusivebound) end date and time of a [*billing period*](#glossary:billing-period). For example, a time period where [BillingPeriodStart](#glossary:billingperiodstart) is '2024-01-01T00:00:00Z' and BillingPeriodEnd is '2024-02-01T00:00:00Z' includes charges for January, since BillingPeriodStart is [*inclusive*](#glossary:inclusivebound), but does not include charges for February since BillingPeriodEnd is *exclusive*.

The BillingPeriodEnd column adheres to the following requirements:

* BillingPeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodEnd MUST be of type Date/Time.
* BillingPeriodEnd MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* BillingPeriodEnd MUST NOT be null.
* BillingPeriodEnd MUST be the *exclusive ending bound* of the *billing period*.
* The sum of [BilledCost](#billedcost) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The [*exclusive*](#glossary:exclusivebound) end date and time of a [*billing period*](#glossary:billing-period).

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Dimension                            |
| Feature level   | Mandatory                            |
| Allows nulls    | False                                |
| Data type       | Date/Time                            |
| Value format    | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
