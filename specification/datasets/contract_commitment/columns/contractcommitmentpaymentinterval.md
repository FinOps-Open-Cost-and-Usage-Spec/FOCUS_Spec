# Contract Commitment Payment Interval

[Contract Commitment Payment Interval](#col) represents the frequency by which a [contract commitment](#term) is invoiced. For [payment models](#col:ContractCommitmentPaymentModel) involving deferred financial obligations, the Payment Interval denotes the ongoing billing cycle. For models paid upfront, the Payment Interval denotes the single settlement event.

> **Note:** Do not confuse the [Contract Commitment Payment Interval](#col) with the [Contract Commitment Fulfillment Interval](#col). For example, a spend-based commitment discount may have an Hourly Fulfillment Interval (usage reset) but a Monthly Payment Interval (billing cycle).

## Requirements

[ContractCommitmentPaymentInterval](#col) MUST adhere to the following requirements:

* [ContractCommitmentPaymentInterval](#col) MUST be of type String.
* [ContractCommitmentPaymentInterval](#col) MUST NOT be null.
* [ContractCommitmentPaymentInterval](#col) MUST be one of the allowed values.
* [ContractCommitmentPaymentInterval](#col) MUST be ["One-Time"](#val:ContractCommitmentPaymentInterval) when [ContractCommitmentPaymentModel](#col) is ["All Upfront"](#val:ContractCommitment.ContractCommitmentPaymentModel).
* [ContractCommitmentPaymentInterval](#col) SHOULD represent a time granularity equal to or lesser than the time granularity represented by [ContractCommitmentDurationType](#col).

## Allowed Values

| Value       | Sort Order | Description                                                         | Typical Use Case                                  |
| ----------- | ---------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| One-Time    | 10         | A single invoice is generated for the entire obligation. | All Upfront models (e.g., 3yr All-Upfront RI) or single-invoice arrears paid at the end of a term. |
| Monthly     | 20         | Invoices for the deferred balance are generated once per month. | No Upfront Savings Plans or Monthly SaaS. |
| Quarterly   | 30         | Invoices for the deferred balance are generated every three months. | Partial Upfront deals with 90-day true-ups. |
| Semi-Annual | 40         | Invoices for the deferred balance are generated every six months. | Split-payment agreements. |
| Annual      | 50         | Invoices for the deferred balance are generated once per year. | Partial Upfront EAs billed yearly. |
| Custom      | 60         | Hourly/Daily or other irregular cycles. | Irregular bridge contracts or non-standard terms. |

## Column ID

ContractCommitmentPaymentInterval

## Display Name

Contract Commitment Payment Interval

## Description

Represents the frequency by which a [contract commitment](#term) is invoiced.

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
