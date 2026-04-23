# Contract Commitment Cost

Contract Commitment Cost represents the monetary value of the [*contract commitment*](#glossary:contract-commitment). Contract Commitment Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a service provider and a customer.

## Requirements

ContractCommitmentCost MUST adhere to the following requirements:

* ContractCommitmentCost MUST be of type Decimal.
* ContractCommitmentCost MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractCommitmentCost MUST adhere to the following nullability requirements:
  * ContractCommitmentCost MUST NOT be null when [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory) is "Spend".
  * ContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
* ContractCommitmentCost MUST be denominated in the [BillingCurrency](#datasets.contractcommitment.billingcurrency).

## Column ID

ContractCommitmentCost

## Display Name

Contract Commitment Cost

## Description

The monetary value of the *contract commitment*.

## Content Constraints

| Constraint    | Value                                                |
| :------------ | :--------------------------------------------------- |
| Dataset       | [Contract Commitment](#datasets.contractcommitment)  |
| Column type   | Metric                                               |
| Feature level | Mandatory                                            |
| Allows nulls  | True                                                 |
| Data type     | Decimal                                              |
| Value format  | Numeric Format          |
| Number range  | Any valid decimal value                              |

## Introduced (version)

1.3
