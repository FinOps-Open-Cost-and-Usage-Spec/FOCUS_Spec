# Invoice Detail

The Invoice Detail dataset is a transactional dataset that represents the financial record of [*charges*](#glossary:charges) as they appear on invoices provided by an invoice issuer. This dataset enables FinOps practitioners to perform financial reconciliation, tax reporting, and payment processing tasks. While the [Cost and Usage](#datasets.costandusage) dataset provides granular visibility into consumption, the Invoice Detail dataset ensures alignment with the physical or electronic billing documents.

## Columns<!--SkipTOC-->

| Column                                                                           | Column Type | Feature Level | Allows Nulls | Data Type |
| :------------------------------------------------------------------------------- | :---------- | :------------ | :----------- | :-------- |
| [Billed Cost](#datasets.invoicedetail.billedcost)                                | Metric      | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datasets.invoicedetail.billingaccountid)                   | Dimension   | Mandatory     | False        | String    |
| [Billing Currency](#datasets.invoicedetail.billingcurrency)                      | Dimension   | Mandatory     | False        | String    |
| [Billing Period End](#datasets.invoicedetail.billingperiodend)                   | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datasets.invoicedetail.billingperiodstart)                 | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Created](#datasets.invoicedetail.invoicedetailcreated)           | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Description](#datasets.invoicedetail.invoicedetaildescription)   | Dimension   | Mandatory     | True         | String    |
| [Invoice Detail Grain](#datasets.invoicedetail.invoicedetailgrain)               | Dimension   | Mandatory     | True         | JSON      |
| [Invoice Detail ID](#datasets.invoicedetail.invoicedetailid)                     | Dimension   | Mandatory     | False        | String    |
| [Invoice Detail Last Updated](#datasets.invoicedetail.invoicedetaillastupdated)   | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice ID](#datasets.invoicedetail.invoiceid)                                 | Dimension   | Mandatory     | False        | String    |
| [Invoice Issue Date](#datasets.invoicedetail.invoiceissuedate)                   | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Issuer Name](#datasets.invoicedetail.invoiceissuername)                 | Dimension   | Mandatory     | False        | String    |
| [Invoice Status](#datasets.invoicedetail.invoicestatus)                         | Dimension   | Mandatory     | False        | String    |
| [Payment Currency](#datasets.invoicedetail.paymentcurrency)                     | Dimension   | Mandatory     | False        | String    |
| [Payment Currency Billed Cost](#datasets.invoicedetail.paymentcurrencybilledcost) | Metric      | Mandatory     | False        | Decimal   |
| [Payment Due Date](#datasets.invoicedetail.invoicepaymentduedate)         | Dimension   | Mandatory   | True         | Date/Time |
| [Payment Terms](#datasets.invoicedetail.invoicepaymentterms)             | Dimension   | Mandatory     | False        | String    |
| [Purchase Order Number](#datasets.invoicedetail.purchaseordernumber)               | Dimension   | Conditional   | False        | String    |
| [Reference Invoice ID](#datasets.invoicedetail.referenceinvoiceid)               | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The Invoice Detail dataset can be joined to the [Cost and Usage](#dataset.costandusage) dataset through the use of either Invoice ID or Invoice Detail ID.  Take note: one or both datasets will need to be aggregated in order to facilitate any comparison.  For more information, see the Invoice Reconciliation(#supportedfeatures.invoicereconciliation) supported feature.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Invoice Detail | Invoice ID         | Cost and Usage | Invoice ID         |
| Invoice Detail | Invoice Detail ID  | Cost and Usage | Invoice Detail ID  |

## Requirements<!--SkipTOC-->

InvoiceDetail adheres to the following requirements:

* InvoiceDetail MUST be present if the invoice issuer supports payable invoices.
* InvoiceDetail MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.
* InvoiceDetail MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* InvoiceDetail MUST conform to [InvoiceHandling](#attributes.invoicehandling) requirements.

## Dataset ID<!--SkipTOC-->

InvoiceDetail

## Display Name<!--SkipTOC-->

Invoice Detail

## Description<!--SkipTOC-->

The financial record of *charges* as they appear on invoices provided by an invoice issuer.

## Introduced (version)<!--SkipTOC-->

1.4
