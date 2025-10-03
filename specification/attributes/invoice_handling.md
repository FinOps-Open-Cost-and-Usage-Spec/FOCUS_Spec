# Invoice Handling

## Overview

FinOps practitioners must be able to reconcile FOCUS dataset artifacts with the corresponding invoices and usage statements they receive from Invoice Issuers. In practice, this means ensuring that all monetary [*charges*](#glossary:charge) that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the [*FOCUS dataset*](#glossary:FOCUS-dataset) artifact. Without this alignment, it becomes difficult to perform accurate [*invoice reconciliation*](#glossary:invoice-reconciliation), financial reporting, and chargeback.

This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset artifact, enabling FOCUS dataset artifacts to be used in a system of record for all invoiced costs.

### Invoice Reconciliation and Issuance

Prior to invoice issuance, all charges in the FOCUS Cost and Usage dataset artifacts that are associated with the invoice must be reconciled with the metrics and dimensions presented on the invoice. This reconciliation ensures alignment between invoice content and the underlying cost and usage data.

Invoice data is typically derived through aggregation of individual cost and usage charges. The aggregation set and the scope of reconciliation are defined by a subset of metrics and dimensions present in the FOCUS cost and usage charges, including but not limited to: BilledCost, BillingCurrency, InvoiceId, InvoiceIssuer, BillingAccountId, BillingPeriodStart, and BillingPeriodEnd. Depending on the Invoice Issuer, reconciliation may also extend to additional metrics and dimensions included on the invoice.

Once an invoice is issued, it becomes the authoritative financial document. Issued invoice is considered finalized, and the cost and usage data it contains must not be altered. While corrections to the underlying cost and usage charges associated with an *issued invoice* (including updates, additions, or omissions) may be permitted, they must not compromise the integrity of the issued invoice. Only corrections that maintain alignment with the invoice content are acceptable. Any misalignment would invalidate the prior *invoice reconciliation* and undermine the invoice's financial validity.

Corrections to the underlying cost and usage charges associated with an issued invoice that do not impact data presented on the invoice are allowed. However, although these corrections do not affect *invoice reconciliation*, they can still result in loss of auditability and traceability, which in turn complicates modifications and mappings required in downstream FinOps activities, such as cost allocation, chargeback, or budgeting. For this reason, such corrections are not preferred and should only be applied when explicitly requested by the end-user.

### Handling Closed Billing Periods

A [*closed billing period*](#glossary:closed-billing-period) represents a billing period for which all planned invoices have been successfully issued by the designated Invoice Issuer. This status indicates that the billing period is financially closed, and no additional invoices will be associated with that timeframe.

Any necessary corrections to previously *closed billing period* that require issuing additional invoices must instead be reflected in a subsequent [*open billing period*](#glossary:open-billing-period), with the charge period indicating when the cost was incurred.

The ability to determine whether a billing period is "open" or "closed" must be documented by the Invoice Issuer and made accessible to practitioners.

This approach establishes a clear temporal boundary between billing cycles, preserving the historical financial accuracy and integrity of closed billing periods while enabling transparent and auditable tracking of corrections in future periods.

Exceptionally, additional invoices may be issued for a closed billing period only if explicitly requested by the end-user.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Indicates how invoice-level *charges*, including those not directly tied to usage, should be represented in a FOCUS Cost and Usage dataset artifacts.

## Requirements

* All costs that appear on any invoice issued to a [*BillingAccountId*](#billingaccountid) MUST be included in the FOCUS Cost and Usage dataset artifacts.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, providers MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the FOCUS Cost and Usage dataset artifacts.
* *Invoice reconciliation* MUST include (but is not limited to) the following metrics and dimensions: BilledCost, BillingCurrency, InvoiceId, InvoiceIssuer, BillingAccountId, BillingPeriodStart, and BillingPeriodEnd.
* *Invoice reconciliation* MUST be performed by the Invoice Issuer before issuing an invoice.
* Cost and usage data presented on an invoice and included in *invoice reconciliation* MUST be documented by the Invoice Issuer and accessible to practitioners.
* Cost and usage data presented on an *issued invoice* MUST NOT be altered.
* Modifications (including updates, additions, or omissions) to the underlying cost and usage charges associated with an *issued invoice* MUST NOT be applied when they affect the cost and usage data presented on the invoice.
* Modifications (including updates, additions, or omissions) to the underlying cost and usage charges associated with an *issued invoice* SHOULD NOT be applied when they do not affect the cost and usage data presented on the invoice.
* Billing period MUST be considered "open" until all planned invoices for that period have been issued.
* Billing period MUST be considered "closed" when all planned invoices for that period have been issued.
* Ability to determine whether a billing period is "open" or "closed" MUST be documented by the Invoice Issuer and accessible to practitioners.
* Additional invoices MUST NOT be associated with a *closed billing period*.

## Exceptions

* Informational line items that have zero monetary impact and are included solely for transparency MAY be excluded. Examples include:
  * Tax exemption notifications
  * SLA credit details when the credit is already applied to the charged amount
* If such informational items are excluded, providers MUST document this in their FOCUS implementation guide and ensure the sum of included charges still equals the invoice total.
* Exceptions to the restrictions on *issued invoices* and *closed billing period* MAY apply in the following cases:
  * Upon explicit request from the end-user (subject to validation and approval processes).
  * Due to technical issues encountered during or after invoice issuance or billing period closure.

## Introduced (version)

1.3
