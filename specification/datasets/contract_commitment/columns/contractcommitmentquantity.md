# Contract Commitment Quantity

Contract Commitment Quantity represents the amount associated with the [*contract commitment*](#glossary:contract-commitment), denominated in a service-provider-defined [Contract Commitment Unit](#datasets.contractcommitment.contractcommitmentunit).  Contract Commitment Quantity is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [*resources*](#glossary:resource) or [*services*](#glossary:service) as agreed between a provider and a customer.

## Requirements

ContractCommitmentQuantity MUST adhere to the following requirements:

* ContractCommitmentQuantity MUST be of type Decimal.
* ContractCommitmentQuantity MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractCommitmentQuantity MUST adhere to the following nullability requirements:
  * ContractCommitmentQuantity MUST NOT be null when [ContractCommitmentCategory](#datasets.contractcommitment.contractcommitmentcategory) is "Usage".
  * ContractCommitmentQuantity MAY be null when ContractCommitmentCategory is "Spend".

## Column ID

ContractCommitmentQuantity

## Display Name

Contract Commitment Quantity

## Description

The amount associated with the *contract commitment*.

## Content Constraints

| Constraint      | Value                                                |
|:----------------|:-----------------------------------------------------|
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Metric                                               |
| Feature level   | Mandatory                                            |
| Allows nulls    | True                                                 |
| Data type       | Decimal                                              |
| Value format    | [Numeric Format](#attributes.numericformat)          |
| Number range    | Any valid decimal value                              |

## Introduced (version)

1.3
