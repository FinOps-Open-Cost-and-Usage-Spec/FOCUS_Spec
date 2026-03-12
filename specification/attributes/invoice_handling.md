# Invoice Handling

FinOps practitioners must be able to reconcile FOCUS datasets with the corresponding invoices and usage statements they receive from [*Invoice Issuers*](#glossary:InvoiceIssuer). In practice, this means ensuring that all monetary [*charges*](#glossary:charge) that appear on an invoice or usage statement — including those not tied to metered usage — are represented in the [*FOCUS dataset*](#glossary:FOCUS-dataset). Without this alignment, it becomes difficult to perform accurate invoice reconciliation, financial reporting, and chargeback.

This attribute introduces requirements for how charges such as usage, taxes, credits, refunds, etc, inclusive of support, training, and marketplace transactions, and any other type of charge should be captured and categorized. It also defines expectations around the completeness and consistency of invoice-level totals within the dataset, enabling FOCUS datasets to be used in a system of record for all invoiced costs.

## Attribute ID

InvoiceHandling

## Attribute Name

Invoice Handling

## Description

Indicates how invoice-level *charges*, including those not directly tied to usage, should be represented in a FOCUS Cost and Usage dataset.

## Requirements

Dataset conforming to InvoiceHandling attribute MUST adhere to the following requirements:

* CostAndUsage *FOCUS dataset* MUST account for all monetary line items included on any invoice issued to a BillingAccountId.
* CostAndUsage *FOCUS dataset* MAY omit informational line items with zero monetary impact included on invoice only for transparency (e.g., tax exemption notifications, SLA credit details when the credit is already applied to the charged amount).
* CostAndUsage *FOCUS dataset* MUST include Custom columns (e.g., x_ChargeSubType) needed to support invoice reconciliation when FOCUS columns are not sufficient.

## Introduced (version)

1.3
