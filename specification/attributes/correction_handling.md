# Correction Handling

Correction Handling attribute defines how updates to previously provided charge records are represented in FOCUS datasets.

Although the FOCUS Glossary currently limits the definition of "Correction" to invoiced billing periods, this attribute broadens the scope to encompass all corrections — independent of billing period or invoice status.

This attribute applies to all corrections, whether the original charge was from:

* A previously invoiced and closed billing period
* A prior billing period that is not yet invoiced
* The current billing period

Corrections may arise from a variety of operational or technical causes, such as refunds, late-arriving or delayed cost and usage records, rounding errors or post-processing adjustments, etc.

Correctly modeling corrections is essential for a range of business-critical processes:

* Auditability: Consumers of cost data must be able to trace the full lifecycle of a charge, including the original record and all related corrections.
* Legal and Financial Integrity: Since invoices are binding financial documents, post-invoice corrections must preserve original data and record changes separately.
* Cost Allocation and Chargeback: Corrections must be clearly attributed to the right dimensions (e.g., account, SKU, region) to ensure accurate allocation.
* Temporal Accuracy: The timing of a correction (when it's recorded) may differ from when the charge was incurred — both must be accurately captured.

## Provisioning Styles

To ensure consistent interpretation and correct implementation, it's important to clarify how Correction Handling relates to other foundational concepts such as data delivery styles and invoice finalization.

Data generators typically deliver cost and usage records using one of two models:

* Replacement — Previously delivered records are overwritten with updated versions. This model assumes consumers will discard prior versions and always use the latest available data.
* Append-only — To correct the original, one or more new records are added without modifying existing ones. Corrections are represented by adding new rows, and previously delivered rows remain unchanged.

FOCUS supports both Replacement and Append-only delivery styles for most use cases. However, for corrections to charges originally incurred in previously closed billing periods, only append-only modeling is permitted. This ensures financial integrity and enables accurate audit trails.

There are two standard approaches to modeling corrections in append-only delivery systems supported by FOCUS.

In ledger-style correction, adjustments are modeled by adding one or more records that increment or decrement the cost or usage quantity. These records MUST retain all non-numeric fields (e.g., service, region, usage type) identical to the original. There is no explicit reversal of the original record; only the net effect is reflected. This method reduces data volume but provides limited audit transparency.

In contrast, accounting-style correction uses a two-step representation: the original record is first reversed using a row with negative values for cost and quantity, and then followed by a new record with the corrected values. The reversal MUST match the original in all fields, except for the negated numeric amounts. This model preserves a full correction history and is RECOMMENDED when transparency and traceability are required.

## Invoice Finalization

A billing period is considered closed once all invoices for that period are finalized. After that point, the original invoice and its records must remain immutable. Corrections to such periods must not overwrite existing records and must follow special provisioning rules (see below).

If a correction is applied to a charge from a closed billing period, the corrected record must:

* The correction MUST NOT replace or omitt the original record.
* Be assigned to a different invoice (i.e., not the one originally associated with the charge).
* Have BillingPeriodStart and BillingPeriodEnd values that correspond to the open billing period in which the correction is issued.
* Preserve the original ChargePeriodStart and ChargePeriodEnd values to indicate when the corrected cost was actually incurred.

This dual treatment—distinguishing the charge period from the billing period—allows cost data consumers to understand both the historical intent and the current accounting context for each correction.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how updates to previously provided charge records are represented in FOCUS datasets.

## Requirements

> WORK IN PROGRESS !!!

All corrections/changes to previously provided charge records in FOCUS dataset MUST follow the correction handling requirements listed below.

* Corrections to charges in previously closed billing periods MUST satisfy the following:
  * The correction MUST NOT replace or omit the original record.
  * The corrected row(s) MUST be assigned to a different InvoiceId than the one associated with the original record.
  * The BillingPeriodStart and BillingPeriodEnd MUST reflect the current open billing period in which the correction is being issued.
  * The ChargePeriodStart and ChargePeriodEnd MUST retain the original time interval in which the charge occurred.
  * ChargeClass MUSt be set to "Correction".
* Providers MUST clearly document which provisioning and correction styles are in use (Replacement, Ledger-style, Accounting-style).
* Etc.

## Exceptions

Potential exceptions, to be discussed:

* (TODO) Restatement of Dimensions Not on Original Invoice: Determine whether exceptions will be allowed for corrections that modify only non-invoiced dimensions.
* Technical issues mentioned by Riley.
* Replacment over Append-only explicitly specified by the end-user.

## Introduced (version)

1.3
