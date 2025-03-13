# Billing Period End

Billing Period End represents the [*exclusive end bound*](#glossary:exclusiveendbound) of a [*billing period*](#glossary:billing-period). For example, a time period where [Billing Period Start](#billingperiodstart) is '2024-01-01T00:00:00Z' and Billing Period End is '2024-02-01T00:00:00Z' includes charges for January since Billing Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound), but does not include charges for February since Billing Period End represents the *exclusive end bound*.

The BillingPeriodEnd column adheres to the following requirements:

* BillingPeriodEnd MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodEnd MUST be of type Date/Time.
* BillingPeriodEnd MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* BillingPeriodEnd MUST NOT be null.
* BillingPeriodEnd MUST be the *exclusive end bound* of the *billing period*.

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The *exclusive end bound* of a *billing period*.

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
