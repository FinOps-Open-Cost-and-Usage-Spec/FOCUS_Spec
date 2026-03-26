# Invoice Detail

The Invoice Detail dataset is a transactional dataset that represents the financial record of [*charges*](#glossary:charge) as they appear on invoices provided by an invoice issuer. This dataset enables FinOps practitioners to perform financial reconciliation, tax reporting, and payment processing tasks. While the [Cost and Usage](#datasets.costandusage) dataset provides granular visibility into consumption, the Invoice Detail dataset ensures alignment with the physical or electronic billing documents.

## Columns<!--SkipTOC-->

| Column                                                                           | Column Type | Feature Level | Allows Nulls | Data Type |
| :------------------------------------------------------------------------------- | :---------- | :------------ | :----------- | :-------- |
| [Billed Cost](#datasets.invoicedetail.billedcost)                                | Metric      | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datasets.invoicedetail.billingaccountid)                   | Dimension   | Mandatory     | False        | String    |
| [Billing Currency](#datasets.invoicedetail.billingcurrency)                      | Dimension   | Mandatory     | False        | String    |
| [Charge Category](#datasets.invoicedetail.chargecategory)                        | Dimension   | Mandatory     | False        | String    |
| [Billing Period End](#datasets.invoicedetail.billingperiodend)                   | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datasets.invoicedetail.billingperiodstart)               | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Created](#datasets.invoicedetail.invoicedetailcreated)           | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Description](#datasets.invoicedetail.invoicedetaildescription)   | Dimension   | Mandatory     | True         | String    |
| [Invoice Detail Grain](#datasets.invoicedetail.invoicedetailgrain)               | Dimension   | Mandatory     | True         | JSON      |
| [Invoice Detail ID](#datasets.invoicedetail.invoicedetailid)                     | Dimension   | Mandatory     | False        | String    |
| [Invoice Detail Last Updated](#datasets.invoicedetail.invoicedetaillastupdated)   | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice ID](#datasets.invoicedetail.invoiceid)                                 | Dimension   | Mandatory     | False        | String    |
| [Invoice Issue Date](#datasets.invoicedetail.invoiceissuedate)                   | Dimension   | Mandatory     | True        | Date/Time |
| [Invoice Issue Status](#datasets.invoicedetail.invoiceissuestatus)             | Dimension   | Mandatory     | False        | String    |
| [Invoice Issuer Name](#datasets.invoicedetail.invoiceissuername)                 | Dimension   | Mandatory     | False        | String    |
| [Payment Currency](#datasets.invoicedetail.paymentcurrency)                     | Dimension   | Mandatory     | False        | String    |
| [Payment Currency Billed Cost](#datasets.invoicedetail.paymentcurrencybilledcost) | Metric      | Conditional   | False        | Decimal   |
| [Payment Currency Invoice Detail ID](#datasets.invoicedetail.paymentcurrencyinvoicedetailid) | Dimension | Conditional | False | String |
| [Payment Due Date](#datasets.invoicedetail.paymentduedate)               | Dimension   | Mandatory     | True         | Date/Time |
| [Payment Terms](#datasets.invoicedetail.paymentterms)                     | Dimension   | Mandatory     | False        | String    |
| [Purchase Order Number](#datasets.invoicedetail.purchaseordernumber)             | Dimension   | Conditional   | True        | String    |
| [Reference Invoice ID](#datasets.invoicedetail.referenceinvoiceid)               | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The Invoice Detail dataset can be joined to the [Cost and Usage](#datasets.costandusage) dataset through Invoice Issuer Name, Invoice ID, and (optionally) Invoice Detail ID. Take note: one or both datasets will need to be aggregated in order to facilitate any comparison.

The timing of Invoice ID and Invoice Detail ID availability in Cost and Usage varies across data generators. Some data generators populate these values while the [*billing period*](#glossary:billing-period) is still open, while others do not populate them until after the *billing period* is closed and invoices have been issued.

For more information, see the [Invoice Reconciliation](#supportedfeatures.invoicereconciliation) supported feature.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Invoice Detail | Invoice Issuer Name and Invoice ID         | Cost and Usage | Invoice Issuer Name and Invoice ID         |
| Invoice Detail | Invoice Issuer Name, Invoice ID, and Invoice Detail ID  | Cost and Usage | Invoice Issuer Name, Invoice ID, and Invoice Detail ID  |

## Requirements<!--SkipTOC-->

InvoiceDetail MUST adhere to the following requirements:

* InvoiceDetail MUST be present if the invoice issuer supports payable invoices.
* The presence of columns in InvoiceDetail MUST adhere to the following requirements:
  * InvoiceDetail MUST include [BilledCost](#datasets.invoicedetail.billedcost).
  * InvoiceDetail MUST include [BillingAccountId](#datasets.invoicedetail.billingaccountid).
  * InvoiceDetail MUST include [BillingCurrency](#datasets.invoicedetail.billingcurrency).
  * InvoiceDetail MUST include [BillingPeriodEnd](#datasets.invoicedetail.billingperiodend).
  * InvoiceDetail MUST include [BillingPeriodStart](#datasets.invoicedetail.billingperiodstart).
  * InvoiceDetail MUST include [ChargeCategory](#datasets.invoicedetail.chargecategory).
  * InvoiceDetail MUST include [InvoiceDetailCreated](#datasets.invoicedetail.invoicedetailcreated).
  * InvoiceDetail MUST include [InvoiceDetailDescription](#datasets.invoicedetail.invoicedetaildescription).
  * InvoiceDetail MUST include [InvoiceDetailGrain](#datasets.invoicedetail.invoicedetailgrain).
  * InvoiceDetail MUST include [InvoiceDetailId](#datasets.invoicedetail.invoicedetailid).
  * InvoiceDetail MUST include [InvoiceDetailLastUpdated](#datasets.invoicedetail.invoicedetaillastupdated).
  * InvoiceDetail MUST include [InvoiceId](#datasets.invoicedetail.invoiceid).
  * InvoiceDetail MUST include [InvoiceIssueDate](#datasets.invoicedetail.invoiceissuedate).
  * InvoiceDetail MUST include [InvoiceIssueStatus](#datasets.invoicedetail.invoiceissuestatus).
  * InvoiceDetail MUST include [InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername).
  * InvoiceDetail MUST include [PaymentCurrency](#datasets.invoicedetail.paymentcurrency) if the invoice issuer supports billing and payment in different currencies.
  * InvoiceDetail MUST include [PaymentCurrencyBilledCost](#datasets.invoicedetail.paymentcurrencybilledcost) if the invoice issuer supports billing and payment in different currencies.
  * InvoiceDetail MUST include [PaymentCurrencyInvoiceDetailId](#datasets.invoicedetail.paymentcurrencyinvoicedetailid) if the invoice issuer represents billing currency and payment currency at different aggregation levels on payable invoices.
  * InvoiceDetail MUST include [PaymentDueDate](#datasets.invoicedetail.paymentduedate).
  * InvoiceDetail MUST include [PaymentTerms](#datasets.invoicedetail.paymentterms).
  * InvoiceDetail MUST include [PurchaseOrderNumber](#datasets.invoicedetail.purchaseordernumber) if the invoice issuer supports customer input of purchase order numbers.
  * InvoiceDetail MUST include [ReferenceInvoiceId](#datasets.invoicedetail.referenceinvoiceid).
* InvoiceDetail MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.
* InvoiceDetail MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.
* InvoiceDetail MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* InvoiceDetail MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* InvoiceDetail MUST represent all invoice line items with a non-zero BilledCost on any invoice associated with a BillingAccountId.
* InvoiceDetail MUST include custom columns to represent any monetary metric that appears on an invoice issued to a BillingAccountId when there is no equivalent FOCUS column.
* InvoiceDetail documentation MUST adhere to the following requirements:
  * InvoiceDetail documentation MUST specify how InvoiceDetail records correspond to invoice line items.
  * InvoiceDetail documentation MUST specify whether invoice line items with BilledCost of 0 are excluded from InvoiceDetail.
  * InvoiceDetail documentation MUST describe how columns in the CostAndUsage and InvoiceDetail datasets represent the invoice issuer's [*invoice reconciliation*](#glossary:invoice-reconciliation) process.
  * InvoiceDetail documentation MUST be freely accessible to FOCUS consumers.

## Dataset ID<!--SkipTOC-->

InvoiceDetail

## Display Name<!--SkipTOC-->

Invoice Detail

## Description<!--SkipTOC-->

The financial record of *charges* as they appear on invoices provided by an invoice issuer.

## Introduced (version)<!--SkipTOC-->

1.4
