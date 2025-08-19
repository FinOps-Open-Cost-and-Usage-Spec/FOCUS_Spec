# Correction Handling

Correction Handling attribute defines how updates to previously provided charge records are represented in FOCUS datasets.

**Terminology Note:** The term "Correction" (uppercase) refers specifically to the allowed value in the Charge Class column, which is limited to corrections for previously invoiced billing periods. In contrast, the Correction Handling attribute covers corrections (lowercase) to previously provided charge records, including those that occurred in previously invoiced, uninvoiced, or current billing periods.

Corrections may arise from a variety of operational or technical causes, such as refunds, delayed or missing usage data, rounding errors, post-processing adjustments, etc.

Accurate correction handling is essential for a range of business-critical processes, including but not limited to:

* Temporal accuracy - capturing both when the charge was incurred (reflected in charge period columns, i.e., Charge Period Start and Charge Period End) and when the correction was invoiced (reflected in billing period columns, i.e., Billing Period Start and Billing Period End columns).
* Financial and legal integrity - preserving original charge records associated with finalized invoices while recording changes to those records separately, as finalized invoices represent binding financial documents requiring immutability and traceability.
* Cost allocation and chargeback - attributing corrections to the correct dimensions (e.g., Billing Account, Sub Account, SKU ID, SKU Price ID, Resource ID).
* Auditability - tracing the full lifecycle of a charge from the original record through all subsequent corrections.

## Provisioning Styles

To ensure consistent interpretation and correct implementation, it is important to clarify how Correction Handling relates to other foundational concepts such as data delivery styles and invoice finalization.

Data generators typically deliver cost and usage records using one of two models:

* Replacement:
  * Previously delivered records are overwritten with updated versions, omitted if obsolete, or supplemented with additional records. This model assumes consumers will discard prior versions and always use the latest available data.
  * Previously delivered records may be overwritten with updated versions, omitted when obsolete, or supplemented with additional records to represent related corrections (e.g., refunds). Multiple records for the same dimensions may coexist, so consumers should handle such cases appropriately. This model does not provide a built-in audit trail; consumers must maintain historical snapshots independently to enable auditability.
* Append-only:
  * To correct the original, one or more new records are added without modifying existing ones. Corrections are represented by adding new rows, and previously delivered rows remain unchanged.
  * Corrections are implemented by adding one or more new records without modifying or deleting any previously delivered records. Duplicate records are explicitly disallowed. All original and correction records are preserved as distinct entries, inherently supporting a built-in audit trail.

FOCUS supports both Replacement and Append-only delivery styles for most use cases. However, for corrections to charges originally incurred in previously invoiced billing periods, only append-only modeling is permitted. This ensures financial integrity and enables accurate audit trails.

There are two standard approaches to modeling corrections in append-only delivery model:

* In ledger-style correction, adjustments are modeled by adding one or more records that increment or decrement the cost or usage quantity. These records MUST retain all non-numeric fields (e.g., service, region, usage type) identical to the original. There is no explicit reversal of the original record; only the net effect is reflected. This method reduces data volume but provides limited audit transparency.
* In contrast, accounting-style correction uses a two-step representation: the original record is first reversed using a row with negative values for cost and quantity, and then followed by a new record with the corrected values. The reversal MUST match the original in all fields, except for the negated numeric amounts. This model preserves a full correction history and is RECOMMENDED when transparency and traceability are required.

## Invoice Finalization

A billing period is considered closed once all invoices for that period are finalized. After that point, the original invoice and its records must remain immutable. Corrections to such periods must not overwrite existing records and must follow special provisioning rules (see below).

If a correction is applied to a charge from a closed billing period, the corrected record must:

* The correction MUST NOT replace or omit the original record.
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
  * ChargeClass MUST be set to "Correction".
* Providers MUST clearly document which provisioning and correction styles are in use (Replacement, Ledger-style, Accounting-style).
* Etc.

## Exceptions

> WORK IN PROGRESS !!!

Potential exceptions, to be discussed:

* Restatement of Dimensions Not on Original Invoice: Determine whether exceptions will be allowed for corrections that modify only non-invoiced dimensions.
* Technical issues mentioned by Riley.
* Replacment over Append-only explicitly specified by the end-user.

## Introduced (version)

1.3
