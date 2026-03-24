# Invoice and Billing Period Handling

## Overview

A primary use case for FinOps practitioners is the reconciliation of invoices and usage statements. In FOCUS, this process is supported through [*FOCUS datasets*](#glossary:FOCUS-dataset), notably the [Cost and Usage](#datasets.costandusage), [Invoice Detail](#datasets.invoicedetail), and [Billing Period](#datasets.billingperiod) datasets.

In the context of FOCUS, successful [*invoice reconciliation*](#glossary:invoice-reconciliation) relies on all monetary data appearing on an invoice or usage statement (including non-usage charges such as taxes, credits, refunds, support, training, and marketplace transactions) being accurately captured and categorized in these datasets.

Without this fundamental alignment, downstream processes like financial reporting and chargeback become unreliable.

### Invoice Reconciliation and Issuance

Before an [*invoice is issued*](#glossary:issued-invoice), i.e., before the [Invoice Issue Status](#datasets.invoicedetail.invoiceissuestatus) in the Invoice Detail dataset transitions to "Issued", data generators typically perform internal *invoice reconciliation* to ensure consistency between the invoice, the Invoice Detail dataset, and the Cost and Usage dataset.

At the conclusion of this process, a key objective is for the aggregated [Billed Costs](#datasets.invoicedetail.billedcost) in the Invoice Detail dataset for a given [Invoice Detail ID](#datasets.invoicedetail.invoicedetailid) to align with the payable amounts presented on the corresponding invoice line items. This alignment is performed across [Invoice ID](#datasets.invoicedetail.invoiceid), Invoice Detail ID, and [Invoice Issuer](#datasets.invoicedetail.invoiceissuername).

Similarly, practitioners rely on the aggregated Billed Costs in the Invoice Detail dataset matching the aggregated [Billed Costs](#datasets.costandusage.billedcost) in the Cost and Usage dataset for the same identifiers.

Practitioners may perform *invoice reconciliation* independently by verifying that invoice line items align with data delivered in [*FOCUS dataset artifacts*](#glossary:dataset-artifact), particularly Cost and Usage, Invoice Detail, and Billing Period.

Once an invoice is issued, it becomes an authoritative financial document, and the information it contains is expected not to change.

[*Corrections*](#glossary:correction) related to *issued invoices* (i.e., updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period datasets) are permitted in accordance with the Invoice Issue Status requirements, as well as the Billed Cost requirements in both Invoice Detail and Cost and Usage datasets. In other words, such *corrections* are typically performed upon explicit request or approval by the customer, provided that they do not compromise the integrity of the issued invoice.

*Corrections* to underlying records that do not impact *invoice reconciliation* are allowed regardless of Invoice Issue Status. However, even in this case, they may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

### Open and Closed Billing Periods

A [*closed billing period*](#glossary:closed-billing-period) represents a billing period for which all anticipated invoices have been successfully issued by the designated invoice issuers, and no additional invoices are generally expected to be associated with that period, except where explicitly requested or approved by the customer. In contrast, an [*open billing period*](#glossary:open-billing-period) remains subject to ongoing billing activities until it is formally closed.

The Billing Period dataset provides the necessary context to determine the status of each billing period for a specific invoice issuer. Since invoice issuer and *billing period*-related columns are present in all three *FOCUS datasets* (Billing Period, Cost and Usage, and Invoice Detail), records across the three datasets can be consistently associated with the corresponding billing cycles.

*Corrections* related to *closed billing periods* (i.e., updates, additions, or omissions of underlying records in Cost and Usage, Invoice Detail, and Billing Period *FOCUS datasets*) are permitted in accordance with the [Billing Period Status](#datasets.billingperiod.billingperiodstatus) requirements, as well as the Billed Cost requirements in both Invoice Detail and Cost and Usage datasets. In other words, such *corrections* are typically performed upon explicit request or approval by the customer, provided that they do not compromise the integrity of the *closed billing period*.

*Corrections* to underlying records that do not impact the integrity of the *closed billing period* or *invoice reconciliation*, such as informational or metadata updates, are allowed regardless of Billing Period Status.

If the original *closed billing period* is not reopened, corrections that require issuing additional invoices are best represented by associating them with a subsequent *open billing period*. This approach preserves historical financial accuracy, ensures clear temporal boundaries between billing cycles, and guarantees that all corrections are transparently tracked and auditable in future periods.
