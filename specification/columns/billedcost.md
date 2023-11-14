# Billed Cost

The Billed Cost represents a charge serving as the basis for invoicing, inclusive of the impacts of all reduced rates and discounts while excluding the amortization of relevant purchases (one-time or recurring) paid to cover future eligible charges. This cost is denominated in the [Billing Currency](#billingcurrency). The Billed Cost is commonly used to perform FinOps capabilities that require cash-basis accounting such as cost allocation, budgeting, and invoice reconciliation.

The BilledCost column MUST be present in the billing data and MUST NOT be null. This column MUST be of type Decimal, MUST conform to [Numeric Format](#numericformat), and be denominated in the BillingCurrency. The aggregated BilledCost for a billing period MUST match the charge received on the invoice for the same billing period.

## Column ID

BilledCost

## Display name

Billed Cost

## Description

A charge serving as the basis for invoicing, inclusive of all reduced rates and discounts while excluding the amortization of upfront charges (one-time or recurring).

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column Type     | Metric                  |
| Column required | True                    |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
