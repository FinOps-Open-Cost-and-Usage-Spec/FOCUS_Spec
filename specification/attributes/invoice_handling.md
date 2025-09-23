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

* All costs that appear on any invoice issued to a [*BillingAccountId*](#billingaccountid) MUST be included in the FOCUS Cost and Usage dataset.
* If an invoice-level *charge* appears on a customer invoice but cannot be expressed using existing FOCUS columns, providers MUST include provider-defined columns (e.g., x_ChargeSubType) to capture the non-FOCUS-defined details needed to support invoice *charges* reconciliation using the FOCUS Cost and Usage dataset.

## Exceptions

* Informational line items that have zero monetary impact and are included solely for transparency MAY be excluded. Examples include:
  * Tax exemption notifications
  * SLA credit details when the credit is already applied to the charged amount
* If such informational items are excluded, providers MUST document this in their FOCUS implementation guide and ensure the sum of included charges still equals the invoice total.

None

## Introduced (version)

1.3
