# Billed Cost

The [Billed Cost](#glossary:billed-cost) represents a [*charge*](#glossary:charge) serving as the basis for invoicing, inclusive of the impacts of all reduced rates and discounts while excluding the [*amortization*](#glossary:amortization) of relevant purchases (one-time or recurring) paid to cover future eligible *charges*. This cost is denominated in the [Billing Currency](#billingcurrency). The Billed Cost is used to perform FinOps capabilities that require cash-basis accounting such as cost allocation, budgeting, and invoice reconciliation.

The BilledCost column MUST be present in the billing data. This column MUST be a valid numeric value of type Decimal, denominated in the BillingCurrency, and MUST NOT be null. The aggregated BilledCost for a [*billing period*](#glossary:billing-period) MUST match the *charge* received on the invoice for the same *billing period*.

## Column ID

BilledCost

## Display name

Billed Cost

## Description

A *charge* serving as the basis for invoicing, inclusive of all reduced rates and discounts while excluding the *amortization* of upfront *charges* (one-time or recurring).

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column required | True                    |
| Data type       | Decimal                 |
| Allows nulls    | False                   |
| Value format    | Numeric value           |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
