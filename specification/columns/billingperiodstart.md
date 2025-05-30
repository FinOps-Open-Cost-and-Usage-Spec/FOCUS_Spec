# Billing Period Start

Billing Period Start represents the [*inclusive start bound*](#glossary:inclusivestartbound) of a [*billing period*](#glossary:billing-period). For example, a time period where Billing Period Start is '2024-01-01T00:00:00Z' and [Billing Period End](#billingperiodend) is '2024-02-01T00:00:00Z' includes [*charges*](#glossary:charge) for January since Billing Period Start represents the *inclusive start bound*, but does not include *charges* for February since BillingPeriodEnd represents the [*exclusive end bound*](#glossary:exclusiveendbound).

The BillingPeriodStart column adheres to the following requirements:

* BillingPeriodStart MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BillingPeriodStart MUST be of type Date/Time.
* BillingPeriodStart MUST conform to [DateTimeFormat](#date/timeformat) requirements.
* BillingPeriodStart MUST NOT be null.
* BillingPeriodStart MUST be the *inclusive start bound* of the *billing period*.

## Column ID

BillingPeriodStart

## Display Name

Billing Period Start

## Description

The *inclusive start bound* of a *billing period*.

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
