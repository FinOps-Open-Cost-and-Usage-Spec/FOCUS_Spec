# Pricing Denomination to Billing Currency

A Pricing Denomination to Billing Currency represents the conversion factor from [Pricing Denomination](#pricingdenomination) to [Billing Currency](#billingcurrency).  Pricing Denomination to Billing Currency is commonly used in scenarios where costs need to be grouped or aggregated by proprietary units of measure.

The PricingDenominationToBillingCurrency column adheres to the following requirements:

* PricingDenominationToBillingCurrency MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset) when the provider presents prices in a proprietary, non-currency unit of measure (e.g. credits, tokens).
* PricingDenominationToBillingCurrency MUST be of type Decimal.
* PricingDenominationToBillingCurrency MUST conform to [Numeric Format](#numericformat) requirements.
* PricingDenominationToBillingCurrency MUST NOT be null when the provider presents prices in a proprietary, non-currency unit of measure (e.g. credits, tokens).
* PricingDenominationToBillingCurrency MUST be a non-negative decimal value.

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
