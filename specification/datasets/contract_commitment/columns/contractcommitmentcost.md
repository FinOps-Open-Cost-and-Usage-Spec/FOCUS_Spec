# Contract Commitment Cost

Contract Commitment Cost represents the monetary value of the [*contract commitment*](#glossary:contract-commitment).  Contract Commitment Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a provider and a customer.

The ContractCommitmentCost column adheres to the following requirements:

* ContractCommitmentCost MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentCost MUST be of type Decimal.
* ContractCommitmentCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractCommitmentCost nullability is defined as follows:
  * ContractCommitmentCost MUST NOT be null when [ContractCommitmentCategory](#contractcommitmentcategory) is "Spend".
  * ContractCommitmentCost MAY be null when ContractCommitmentCategory is "Usage".
* ContractCommitmentCost MUST be a valid decimal value.
* ContractCommitmentCost MUST be denominated in the [BillingCurrency](#billingcurrency-1).

## Column ID

ContractCommitmentCost

## Display Name

Contract Commitment Cost

## Description

The monetary value of the *contract commitment*.

## Content Constraints

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Column type   | Metric                             |
| Feature level | Mandatory                          |
| Allows nulls  | True                               |
| Data type     | Decimal                            |
| Value format  | [Numeric Format](#numericformat)   |
| Number range  | Any valid decimal value            |

## Introduced (version)

1.3
