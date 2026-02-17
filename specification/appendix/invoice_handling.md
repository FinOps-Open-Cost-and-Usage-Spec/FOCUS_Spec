# Invoice Handling

## Overview

FinOps practitioners must be able to reconcile [*FOCUS datasets*](#glossary:FOCUS-dataset) (including [Cost and Usage](#datasets.costandusage), [Invoice Detail](#datasets.invoicedetail), and [Billing Period](#datasets.billingperiod) datasets) with the corresponding [*invoices*](#glossary:invoice) and usage statements they receive from [*invoice issuers*](#glossary:InvoiceIssuer). 

In practice, this means ensuring that all monetary data appearing on an invoice or usage statement, including data not tied to metered usage (such as taxes, credits, refunds, support, training, and marketplace transactions), is accurately captured and categorized in *FOCUS datasets*. 

Without this alignment, it becomes difficult to perform accurate [*invoice reconciliation*](#glossary:invoice-reconciliation), financial reporting, and chargeback.

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
