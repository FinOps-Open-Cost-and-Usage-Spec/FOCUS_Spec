# Invoice Handling

FinOps practitioners must be able to reconcile FOCUS datasets with the corresponding invoices and usage statements they receive from [*Invoice Issuers*](#glossary:InvoiceIssuer). In practice, this means ensuring that all monetary [*charges*](#glossary:charge) that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the [*FOCUS dataset*](#glossary:FOCUS-dataset). Without this alignment, it becomes difficult to perform accurate invoice reconciliation, financial reporting, and chargeback.

This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset, enabling FOCUS datasets to be used in a system of record for all invoiced costs.

Prior to invoice issuance, all charges in FOCUS Cost and Usage dataset artifacts associated with the invoice must be aligned and [*reconciled*](#glossary:invoice-reconciliation) with the financial values presented on the invoice. Once an invoice is issued, it serves as the authoritative financial document and is considered finalized and immutable. Modifications to charges associated with an issued invoice (whether as updates, additions, or omissions) are not permitted if they would change reconciled invoice data. The scope of *invoice reconciliation* includes (but is not limited to) the following metrics and dimensions: BilledCost, BillingCurrency, InvoiceId, InvoiceIssuer, BillingAccountId, BillingPeriodStart, BillingPeriodEnd. Depending on the Invoice Issuer, these restrictions may extend to additional metrics and dimensions included on the invoice. These constraints ensure the integrity of issued invoices and their supporting data for financial, audit, and compliance purposes. Modifications (including updates, additions, or omissions) that do not impact any invoice-presented financial data are allowed but must be applied with care to preserve traceability. This is particularly important for dimensions and metrics used in essential downstream FinOps capabilities subject to financial data, such as chargeback.

For an invoiced (closed) billing period, it is understood that all invoices for that period have been issued, and no new invoices may be associated with it unless explicitly requested by the end-user. The Invoice Issuer must publish in their respective documentation how to identify an invoiced (closed) billing period. Any necessary corrections to charges originally incurred in an invoiced billing period that have financial impact and require issuing additional invoices must instead be reflected in a subsequent open billing period, with the charge period indicating when the cost was incurred. This establishes a clear temporal boundary between billing cycles, preserving the historical accuracy and integrity of closed billing periods, while enabling transparent and auditable tracking of any necessary corrections in subsequent open billing periods.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Indicates how invoice-level *charges*, including those not directly tied to usage, should be represented in a FOCUS Cost and Usage dataset.

## Requirements

* All costs that appear on any invoice issued to a [*BillingAccountId*](#billingaccountid) MUST be included in the FOCUS Cost and Usage dataset.
* Invoice Issuer MUST document all metrics and dimensions presented on the invoice and included in Invoice Reconciliation.
* Invoice Reconciliation MUST include (but is not limited to) the following metrics and dimensions: BilledCost, BillingCurrency, InvoiceId, InvoiceIssuer, BillingAccountId, BillingPeriodStart, BillingPeriodEnd, and ChargeCategory.
* Invoice Issuer MUST perform internal invoice reconciliation before invoice issuance.
* Invoice MUST be considered finalized and immutable once issued.
* Modifications to charges associated with an issued invoice (including updates, additions, deletions, or omissions) MUST NOT be applied if they would impact reconciled invoice data.
* Modifications to charges associated with an issued invoice (including updates, additions, deletions, or omissions) that do not impact reconciled invoice data SHOULD NOT be applied if they affect dimensions and metrics used in downstream FinOps capabilities subject to financial data, such as chargeback, unless explicitly requested by the end-user.
* Invoice Issuer MUST document how to identify an invoiced (closed) billing period.
* Billing period MUST be considered invoiced (closed) only if all invoices for that billing period have been issued.
* Additional invoices MUST NOT be associated with a billing period once it is invoiced and closed, unless explicitly requested by the end-user.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, providers MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the FOCUS Cost and Usage dataset.

## Exceptions

* Informational line items that have zero monetary impact and are included solely for transparency MAY be excluded. Examples include:
  * Tax exemption notifications
  * SLA credit details when the credit is already applied to the charged amount
* If such informational items are excluded, providers MUST document this in their FOCUS implementation guide and ensure the sum of included charges still equals the invoice total.
* Exceptions to the restrictions on issued invoices and invoiced billing periods MAY apply in the following cases:
  * Upon explicit request from the end-user (subject to validation and approval processes).
  * Due to technical issues encountered during or after invoice issuance or billing period closure.

## Introduced (version)

1.3
