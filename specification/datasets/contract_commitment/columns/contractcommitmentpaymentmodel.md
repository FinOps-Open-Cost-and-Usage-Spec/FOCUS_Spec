# Contract Commitment Payment Model

[Contract Commitment Payment Model](#col) defines the financial settlement structure of a [contract commitment](#term). It identifies whether the financial obligation is settled via a single upfront payment, distributed recurring charges, or a combination of both over the [contract commitment duration type](#col).

[Contract Commitment Payment Model](#col) has three possible values: **No Upfront**, **Partial Upfront**, and **All Upfront**.

* No Upfront denotes that the obligation is settled entirely through recurring charges with no initial payment.
* Partial Upfront denotes that the obligation is settled through a combination of an initial payment and recurring charges.
* All Upfront denotes that the obligation is settled via a single payment at the start of the duration.

## Requirements

[ContractCommitmentPaymentModel](#col) MUST adhere to the following requirements:

* [ContractCommitmentPaymentModel](#col) MUST be of type String.
* [ContractCommitmentPaymentModel](#col) MUST NOT be null.
* [ContractCommitmentPaymentModel](#col) MUST be one of the allowed values.

## Allowed Values

| Value           | Sort Order | Description                                                                                  | Typical Use Case                                              |
| --------------- | ---------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| No Upfront      | 10         | The obligation is settled entirely through deferred payment(s) (typically multiple recurring charges) with no initial payment. | Pay-as-you-go Savings Plans or monthly-billed SaaS. |
| Partial Upfront | 20         | The obligation is settled through a combination of an initial payment and deferred payment(s) (typically multiple recurring charges). | Hybrid RIs or EAs with a "Year 1" deposit plus installments. |
| All Upfront     | 30         | The total obligation is settled via a single payment at the start of the duration. | High-discount RIs or multi-year contracts paid in full Day 1. |

## Implementation Guidance

* Settled via Upfront: Refer to the [contract commitment period start](#col) for the cash event.
* Settled via Recurring Charges: Refer to the [contract commitment payment interval](#col) to understand the frequency of those subsequent cash events.

## Column ID

ContractCommitmentPaymentModel

## Display Name

Contract Commitment Payment Model

## Description

Defines the financial settlement structure of a [contract commitment](#term).

## Content Constraints

| Constraint                 | Value                                                |
| :------------------------- | :--------------------------------------------------- |
| Dataset                    | [Contract Commitment](#ds)                           |
| Operating model conditions | Not applicable                                       |
| Column type                | Dimension                                            |
| Feature level              | Mandatory                                            |
| Allows nulls               | False                                                |
| Data type                  | String                                               |
| Value format               | Allowed values                                       |

## Version Introduced

1.4
