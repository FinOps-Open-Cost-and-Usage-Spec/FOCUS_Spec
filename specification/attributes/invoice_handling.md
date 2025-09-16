# Invoice Handling

FinOps practitioners must be able to reconcile FOCUS datasets with the corresponding invoices and usage statements they receive from [*Invoice Issuers*](#glossary:InvoiceIssuer). In practice, this means ensuring that all monetary [*charges*](#glossary:charge) that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the [*FOCUS dataset*](#glossary:FOCUS-dataset). Without this alignment, it becomes difficult to perform accurate invoice reconciliation, financial reporting, and chargeback.

This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset, enabling FOCUS datasets to be used in a system of record for all invoiced costs.

Once an invoice is issued, it serves as the authoritative financial document and is considered finalized and immutable. All charge records associated with an issued invoice are also considered finalized and must remain unchanged (i.e., corrections to finalized charge records, whether as updates, deletions or omissions, are not permitted). Furthermore, no additional charge records may be associated with an invoice once it has been issued. This ensures that issued invoices and their underlying charge records remain immutable for financial, auditing, and compliance purposes.

A billing period is considered invoiced (or closed) once all invoices for that period have been issued and all charge records for that period are finalized. After a billing period is invoiced, no new charge records may be associated with it, and all previously finalized charge records remain unchanged. Any necessary corrections to charges originally incurred in an invoiced billing period must instead be reflected in a subsequent open billing period, with the charge period indicating when the cost was incurred. This provides a clear temporal boundary between billing cycles, preserving immutability while still allowing corrections to be tracked transparently in later billing periods.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Indicates how invoice-level *charges*, including those not directly tied to usage, should be represented in a FOCUS Cost and Usage dataset.

## Requirements

* All costs that appear on an invoice MUST be included in the FOCUS Cost and Usage dataset.
* Invoice MUST be considered finalized and immutable once issued.
* Billing period MUST be considered invoiced and closed once all invoices for that period are issued.
* Once the associated invoice is issued, each underlying *charge* adheres to the following additional requirements:
  * *Charge* MUST be considered finalized and immutable.
  * *Charge* MUST NOT be updated, deleted, or omitted.
* Additional *charges* MUST NOT be associated with an invoice once it is issued.
* Additional *charges* MUST NOT be associated with a billing period once it is invoiced and closed.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, providers MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the FOCUS Cost and Usage dataset.

## Exceptions

None

## Introduced (version)

1.3
