# Contract Commitment Fulfillment Interval

Contract Commitment Fulfillment Interval represents the specific [*period*](#glossary:period) used to measure and reset the fulfillment of a [*contract commitment*](#glossary:contract-commitment). It establishes the window during which usage is aggregated to determine if commitment obligations have been met. At the end of each fulfillment interval, the [contract commitment model](#datasets.contractcommitment.contractcommitmentmodel) logic is applied, either resulting in the expiration of unused capacity (Continuous) or the calculation of a balance or true-up (Discontinuous).

Contract Commitment Fulfillment Interval has a series of possible values that represent a length of time, typically recurring over the [contract commitment duration type](#datasets.contractcommitment.contractcommitmentdurationtype). Continuous models are typically Hourly, whereas Discontinuous models are typically Daily or greater.

## Requirements

ContractCommitmentFulfillmentInterval MUST adhere to the following requirements:

* ContractCommitmentFulfillmentInterval MUST be of type String.
* ContractCommitmentFulfillmentInterval MUST NOT be null.
* ContractCommitmentFulfillmentInterval MUST be one of the allowed values.
* ContractCommitmentFulfillmentInterval MUST NOT be "Full Period" if [ContractCommitmentModel](#datasets.contractcommitment.contractcommitmentmodel) is "Continuous".

## Column ID

ContractCommitmentFulfillmentInterval

## Display Name

Contract Commitment Fulfillment Interval

## Description

Represents the specific [*period*](#glossary:period) used to measure and reset the fulfillment of a [*contract commitment*](#glossary:contract-commitment).

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

| Value         | Sort Order | Description                                                                            | Typical Use Case                                                           |
| ------------- | ---------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Hourly        | 10         | Measured over a 60-minute period. | Continuous Model: Cloud-native RIs and Savings Plans. |
| Daily         | 20         | Measured over a calendar day. | Daily active user (DAU) caps or daily license minimums. |
| Weekly        | 30         | Measured over a rolling or fixed 7-day period. | Burstable bandwidth or weekly sprint-based SaaS usage. |
| Monthly       | 40         | Measured over a calendar month. | Discontinuous Model: SaaS MRR minimums or tiered discounts. |
| Quarterly     | 50         | Measured over a 3-month fiscal period. | Enterprise true-ups or volume-based rebate targets. |
| Semi-Annual   | 60         | Measured over a 6-month period. | Mid-year budget alignments or review cycles. |
| Annual        | 70         | Measured over a 12-month period. | Discontinuous Model: Cloud EAs (Enterprise Agreements). |
| Full Period   | 80         | The fulfillment interval is the full duration of the contract commitment, with no internal resets. | "Pool-of-funds commitments" spanning the full commitment duration. |
| Transactional | 90         | No time-based reset; based purely on event volume or credit consumption. | API call bundles or "Credit Packs" with no expiration date. |
| Custom        | 100        | A bespoke interval that does not fit standard calendar units. | Bridge contracts, unique POCs, or non-standard durations (e.g., 100 days). |

Note: the sort orders and use cases presented above are included for convenience and are not defined as separate FOCUS columns.

## Introduced (version)

1.4
