# Contract Commitment Cost

[Contract Commitment Cost](#col) represents the monetary value of the [contract commitment](#term). [Contract Commitment Cost](#col) is commonly used for monitoring the progress towards fulfilling contractual commitments that may facilitate discounts for [resources](#term) or [services](#term) as agreed between a service provider and a customer.

## Requirements

[ContractCommitmentCost](#col) MUST adhere to the following requirements:

* [ContractCommitmentCost](#col) MUST be of type Decimal.
* [ContractCommitmentCost](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ContractCommitmentCost](#col) MUST adhere to the following nullability requirements:
  * [ContractCommitmentCost](#col) MUST NOT be null when [ContractCommitmentCategory](#col) is ["Spend"](#val:ContractCommitment.ContractCommitmentCategory).
  * [ContractCommitmentCost](#col) MAY be null when [ContractCommitmentCategory](#col) is ["Usage"](#val:ContractCommitment.ContractCommitmentCategory).
* [ContractCommitmentCost](#col) MUST be denominated in the [BillingCurrency](#col).

## Column ID

ContractCommitmentCost

## Display Name

Contract Commitment Cost

## Description

The monetary value of the [contract commitment](#term).

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
