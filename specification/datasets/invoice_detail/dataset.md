# Invoice Detail

The Invoice Detail dataset represents the definitive financial record of charges as they appear on an official invoice issued by a provider.

The specification for the Invoice Detail dataset defines a group of columns that provide qualitative values (dimensions) and quantitative values (metrics) that act as the "Source of Truth" for financial reconciliation, tax reporting, and payment processing. While the [Cost and Usage](#datasets.costandusage) dataset provides granular visibility into consumption, the Invoice Detail dataset ensures alignment with the physical or electronic billing documents. The columns are presented in alphabetical order.

## Columns<!--SkipTOC-->

| Column                                                                           | Column Type | Feature Level | Allows Nulls | Data Type |
| :------------------------------------------------------------------------------- | :---------- | :------------ | :----------- | :-------- |
| [Billed Cost](#datasets.invoicedetail.billedcost)                                | Metric      | Mandatory     | False        | Decimal   |
| [Billing Account ID](#datasets.invoicedetail.billingaccountid)                   | Dimension   | Mandatory     | False        | String    |
| [Billing Currency](#datasets.invoicedetail.billingcurrency)                      | Dimension   | Mandatory     | False        | String    |
| [Billing Period End](#datasets.invoicedetail.billingperiodend)                   | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Start](#datasets.invoicedetail.billingperiodstart)                 | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Created](#datasets.invoicedetail.invoicedetailcreated)           | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Detail Description](#datasets.invoicedetail.invoicedetaildescription)   | Dimension   | Mandatory     | False        | String    |
| [Invoice Detail Grain](#datasets.invoicedetail.invoicedetailgrain)               | Dimension   | Mandatory     | True         | JSON      |
| [Invoice Detail ID](#datasets.invoicedetail.invoicedetailid)                     | Dimension   | Mandatory     | False        | String    |
| [Invoice Detail Last Updated](#datasets.invoicedetail.invoicedetaillastupdated)   | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice ID](#datasets.invoicedetail.invoiceid)                                 | Dimension   | Mandatory     | False        | String    |
| [Invoice Issue Date](#datasets.invoicedetail.invoiceissuedate)                   | Dimension   | Mandatory     | False        | Date/Time |
| [Invoice Issuer Name](#datasets.invoicedetail.invoiceissuername)                 | Dimension   | Mandatory     | False        | String    |
| [Invoice Payment Due Date](#datasets.invoicedetail.invoicepaymentduedate)         | Dimension   | Conditional   | True         | Date/Time |
| [Invoice Payment Terms](#datasets.invoicedetail.invoicepaymentterms)             | Dimension   | Mandatory     | False        | String    |
| [Invoice Status](#datasets.invoicedetail.invoicestatus)                         | Dimension   | Mandatory     | False        | String    |
| [Payment Currency](#datasets.invoicedetail.paymentcurrency)                     | Dimension   | Mandatory     | False        | String    |
| [Payment Currency Billed Cost](#datasets.invoicedetail.paymentcurrencybilledcost) | Metric      | Mandatory     | False        | Decimal   |
| [Payment Order Number](#datasets.invoicedetail.paymentordernumber)               | Dimension   | Conditional   | False        | String    |
| [Reference Invoice ID](#datasets.invoicedetail.referenceinvoiceid)               | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The Invoice Detail dataset can be joined to the Cost and Usage dataset through the use of the Invoice ID and Billing Account ID.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Invoice Detail | Invoice ID         | Cost and Usage | Invoice ID         |
| Invoice Detail | Billing Account ID | Cost and Usage | Billing Account ID |

## Requirements<!--SkipTOC-->

InvoiceDetail adheres to the following requirements:

* InvoiceDetail MUST be present if the invoice issuer supports payable invoices.
* InvoiceDetail MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.
* InvoiceDetail MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* InvoiceDetail MUST conform to [InvoiceHandling](#attributes.invoicehandling) requirements.
* Values in InvoiceDetail MUST align with the official billing documents provided by the [Invoice Issuer Name](#datasets.invoicedetail.invoiceissuername).

## Dataset ID<!--SkipTOC-->

InvoiceDetail

## Display Name<!--SkipTOC-->

Invoice Detail

## Description<!--SkipTOC-->

Describes the definitive financial records and line-item details of an official [*invoice*](#glossary:invoice) provided by an invoice issuer.

## Introduced (version)<!--SkipTOC-->

1.4
