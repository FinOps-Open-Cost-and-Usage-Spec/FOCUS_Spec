# Invoice Handling

FinOps practitioners must be able to reconcile FOCUS datasets with the corresponding invoices and usage statements they receive from providers. In practice, this means ensuring that all monetary charges that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the FOCUS dataset. Without this alignment, it becomes difficult to perform accurate invoice reconciliation, financial reporting, and chargeback.

This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge SHOULD be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset, enabling FOCUS to serve as a reliable system of record for all invoiced costs.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Indicates how invoice-level monetary charges, including those not directly tied to usage, should be represented in a FOCUS dataset. 

## Requirements

* All costs that appear on an invoice SHOULD be present in the FOCUS dataset.
* Monetary transactions MAY be expressed as individual rows or as part of aggregated rows, provided they remain distinguishable using existing FOCUS dimensions and metrics.
* ChargeCategory SHOULD be used to differentiate types of non-usage charges (e.g., "Tax", "Credit", "Purchase", "Adjustment").
* If a monetary transaction cannot be expressed using existing FOCUS columns, providers SHOULD include supplemental columns (e.g., x_ChargeSubType) to capture this information.
* The total cost associated with a given Invoice ID in the FOCUS dataset SHOULD match the total cost presented on the associated invoice.

## Exceptions

* Invoice corrections or adjustments applied outside the represented billing period MAY be excluded from the current dataset if they are expected to appear in a subsequent period’s FOCUS dataset.
* Charges withheld due to legal, regulatory, or contractual restrictions MAY be omitted if they cannot be shared within structured billing data. In such cases, the data generator SHOULD document the reason for exclusion and MAY include a redacted or summarized charge entry with explanatory metadata.

## Introduced (version)

1.3