# Contract Commitment Quantity

[Contract Commitment Quantity](#col) represents the amount associated with the [contract commitment](#term), denominated in a service-provider-defined [Contract Commitment Unit](#col). [Contract Commitment Quantity](#col) is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [resources](#term) or [services](#term) as agreed between a provider and a customer.

## Requirements

[ContractCommitmentQuantity](#col) MUST adhere to the following requirements:

* [ContractCommitmentQuantity](#col) MUST be of type Decimal.
* [ContractCommitmentQuantity](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ContractCommitmentQuantity](#col) MUST adhere to the following nullability requirements:
  * [ContractCommitmentQuantity](#col) MUST NOT be null when [ContractCommitmentCategory](#col) is ["Usage"](#val:ContractCommitment.ContractCommitmentCategory).
  * [ContractCommitmentQuantity](#col) MAY be null when [ContractCommitmentCategory](#col) is ["Spend"](#val:ContractCommitment.ContractCommitmentCategory).

## Column ID

ContractCommitmentQuantity

## Display Name

Contract Commitment Quantity

## Description

The amount associated with the [contract commitment](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Metric                                               |
| Feature level              | Mandatory                                            |
| Allows nulls               | True                                                 |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attr)                              |
| Number range               | Any valid decimal value                              |

## Version Introduced

1.3
