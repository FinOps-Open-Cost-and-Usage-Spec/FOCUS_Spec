# Invoice and Billing Period Handling

## Overview

A primary use case for FinOps practitioners is the reconciliation of invoices and usage statements. In FOCUS, this process is supported through [FOCUS datasets](#term), notably the [Cost and Usage](#ds), [Invoice Detail](#ds), and [Billing Period](#ds) datasets.

In the context of FOCUS, successful [invoice reconciliation](#term) relies on all monetary data appearing on an invoice or usage statement (including non-usage charges such as taxes, credits, refunds, support, training, and marketplace transactions) being accurately captured and categorized in these datasets.

Without this fundamental alignment, downstream processes like financial reporting and chargeback become unreliable.

### Invoice Reconciliation and Issuance

Before an [invoice is issued](#term:issued-invoice), i.e., before the [Invoice Issue Status](#col) in the [Invoice Detail](#ds) dataset transitions to "Issued", data generators typically perform internal [invoice reconciliation](#term) to ensure consistency between the invoice, the [Invoice Detail](#ds) dataset, and the [Cost and Usage](#ds) dataset.

At the conclusion of this process, a key objective is for the aggregated [Billed Costs](#col:InvoiceDetail.BilledCost) in the [Invoice Detail](#ds) dataset for a given [Invoice Detail ID](#col:InvoiceDetail.InvoiceDetailId) to align with the payable amounts presented on the corresponding invoice line items. This alignment is performed across [Invoice ID](#col:InvoiceDetail.InvoiceId), Invoice Detail ID, and [Invoice Issuer](#col:InvoiceDetail.InvoiceIssuerName).

Similarly, practitioners rely on the aggregated Billed Costs in the [Invoice Detail](#ds) dataset to reconcile with the aggregated [Billed Costs](#col:CostAndUsage.BilledCost) in the [Cost and Usage](#ds) dataset for the same identifiers, subject to [Rounding Variance Tolerance](#appendix.roundingvariancetolerance).

Practitioners may perform [invoice reconciliation](#term) independently by verifying that invoice line items align with data delivered in [FOCUS dataset artifacts](#term:dataset-artifact), particularly [Cost and Usage](#ds), [Invoice Detail](#ds), and Billing Period.

Once an invoice is issued, it becomes an authoritative financial document, and the information it contains is expected not to change.

[Corrections](#term) related to [issued invoices](#term) (i.e., updates, additions, or omissions of underlying records in [Cost and Usage](#ds), [Invoice Detail](#ds), and Billing Period datasets) are permitted in accordance with the [Invoice Issue Status](#col) requirements, as well as the Billed Cost requirements in both [Invoice Detail](#ds) and [Cost and Usage](#ds) datasets. In other words, such [corrections](#term) are typically performed upon explicit request or approval by the customer, provided that they do not compromise the integrity of the issued invoice.

[Corrections](#term) to underlying records that do not impact [invoice reconciliation](#term) are allowed regardless of [Invoice Issue Status](#col). However, even in this case, they may reduce auditability and traceability or affect downstream processes (e.g., cost allocation, chargeback, reporting).

### Open and Closed Billing Periods

A [closed billing period](#term) represents a billing period for which all anticipated invoices have been successfully issued by the designated [invoice issuers](#term), and no additional invoices are generally expected to be associated with that period, except where explicitly requested or approved by the customer. In contrast, an [open billing period](#term) remains subject to ongoing billing activities until it is formally closed.

The Billing Period dataset provides the necessary context to determine the status of each billing period for a specific invoice issuer. Since invoice issuer and [billing period](#term)-related columns are present in all three [FOCUS datasets](#term) (Billing Period, [Cost and Usage](#ds), and [Invoice Detail](#ds)), records across the three datasets can be consistently associated with the corresponding billing cycles.

[Corrections](#term) related to [closed billing periods](#term) (i.e., updates; additions; or omissions of underlying records in [Cost and Usage](#ds), [Invoice Detail](#ds), and Billing Period [FOCUS datasets](#term)) are permitted in accordance with the [Billing Period Status](#col) requirements, as well as the Billed Cost requirements in both [Invoice Detail](#ds) and [Cost and Usage](#ds) datasets. In other words, such [corrections](#term) are typically performed upon explicit request or approval by the customer, provided that they do not compromise the integrity of the [closed billing period](#term).

[Corrections](#term) to underlying records that do not impact the integrity of the [closed billing period](#term) or [invoice reconciliation](#term), such as informational or metadata updates, are allowed regardless of [Billing Period Status](#col).

If the original [closed billing period](#term) is not reopened, corrections that require issuing additional invoices are best represented by associating them with a subsequent [open billing period](#term). This approach preserves historical financial accuracy, ensures clear temporal boundaries between billing cycles, and guarantees that all corrections are transparently tracked and auditable in future periods.
