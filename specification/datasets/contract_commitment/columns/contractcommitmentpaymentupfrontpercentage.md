# Contract Commitment Payment Upfront Percentage

Contract Commitment Payment Upfront Percentage represents the portion of the total [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) paid at the start of the duration of a [*contract commitment*](#glossary:contract-commitment).

This column allows for precise financial modeling of "Partial Upfront" [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel), enabling FinOps practitioners and accounting professionals to distinguish between immediate cash outlays and deferred liabilities.

## Requirements

* ContractCommitmentPaymentUpfrontPercentage MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset) if the service provider offers "Partial Upfront" [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel).
* ContractCommitmentPaymentUpfrontPercentage MUST be of type Decimal.
* ContractCommitmentPaymentUpfrontPercentage MUST conform to [NumericFormat](#attributes.numericformat) requirements.
* ContractCommitmentPaymentUpfrontPercentage MUST NOT be null.
* ContractCommitmentPaymentUpfrontPercentage MUST be a value between 0.0 and 1.0.
* ContractCommitmentPaymentUpfrontPercentage MUST be 1.0 when [ContractCommitmentPaymentModel] is "All Upfront".
* ContractCommitmentPaymentUpfrontPercentage MUST be 0.0 when [ContractCommitmentPaymentModel] is "No Upfront".

## Column ID
ContractCommitmentPaymentUpfrontPercentage

## Display Name
Contract Commitment Payment Upfront Percentage

## Description
Represents the portion of the total [Contract Commitment Cost](#datasets.contractcommitment.contractcommitmentcost) paid at the start of the duration of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint    | Value            |
| :------------ | :--------------- |
| Column type   | Dimension        |
| Feature level | Conditional      |
| Allows nulls  | False            |
| Data type     | Decimal          |
| Value format  | 0.0 to 1.0       |