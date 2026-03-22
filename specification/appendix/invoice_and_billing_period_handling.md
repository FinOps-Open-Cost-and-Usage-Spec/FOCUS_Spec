# Invoice and Billing Period Handling

## Overview

A primary use case for FinOps practitioners is the reconciliation of invoices and usage statements. This critical process requires the use of [*FOCUS datasets*](#glossary:FOCUS-dataset), notably the [Cost and Usage](#datasets.costandusage), [Invoice Detail](#datasets.invoicedetail), and [Billing Period](#datasets.billingperiod) datasets.

In practice, successful [*invoice reconciliation*](#glossary:invoice-reconciliation) requires that all monetary data appearing on an invoice or usage statement -- including non-usage charges such as taxes, credits, refunds, support, training, and marketplace transactions -- is accurately captured and categorized within these datasets.

Without this fundamental alignment, downstream processes like invoice reconciliation, financial reporting, and chargeback become unreliable.

### Invoice Reconciliation and Issuance

Before an [*invoice is issued*](#glossary:issued-invoice), i.e., the [Invoice Issue Status](#datasets.invoicedetail.invoiceissuestatus) (within Invoice Detail *FOCUS dataset*) transitions to "Issued", the [data generator](#metadata.datagenerator) is expected to perform a reconciliation to ensure consistency between the invoice, [Invoice Detail](#datasets.invoicedetail) FOCUS dataset, and [Cost and Usage](#datasets.costandusage) FOCUS dataset.

At the conclusion of this process, the aggregated [Billed Costs](#datasets.invoicedetail.billedcost) in the Invoice Detail *FOCUS dataset* for a given [InvoiceDetail.InvoiceDetailId](#datasets.invoicedetail.invoicedetailid) are expected to match the payable amounts presented on the corresponding invoice line items.

Similarly, the aggregated Billed Cost in the Invoice Detail *FOCUS dataset* for a given InvoiceDetail.InvoiceDetailId is expected to match the corresponding aggregated [Billed Costs](#datasets.costandusage.billedcost) in the Cost and Usage *FOCUS dataset* for the same [CostAndUsage.InvoiceDetailId](#datasets.costandusage.invoicedetailid).

Practitioners may independently perform *invoice reconciliation* by verifying that invoice line items are aligned with data delivered in the [*FOCUS dataset artifacts*](#glossary:dataset-artifact), particularly Cost and Usage, Invoice Detail, and Billing Period.

Once an invoice is issued, it becomes an authoritative financial document, and the information it contains is expected not to change. [*Corrections*](#glossary:correction) to an *issued invoice* (including updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period *FOCUS datasets*) may be permitted only in accordance with the [Invoice Issue Status](#datasets.invoicedetail.invoiceissuestatus) requirements and must not compromise the integrity of the *issued invoice*.

Corrections to underlying records that do not impact *invoice reconciliation* are allowed regardless of Invoice Issue Status, but even in this case they may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

### Open and Closed Billing Periods

A [*closed billing period*](#glossary:closed-billing-period) represents a billing period for which all planned invoices have been successfully issued by the designated invoice issuers, and no additional invoices are expected to be associated with that period, except where explicitly requested or approved by the customer. In contrast, an [*open billing period*](#glossary:open-billing-period) remains subject to ongoing billing activities until it is formally closed.

The Billing Period *FOCUS dataset* provides the necessary context to determine the status of each billing period for a specific invoice issuer. Since invoice issuer and *billing period*-related columns are present in all three FOCUS datasets (Billing Period, Cost and Usage, and Invoice Detail), records across the three datasets can be consistently associated with the corresponding billing cycles.

For a *closed billing period*, the data delivered in *FOCUS dataset artifacts* is expected not to change. *Corrections* to *closed billing periods* (including updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period *FOCUS datasets*) may be permitted only in accordance with the [Billing Period Status](#datasets.billingperiod.billingperiodstatus) requirements and must not compromise the integrity of the *closed billing period*.

Corrections that do not impact the integrity of the closed billing period, such as informational or metadata updates, are allowed regardless of Billing Period Status.

If the original closed period is not reopened, corrections that require issuing additional invoices must always be represented in the context of a subsequent *open billing period*. This approach preserves historical financial accuracy, ensures clear temporal boundaries between billing cycles, and guarantees that all corrections are transparently tracked and auditable in future periods.
