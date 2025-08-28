# Invoice Handling

FinOps practitioners must be able to reconcile FOCUS datasets with the corresponding invoices and usage statements they receive from [*Invoice Issuers*](#glossary:InvoiceIssuer). In practice, this means ensuring that all monetary [*charges*](#glossary:charge) that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the [*FOCUS dataset*](#glossary:FOCUS-dataset). Without this alignment, it becomes difficult to perform accurate invoice reconciliation, financial reporting, and chargeback.

This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset, enabling FOCUS datasets to be used in a system of record for all invoiced costs.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Indicates how invoice-level *charges*, including those not directly tied to usage, should be represented in a FOCUS dataset. 

## Requirements

* All costs that appear on an invoice SHOULD be present in the *FOCUS dataset*.
* Invoice-level charges MAY be expressed as individual rows or as part of aggregated rows, provided they remain distinguishable and use or closely align with the FOCUS schema.
* If an invoice-level transaction appears on a customer’s invoice but cannot be fully represented using existing FOCUS columns, providers SHOULD include supplemental columns (e.g., x_ChargeSubType) to ensure that the invoice charge is captured in the FOCUS dataset. 


## Exceptions

None

## Introduced (version)

1.3