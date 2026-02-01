# Contract Commitment Interval

Contract Commitment Interval represents the time boundary or "reset window" of a [*contract commitment*](#glossary:contract-commitment). This defines the period over which usage is aggregated or measured before the terms of the [contract commitment model](#datasets.contractcommitment.contractcommitmentmodel) (i.e., a Continuous model "use-it-or-lose-it", or a Discontinuous model's "true-up")  are applied.

Contract Commitment Interval has a series of possible values that represent a length of time, typically recurring over the [contract commitment duration](#datasets.contractcommitment.contractcommitmentduration).  Discontinuous models are typically Hourly, whereas Continuous models are typically Daily or greater.

## Requirements

ContractCommitmentInterval adheres to the following requirements:

* ContractCommitmentInterval MUST be present in a Contract Commitment [*FOCUS dataset*](#glossary:FOCUS-dataset).
* ContractCommitmentInterval MUST be of type String.
* ContractCommitmentInterval MUST NOT be null.
* ContractCommitmentInterval MUST be one of the allowed values.

## Column ID

ContractCommitmentInterval

## Display Name

Contract Commitment Interval

## Description

Represents the time boundary or "reset window" of a [*contract commitment*](#glossary:contract-commitment).

## Content Constraints

| Constraint      | Value          |
| :-------------- | :------------- |
| Column type     | Dimension      |
| Feature level   | Mandatory      |
| Allows nulls    | False          |
| Data type       | String         |
| Value format    | Allowed values |

Allowed values:

| Value         | Sort Order | Description                                                                            | Typical Use Case                                                           |
| ------------- | ---------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Hourly        | 10         | Resets every 60 minutes; unused commitment is lost immediately.                        | Continuous Model: Cloud-native RIs and Savings Plans.                      |
| Daily         | 20         | Resets at the end of each calendar day.                                                | Daily active user (DAU) caps or daily license minimums.                    |
| Weekly        | 30         | Measured over a rolling or fixed 7-day period.                                         | Burstable bandwidth or weekly sprint-based SaaS usage.                     |
| Monthly       | 40         | Resets at the end of the calendar month.                                               | Discontinuous Model: SaaS MRR minimums or tiered discounts.                |
| Quarterly     | 50         | Measured over a 3-month fiscal period.                                                 | Enterprise true-ups or volume-based rebate targets.                        |
| Semi-Annual   | 60         | Resets every 6 months.                                                                 | Mid-year budget alignments or review cycles.                               |
| Annual        | 70         | Measured over a 12-month period.                                                       | Discontinuous Model: Cloud EAs (Enterprise Agreements).                    |
| Total Term    | 80         | The commitment applies to the entire duration of the contract with no internal resets. | Multi-year "Pool of Funds" or total contract value (TCV) commits.          |
| Transactional | 90         | No time-based reset; based purely on event volume or credit consumption.               | API call bundles or "Credit Packs" with no expiration date.                |
| Custom        | 100        | A bespoke interval that does not fit standard calendar units.                          | Bridge contracts, unique POCs, or non-standard durations (e.g., 100 days). |

Note: the sort orders and use cases presented above are included for convenience and are not defined as separate FOCUS columns.

## Introduced (version)

1.4
