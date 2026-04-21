# Contract Commitment Payment Model

Contract Commitment Payment Model defines the financial settlement structure of a [*contract commitment*](#glossary:contract-commitment). It identifies whether the financial obligation is settled via a single upfront payment, distributed recurring charges, or a combination of both over the [contract commitment duration type](#datasets.contractcommitment.contractcommitmentdurationtype).

Contract Commitment Payment Model has three possible values: **No Upfront**, **Partial Upfront**, and **All Upfront**.

* No Upfront denotes that the obligation is settled entirely through recurring charges with no initial payment.
* Partial Upfront denotes that the obligation is settled through a combination of an initial payment and recurring charges.
* All Upfront denotes that the obligation is settled via a single payment at the start of the duration.

## Requirements

ContractCommitmentPaymentModel MUST adhere to the following requirements:

* ContractCommitmentPaymentModel MUST be of type String.
* ContractCommitmentPaymentModel MUST NOT be null.
* ContractCommitmentPaymentModel MUST be one of the allowed values.

## Implementation Context

* Settled via Upfront: Refer to the [contract commitment period start](#datasets.contractcommitment.contractcommitmentperiodstart) for the cash event.
* Settled via Recurring Charges: Refer to the [contract commitment payment interval](#datasets.contractcommitment.contractcommitmentpaymentinterval) to understand the frequency of those subsequent cash events.

## Column ID

ContractCommitmentPaymentModel

## Display Name

Contract Commitment Payment Model

## Description

Defines the financial settlement structure of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Dataset         | [Contract Commitment](#datasets.contractcommitment)  |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value           | Sort Order | Description                                                                                  | Typical Use Case                                              |
| --------------- | ---------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| No Upfront      | 10         | The obligation is settled entirely through deferred payment(s) (typically multiple recurring charges) with no initial payment. | Pay-as-you-go Savings Plans or monthly-billed SaaS. |
| Partial Upfront | 20         | The obligation is settled through a combination of an initial payment and deferred payment(s) (typically multiple recurring charges). | Hybrid RIs or EAs with a "Year 1" deposit plus installments. |
| All Upfront     | 30         | The total obligation is settled via a single payment at the start of the duration. | High-discount RIs or multi-year contracts paid in full Day 1. |

## Introduced (version)

1.4
