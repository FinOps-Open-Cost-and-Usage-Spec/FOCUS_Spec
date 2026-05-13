# Data Model

The FOCUS data model defines many individual datasets, each comprised of a set of columns, which abide by the attributes outlined in this FOCUS Specification.

## Datasets<!--SkipTOC-->

Datasets are sorted first by Feature Level (i.e., Mandatory, then Conditional), then alphabetically by name.

| Dataset                                             | Dataset Type | Feature Level | Description                                                                                                   |
| --------------------------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------- |
| [Cost and Usage](#datasets.costandusage)            | Transaction  | Mandatory     | Describes the cost and usage incurred through using or purchasing a service provider's resources or services. |
| [Billing Period](#datasets.billingperiod)           | Reference    | Conditional   | Describes the billing periods by which cost and usage is invoiced. |
| [Contract Commitment](#datasets.contractcommitment) | Reference    | Conditional   | Describes the terms of contracts agreed between a service provider and a customer. |
| [Invoice Detail](#datasets.invoicedetail)           | Transaction  | Conditional   | Describes the cost and usage issued on invoices. |

## Requirements<!--SkipTOC-->

DataModel MUST adhere to the following requirements:

* DataModel MUST include [CostAndUsage](#datasets.costandusage).
* DataModel MUST include [BillingPeriod](#datasets.billingperiod) when the invoice issuer supports payable invoices.
* DataModel MUST include [ContractCommitment](#datasets.contractcommitment) when the service provider supports [*contract commitments*](#glossary:contract-commitment).
* DataModel MUST include [InvoiceDetail](#datasets.invoicedetail) when the invoice issuer supports payable invoices.

## Dataset ID<!--SkipTOC-->

DataModel

## Display Name<!--SkipTOC-->

Data Model

## Description<!--SkipTOC-->

The datasets that comprise the FOCUS schema.

## Version Introduced<!--SkipTOC-->

0.5

