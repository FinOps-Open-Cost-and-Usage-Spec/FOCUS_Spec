# Billing Currency

[*Billing currency*](#glossary:billing-currency) is an identifier that represents the currency in which the estimated savings of a recommendation are denominated. Billing Currency in the Recommendation dataset is commonly used to aggregate estimated savings consistently across recommendations.

## Requirements

BillingCurrency MUST adhere to the following requirements:

* BillingCurrency MUST be of type String.
* BillingCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* BillingCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* BillingCurrency MUST NOT be null when [EstimatedCostSavings](#datasets.recommendation.estimatedcostsavings) is not null.
* BillingCurrency MUST be expressed in [*national currency*](#glossary:national-currency) (e.g., USD, EUR).

## Column ID

BillingCurrency

## Display Name

Billing Currency

## Description

Represents the currency in which the estimated savings of a recommendation are denominated.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Mandatory                                      |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | [Currency Format](#attributes.currencyformat)  |

## Version Introduced

1.5
