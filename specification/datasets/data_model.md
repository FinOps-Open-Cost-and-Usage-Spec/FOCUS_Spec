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
| [SKU Price](#datamodel.skuprice) (preview)           | Reference    | Conditional   | Describes the unit prices offered by a service provider. |

> **Preview:** The [SKU Price](#ds) dataset is a preview in this version of FOCUS. The requirement that the Data Model include [SKU Price](#ds) is excluded from conformance while that dataset is a preview.

## Requirements<!--SkipTOC-->

DataModel MUST adhere to the following requirements:

* DataModel MUST include [CostAndUsage](#ds).
* DataModel MUST include [BillingPeriod](#ds) when the [operating model](#term) [includes payable invoices](#omc).
* DataModel MUST include [ContractCommitment](#ds) when the [operating model](#term) [includes contract commitments](#omc).
* DataModel MUST include [InvoiceDetail](#ds) when the [operating model](#term) includes payable invoices.
* DataModel MUST include [SkuPrice](#ds) when the [operating model](#term) [includes unit pricing](#omc).

## Data Model ID<!--SkipTOC-->

DataModel

## Display Name<!--SkipTOC-->

Data Model

## Description<!--SkipTOC-->

The datasets that comprise the FOCUS schema.

## Version Introduced<!--SkipTOC-->

0.5
