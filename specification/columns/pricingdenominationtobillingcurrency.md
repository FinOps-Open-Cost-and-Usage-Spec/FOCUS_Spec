# Pricing Denomination to Billing Currency

The Pricing Denomination to Billing Currency represents the conversion factor from [Pricing Denomination](#pricingdenomination) to [Billing Currency](#billingcurrency).

The Pricing Denomination to Billing Currency is commonly used for `<<USE CASE TBD>>`.

The PricingDenominationToBillingCurrency column adheres to the following requirements:

* The ListUnitPrice column MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider `<<CONDITION TBD>>`.
* This column MUST be a Decimal within the range of non-negative decimal values and MUST conform to [Numeric Format](#numericformat) requirements.
* `<<NULLABILITY REQ TBD>>`

## Column ID

PricingDenominationToBillingCurrency

## Display Name

Pricing Denomination to Billing Currency

## Description

The conversion factor from Pricing Denomination to Billing Currency.

## Usability Constraints

**Aggregation:** Column values should only be viewed in the context of their row and not aggregated to produce a total.

## Content Constraints

| Constraint      | Value                                |
|:----------------|:-------------------------------------|
| Column type     | Metric                               |
| Feature level   | Conditional                          |
| Allows nulls    | True                                 |
| Data type       | Decimal                              |
| Value format    | [Numeric Format](#numericformat)     |
| Number range    | Any valid non-negative decimal value |

## Introduced (version)

1.2
