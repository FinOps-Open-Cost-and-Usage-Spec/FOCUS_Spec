# Contract Commitment Payment Interval

Contract Commitment Payment Interval represents the frequency by which a [*contract commitment*](#glossary:contract-commitment) is invoiced. For [payment models](#datasets.contractcommitment.contractcommitmentpaymentmodel) involving deferred financial obligations, the Payment Interval denotes the ongoing billing cycle. For models paid upfront, the Payment Interval denotes the single settlement event.

Note: Do not confuse the Contract Commitment Payment Interval with the [Contract Commitment Fulfillment Interval](#datasets.contractcommitment.contractcommitmentfulfillmentinterval). For example, a spend-based commitment discount may have an Hourly Fulfillment Interval (usage reset) but a Monthly Payment Interval (billing cycle).

## Requirements

ContractCommitmentPaymentInterval MUST adhere to the following requirements:

* ContractCommitmentPaymentInterval MUST be of type String.
* ContractCommitmentPaymentInterval MUST NOT be null.
* ContractCommitmentPaymentInterval MUST be one of the allowed values.
* ContractCommitmentPaymentInterval MUST be "One-Time" if [ContractCommitmentPaymentModel](#datasets.contractcommitment.contractcommitmentpaymentmodel) is "All Upfront".
* ContractCommitmentPaymentInterval SHOULD represent a time granularity equal to or lesser than the time granularity represented by [ContractCommitmentDurationType](#datasets.contractcommitment.contractcommitmentdurationtype).

## Column ID

ContractCommitmentPaymentInterval

## Display Name

Contract Commitment Payment Interval

## Description

Represents the frequency by which a [*contract commitment*](#glossary:contract-commitment) is invoiced.

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

| Value       | Sort Order | Description                                                         | Typical Use Case                                  |
| ----------- | ---------- | ------------------------------------------------------------------- | ------------------------------------------------- |
| One-Time    | 10         | A single invoice is generated for the entire obligation. | All Upfront models (e.g., 3yr All-Upfront RI) or single-invoice arrears paid at the end of a term. |
| Monthly     | 20         | Invoices for the deferred balance are generated once per month. | No Upfront Savings Plans or Monthly SaaS. |
| Quarterly   | 30         | Invoices for the deferred balance are generated every three months. | Partial Upfront deals with 90-day true-ups. |
| Semi-Annual | 40         | Invoices for the deferred balance are generated every six months. | Split-payment agreements. |
| Annual      | 50         | Invoices for the deferred balance are generated once per year. | Partial Upfront EAs billed yearly. |
| Custom      | 60         | Hourly/Daily or other irregular cycles. | Irregular bridge contracts or non-standard terms. |

## Introduced (Version)

1.4
