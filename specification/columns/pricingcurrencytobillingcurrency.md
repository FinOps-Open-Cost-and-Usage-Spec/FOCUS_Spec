# Pricing Currency to Billing Currency

A Pricing Currency to Billing Currency represents the conversion factor from [Pricing Currency](#pricingcurrency) to [Billing Currency](#billingcurrency).  Pricing Currency to Billing Currency is commonly used in scenarios where costs need to be grouped or aggregated by some combination of the following currency types:

* Fiat currency (e.g. USD, EUR).
* Virtual currency (e.g. tokens, credits).

The PricingCurrencyToBillingCurrency column adheres to the following requirements:

* PricingCurrencyToBillingCurrency presence in a [*FOCUS dataset*](#glossary:FOCUS-dataset) is defined as follows:
  * PricingCurrencyToBillingCurrency MUST be present in a FOCUS dataset when the provider presents prices in a virtual currency (e.g. credits, tokens).
  * PricingCurrencyToBillingCurrency MUST be present in a FOCUS dataset when the provider presents prices and bills in different fiat currencies (e.g. priced in USD and billed in EUR).
  * PricingCurrencyToBillingCurrency MAY be present in a FOCUS dataset in all other cases.
* PricingCurrencyToBillingCurrency MUST be of type Decimal.
* PricingCurrencyToBillingCurrency MUST conform to [Numeric Format](#numericformat) requirements.
* PricingCurrencyToBillingCurrency MUST NOT be null.
* PricingCurrencyToBillingCurrency MUST be a non-negative decimal value.
* PricingCurrencyToBillingCurrency MUST represent the conversion factor from [Pricing Currency](#pricingcurrency) to [Billing Currency](#billingcurrency).
* PricingCurrencyToBillingCurrency MUST equal 1 when the Pricing Currency and Billing Currency are the same value.

## Column ID

PricingCurrencyToBillingCurrency

## Display Name

Pricing Currency to Billing Currency

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
