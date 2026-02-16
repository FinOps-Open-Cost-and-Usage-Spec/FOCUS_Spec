# Invoice Handling

## Overview

The Invoice Handling attribute defines how [*FOCUS datasets*](#glossary:FOCUS-dataset) should reflect the information presented on an [*invoice*](#glossary:invoice).

Its purpose is to ensure that all monetary [*charges*](#glossary:charge) (including, but not limited to, usage, taxes, credits, refunds, support, training, and marketplace transactions) are accurately captured and categorized in FOCUS datasets.

FOCUS datasets (including [Cost and Usage](#datasets.costandusage), [Invoice Detail](#datasets.invoicedetail), and [Billing Period](#datasets.billingperiod) *FOCUS datasets*) must provide consistent and complete representations of all invoiced charges to facilitate alignment with the corresponding *invoices* and usage statements they receive from [*invoice issuers*](#datasets.costandusage.invoiceissuername). In practice, this means ensuring that all cost and usage data that appear on an invoice or usage statement, including those not tied to metered usage, are represented in *FOCUS datasets*.

This enables FinOps practitioners to perform [*invoice reconciliation*](#glossary:invoice-reconciliation), financial reporting, and chargeback.

### Invoice Reconciliation and Issuance

Before an [*invoice is issued*](#glossary:issued-invoice), i.e., the [Invoice Status](#datasets.invoicedetail.invoicestatus) (within Invoice Detail *FOCUS dataset*) is set to "Closed", the [data generator](#metadata.datagenerator) must perform a reconciliation to ensure consistency between the invoice, Invoice Detail FOCUS dataset, and Cost and Usage FOCUS dataset.

At the conclusion of this process, the aggregated [Billed Costs](#datasets.invoicedetail.billedcost) in the Invoice Detail *FOCUS dataset* for a given [InvoiceDetail.InvoiceDetailId](#datasets.invoicedetail.invoicedetailid) are expected to match the payable amounts presented on the corresponding invoice line items.

Similarly, the aggregated Billed Cost in the Invoice Detail *FOCUS dataset* for a given InvoiceDetail.InvoiceDetailId is expected to match the corresponding aggregated [Billed Costs](#datasets.costandusage.billedcost) in the Cost and Usage *FOCUS dataset* for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid).

Practitioners may independently perform *invoice reconciliation* by verifying that invoice line items are aligned with data provided in the FOCUS datasets, particularly Cost and Usage, Invoice Detail, and Billing Period.

Once an invoice is issued, it becomes an authoritative financial document, and the information it contains is expected not to change. [*Corrections*](#glossary:correction) to *issued invoice* (including updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period *FOCUS datasets*) may be permitted only in accordance with the [Correction Handling attribute](#attributes.correctionhandling) and must not compromise the integrity of the *issued invoice*.

### Open and Closed Billing Periods

A [*closed billing period*](#glossary:closed-billing-period) represents a billing period for which all planned invoices have been successfully issued by the designated [invoice issuers](#datasets.billingperiod.invoiceissuername), and no additional invoices are expected to be associated with that period, except where explicitly requested by the customer. In contrast, an [*open billing period*](#glossary:open-billing-period) remains subject to ongoing billing activities until it is formally closed.

The Billing Period *FOCUS dataset* provides the necessary context to determine the status of each billing period for a specific invoice issuer. Since *invoice issuer* and *billing period*-related columns are present in all three FOCUS datasets (Billing Period, Cost and Usage, and Invoice Detail), records across the three datasets can be consistently associated with the corresponding billing cycles.

For a *closed billing period*, the data presented in *FOCUS dataset* artifacts is expected not to change. Corrections to *closed billing periods* (including updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period *FOCUS datasets*) may be permitted only in accordance with the [Correction Handling attribute](#attributes.correctionhandling) and must not compromise the integrity of the *closed billing period*.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Defines how a *FOCUS dataset* should reflect details for the information presented on an *invoice*.

## Requirements

InvoiceHandling MUST adhere to the following requirements:

* *FOCUS dataset* MUST account for all monetary line items included on any invoice issued to a BillingAccountId.
* *FOCUS dataset* MAY omit informational line items with zero monetary impact included on invoice only for transparency (e.g., tax exemption notifications, SLA credit details when the credit is already applied to the charged amount).
* InvoiceDetail *FOCUS dataset* MUST have its invoice reconciliation process documented and accessible to practitioners, including a list of columns from both CostAndUsage and InvoiceDetail FOCUS datasets used in reconciliation.
* CostAndUsage *FOCUS dataset* MUST include Custom columns (e.g., x_ChargeSubType) needed to support invoice reconciliation when FOCUS columns are not sufficient.
* CostAndUsage.BillingPeriodStart for a given CostAndUsage.InvoiceId MUST match InvoiceDetail.BillingPeriodStart for the same InvoiceDetail.InvoiceId.
* CostAndUsage.BillingPeriodEnd for a given CostAndUsage.InvoiceId MUST match InvoiceDetail.BillingPeriodEnd for the same InvoiceDetail.InvoiceId.
* The sum of InvoiceDetail.BilledCost for a given InvoiceDetail.InvoiceDetailId MUST match the payable amount provided in the corresponding invoice line items when InvoiceDetail.InvoiceStatus is "Closed".
* The sum of InvoiceDetail.BilledCost for a given InvoiceDetail.InvoiceDetailId MUST match the sum of CostAndUsage.BilledCost for the same CostAndUsage.InvoiceDetailId when InvoiceDetail.InvoiceStatus is "Closed".
* The sum of InvoiceDetail.BilledCost for a given InvoiceDetail.InvoiceDetailId MAY differ from the sum of CostAndUsage.BilledCost for the same CostAndUsage.InvoiceDetailId when InvoiceDetail.InvoiceStatus is "Open".
* [InvoiceDetail.InvoiceDetailCreated](#datasets.invoicedetail.invoicedetailcreated) MUST be earlier than or equal to [BillingPeriod.BillingPeriodLastUpdated](#datasets.billingperiod.billingperiodlastupdated) when the following conditions are met:
  * [BillingPeriod.BillingPeriodStatus](#datasets.billingperiod.billingperiodstatus) is "Closed",
  * given [InvoiceDetail.InvoiceIssuerName](#datasets.invoicedetail.invoiceissuername) matches BillingPeriod.InvoiceIssuerName,
  * and given [InvoiceDetail.BillingPeriodStart](#datasets.invoicedetail.billingperiodstart) matches [BillingPeriod.BillingPeriodStart](#datasets.billingperiod.billingperiodstart).

## Exceptions

None

## Introduced (version)

1.3
