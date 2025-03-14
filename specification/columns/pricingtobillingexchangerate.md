# Pricing to Billing Exchange Rate

A Pricing to Billing Exchange Rate represents the conversion factor from [Pricing Currency](#pricingcurrency) to [Billing Currency](#billingcurrency).  Pricing to Billing Exchange Rate is commonly used in scenarios where costs need to be grouped or aggregated by some combination of the following currency types:

* National currency (e.g. USD, EUR).
* Virtual currency (e.g. tokens, credits).

The PricingToBillingExchangeRate column adheres to the following requirements:

* PricingToBillingExchangeRate presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingToBillingExchangeRate MUST be present in a FOCUS dataset when the provider presents prices in a virtual currency (e.g. credits, tokens).
  * PricingToBillingExchangeRate MUST be present in a FOCUS dataset when the provider presents prices and bills in different national currencies (e.g. priced in USD and billed in EUR).
  * PricingToBillingExchangeRate MAY be present in a FOCUS dataset in all other cases.
* PricingToBillingExchangeRate MUST be of type Decimal.
* PricingToBillingExchangeRate MUST conform to [Numeric Format](#numericformat) requirements.
* PricingToBillingExchangeRate MUST NOT be null.
* PricingToBillingExchangeRate MUST be a non-negative decimal value.
* PricingToBillingExchangeRate MUST represent the conversion factor from [Pricing Currency](#pricingcurrency) to [Billing Currency](#billingcurrency).
* PricingToBillingExchangeRate MUST equal 1 when the Pricing Currency and Billing Currency are the same value.

## Column ID

PricingToBillingExchangeRate

## Display Name

Pricing to Billing Exchange Rate

## Description

The conversion factor from Pricing Currency to Billing Currency.

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
