# Pricing Currency Contract Commitment Cost

[Pricing Currency Contract Commitment Cost](#col) represents the monetary value of the [contract commitment](#term) denominated in the [Pricing Currency](#col). This metric is used to track progress towards fulfilling contractual milestones using the original negotiated value, independent of currency exchange rate fluctuations.

## Requirements

[PricingCurrencyContractCommitmentCost](#col) MUST adhere to the following requirements:

* [PricingCurrencyContractCommitmentCost](#col) MUST be of type Decimal.
* [PricingCurrencyContractCommitmentCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [PricingCurrencyContractCommitmentCost](#col) MUST adhere to the following nullability requirements:
  * [PricingCurrencyContractCommitmentCost](#col) MUST NOT be null when [ContractCommitmentCategory](#col) is ["Spend"](#val:ContractCommitment.ContractCommitmentCategory) and [PricingCurrency](#col) is provided.
  * [PricingCurrencyContractCommitmentCost](#col) MAY be null when [ContractCommitmentCategory](#col) is ["Usage"](#val:ContractCommitment.ContractCommitmentCategory).
* [PricingCurrencyContractCommitmentCost](#col) MUST be denominated in the [PricingCurrency](#col).

## Column ID

PricingCurrencyContractCommitmentCost

## Display Name

Pricing Currency Contract Commitment Cost

## Description

The monetary value of the [contract commitment](#term) in the [Pricing Currency](#col).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | [Includes Pricing-Billing Currency Differences](#omc)                                                                 |
| Column type                | Metric                                               |
| Feature level              | Conditional                                          |
| Allows nulls               | True                                                 |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attr)                              |
| Number range               | Any valid decimal value                              |

## Version Introduced

1.4
