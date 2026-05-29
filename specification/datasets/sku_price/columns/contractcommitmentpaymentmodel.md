# Contract Commitment Payment Model

Contract Commitment Payment Model defines the financial settlement structure of a [*contract commitment*](#glossary:contract-commitment). It identifies whether the financial obligation is settled via a single upfront payment, distributed recurring charges, or a combination of both over the [contract commitment duration type](#datasets.skuprice.contractcommitmentdurationtype).

Contract Commitment Payment Model has three possible values: **No Upfront**, **Partial Upfront**, and **All Upfront**.

* No Upfront denotes that the obligation is settled entirely through recurring charges with no initial payment.
* Partial Upfront denotes that the obligation is settled through a combination of an initial payment and recurring charges.
* All Upfront denotes that the obligation is settled via a single payment at the start of the duration.

## Requirements

ContractCommitmentPaymentModel MUST adhere to the following requirements:

* ContractCommitmentPaymentModel MUST be of type String.
* ContractCommitmentPaymentModel MUST NOT be null when [Pricing Category](#datasets.skuprice.pricingcategory) is "Committed".
* ContractCommitmentPaymentModel MUST be one of the allowed values when present.

## Allowed Values

| Value           | Sort Order | Description                                                                                  | Typical Use Case                                              |
| --------------- | ---------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| No Upfront      | 10         | The obligation is settled entirely through deferred payment(s) (typically multiple recurring charges) with no initial payment. | Pay-as-you-go Savings Plans or monthly-billed SaaS. |
| Partial Upfront | 20         | The obligation is settled through a combination of an initial payment and deferred payment(s) (typically multiple recurring charges). | Hybrid RIs or EAs with a "Year 1" deposit plus installments. |
| All Upfront     | 30         | The total obligation is settled via a single payment at the start of the duration. | High-discount RIs or multi-year contracts paid in full Day 1. |

## Implementation Guidance

Within the SKU Price dataset, the Contract Commitment Payment Model helps practitioners understand how a committed rate is structured across different catalog rows:

* **All Upfront:** The corresponding SKU Price record typically has a [Charge Frequency](#datasets.skuprice.chargefrequency) of "One-Time".
* **No Upfront:** The corresponding SKU Price record typically has a [Charge Frequency](#datasets.skuprice.chargefrequency) of "Recurring" or "Usage-Based".
* **Partial Upfront:** This pricing model typically requires multiple associated SKU Price records to accurately represent the cost (e.g., one record for the "One-Time" upfront fee, and a separate record for the "Recurring" or "Usage-Based" discounted rate).

## Column ID

ContractCommitmentPaymentModel

## Display Name

Contract Commitment Payment Model

## Description

Defines the financial settlement structure of a *contract commitment*.

## Content Constraints

| Constraint      | Value                                                                                      |
| :-------------- | :----------------------------------------------------------------------------------------- |
| Dataset         | [SKU Price](#datasets.skuprice)                                                            |
| Column type     | Dimension                                                                                  |
| Feature level   | Conditional                                                                                |
| Condition       | [Includes contract commitments](#conditions.includescontractcommitments)                   |
| Allows nulls    | True                                                                                       |
| Data type       | String                                                                                     |
| Value format    | Allowed values                                                                             |

## Version Introduced

1.5
