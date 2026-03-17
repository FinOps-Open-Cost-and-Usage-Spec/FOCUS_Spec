# Pricing Currency

Pricing Currency is the national or virtual currency denomination that a [*contract commitment*](#glossary:contract-commitment) was priced in. This is commonly used in scenarios where a commitment is negotiated in one currency but billed in another.

## Requirements

PricingCurrency MUST adhere to the following requirements:

* PricingCurrency MUST be of type String.
* PricingCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* PricingCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* PricingCurrency MUST NOT be null.

## Column ID

PricingCurrency

## Display Name

Pricing Currency

## Description

The national or virtual currency denomination that the [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) was priced in.

## Content Constraints

| Constraint      | Value                               |
|:----------------|:------------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension                           |
| Feature level   | Conditional                         |
| Allows nulls    | False                               |
| Data type       | String                              |
| Value format    | [Currency Format](#attributes.currencyformat) |

## Introduced (version)

1.4
