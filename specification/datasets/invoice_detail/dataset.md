# Invoice Detail

The [Invoice Detail](#ds) dataset is a transactional dataset that represents the financial record of [charges](#term) as they appear on invoices provided by an [invoice issuer](#term). This dataset enables FinOps practitioners to perform financial reconciliation, tax reporting, and payment processing tasks. While the [Cost and Usage](#ds) dataset provides granular visibility into consumption, the [Invoice Detail](#ds) dataset ensures alignment with the physical or electronic billing documents.

## Columns<!--SkipTOC-->

| Column                                                                           | Column Type | Feature Level | Allows Nulls | Data Type |
| :------------------------------------------------------------------------------- | :---------- | :------------ | :----------- | :-------- |
| [Billed Cost](#datamodel.invoicedetail.billedcost)                                | Metric      | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datamodel.invoicedetail.billingaccountid)                   | Dimension   | Mandatory     | False        | String    |
| [Billing Currency](#datamodel.invoicedetail.billingcurrency)                      | Dimension   | Mandatory     | False        | String    |
| [Charge Category](#datamodel.invoicedetail.chargecategory)                        | Dimension   | Mandatory     | False        | String    |
| [Billing Period End](#datamodel.invoicedetail.billingperiodend)                   | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datamodel.invoicedetail.billingperiodstart)               | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Created](#datamodel.invoicedetail.invoicedetailcreated)           | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Description](#datamodel.invoicedetail.invoicedetaildescription)   | Dimension   | Mandatory     | True         | String    |
| [Invoice Detail Grain](#datamodel.invoicedetail.invoicedetailgrain)               | Dimension   | Mandatory     | True         | JSON      |
| [Invoice Detail ID](#datamodel.invoicedetail.invoicedetailid)                     | Dimension   | Mandatory     | False        | String    |
| [Invoice Detail Last Updated](#datamodel.invoicedetail.invoicedetaillastupdated)   | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice ID](#datamodel.invoicedetail.invoiceid)                                 | Dimension   | Mandatory     | False        | String    |
| [Invoice Issue Date](#datamodel.invoicedetail.invoiceissuedate)                   | Dimension   | Mandatory     | True        | Date/Time |
| [Invoice Issue Status](#datamodel.invoicedetail.invoiceissuestatus)             | Dimension   | Mandatory     | False        | String    |
| [Invoice Issuer Name](#datamodel.invoicedetail.invoiceissuername)                 | Dimension   | Mandatory     | False        | String    |
| [Payment Currency](#datamodel.invoicedetail.paymentcurrency)                     | Dimension   | Conditional   | False        | String    |
| [Payment Currency Billed Cost](#datamodel.invoicedetail.paymentcurrencybilledcost) | Metric      | Conditional   | False        | Decimal   |
| [Payment Currency Invoice Detail ID](#datamodel.invoicedetail.paymentcurrencyinvoicedetailid) | Dimension | Conditional | False | String |
| [Payment Due Date](#datamodel.invoicedetail.paymentduedate)               | Dimension   | Mandatory     | True         | Date/Time |
| [Payment Terms](#datamodel.invoicedetail.paymentterms)                     | Dimension   | Mandatory     | False        | String    |
| [Purchase Order Number](#datamodel.invoicedetail.purchaseordernumber)             | Dimension   | Conditional   | True        | String    |
| [Reference Invoice ID](#datamodel.invoicedetail.referenceinvoiceid)               | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The [Invoice Detail](#ds) dataset can be joined to the [Cost and Usage](#ds) dataset through [Invoice Issuer Name](#col), [Invoice ID](#col), and (optionally) [Invoice Detail ID](#col).

> **Note:** One or both datasets will need to be aggregated in order to facilitate any comparison.

The timing of [Invoice ID](#col) and [Invoice Detail ID](#col) availability in [Cost and Usage](#ds) varies across data generators. Some data generators populate these values while the [billing period](#term) is still open, while others do not populate them until after the [billing period](#term) is closed and invoices have been issued.

For more information, see the [Invoice Reconciliation](#supportedfeatures.invoicereconciliation) supported feature.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Invoice Detail | Invoice Issuer Name and Invoice ID         | Cost and Usage | Invoice Issuer Name and Invoice ID         |
| Invoice Detail | Invoice Issuer Name, Invoice ID, and Invoice Detail ID  | Cost and Usage | Invoice Issuer Name, Invoice ID, and Invoice Detail ID  |

## Requirements<!--SkipTOC-->

[InvoiceDetail](#ds) MUST adhere to the following requirements:

* [InvoiceDetail](#ds) column presence MUST adhere to the following requirements:
  * [InvoiceDetail](#ds) MUST include [BilledCost](#col).
  * [InvoiceDetail](#ds) MUST include [BillingAccountId](#col).
  * [InvoiceDetail](#ds) MUST include [BillingCurrency](#col).
  * [InvoiceDetail](#ds) MUST include [BillingPeriodEnd](#col).
  * [InvoiceDetail](#ds) MUST include [BillingPeriodStart](#col).
  * [InvoiceDetail](#ds) MUST include [ChargeCategory](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceDetailCreated](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceDetailDescription](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceDetailGrain](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceDetailId](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceDetailLastUpdated](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceId](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceIssueDate](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceIssueStatus](#col).
  * [InvoiceDetail](#ds) MUST include [InvoiceIssuerName](#col).
  * [InvoiceDetail](#ds) MUST include [PaymentCurrency](#col) when the [operating model](#term) [includes billing and payment currency differences](#omc).
  * [InvoiceDetail](#ds) MUST include [PaymentCurrencyBilledCost](#col) when the [operating model](#term) includes billing and payment currency differences.
  * [InvoiceDetail](#ds) MUST include [PaymentCurrencyInvoiceDetailId](#col) when the [operating model](#term) [includes aggregation level currency differences](#omc).
  * [InvoiceDetail](#ds) MUST include [PaymentDueDate](#col).
  * [InvoiceDetail](#ds) MUST include [PaymentTerms](#col).
  * [InvoiceDetail](#ds) MUST include [PurchaseOrderNumber](#col) when the [operating model](#term) [includes purchase order numbers](#omc).
  * [InvoiceDetail](#ds) MUST include [ReferenceInvoiceId](#col).
  * [InvoiceDetail](#ds) MUST include [custom columns](#term) to represent any monetary metric that appears on an invoice issued to a [BillingAccountId](#col) when there is no equivalent [FOCUS column](#term).
* [InvoiceDetail](#ds) MUST conform to [CorrectionHandling](#attr) requirements.
* [InvoiceDetail](#ds) MUST conform to [DatasetCompleteness](#attr) requirements.
* [InvoiceDetail](#ds) MUST conform to [DatasetConfiguration](#attr) requirements.
* [InvoiceDetail](#ds) MUST conform to [DeliveryHandling](#attr) requirements.
* [InvoiceDetail](#ds) MUST represent all invoice line items with a non-zero [BilledCost](#col) on any invoice associated with a [BillingAccountId](#col).
* [InvoiceDetail](#ds) [FOCUS columns](#term) MUST conform to [FocusColumnHandling](#attr) requirements.
* [InvoiceDetail](#ds) [FOCUS columns](#term) MUST conform to [NullHandling](#attr) requirements.
* [InvoiceDetail](#ds) [custom columns](#term) MUST conform to [CustomColumnHandling](#attr) requirements.
* [InvoiceDetail](#ds) documentation MUST adhere to the following requirements:
  * [InvoiceDetail](#ds) documentation MUST specify how [InvoiceDetail](#ds) records correspond to invoice line items.
  * [InvoiceDetail](#ds) documentation MUST specify whether invoice line items with [BilledCost](#col) of 0 are excluded from [InvoiceDetail](#ds).
  * [InvoiceDetail](#ds) documentation MUST describe how columns in the [CostAndUsage](#ds) and [InvoiceDetail](#ds) [dataset instances](#term) represent the invoice issuer's [invoice reconciliation](#term) process.
  * [InvoiceDetail](#ds) documentation MUST be freely accessible to FOCUS consumers.

## Dataset ID<!--SkipTOC-->

InvoiceDetail

## Display Name<!--SkipTOC-->

Invoice Detail

## Description<!--SkipTOC-->

The financial record of [charges](#term) as they appear on invoices provided by an invoice issuer.

## Version Introduced<!--SkipTOC-->

1.4
