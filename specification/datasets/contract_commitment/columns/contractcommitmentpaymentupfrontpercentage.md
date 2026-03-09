# Contract Commitment Payment Upfront Percentage

Contract Commitment Payment Upfront Percentage represents the portion of the total [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) paid at the start of the duration of a [*contract commitment*](#glossary:contract-commitment).

This column allows for precise financial modeling of "Partial Upfront" [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel), enabling FinOps practitioners and accounting professionals to distinguish between immediate cash outlays and deferred liabilities.

## Requirements

ContractCommitmentPaymentUpfrontPercentage MUST adhere to the following requirements:

* ContractCommitmentPaymentUpfrontPercentage MUST be of type Decimal.
* ContractCommitmentPaymentUpfrontPercentage MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractCommitmentPaymentUpfrontPercentage MUST NOT be null.
* ContractCommitmentPaymentUpfrontPercentage MUST be a value between 0.0 and 1.0, inclusive.
* ContractCommitmentPaymentUpfrontPercentage MUST be 1.0 when [ContractCommitmentPaymentModel](#datasets.contractcommitment.contractcommitmentpaymentmodel) is "All Upfront".
* ContractCommitmentPaymentUpfrontPercentage MUST be 0.0 when [ContractCommitmentPaymentModel](#datasets.contractcommitment.contractcommitmentpaymentmodel) is "No Upfront".

## Column ID

ContractCommitmentPaymentUpfrontPercentage

## Display Name

Contract Commitment Payment Upfront Percentage

## Description

Represents the portion of the total [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) paid at the start of the duration of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint    | Value            |
| :------------ | :--------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type   | Dimension        |
| Feature level | Conditional      |
| Allows nulls  | False            |
| Data type     | Decimal          |
| Value format  | [Numeric Format](#attributes.numericformat)  |
| Number range  | 0.0 to 1.0             |

## Introduced (version)

1.4