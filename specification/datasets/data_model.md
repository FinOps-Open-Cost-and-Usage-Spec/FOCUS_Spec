# Data Model

The FOCUS data model defines many individual datasets, each comprised of a set of columns, which abide by the attributes outlined in this FOCUS Specification.

## Datasets<!--SkipTOC-->

Datasets are sorted first by Feature Level (i.e., Mandatory, then Conditional), then alphabetically by name.

| Dataset                                             | Dataset Type | Feature Level | Description                                                                                                   |
| --------------------------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------- |
| [Cost and Usage](#datamodel.costandusage)            | Transaction  | Mandatory     | Describes the cost and usage incurred through using or purchasing a service provider's resources or services. |
| [Billing Period](#datamodel.billingperiod)           | Reference    | Conditional   | Describes the billing periods by which cost and usage is invoiced. |
| [Contract Commitment](#datamodel.contractcommitment) | Reference    | Conditional   | Describes the terms of contracts agreed between a service provider and a customer. |
| [Invoice Detail](#datamodel.invoicedetail)           | Transaction  | Conditional   | Describes the cost and usage issued on invoices. |

## Requirements<!--SkipTOC-->

DataModel MUST adhere to the following requirements:

* DataModel MUST include [CostAndUsage](#datamodel.costandusage).
* DataModel MUST include [BillingPeriod](#datamodel.billingperiod) when the [*operating model*](#glossary:operating-model) [includes payable invoices](#conditions.includespayableinvoices).
* DataModel MUST include [ContractCommitment](#datamodel.contractcommitment) when the *operating model* [includes contract commitments](#conditions.includescontractcommitments).
* DataModel MUST include [InvoiceDetail](#datamodel.invoicedetail) when the *operating model* includes payable invoices.

## Data Model ID<!--SkipTOC-->

DataModel

## Display Name<!--SkipTOC-->

Data Model

## Description<!--SkipTOC-->

The datasets that comprise the FOCUS schema.

## Version Introduced<!--SkipTOC-->

0.5
