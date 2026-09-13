# Billing Period

The Billing Period dataset is a supporting dataset that defines the time intervals and statuses associated with an [*invoice issuer's*](#glossary:invoice-issuer) billing cycles for grouping and presenting [*charges*](#glossary:charge) on invoices. This dataset helps FinOps practitioners better understand how and when they can leverage [Cost and Usage](#datamodel.costandusage) and [Invoice Detail](#datamodel.invoicedetail) data for formal financial reporting and showback/chargeback processes.

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

The Billing Period dataset is primarily used to provide context for the [Cost and Usage](#datamodel.costandusage) and [Invoice Detail](#datamodel.invoicedetail) datasets. It is joined using the Billing Period Start and Invoice Issuer Name columns available in those datasets.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Billing Period | Billing Period Start and Invoice Issuer Name | Cost and Usage | Billing Period Start and Invoice Issuer Name |
| Billing Period | Billing Period Start and Invoice Issuer Name | Invoice Detail | Billing Period Start and Invoice Issuer Name |

## Requirements<!--SkipTOC-->

BillingPeriod MUST adhere to the following requirements:

* BillingPeriod column presence MUST adhere to the following requirements:
  * BillingPeriod MUST include [BillingPeriodCreated](#datamodel.billingperiod.billingperiodcreated).
  * BillingPeriod MUST include [BillingPeriodEnd](#datamodel.billingperiod.billingperiodend).
  * BillingPeriod MUST include [BillingPeriodLastUpdated](#datamodel.billingperiod.billingperiodlastupdated).
  * BillingPeriod MUST include [BillingPeriodStart](#datamodel.billingperiod.billingperiodstart).
  * BillingPeriod MUST include [BillingPeriodStatus](#datamodel.billingperiod.billingperiodstatus).
  * BillingPeriod MUST include [InvoiceIssuerName](#datamodel.billingperiod.invoiceissuername).
* BillingPeriod MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.
* BillingPeriod MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* BillingPeriod MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* BillingPeriod MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* BillingPeriod [*FOCUS columns*](#glossary:FOCUS-column) MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* BillingPeriod *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* BillingPeriod [*custom columns*](#glossary:custom-column) MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.

## Dataset ID<!--SkipTOC-->

BillingPeriod

## Display Name<!--SkipTOC-->

Billing Period

## Description<!--SkipTOC-->

Describes the time intervals and statuses associated with an invoice issuer's billing cycles.

## Version Introduced<!--SkipTOC-->

1.4
