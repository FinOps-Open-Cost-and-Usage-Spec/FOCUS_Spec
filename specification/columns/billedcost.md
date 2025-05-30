# Billed Cost

The [*billed cost*](#glossary:billed-cost) represents a [*charge*](#glossary:charge) serving as the basis for invoicing, inclusive of the impacts of all reduced rates and discounts while excluding the [*amortization*](#glossary:amortization) of relevant purchases (one-time or recurring) paid to cover future eligible *charges*. This cost is denominated in the [Billing Currency](#billingcurrency). The Billed Cost is commonly used to perform FinOps capabilities that require cash-basis accounting such as cost allocation, budgeting, and invoice reconciliation.

The BilledCost column adheres to the following requirements:

* BilledCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* BilledCost MUST be of type Decimal.
* BilledCost MUST conform to [NumericFormat](#numericformat) requirements.
* BilledCost MUST NOT be null.
* BilledCost MUST be a valid decimal value.
* BilledCost MUST be 0 for *charges* where payments are received by a third party (e.g., marketplace transactions).
* BilledCost MUST be denominated in the BillingCurrency.
* The sum of the BilledCost for a given [InvoiceId](#invoiceid) MUST match the sum of the payable amount provided in the corresponding invoice with the same id generated by the [InvoiceIssuer](#InvoiceIssuer).

## Column ID

BilledCost

## Display Name

Billed Cost

## Description

A *charge* serving as the basis for invoicing, inclusive of all reduced rates and discounts while excluding the *amortization* of upfront *charges* (one-time or recurring).

## Content constraints

|    Constraint   |      Value              |
|:----------------|:------------------------|
| Column type     | Metric                  |
| Feature level   | Mandatory               |
| Allows nulls    | False                   |
| Data type       | Decimal                 |
| Value format    | [Numeric Format](#numericformat) |
| Number range    | Any valid decimal value |

## Introduced (version)

0.5
