# Contract Commitment Cost

Contract Commitment Cost represents the monetary value of the [*contract commitment*](#glossary:contract-commitment).  Contract Commitment Cost is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as negotiated between a provider and a customer.

The ContractCommitmentCost column adheres to the following requirements:

* ContractCommitmentCost MUST be present in a [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentCost MUST be of type Decimal.
* ContractCommitmentCost MUST conform to [NumericFormat](#numericformat) requirements.
* ContractCommitmentCost nullability is defined as follows:
  * ContractCommitmentCost MUST NOT be null when ContractCommitmentQuantity is null.
  * ContractCommitmentCost MAY be null when ContractCommitmentQuantity is not null.
* ContractCommitmentCost MUST be a valid decimal value.

## Column ID

ContractCommitmentCost

## Display Name

Contract Commitment Cost

## Description

The monetary value of the *contract commitment*.

## Content Constraints

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Column type   | Dimension                          |
| Feature level | Conditional                        |
| Allows nulls  | True                               |
| Data type     | Decimal                            |
| Value format  | \<not specified>                   |

## Introduced (version)

1.3
