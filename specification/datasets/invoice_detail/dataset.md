# Invoice Detail

The Invoice Detail dataset is a transactional dataset that represents the financial record of [*charges*](#glossary:charge) as they appear on invoices provided by an [*invoice issuer*](#glossary:invoice-issuer). This dataset enables FinOps practitioners to perform financial reconciliation, tax reporting, and payment processing tasks. While the [Cost and Usage](#datamodel.costandusage) dataset provides granular visibility into consumption, the Invoice Detail dataset ensures alignment with the physical or electronic billing documents.

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
| [Payment Currency](#datamodel.invoicedetail.paymentcurrency)                     | Dimension   | [Conditional](#operatingmodelconditions.includesbillingandpaymentcurrencydifferences)   | False        | String    |
| [Payment Currency Billed Cost](#datamodel.invoicedetail.paymentcurrencybilledcost) | Metric      | [Conditional](#operatingmodelconditions.includesbillingandpaymentcurrencydifferences)   | False        | Decimal   |
| [Payment Currency Invoice Detail ID](#datamodel.invoicedetail.paymentcurrencyinvoicedetailid) | Dimension | [Conditional](#operatingmodelconditions.includesaggregationlevelcurrencydifferences) | False | String |
| [Payment Due Date](#datamodel.invoicedetail.paymentduedate)               | Dimension   | Mandatory     | True         | Date/Time |
| [Payment Terms](#datamodel.invoicedetail.paymentterms)                     | Dimension   | Mandatory     | False        | String    |
| [Purchase Order Number](#datamodel.invoicedetail.purchaseordernumber)             | Dimension   | [Conditional](#operatingmodelconditions.includespurchaseordernumbers)   | True        | String    |
| [Reference Invoice ID](#datamodel.invoicedetail.referenceinvoiceid)               | Dimension   | Mandatory     | False        | String    |

## Relationships<!--SkipTOC-->

The Invoice Detail dataset can be joined to the [Cost and Usage](#datamodel.costandusage) dataset through Invoice Issuer Name, Invoice ID, and (optionally) Invoice Detail ID. Take note: one or both datasets will need to be aggregated in order to facilitate any comparison.

The timing of Invoice ID and Invoice Detail ID availability in Cost and Usage varies across data generators. Some data generators populate these values while the [*billing period*](#glossary:billing-period) is still open, while others do not populate them until after the *billing period* is closed and invoices have been issued.

For more information, see the [Invoice Reconciliation](#supportedfeatures.invoicereconciliation) supported feature.

| Dataset A      | Dataset A Column   | Dataset B      | Dataset B Column   |
| :------------- | :----------------- | :------------- | :----------------- |
| Invoice Detail | Invoice Issuer Name and Invoice ID         | Cost and Usage | Invoice Issuer Name and Invoice ID         |
| Invoice Detail | Invoice Issuer Name, Invoice ID, and Invoice Detail ID  | Cost and Usage | Invoice Issuer Name, Invoice ID, and Invoice Detail ID  |

## Requirements<!--SkipTOC-->

InvoiceDetail MUST adhere to the following requirements:

* InvoiceDetail column presence MUST adhere to the following requirements:
  * InvoiceDetail MUST include [BilledCost](#datamodel.invoicedetail.billedcost).
  * InvoiceDetail MUST include [BillingAccountId](#datamodel.invoicedetail.billingaccountid).
  * InvoiceDetail MUST include [BillingCurrency](#datamodel.invoicedetail.billingcurrency).
  * InvoiceDetail MUST include [BillingPeriodEnd](#datamodel.invoicedetail.billingperiodend).
  * InvoiceDetail MUST include [BillingPeriodStart](#datamodel.invoicedetail.billingperiodstart).
  * InvoiceDetail MUST include [ChargeCategory](#datamodel.invoicedetail.chargecategory).
  * InvoiceDetail MUST include [InvoiceDetailCreated](#datamodel.invoicedetail.invoicedetailcreated).
  * InvoiceDetail MUST include [InvoiceDetailDescription](#datamodel.invoicedetail.invoicedetaildescription).
  * InvoiceDetail MUST include [InvoiceDetailGrain](#datamodel.invoicedetail.invoicedetailgrain).
  * InvoiceDetail MUST include [InvoiceDetailId](#datamodel.invoicedetail.invoicedetailid).
  * InvoiceDetail MUST include [InvoiceDetailLastUpdated](#datamodel.invoicedetail.invoicedetaillastupdated).
  * InvoiceDetail MUST include [InvoiceId](#datamodel.invoicedetail.invoiceid).
  * InvoiceDetail MUST include [InvoiceIssueDate](#datamodel.invoicedetail.invoiceissuedate).
  * InvoiceDetail MUST include [InvoiceIssueStatus](#datamodel.invoicedetail.invoiceissuestatus).
  * InvoiceDetail MUST include [InvoiceIssuerName](#datamodel.invoicedetail.invoiceissuername).
  * InvoiceDetail MUST include [PaymentCurrency](#datamodel.invoicedetail.paymentcurrency) when the [*operating model*](#glossary:operating-model) [includes billing and payment currency differences](#operatingmodelconditions.includesbillingandpaymentcurrencydifferences).
  * InvoiceDetail MUST include [PaymentCurrencyBilledCost](#datamodel.invoicedetail.paymentcurrencybilledcost) when the *operating model* [includes billing and payment currency differences](#operatingmodelconditions.includesbillingandpaymentcurrencydifferences).
  * InvoiceDetail MUST include [PaymentCurrencyInvoiceDetailId](#datamodel.invoicedetail.paymentcurrencyinvoicedetailid) when the *operating model* [includes aggregation level currency differences](#operatingmodelconditions.includesaggregationlevelcurrencydifferences).
  * InvoiceDetail MUST include [PaymentDueDate](#datamodel.invoicedetail.paymentduedate).
  * InvoiceDetail MUST include [PaymentTerms](#datamodel.invoicedetail.paymentterms).
  * InvoiceDetail MUST include [PurchaseOrderNumber](#datamodel.invoicedetail.purchaseordernumber) when the *operating model* [includes purchase order numbers](#operatingmodelconditions.includespurchaseordernumbers).
  * InvoiceDetail MUST include [ReferenceInvoiceId](#datamodel.invoicedetail.referenceinvoiceid).
  * InvoiceDetail MUST include [*custom columns*](#glossary:custom-column) to represent any monetary metric that appears on an invoice issued to a BillingAccountId when there is no equivalent [*FOCUS column*](#glossary:FOCUS-column).
* InvoiceDetail MUST conform to [CorrectionHandling](#attributes.correctionhandling) requirements.
* InvoiceDetail MUST conform to [DatasetCompleteness](#attributes.datasetcompleteness) requirements.
* InvoiceDetail MUST conform to [DatasetConfiguration](#attributes.datasetconfiguration) requirements.
* InvoiceDetail MUST conform to [DeliveryHandling](#attributes.deliveryhandling) requirements.
* InvoiceDetail MUST represent all invoice line items with a non-zero BilledCost on any invoice associated with a BillingAccountId.
* InvoiceDetail [*FOCUS columns*](#glossary:FOCUS-column) MUST conform to [FocusColumnHandling](#attributes.focuscolumnhandling) requirements.
* InvoiceDetail *FOCUS columns* MUST conform to [NullHandling](#attributes.nullhandling) requirements.
* InvoiceDetail *custom columns* MUST conform to [CustomColumnHandling](#attributes.customcolumnhandling) requirements.
* InvoiceDetail documentation MUST adhere to the following requirements:
  * InvoiceDetail documentation MUST specify how InvoiceDetail records correspond to invoice line items.
  * InvoiceDetail documentation MUST specify whether invoice line items with BilledCost of 0 are excluded from InvoiceDetail.
  * InvoiceDetail documentation MUST describe how columns in the CostAndUsage and InvoiceDetail [*dataset instances*](#glossary:dataset-instance) represent the invoice issuer's [*invoice reconciliation*](#glossary:invoice-reconciliation) process.
  * InvoiceDetail documentation MUST be freely accessible to FOCUS consumers.

## Dataset ID<!--SkipTOC-->

InvoiceDetail

## Display Name<!--SkipTOC-->

Invoice Detail

## Description<!--SkipTOC-->

The financial record of *charges* as they appear on invoices provided by an invoice issuer.

## Version Introduced<!--SkipTOC-->

1.4
