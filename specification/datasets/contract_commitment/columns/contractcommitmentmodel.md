# Contract Commitment Model

[Contract Commitment Model](#col) represents the operational behavior and consumption flexibility of a [contract commitment](#term). This field distinguishes between rigid, "use-it-or-lose-it" obligations (typically hourly) and flexible, aggregate-based agreements that accommodate variable usage patterns.

[Contract Commitment Model](#col) has two possible values: **Continuous** and **Discontinuous**. Continuous models (e.g., reserved instances, savings plans) represent a flat, constant "floor" of commitment where any dip in usage results in immediate, unrecoverable waste. Discontinuous models (e.g., enterprise agreements, SaaS minimum spend agreements) represent a broader, more flexible bucket where the commitment is "spikier": the usage can fluctuate wildly, but as long as the aggregate hits the target (or the true-up handles the variance), the commitment is satisfied. In either case, the interval of the commitment is represented by the [Contract Commitment Fulfillment Interval](#col).

## Requirements

[ContractCommitmentModel](#col) MUST adhere to the following requirements:

* [ContractCommitmentModel](#col) MUST be of type String.
* [ContractCommitmentModel](#col) MUST NOT be null.
* [ContractCommitmentModel](#col) MUST be one of the allowed values.
* [ContractCommitmentModel](#col) MUST be ["Discontinuous"](#val:ContractCommitmentModel) when [ContractCommitmentFulfillmentInterval](#col) is ["Full Period"](#val:ContractCommitment.ContractCommitmentFulfillmentInterval).

## Allowed Values

| Value         | Description                                                                                                                                                     |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Continuous    | A flat, constant "floor" of commitment (e.g., RIs, Savings Plans). Coverage is applied at a fixed rate per Contract Commitment Fulfillment Interval (usually hourly), and benefits are not carried over to subsequent intervals. |
| Discontinuous | A flexible, aggregate commitment (e.g., Enterprise Agreements, SaaS Minimum Spend). Coverage is measured over a broad window or against a total monetary value. |

## Implementation Guidance

### Reporting and Analysis

* For _continuous_ models: report on Utilization % to identify immediate waste.
* For _discontinuous_ models: report on Burn Rate and Remaining Balance to ensure the "spikes" are not trending toward an early exhaustion of the fund or a massive year-end true-up bill.

### Relationship with Fulfillment Interval

Because a `Continuous` model dictates a recurring, "use-it-or-lose-it" evaluation window, it cannot logically span an entire, cumulative contract term without a reset. Therefore, if the associated [Contract Commitment Fulfillment Interval](#col) is `Full Period`, the [Contract Commitment Model](#col) must be categorized as `Discontinuous`.

## Column ID

ContractCommitmentModel

## Display Name

Contract Commitment Model

## Description

Represents the operational behavior and consumption flexibility of a [contract commitment](#term).

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
