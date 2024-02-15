# Billing Period Start

Billing Period Start represents the start date and time of the [*billing period*](#glossary:billing-period).

The BillingPeriodStart column MUST be present in all FOCUS-compatible billing datasets. This column MUST be of type Date/Time and MUST NOT contain null values. BillingPeriodStart column MUST conform to the [Date/Time Format](#date/timeformat). The sum of the [BilledCost](#billedcost) metric for [*rows*](#glossary:row) in a given *billing period* MUST match the sum of the invoices received for that *billing period* for a [*billing account*](#glossary:billing-account).

## Column ID

BillingPeriodStart

## Display Name

Billing Period Start

## Description

The beginning date and time of the *billing period*.

## Content Constraints

| Constraint          | Value                                |
|:--------------------|:-------------------------------------|
| Column type         | Dimension                            |
| Dataset requirement | Both                                 |
| Allows nulls        | False                                |
| Data type           | Date/Time                            |
| Value format        | [Date/Time Format](#date/timeformat) |

## Introduced (version)

0.5
