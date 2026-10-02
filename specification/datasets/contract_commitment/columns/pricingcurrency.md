# Pricing Currency

Pricing Currency is the [*national*](#glossary:national-currency) or [*consumption currency*](#glossary:consumption-currency) denomination that a [*contract commitment*](#glossary:contract-commitment) was priced in. This is commonly used in scenarios where a commitment is negotiated in one currency but billed in another.

## Requirements

PricingCurrency MUST adhere to the following requirements:

* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* PricingCurrency MUST NOT be null.
* PricingCurrency MUST represent a *national currency* or a *consumption currency*.
* PricingCurrency documentation MUST adhere to the following requirements:
  * PricingCurrency documentation MUST specify how to determine whether a value represents a *national currency*.
  * PricingCurrency documentation MUST be accessible to practitioners.

## Column ID

PricingCurrency

## Display Name

Pricing Currency

## Description

The *national* or *consumption currency* denomination that the [Contract Commitment Cost](#datamodel.contractcommitment.contractcommitmentcost) was priced in.

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#datamodel.contractcommitment) |
| Operating Model Conditions | [Includes Pricing-Billing Currency Differences](#operatingmodelconditions.includespricing-billingcurrencydifferences) |
| Column type                | Dimension                                            |
| Feature level              | Conditional                                          |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | [Currency Format](#attributes.currencyformat)        |

## Version Introduced

1.4
