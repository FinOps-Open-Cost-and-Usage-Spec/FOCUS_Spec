# Correction Handling

Correction Handling attribute defines how updates to previously provided charge records are represented in FOCUS datasets.

**Terminology Note:** The term "Correction" (uppercase) refers specifically to the allowed value in the Charge Class column, which is limited to corrections for previously invoiced billing periods. In contrast, the Correction Handling attribute covers corrections (lowercase) to previously provided charge records, including those that occurred in previously invoiced, uninvoiced, or current billing periods.

Corrections may arise from a variety of operational or technical causes, such as refunds, delayed or missing usage data, rounding errors, post-processing adjustments, etc.

Accurate correction handling is essential for a range of business-critical processes, including but not limited to:

* Temporal accuracy - capturing both when the charge was incurred (reflected in charge period columns, i.e., Charge Period Start and Charge Period End) and when the correction was invoiced (reflected in billing period columns, i.e., Billing Period Start and Billing Period End columns).
* Financial and legal integrity - preserving original charge records associated with finalized invoices while recording changes to those records separately, as finalized invoices represent binding financial documents requiring immutability and traceability.
* Cost allocation and chargeback - attributing corrections to the correct dimensions (e.g., Billing Account, Sub Account, SKU ID, SKU Price ID, Resource ID).
* Auditability - tracing the full lifecycle of a charge from the original record through all subsequent corrections.

Once an invoice is issued, it serves as the authoritative financial document and is considered finalized and immutable. All charge records associated with an issued invoice are also considered finalized and must remain unchanged (i.e., corrections to finalized charge records, whether as updates, deletions or omissions, are not permitted). Furthermore, no additional charge records may be associated with an invoice once it has been issued. This ensures that issued invoices and their underlying charge records remain immutable for financial, auditing, and compliance purposes.

A billing period is considered closed once all invoices for that period have been issued and all charge records for that period are finalized. After a billing period is closed, no new charge records may be associated with it, and all previously finalized charge records remain unchanged. Any necessary corrections to charges originally incurred in a closed billing period must instead be reflected in a subsequent open billing period, with the charge period indicating when the cost was incurred. This provides a clear temporal boundary between billing cycles, preserving immutability while still allowing corrections to be tracked transparently in later billing periods.

FOCUS datasets can be delivered using one of two mechanisms - Replacement or sppend-only.

For the Replacement mechanism, the initial and each subsequent dataset for a billing period provide a complete snapshot of cost and usage data collected for that period up to the time of delivery, with each subsequent dataset reflecting any updates, omissions, or additions since the previous one. This mechanism does not provide a built-in audit trail, so historical snapshots must be maintained separately to support traceability.

In the Replacement mechanism, charge records in subsequent datasets are handled as follows:

* Unchanged charge records – carried over unchanged from the previously delivered dataset.
* Updated charge records – overwritten with the latest values.
* Additional charge records – new entries representing either billing period segments not previously reported, or supplements to segments included in the previously delivered dataset (e.g., refunds or delayed cost and usage data).
* Omitted charge records – removed from the dataset because they are no longer applicable.

In the Append-only mechanism, corrections are represented exclusively by appending one or more new records, while previously delivered records remain unchanged. Duplicate records are explicitly disallowed. This mechanism inherently supports a built-in audit trail, since all original and correction records are retained as distinct entries.

When the Append-only delivery mechanism is used, there are two common styles for modeling corrections:

* In ledger-style correction, corrections are represented by adding one or more records that increment or decrement the cost or usage quantity. These records MUST retain all non-numeric fields (e.g., service, region, usage type) identical to the original. There is no explicit reversal of the original record; only the net effect is reflected. This method reduces data volume but provides limited audit transparency.

* In contrast, accounting-style correction uses a two-step representation: the original record is first reversed using a charge record that matches all fields of the original except for the numeric values, which are inverted, followed by a new record with the corrected values. This model preserves a full correction history and is preferred when transparency and traceability are required.

* In contrast, accounting-style correction uses a two-step representation: the original record is first reversed using a row with negative values for cost and quantity, and then followed by a new record with the corrected values. The reversal MUST match the original in all fields, except for the negated numeric amounts. This model preserves a full correction history and is RECOMMENDED when transparency and traceability are required.

FOCUS supports both Replacement and Append-only cost and usage data delivery mechanisms for most use cases. However, for corrections to charges originally incurred in previously invoiced billing periods, only Append-only delivery mechanism is permitted. This ensures financial integrity and enables accurate audit trails.

All correction charge records adhere to the correction handling requirements listed below.

## Attribute ID

CorrectionHandling

## Attribute Name

Correction Handling

## Description

Defines how updates to previously provided charge records are represented in FOCUS datasets.

## Requirements

> WORK IN PROGRESS !!!

* Corrections to charges in previously closed billing periods adhere to the following additional requirements:
  * The correction MUST NOT replace or omit the original record.
  * The corrected row(s) MUST be assigned to a different InvoiceId than the one associated with the original record.
  * The BillingPeriodStart and BillingPeriodEnd MUST reflect the current open billing period in which the correction is being issued (correspond to the open billing period in which the correction is issued).
  * The ChargePeriodStart and ChargePeriodEnd MUST retain the original time window in which the charge occurred (cost was actually incurred).
  * ChargeClass MUST be set to "Correction".
* Providers MUST clearly document which provisioning and correction styles are in use (Replacement, Ledger-style, Accounting-style).

## Exceptions

> WORK IN PROGRESS !!!

Potential exceptions, to be discussed:

* Restatement of Dimensions Not on Original Invoice: Determine whether exceptions will be allowed for corrections that modify only non-invoiced dimensions.
* Technical issues mentioned by Riley.
* Replacment over Append-only explicitly specified by the end-user.

## Introduced (version)

1.3
