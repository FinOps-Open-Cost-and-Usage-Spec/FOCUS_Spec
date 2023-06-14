# Billed Cost

The Billed Cost represents a charge inclusive of negotiated discounts that a consumer would be charged for each billing period. Billed Cost does not amortize upfront charges (one-time or recurring). The currency for the value specified in Billed Cost can be found in the [Billing Currency](#billingcurrency) column. Billed Cost is often used to perform FinOps capabilities that require cash-basis accounting such as cost allocation, budgeting, and invoice reconciliation.

The BilledCost column MUST be present in the billing data. This column MUST be a numeric value of type Decimal and MUST NOT contain null values. The aggregated BilledCost for a billing period MUST match the charge received on the invoice for the same billing period.

## Column ID

BilledCost

## Display name

Billed Cost

## Description

A charge inclusive of negotiated discounts that a consumer would be charged for each billing period.

## Content constraints

|    Constraint   |      Value      |
|:----------------|:----------------|
| Column required | True            |
| Data type       | Decimal         |
| Allows nulls    | False           |
| Value format    | Numeric value   |

## Introduced (version)

0.5
