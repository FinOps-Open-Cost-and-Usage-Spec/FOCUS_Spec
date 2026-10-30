# Billing Period

The Billing Period dataset is a supporting dataset that defines the time intervals and statuses associated with an [invoice issuer's](#term:invoice-issuer) billing cycles for grouping and presenting [charges](#term) on invoices. This dataset helps FinOps practitioners better understand how and when they can leverage [Cost and Usage](#ds) and [Invoice Detail](#ds) data for formal financial reporting and showback/chargeback processes.

## Columns<!--SkipTOC-->

| Column                                                                    | Column Type | Feature Level | Allows Nulls | Data Type |
| :------------------------------------------------------------------------ | :---------- | :------------ | :----------- | :-------- |
| [Billing Period Created](#datamodel.billingperiod.billingperiodcreated)   | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period End](#datamodel.billingperiod.billingperiodend)           | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Last Updated](#datamodel.billingperiod.billingperiodlastupdated) | Dimension | Mandatory | False        | Date/Time |
| [Billing Period Start](#datamodel.billingperiod.billingperiodstart)       | Dimension   | Mandatory     | False        | Date/Time |
| [Billing Period Status](#datamodel.billingperiod.billingperiodstatus)     | Dimension   | Mandatory     | False        | String    |
| [Invoice Issuer Name](#datamodel.billingperiod.invoiceissuername)     | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The Billing Period dataset is primarily used to provide context for the [Cost and Usage](#ds) and [Invoice Detail](#ds) datasets. It is joined using the [Billing Period Start](#col) and [Invoice Issuer Name](#col) columns available in those datasets.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Billing Period | Billing Period Start and Invoice Issuer Name | Cost and Usage | Billing Period Start and Invoice Issuer Name |
| Billing Period | Billing Period Start and Invoice Issuer Name | Invoice Detail | Billing Period Start and Invoice Issuer Name |

## Requirements<!--SkipTOC-->

[BillingPeriod](#ds) MUST adhere to the following requirements:

* [BillingPeriod](#ds) column presence MUST adhere to the following requirements:
  * [BillingPeriod](#ds) MUST include [BillingPeriodCreated](#col).
  * [BillingPeriod](#ds) MUST include [BillingPeriodEnd](#col).
  * [BillingPeriod](#ds) MUST include [BillingPeriodLastUpdated](#col).
  * [BillingPeriod](#ds) MUST include [BillingPeriodStart](#col).
  * [BillingPeriod](#ds) MUST include [BillingPeriodStatus](#col).
  * [BillingPeriod](#ds) MUST include [InvoiceIssuerName](#col).
* [BillingPeriod](#ds) MUST conform to [CorrectionHandling](#attr) requirements.
* [BillingPeriod](#ds) MUST conform to [DatasetCompleteness](#attr) requirements.
* [BillingPeriod](#ds) MUST conform to [DatasetConfiguration](#attr) requirements.
* [BillingPeriod](#ds) MUST conform to [DeliveryHandling](#attr) requirements.
* [BillingPeriod](#ds) [FOCUS columns](#term) MUST conform to [FocusColumnHandling](#attr) requirements.
* [BillingPeriod](#ds) [FOCUS columns](#term) MUST conform to [NullHandling](#attr) requirements.
* [BillingPeriod](#ds) [custom columns](#term) MUST conform to [CustomColumnHandling](#attr) requirements.

## Dataset ID<!--SkipTOC-->

BillingPeriod

## Display Name<!--SkipTOC-->

Billing Period

## Description<!--SkipTOC-->

Describes the time intervals and statuses associated with an invoice issuer's billing cycles.

## Version Introduced<!--SkipTOC-->

1.4
