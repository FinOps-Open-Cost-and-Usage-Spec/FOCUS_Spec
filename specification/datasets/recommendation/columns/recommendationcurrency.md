# Recommendation Currency

Recommendation Currency is an identifier that represents the currency in which a recommendation's [Estimated Delta Cost](#datamodel.recommendation.estimateddeltacost) is expressed. Recommendation Currency matches the [*billing currency*](#glossary:billing-currency) of the [Billing Account ID](#datamodel.recommendation.billingaccountid) when one is present.

## Requirements

RecommendationCurrency MUST adhere to the following requirements:

* RecommendationCurrency MUST be of type String.
* RecommendationCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* RecommendationCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* RecommendationCurrency MUST adhere to the following nullability requirements:
  * RecommendationCurrency MUST NOT be null when EstimatedDeltaCost is not null.
  * RecommendationCurrency MUST be null when EstimatedDeltaCost is null.
* RecommendationCurrency MUST be expressed in [*national currency*](#glossary:national-currency) (e.g., USD, EUR).
* When RecommendationCurrency and BillingAccountId are not null, RecommendationCurrency for a given BillingAccountId MUST match [CostAndUsage.BillingCurrency](#datamodel.costandusage.billingcurrency) for the same [CostAndUsage.BillingAccountId](#datamodel.costandusage.billingaccountid).

## Column ID

RecommendationCurrency

## Display Name

Recommendation Currency

## Description

Represents the currency in which a recommendation's estimated delta cost is expressed.

## Content Constraints

| Constraint                 | Value                                         |
| :------------------------- | :-------------------------------------------- |
| Dataset                    | [Recommendation](#datamodel.recommendation)   |
| Operating Model Conditions | Not applicable                                |
| Column type                | Dimension                                     |
| Feature level              | Mandatory                                     |
| Allows nulls               | True                                          |
| Data type                  | String                                        |
| Value format               | [Currency Format](#attributes.currencyformat) |

## Version Introduced

1.5
