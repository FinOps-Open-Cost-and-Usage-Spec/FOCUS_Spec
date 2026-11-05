# Contract Commitment Payment Upfront Percentage

[Contract Commitment Payment Upfront Percentage](#col) represents the portion of the total [Contract Commitment Cost](#col) paid at the start of the duration of a [contract commitment](#term).

This column allows for precise financial modeling of "Partial Upfront" [payment models](#col:ContractCommitmentPaymentModel), enabling FinOps practitioners and accounting professionals to distinguish between immediate cash outlays and deferred liabilities.

## Requirements

[ContractCommitmentPaymentUpfrontPercentage](#col) MUST adhere to the following requirements:

* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST be of type Decimal.
* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST conform to [NumericFormat](#attr) requirements.
* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST NOT be null.
* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST be a value between 0.0 and 1.0, inclusive.
* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST be 1.0 when [ContractCommitmentPaymentModel](#col) is ["All Upfront"](#val:ContractCommitment.ContractCommitmentPaymentModel).
* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST be 0.0 when [ContractCommitmentPaymentModel](#col) is ["No Upfront"](#val:ContractCommitment.ContractCommitmentPaymentModel).
* [ContractCommitmentPaymentUpfrontPercentage](#col) MUST be greater than 0.0 and less than 1.0 when [ContractCommitmentPaymentModel](#col) is ["Partial Upfront"](#val:ContractCommitment.ContractCommitmentPaymentModel).

## Column ID

ContractCommitmentPaymentUpfrontPercentage

## Display Name

Contract Commitment Payment Upfront Percentage

## Description

Represents the portion of the total [Contract Commitment Cost](#col) paid at the start of the duration of a [contract commitment](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | [Includes Partial Upfront Payments](#omc)                                                     |
| Column type                | Metric                                               |
| Feature level              | Conditional                                          |
| Allows nulls               | False                                                |
| Data type                  | Decimal                                              |
| Value format               | [Numeric Format](#attr)                              |
| Number range               | 0.0 to 1.0 (inclusive)                               |

## Version Introduced

1.4
