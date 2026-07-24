# Currency

Currency is an identifier that represents the currency in which a recommendation's [Estimated Monthly Cost Impact](#datasets.recommendation.estimatedmonthlycostimpact) is expressed.

## Requirements

Currency MUST adhere to the following requirements:

* Currency MUST be of type String.
* Currency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* Currency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* Currency MUST adhere to the following nullability requirements:
  * Currency MUST NOT be null when EstimatedMonthlyCostImpact is not null.
  * Currency MUST be null when EstimatedMonthlyCostImpact is null.
* Currency MUST be expressed in [*national currency*](#glossary:national-currency) (e.g., USD, EUR).

## Column ID

Currency

## Display Name

Currency

## Description

Represents the currency in which a recommendation's estimated cost impact is expressed.

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
