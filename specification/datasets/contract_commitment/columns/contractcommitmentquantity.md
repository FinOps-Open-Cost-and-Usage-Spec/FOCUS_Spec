# Contract Commitment Quantity

Contract Commitment Quantity represents the amount associated with the [*contract commitment*](#glossary:contract-commitment), denominated in a provider-defined [Contract Commitment Unit](#contractcommitmentunit).  Contract Commitment Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a provider and a customer.

The ContractCommitmentQuantity column adheres to the following requirements:

* ContractCommitmentQuantity MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentQuantity MUST be of type Decimal.
* ContractCommitmentQuantity MUST conform to [NumericFormat](#numericformat) requirements.
* ContractCommitmentQuantity nullability is defined as follows:
  * ContractCommitmentQuantity MUST NOT be null when [ContractCommitmentCategory](#contractcommitmentcategory) is "Usage".
  * ContractCommitmentQuantity MAY be null when ContractCommitmentCategory is "Spend".
* ContractCommitmentQuantity MUST be a valid decimal value.

## Column ID

ContractCommitmentQuantity

## Display Name

Contract Commitment Quantity

## Description

The amount associated with the *contract commitment*.

## Content Constraints

| Constraint    | Value                              |
| :------------ | :--------------------------------- |
| Column type   | Metric                             |
| Feature level | Mandatory                          |
| Allows nulls  | True                               |
| Data type     | Decimal                            |
| Value format  | [Numeric Format](#numericformat)   |
| Number range  | Any valid decimal value            |

## Introduced (version)

1.3
