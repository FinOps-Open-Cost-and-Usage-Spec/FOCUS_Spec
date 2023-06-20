# Billing Period End

Billing period represents the time window for which you have or will receive an invoice for. The time window is inclusive of the billing period start date and exclusive of the billing period end date. 

The BillingPeriodEnd column MUST be present in the billing data and MUST NOT be null. The sum of the Billed Cost for line items in a given billing period MUST match the sum of the invoices received for that billing period. BillingPeriodEnd values MUST conform to [Date/Time Requirements](#date/timerequirements).

## Column ID

BillingPeriodEnd

## Display Name

Billing Period End

## Description

The time period which an invoice for the billed cost would be generated for. 

## Content Constraints

| Constraint   | True                                                                 |
|--------------|----------------------------------------------------------------------|
| Data type    | Datetime                                                             |
| Allows nulls | False                                                                |
| Value format | Meets [FOCUS Date/Time Format] (#date/timerequirements) requirements |

## Introduced (version)

0.5
