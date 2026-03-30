# Pricing Currency Contract Commitment Cost

Pricing Currency Contract Commitment Cost represents the monetary value of the [*contract commitment*](#glossary:contract-commitment) denominated in the [*Pricing Currency*](#datasets.contractcommitment.pricingcurrency). This metric is used to track progress towards fulfilling contractual milestones using the original negotiated value, independent of currency exchange rate fluctuations.

## Requirements

PricingCurrencyContractCommitmentCost MUST adhere to the following requirements:

* PricingCurrencyContractCommitmentCost MUST be of type Decimal.
* PricingCurrencyContractCommitmentCost MUST adhere to the following nullability requirements:
  * PricingCurrencyContractCommitmentCost MUST NOT be null when [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory) is "Spend" and [PricingCurrency](#datasets.contractcommitment.pricingcurrency) is provided.
  * PricingCurrencyContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
* PricingCurrencyContractCommitmentCost MUST be denominated in the [PricingCurrency](#datasets.contractcommitment.pricingcurrency).

## Column ID

PricingCurrencyContractCommitmentCost

## Display Name

Pricing Currency Contract Commitment Cost

## Description

The monetary value of the *contract commitment* in the [Pricing Currency](#datasets.contractcommitment.pricingcurrency).

## Content Constraints

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type   | Metric                             |
| Feature level | Conditional                        |
| Allows nulls  | True                               |
| Data type     | Decimal                            |
| Value format  | [Numeric Format](#attributes.numericformat) |
| Number range  | Any valid decimal value            |

## Introduced (version)

1.4