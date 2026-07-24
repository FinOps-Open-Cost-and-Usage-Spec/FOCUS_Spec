# Contract Commitment Payment Model

Contract Commitment Payment Model defines the financial settlement structure of the [*contract commitment*](#glossary:contract-commitment) a recommendation proposes to purchase. It identifies whether the obligation would be settled via a single upfront payment, distributed recurring charges, or a combination of both.

Contract Commitment Payment Model has three possible values: **No Upfront**, **Partial Upfront**, and **All Upfront**.

* No Upfront denotes that the obligation is settled entirely through deferred payment(s) (typically multiple recurring charges) with no initial payment.
* Partial Upfront denotes that the obligation is settled through a combination of an initial payment and deferred payment(s) (typically multiple recurring charges).
* All Upfront denotes that the obligation is settled via a single payment at the start of the duration.

## Requirements

ContractCommitmentPaymentModel MUST adhere to the following requirements:

* ContractCommitmentPaymentModel MUST be of type String.
* ContractCommitmentPaymentModel MUST adhere to the following nullability requirements:
  * ContractCommitmentPaymentModel MUST NOT be null when a recommendation proposes the purchase of a *contract commitment*.
  * ContractCommitmentPaymentModel MUST be null when a recommendation does not propose the purchase of a *contract commitment*.
* ContractCommitmentPaymentModel MUST be one of the allowed values when not null.

## Allowed Values

| Value           | Description                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------- |
| No Upfront      | The obligation is settled entirely through deferred payment(s) (typically multiple recurring charges) with no initial payment. |
| Partial Upfront | The obligation is settled through a combination of an initial payment and deferred payment(s) (typically multiple recurring charges). |
| All Upfront     | The total obligation is settled via a single payment at the start of the duration. |

## Column ID

ContractCommitmentPaymentModel

## Display Name

Contract Commitment Payment Model

## Description

Defines the financial settlement structure of the *contract commitment* a recommendation proposes to purchase.

## Content Constraints

| Constraint      | Value                                          |
| :-------------- | :--------------------------------------------- |
| Dataset         | [Recommendation](#datasets.recommendation)     |
| Column type     | Dimension                                      |
| Feature level   | Conditional                                    |
| Allows nulls    | True                                           |
| Data type       | String                                         |
| Value format    | Allowed values                                 |

## Version Introduced

1.5
