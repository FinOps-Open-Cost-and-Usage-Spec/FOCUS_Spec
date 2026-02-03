# Contract Commitment Pricing Currency

Contract Commitment Pricing Currency is the national or virtual currency denomination that a [*contract commitment*](#glossary:contract-commitment) was priced in. This is commonly used in scenarios where a commitment is negotiated in one currency but billed in another.

## Requirements

* ContractCommitmentPricingCurrency MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset) when the service provider supports pricing and billing in different currencies.
* ContractCommitmentPricingCurrency MUST be of type String.
* ContractCommitmentPricingCurrency MUST conform to [StringHandling](#attributes.stringhandling) requirements.
* ContractCommitmentPricingCurrency MUST conform to [CurrencyFormat](#attributes.currencyformat) requirements.
* ContractCommitmentPricingCurrency MUST NOT be null.

## Column ID
ContractCommitmentPricingCurrency

## Display Name
Contract Commitment Pricing Currency

## Description
The national or virtual currency denomination that the [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) was priced in.

## Content Constraints

| Constraint      | Value                               |
|:----------------|:------------------------------------|
| Column type     | Dimension                           |
| Feature level   | Conditional                         |
| Allows nulls    | False                               |
| Data type       | String                              |
| Value format    | [Currency Format](#attributes.currencyformat) |

## Introduced (version)

1.4
