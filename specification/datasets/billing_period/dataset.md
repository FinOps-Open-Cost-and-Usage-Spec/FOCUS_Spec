# Billing Period

The Billing Period dataset is a supporting dataset that defines the time intervals and statuses associated with an invoice issuer's billing cycles for grouping and presenting [*charges*](#glossary:charge) on invoices.  This dataset helps FinOps practitioners better understand how and when they can leverage [Cost and Usage](#datasets.costandusage) and [Invoice Detail](#datasets.invoicedetail) data for formal financial reporting and showback/chargeback processes.

## Columns<!--SkipTOC-->

| Column                                                                    | Column Type | Feature Level | Allows Nulls | Data Type |
| :------------------------------------------------------------------------ | :---------- | :------------ | :----------- | :-------- |
| [Billing Period Created](#datasets.billingperiod.billingperiodcreated)   | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period End](#datasets.billingperiod.billingperiodend)           | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Last Updated](#datasets.billingperiod.billingperiodlastupdated) | Dimension | Mandatory | False        | Date/Time |
| [Billing Period Start](#datasets.billingperiod.billingperiodstart)       | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Status](#datasets.billingperiod.billingperiodstatus)     | Dimension   | Mandatory     | False        | String    |
| [Invoice Issuer Name](#datasets.billingperiod.invoiceissuername)     | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The Billing Period dataset is primarily used to provide context for the [Cost and Usage](#datasets.costandusage) and [Invoice Detail](#datasets.invoicedetail) datasets. It is joined using the Billing Period Start and Invoice Issuer Name columns available in those datasets.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Billing Period | Billing Period Start and Invoice Issuer Name | Cost and Usage | Billing Period Start and Invoice Issuer Name |
| Billing Period | Billing Period Start and Invoice Issuer Name | Invoice Detail | Billing Period Start and Invoice Issuer Name |

## Requirements<!--SkipTOC-->

BillingPeriod MUST adhere to the following requirements:

* BillingPeriod MUST be present when the invoice issuer supports payable invoices.
* The presence of columns in BillingPeriod MUST adhere to the following requirements:
  * BillingPeriod MUST include [BillingPeriodCreated](#datasets.billingperiod.billingperiodcreated).
  * BillingPeriod MUST include [BillingPeriodEnd](#datasets.billingperiod.billingperiodend).
  * BillingPeriod MUST include [BillingPeriodLastUpdated](#datasets.billingperiod.billingperiodlastupdated).
  * BillingPeriod MUST include [BillingPeriodStart](#datasets.billingperiod.billingperiodstart).
  * BillingPeriod MUST include [BillingPeriodStatus](#datasets.billingperiod.billingperiodstatus).
  * BillingPeriod MUST include [InvoiceIssuerName](#datasets.billingperiod.invoiceissuername).
* BillingPeriod MUST conform to [ColumnHandling](#attributes.columnhandling) requirements.
* BillingPeriod MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.

## Dataset ID<!--SkipTOC-->

BillingPeriod

## Display Name<!--SkipTOC-->

Billing Period

## Description<!--SkipTOC-->

Describes the time intervals and statuses associated with an invoice issuer's billing cycles.

## Introduced (version)<!--SkipTOC-->

1.4